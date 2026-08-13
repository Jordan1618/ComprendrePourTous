#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenere les deux index transversaux a partir du frontmatter des chapitres.

"3 - Transversal/Par sujet.md" et "3 - Transversal/Par angle.md" sont des
artefacts : ne jamais les editer a la main, relancer ce script apres tout
ajout ou renommage de chapitre.

C'est ce script qui evite l'oubli le plus facile du projet : ajouter un
guide sans le referencer dans les index.

Usage :  python build-index.py
"""

import os
import re
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
GUIDES = os.path.join(ROOT, "1 - Guides")
TRANSVERSAL = os.path.join(ROOT, "3 - Transversal")

# Ordre d'affichage des guides. Un guide absent de cette liste est place
# a la fin plutot que d'etre silencieusement ignore.
ORDRE_GUIDES = [
    "Pour Elle",
    "Pour Lui",
    "Pour Nous",
    "La rencontre",
    "L amour",
    "Les emotions",
    "IST, depistage et prevention",
    "Massage professionnel",
    "Questions et communication",
    "Les nouvelles compositions familiales",
    "Reseaux sociaux",
]

SUJETS = [
    ("corps féminin", "Corps féminin",
     "Ce qui concerne le corps et le fonctionnement féminins. À lire pour se "
     "comprendre soi-même, ou pour comprendre une partenaire."),
    ("corps masculin", "Corps masculin",
     "Ce qui concerne le corps et le fonctionnement masculins. À lire pour se "
     "comprendre soi-même, ou pour comprendre un partenaire."),
    ("commun", "Commun",
     "Ce qui ne dépend ni du sexe ni du genre : la rencontre, l'amour, la vie "
     "à deux, les émotions, la prévention, le toucher, la communication."),
]

ANGLES = [
    ("physiologie", "Physiologie",
     "Comment le corps fonctionne concrètement, mécanisme par mécanisme."),
    ("psychologie", "Psychologie",
     "Comment le fonctionnement mental se construit, et ce qui le fait dérailler."),
    ("prévention", "Prévention",
     "Dépistage, protection, risque réel contre risque perçu."),
    ("relation", "Relation",
     "Ce que ça change concrètement quand on est deux."),
    ("pratique", "Pratique",
     "Quoi faire, concrètement, avec des formulations et des gestes précis."),
    ("repères", "Repères",
     "Chiffres, glossaires, sources, ressources : de quoi vérifier et aller plus loin."),
]


def lire_frontmatter(texte):
    if not texte.startswith("---"):
        return {}, texte
    fin = texte.index("\n---", 3)
    fm = {}
    for ligne in texte[4:fin].split("\n"):
        if ":" in ligne:
            cle, val = ligne.split(":", 1)
            fm[cle.strip()] = val.strip().strip('"')
    return fm, texte[fin + 4:]


def tri_chapitre(nom):
    m = re.match(r"(\d+)([a-z]?)", nom)
    if not m:
        return (999, 0)
    return (int(m.group(1)), ord(m.group(2)) - 96 if m.group(2) else 0)


def collecter():
    """Retourne la liste des chapitres, dans l'ordre des guides puis des numeros."""
    chapitres = []
    dossiers = [d for d in os.listdir(GUIDES)
                if os.path.isdir(os.path.join(GUIDES, d))]
    dossiers.sort(key=lambda d: (ORDRE_GUIDES.index(d)
                                 if d in ORDRE_GUIDES else 999, d))
    for dossier in dossiers:
        chemin = os.path.join(GUIDES, dossier)
        readme = os.path.join(chemin, "README.md")
        titre_guide = dossier
        if os.path.exists(readme):
            fm, _ = lire_frontmatter(open(readme, encoding="utf-8").read())
            titre_guide = fm.get("guide", dossier)
        fichiers = sorted([f for f in os.listdir(chemin)
                           if f.endswith(".md") and f != "README.md"],
                          key=tri_chapitre)
        for f in fichiers:
            fm, _ = lire_frontmatter(open(os.path.join(chemin, f), encoding="utf-8").read())
            chapitres.append({
                "guide": titre_guide,
                "dossier": dossier,
                "fichier": f,
                "titre": fm.get("titre", os.path.splitext(f)[0]),
                "sujet": fm.get("sujet", "commun"),
                "angle": fm.get("angle", "repères"),
            })
    return chapitres


