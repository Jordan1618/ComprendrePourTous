#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere les guides complets a partir des chapitres.

Les chapitres de "1 - Guides/" sont la source de verite.
Les fichiers de "0 - Guides complets/" sont un artefact : ne jamais les editer
a la main, relancer ce script apres toute modification d'un chapitre.

Usage :  python3 build-guides-complets.py
"""

import os, re, json, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
CHAPITRES = os.path.join(ROOT, "1 - Guides")
COMPLETS = os.path.join(ROOT, "0 - Guides complets")

DOSSIERS = [
    "Cycle et sante feminine",
    "Sante emotionnelle masculine",
    "IST, depistage et prevention",
    "Massage professionnel",
    "Questions et communication",
]

def lire_frontmatter(texte):
    if not texte.startswith("---\n"):
        return {}, texte
    fin = texte.index("\n---", 4)
    bloc = texte[4:fin]
    corps = texte[fin + 4:].lstrip("\n")
    fm = {}
    for ligne in bloc.split("\n"):
        if ":" in ligne:
            cle, val = ligne.split(":", 1)
            fm[cle.strip()] = val.strip().strip('"')
    return fm, corps

def tri_chapitre(nom):
    """01 -> (1,0) ; 02b -> (2,1) ; 10b -> (10,1)"""
    m = re.match(r"(\d+)([a-z]?)", nom)
    return (int(m.group(1)), ord(m.group(2)) - 96 if m.group(2) else 0)

os.makedirs(COMPLETS, exist_ok=True)
aujourdhui = datetime.date.today().isoformat()
resume = []

for dossier in DOSSIERS:
    chemin = os.path.join(CHAPITRES, dossier)

    # preambule : on reprend le README du guide
    fm_readme, corps_readme = lire_frontmatter(
        open(os.path.join(chemin, "README.md"), encoding="utf-8").read())

    fichiers = sorted(
        [f for f in os.listdir(chemin) if f.endswith(".md") and f != "README.md"],
        key=tri_chapitre)

    # le preambule reprend le texte du README, sans son tableau de chapitres
    intro = corps_readme.split("## Chapitres")[0].strip()
    intro = re.sub(r"^# .+\n", "", intro, count=1).strip()
    # retirer le renvoi vers l'integrale : on est deja dedans
    intro = "\n".join(l for l in intro.split("\n")
                      if "existe aussi en un seul fichier" not in l).strip()

    parties = []
    sommaire = []
    total_mots = 0

    for f in fichiers:
        fm, corps = lire_frontmatter(open(os.path.join(chemin, f), encoding="utf-8").read())
        # le H1 du chapitre devient un H2 dans le document complet
        corps = re.sub(r"^# ", "## %s. " % fm["chapitre"], corps, count=1)
        corps = corps.strip()
        parties.append(corps)
        sommaire.append("- **%s.** %s" % (fm["chapitre"], fm["titre"]))
        total_mots += len(corps.split())

    guide = fm_readme["guide"]
    entete = [
        "---",
        'type: "guide-complet"',
        'guide: "%s"' % guide,
        'sujet: "%s"' % fm_readme["sujet"],
        "chapitres: %d" % len(fichiers),
        "mots: %d" % total_mots,
        "verifie_le: %s" % fm_readme["verifie_le"],
        'licence: "CC BY 4.0"',
        'genere: "automatiquement depuis 1 - Guides/%s"' % dossier,
        "genere_le: %s" % aujourdhui,
        "---",
        "",
        "# %s" % guide,
        "",
        "**Version intégrale.** Ce fichier est généré automatiquement à partir des chapitres "
        "de `1 - Guides/%s`. Ne pas l'éditer directement : toute correction doit être faite "
        "dans le chapitre concerné, puis `build-guides-complets.py` relancé." % dossier,
        "",
        "---",
        "",
        intro,
        "",
        "## Sommaire",
        "",
    ]
    entete += ["%s" % s for s in sommaire]
    entete += ["", "---", "", ""]

    contenu = "\n".join(entete) + "\n\n---\n\n".join(parties) + "\n"

    nom = "%s.md" % guide.replace("/", "-")
    open(os.path.join(COMPLETS, nom), "w", encoding="utf-8").write(contenu)
    resume.append((nom, len(fichiers), total_mots))

for nom, n, m in resume:
    print("%-40s %2d chapitres  %6d mots" % (nom, n, m))
print("\nTotal : %d mots" % sum(m for _, _, m in resume))
