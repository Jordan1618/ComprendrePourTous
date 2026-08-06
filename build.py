#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere le site statique de "Comprendre pour tous" dans _site/.

Aucune dependance : uniquement la bibliotheque standard Python. Le site est
du HTML/CSS/JS statique, servi tel quel par GitHub Pages.

Les fichiers Markdown du depot sont la source de verite. _site/ est un
artefact : ne jamais l'editer a la main, relancer ce script.

Usage :  python build.py
"""

import html as html_mod
import json
import re
import shutil
import unicodedata
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_site"
ASSETS = ROOT / "assets"

REPO = "https://github.com/Jordan1618/ComprendrePourTous"
BLOB = REPO + "/blob/main"
TREE = REPO + "/tree/main"

DOMAIN = "www.comprendrepourtous.fr"
SITE_TITLE = "Comprendre pour tous"
TAGLINE = "Le corps, les émotions et la relation, expliqués pour de vrai."

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]

# Sections publiees : (dossier source, slug d'URL, titre, description)
SECTIONS = [
    ("1 - Guides", "guides", "Les guides",
     "Un guide par sujet, découpé chapitre par chapitre : cycle féminin, "
     "santé émotionnelle masculine, IST, massage, communication."),
    ("2 - Notions", "notions", "Les notions",
     "Des notes courtes par concept — consentement, charge mentale, "
     "alexithymie — avec des liens vers les développements complets."),
    ("3 - Transversal", "transversal", "Transversal",
     "Index par sujet et par angle, glossaire général, sources vérifiées, "
     "et les signaux d'alerte à connaître."),
    ("0 - Guides complets", "guides-complets", "Guides complets",
     "Chaque guide en un seul fichier, pour une lecture d'une traite ou "
     "une impression."),
]

# Ordre d'affichage des guides (les dossiers de "1 - Guides").
GUIDE_ORDER = [
    "Cycle et sante feminine",
    "Sante emotionnelle masculine",
    "IST, depistage et prevention",
    "Massage professionnel",
    "Questions et communication",
]

# Ordre d'affichage des fichiers de "0 - Guides complets".
FULL_GUIDE_ORDER = [
    "Le meilleur de chaque guide",
    "Cycle et santé féminine",
    "Santé émotionnelle masculine",
    "IST, dépistage et prévention",
    "Massage professionnel",
    "Questions et communication",
]

# Fichiers de la racine qui ne sont pas publies comme pages.
SKIP_ROOT = {"README.md", "MAINTENANCE.md"}


# --------------------------------------------------------------------------
# Utilitaires
# --------------------------------------------------------------------------

def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def split_prefix(stem):
    """'02b - Le substrat' -> ((2, 'b'), 'Le substrat')"""
    m = re.match(r"^(\d+)([a-z]?)\s*-\s*(.+)$", stem)
    if m:
        return (int(m.group(1)), m.group(2)), m.group(3)
    return (0, ""), stem


def parse_front_matter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    data = {}
    for line in m.group(1).splitlines():
        if ":" not in line or not line.strip():
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        if len(val) > 1 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        data[key.strip()] = val
    return data, m.group(2)


def format_date(value):
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", str(value).strip())
    if not m:
        return str(value)
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if not 1 <= mo <= 12:
        return str(value)
    return "%d %s %d" % (d, MOIS[mo - 1], y)


def gh_blob(rel_path):
    return BLOB + "/" + quote(str(rel_path).replace("\\", "/"))


def gh_tree(rel_path):
    return TREE + "/" + quote(str(rel_path).replace("\\", "/"))


def esc(text):
    return html_mod.escape(str(text), quote=True)


# --------------------------------------------------------------------------
# Convertisseur Markdown -> HTML (sous-ensemble utilise par le depot)
# --------------------------------------------------------------------------

LIST_RE = re.compile(r"^(\s*)([-*+]|(\d+)\.)\s+(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HR_RE = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
FENCE_RE = re.compile(r"^\s*```+\s*(\S*)\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")
URL_RE = re.compile(r"(?<![\"\w])(https?://[^\s<>\"'\)]+[^\s<>\"'\).,;:])")


class Markdown(object):
    """Convertisseur bloc + inline. resolve_link(target) -> url ou None."""

    def __init__(self, resolve_link=None):
        self.resolve_link = resolve_link or (lambda t: None)
        self.headings = []
        self._ids = {}
        self._stash = []

    # --- inline ---------------------------------------------------------

    def _keep(self, html):
        self._stash.append(html)
        return "\x00%d\x00" % (len(self._stash) - 1)

    def _link(self, label, target):
        target = target.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        url = self.resolve_link(target)
        if url is None:
            url = target
        attrs = ""
        if url.startswith("http") and DOMAIN not in url:
            attrs = ' target="_blank" rel="noopener"'
        return self._keep('<a href="%s"%s>%s</a>' % (esc(url), attrs, label))

    def inline(self, text):
        # 1. mettre de cote les portions de code
        def code(m):
            return self._keep("<code>%s</code>" % esc(m.group(1)))
        text = re.sub(r"`([^`\n]+)`", code, text)

        # 2. liens markdown AVANT l'echappement : la forme [x](<chemin>) contient
        #    des chevrons, qui seraient transformes en &lt;/&gt; sinon.
        def mdlink(m):
            label = self._emphasis(html_mod.escape(m.group(1), quote=False))
            return self._link(label, m.group(2))
        text = re.sub(r"\[([^\]]*)\]\(<([^>]*)>\)", mdlink, text)
        text = re.sub(r"\[([^\]]*)\]\(([^)\s]*)\)", mdlink, text)

        # 3. echapper ce qui reste (les portions mises de cote sont a l'abri)
        text = html_mod.escape(text, quote=False)

        # 4. URLs nues restantes
        def auto(m):
            u = m.group(1)
            return self._keep('<a href="%s" target="_blank" rel="noopener">%s</a>'
                              % (esc(u), esc(u)))
        text = URL_RE.sub(auto, text)

        # 5. gras / italique
        text = self._emphasis(text)

        # 6. remettre les portions mises de cote
        for i in range(len(self._stash) - 1, -1, -1):
            text = text.replace("\x00%d\x00" % i, self._stash[i])
        self._stash = []
        return text

    @staticmethod
    def _emphasis(text):
        text = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"(?<!\*)\*(?=\S)([^*]+?)(?<=\S)\*(?!\*)", r"<em>\1</em>", text)
        return text

    # --- identifiants de titres ----------------------------------------

    def heading_id(self, text):
        base = slugify(re.sub(r"[*`\[\]]", "", text)) or "section"
        n = self._ids.get(base, 0)
        self._ids[base] = n + 1
        return base if n == 0 else "%s-%d" % (base, n)

    # --- blocs ----------------------------------------------------------

    def convert(self, text):
        lines = text.replace("\r\n", "\n").split("\n")
        out = []
        i = 0
        while i < len(lines):
            line = lines[i]

            if not line.strip():
                i += 1
                continue

            m = FENCE_RE.match(line)
            if m:
                buf = []
                i += 1
                while i < len(lines) and not FENCE_RE.match(lines[i]):
                    buf.append(lines[i])
                    i += 1
                i += 1
                out.append("<pre><code>%s</code></pre>" % esc("\n".join(buf)))
                continue

            if HR_RE.match(line):
                out.append("<hr>")
                i += 1
                continue

            m = HEADING_RE.match(line)
            if m:
                level = len(m.group(1))
                raw = m.group(2).strip()
                hid = self.heading_id(raw)
                if level in (2, 3):
                    self.headings.append((level, hid, re.sub(r"[*`]", "", raw)))
                out.append(
                    '<h%d id="%s">%s<a class="anchor" href="#%s" '
                    'aria-label="Lien vers cette section">#</a></h%d>'
                    % (level, hid, self.inline(raw), hid, level))
                i += 1
                continue

            if line.lstrip().startswith("|") and i + 1 < len(lines) \
                    and TABLE_SEP_RE.match(lines[i + 1]) and "|" in lines[i + 1]:
                html, i = self._table(lines, i)
                out.append(html)
                continue

            if line.strip().startswith(">"):
                buf = []
                while i < len(lines) and lines[i].strip().startswith(">"):
                    buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                out.append("<blockquote>%s</blockquote>" % self.convert("\n".join(buf)))
                continue

            if LIST_RE.match(line):
                html, i = self._list(lines, i)
                out.append(html)
                continue

            buf = []
            while i < len(lines) and lines[i].strip() \
                    and not HEADING_RE.match(lines[i]) \
                    and not HR_RE.match(lines[i]) \
                    and not LIST_RE.match(lines[i]) \
                    and not FENCE_RE.match(lines[i]) \
                    and not lines[i].strip().startswith(">") \
                    and not lines[i].lstrip().startswith("|"):
                buf.append(lines[i].strip())
                i += 1
            if buf:
                out.append("<p>%s</p>" % self.inline(" ".join(buf)))
        return "\n".join(out)

    def _table(self, lines, i):
        def cells(row):
            row = row.strip()
            if row.startswith("|"):
                row = row[1:]
            if row.endswith("|"):
                row = row[:-1]
            return [c.strip() for c in row.split("|")]

        header = cells(lines[i])
        aligns = []
        for spec in cells(lines[i + 1]):
            spec = spec.strip()
            if spec.startswith(":") and spec.endswith(":"):
                aligns.append(" style=\"text-align:center\"")
            elif spec.endswith(":"):
                aligns.append(" style=\"text-align:right\"")
            else:
                aligns.append("")
        i += 2

        rows = []
        while i < len(lines) and lines[i].lstrip().startswith("|"):
            rows.append(cells(lines[i]))
            i += 1

        def align(n):
            return aligns[n] if n < len(aligns) else ""

        html = ["<div class=\"table-wrap\"><table><thead><tr>"]
        for n, c in enumerate(header):
            html.append("<th%s>%s</th>" % (align(n), self.inline(c)))
        html.append("</tr></thead><tbody>")
        for row in rows:
            html.append("<tr>")
            for n, c in enumerate(row):
                html.append("<td%s>%s</td>" % (align(n), self.inline(c)))
            html.append("</tr>")
        html.append("</tbody></table></div>")
        return "".join(html), i

    def _list(self, lines, i):
        items = []
        while i < len(lines):
            m = LIST_RE.match(lines[i])
            if m:
                items.append([len(m.group(1)), m.group(3) is not None, [m.group(4)]])
                i += 1
            elif not lines[i].strip():
                if i + 1 < len(lines) and LIST_RE.match(lines[i + 1]):
                    i += 1
                else:
                    break
            elif lines[i].startswith("  ") and items:
                items[-1][2].append(lines[i].strip())
                i += 1
            else:
                break

        root = []
        stack = [(-1, root)]
        for indent, ordered, content in items:
            while len(stack) > 1 and stack[-1][0] >= indent:
                stack.pop()
            node = {"ordered": ordered, "content": content, "children": []}
            stack[-1][1].append(node)
            stack.append((indent, node["children"]))
        return self._render_list(root), i

    def _render_list(self, nodes):
        if not nodes:
            return ""
        tag = "ol" if nodes[0]["ordered"] else "ul"
        parts = ["<%s>" % tag]
        for n in nodes:
            parts.append("<li>%s%s</li>" % (
                self.inline(" ".join(n["content"])),
                self._render_list(n["children"])))
        parts.append("</%s>" % tag)
        return "".join(parts)


# --------------------------------------------------------------------------
# Decouverte du contenu
# --------------------------------------------------------------------------

class Page(object):
    def __init__(self, src, url, title, section, fm, body,
                 weight=0, parent=None, kind="page"):
        self.src = src            # Path relatif a ROOT, ou None
        self.url = url            # "/guides/x/y/"
        self.title = title
        self.section = section    # slug de section
        self.fm = fm
        self.body = body
        self.weight = weight
        self.parent = parent      # url du parent
        self.kind = kind          # page | guide | section | home
        self.children = []
        self.html = ""
        self.headings = []
        self.text = ""


def discover():
    pages = []
    by_src = {}

    def add(page):
        pages.append(page)
        if page.src:
            by_src[str(page.src).replace("\\", "/")] = page
        return page

    # Accueil
    fm, body = parse_front_matter((ROOT / "README.md").read_text(encoding="utf-8"))
    home = add(Page(Path("README.md"), "/", SITE_TITLE, None, fm, body, kind="home"))

    for si, (folder, slug, title, desc) in enumerate(SECTIONS):
        src_dir = ROOT / folder
        if not src_dir.is_dir():
            continue
        section_url = "/%s/" % slug

        sec_fm, sec_body = {}, ""
        readme = src_dir / "README.md"
        sec_src = None
        if readme.exists():
            sec_fm, sec_body = parse_front_matter(readme.read_text(encoding="utf-8"))
            sec_src = readme.relative_to(ROOT)
        section = add(Page(sec_src, section_url, title, slug, sec_fm, sec_body,
                           weight=si, parent="/", kind="section"))
        section.description = desc
        section.folder = folder

        subdirs = sorted([p for p in src_dir.iterdir() if p.is_dir()],
                         key=lambda p: (GUIDE_ORDER.index(p.name)
                                        if p.name in GUIDE_ORDER else 999, p.name))
        for gi, d in enumerate(subdirs):
            g_readme = d / "README.md"
            g_fm, g_body = ({}, "")
            g_src = None
            if g_readme.exists():
                g_fm, g_body = parse_front_matter(g_readme.read_text(encoding="utf-8"))
                g_src = g_readme.relative_to(ROOT)
            g_title = g_fm.get("guide") or d.name
            guide = add(Page(g_src, "%s%s/" % (section_url, slugify(d.name)),
                             g_title, slug, g_fm, g_body,
                             weight=gi, parent=section_url, kind="guide"))
            guide.folder = str(d.relative_to(ROOT)).replace("\\", "/")
            section.children.append(guide)

            chapters = [p for p in d.iterdir()
                        if p.is_file() and p.suffix == ".md" and p.name != "README.md"]
            chapters.sort(key=lambda p: split_prefix(p.stem)[0])
            for ci, p in enumerate(chapters):
                fm, body = parse_front_matter(p.read_text(encoding="utf-8"))
                _, rest = split_prefix(p.stem)
                title_ = fm.get("titre") or rest
                page = add(Page(p.relative_to(ROOT),
                                "%s%s/" % (guide.url, slugify(rest)),
                                title_, slug, fm, body,
                                weight=ci, parent=guide.url))
                guide.children.append(page)

        files = [p for p in src_dir.iterdir()
                 if p.is_file() and p.suffix == ".md" and p.name != "README.md"]

        def file_key(p):
            if folder == "0 - Guides complets":
                return (FULL_GUIDE_ORDER.index(p.stem)
                        if p.stem in FULL_GUIDE_ORDER else 999, p.stem)
            return (0, p.stem)

        for fi, p in enumerate(sorted(files, key=file_key)):
            fm, body = parse_front_matter(p.read_text(encoding="utf-8"))
            title_ = fm.get("titre") or fm.get("guide") or p.stem
            page = add(Page(p.relative_to(ROOT),
                            "%s%s/" % (section_url, slugify(p.stem)),
                            title_, slug, fm, body,
                            weight=fi, parent=section_url))
            section.children.append(page)

    # Licence
    lic = ROOT / "LICENSE.md"
    if lic.exists():
        fm, body = parse_front_matter(lic.read_text(encoding="utf-8"))
        add(Page(lic.relative_to(ROOT), "/licence/", "Licence", None, fm, body,
                 parent="/", kind="page"))

    return home, pages, by_src


def make_resolver(page, by_src):
    """Resout un lien Markdown relatif vers une URL du site."""
    base = (ROOT / page.src).parent if page.src else ROOT

    def resolve(target):
        if not target or target.startswith(("http://", "https://", "#", "mailto:")):
            return None
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        if not target:
            return anchor or None
        try:
            abs_path = (base / target).resolve()
            rel = abs_path.relative_to(ROOT)
        except (ValueError, OSError):
            return None
        key = str(rel).replace("\\", "/")
        if key in by_src:
            return by_src[key].url + anchor
        if abs_path.is_dir():
            return gh_tree(rel)
        if abs_path.exists():
            return gh_blob(rel)
        return None

    return resolve


# --------------------------------------------------------------------------
# Gabarits HTML
# --------------------------------------------------------------------------

def nav_html(pages, current_url):
    sections = [p for p in pages if p.kind == "section"]
    out = ['<ul class="nav-root">']
    for sec in sorted(sections, key=lambda p: p.weight):
        open_sec = current_url.startswith(sec.url)
        out.append("<li>")
        out.append('<details%s><summary><a href="%s"%s>%s</a></summary>'
                   % (" open" if open_sec else "", sec.url,
                      ' class="active"' if current_url == sec.url else "",
                      esc(sec.title)))
        out.append("<ul>")
        for child in sec.children:
            if child.kind == "guide":
                open_g = current_url.startswith(child.url)
                out.append("<li>")
                out.append('<details%s><summary><a href="%s"%s>%s</a></summary><ul>'
                           % (" open" if open_g else "", child.url,
                              ' class="active"' if current_url == child.url else "",
                              esc(child.title)))
                for leaf in child.children:
                    out.append('<li><a href="%s"%s>%s</a></li>'
                               % (leaf.url,
                                  ' class="active"' if current_url == leaf.url else "",
                                  esc(leaf.title)))
                out.append("</ul></details></li>")
            else:
                out.append('<li><a href="%s"%s>%s</a></li>'
                           % (child.url,
                              ' class="active"' if current_url == child.url else "",
                              esc(child.title)))
        out.append("</ul></details></li>")
    out.append("</ul>")
    return "".join(out)


def layout(title, description, body, nav, current_url, extra_head=""):
    full_title = SITE_TITLE if current_url == "/" else "%s · %s" % (title, SITE_TITLE)
    canonical = "https://%s%s" % (DOMAIN, current_url)
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="%(canonical)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:url" content="%(canonical)s">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#128218;</text></svg>">
<script>try{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t;}catch(e){}</script>
%(extra_head)s
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<input type="checkbox" id="nav-toggle" hidden>
<header class="topbar">
  <label for="nav-toggle" class="burger" aria-label="Menu"><span></span><span></span><span></span></label>
  <a class="brand" href="/"><span class="brand-mark">📚</span><span>%(site)s</span></a>
  <form class="topsearch" action="/recherche/" method="get" role="search">
    <input type="search" name="q" placeholder="Rechercher…" aria-label="Rechercher">
  </form>
  <button class="theme-btn" type="button" aria-label="Changer de thème"></button>
</header>
<div class="shell">
  <label for="nav-toggle" class="scrim"></label>
  <aside class="sidebar"><nav aria-label="Sommaire du site">%(nav)s</nav></aside>
  <main id="contenu">%(body)s</main>
</div>
<footer class="footer">
  <p><strong>%(site)s</strong> — %(tagline)s</p>
  <p>Textes sous licence <a href="https://creativecommons.org/licenses/by/4.0/deed.fr" target="_blank" rel="noopener">CC BY 4.0</a> ·
     <a href="%(repo)s" target="_blank" rel="noopener">Dépôt GitHub</a> ·
     <a href="/licence/">Licence</a></p>
  <p class="disclaimer">Rien ici n'est un avis médical individualisé. Pour toute situation concrète, un professionnel de santé reste irremplaçable.</p>
</footer>
<script src="/assets/app.js" defer></script>
</body>
</html>
""" % {
        "title": esc(full_title),
        "desc": esc(description),
        "canonical": esc(canonical),
        "site": esc(SITE_TITLE),
        "tagline": esc(TAGLINE),
        "repo": REPO,
        "nav": nav,
        "body": body,
        "extra_head": extra_head,
    }


