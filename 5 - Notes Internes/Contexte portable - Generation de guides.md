---
type: "interne"
mis_a_jour_le: 2026-09-17
---

# Contexte portable — génération de guides

Fichier de travail, **non publié**, pensé pour être copié-collé dans une nouvelle session Claude Code afin de continuer le chantier d'enrichissement des guides sans avoir à redériver le contexte. Le projet tourne avec plusieurs sessions en parallèle sur des guides différents.

## Ce qu'il faut savoir avant de commencer

1. **Toujours lire `CLAUDE.md` et `MAINTENANCE.md` en entier** avant de toucher au contenu (chargés automatiquement en général, mais à vérifier).
2. **Avant d'écrire ou d'enrichir un guide, dérouler l'élicitation complète du skill `Faiseur2Guide` directement dans la conversation** : inventaire du dépôt, grille des 10 familles d'angles en entier, angles déjà présents dans le dépôt, question de recoupement, et les deux exemples de 30 sous-thèmes. Jamais délégué à un agent en arrière-plan, jamais résumé même si la demande semble déjà précise.
3. **Règle par défaut désormais (v17-v18 du skill)** : sauf consigne contraire explicite, intégrer l'ensemble des thèmes présentés (toutes les familles pertinentes + les deux exemples de 30 sous-thèmes en entier) sans attendre un tri de l'utilisateur. Un recoupement avec un sujet déjà traité ailleurs ne justifie plus d'écarter un thème : l'écrire quand même sous l'angle propre au guide, avec un renvoi croisé explicite dans les deux sens.
4. **Longueur par chapitre : 1 500 à 3 500 mots** (v17, remplace l'ancien seuil de 7 500-9 000 jamais atteint en pratique). Compter avec `wc -w` ou l'équivalent Python (`len(body.split())` après avoir retiré le frontmatter). Ne jamais combler par du remplissage : si le sujet a moins de matière sourcée disponible, le dire plutôt que gonfler.
5. **Témoignages réels obligatoires quand le sujet touche à un vécu personnel fort** (v16) : chercher un vrai témoignage publié (association de patients, presse, forum public), le sourcer comme n'importe quelle autre affirmation. Jamais en inventer un, même "à titre illustratif". Si aucun n'est trouvé après recherche sérieuse, le dire explicitement dans le chapitre plutôt que de laisser un vide ou d'en fabriquer un.
6. **Neutralité de genre du lecteur** (v15) : quand un guide tutoie un lecteur qui peut être de plusieurs genres, accorder au masculin non marqué ou restructurer la phrase, jamais accorder au hasard. Ne s'applique pas aux chapitres construits en miroir de genre ("Ce que les hommes attendent des femmes"), où le genre du sujet fait partie du sujet même.
7. **Sourçage** : le lien se pose sur l'affirmation elle-même (`[la phrase](url)`), jamais un tag `(source : ...)` nu. Au moins une source réelle et vérifiable par sous-partie (`###`). Jamais fabriquer une URL, un DOI ou un chiffre. Réciprocité obligatoire avec `4 - Sources/<Nom du guide>.md`.
8. **Pas de chapitre final "Sources vérifiables" agrégeant tout le guide** : chaque chapitre garde sa propre section de sources en fin de chapitre, `4 - Sources/` reste le seul endroit avec la liste consolidée.
9. **Bandeau d'avertissement obligatoire** en tête de chaque `README.md` de guide (texte exact dans `MAINTENANCE.md`), et **pied de page réduit** (`Retour à [l'accueil...]`, jamais de section "Autour de ce guide" / "La suite" / "Sources et mise à jour").
10. **Travail en parallèle — vérifier `git status` avant tout commit.** D'autres sessions travaillent en même temps sur d'autres guides (Pour Elle et Pour Lui ont été vus en cours de modification par une autre session le 17/09/2026, ex. nouveau chapitre "35 - Les conflits entre femmes.md" dans Pour Elle). Ne jamais stager en aveugle (`git add -A` sur tout le dépôt) : se limiter aux fichiers réellement concernés par sa propre tâche, laisser les fichiers apparus sans qu'on les ait créés soi-même.
11. **`build.py`** est aussi parfois modifié par un autre processus en parallèle (vu le 16/09/2026, ajout de données structurées JSON-LD). Vérifier avant de le committer, il n'est probablement pas de son ressort.

## Pipeline après toute modification de contenu

```
python build-guides-complets.py   régénère 0 - Guides complets/
python build-index.py             régénère 3 - Transversal/Par sujet.md et Par angle.md
python build.py                   régénère le site dans _site/
```

Puis vérifier les liens cassés :
```
python -c "import pathlib,re; [print('CASSE',f,m.group(1)) for f in pathlib.Path('.').rglob('*.md') for m in re.finditer(r'\]\(<([^>]+)>\)', f.read_text(encoding='utf-8')) if not (f.parent/m.group(1)).resolve().exists()]"
```
(faux positifs connus et acceptés : les exemples de syntaxe dans `MAINTENANCE.md`, `CLAUDE.md` et le skill.)

Pour calculer une ancre de titre (nécessaire pour convertir un renvoi interne du type "voir 4.4" en lien cliquable), reproduire exactement la fonction `slugify` de `build.py` : normaliser en NFKD, encoder en ASCII en ignorant les caractères non-ASCII, mettre en minuscule, remplacer toute suite de caractères non alphanumériques par un tiret, puis strip des tirets en bord de chaîne. L'ancre se calcule sur le texte complet du titre, numéro de sous-partie inclus (ex. "4.4 Honte et culpabilité" → `4-4-honte-et-culpabilite`).

## État des guides au 17/09/2026 (mots / chapitres)

| Guide | Chapitres | Mots | Statut |
|---|---|---|---|
| Pour Elle | 35 (en cours ailleurs) | 75 568 | Référence, modifié par une autre session en ce moment |
| Pour Lui | 34 (en cours ailleurs) | 65 388 | Référence, modifié par une autre session en ce moment |
| Les émotions | 20 | 45 154 | Fait (chapitres émotions positives + bonheur sociétal ajoutés le 15/09) |
| Réseaux sociaux | 20 | 25 233 | Fait le 17/09 (10 nouveaux chapitres : économie, géopolitique, régulation, populations spécifiques) |
| Massage professionnel | 21 | 22 778 | Fait le 16/09 (9 nouveaux chapitres + passe d'étoffement sur les 12 premiers) |
| IST, dépistage et prévention | 25 | 18 266 | Fait le 16/09 (8 nouveaux chapitres : dépistage en pratique, résistance antibiotique, IST une par une avec témoignages) |
| Questions et communication | 46 | 75 620 | Fait le 17/09 (étoffement des 23 chapitres existants + 23 nouveaux chapitres couvrant les deux exemples de 30 sous-thèmes et l'intégralité de la grille des 100 angles, voir `Chantier - Questions et communication.md`) |
| Pour Nous | 11 | 12 296 | **Pas encore repris** |
| La rencontre | 9 | 11 873 | **Pas encore repris** |
| L'amour | 9 | 10 128 | **Pas encore repris** |
| Les nouvelles compositions familiales | 4 | 6 829 | **Pas encore repris**, le guide le plus étroit (seulement 4 chapitres) |

## Prochains guides à faire, par ordre de priorité suggéré

1. **Questions et communication** — étoffer les 23 chapitres existants plutôt que d'en ajouter, chacun est sous le seuil de 1 500 mots.
2. **Les nouvelles compositions familiales** — seulement 4 chapitres, le guide le plus étroit, gagnerait à une vraie élicitation complète (nouveaux angles + chapitres).
3. **Pour Nous**, **La rencontre**, **L'amour** — même profil (9-11 chapitres, ~1 100-1 300 mots/chapitre), à traiter chacun avec l'élicitation complète.

Ne pas toucher Pour Elle / Pour Lui sans vérifier d'abord l'état réel (`git log`, `git status`) : une autre session y travaille activement à la date de rédaction de ce fichier.

## Chantiers de fond toujours ouverts (voir `MAINTENANCE.md`)

- Revérification des chiffres pour tous les guides sauf IST (déjà fait le 16/09/2026).
- Vérifier la réciprocité des sources des chapitres au-delà des tout premiers, sur les guides autres qu'IST, Les émotions, Massage professionnel et Réseaux sociaux (le trou comblé sur ces guides-là peut exister ailleurs, non vérifié systématiquement).
- Passe de nuance globale sur les guides les plus anciens.
- Piste de guides sur la recherche non occidentale (hikikomori au Japon, charge parentale liée à l'enfant unique en Chine, mariages arrangés en Inde), notée dans `5 - Notes Internes/Ce qu'il faut faire.md`, non urgente.

## Comment reprendre

Dans la nouvelle session : coller ce fichier, dire quel guide traiter en premier (ou suivre l'ordre de priorité ci-dessus), et dérouler l'élicitation complète avant d'écrire quoi que ce soit, même si la demande semble déjà tranchée par ce document.
