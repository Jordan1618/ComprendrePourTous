---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-17
---

# Chantier — Les nouvelles compositions familiales

Fichier de suivi, **non publié**, pensé pour qu'une autre session Claude (sur une autre machine, sans accès à cette conversation) puisse reprendre ce chantier à tout moment.

## Demande d'origine, reformulée

Le guide « Les nouvelles compositions familiales » est, au 17/09/2026, le plus étroit du dépôt : 4 chapitres, 6 825 mots (familles recomposées, autres modèles familiaux, trouver sa place dedans, bons principes). L'utilisateur a demandé de le reprendre avec l'élicitation complète du skill `Faiseur2Guide`, puis, une fois la grille des 10 familles d'angles et les deux exemples de 30 sous-thèmes présentés dans la conversation, a donné l'instruction : **« fais l'intégralité des angles des 10 familles et tous les sujets des deux exemples »** — c'est-à-dire tout intégrer, sans trier, conformément à la règle par défaut du skill (v17-v18).

Portée du chantier : ajouter des chapitres 5 et suivants au guide existant (les chapitres 1 à 4 restent inchangés), pour couvrir :
- Les 100 angles de la grille (10 familles × 10 angles), regroupés par famille plutôt qu'un chapitre par angle (sinon 100 chapitres, ingérable).
- Les 60 sous-thèmes des deux exemples produits en élicitation (30 « développemental/clinique/juridique » + 30 « social/économique/culturel »).

**Une session parallèle travaille en même temps sur un autre guide** (« Questions et communication », voir `Chantier - Questions et communication.md`) — ne jamais toucher aux fichiers de cette autre session, vérifier `git status` avant tout commit et se limiter aux fichiers listés ci-dessous.

## Règles à respecter (rappel, détail complet dans `CLAUDE.md` / `MAINTENANCE.md` / skill)