def breadcrumb(page, by_url):
    crumbs = []
    cur = page
    seen = set()
    while cur and cur.parent and cur.parent not in seen:
        seen.add(cur.parent)
        parent = by_url.get(cur.parent)
        if not parent:
            break
        crumbs.append(parent)
        cur = parent
    crumbs.reverse()
    parts = ['<nav class="crumbs" aria-label="Fil d\'ariane">']
    parts.append('<a href="/">Accueil</a>')
    for c in crumbs:
        if c.url == "/":
            continue
        parts.append('<span>/</span><a href="%s">%s</a>' % (c.url, esc(c.title)))
    parts.append('<span>/</span><span class="here">%s</span>' % esc(page.title))
    parts.append("</nav>")
    return "".join(parts)


def meta_bar(page):
    bits = []
    if page.fm.get("sujet"):
        bits.append('<span class="chip">%s</span>' % esc(page.fm["sujet"]))
    if page.fm.get("angle"):
        bits.append('<span class="chip chip-accent">%s</span>' % esc(page.fm["angle"]))
    words = len(page.body.split())
    if words > 200:
        bits.append('<span class="chip chip-ghost">%s mots</span>'
                    % "{:,}".format(words).replace(",", " "))
    date = page.fm.get("verifie_le") or page.fm.get("mis_a_jour_le")
    if date:
        bits.append('<span class="chip chip-ghost">Vérifié le %s</span>'
                    % esc(format_date(date)))
    if not bits:
        return ""
    return '<p class="chips">%s</p>' % "".join(bits)


