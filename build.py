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
    "Pour Elle",
    "Pour Lui",
    "IST, depistage et prevention",
    "Massage professionnel",
    "Questions et communication",
    "La rencontre",
    "L amour",
    "Pour Nous",
]

# Ordre d'affichage des fichiers de "0 - Guides complets".
FULL_GUIDE_ORDER = [
    "Le meilleur de chaque guide",
    "Pour Elle",
    "Pour Lui",
    "IST, dépistage et prévention",
    "Massage professionnel",
    "Questions et communication",
    "La rencontre",
    "L'amour",
    "Pour Nous",
]

# Fichiers de la racine qui ne sont pas publies comme pages.
SKIP_ROOT = {"README.md", "MAINTENANCE.md"}

AUTEUR = "Jordan1618"
LINKEDIN = "https://www.linkedin.com/in/jordan-p-77a697228"

# Teinte HSL par section et par guide. Le CSS derive tout seul l'accent
# clair et l'accent sombre a partir de cette unique valeur, ce qui evite
# de maintenir deux palettes par couleur.
DEFAULT_HUE = 174
SECTION_HUE = {
    "guides": 174,
    "guides-complets": 250,
    "notions": 32,
    "transversal": 292,
}
GUIDE_HUE = {
    "pour-elle": 338,
    "pour-lui": 212,
    "ist-depistage-et-prevention": 265,
    "massage-professionnel": 18,
    "questions-et-communication": 152,
    "la-rencontre": 8,
    "l-amour": 348,
    "pour-nous": 196,
}

# Illustrations : SVG en ligne, decoratifs, qui prennent la teinte de la
# page via currentColor. Aucun fichier image, aucune requete reseau.
ILLOS = {
    "guides": (
        '<path d="M12 62V20c14-6 26-6 48 2v42c-22-8-34-8-48-2Z" fill="currentColor" opacity=".12"/>'
        '<path d="M108 62V20c-14-6-26-6-48 2v42c22-8 34-8 48-2Z" fill="currentColor" opacity=".22"/>'
        '<path d="M12 62V20c14-6 26-6 48 2v42c-22-8-34-8-48-2Zm96 0V20c-14-6-26-6-48 2v42c22-8 34-8 48-2Z"'
        ' fill="none" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round"/>'
        '<path d="M60 22v42" stroke="currentColor" stroke-width="2.5" opacity=".45"/>'
    ),
    "guides-complets": (
        '<rect x="26" y="14" width="68" height="15" rx="4" fill="currentColor" opacity=".3"/>'
        '<rect x="17" y="33" width="86" height="15" rx="4" fill="currentColor" opacity=".19"/>'
        '<rect x="26" y="52" width="68" height="15" rx="4" fill="currentColor" opacity=".12"/>'
        '<rect x="26" y="14" width="68" height="15" rx="4" fill="none" stroke="currentColor" stroke-width="2.5"/>'
        '<rect x="17" y="33" width="86" height="15" rx="4" fill="none" stroke="currentColor" stroke-width="2.5"/>'
    ),
    "notions": (
        '<path d="M27 57 59 25l33 23" fill="none" stroke="currentColor" stroke-width="2.5" opacity=".5"/>'
        '<circle cx="27" cy="57" r="9" fill="currentColor" opacity=".18"/>'
        '<circle cx="59" cy="25" r="11" fill="currentColor" opacity=".3"/>'
        '<circle cx="92" cy="48" r="8" fill="currentColor" opacity=".18"/>'
        '<circle cx="27" cy="57" r="9" fill="none" stroke="currentColor" stroke-width="2.5"/>'
        '<circle cx="59" cy="25" r="11" fill="none" stroke="currentColor" stroke-width="2.5"/>'
        '<circle cx="92" cy="48" r="8" fill="none" stroke="currentColor" stroke-width="2.5"/>'
    ),
    "transversal": (
        '<circle cx="60" cy="40" r="26" fill="currentColor" opacity=".12"/>'
        '<circle cx="60" cy="40" r="26" fill="none" stroke="currentColor" stroke-width="2.5"/>'
        '<path d="M60 12v56M32 40h56" stroke="currentColor" stroke-width="2.5" opacity=".45"/>'
        '<path d="m47 53 11-25 15 11-26 14Z" fill="currentColor" opacity=".55"/>'
    ),
}

