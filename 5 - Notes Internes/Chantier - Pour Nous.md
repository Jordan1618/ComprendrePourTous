---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-18
---

# Chantier — Pour Nous

Fichier de suivi, **non publié**, pensé pour qu'une autre session Claude (sur une autre machine, sans accès à cette conversation) puisse reprendre ce chantier à tout moment.

## Demande d'origine, reformulée

Le guide « Pour Nous » (construction à deux, traverser les étapes de la vie) est, au 18/09/2026, resté à 11 chapitres / ~12 296 mots depuis sa création, alors que plusieurs guides voisins (Les nouvelles compositions familiales, Questions et communication) viennent d'être largement étoffés. L'utilisateur a demandé sa reprise complète. Après l'élicitation dans la conversation (grille des 10 familles, inventaire du dépôt, question de recoupement, deux exemples de 30 sous-thèmes), il a donné l'instruction : **« fais l'intégralité des angles des 10 familles et tous les sujets des deux exemples »**.

Portée : ajouter des chapitres 12 et suivants (les chapitres 1 à 11 existants restent inchangés).

## Règles à respecter (rappel, détail complet dans `CLAUDE.md` / `MAINTENANCE.md` / skill)

- Chapitre : 1 500 à 3 500 mots, jamais de remplissage.
- Sourçage par sous-partie, lien posé sur l'affirmation elle-même, jamais de `(source : ...)` nu, jamais d'URL/DOI fabriqué.
- Témoignage réel si vécu personnel fort (violence conjugale, maladie, deuil, divorce) — jamais inventé ; dire l'absence si rien trouvé.
- Réciprocité obligatoire avec `4 - Sources/Pour Nous.md` (déjà existant, à compléter par ajout, jamais écraser l'existant).
- Pas de chapitre final « Sources vérifiables » agrégeant tout le guide.
- Neutralité de genre du lecteur, nuance systématique sur le couple et la famille.
- Renvois croisés vers `Les nouvelles compositions familiales` (coparentalité, droit de la famille recomposée), `Questions et communication` (formulations), `La rencontre` et `L'amour` (ce qui précède la construction à deux). Notion `Contrôle coercitif` à mobiliser pour le chapitre violence, pas à réexpliquer.
- Après la dernière modification : `python build-guides-complets.py`, `python build-index.py`, `python build.py`, puis contrôle des liens cassés.
- Mettre à jour le tableau `README.md` (chapitres, mots) et le frontmatter à la fin.

## Plan de chapitres retenu (regroupement des 100 angles + 60 sous-thèmes)

Chapitres 1-11 existants non modifiés. Nouveaux chapitres :

| # | Titre | Familles/angles couverts | Sous-thèmes des exemples couverts | Statut |
|---|---|---|---|---|
| 12 | Le corps du lien : neurobiologie et hormones du couple dans la durée | Sciences du vivant (neurologique, hormonal, génétique traités) | Ex1 : 1, 2, 3, 15, 29 | fait (1 554 mots) |
| 13 | Le droit et l'argent du couple : mariage, PACS, fiscalité, succession | Droit (juridique/institutionnel) + Économie (économique/financier/actuariel) | Ex1 : 4, 5, 6, 7, 8, 9, 25 | fait (1 455 mots) |
| 14 | Infidélité, violence et sécurité du couple | Risque/prévention + juridique (renvoi notion Contrôle coercitif) | Ex1 : 13, 21, 22 | fait (1 459 mots) |
| 15 | Ce qui prédit la réussite ou l'échec : 50 ans de recherche | Psychologie, angles restants (comportemental, cognitif, différentiel) | Ex1 : 14, 24, 26, 30 (23 médiation renvoyé au ch.5 existant) | fait (1 411 mots) |
| 16 | Traverser la maladie, le handicap et vieillir ensemble | Corps/intimité (hormonal, sexologique, physiologique traités) | Ex1 : 16, 17, 18, 19, 20 ; Ex2 : 26 | fait (1 451 mots) |
| 17 | Sociologie, anthropologie et histoire du couple | Sociologique, démographique, anthropologique (historique déjà ch.11) | Ex1 : 28 ; Ex2 : 1, 2 | fait (1 390 mots) |
| 18 | Philosophie et sens de l'engagement à deux | Philosophique, existentiel, spirituel/religieux, stoïcien traités ; métaphysique/épistémologique/esthétique/politique-philo signalés sans source | Ex2 : 3, 4 | fait (1 344 mots) |
| 19 | Rituels et communication non dite du couple | Communication : narratif/rituel, non-verbal, humoristique traités | Ex2 : 5, 11, 14, 27 | fait (1 387 mots) |
| 20 | La charge domestique et l'argent de poche : négocier l'équitable | Managérial, sociologique (genre) | Ex1 : 10 ; Ex2 : 6, 10, 12 | fait (1 457 mots) |
| 21 | Le couple vu du dehors : réseaux sociaux, belle-famille, amitiés, télétravail | Médiatique, sociologique, technologique traités | Ex2 : 7, 9, 18, 19, 20 (13 climat/écologique non traité) | fait (1 450 mots) |
| 22 | Enfant, pas enfant : désirs asymétriques et coparentalité au sein du couple | Reproductif, sociologique | Ex2 : 15, 16, 17 | fait (1 415 mots) |
| 23 | Le couple en culture : cinéma, musique, folklore, jeu | Cinématographique/médiatique, musical, ludique, culinaire, folklorique traités | Ex2 : 8, 21, 22, 23, 24 | fait (1 385 mots) |
| 24 | Formes non classiques : distance, non-monogamie, choix de ne pas se marier | Genre/sexologique restants | Ex1 : 27 ; Ex2 : 25 | fait (1 209 mots) |
| 25 | Ce que les couples de longue date en disent, et ce qui reste ouvert | — (clôture) | Ex2 : 30 (28 transmission, 29 deuil d'un tiers signalés comme ouverts, non traités en autonome) | fait (1 034 mots) |

## Fichiers concernés par ce chantier

- `1 - Guides/Pour Nous/12...` à `25...` (nouveaux fichiers)
- `1 - Guides/Pour Nous/README.md` (tableau des chapitres, frontmatter — à la fin)
- `4 - Sources/Pour Nous.md` (complété par ajout)
- `2 - Notions/` : notions à créer si un concept recurrent le justifie (à évaluer en cours de rédaction)
- Renvois croisés ponctuels possibles vers `Les nouvelles compositions familiales`, `Questions et communication`, `La rencontre`, `L'amour` — pas de réécriture de leurs chapitres.

**Ne pas toucher** : chapitres 1-11 existants de ce guide, ni les fichiers d'autres guides au-delà d'un lien croisé ponctuel.

## État au 18/09/2026 : rédaction terminée

Les 14 chapitres (12 à 25) sont rédigés, sourcés par sous-partie, avec nuance systématique et sans fabrication. Finition :
- README mis à jour (25 chapitres, 31 686 mots, tableau complet, « Par où commencer » étoffé).
- `4 - Sources/Pour Nous.md` complété par ajout (six nouvelles sections thématiques), rien écrasé de l'existant.
- Pipeline relancé (`build-guides-complets.py`, `build-index.py`, `build.py`) : aucun lien cassé propre à ce guide.
- Recoupements : renvois explicites vers Les nouvelles compositions familiales (coparentalité), Questions et communication, Réseaux sociaux, La rencontre, L'amour.

**Non fait, à reprendre si besoin** :
- Réciprocité entrante (renvois depuis Réseaux sociaux et La rencontre vers ce guide) — à vérifier une fois ces deux guides stabilisés (une autre session enrichit actuellement La rencontre, passée à 28 chapitres).
- Deux sous-thèmes de l'élicitation restent signalés comme non traités en autonome (transmission aux enfants/entourage, deuil d'un ami commun) — voir chapitre 25, section 25.3.
- Pas encore commité — `git status` à vérifier avant tout commit, plusieurs sessions travaillent en parallèle sur d'autres guides du dépôt.

## Comment reprendre

Le chantier de rédaction est terminé. Une reprise concernerait uniquement la réciprocité entrante ou un commit à faire sur demande explicite.