def toc_html(headings):
    items = [h for h in headings if h[0] in (2, 3)]
    if len(items) < 3:
        return ""
    # certains chapitres n'utilisent que des h3 : on indente relativement au
    # niveau le plus haut present, sinon tout apparait decale pour rien.
    top = min(h[0] for h in items)
    parts = ['<details class="toc" open><summary>Sur cette page</summary><ul>']
    for level, hid, text in items:
        parts.append('<li class="lvl%d"><a href="#%s">%s</a></li>'
                     % (2 + (level - top), hid, esc(text)))
    parts.append("</ul></details>")
    return "".join(parts)


def source_link(page):
    if not page.src:
        return ""
    return ('<p class="source"><a href="%s" target="_blank" rel="noopener">'
            'Voir la source de cette page sur GitHub</a></p>' % gh_blob(page.src))


def prev_next_html(page, by_url):
    parent = by_url.get(page.parent) if page.parent else None
    if not parent:
        return ""
    sibs = parent.children
    if page not in sibs:
        return ""
    idx = sibs.index(page)
    prev = sibs[idx - 1] if idx > 0 else None
    nxt = sibs[idx + 1] if idx + 1 < len(sibs) else None
    if not prev and not nxt:
        return ""
    parts = ['<nav class="pager">']
    if prev:
        parts.append('<a class="pager-prev" href="%s"><span>← Précédent</span><strong>%s</strong></a>'
                     % (prev.url, esc(prev.title)))
    else:
        parts.append("<span></span>")
    if nxt:
        parts.append('<a class="pager-next" href="%s"><span>Suivant →</span><strong>%s</strong></a>'
                     % (nxt.url, esc(nxt.title)))
    parts.append("</nav>")
    return "".join(parts)