ANCHOR_SVG = (
    '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor"'
    ' stroke-width="2.2" stroke-linecap="round" aria-hidden="true">'
    '<path d="M10.5 13.5a4.5 4.5 0 0 0 6.4 0l2.6-2.6a4.5 4.5 0 0 0-6.4-6.4l-1 1"/>'
    '<path d="M13.5 10.5a4.5 4.5 0 0 0-6.4 0l-2.6 2.6a4.5 4.5 0 0 0 6.4 6.4l1-1"/></svg>'
)


# Anciennes URL a rediriger apres le renommage des guides, pour ne pas
# casser les liens deja partages. Prefixe -> nouveau prefixe.
REDIRECTS = {
    "/guides/cycle-et-sante-feminine/": "/guides/pour-elle/",
    "/guides/sante-emotionnelle-masculine/": "/guides/pour-lui/",
    "/guides/durer-et-construire/": "/guides/pour-nous/",
    "/guides-complets/cycle-et-sante-feminine/": "/guides-complets/pour-elle/",
    "/guides-complets/sante-emotionnelle-masculine/": "/guides-complets/pour-lui/",
    "/guides-complets/durer-et-construire/": "/guides-complets/pour-nous/",
}


def redirect_page(target):
    return ("""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>Page déplacée</title><link rel="canonical" href="https://%s%s">
<meta http-equiv="refresh" content="0; url=%s">
<meta name="robots" content="noindex"></head>
<body><p>Cette page a été déplacée. <a href="%s">Continuer</a>.</p>
<script>location.replace(%s);</script></body></html>
""" % (DOMAIN, target, target, target, json.dumps(target)))


def illo(name, cls="illo"):
    shapes = ILLOS.get(name)
    if not shapes:
        return ""
    return ('<svg class="%s" viewBox="0 0 120 80" aria-hidden="true" focusable="false">%s</svg>'
            % (cls, shapes))


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
                    'aria-label="Lien direct vers cette section">%s</a></h%d>'
                    % (level, hid, self.inline(raw), hid, ANCHOR_SVG, level))
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
    hue = DEFAULT_HUE

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
        section.hue = SECTION_HUE.get(slug, DEFAULT_HUE)

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
            g_slug = slugify(d.name)
            guide = add(Page(g_src, "%s%s/" % (section_url, g_slug),
                             g_title, slug, g_fm, g_body,
                             weight=gi, parent=section_url, kind="guide"))
            guide.folder = str(d.relative_to(ROOT)).replace("\\", "/")
            guide.hue = GUIDE_HUE.get(g_slug, section.hue)
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
                page.hue = guide.hue
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
            page.hue = GUIDE_HUE.get(slugify(p.stem), section.hue)
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
    out = ['<a class="nav-home%s" href="/">'
           '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor"'
           ' stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<path d="M3 10.5 12 3l9 7.5"/><path d="M5.5 9.5V20h13V9.5"/></svg>'
           '<span>Accueil</span></a>'
           % (" active" if current_url == "/" else "")]
    out.append('<ul class="nav-root">')
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


def layout(title, description, body, nav, current_url, extra_head="", hue=DEFAULT_HUE):
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
<body style="--hue: %(hue)d">
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
  <p class="footer-brand"><strong>%(site)s</strong> — %(tagline)s</p>
  <p class="footer-author">Tout a été fait par <strong>%(auteur)s</strong>. Vous pouvez me contacter sur
     <a href="%(repo)s" target="_blank" rel="noopener">GitHub</a> ou sur
     <a href="%(linkedin)s" target="_blank" rel="noopener">LinkedIn</a>.</p>
  <nav class="footer-links" aria-label="Liens de bas de page">
    <a href="/licence/">Licence CC BY 4.0</a>
    <a href="/mentions-legales/">Mentions légales</a>
    <a href="/confidentialite/">Confidentialité</a>
    <a href="/index-alphabetique/">Index</a>
    <a href="/recherche/">Rechercher</a>
  </nav>
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
        "auteur": esc(AUTEUR),
        "linkedin": LINKEDIN,
        "hue": hue,
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


