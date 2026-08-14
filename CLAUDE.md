# Comprendre pour tous — instructions pour Claude Code

Ce fichier est chargé automatiquement au début de chaque session dans ce dossier. Il ne remplace ni `MAINTENANCE.md` ni le skill `Faiseur2Guide` — il garantit que leurs règles les plus critiques sont appliquées même si personne ne pense à relire ces documents.

## Avant de toucher au contenu

- **Lire `MAINTENANCE.md` en entier** avant de modifier un guide existant.
- **Avant d'écrire un nouveau guide ou d'enrichir un guide existant, dérouler l'élicitation complète du skill `Faiseur2Guide` directement dans la conversation, jamais déléguée à un agent en arrière-plan** : présenter, **dans le même message**, la grille des 10 familles en entier (pas une sélection), les angles déjà présents dans le dépôt, la question de recoupement, ET les deux exemples de 30 sous-thèmes (ne jamais les faire attendre derrière un premier tour de réponse). Attendre la validation de l'interlocuteur avant d'écrire ou de faire écrire une seule ligne de contenu. Ne jamais résumer ou sauter cette étape même si la demande semble déjà assez précise.

## Règles non négociables (rappel — le détail et le "pourquoi" sont dans `MAINTENANCE.md`)

- **Bandeau d'avertissement obligatoire** en tête de chaque `README.md` de guide, juste après le titre `#`, texte exact repris depuis `MAINTENANCE.md`.
- **Sourçage en hyperlien**, jamais un tag `(source : ...)` nu : le lien se pose directement sur la phrase que la source appuie. Ne jamais fabriquer une URL ou un DOI — si aucune source vérifiable n'est trouvée après recherche sérieuse, le dire explicitement dans le texte plutôt que d'inventer ou d'omettre.
- **Réciprocité obligatoire avec `4 - Sources/<Guide>.md`** : toute source hyperliée dans un chapitre doit aussi y figurer, avec le même lien direct.
- **Pas de chapitre final "Sources vérifiables" par guide** (règle v12 du skill, 13 août 2026) — chaque chapitre garde sa propre section de sources en fin de chapitre, mais l'agrégation complète du guide n'existe que dans `4 - Sources/`.
- **Pied de page réduit à l'essentiel** : la dernière section de contenu utile suivie de `Retour à [l'accueil de Comprendre pour tous](<../../README.md>).` — jamais de section "Autour de ce guide", "La suite", "Le guide jumeau" ni "Sources et mise à jour". "Par où commencer" reste bienvenue.
- **Nuance systématique** : aucune affirmation universalisante sur le couple, la famille ou le genre — "dans la plupart des cas", jamais présenté comme une règle qui s'appliquerait partout.
- **Rien de journal ou de mainteneur dans le contenu publié** : pas de "Ajouts du [date]", pas de "ce qui reste à faire", pas de cadence de révision. Ce type de contenu va dans `5 - Notes Internes/`, jamais dans un dossier consultable.

## Le pipeline

- `1 - Guides/` est la source de vérité. `0 - Guides complets/` et `3 - Transversal/Par sujet.md` / `Par angle.md` sont **générés** — ne jamais les éditer à la main.
- Après toute modification de contenu : `python build-guides-complets.py` puis `python build-index.py` puis `python build.py`.
- Avant de committer, vérifier les liens cassés :
  ```
  python -c "import pathlib,re; [print('CASSE',f,m.group(1)) for f in pathlib.Path('.').rglob('*.md') for m in re.finditer(r'\]\(<([^>]+)>\)', f.read_text(encoding='utf-8')) if not (f.parent/m.group(1)).resolve().exists()]"
  ```
  (deux faux positifs connus et acceptés : les exemples de syntaxe dans `MAINTENANCE.md` et dans le skill.)

## Contraintes du site

Site statique hébergé sur GitHub Pages, nom de domaine sur OVHcloud — aucun serveur applicatif, aucune base de données côté site. Annoncer explicitement ce qui n'est pas faisable dans ce cadre avant de commencer à coder une fonctionnalité qui en aurait besoin, plutôt que de la simuler ou de l'abandonner en silence.

## Style d'écriture

Ton confiant et direct, jamais professoral (voir les personas du skill selon le sujet). Pas d'italique, pas de tiret cadratin — virgule, point-virgule ou deux-points. Guillemets français (« ») pour les titres d'ouvrages et noms propres, gras pour l'emphase.

## Git

Ne committer que sur demande explicite. Message de commit en français, descriptif, orienté sur le "pourquoi". Toujours terminer par :
```
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```

## Historique des demandes

Après chaque demande de l'utilisateur (chaque message qui déclenche du travail, pas les accusés de réception automatiques), ajouter une ligne à `5 - Notes Internes/Historique des demandes.md` : numéro suivant, date, heure, un contexte en une phrase, et le texte de la demande. Ce fichier n'est jamais publié. Ne pas attendre une relance explicite pour le faire — c'est systématique, comme une règle de fond, pas une tâche ponctuelle.

## Travail en parallèle

Pour une tâche volumineuse et indépendante (nouveau guide, passe de nuance sur des guides différents de ceux déjà en cours), il est possible de paralléliser via plusieurs agents en arrière-plan. Toujours vérifier `git status` avant de committer pour ne pas écraser ou dupliquer le travail d'un autre agent en cours, et se limiter aux fichiers réellement concernés par sa propre tâche plutôt que de tout stager en aveugle.