# --------------------------------------------------------------------------
# Rendu des pages
# --------------------------------------------------------------------------

def write(url, html):
    path = OUT / url.strip("/") / "index.html" if url != "/" else OUT / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def excerpt(text, n=180):
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).strip()
    return text[:n].rstrip() + ("…" if len(text) > n else "")


def render_home(home, pages, by_url, nav):
    sections = sorted([p for p in pages if p.kind == "section"], key=lambda p: p.weight)
    # on ne compte que les chapitres des guides : les notions, les pages
    # transversales et les guides complets ne sont pas des chapitres.
    chapter_pages = [p for p in pages if p.kind == "page" and p.section == "guides"]
    chapters = len(chapter_pages)
    words = sum(len(p.body.split()) for p in chapter_pages)
    guides = len([p for p in pages if p.kind == "guide"])

    cards = []
    for sec in sections:
        count = len(sec.children)
        label = "guides" if sec.section == "guides" else "pages"
        cards.append(
            '<a class="card" href="%s"><h2>%s</h2><p>%s</p>'
            '<span class="card-meta">%d %s</span></a>'
            % (sec.url, esc(sec.title), esc(sec.description), count, label))

    body = ['<div class="hero">']
    body.append("<h1>%s</h1>" % esc(SITE_TITLE))
    body.append('<p class="lead">%s</p>' % esc(TAGLINE))
    body.append('<form class="hero-search" action="/recherche/" method="get" role="search">'
                '<input type="search" name="q" placeholder="Chercher une notion, un symptôme, un mot…" '
                'aria-label="Rechercher sur le site"><button type="submit">Rechercher</button></form>')
    body.append('<p class="hero-stats">%d guides · %d chapitres · %s mots · sources datées</p>'
                % (guides, chapters, "{:,}".format(words).replace(",", " ")))
    body.append("</div>")
    body.append('<div class="cards">%s</div>' % "".join(cards))
    body.append('<div class="prose home-prose">%s</div>' % home.html)
    body.append(source_link(home))

    return layout(SITE_TITLE, TAGLINE, "".join(body), nav, "/")


