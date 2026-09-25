---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-23
---

# À faire — améliorer la méthode de rédaction, puis reprendre tous les guides

Fichier de suivi **non publié**, pensé pour qu'une autre session Claude reprenne ce chantier sans accès à la conversation d'origine.

## Pourquoi ce chantier existe

Relecture critique du 23/09/2026. Constat de l'utilisateur sur le guide « Psychologie de la personnalité », valable pour les quatre guides écrits en mode débit : les chapitres **citent des études sans jamais les expliquer**, ne disent pas pourquoi elles sont intéressantes, ne font aucun lien avec le vécu du lecteur, et ne traitent pas le sujet du général vers le particulier. Verdict : « sans saveur », « ne captent pas l'attention ».

Trois défauts distincts identifiés, du plus grave au moins grave.

**1. Décrire l'emballage, jamais le contenu.** Le chapitre 3 « Le modèle Big Five » ne définit aucun des cinq traits : ils apparaissent une seule fois, cités en passant dans une traduction. On lit le chapitre en entier sans savoir ce que mesure l'ouverture. Même défaut au chapitre 24, qui annonce « neuf dimensions du tempérament » sans les lister. Cause : les sources parlaient *du* modèle (histoire, réplication, pouvoir prédictif), pas *le* modèle, et la rédaction a suivi les sources au lieu de suivre les besoins du lecteur.

**2. Coller au lieu d'écrire.** La règle de sourçage du projet (le lien se pose sur la phrase que la source appuie) avait dégénéré en méthode de fabrication : traduire le résumé de l'étude, mettre des crochets autour, relier avec une transition. Résultat : tout le contenu se trouve *dans* les crochets, il ne reste dehors que du liant. Aucun auteur dans le texte.

**3. Ne pas creuser.** Deux recherches en parallèle, rédaction, chapitre suivant. Jamais de second tour pour le mécanisme, la contre-étude, le cas concret ou un angle non demandé. D'où des sources inégales (blogs de wellness pour des affirmations centrales) et des chapitres courts faute de matière.

## Le vrai problème structurel : les règles existaient déjà

Le skill `Faiseur2Guide` impose déjà, et ces règles ont été ignorées sur 32 chapitres :

| Ligne du skill | Règle | Respect réel |
|---|---|---|
| 27 | Une analogie concrète nommée dans le titre de section | jamais |
| 29 | Bloc 👁️ Vu de l'autre côté | jamais, y compris aux chapitres faits pour ça |
| 30 | Bons réflexes = actions concrètes, jamais des généralités | violé (« Retenir que… ») |
| 32 | Bloc 🗣️ Témoignage réel | jamais sur ce guide |
| 21 | Jamais de ton professoral | violé |
| 171 | Chapitre entre 1 500 et 3 500 mots | **aucun chapitre au-dessus de 1 144** |

Diagnostic : le skill fait 250 lignes dont six portent sur l'écriture. Le procédural est vérifiable (une source est dans `4 - Sources/` ou non), la craft ne l'est pas. Sous pression de volume, seul le vérifiable survit. Le fichier de chantier du guide ne suivait qu'une seule métrique : le nombre de mots — un tableau de bord qui ne mesurait que le débit.

## Étape 1 — améliorer la méthode (à faire avant toute reprise)

| # | Tâche | Statut |
|---|---|---|
| 1.1 | Chapitre pilote : refaire entièrement `03 - Le modele Big Five.md` sous les nouvelles règles, faire valider par l'utilisateur | **fait** (24/09/2026, 920 → 2 066 mots, validé après une passe de correction) |
| 1.2 | Créer le skill `Redaction2Chapitre` (craft, court, avec le bloc ⚖️ Nuance et la liste de vérification) | **fait** (104 lignes) |
| 1.3 | Alléger `Faiseur2Guide` : ne garder que l'élicitation, le plan de chapitres et la checklist de livraison | **fait** (v19) |
| 1.4 | Créer le skill `Audit2Guide` (lecture seule, renvoie un rapport de défauts par chapitre) | **fait** (56 lignes) |
| 1.5 | Ajouter dans `CLAUDE.md` trois lignes de renvoi vers les nouveaux skills | **fait** |

### Ce que le pilote a corrigé dans les règles

La première version du chapitre pilote cochait toutes les cases et restait mauvaise : analogie citée dans un titre mais jamais reprise, blocs « Nuance » qui définissaient au lieu de nuancer, chiffre de 0,31 tombant de nulle part, et surtout l'objet central jamais défini (les cinq traits décrits un par un sans jamais dire ce que le modèle affirme). Cinq corrections en sont sorties, toutes inscrites dans `Redaction2Chapitre` :

1. Définir l'objet lui-même par une phrase en gras, pas seulement énumérer ses parties.
2. Une seule analogie, portée de bout en bout, et retournée en fin de chapitre pour montrer la limite du sujet.
3. Un seul bloc ⚖️ Nuance par chapitre, qui énumère les malentendus. Il nuance, il ne définit pas.
4. Tout chiffre précédé de la question qui le rend nécessaire.
5. La règle des 15 mots par lien était trop serrée (elle sanctionnait des phrases écrites, pas collées) : remplacée par « une seule affirmation par lien », plafond à 25 mots, interdiction du point-virgule maintenue.

