#!/usr/bin/env python3
"""
Régénère site/content/ à partir des dossiers sources du dépôt
(1 - Guides, 2 - Notions, 3 - Transversal, README.md, LICENSE.md).

Ce script est le pendant, côté site, de build-guides-complets.py :
site/content/ est un artefact généré, à ne jamais éditer à la main.
"""
import re
import shutil
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE_CONTENT = ROOT / "site" / "content"

REPO_BLOB = "https://github.com/Jordan1618/ComprendrePourTous/blob/main"

# Dossiers sources à publier, avec leur slug de section et leur poids de menu.
SECTIONS = [
    ("1 - Guides", "guides", 10),
    ("0 - Guides complets", "guides-complets", 15),
    ("2 - Notions", "notions", 20),
    ("3 - Transversal", "transversal", 30),
]

# Ordre d'affichage des guides dans le menu (poids croissants).
GUIDE_ORDER = [
    "Cycle et sante feminine",
    "Sante emotionnelle masculine",
    "IST, depistage et prevention",
    "Massage professionnel",
    "Questions et communication",
]

# Ordre d'affichage des fichiers dans "0 - Guides complets".
FULL_GUIDE_ORDER = [
    "Le meilleur de chaque guide",
    "Cycle et santé féminine",
    "Santé émotionnelle masculine",
    "IST, dépistage et prévention",
    "Massage professionnel",
    "Questions et communication",
]

EXCLUDE_FILES = {"MAINTENANCE.md"}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def split_prefix(stem: str):
    """'02b - Le substrat...' -> (weight_key=(2,'b'), 'Le substrat...')"""
    m = re.match(r"^(\d+)([a-z]?)\s*-\s*(.+)$", stem)
    if m:
        num, letter, rest = m.groups()
        return (int(num), letter), rest
    return (0, ""), stem