def render_section(sec, by_url, nav):
    body = ['<article class="prose">']
    body.append(breadcrumb(sec, by_url))
    body.append("<h1>%s</h1>" % esc(sec.title))
    body.append('<p class="lead">%s</p>' % esc(sec.description))
    if sec.html:
        body.append('<div class="section-intro">%s</div>' % sec.html)

    guides = [c for c in sec.children if c.kind == "guide"]
    leaves = [c for c in sec.children if c.kind != "guide"]

    if guides:
        cards = []
        for g in guides:
            cards.append(
                '<a class="card" href="%s"><h2>%s</h2><p>%s</p>'
                '<span class="card-meta">%d chapitres</span></a>'
                % (g.url, esc(g.title), esc(excerpt(g.html, 150)), len(g.children)))
        body.append('<div class="cards">%s</div>' % "".join(cards))

    if leaves:
        rows = []
        for p in leaves:
            chips = ""
            if p.fm.get("angle"):
                chips = '<span class="chip">%s</span>' % esc(p.fm["angle"])
            rows.append('<li><a href="%s"><strong>%s</strong>%s</a>'
                        '<span class="row-desc">%s</span></li>'
                        % (p.url, esc(p.title), chips, esc(excerpt(p.html, 130))))
        body.append('<ul class="rows">%s</ul>' % "".join(rows))

    body.append('<p class="source"><a href="%s" target="_blank" rel="noopener">'
                'Voir ce dossier sur GitHub</a></p>' % gh_tree(sec.folder))
    body.append("</article>")
    return layout(sec.title, sec.description, "".join(body), nav, sec.url)


