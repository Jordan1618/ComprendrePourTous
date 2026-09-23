---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-22
---

# Chantier — Alimentation (nouveau guide)

Fichier de suivi, **non publié**, pensé pour qu'une autre session Claude reprenne ce chantier sans accès à cette conversation.

## Demande d'origine, reformulée

Nouveau guide sur l'alimentation et la nutrition, jamais traité comme sujet à part entière dans le dépôt (35 fichiers avec mention tangentielle seulement — sport, grossesse, alimentation émotionnelle — mais aucun guide ni notion dédiée). Élicitation complète déroulée dans la conversation le 22/09/2026 (grille des 10 familles, inventaire confirmant l'absence de doublon, question de recoupement posée, deux exemples de 30 sous-thèmes chacun : un clinique/pratique, un socioculturel/relationnel). Feu vert pour tout intégrer.

**Règle permanente rappelée à cette occasion** (déjà en mémoire `doublons-contenu-tolere-sources-notions-non`) : le contenu peut se recouper entre chapitres ou guides sans problème, mais les entrées de `4 - Sources/` et les notions de `2 - Notions/` ne doivent jamais être dupliquées — vérifier avant d'ajouter.

## Règles à respecter (rappel, détail complet dans `CLAUDE.md` / `MAINTENANCE.md` / skill Faiseur2Guide)

- Bandeau d'avertissement obligatoire en tête du README (texte exact dans MAINTENANCE.md).
- Chapitre : viser 1 500 à 3 500 mots, accepter 900-1500 si le sujet est réellement plus mince plutôt que de gonfler artificiellement.
- Sourçage par sous-partie, lien posé sur l'affirmation, jamais de `(source : ...)` nu, jamais d'URL/DOI fabriqué.
- Témoignage réel si vécu personnel fort (TCA, précarité alimentaire, grossophobie vécue) — jamais inventé.
- Créer `4 - Sources/Alimentation.md` dès le premier chapitre, réciprocité obligatoire.
- Vérifier `2 - Notions/README.md` avant de créer une notion (aucune notion nutrition existante à ce jour).
- Pas de chapitre final « Sources vérifiables » agrégeant tout le guide.
- Neutralité de genre du lecteur, nuance systématique — en particulier sur poids/corps/grossophobie.
- `angle:` du frontmatter DOIT utiliser la taxonomie réelle du site (physiologie/psychologie/prévention/relation/pratique/repères/société), jamais les labels bruts de la grille des 100 angles (leçon apprise sur le chantier « Le sommeil »).
- Renvois croisés vers Pour Elle, Pour Lui, Pour Nous, Les émotions, Le sommeil, Réseaux sociaux — pas de réécriture de leurs chapitres.
- Après la dernière modification : ajouter "Alimentation" aux listes `DOSSIERS`/`ORDRE_GUIDES` codées en dur dans `build-guides-complets.py` et `build-index.py` (piège déjà rencontré), puis `python build-guides-complets.py`, `python build-index.py`, `python build.py`, puis contrôle des liens cassés.
- Ajouter le guide au README racine (tableau `## Les guides`, frontmatter `guides:`).

## Plan de chapitres retenu (fusion des deux exemples de 30 sous-thèmes)