def breadcrumb_simple(title):
    return ('<nav class="crumbs" aria-label="Fil d\'ariane"><a href="/">Accueil</a>'
            '<span>/</span><span class="here">%s</span></nav>' % esc(title))


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
            '<a class="card" href="%s" style="--hue: %d">%s<h2>%s</h2><p>%s</p>'
            '<span class="card-meta">%d %s</span></a>'
            % (sec.url, sec.hue, illo(sec.section), esc(sec.title),
               esc(sec.description), count, label))

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
    body.append('<div class="page-head">%s<div><h1>%s</h1>'
                '<p class="lead">%s</p></div></div>'
                % (illo(sec.section, "illo illo-head"), esc(sec.title),
                   esc(sec.description)))
    if sec.html:
        body.append('<div class="section-intro">%s</div>' % sec.html)

    guides = [c for c in sec.children if c.kind == "guide"]
    leaves = [c for c in sec.children if c.kind != "guide"]

    if guides:
        cards = []
        for g in guides:
            cards.append(
                '<a class="card card-guide" href="%s" style="--hue: %d">'
                '<span class="card-dot"></span><h2>%s</h2><p>%s</p>'
                '<span class="card-meta">%d chapitres</span></a>'
                % (g.url, g.hue, esc(g.title), esc(excerpt(g.html, 150)),
                   len(g.children)))
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
    return layout(sec.title, sec.description, "".join(body), nav, sec.url,
                  hue=sec.hue)


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
                  "".join(body), nav, guide.url, hue=guide.hue)


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
                  "".join(body), nav, page.url, hue=page.hue)


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


def render_mentions(nav):
    body = ['<article class="prose legal">']
    body.append(breadcrumb_simple("Mentions légales"))
    body.append("<h1>Mentions légales</h1>")
    body.append("""
<h2>Éditeur du site</h2>
<p>Ce site est édité à titre personnel et non commercial par <strong>%(auteur)s</strong>,
personne physique, qui en assure la rédaction et la publication.</p>
<p>Contact : <a href="%(repo)s/issues" target="_blank" rel="noopener">signaler une erreur ou
écrire via GitHub</a>, ou <a href="%(linkedin)s" target="_blank" rel="noopener">LinkedIn</a>.</p>
<p>Directeur de la publication : %(auteur)s.</p>

<h2>Hébergement</h2>
<p>Le site est hébergé par <strong>GitHub Pages</strong> — GitHub, Inc., 88 Colin P. Kelly Jr.
Street, San Francisco, CA 94107, États-Unis
(<a href="https://github.com" target="_blank" rel="noopener">github.com</a>).</p>
<p>Le nom de domaine est enregistré chez <strong>OVH SAS</strong>, 2 rue Kellermann,
59100 Roubaix, France.</p>

<h2>Propriété intellectuelle et réutilisation</h2>
<p>Les textes sont publiés sous licence
<a href="https://creativecommons.org/licenses/by/4.0/deed.fr" target="_blank" rel="noopener">Creative
Commons Attribution 4.0 International (CC BY 4.0)</a>. Vous pouvez les copier, les modifier, les
traduire et les rediffuser, y compris à des fins commerciales, à condition de citer le projet et
son auteur et d'indiquer si des modifications ont été apportées. Voir la
<a href="/licence/">page de licence</a> pour la mention d'attribution à reprendre.</p>
<p>Le code source du site est consultable
<a href="%(repo)s" target="_blank" rel="noopener">sur GitHub</a>.</p>

<h2>Nature du contenu et responsabilité</h2>
<p>Ce site a une vocation strictement <strong>éducative et informative</strong>. Son auteur n'est
ni médecin, ni psychologue, ni sexologue, et le déclare ouvertement. Les contenus publiés sont des
synthèses sourcées et datées, rédigées avec assistance d'intelligence artificielle puis vérifiées
et relues.</p>
<p><strong>Rien sur ce site ne constitue un avis médical, psychologique ou juridique
individualisé</strong>, ni un diagnostic, ni une prescription. Aucune information lue ici ne
remplace la consultation d'un professionnel qualifié ayant examiné une situation réelle. L'auteur
ne saurait être tenu responsable de l'usage fait de ces informations.</p>
<p>Les données chiffrées portent leur date de vérification. Une donnée peut avoir été mise à jour
par la recherche depuis sa publication.</p>

<h2>En cas d'urgence</h2>
<p><strong>15</strong> (SAMU) pour une urgence médicale. <strong>3114</strong> pour la prévention
du suicide, gratuit, 24 h/24 et 7 j/7, accessible aussi bien à la personne concernée qu'à un
proche inquiet. Voir la page <a href="/transversal/signaux-d-alerte/">signaux d'alerte</a>.</p>

<h2>Liens externes</h2>
<p>Ce site renvoie vers des ressources externes (institutions de santé, associations, publications
scientifiques). Leur contenu n'engage que leurs éditeurs respectifs.</p>

<h2>Signaler une erreur</h2>
<p>Toute erreur signalée est corrigée. C'est la contribution la plus utile qu'un lecteur puisse
apporter : <a href="%(repo)s/issues" target="_blank" rel="noopener">ouvrir un signalement</a>.</p>
""" % {"auteur": esc(AUTEUR), "repo": REPO, "linkedin": LINKEDIN})
    body.append("</article>")
    return layout("Mentions légales",
                  "Éditeur, hébergeur, licence et responsabilité éditoriale du site.",
                  "".join(body), nav, "/mentions-legales/", hue=292)