def render_guide(guide, by_url, nav):
    body = ['<article class="prose">']
    body.append(breadcrumb(guide, by_url))
    body.append("<h1>%s</h1>" % esc(guide.title))
    body.append(meta_bar(guide))
    if guide.html:
        body.append('<div class="section-intro">%s</div>' % guide.html)
    rows = []
    for n, p in enumerate(guide.children, 1):
        chips = ""
        if p.fm.get("angle"):
            chips = '<span class="chip">%s</span>' % esc(p.fm["angle"])
        rows.append('<li><a href="%s"><span class="num">%d</span>'
                    '<strong>%s</strong>%s</a></li>'
                    % (p.url, n, esc(p.title), chips))
    body.append('<ol class="chapters">%s</ol>' % "".join(rows))
    body.append('<p class="source"><a href="%s" target="_blank" rel="noopener">'
                'Voir ce dossier sur GitHub</a></p>' % gh_tree(guide.folder))
    body.append("</article>")
    return layout(guide.title, excerpt(guide.html) or guide.title,
                  "".join(body), nav, guide.url)


def render_page(page, by_url, nav):
    body = ['<article class="prose">']
    body.append(breadcrumb(page, by_url))
    body.append("<h1>%s</h1>" % esc(page.title))
    body.append(meta_bar(page))
    body.append(toc_html(page.headings))
    body.append(page.html)
    body.append(source_link(page))
    body.append("</article>")
    body.append(prev_next_html(page, by_url))
    return layout(page.title, excerpt(page.html) or page.title,
                  "".join(body), nav, page.url)


