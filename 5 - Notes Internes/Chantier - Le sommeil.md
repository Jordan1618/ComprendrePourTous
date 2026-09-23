---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-22
---

# Chantier — Le sommeil (nouveau guide)

Fichier de suivi, **non publié**, pensé pour qu'une autre session Claude reprenne ce chantier sans accès à cette conversation.

## Demande d'origine, reformulée

Nouveau guide sur le sommeil, jamais traité comme sujet à part entière dans le dépôt (seulement des mentions tangentielles dans une quarantaine de chapitres — stress, écrans, post-partum). Élicitation complète déroulée dans la conversation le 22/09/2026 (grille des 10 familles, inventaire confirmant l'absence de doublon, question de recoupement posée et acceptée comme léger, deux exemples de 30 sous-thèmes). Feu vert pour tout intégrer.

**Consigne permanente donnée à cette occasion, valable pour toutes les demandes futures** : le contenu peut se recouper entre chapitres ou guides sans problème, mais les entrées de `4 - Sources/` et les notions de `2 - Notions/` ne doivent jamais être dupliquées — vérifier avant d'ajouter. Voir la mémoire `doublons-contenu-tolere-sources-notions-non`.

## Règles à respecter (rappel, détail complet dans `CLAUDE.md` / `MAINTENANCE.md` / skill Faiseur2Guide)

- Bandeau d'avertissement obligatoire en tête du README (texte exact dans MAINTENANCE.md).
- Chapitre : 1 500 à 3 500 mots.
- Sourçage par sous-partie, lien posé sur l'affirmation, jamais de `(source : ...)` nu, jamais d'URL/DOI fabriqué.
- Témoignage réel si vécu personnel fort (insomnie chronique, apnée non diagnostiquée, privation de sommeil comme contrôle coercitif) — jamais inventé.
- Créer `4 - Sources/Le sommeil.md` dès le premier chapitre, réciprocité obligatoire.
- Vérifier `2 - Notions/README.md` avant de créer une notion — ne jamais dupliquer une notion existante (Charge mentale, Contrôle coercitif, Hypervigilance sont déjà pertinentes et à réutiliser par renvoi plutôt qu'à redire).
- Pas de chapitre final « Sources vérifiables » agrégeant tout le guide.
- Neutralité de genre du lecteur, nuance systématique.
- Renvois croisés vers Les émotions, Pour Elle/Pour Lui, Pour Nous, Réseaux sociaux, Les nouvelles compositions familiales, Contrôle coercitif — pas de réécriture de leurs chapitres.
- Après la dernière modification : `python build-guides-complets.py`, `python build-index.py`, `python build.py`, puis contrôle des liens cassés.
- Ajouter le guide au README racine (tableau `## Les guides`, frontmatter `guides:`).

## Plan de chapitres retenu (fusion des 100 angles + 60 sous-thèmes)

| # | Titre | Familles/angles couverts | Sous-thèmes des exemples couverts | Statut |
|---|---|---|---|---|
| 1 | Ce que le sommeil fait vraiment : cycles, hormones, nettoyage cérébral | Sciences du vivant : neurologique, hormonal, médical, évolutionniste | Ex1 : 1, 12, 13, 14 | fait (1 543 mots) |
| 2 | L'horloge interne : chronotype, décalage horaire, travail posté | Chronobiologique, génétique | Ex1 : 2, 3, 20 | fait (1 312 mots) |
| 3 | Les troubles les plus fréquents : insomnie, apnée, jambes sans repos, narcolepsie | Médical | Ex1 : 5, 6, 7, 8 | fait (1 096 mots) |
| 4 | Le sommeil à chaque âge : nourrisson, enfant, adolescent, senior, grossesse/post-partum | Neurodéveloppemental, différentiel, reproductif | Ex1 : 9, 10, 11, 24 | fait (1 782 mots — fusionné, ex-chapitres 4+5) |
| 5 | Ce qui aide vraiment : TCC-I, hygiène de sommeil, somnifères, mélatonine | Pharmacologique, préventif | Ex1 : 17, 18, 19 | fait (1 030 mots) |
| 6 | Sommeil et corps : poids, immunité, mémoire, accidents | Épidémiologique, statistique | Ex1 : 15, 16, 26 | fait (1 103 mots) |
| 7 | Sommeil et santé mentale, sommeil chez les personnes neuroatypiques | Psychologique, différentiel | Ex1 : 25, 29 | fait (1 139 mots) |
| 8 | Métiers à risque : soignants, travail posté, épigénétique du sommeil | Sociotechnique, épigénétique | Ex1 : 27, 28 | fait (871 mots) |
| 9 | Une histoire longue du sommeil : avant/après l'électricité, sommeil biphasique | Historique | Ex2 : 1, 2 | fait (1 036 mots) |
| 10 | Le sommeil ailleurs : cultures, religions, cosleeping | Culturel/comparatif, spirituel/religieux, anthropologique | Ex2 : 3, 4 | fait (878 mots) |
| 11 | Ce que le manque de sommeil coûte : économie, travail, droit | Économique, juridique | Ex2 : 5, 10, 11, 17 | fait (1 016 mots) |
| 12 | L'industrie du sommeil : matelas connectés, applications, marketing | Consumériste, technologique | Ex2 : 6, 22 | fait (972 mots) |
| 13 | Le sommeil en couple et en famille : lits séparés, charge nocturne, écrans | Relationnel, systémique-familial | Ex2 : 7, 8, 9, 12, 13, 26, 27 | fait (1 222 mots) |
| 14 | Sommeil, précarité, institutions et contrôle coercitif | Sécuritaire, criminologique | Ex2 : 14, 15, 16 | fait (981 mots) |
| 15 | Le sommeil dans l'art, la culture populaire et le folklore | Artistique, cinématographique, mythologique, musical | Ex2 : 18, 19, 20, 21 | fait (904 mots) |
| 16 | Rituels, sport, alimentation : ce qui aide concrètement au coucher | Sportif/performance, nutritionnel | Ex2 : 23, 24, 25, 28, 29, 30 | fait (1 007 mots) |

Philosophie/sens (existentiel, stoïcien, éthique du repos) à intégrer en fil rouge dans les chapitres 1 et 16 plutôt qu'en chapitre séparé — évaluer en cours de rédaction si un chapitre dédié se justifie. Guide révisé à 16 chapitres au total (fusion des ex-chapitres 4 et 5).

## Fichiers concernés

- `1 - Guides/Le sommeil/01...` à `17...` + `README.md`
- `4 - Sources/Le sommeil.md` (nouveau)
- `2 - Notions/` : vérifier avant toute création (voir consigne permanente ci-dessus)
- `README.md` racine : ajouter la ligne du guide au tableau, incrémenter `guides:`
- `3 - Transversal/` régénéré par script, ne pas éditer à la main

## État : chantier terminé (22/09/2026)

Les 16 chapitres sont rédigés (17 900 mots), `4 - Sources/Le sommeil.md` complet avec réciprocité vérifiée, README du guide rempli (tableau des chapitres, frontmatter `chapitres: 16` / `mots: 17900`), guide ajouté au README racine (`## Les guides`, `guides: 12`). Deux notions existantes enrichies avec un renvoi vers ce guide plutôt que dupliquées : `Charge mentale` (13.2) et `Contrôle coercitif` (14.2, avec témoignages réels) ; `Hypervigilance` également enrichie (7.2). `build-guides-complets.py` et `build-index.py` ne listaient pas encore « Le sommeil » dans leurs dossiers codés en dur : les deux scripts ont été corrigés pour l'inclure. Les frontmatters `angle:` ont été recalés sur la taxonomie réelle du site (physiologie/psychologie/prévention/relation/pratique/repères/société), les labels du skill (ex. « chronobiologique, génétique ») n'étant qu'un outil de brainstorming, pas la valeur à publier. Pipeline complet relancé (guides complets, index, site) et contrôle des liens cassés effectué : aucun lien cassé propre à ce guide.

Reste à faire, hors scope de ce chantier : rien d'identifié pour l'instant. Ne pas committer/pousser sans demande explicite.
