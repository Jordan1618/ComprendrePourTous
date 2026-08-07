---
type: "interne"
mis_a_jour_le: 2026-08-07
---

# Journal des modifications

Fichier de travail, **non publié**. Le journal détaillé et daté est de toute façon dans l'historique Git ; ce fichier ne garde que les décisions structurantes.

## 7 août 2026

- Pour Elle et Pour Lui renumérotés sur un squelette commun de 26 emplacements. 33 chapitres déplacés, aucun supprimé, URL inchangées.
- Quatre chapitres ajoutés pour combler des déséquilibres : contraception masculine, sexualité masculine sous son versant clinique, dépression et anxiété féminines.
- Section `4 - Sources` réorganisée en une page par guide, triée par thématique.
- 8 notions créées, 54 liens posés depuis les deux guides.
- **Toutes les notes de maintenance sorties du contenu public** vers ce dossier : cadences de révision, listes de ce qui reste à faire, sections « Ajouts du … ». Le contenu publié s'adresse à des lecteurs inconnus, pas au mainteneur.
- Source GitHub Pages basculée sur « GitHub Actions » ; l'ancienne configuration servait la racine du dépôt et cassait le site.

## 6 août 2026

- Hugo remplacé par un générateur maison en Python pur (`build.py`), sans dépendance.
- Guides La rencontre, L'amour, Pour Nous, Les émotions écrits.
- `build-index.py` créé pour régénérer les index transversaux depuis le frontmatter et rendre impossible l'oubli d'un guide.

## Règles retenues

- Rien de ce qui s'adresse au mainteneur ne va dans le contenu publié.
- Pas de section « Ajouts du … » : le site n'est pas un journal.
- Chaque sous-partie doit porter au moins une source scientifique.
- Ne jamais fabriquer une référence, une URL ou un DOI.