def render_search(nav):
    body = ['<article class="prose">']
    body.append('<h1>Rechercher</h1>')
    body.append('<form class="hero-search" id="search-form" role="search">'
                '<input type="search" id="q" name="q" autofocus '
                'placeholder="Un mot, une notion, un symptôme…" aria-label="Rechercher">'
                '<button type="submit">Rechercher</button></form>')
    body.append('<p class="muted" id="search-status">Chargement de l\'index…</p>')
    body.append('<ul class="results" id="results"></ul>')
    body.append("</article>")
    return layout("Rechercher", "Recherche plein texte dans tous les guides.",
                  "".join(body), nav, "/recherche/")


def render_index_az(pages, nav):
    entries = []
    for p in pages:
        if p.kind in ("home",) or not p.section:
            continue
        entries.append(p)
    entries.sort(key=lambda p: unicodedata.normalize("NFKD", p.title.lower()))

    groups = {}
    for p in entries:
        letter = unicodedata.normalize("NFKD", p.title[:1].upper())
        letter = letter.encode("ascii", "ignore").decode("ascii") or "#"
        if not letter.isalpha():
            letter = "#"
        groups.setdefault(letter, []).append(p)

    body = ['<article class="prose">']
    body.append('<h1>Index alphabétique</h1>')
    body.append('<p class="lead">Toutes les pages du site, classées par titre.</p>')
    letters = sorted(groups)
    body.append('<p class="az-jump">%s</p>' % " ".join(
        '<a href="#lettre-%s">%s</a>' % (l, l) for l in letters))
    for l in letters:
        body.append('<h2 id="lettre-%s">%s</h2><ul class="rows">' % (l, l))
        for p in groups[l]:
            body.append('<li><a href="%s"><strong>%s</strong></a>'
                        '<span class="row-desc">%s</span></li>'
                        % (p.url, esc(p.title), esc(p.section or "")))
        body.append("</ul>")
    body.append("</article>")
    return layout("Index alphabétique", "Toutes les pages classées par titre.",
                  "".join(body), nav, "/index-alphabetique/")