def render_privacy(nav):
    body = ['<article class="prose legal">']
    body.append(breadcrumb_simple("Confidentialité"))
    body.append("<h1>Confidentialité et données personnelles</h1>")
    body.append("""
<p class="lead">Ce site ne collecte aucune donnée personnelle, n'utilise aucun cookie et
n'embarque aucun outil de mesure d'audience. Le détail ci-dessous explique ce que cela implique
concrètement.</p>

<h2>Aucune collecte, aucun cookie</h2>
<p>Ce site est entièrement <strong>statique</strong> : ce sont des fichiers HTML pré-calculés,
servis tels quels. Il n'y a ni base de données, ni compte utilisateur, ni formulaire de contact,
ni commentaire, ni newsletter.</p>
<ul>
<li><strong>Aucun cookie</strong> n'est déposé, ni technique, ni publicitaire. C'est pourquoi
aucune bannière de consentement ne vous est présentée : il n'y a rien à consentir.</li>
<li><strong>Aucun traceur ni mesure d'audience</strong> : pas de Google Analytics, pas de pixel,
pas de service tiers de statistiques.</li>
<li><strong>Aucune ressource externe</strong> : les styles, le script et les illustrations sont
servis depuis ce domaine. Aucune police ni bibliothèque n'est chargée depuis un serveur tiers,
donc aucun tiers ne voit votre visite.</li>
<li><strong>Aucune publicité</strong>, aucun partage ni revente de données.</li>
</ul>

<h2>Ce qui reste stocké dans votre navigateur</h2>
<p>Une seule information est conservée, <strong>sur votre appareil uniquement</strong> : votre
préférence de thème clair ou sombre, enregistrée dans le stockage local du navigateur
(<code>localStorage</code>) sous la clé <code>theme</code>. Elle n'est jamais transmise, ne permet
aucune identification, et disparaît si vous videz les données du site.</p>

<h2>Journaux techniques de l'hébergeur</h2>
<p>Le site est hébergé par <strong>GitHub Pages</strong>. Comme tout serveur web, GitHub peut
enregistrer des journaux techniques de connexion (adresse IP, date, page demandée, type de
navigateur) à des fins de sécurité et de fonctionnement du service. Ce traitement relève de
GitHub, Inc. en tant que responsable, et non de l'éditeur de ce site, qui n'y a pas accès et n'en
tire aucune statistique.</p>
<p>Voir la
<a href="https://docs.github.com/fr/site-policy/privacy-policies/github-privacy-statement" target="_blank" rel="noopener">déclaration
de confidentialité de GitHub</a> et sa
<a href="https://docs.github.com/fr/pages/getting-started-with-github-pages/what-is-github-pages#data-collection" target="_blank" rel="noopener">note
sur la collecte de données de GitHub Pages</a>.</p>
<p>GitHub, Inc. étant établi aux États-Unis, ces journaux peuvent impliquer un transfert de
données hors de l'Union européenne, encadré par les clauses contractuelles types de la Commission
européenne et le cadre de protection des données UE–États-Unis.</p>

<h2>Vos droits (RGPD)</h2>
<p>Le règlement (UE) 2016/679 vous ouvre des droits d'accès, de rectification, d'effacement,
d'opposition, de limitation et de portabilité sur vos données personnelles.</p>
<p>L'éditeur de ce site <strong>ne détenant aucune donnée personnelle vous concernant</strong>, il
n'a matériellement rien à vous communiquer, rectifier ou effacer. Pour les journaux techniques
mentionnés ci-dessus, ces droits s'exercent auprès de GitHub, Inc.</p>
<p>Pour toute question, vous pouvez écrire via
<a href="%(repo)s/issues" target="_blank" rel="noopener">GitHub</a> ou
<a href="%(linkedin)s" target="_blank" rel="noopener">LinkedIn</a>. Vous avez également le droit
d'introduire une réclamation auprès de la
<a href="https://www.cnil.fr" target="_blank" rel="noopener">CNIL</a>.</p>

<h2>Ce que vous lisez ici ne quitte pas votre appareil</h2>
<p>Ce point mérite d'être dit explicitement, vu les sujets traités sur ce site : santé, sexualité,
santé mentale, dépistage. <strong>Personne, y compris l'auteur, ne peut savoir quelles pages vous
consultez</strong>, combien de temps, ni ce que vous recherchez. La recherche du site s'exécute
entièrement dans votre navigateur : votre requête n'est envoyée à aucun serveur.</p>
<p>Seule réserve, valable pour n'importe quel site : votre fournisseur d'accès et l'hébergeur
voient qu'une connexion a lieu vers ce domaine. Si vous consultez ce site depuis un appareil
partagé, la navigation privée reste la précaution la plus simple.</p>

<h2>Modification de cette page</h2>
<p>Toute évolution de ces pratiques sera publiée ici. L'historique complet des modifications est
consultable <a href="%(repo)s/commits/main" target="_blank" rel="noopener">dans le dépôt</a>.</p>
""" % {"repo": REPO, "linkedin": LINKEDIN})
    body.append("</article>")
    return layout("Confidentialité",
                  "Aucune donnée collectée, aucun cookie, aucun traceur. Détail et droits RGPD.",
                  "".join(body), nav, "/confidentialite/", hue=292)


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
    write("/mentions-legales/", render_mentions(nav_for("/mentions-legales/")))
    write("/confidentialite/", render_privacy(nav_for("/confidentialite/")))
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

    # Redirections des anciennes URL vers les guides renommes.
    n_redir = 0
    for old_prefix, new_prefix in REDIRECTS.items():
        for p in pages:
            if not p.url.startswith(new_prefix):
                continue
            old_url = old_prefix + p.url[len(new_prefix):]
            if old_url in by_url:
                continue
            write(old_url, redirect_page(p.url))
            n_redir += 1
        if new_prefix in by_url and old_prefix not in by_url:
            write(old_prefix, redirect_page(new_prefix))
            n_redir += 1

    (OUT / "CNAME").write_text(DOMAIN + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: https://%s/sitemap.xml\n" % DOMAIN,
        encoding="utf-8")

    urls = ["/", "/recherche/", "/index-alphabetique/",
            "/mentions-legales/", "/confidentialite/"] + [
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