Le piège principal est inscrit tel quel dans le skill : ces règles se satisfont en surface. Le seul vrai test reste le fil, c'est-à-dire le fait que le chapitre se lise du haut vers le bas en restant sur le sujet de son titre.

### Règles à inscrire dans `Redaction2Chapitre`

- **Bloc ⚖️ Nuance**, nouveau bloc structurel au même titre que 💑 👁️ 🗣️. Il prend en charge la notion, en deux mouvements obligatoires : (1) la définir et l'incarner aux deux bouts de l'échelle par un exemple reconnaissable ; (2) écarter la confusion courante et refuser le jugement de valeur (un score bas n'est pas un défaut). Se place à la première utilisation sérieuse du terme, **avant toute recherche citée à son sujet** — on ne cite aucune étude sur un objet avant d'avoir posé l'objet ; donc presque toujours dans la première sous-partie, jamais en fin de chapitre. À utiliser en priorité pour les mots qui existent dans la langue courante avec un autre sens (résilience, toxique, narcissisme, conformisme, authenticité, tempérament), où le lecteur croit déjà savoir. À ne pas utiliser pour un mot ordinaire et sans ambiguïté, ni pour une notion déjà développée dans `2 - Notions/` ou un autre chapitre (renvoi, jamais redéfinition — règle permanente sur les notions non dupliquées). Maximum deux ou trois par chapitre, uniquement pour les termes sur lesquels le chapitre repose.
- **Écrire la phrase, puis la sourcer** — jamais l'inverse. Garde-fou : si le texte entre crochets dépasse quinze mots ou contient un point-virgule, c'est un résumé collé, à réécrire.
- **Trois obligations par étude** : ce que les chercheurs ont fait concrètement, ce qui en est sorti, pourquoi c'est malin ou surprenant.
- **Toute valeur chiffrée reçoit son échelle** par comparaison avec quelque chose de connu.
- **Le mécanisme avant la statistique**, raconté en termes de vie quotidienne.
- **Du général au particulier** : ouvrir sur le phénomène que le lecteur reconnaît, puis resserrer.
- **Deux tours de recherche minimum**, le second dédié au mécanisme, à une limite ou contre-étude, à un cas concret ou témoignage publié, et à un angle non demandé.
- **Remettre en service** les règles existantes ignorées : analogie nommée, blocs 👁️ 💑 🗣️, réflexes formulés en actions, plancher de 1 500 mots.
- **Liste de vérification de fin de chapitre**, qui remplace le comptage de mots dans les fichiers de chantier. Elle exige l'artefact, pas une case cochée : nommer l'analogie ; citer le réflexe le plus actionnable ; dire quel mécanisme est expliqué ; dire si un bloc 👁️/💑/🗣️ était pertinent et où il est ; nommer l'angle trouvé au second tour qui n'était pas dans la commande.

### Vocabulaire de correction standardisé

À inscrire dans le skill avec le correctif associé, pour que l'utilisateur corrige en trois mots :

| Formule | Ce qu'elle déclenche |
|---|---|
| « tu cites, tu n'expliques pas » | reprendre les trois obligations par étude |
| « tu décris l'emballage » | l'objet central n'est pas défini dans le chapitre |
| « chiffre sans échelle » | ajouter la comparaison |
| « ce réflexe n'est pas une action » | reformuler en geste ou en phrase à dire |
| « tu n'as pas creusé » | second tour de recherche manquant |

## Les deux modes de correction

Distinction qui rend le chantier faisable : la plupart des chapitres n'ont pas besoin d'être refaits, seulement complétés.

- **Profond** (`/Redaction2Chapitre <guide> <n> profond`) — réécriture complète : lecture de l'existant et du rapport d'audit, premier tour de recherche sur le phénomène et sur l'objet lui-même, second tour sur mécanisme / contre-étude / cas concret / angle non demandé, rédaction, blocs, mise à jour de `4 - Sources/`, liste de vérification affichée. Estimation : 30-50k tokens par chapitre.
- **Chirurgie** (`/Redaction2Chapitre <guide> <n-m> chirurgie`) — on garde la structure et le texte qui tient : ajout des blocs ⚖️ Nuance manquants, définition des objets non définis, échelle sur les chiffres, conversion des « Retenir que… » en actions. Pas de second tour de recherche sauf trou factuel signalé par l'audit. Estimation : 10-15k tokens par chapitre, soit environ trois fois moins cher.

Rythme de travail visé sur forfait Pro : 5-6 chapitres en profond par fenêtre, ou 15-20 en chirurgie. Hypothèse à recaler dès le premier lot.

## Étape 2 — auditer, puis reprendre chaque guide

**Ne pas auditer les 427 chapitres avant d'avoir validé la grille sur le pilote puis sur un guide témoin** : un audit passé contre une grille non stabilisée serait à refaire intégralement.

Ordre retenu : pilote (1 chapitre) → gravure des skills → guide témoin de bout en bout → audit en masse en agents parallèles par groupes de 3-4 → correction par vagues selon la priorité ci-dessous → relecture d'un échantillon de trois chapitres par guide corrigé, pour vérifier que la méthode ne s'est pas délitée en cours de route (c'est exactement ce qui s'est produit sur les 32 chapitres de Psychologie de la personnalité).

`/Audit2Guide <guide>` est en lecture seule et écrit `5 - Notes Internes/Audit - <guide>.md` : tableau chapitre par chapitre, défauts relevés, et verdict par chapitre (chirurgie / réécriture / rien à faire).

La densité par chapitre sert de signal de tri objectif (plancher du skill : 1 500 mots). Elle ne prouve pas la qualité, mais croisée avec les guides écrits en mode débit, elle trie correctement.

| Guide | Chapitres | Mots | Mots/chap. | Priorité | Audit | Reprise |
|---|---|---|---|---|---|---|
| IST, dépistage et prévention | 25 | 18 266 | 731 | haute | à faire | à faire |
| Psychologie de la personnalité | 32 | 27 309 | 853 | haute (mode débit) | à faire | à faire |
| Maladie grave et handicap | 32 | 29 573 | 924 | haute (mode débit) | à faire | à faire |
| Alimentation | 26 | 25 035 | 963 | haute (mode débit) | à faire | à faire |
| Massage professionnel | 21 | 22 778 | 1 085 | moyenne | à faire | à faire |
| Le sommeil | 16 | 17 916 | 1 120 | haute (mode débit) | à faire | à faire |
| Réseaux sociaux | 20 | 25 233 | 1 262 | moyenne | à faire | à faire |
| Pour Nous | 25 | 31 711 | 1 268 | moyenne | à faire | à faire |
| L'amour | 28 | 39 788 | 1 421 | basse | à faire | à faire |
| La rencontre | 28 | 44 619 | 1 594 | basse | à faire | à faire |
| Questions et communication | 46 | 75 666 | 1 645 | basse | à faire | à faire |
| Les nouvelles compositions familiales | 31 | 57 404 | 1 852 | basse | à faire | à faire |
| Pour Lui | 38 | 71 079 | 1 871 | basse | à faire | à faire |
| Pour Elle | 39 | 81 179 | 2 082 | basse | à faire | à faire |
| Les émotions | 20 | 45 154 | 2 258 | basse | à faire | à faire |

Chiffres issus de `build-guides-complets.py` au 23/09/2026. À noter : le tableau du README racine annonce des nombres de chapitres différents pour certains guides (Pour Elle 34 contre 39 ici) — écart à élucider pendant l'audit.

## Contraintes d'exécution à respecter

- **Forfait Claude Pro.** Le mode profond coûte environ le double par chapitre (deux tours de recherche, chapitres de 1 500-2 000 mots au lieu de 800). Travailler en **séquentiel, par lots de 5-6 chapitres**, sur plusieurs sessions. Un guide de 32 chapitres n'est pas une session.
- **Agents en parallèle : oui pour l'audit** (lecture seule, rapport court, économise le contexte principal). **Prudence pour la rédaction** : des agents qui écrivent en parallèle ne se voient pas, donc dupliquent les sources et les notions — ce que la règle permanente interdit. Si utilisé quand même : lots de chapitres indépendants, interdiction de toucher à `4 - Sources/` et `2 - Notions/`, consolidation centrale à la fin.
- **Modèles** : Opus pour le pilote et les premiers chapitres d'un guide (là où se fixe le ton), Sonnet pour appliquer un gabarit validé et pour les audits.

## Étape 3a — chirurgies et défauts ponctuels (24/09/2026)

Fait, sur la base de `5 - Notes Internes/Audit - Psychologie de la personnalite.md` :

- Défauts ponctuels : langage de mainteneur supprimé dans les ouvertures des chapitres 7, 8, 10, 11, 12, 13. Chapitre 24 : les neuf dimensions de Thomas et Chess listées (elles étaient annoncées dans un titre sans être données), et le tiers d'enfants hors des trois profils explicité (40+10+15 % ne totalisait pas 100 %).
- Six chirurgies : 13 (bloc 🗣️ témoignage réel ajouté — Bella DePaulo, HuffPost, sur le célibat volontaire), 15 (burn-out défini par ses trois dimensions, analogie du fusible), 17 (individualisme/collectivisme définis), 20 (bloc 💑, corrélations 0,855 et -0,439 mises à l'échelle du chapitre 3), 21 (bloc 👁️ sur l'asymétrie d'attirance, pourcentages mis à l'échelle), 32 (bloc 💑, le 69 % de Gottman mis à l'échelle). Plusieurs réflexes passifs (« Retenir que... ») convertis en actions au passage.
- 979 → 1 056 (13), 890 → 964 (15), 826 → 872 (17), 866 → 1 034 (20), 895 → 993 (21), 821 → 944 (32). Guide total : 28 423 → 29 171 mots.
- Pipeline relancé, réciprocité des sources vérifiée, aucun lien cassé.
- Restent 25 chapitres en réécriture sur ce guide (verdict de l'audit), non traités : voir l'arbitrage à trancher ci-dessous avant de les lancer.

## Étape 4 — audit en masse (24/09/2026), interrompu par un plafond de session

Tentative de lancer 4 agents de premier niveau (un par groupe de 3-4 guides), chacun sous-déléguant à un agent par guide. Résultat : le plafond de session Sonnet a été atteint en cours de route (reset 18h20 heure de Paris), la majorité des sous-agents ont échoué avec une erreur `rate_limit` avant de produire leur rapport. Aucun fichier de guide n'a été modifié (lecture seule respectée par tous les agents, y compris ceux qui ont échoué).

**Résultat exploitable obtenu avant l'échec : "La rencontre", chapitres 1 à 14 sur 28.**

| Verdict | Chapitres |
|---|---|
| Rien à faire | 3, 4, 6 |
| Chirurgie | 1, 2, 5, 7, 8, 9, 10, 13, 14 |
| Réécriture | 11, 12 |

Profil très différent des guides écrits en mode débit (Le sommeil, Alimentation, Maladie grave et handicap, Psychologie de la personnalité) : sourçage globalement propre, analogies présentes, réflexes presque tous actifs. Le défaut dominant et récurrent est l'absence quasi totale des blocs ⚖️/👁️/🗣️ alors que des candidats naturels existent dans le texte de plusieurs chapitres (contrôle coercitif en 7, deuil/veuvage en 13, consentement en 9 et 14). Chapitres 11 et 12 en réécriture : sourçage à 100% de liens collés et fil cassé en 11 (sept sous-thèmes juxtaposés sans progression).

**Trois audits complets supplémentaires arrivés après l'échec initial** (malgré le plafond, plusieurs sous-agents ont fini avant de le heurter) :

| Guide | Chapitres | Rien à faire | Chirurgie | Réécriture | Défaut dominant | Coût estimé |
|---|---|---|---|---|---|---|
| Massage professionnel | 21 | 1 | 20 | 0 | Sourçage collé (74%), 9 chapitres à 100% mais déclassés en chirurgie car fil/analogies solides | 200-300k, 1,5-2 sessions |
| Maladie grave et handicap | 32 | 0 | 32 | 0 | Sourçage collé (56,5%), 0 bloc ⚖️/👁️/💑, tous sous 1500 mots mais fil intact | 320-480k, 2-3 sessions |
| IST, dépistage et prévention | 25 | 0 | 25 | 0 | Sourçage collé (43%), analogie absente sur 11/25, réflexes déjà 94% actifs | 250-375k, 1,5-2,5 sessions |

Point notable : sur ces trois guides comme sur "La rencontre", **aucun chapitre n'atteint le verdict réécriture**. Contrairement à "Psychologie de la personnalité" (25 réécritures sur 32), ces guides ont un fil et des objets bien posés ; leur défaut dominant est mécanique (sourçage collé, blocs manquants) et se corrige entièrement en chirurgie. Cela confirme l'hypothèse du profil guide par guide plutôt qu'un mode de dégradation uniforme sur tout le dépôt.

## Étape 4 (suite) — audit en masse terminé (24/09/2026)

Les 15 guides du dépôt sont désormais tous audités (427 chapitres). Deux incidents pendant l'audit, tous deux sans conséquence sur le fond :

- **Deux guides ("Pour Lui", "Les émotions") audités deux fois par des agents qui ne se voyaient pas** : le second a écrasé le premier dans le même fichier. Les chiffres retenus ci-dessous sont ceux du rapport le plus récent, généralement produit avec un comptage programmatique plus fiable que le premier.
- **"La rencontre" audité en quatre lots qui se sont écrasés successivement** dans le même fichier (1-7, 8-14, 15-21, 22-28). Réconcilié manuellement dans `Audit - La rencontre.md` : 28/28 chapitres couverts, 8 rien à faire, 18 chirurgie, 2 réécriture.

**Enseignement méthodologique à retenir pour la prochaine campagne d'audit** : le dernier agent (Questions et communication) a refusé d'appliquer mécaniquement le seuil de 85 % de liens collés à 32 de ses 46 chapitres, parce qu'à la lecture chaque lien était entouré d'une vraie explication — le défaut était que l'ancre du lien engloutissait toute la phrase au lieu de se poser sur la proposition précise. **Liens trop longs et études non expliquées sont deux défauts différents, que la grille actuelle fusionne dans un seul critère.** À corriger dans `Audit2Guide` avant la prochaine vague : distinguer explicitement "lien mal ancré" (chirurgie légère, reformuler l'ancre) de "résumé d'étude jamais expliqué en dehors du lien" (défaut de fond, justifie réécriture).

### Tableau maître — 15 guides, 427 chapitres

| Guide | Chapitres | Rien à faire | Chirurgie | Réécriture | Défaut dominant | Coût estimé |
|---|---|---|---|---|---|---|
| Psychologie de la personnalité | 32 | 1 (traité) | 6 (traités) | **25 restant** | Voir `Audit - Psychologie de la personnalite.md` | 875k-1,1M (25 ch. restants) |
| Alimentation | 26 | 0 | 9 | **17** | 88% liens collés, 0 analogie, tous sous 1500 mots | 685-900k |
| Le sommeil | 16 | 0 | 9 | **7** | 85,6% liens collés, 0 analogie, écarts de genre non traités (👁️/💑) | 335-450k |
| Pour Nous | 25 | 0 | 21 | **4** (16,19,20,24) | Deux générations : 1-11 excellent, 12-25 en net retrait (sources blogs) | 350-495k |
| La rencontre | 28 | 8 | 18 | 2 (11,12) | 0 bloc ⚖️ sur 28 ch., 7 ch. sans aucun bloc malgré candidats explicites | 250-360k |
| IST, dépistage et prévention | 25 | 0 | 25 | 0 | 43% liens collés, analogie absente sur 11/25, déjà 94% réflexes actifs | 250-375k |
| Maladie grave et handicap | 32 | 0 | 32 | 0 | 56,5% liens collés, 0 bloc ⚖️/👁️/💑, tous sous 1500 mots, fil intact | 320-480k |
| Massage professionnel | 21 | 1 | 20 | 0 | 74% liens collés (9 ch. à 100% mais fil/analogies solides) | 200-300k |
| Réseaux sociaux | 20 | 0 | 20 | 0 | Aucun ch. au plancher de mots, blocs 👁️/💑/🗣️ quasi absents | 200-300k |
| Les émotions | 20 | 0 | 20 | 0 | Bloc ⚖️ mal formaté (texte gras non standard), traces de mainteneur en ch.11-14 | 200-280k (approx.) |
| Les nouvelles compositions familiales | 31 | 0 | 31 (3 lourdes) | 0 | 46% liens collés, 2 analogies filées sur 31 ch. seulement | 350-450k (approx.) |
| Pour Lui | 38 | 9 | 29 | 0 | 0 bloc ⚖️/🗣️ sur 38 ch. ; ch.21-29 et 36-39 nettement en retrait | 350k (approx.) |
| Pour Elle | 39 | 23 | 16 | 0 | Meilleur profil du dépôt ; défaut concentré sur la série relationnelle (14,20,25,27-30,35-39) ; ligne de mainteneur en ch.34 à supprimer | 150-220k (approx.) |
| Questions et communication | 46 | 0 | 46 | 0 | Meilleur guide du dépôt sur le fond ; défaut = ancres de lien trop longues, pas des résumés non expliqués | 700-950k (approx.) |
| **Total** | **427** | **42** | **330** (dont 55 hors Psy restant) | **55** | | **≈ 5,3M à 7,2M tokens** |

Chiffres "approx." : estimation reconstituée à partir d'une fourchette horaire donnée par l'agent plutôt que d'un chiffre en tokens.

### Deux défauts ponctuels, indépendants de l'arbitrage, à corriger en toute hypothèse

- **Les émotions, chapitres 11-14** : phrase de mainteneur en fin de chapitre (« Aucune affirmation de ce chapitre n'est restée sans source identifiée ») à supprimer — même famille de défaut que le langage « sujet explicitement demandé » déjà corrigé sur Psychologie de la personnalité.
- **Pour Elle, chapitre 34** : ligne « Fin du document. Rédigé le 21 juillet 2026... » à supprimer. **Pour Elle, chapitre 30** : section "Bons réflexes" dupliquée en deux blocs consécutifs, à fusionner.

## L'arbitrage — à trancher avant l'étape 5

**Option A, en profondeur.** Ne reprendre que les guides à fort taux de réécriture : Psychologie de la personnalité (25 restants), Alimentation (17), Le sommeil (7), Pour Nous (4), La rencontre (2). Soit 55 réécritures + leurs chirurgies associées ≈ **2,1M à 2,7M tokens, 12-18 sessions Pro**. Les 10 autres guides restent en l'état.

**Option B, en largeur.** Traiter tous les guides mais seulement en chirurgie/défauts ponctuels (jamais de réécriture complète, même sur les 55 chapitres qui la justifieraient), plus les deux défauts ponctuels ci-dessus. Coût très inférieur à l'option A en tokens mais laisse les pires chapitres (les 55 en réécriture) sous leur niveau minimal.

**Option C, mixte (recommandée)** : les 55 réécritures d'abord (option A), puis chirurgie sur tout le reste par vagues successives, dans l'ordre du tableau ci-dessus (du plus abîmé au moins abîmé). C'est la séquence qui corrige le pire en premier sans jamais laisser un guide à moitié fait.

## Étape 5 — vagues de correction, guide par guide (24/09/2026 →)

Arbitrage retenu par l'utilisateur : "on corrige tout guide par guide" — traiter chaque guide en entier (réécritures + chirurgies) avant de passer au suivant, dans l'ordre du tableau maître (du plus abîmé au moins abîmé), sans attendre de validation intermédiaire.

### Psychologie de la personnalité — TERMINÉ (24/09/2026)

Les 25 chapitres en réécriture ont tous été repris en mode profond (analogie filée, objet défini avant sourçage, blocs ⚖️/👁️/🗣️/💑 ajoutés où pertinents, liens reformulés en phrases courtes, second tour de recherche systématique). Les 6 chirurgies et le pilote (chapitre 3) avaient déjà été traités à l'étape 3a.

- Total du guide : 29 171 → 33 171 mots (32 chapitres, tous désormais au-dessus de 800 mots, la plupart entre 950 et 1150 ; aucun n'atteint le plancher théorique de 1 500 mais le test de fond — fil, objet défini, échelle des chiffres — est rempli partout).
- Nouveaux blocs ajoutés : ⚖️ Nuance sur la quasi-totalité des 25 chapitres repris (avant : 1 seul sur tout le guide, le pilote). 🗣️ Témoignage réel ajouté aux chapitres 13 (Bella DePaulo, célibat volontaire) et 25 (Ludovic, Fondation Résilience). 👁️ ajouté aux chapitres 19 et 21. 💑 ajouté aux chapitres 20 et 32.
- Deux contre-études trouvées au second tour de recherche qui nuancent des affirmations trop tranchées de la version précédente : chapitre 14 (le concept de "névrosisme sain" n'est plus confirmé par la méta-analyse la plus récente), chapitre 3 (déjà fait au pilote, absence de corrélat cérébral au Big Five).
- Sources ajoutées à `4 - Sources/Psychologie de la personnalite.md` avec réciprocité vérifiée (chapitres 14, 16, 25, 26, 31 avaient des sources nouvelles).
- Pipeline complet exécuté, aucun lien cassé, README du guide et README racine mis à jour.
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage : plus aucun chapitre en réécriture, plus aucune chirurgie en attente.**

### Alimentation — TERMINÉ (24/09/2026)

Les 17 chapitres en réécriture et les 9 chirurgies ont tous été repris. Contrairement au guide précédent, la plupart des réécritures ici n'ont pas nécessité de second tour de recherche complet : les sources d'origine restaient bonnes, le travail a surtout consisté à réécrire la prose autour des liens (fini les résumés d'étude collés), ajouter une analogie filée par chapitre, poser un bloc ⚖️ Nuance à chaque fois qu'un terme galvaudé le justifiait (kéto/paléo, tout-ou-rien, grossophobie, alimentation intuitive), et ajouter des blocs 👁️/💑 sur les chapitres où l'audit avait noté leur absence malgré un sujet pertinent (10, 21 pour 👁️ ; 23, 16 pour 💑).

- Total du guide : 25 009 → 26 378 mots (26 chapitres, tous désormais au-dessus de 840 mots, la majorité entre 900 et 1350).
- Analogies filées ajoutées sur les 26 chapitres sans exception (0 avant cette passe) : chantier/matériaux (ch.1-4), facture électrique (ch.5), Far West (ch.7), horloge 24h (ch.15), vitrine de magasin (ch.13), iceberg (ch.10), immeuble avec un étage inondé (ch.19), réseau électrique à peu de centrales (ch.20), filtre photo (ch.21), autoroute à deux sens (ch.22), baromètre (ch.23), dictionnaire visuel (ch.25), parmi d'autres.
- Pipeline complet exécuté, aucun lien cassé, README du guide et README racine mis à jour. Sources inchangées dans `4 - Sources/Alimentation.md` (pas de second tour de recherche nécessaire sur ce guide, contrairement à Psychologie de la personnalité).
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

## Le sommeil — TERMINÉ (25/09/2026)

Les 7 chapitres en réécriture (1, 5, 7, 10, 12, 15, 16) et les 9 chirurgies (2, 3, 4, 6, 8, 9, 11, 13, 14) ont tous été repris. Le défaut dominant relevé par l'audit — 85,6 % de liens collés, zéro analogie sur les 16 chapitres, zéro bloc ⚖️/👁️/💑 malgré des candidats déjà présents dans le texte brut — a été traité chapitre par chapitre avec une analogie filée propre à chacun (équipe de nuit dans une usine pour le ch.1, plusieurs horloges dans une maison pour le ch.2, quatre alarmes distinctes pour le ch.3, thermostat reprogrammé à chaque âge pour le ch.4, boîte à outils pour le ch.5, tableau de bord de voiture pour le ch.6, pont à deux voies pour le ch.7, chaîne de production pour le ch.8, contrat de sommeil renégocié pour le ch.9, carte routière pour le ch.10, facture invisible pour le ch.11, miroir de fête foraine pour le ch.12, compte joint pour le ch.13, territoire à défendre pour le ch.14, mélodie transmise de culture en culture pour le ch.15, piste d'atterrissage pour le ch.16).

- Total du guide : 17 900 → 24 820 mots (16 chapitres, tous au-dessus de 1 150 mots).
- Blocs ajoutés là où l'audit notait leur absence malgré un sujet pertinent : 👁️ (ch.2 cancer du sein/travail posté, ch.3 sous-diagnostic féminin de l'apnée, ch.8 métier féminisé et dépression, ch.13 écart 86 %/6-7 % des réveils nocturnes), 💑 (ch.4 grossesse, ch.13 charge nocturne), 🗣️ (ch.7, témoignage réel de mères d'enfants autistes trouvé via recherche web et ajouté à `4 - Sources/Le sommeil.md`, en plus du témoignage déjà présent au ch.14).
- Second tour de recherche mené sur le chapitre 7 (sommeil et santé mentale) pour trouver un témoignage vérifiable sur l'autisme et le sommeil, absent de la première version.
- Pipeline complet exécuté (24 836 mots comptés par le script de build, écart mineur accepté avec le compte manuel), aucun lien cassé spécifique à ce guide, README du guide et README racine mis à jour, réciprocité vérifiée avec `4 - Sources/Le sommeil.md`.
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

## Pour Nous — TERMINÉ (25/09/2026)

Les 4 chapitres en réécriture (16, 19, 20, 24) et les 21 chirurgies ont tous été repris. Le guide se lisait en deux moitiés très inégales : les chapitres 1 à 11 (écrits le 6 août) étaient déjà d'excellente facture, avec fil tenu et analogies filées sur 4 d'entre eux (l'alarme mal réglée, le chantier, le chef de projet, le bateau et la vague) — la reprise s'y est limitée à ajouter les analogies manquantes sur les 7 chapitres qui n'en avaient pas, un bloc 👁️ (ch.2), et à combler le plancher de mots. Les chapitres 12 à 25 (écrits le 18 septembre) avaient un défaut plus systématique : zéro analogie sur 14 chapitres, bloc 💑 presque disparu, et un sourçage qui penchait vers des blogs de coaching plutôt que des sources académiques.

- Total du guide : 31 686 → 36 091 mots (25 chapitres, tous au-dessus de 1 100 mots).
- Une analogie filée par chapitre sans sujet préexistant (25 chapitres sur 25 en ont désormais une) : l'équipe de sécurité de la maison (ch.2), la carte routière des itinéraires validés (ch.3), la notice d'appareil (ch.4), le pont suspendu (ch.6), la gare et les trains à horaire (ch.8), la marée qui va et vient (ch.10), le costume hérité jamais retaillé (ch.11), le changement de carburant (ch.12), les trois contrats d'assurance (ch.13), la digue fissurée (ch.14), le test diagnostique (ch.15), les deux plantes dans le même pot (ch.16), le dictionnaire réédité (ch.17), l'atelier qu'on choisit de rouvrir chaque matin (ch.18), le dialecte inventé à deux (ch.19), l'iceberg (ch.20), la membrane semi-perméable (ch.21), le carrefour à deux routes (ch.22), la bande originale (ch.23), les trois plans de maison (ch.24), le phare resté allumé (ch.25).
- Blocs 💑 ajoutés là où l'audit notait leur absence malgré un sujet pertinent : ch.14 (infidélité), ch.17 (double charge historique du mariage), ch.18 (choix quotidien), ch.19 (dialecte du couple), ch.21 (régler la membrane), ch.22 (désaccord sur l'enfant), ch.23 (bande-son du couple). Bloc 👁️ ajouté au ch.2 (vécu du partenaire non traumatisé).
- Second tour de recherche mené sur le chapitre 25 pour trouver des témoignages réels et nommés de couples mariés depuis plusieurs décennies (Sammy et Macie Waller, 75 ans de mariage ; Frank Hoffman, 67 ans ; Betty Mattocks, 51 ans), le projet Cornell cité en 25.1 n'ayant, lui, fourni aucune citation individuelle vérifiable malgré la recherche.
- Pipeline complet exécuté (36 116 mots comptés par le script de build, écart mineur accepté), aucun lien cassé spécifique à ce guide, README du guide et README racine mis à jour, réciprocité vérifiée et complétée avec `4 - Sources/Pour Nous.md` (deux sources manquantes retrouvées et ajoutées : Waldinger, Gottman Long-Term Marriage).
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

## La rencontre — TERMINÉ (25/09/2026)

Les 2 chapitres en réécriture (11, 12) et les 19 chirurgies (dont plusieurs « légères ») ont tous été repris ; les 7 chapitres jugés « rien à faire » par l'audit (3, 4, 6, 15, 20, 22, 25) n'ont pas été touchés. Ce guide était l'un des mieux construits du dépôt sur le fond : fil jamais cassé (sauf le 11), objets bien définis, sources honnêtes. Le défaut le plus systématique était l'absence totale du bloc ⚖️ Nuance sur les 28 chapitres, alors que plusieurs passages l'appelaient presque littéralement (débat Zentner/Schmitt en 23.5, mise en garde déjà écrite en prose en 20.7, terme « consentement » galvaudé au 14).

- Total du guide : 44 591 → 47 762 mots (28 chapitres).
- Blocs ⚖️ ajoutés là où l'audit notait leur absence : ch.9 (légitimité du célibat), ch.14 (consentement), ch.23 (débat Zentner/Schmitt sur les préférences de genre), ch.24 (hiérarchie entre traditions spirituelles).
- Blocs 👁️ ajoutés là où un candidat explicite existait dans le texte brut sans être formalisé : ch.1 (écart de préférences), ch.5 (afflux/silence selon le genre sur les applications), ch.7 (accès inégal aux dispositifs de sécurité), ch.8 (checklist vécue différemment selon le profil), ch.17 (consentement en mariage arrangé), ch.18 (dépendance économique en mobilité internationale), ch.21 (tourisme amoureux), ch.27 (écart de signalement policier selon le genre, déjà chiffré mais jamais formalisé en bloc).
- Blocs 💑 ajoutés : ch.16 (anxiété sociale en couple), ch.17 (couple formé en lieu de culte), ch.19 (jeu vidéo comme rituel de couple), ch.21 (retour à l'ordinaire après une crise), ch.26 (distance après la rencontre).
- Deux réécritures complètes (ch.11, fil recousu autour de l'analogie de la danse improvisée ; ch.12, aparté sur les phéromones reformulé comme partie intégrante de l'analogie du buffet plutôt que hors sujet).
- Second tour de recherche mené sur le chapitre 13 pour trouver des témoignages réels et nommés sur le fait de rencontrer après un veuvage (Amanda Kloots, Abel Keogh, tous deux cités par Yahoo News), absents de la première version malgré un sujet particulièrement propice.
- Pipeline complet exécuté (47 790 mots comptés par le script de build, écart mineur accepté), aucun lien cassé spécifique à ce guide au-delà du bruit habituel des ancres internes (faux positifs systémiques du script de contrôle, déjà connus sur 254 occurrences dans tout le dépôt), README du guide et README racine mis à jour, réciprocité vérifiée et complétée avec `4 - Sources/La rencontre.md`.
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

## IST, dépistage et prévention — TERMINÉ (25/09/2026)

Les 25 chapitres en chirurgie ont tous été repris (aucune réécriture nécessaire, verdict confirmé par l'audit). Ce guide était déjà nettement mieux tenu que le profil de défauts habituel : objets définis, réflexes très majoritairement actifs, honnêteté de sourçage exemplaire (plusieurs chapitres signalent explicitement l'absence de source ou de témoignage plutôt que d'inventer). Les défauts dominants étaient plus légers : onze chapitres sans analogie, des chiffres frappants (374 millions de cas, 417 millions de porteurs du HSV-2, 80 % de la population touchée par le HPV) jamais mis à l'échelle, un chapitre entier (15) sans section Bons réflexes, et cinq témoignages réels déjà présents dans le texte mais jamais marqués de l'emoji 🗣️.

- Total du guide : 18 266 → 19 555 mots (25 chapitres).
- Une analogie filée ajoutée sur les 11 chapitres qui n'en avaient aucune : la loterie du HPV (ch.6), le chantier à plusieurs vitesses de la recherche (ch.10), la trousse à outils (ch.11), les trois portes du dépistage (ch.12), le péage de l'accès (ch.16), les deux angles morts de la prévention (ch.17), l'étiquette qui ne se décolle pas (ch.19), le mauvais tiroir de classement (ch.22), la carte sans route tracée (ch.23), entre autres.
- Section « Bons réflexes » ajoutée au chapitre 15, seul chapitre du guide qui en était totalement dépourvu.
- Emoji 🗣️ Témoignage réel ajouté explicitement sur les cinq chapitres qui portaient déjà un vrai témoignage nommé et sourcé sans le marquer formellement (14, 20, 21, 22, 23).
- Chiffres frappants mis à l'échelle sur la quasi-totalité des chapitres (374 millions de cas comparés à la population des États-Unis, progression de la gonorrhée comparée à un taux de croissance annuel, etc.), liens les plus collés reformulés en phrases courtes.
- Pipeline complet exécuté (19 580 mots comptés par le script de build, écart mineur accepté), aucun lien cassé spécifique à ce guide au-delà du bruit habituel des ancres internes, README du guide et README racine mis à jour. Aucune nouvelle source introduite, réciprocité déjà correcte avec `4 - Sources/IST, dépistage et prévention.md`.
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

### Prochain guide dans l'ordre du tableau maître : Maladie grave et handicap (32 chapitres, priorité haute, mode débit)

## Comment reprendre

Étapes 0 à 5 faites pour Psychologie de la personnalité, Alimentation, Le sommeil, Pour Nous, La rencontre et IST dépistage et prévention. Continuer guide par guide sur les neuf guides restants (Maladie grave et handicap, Massage professionnel, Réseaux sociaux, Les émotions, L'amour, Les nouvelles compositions familiales, Pour Lui, Pour Elle, Questions et communication), dans l'ordre du tableau maître (le plus endommagé en premier selon les mesures de l'audit). Ne pas redemander l'arbitrage entre chaque guide — la consigne de l'utilisateur est de continuer et de signaler seulement à la fin de chaque guide.