def render_404(nav):
    body = ['<article class="prose notfound">']
    body.append("<h1>Page introuvable</h1>")
    body.append("<p>Cette adresse ne correspond à aucune page du site.</p>")
    body.append('<p><a class="btn" href="/">Retour à l\'accueil</a> '
                '<a class="btn btn-ghost" href="/recherche/">Rechercher</a></p>')
    body.append("</article>")
    return layout("Page introuvable", "Page introuvable.", "".join(body), nav, "/404/")


# --------------------------------------------------------------------------
# Construction
# --------------------------------------------------------------------------

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    home, pages, by_src = discover()
    by_url = {p.url: p for p in pages}

    # Conversion Markdown -> HTML avec resolution des liens internes
    for p in pages:
        md = Markdown(make_resolver(p, by_src))
        body = p.body
        # le H1 de tete fait doublon avec le titre affiche par le gabarit
        body = re.sub(r"^\s*#\s+.*?\n", "", body, count=1)
        if p.kind == "home":
            # la table des guides fait doublon avec les cartes de l'accueil
            body = re.sub(r"\n## Les guides\n.*?(?=\n## )", "\n", body, flags=re.DOTALL)
        p.html = md.convert(body)
        p.headings = md.headings
        p.text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", p.html)).strip()

    nav_cache = {}

    def nav_for(url):
        if url not in nav_cache:
            nav_cache[url] = nav_html(pages, url)
        return nav_cache[url]

    write("/", render_home(home, pages, by_url, nav_for("/")))

    for p in pages:
        if p.kind == "section":
            write(p.url, render_section(p, by_url, nav_for(p.url)))
        elif p.kind == "guide":
            write(p.url, render_guide(p, by_url, nav_for(p.url)))
        elif p.kind == "page":
            write(p.url, render_page(p, by_url, nav_for(p.url)))

    write("/recherche/", render_search(nav_for("/recherche/")))
    write("/index-alphabetique/", render_index_az(pages, nav_for("/index-alphabetique/")))
    (OUT / "404.html").write_text(render_404(nav_for("/404/")), encoding="utf-8")

    # Index de recherche (les guides complets dupliquent les chapitres)
    index = []
    for p in pages:
        if p.kind == "home" or p.section == "guides-complets":
            continue
        index.append({
            "t": p.title,
            "u": p.url,
            "s": by_url[p.parent].title if p.parent in by_url and p.parent != "/" else "",
            "x": excerpt(p.html, 160),
            "c": p.text[:4000],
        })
    (OUT / "search-index.json").write_text(
        json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    # Ressources statiques
    dest = OUT / "assets"
    dest.mkdir(parents=True, exist_ok=True)
    for f in ASSETS.iterdir():
        if f.is_file():
            shutil.copy2(f, dest / f.name)

    (OUT / "CNAME").write_text(DOMAIN + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: https://%s/sitemap.xml\n" % DOMAIN,
        encoding="utf-8")

    urls = ["/", "/recherche/", "/index-alphabetique/"] + [
        p.url for p in pages if p.kind in ("section", "guide", "page")]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in sorted(set(urls)):
        sitemap.append("<url><loc>https://%s%s</loc></url>" % (DOMAIN, u))
    sitemap.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")

    n_html = sum(1 for _ in OUT.rglob("index.html"))
    print("%d pages HTML generees dans %s" % (n_html, OUT))
    print("%d entrees dans l'index de recherche" % len(index))


if __name__ == "__main__":
    main()
