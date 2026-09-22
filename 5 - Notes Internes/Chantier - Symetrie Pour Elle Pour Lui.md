---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-21
---

# Chantier — Symétrie Pour Elle / Pour Lui

Fichier de suivi, **non publié**, pensé pour qu'une autre session Claude reprenne ce chantier sans accès à cette conversation.

## Demande d'origine, reformulée

Le tableau de comparaison Pour Elle / Pour Lui dans `Ce qu'il faut faire.md` datait d'avant plusieurs sessions d'enrichissement des deux guides et listait 19 cases *à écrire*, dont la plupart correspondaient en réalité à des chapitres déjà rédigés sous un autre titre. Une comparaison réelle, chapitre par chapitre, menée le 21/09/2026 sur l'état actuel des deux guides (35 chapitres Pour Elle, 34 Pour Lui) a réduit la liste à **8 vrais manques**, validés par l'utilisateur avant rédaction.

## Règles à respecter (rappel, détail complet dans `CLAUDE.md` / `MAINTENANCE.md` / skill Faiseur2Guide)

- Chapitre : 1 500 à 3 500 mots.
- Sourçage par sous-partie, lien posé sur l'affirmation, jamais de `(source : ...)` nu, jamais d'URL/DOI fabriqué.
- Témoignage réel si vécu personnel fort — jamais inventé.
- Réciprocité obligatoire avec `4 - Sources/Pour Elle.md` et `4 - Sources/Pour Lui.md` (compléter par ajout, jamais écraser).
- Neutralité de genre du lecteur — sauf pour les chapitres miroir de genre où le genre du sujet fait partie du sujet (le cas ici : chaque chapitre décrit un sexe précis, donc les accords peuvent être genrés en toute légitimité sur le sujet décrit, tout en gardant le lecteur non présupposé quand le guide s'adresse à « toi »).
- Numérotation : ajouter les nouveaux chapitres à la fin de chaque guide (Pour Elle : 36+; Pour Lui : 35+) plutôt que renuméroter tout — pas d'obligation de faire correspondre les numéros entre les deux guides, la table de correspondance existe déjà pour ça.
- Mettre à jour le README de chaque guide (tableau, frontmatter) à la fin.
- Après la dernière modification : `python build-guides-complets.py`, `python build-index.py`, `python build.py`, puis contrôle des liens cassés.

## Les 8 chapitres à écrire

| # | Guide | Titre prévu | Pendant de | Statut |
|---|---|---|---|---|
| 1 | Pour Lui (36) | Troubles et pathologies masculines | Pour Elle 08 | fait (1 544 mots) |
| 2 | Pour Lui (37) | Fertilité, grossesse et paternité | Pour Elle 10-11 | fait (1 294 mots) |
| 3 | Pour Lui (38) | Les pièges de la modernité masculine | Pour Elle 12 | fait (1 345 mots) |
| 4 | Pour Lui (39) | Les peurs masculines, rationnelles ou non | Pour Elle 13 | fait (1 254 mots) |
| 5 | Pour Elle (36) | Le substrat neuro-psychologique féminin | Pour Lui 03 | fait (1 472 mots) |
| 6 | Pour Elle (37) | Le désir féminin dans la durée | Pour Lui 12 | fait (1 472 mots) |
| 7 | Pour Elle (38) | Les reproches récurrents (féminins) | Pour Lui 17 | fait (1 658 mots) |
| 8 | Pour Elle (39) | Le dilemme féminin contemporain | Pour Lui 18 | fait (1 005 mots) |

## Contenu attendu, brièvement (pour ne pas redire ce qui existe déjà)

- **Troubles et pathologies masculines** : pathologies génitales et hormonales masculines (varicocèle, cryptorchidie, hypogonadisme, troubles de la prostate à tout âge, cancer du testicule) — pendant réel de PE08, pas une redite de PL08 (corps masculin général) ni PL06 (dépression).
- **Fertilité, grossesse et paternité** : fertilité masculine, andropause et âge paternel, vécu du futur père pendant la grossesse, paternité en post-partum, dépression paternelle post-partum (réelle et documentée, sous-connue).
- **Pièges de la modernité masculine** : injonctions esthétiques masculines, réseaux sociaux et masculinité, marché du développement personnel masculin (coachs, contenus « alpha »), écrans — pendant de PE12 mais avec un contenu masculin propre, pas une redite.
- **Peurs masculines** : peurs sur le corps, la performance, la santé, la paternité, la place sociale — distinctes de PL23/24 (« ce qui leur fait peur chez les X ») qui traitent la perception croisée, pas les peurs personnelles.
- **Substrat neuro-psychologique féminin** : fondement hormonal/neuro général féminin au-delà du seul cycle menstruel déjà traité en PE02/03 — pendant structurel de PL03.
- **Désir féminin dans la durée** : évolution du désir féminin en couple sur plusieurs années, distinct de PE09 (anatomie/réponse sexuelle) qui ne traite pas la durée.
- **Reproches récurrents féminins** : ce qui est vrai/faux/mal formulé dans les reproches que les femmes adressent le plus souvent — pendant direct de PL17, même structure.
- **Dilemme féminin contemporain** : tensions contemporaines propres aux femmes (charge mentale, injonction à tout réussir, indépendance vs attentes relationnelles) — pendant de PL18, pas une redite de PE12.

## Fichiers concernés

- `1 - Guides/Pour Lui/36...` à `39...` (nouveaux)
- `1 - Guides/Pour Elle/36...` à `39...` (nouveaux)
- `1 - Guides/Pour Lui/README.md`, `1 - Guides/Pour Elle/README.md` (à la fin)
- `4 - Sources/Pour Lui.md`, `4 - Sources/Pour Elle.md` (complétés par ajout)
- `2 - Notions/` : créer une notion si un concept récurrent le justifie (ex. dépression paternelle post-partum, si elle n'existe pas déjà)

**Ne pas toucher** : les chapitres 1-35 (Pour Elle) et 1-34 (Pour Lui) existants.

## État au 21/09/2026 : rédaction terminée

Les 8 chapitres sont rédigés, sourcés par sous-partie, avec le même sérieux méthodologique que le reste du dépôt (aucune statistique fabriquée, gaps signalés explicitement où la recherche n'a rien donné). Finition :
- Pour Lui : 34 → 38 chapitres (65 453 → 71 041 mots). README mis à jour.
- Pour Elle : 35 → 39 chapitres (75 387 → 81 140 mots). README mis à jour.
- `4 - Sources/Pour Lui.md` et `4 - Sources/Pour Elle.md` complétés par ajout (sections dédiées aux nouveaux chapitres), rien écrasé.
- Notion [Mankeeping](<../2 - Notions/Mankeeping.md>) créée ; notion [Dépression du post-partum](<../2 - Notions/Dépression du post-partum.md>) enrichie du volet paternel.
- Pipeline complet relancé, aucun lien cassé propre à ce chantier.
- Le tableau de comparaison dans `Ce qu'il faut faire.md` a été corrigé (il était périmé) avant rédaction.

**Non fait, à reprendre si besoin** : pas encore commité — vérifier `git status` avant tout commit, d'autres sessions peuvent travailler en parallèle sur d'autres guides du dépôt.

## Comment reprendre

Le chantier de rédaction est terminé. Une reprise concernerait uniquement un commit à faire sur demande explicite, ou une éventuelle nouvelle comparaison si l'un des deux guides est à nouveau enrichi unilatéralement.