| # | Titre | Sous-thèmes des exemples couverts | Statut |
|---|---|---|---|
| 1 | Les macronutriments : ce qu'ils font vraiment dans le corps | Ex1 : 1 | fait (1 032 mots) |
| 2 | Micronutriments et carences fréquentes | Ex1 : 2 | fait (897 mots) |
| 3 | Calculer ses besoins : métabolisme, TDEE, et les limites du calcul | Ex1 : 3, 6, 7 | fait (899 mots) |
| 4 | Nutrition selon l'objectif : perte, prise de masse, maintien | Ex1 : 4, 9, 10 | fait (1 102 mots) |
| 5 | Sportif vs sédentaire : deux logiques nutritionnelles | Ex1 : 5, Ex2 : 25 | fait (1 097 mots) |
| 6 | Les régimes populaires passés au crible | Ex1 : 8 | fait (918 mots) |
| 7 | Compléments alimentaires : utilité réelle | Ex1 : 11 | fait (963 mots) |
| 8 | Hydratation, index glycémique, fibres et microbiote | Ex1 : 12, 13, 14 | fait (1 034 mots) |
| 9 | Nutrition et maladies : diabète, cardiovasculaire, obésité | Ex1 : 15, 16, 17 | fait (909 mots) |
| 10 | Troubles du comportement alimentaire : clinique et famille | Ex1 : 18, Ex2 : 15 | fait (1 130 mots) |
| 11 | Allergies, intolérances, végétarisme et véganisme | Ex1 : 19, 23 | fait (881 mots) |
| 12 | Nutrition selon l'âge et la situation (enfant, senior, grossesse) | Ex1 : 20, 21, 22 | fait (1 138 mots) |
| 13 | Lire une étiquette et déjouer le marketing alimentaire | Ex1 : 24, Ex2 : 7 | fait (854 mots) |
| 14 | Outils pratiques : recettes, meal prep, budget, gérer les écarts | Ex1 : 25, 26, 27, 28, Ex2 : 27 | fait (1 150 mots) |
| 15 | Une histoire longue de l'alimentation humaine | Ex2 : 1, 2, 21 | fait (818 mots) |
| 16 | Le repas partagé : anthropologie et sociologie de la table | Ex2 : 3, 4 | fait (822 mots) |
| 17 | Religion, interdits et jeûnes alimentaires | Ex2 : 6 | fait (1 062 mots) |
| 18 | L'industrie agroalimentaire : marketing, lobbying, publicité aux enfants | Ex2 : 7, 8 | fait (848 mots) |
| 19 | Précarité alimentaire, déserts alimentaires, gaspillage | Ex2 : 9, 10 | fait (859 mots) |
| 20 | Écologie et géopolitique de l'alimentation | Ex2 : 11, 12 | fait (888 mots) |
| 21 | Diet culture, grossophobie et réseaux sociaux | Ex2 : 13, 14 | fait (888 mots) |
| 22 | Alimentation émotionnelle et lien intestin-cerveau | Ex2 : 16, 17, Ex1 : 29 | fait (903 mots) |
| 23 | Le couple et la famille à table | Ex2 : 18, 19, 26 | fait (954 mots) |
| 24 | Cuisines du monde et éthique alimentaire | Ex2 : 22, 29 | fait (949 mots) |
| 25 | L'alimentation dans l'art, le folklore et la culture populaire | Ex2 : 23, 24 | fait (1 089 mots) |
| 26 | Sortir de la culpabilité : manger intuitif, cuisiner comme acte de soin | Ex2 : 28, 30 | fait (925 mots) |

26 chapitres au total. Fusionner ou scinder en cours de rédaction si un chapitre s'avère trop mince ou trop chargé (déjà arrivé sur « Le sommeil » : fusion de deux chapitres en un).

## Fichiers concernés

- `1 - Guides/Alimentation/01...` à `26...` + `README.md`
- `4 - Sources/Alimentation.md` (nouveau)
- `2 - Notions/` : vérifier avant toute création
- `README.md` racine : ajouter la ligne du guide au tableau, incrémenter `guides:`
- `build-guides-complets.py` et `build-index.py` : ajouter "Alimentation" aux listes codées en dur
- `3 - Transversal/` régénéré par script, ne pas éditer à la main

## État : chantier terminé (22/09/2026)

Les 26 chapitres sont rédigés (25 009 mots), `4 - Sources/Alimentation.md` complet avec réciprocité vérifiée, README du guide rempli (tableau des chapitres, frontmatter `chapitres: 26` / `mots: 25009`), guide ajouté au README racine (`## Les guides`, `guides: 13`). Aucune notion nouvelle créée (aucune notion nutrition pertinente n'existait, et aucun sujet de ce guide ne justifiait d'en créer une nouvelle plutôt que de renvoyer vers un guide existant). Cross-liens ajoutés vers Pour Elle (grossesse), Le sommeil (alimentation/sommeil), Les émotions (régulation émotionnelle) dans le README, et vers Le sommeil (technoférence) dans le corps du texte. `build-guides-complets.py` et `build-index.py` ont été corrigés dès le départ pour inclure "Alimentation" dans leurs listes codées en dur (piège déjà rencontré et documenté sur le chantier « Le sommeil »). Tous les frontmatters `angle:` utilisent directement la taxonomie du site (physiologie/psychologie/prévention/pratique/relation/repères/société) plutôt que les labels bruts de la grille des 100 angles, cette fois dès la rédaction plutôt qu'en correction a posteriori. Pipeline complet relancé (guides complets, index, site) et contrôle des liens cassés effectué : aucun lien cassé propre à ce guide.

Reste à faire, hors scope de ce chantier : rien d'identifié pour l'instant. Ne pas committer/pousser sans demande explicite.

## Comment reprendre (si chantier repris avant complétion)

Coller ce fichier, reprendre au premier chapitre « à faire ». Marquer chaque chapitre fait avec son nombre de mots avant de passer au suivant. Vérifier `2 - Notions/README.md` avant toute création de notion.