def lien(c):
    return "[%s](<../1 - Guides/%s/%s>)" % (c["titre"], c["dossier"], c["fichier"])


def ecrire_par_sujet(chapitres, aujourdhui):
    out = ["---", 'type: "index"', 'axe: "sujet"',
           "mis_a_jour_le: %s" % aujourdhui, 'licence: "CC BY 4.0"', "---", "",
           "# Index par sujet", "",
           "Le premier des deux axes de classement de la collection. Chaque chapitre "
           "porte son sujet dans son frontmatter ; cet index est régénéré "
           "automatiquement par `build-index.py` et ne doit pas être édité à la main.",
           ""]
    for cle, titre, desc in SUJETS:
        lot = [c for c in chapitres if c["sujet"] == cle]
        if not lot:
            continue
        out += ["## %s" % titre, "", desc, ""]
        guide_courant = None
        for c in lot:
            if c["guide"] != guide_courant:
                guide_courant = c["guide"]
                out += ["**%s**" % guide_courant, ""]
            out.append("- %s  `%s`" % (lien(c), c["angle"]))
        out.append("")
    out += ["## Comment cet index est tenu", "",
            "Il est régénéré depuis le frontmatter des chapitres. Ajouter un guide "
            "ou un chapitre et relancer `build-index.py` suffit à le mettre à jour : "
            "aucun oubli possible.", "",
            "Retour à [l'accueil de Comprendre pour tous](<../README.md>)."]
    chemin = os.path.join(TRANSVERSAL, "Par sujet.md")
    open(chemin, "w", encoding="utf-8").write("\n".join(out) + "\n")
    return len(chapitres)


def ecrire_par_angle(chapitres, aujourdhui):
    out = ["---", 'type: "index"', 'axe: "angle"',
           "mis_a_jour_le: %s" % aujourdhui, 'licence: "CC BY 4.0"', "---", "",
           "# Index par angle", "",
           "Le second axe. Il traverse les guides : un chapitre sur la sexualité "
           "féminine et un chapitre sur la sexualité masculine relèvent du même "
           "angle, et se lisent bien l'un après l'autre. Cet index est régénéré "
           "automatiquement par `build-index.py`.",
           ""]
    connus = {a[0] for a in ANGLES}
    for cle, titre, desc in ANGLES:
        lot = [c for c in chapitres if c["angle"] == cle]
        if not lot:
            continue
        out += ["## %s" % titre, "", desc, ""]
        for c in lot:
            out.append("- %s  `%s` · %s" % (lien(c), c["sujet"], c["guide"]))
        out.append("")
    autres = [c for c in chapitres if c["angle"] not in connus]
    if autres:
        out += ["## Angles non répertoriés", "",
                "Ces chapitres portent un angle absent de la liste officielle. "
                "Soit l'angle est à ajouter, soit le frontmatter est à corriger.", ""]
        for c in autres:
            out.append("- %s  `%s` · %s" % (lien(c), c["angle"], c["guide"]))
        out.append("")
    out += ["Retour à [l'accueil de Comprendre pour tous](<../README.md>)."]
    chemin = os.path.join(TRANSVERSAL, "Par angle.md")
    open(chemin, "w", encoding="utf-8").write("\n".join(out) + "\n")


def main():
    aujourdhui = datetime.date.today().isoformat()
    chapitres = collecter()
    ecrire_par_sujet(chapitres, aujourdhui)
    ecrire_par_angle(chapitres, aujourdhui)

    par_guide = {}
    for c in chapitres:
        par_guide[c["guide"]] = par_guide.get(c["guide"], 0) + 1
    print("%d chapitres indexes dans %d guides" % (len(chapitres), len(par_guide)))
    for g, n in par_guide.items():
        print("   %-32s %2d chapitres" % (g, n))
    inconnus = sorted({c["angle"] for c in chapitres} - {a[0] for a in ANGLES})
    if inconnus:
        print("ATTENTION, angles hors liste :", inconnus)


if __name__ == "__main__":
    main()