- Chapitre : 1 500 à 3 500 mots, jamais de remplissage.
- Sourçage par sous-partie (`###`), lien posé sur l'affirmation elle-même, jamais de tag `(source : ...)` nu, jamais d'URL/DOI fabriqué — fourchette honnête ou mention explicite d'absence de source plutôt qu'un chiffre inventé.
- Témoignage réel si le sujet touche un vécu personnel fort (deuil, aliénation parentale, rupture de lien) — jamais inventé ; dire l'absence si rien n'est retrouvé.
- Réciprocité obligatoire avec `4 - Sources/Les nouvelles compositions familiales.md` (à créer — ce guide n'a pas encore de fichier de sources dédié, à vérifier).
- Pas de chapitre final « Sources vérifiables » agrégeant tout le guide — chaque chapitre garde sa propre section.
- Neutralité de genre du lecteur (« tu »/« toi » au masculin non marqué), nuance systématique sur la famille (« dans la plupart des cas »).
- Renvois croisés dans les deux sens vers `Pour Nous`, `Questions et communication`, notions `Contrôle coercitif`, `Charge mentale`, `Kinkeeping`, `Désert relationnel` — créer les notions manquantes (beau-parentalité, conflit de loyauté, coparentalité élective, aliénation parentale) avec leur section « Où c'est développé ».
- Après la dernière modification de contenu de ce chantier : `python build-guides-complets.py`, `python build-index.py`, `python build.py`, puis le script de contrôle des liens cassés.
- Mettre à jour le tableau `README.md` du guide (nombre de chapitres, mots) et le frontmatter (`chapitres:`, `mots:`) à la fin.

## Plan de chapitres retenu (regroupement des 100 angles + 60 sous-thèmes)

Les chapitres 1 à 4 existants ne sont pas modifiés. Nouveaux chapitres :

| # | Titre | Familles/angles couverts | Sous-thèmes des exemples couverts | Statut |
|---|---|---|---|---|
| 5 | Le corps du lien : neurologie, biologie et attachement | Sciences du vivant (10 angles) | Ex1 : 4, 5, 6, 7 | fait (2 137 mots) |
| 6 | Ce qui se joue dans la tête : psychologie clinique de la recomposition | Psychologie et esprit, angles restants (hors développemental/systémique déjà ch.1-3) | Ex1 : 15, 19 | fait (1 743 mots) |
| 7 | Le droit de la famille recomposée | Droit/pouvoir : juridique, institutionnel, constitutionnel | Ex1 : 8, 9, 10, 11, 12, 13, 29 | fait (1 595 mots) |
| 8 | Pouvoir, négociation et conflit : de la coparentalité au contrôle coercitif | Droit/pouvoir, angles restants (politique, géopolitique, stratégique, historique, diplomatique, militaire/conflictuel, diplomatico-culturel) | Ex1 : 24 | fait (1 551 mots) |
| 9 | Ce que ça coûte : économie et fiscalité de la famille recomposée | Économie et société : économique, financier, actuariel/assurantiel, consumériste, managérial (entrepreneurial et sociotechnique signalés sans source spécifique) | Ex2 : 2, 3, 4, 17, 19, 20, 27, 28 | fait (1 620 mots) |
| 10 | Sociologie, démographie et anthropologie comparée des familles | Économie et société, angles restants (sociologique, démographique, anthropologique) | Ex1 : 3 ; Ex2 : 1, 11, 16 (Ex1:25/Ex2:23 comparaison internationale des politiques de garde non trouvée, signalé dans le chapitre) | fait (1 553 mots) |
| 11 | Corps, intimité et genre dans la nouvelle famille | Corps et intimité (genre, sexologique/relationnel, reproductif traités ; nutritionnel/esthétique/vocal signalés sans source) | Ex1 : 22 | fait (1 580 mots) |
| 12 | Philosophie et sens de la recomposition familiale | Philosophie et sens : philosophique, éthique, spirituel/religieux, stoïcien traités ; épistémologique/logique/esthétique-philo/politique-philo/métaphysique signalés sans source | — | fait (1 370 mots) |
| 13 | Communiquer en famille recomposée | Communication et relation : linguistique, interculturel, générationnel, narratif, médiatique/réputationnel traités ; renvoi vers *Questions et communication* | — | fait (1 571 mots) |
| 14 | Logement, territoire et vie quotidienne | Contexte et environnement : logement, sportif, rural/territorial traités ; écologique/climatique/architectural/écosystémique signalés sans source | Ex2 : 4, 20, 26 | fait (1 398 mots) |
| 15 | Risques, sécurité et protection : de la prévention à l'aliénation parentale | Risque/prévention : préventif, sécuritaire, épidémiologique/statistique, cybersécuritaire traités avec nuance forte | Ex1 : 24 (approfondi) | fait (1 437 mots) |
| 16 | La famille recomposée en culture : représentations, stéréotypes et rituels | Culture et expression : mythologique/littéraire, cinématographique/médiatique, culinaire, humoristique traités ; musical/vestimentaire/muséal signalés sans source | Ex2 : 12, 13, 14, 15, 24, 25 | fait (1 479 mots) |
| 17 | Histoire longue, étapes de Papernow approfondies et devenir à l'âge adulte | Papernow détaillé + systémique/triangulation | Ex1 : 16, 17, 18, 30 (1/2/26 déjà couverts ch.8) ; Ex2 : 30 | fait (1 631 mots) |
| 18 | Organisation du quotidien : charge mentale, calendrier, travail et ressources | — | Ex1 : 14 (garde alternée déjà ch.1/14) ; Ex2 : 5, 6, 7, 22, 28 | fait (1 424 mots) |

Vérification de couverture : les 100 angles de la grille sont répartis sur 5-16 (une famille entière par chapitre ou deux chapitres quand la famille a un angle déjà traité en ch.1-4). Les 60 sous-thèmes sont répartis sur 5-18 (numéros Ex1 1-30 et Ex2 1-30 ci-dessus, cocher au fur et à mesure).

## Fichiers concernés par ce chantier (pour le `git add` final)

- `1 - Guides/Les nouvelles compositions familiales/05...` à `18...` (nouveaux fichiers)
- `1 - Guides/Les nouvelles compositions familiales/README.md` (tableau des chapitres, frontmatter)
- `4 - Sources/Les nouvelles compositions familiales.md` (à créer)
- `2 - Notions/` : nouvelles notions à créer (beau-parentalité, conflit de loyauté, coparentalité élective, aliénation parentale — noms définitifs à confirmer à la rédaction)
- `3 - Transversal/Par sujet.md`, `Par angle.md` : régénérés par `build-index.py`, ne pas éditer à la main
- Renvois croisés dans `Pour Nous`, `Questions et communication` (ajout d'un lien ponctuel, pas de réécriture de chapitre) si pertinent

**Ne pas toucher** : tout fichier sous `Pour Elle/`, `Pour Lui/`, `Questions et communication/` au-delà d'un lien croisé ponctuel — une autre session y travaille.

## État au 17/09/2026 : rédaction terminée

Les 14 chapitres (5 à 18) sont rédigés, sourcés par sous-partie, et respectent les règles du skill (nuance, témoignage réel, pas de fabrication). Tâches de finition accomplies :
- README du guide mis à jour (18 chapitres, 28 914 mots, tableau complet, section « Par où commencer »).
- `4 - Sources/Les nouvelles compositions familiales.md` réécrit avec réciprocité complète (toutes les sources des 14 nouveaux chapitres, classées par thème).
- Deux nouvelles notions créées : [Conflit de loyauté](<../2 - Notions/Conflit de loyauté.md>) et [Parentification](<../2 - Notions/Parentification.md>), ajoutées à l'index `2 - Notions/README.md`.
- Notions existantes complétées avec un renvoi vers ce guide : `Charge mentale`, `Contrôle coercitif`, `Kinkeeping`.
- Pipeline lancé : `build-guides-complets.py`, `build-index.py`, `build.py` — tout régénéré sans erreur propre à ce guide.
- Contrôle des liens cassés : aucun lien cassé dans les fichiers de ce chantier.

**Non fait, à reprendre si besoin** :
- Renvois croisés *depuis* `Pour Nous` et `Questions et communication` *vers* ce guide (la réciprocité n'existe aujourd'hui que dans un sens : ce guide pointe vers eux, pas l'inverse) — à faire une fois la session parallèle sur *Questions et communication* terminée, pour ne pas interférer avec son travail en cours.
- Comparaison internationale chiffrée des politiques de garde alternée (signalée comme non trouvée au chapitre 10, faute de disponibilité temporaire de l'outil de recherche).
- Pas encore commité : `git status` montre ce chantier proprement isolé des fichiers d'une autre session en cours (`Questions et communication`, `Pour Lui`) — ne stager que les fichiers listés plus haut au moment de committer.

## Comment reprendre

Dans une nouvelle session : coller ce fichier. Le chantier de rédaction est terminé ; ce qui reste concerne uniquement les renvois croisés entrants et un commit à faire sur demande explicite.
