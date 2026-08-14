---
type: "note-interne"
sujet: "maintenance"
mis_a_jour_le: 2026-08-14
---

# Chantier : refonte des guides transversaux

Document de reprise, pensé pour être lisible par une instance Claude fraîche, sans mémoire de la conversation d'origine, sur n'importe quelle machine ayant ce dépôt cloné.

## La demande d'origine (verbatim, résumée)

L'utilisateur veut reprendre, un par un, les guides "communs" (transversaux, non genrés) du dépôt, avec deux contraintes fermes pour chacun :

1. **2000 mots minimum par chapitre**, existant ou nouveau — jamais de remplissage artificiel pour l'atteindre, mais un vrai approfondissement (plus de sous-parties, plus de mécanismes développés, plus de sources).
2. **Passer par le skill `/Faiseur2Guide`** avant d'écrire quoi que ce soit : présenter la grille complète des 10 familles d'angles (jamais une sélection), présenter les angles déjà présents dans le dépôt, poser la question de recoupement, puis — **avant même que l'angle final soit choisi, présentés ensemble avec la grille** — produire deux exemples indépendants et différents l'un de l'autre, chacun avec 30 sous-thèmes, une "commande finale" et un plan de chapitres, en appliquant le prompt :

   > « En appliquant mes directives d'écriture habituelles, dresse-moi une liste de 30 sous-thèmes profonds et nuancés sur [SUJET] — incluant son histoire, ses mécanismes scientifiques, ses impacts sociopsychologiques et des solutions pratiques —, puis rédige-moi la commande finale parfaite pour générer ce guide ainsi que le plan détaillé pour structurer chaque chapitre. »

   Puis l'utilisateur valide généralement : « intègre les 10 familles et les 60 exemples » — c'est-à-dire ne pas se contenter de piocher, mais représenter l'ensemble des 10 familles et intégrer la totalité des 60 sous-thèmes des deux exemples (via de nouveaux chapitres ou l'approfondissement des chapitres existants), en plus de garder le fond des chapitres déjà existants intact (titres, numérotation, périmètre).

**Important, appris par erreur deux fois dans cette conversation** : ne jamais lancer la rédaction (agent ou autre) avant d'avoir réellement obtenu la validation de l'utilisateur sur les angles — même si la demande initiale semblait déjà assez précise. L'utilisateur a explicitement corrigé ce raccourci à deux reprises. Le skill lui-même (`.claude/skills/Faiseur2Guide/SKILL.md`, v13, section "Après le choix des angles") doit être mis à jour pour présenter la grille ET les deux exemples ensemble, dès le départ, sans attendre un premier tour de validation des angles — c'est ce que l'utilisateur a demandé explicitement à la fin de cette conversation ("Débrouilles toi pour qu'ils apparaissent à chaque fois que je fais le /faiseur2guide"). **Si ce n'est pas encore fait dans le skill au moment de la reprise, le faire en premier.**

## Règles de fond à respecter (rappel, déjà dans `CLAUDE.md` et `MAINTENANCE.md`)

- Sourçage en hyperlien posé sur l'affirmation, jamais de lien inventé, jamais de tag `(source : ...)` nu.
- Chaque chapitre garde sa propre section "## Sources vérifiables" en bas — **aucun chapitre final séparé** qui recenserait toutes les sources du guide (doublon avec `4 - Sources/<Guide>.md`).
- Réciprocité complète avec `4 - Sources/<Guide>.md` après chaque guide traité.
- Régénérer le pipeline après chaque guide : `python build-guides-complets.py`, `python build-index.py`, `python build.py`.
- Vérifier les liens cassés avant de committer :
  ```
  python -c "import pathlib,re; [print('CASSE',f,m.group(1)) for f in pathlib.Path('.').rglob('*.md') for m in re.finditer(r'\]\(<([^>]+)>\)', f.read_text(encoding='utf-8')) if not (f.parent/m.group(1)).resolve().exists()]"
  ```
  (faux positifs connus et acceptés : exemples de syntaxe dans `MAINTENANCE.md`, `CLAUDE.md`, le skill.)