def parse_front_matter(text: str):
    """Parseur minimal pour le frontmatter YAML plat utilisé dans ce dépôt."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    raw, body = m.groups()
    data = {}
    for line in raw.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        data[key.strip()] = val
    return data, body


def dump_front_matter(data: dict) -> str:
    lines = ["---"]
    for k, v in data.items():
        if isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        else:
            v = str(v).replace('"', '\\"')
            lines.append(f'{k}: "{v}"')
    lines.append("---\n")
    return "\n".join(lines)


def discover():
    """Construit la liste des fichiers à publier + la carte des chemins."""
    entries = []  # list of dict: src(Path), rel_src(Path posix from ROOT), dest(Path), is_index(bool)
    path_map = {}  # posix rel path from ROOT (as used in links) -> hugo ref path (posix, from content/)

    # Page d'accueil
    entries.append({"src": ROOT / "README.md", "dest": SITE_CONTENT / "_index.md", "weight": 0})
    path_map["README.md"] = ""

    for folder_name, section_slug, section_weight in SECTIONS:
        src_section = ROOT / folder_name
        if not src_section.is_dir():
            continue
        dest_section = SITE_CONTENT / section_slug

        subitems = sorted(src_section.iterdir(), key=lambda p: p.name)
        # Sépare sous-dossiers (guides) et fichiers directs (notions, transversal)
        subdirs = [p for p in subitems if p.is_dir()]
        files = [p for p in subitems if p.is_file() and p.suffix == ".md" and p.name not in EXCLUDE_FILES]

        if subdirs:
            entries.append({
                "src": None, "dest": dest_section / "_index.md",
                "title": folder_name.split(" - ", 1)[-1], "weight": section_weight,
                "is_section_stub": True,
            })

        def dir_weight(p: Path):
            try:
                return GUIDE_ORDER.index(p.name)
            except ValueError:
                return 999

        for d in sorted(subdirs, key=dir_weight):
            guide_slug = slugify(d.name)
            dest_guide = dest_section / guide_slug
            readme = d / "README.md"
            if readme.exists():
                dest = dest_guide / "_index.md"
                entries.append({"src": readme, "dest": dest, "weight": section_weight})
                path_map[str(readme.relative_to(ROOT)).replace("\\", "/")] = str(
                    dest.relative_to(SITE_CONTENT)
                ).replace("\\", "/")

            chapters = [
                p for p in d.iterdir()
                if p.is_file() and p.suffix == ".md" and p.name != "README.md"
            ]
            chapters_sorted = sorted(chapters, key=lambda p: split_prefix(p.stem)[0])
            for i, p in enumerate(chapters_sorted):
                _, rest = split_prefix(p.stem)
                dest = dest_guide / f"{slugify(rest)}.md"
                entries.append({"src": p, "dest": dest, "weight": (i + 1) * 10})
                path_map[str(p.relative_to(ROOT)).replace("\\", "/")] = str(
                    dest.relative_to(SITE_CONTENT)
                ).replace("\\", "/")

        # Fichiers directs dans la section (Notions, Transversal)
        readme = src_section / "README.md"
        if readme.exists():
            dest = dest_section / "_index.md"
            entries.append({"src": readme, "dest": dest, "weight": section_weight})
            path_map[str(readme.relative_to(ROOT)).replace("\\", "/")] = str(
                dest.relative_to(SITE_CONTENT)
            ).replace("\\", "/")
        elif not subdirs:
            entries.append({
                "src": None, "dest": dest_section / "_index.md",
                "title": folder_name.split(" - ", 1)[-1], "weight": section_weight,
                "is_section_stub": True,
            })

        def file_weight(p: Path):
            if folder_name == "0 - Guides complets":
                try:
                    return FULL_GUIDE_ORDER.index(p.stem)
                except ValueError:
                    return 999
            return p.name

        direct_files = sorted(
            (p for p in files if p.name != "README.md"), key=file_weight
        )
        for i, p in enumerate(direct_files):
            dest = dest_section / f"{slugify(p.stem)}.md"
            entries.append({"src": p, "dest": dest, "weight": (i + 1) * 10})
            path_map[str(p.relative_to(ROOT)).replace("\\", "/")] = str(
                dest.relative_to(SITE_CONTENT)
            ).replace("\\", "/")

    return entries, path_map


LINK_RE = re.compile(r"\]\(<([^>]+)>\)")


def resolve_link(current_src: Path, target: str, path_map: dict) -> str:
    anchor = ""
    t = target
    if "#" in t:
        t, anchor = t.split("#", 1)
        anchor = "#" + anchor

    if not t.endswith(".md"):
        return None  # pas un lien markdown interne -> laisser tel quel

    target_abs = (current_src.parent / t).resolve()
    try:
        rel = str(target_abs.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return None

    if rel in path_map:
        ref = path_map[rel]
        if ref == "":
            return f"]({{{{< ref \"/\" >}}}}{anchor})"
        return f"]({{{{< ref \"/{ref}\" >}}}}{anchor})"

    # Cible non publiée (ex: 0 - Guides complets, LICENSE.md) -> lien externe GitHub
    from urllib.parse import quote
    return f"]({REPO_BLOB}/{quote(rel)}{anchor})"


def rewrite_links(text: str, current_src: Path, path_map: dict) -> str:
    def repl(m):
        target = m.group(1)
        new = resolve_link(current_src, target, path_map)
        return new if new else m.group(0)

    return LINK_RE.sub(repl, text)


def main():
    if SITE_CONTENT.exists():
        shutil.rmtree(SITE_CONTENT)
    SITE_CONTENT.mkdir(parents=True)

    entries, path_map = discover()

    for e in entries:
        dest: Path = e["dest"]
        dest.parent.mkdir(parents=True, exist_ok=True)

        if e.get("is_section_stub"):
            data = {"title": e["title"], "weight": e["weight"], "bookCollapseSection": True}
            dest.write_text(dump_front_matter(data), encoding="utf-8")
            continue

        src: Path = e["src"]
        raw = src.read_text(encoding="utf-8")
        fm, body = parse_front_matter(raw)

        title = fm.get("titre") or fm.get("guide") or fm.get("type") or src.stem
        if dest.name == "_index.md" and "guide" in fm:
            title = fm["guide"]
        if src == ROOT / "README.md":
            title = "Apollon"

        new_fm = {"title": title, "weight": e["weight"]}
        for k in ("sujet", "angle", "type", "verifie_le", "mis_a_jour_le", "licence", "guide"):
            if k in fm:
                new_fm[k] = fm[k]
        if dest.name == "_index.md" and any(
            d.get("dest") and d["dest"].parent == dest.parent and d["dest"] != dest for d in entries
        ):
            new_fm["bookCollapseSection"] = True

        body = rewrite_links(body, src, path_map)
        dest.write_text(dump_front_matter(new_fm) + body, encoding="utf-8")

    print(f"{len([e for e in entries if e.get('src')])} pages générées dans {SITE_CONTENT}")


if __name__ == "__main__":
    main()