- Mettre à jour `README.md` à la racine (nombre de chapitres et de mots du guide concerné + total du projet) après chaque guide.
- Ajouter une ligne à `5 - Notes Internes/Historique des demandes.md` après chaque demande de l'utilisateur (règle systématique, voir `CLAUDE.md`).
- Après chaque guide terminé, **mettre à jour le tableau ci-dessous dans ce fichier** et committer/pousser.

## État d'avancement, guide par guide

| Guide | Statut | Détail |
|---|---|---|
| Questions et communication | ✅ Fini | 23 chapitres, ~21 200 mots (fait avant l'instauration de la règle des 2000 mots/chapitre stricte — chapitres à 800-1300 mots, pas repris depuis). |
| Les émotions | 🔄 En cours au moment de la rédaction de cette note | 18 chapitres visés (10 existants approfondis à 2000+ mots + 8 nouveaux : histoire, cultures, art/musique/cinéma, travail émotionnel, émotions collectives, argent/pouvoir/politique, éco-anxiété, corps/performance). Les 4 lots de rédaction (01-05, 06-10, 11-14, 15-18) sont terminés côté contenu. **Reste à vérifier au moment de la reprise** : la consolidation finale a-t-elle été faite (README du guide réécrit, `4 - Sources/Les emotions.md` mis à jour, notions transversales créées si pertinent, pipeline régénéré, README racine mis à jour, commit final poussé) ? Si non, c'est la priorité absolue avant de continuer sur un autre guide. |
| La rencontre | 🔄 Élicitation faite (grille + 2 exemples de 30 sous-thèmes présentés : « histoire et sociologie de la rencontre » et « le corps et les sens dans l'attraction »), rédaction en cours de lancement au moment de cette note | Plan prévu : 9 chapitres existants approfondis à 2000+ mots + environ 6 nouveaux chapitres intégrant les 60 sous-thèmes des deux exemples (histoire de la rencontre du mariage arrangé au swipe, endogamie et paradoxe du choix, corps et sens dans l'attraction, chimie du premier rendez-vous, rituels de cour à travers les cultures, langage corporel et contexte sensoriel). **Vérifier au moment de la reprise si un agent a déjà été lancé et où il en est.** |
| L'amour | ⏳ Pas commencé | Prochain sur la liste après La rencontre. |
| Pour Nous | ⏳ Pas commencé | |
| Les nouvelles compositions familiales | ⏳ Pas commencé | Déjà enrichi une fois cette session (nouveau chapitre sur les autres modèles familiaux), mais pas encore passé par le traitement "2000 mots/chapitre + 10 familles + 60 exemples". |
| Réseaux sociaux | ⏳ Pas commencé | Guide déjà volumineux (10 chapitres, ~14 500 mots) créé cette même session — l'utilisateur n'a pas confirmé s'il doit aussi passer par ce traitement, à clarifier au moment venu. |

## Comment reprendre

1. Lire ce fichier en entier, puis `CLAUDE.md` à la racine, puis `MAINTENANCE.md`.
2. Vérifier l'état réel du dépôt (`git log`, `git status`, lire les guides concernés) plutôt que de faire confiance aveuglément au tableau ci-dessus s'il n'a pas été mis à jour en même temps que le dernier commit.
3. Invoquer `/Faiseur2Guide` pour le prochain guide de la liste, dérouler l'élicitation complète (grille des 10 familles + angles existants + question de recoupement + les deux exemples à 30 sous-thèmes, présentés ensemble) **dans la conversation**, attendre la validation de l'utilisateur.
4. Une fois validé, rédiger (déléguer à des agents en arrière-plan si le volume le justifie, comme cela a été fait pour Les émotions : plusieurs lots en parallèle, consolidation finale par un seul agent).
5. Mettre à jour ce fichier (tableau d'état) et le committer avec le reste.
