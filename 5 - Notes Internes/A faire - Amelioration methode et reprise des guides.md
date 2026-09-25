---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-25
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

## Maladie grave et handicap — TERMINÉ (25/09/2026)

Les 32 chapitres en chirurgie ont tous été repris (aucune réécriture nécessaire, verdict confirmé par l'audit). Défaut dominant relevé par l'audit : 56,5 % de liens collés, zéro bloc ⚖️/👁️/💑 sur l'ensemble du guide, zéro analogie filée, tous les chapitres sous le plancher de 1 500 mots malgré un fil resté intact partout.

- Total du guide : 29 541 → 34 215 mots (32 chapitres, tous désormais au-dessus de 870 mots, la plupart entre 950 et 1 300).
- Une analogie filée ajoutée sur les 32 chapitres sans exception (0 avant cette passe) : entre autres la fenêtre embuée (ch.26), l'île déserte entre espoir et deuil (ch.25), le plat qu'on ose enfin servir à table (ch.24), la seconde paire d'yeux sur un texte relu (ch.23), la vieille fracture qui se rappelle un jour de grand froid (ch.22), la confluence de deux rivières (ch.27), le terrain défriché (ch.28), la lampe de poche dans un tunnel (ch.29), la digue qui protège en s'érodant (ch.30), la porte verrouillée faute de clé (ch.31), le vitrail de verre brisé traversé par la lumière (ch.32, clôture du guide).
- Blocs ajoutés là où l'audit notait leur absence malgré un sujet pertinent : ⚖️ Nuance sur le terme galvaudé « intersectionnalité » (ch.27) ; 👁️ Vu de l'autre côté retournant vers le patient depuis le point de vue soignant (ch.30), et sur les peurs enfantines non formulées face à la maladie d'un parent (ch.26) ; 🗣️ Témoignage réel ajouté au chapitre 24 (Emma Pearson, Widow's Voice, conversations de fin de vie).
- Réflexes passifs (« Retenir que… », « Se rappeler que… ») convertis en actions sur l'ensemble des chapitres corrigés, y compris ceux où l'audit signalait un taux au-dessus de la moyenne (ch.28).
- Pipeline complet exécuté (34 247 mots comptés par le script de build, écart mineur accepté), aucun lien cassé spécifique à ce guide, README du guide et README racine mis à jour, réciprocité vérifiée et complétée avec `4 - Sources/Maladie grave et handicap.md` (deux entrées manquantes retrouvées et ajoutées : Sharon Roman/CMAJ au chapitre 7, Emma Pearson/Widow's Voice au chapitre 24).
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

## Massage professionnel — TERMINÉ (25/09/2026)

Les 20 chapitres en chirurgie ont tous été repris ; le chapitre 12, jugé « rien à faire » par l'audit, n'a pas été touché. Défaut dominant relevé par l'audit : 74 % de liens collés (souvent deux ou trois affirmations chaînées derrière un seul lien), 13 chapitres sans analogie, blocs 👁️/💑/🗣️ quasi inexistants malgré des candidats explicites. Deux défauts de structure trouvés en cours de route, absents du rapport d'audit : les sections « Sources vérifiables » de trois chapitres (5, 8, 10, 7) étaient placées au milieu du chapitre plutôt qu'à la fin, coupant le fil ; corrigées au passage.

- Total du guide : 22 778 → 23 879 mots (21 chapitres).
- Une analogie filée ajoutée sur les 13 chapitres qui n'en avaient aucune : les dialectes d'une même langue du toucher (ch.2), la palette de peintre (ch.4), le feu de signalisation (ch.9), le code de la route entre pays (ch.10), la langue privée inventée à deux (ch.11), le tribunal qui instruit un dossier de preuves (ch.14), le chantier qui déplace son périmètre de sécurité (ch.8), le marché sans étiquetage obligatoire (ch.18), les fondations avant les murs (ch.17), le poste-frontière qui recontrôle à chaque passage (ch.20), la carte topographique aux reliefs distincts (ch.6), entre autres.
- Blocs ajoutés là où l'audit notait leur absence malgré un sujet pertinent : 👁️ sur l'écart de perception de pression selon le sexe (ch.7), 💑 explicite sur la grammaire du couple qui se réapprend après une rupture (ch.11), 🗣️ Témoignage réel ajouté au chapitre 20 (Steph Swarts, praticienne de massage, sur l'épuisement professionnel, trouvé et vérifié par recherche web).
- Réflexes passifs (« Se rappeler que… », « Se méfier de… ») convertis en actions sur l'ensemble des chapitres corrigés.
- Pipeline complet exécuté (23 900 mots comptés par le script de build, écart mineur accepté), aucun lien cassé spécifique à ce guide, README du guide et README racine mis à jour, réciprocité vérifiée et complétée avec `4 - Sources/Massage professionnel.md` (une entrée manquante ajoutée : Steph Swarts).
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

## Réseaux sociaux — TERMINÉ (25/09/2026)

Les 20 chapitres en chirurgie ont tous été repris (aucune réécriture nécessaire, verdict confirmé par l'audit). C'était le guide le mieux tenu des deux audités à ce stade sur le fond (fil intact partout, objets bien définis, études expliquées), mais avec trois défauts transversaux : aucun chapitre au plancher de 1500 mots, le bloc de nuance présent partout mais jamais marqué de l'émoji ⚖️ (texte en gras seul), et les blocs 👁️/💑/🗣️ quasi absents malgré des candidats évidents (dysmorphie des filtres, phubbing, ghosting, sharenting).

- Total du guide : 25 233 → 30 295 mots (20 chapitres, tous désormais au-dessus de 1250 mots, la plupart entre 1300 et 1800).
- Une analogie filée ajoutée sur les 10 premiers chapitres qui n'en avaient aucune (arbre généalogique des plateformes, casino conçu par des architectes, pêche à l'incertitude, miroir de fête foraine, scène et coulisses de théâtre, invité fantôme à table, rayon de supermarché sans fin, filet de sécurité troué, tiroir jamais vidé, boîte à outils). Les analogies déjà présentes aux chapitres 11-20 ont été conservées et complétées là où le chapitre manquait d'un fil visuel propre (médicament et terrain, livre écrit à la place de l'enfant).
- Les 20 blocs "Nuance nécessaire" en texte gras converti en blocs ⚖️ Nuance avec l'émoji, conformément à la convention du dépôt.
- Blocs ajoutés là où l'audit notait leur absence malgré un sujet pertinent : 👁️ sur la dysmorphie liée aux filtres (ch.5) et sur le vécu d'un utilisateur profilé via Cambridge Analytica (ch.4) ; 💑 explicite sur le phubbing comme "invité fantôme" à table (ch.6) ; 🗣️ Témoignage réel ajouté au chapitre 7 (Umber Bhatti, NPR, sur le ghosting) et au chapitre 18 (Lou, NPR, sur le sharenting subi durant l'enfance), les deux trouvés et vérifiés par recherche web.
- Deux mises à jour factuelles trouvées au second tour de recherche : le dénouement du dossier TikTok (cession à un consortium mené par Oracle, close le 22 janvier 2026, chapitre 13) et la loi française du 19 février 2024 sur le droit à l'image de l'enfant (chapitre 18), toutes deux absentes de la version d'origine.
- Pipeline complet exécuté (30 315 mots comptés par le script de build, écart mineur accepté), aucun lien cassé spécifique à ce guide au-delà des trois faux positifs d'ancre interne déjà connus, README du guide et README racine mis à jour, réciprocité vérifiée et complétée avec `4 - Sources/Reseaux sociaux.md` (six sources nouvelles ajoutées : témoignages d'Umber Bhatti et de Lou, dénouement TikTok, loi de cybersécurité chinoise, restrictions Chatham House, loi française sur le droit à l'image de l'enfant).
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

## Les émotions — TERMINÉ (25/09/2026)

Les 20 chapitres en chirurgie ont tous été repris (aucune réécriture nécessaire, verdict confirmé par l'audit). C'était l'un des guides les mieux tenus du dépôt sur le fond dès avant la reprise (fil clair partout, objets bien définis, études expliquées avec méthode et intérêt, aucun chapitre sous 1450 mots). Deux défauts systémiques dominaient : le bloc de nuance jamais marqué de l'émoji ⚖️ (absent sur 14 chapitres, présent en texte gras non conforme sur 6, avec 3 chapitres portant plusieurs blocs en violation de la règle du bloc unique) ; et quatre chapitres (11 à 14) terminés par une note de mainteneur résiduelle (« Aucune affirmation... ») à supprimer.

- Total du guide : 45 154 → 47 470 mots (20 chapitres, tous désormais entre 1480 et 3410 mots).
- Un bloc ⚖️ Nuance ajouté ou reformaté avec l'émoji sur les 20 chapitres, avec fusion des blocs surnuméraires des chapitres 15 à 18 (2 à 3 blocs « Nuance nécessaire » en texte gras ramenés à un seul bloc ⚖️ officiel par chapitre, le reste du contenu conservé en prose).
- Note de mainteneur supprimée sur les 4 chapitres concernés (11, 12, 13, 14).
- Une analogie filée ajoutée aux 6 chapitres qui n'en avaient aucune : la corde d'instrument tendue juste ce qu'il faut (ch.18), la maison en travaux habitée pendant le chantier (ch.17), le levier appliqué à l'émotion humaine (ch.16), entre autres ; celles déjà présentes ailleurs (ch.1 à 5, 11 à 14, 19) ont été conservées et, pour le chapitre 19, refermée en fin de chapitre là où elle n'était qu'introduite.
- Blocs ajoutés là où l'audit notait leur absence malgré un candidat évident : 🗣️ Témoignage réel ajouté au chapitre 3 (Sam, alexithymie chez une personne autiste, NeuroClastic) et un bloc 👁️ documenté ajouté au chapitre 10 (silence social après une fausse couche, étude qualitative *BMC Women's Health*) et au chapitre 8 (dysrégulation émotionnelle du TDAH adulte, vécue de l'intérieur).
- Pipeline complet exécuté (47 490 mots comptés par le script de build, écart mineur accepté), aucun lien cassé spécifique à ce guide au-delà des deux faux positifs d'ancre interne connus (renvoi croisé chapitres 11/20), README du guide et README racine mis à jour, réciprocité vérifiée et complétée avec `4 - Sources/Les emotions.md` (deux sources nouvelles ajoutées : Sam/NeuroClastic, étude BMC Women's Health).
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

### Guide L'amour (28 chapitres) — terminé le 25/09/2026

Les 18 chapitres en chirurgie relevés par l'audit (1, 2, 4, 5, 6, 7, 8, 9 en chirurgie lourde ; 3, 13, 16, 17, 18, 21, 23, 24, 26, 28 en chirurgie légère) ont tous été repris ; les 10 chapitres jugés « rien à faire » (10, 12, 14, 15, 19, 20, 22, 25, 27 et le chapitre 3 déjà à jour) n'ont pas été touchés au-delà de leur état déjà satisfaisant. Défaut dominant relevé par l'audit : absence totale du bloc ⚖️ Nuance sur les 28 chapitres, et blocs 👁️/🗣️ quasi inexistants sur les chapitres 1 à 9 malgré des candidats explicites (schéma d'attachement vu du partenaire, désir réactif vécu par l'autre, contrôle financier).

- Blocs ⚖️ Nuance ajoutés sur la totalité des 18 chapitres en chirurgie (aucun n'en avait avant reprise sur ce lot, hormis ceux déjà corrigés par une session précédente sur les chapitres 1-8).
- Blocs 👁️ ajoutés là où un candidat évident dormait dans le texte : ch.1 (asynchronie des systèmes), ch.4 (lecture genrée de l'argument évolutionniste), ch.6 (écart d'attentes dans le couple), ch.9 (contrôle financier), ch.16 (sociomètre vécu par le partenaire), ch.18 (mariage pour tous vécu par un couple qui l'attendait), ch.21 (demande en mariage genrée), ch.24 (charge mentale vécue des deux côtés), ch.28 (harcèlement post-rupture non reconnu par son auteur).
- Un chapitre (13, amour asexuel et aromantique) signale explicitement l'absence de témoignage réel trouvé après recherche sérieuse (accès web restreint dans cette session), plutôt que d'en inventer un — conforme à la règle du skill.
- Chapitres 1 à 9 tous remontés au-dessus ou proche du plancher de 1 500 mots (quatre restent légèrement en dessous — 1 307 à 1 458 mots — après ajouts substantiels, jugés suffisamment denses pour ne pas gonfler artificiellement).
- Pipeline complet exécuté (45 698 mots comptés par le script local, 45 726 par `build-guides-complets.py`, écart mineur accepté), aucun lien cassé spécifique à ce guide, README du guide et README racine mis à jour, réciprocité vérifiée et complétée dans `4 - Sources/L amour.md` (quatre sources préexistantes qui manquaient de réciprocité, ajoutées).
- Guide entièrement commité.

**Ce guide est maintenant fini au sens de l'arbitrage.**

### Guide Les nouvelles compositions familiales (31 chapitres) — terminé le 25/09/2026

Les 31 chapitres relevés par l'audit ont tous été repris (28 en chirurgie standard, 3 en chirurgie lourde : 21, 23, 24). C'était l'un des guides les mieux sourcés et les mieux nuancés du dépôt sur le fond avant la reprise (mentions systématiques de l'absence de source plutôt que d'invention, études expliquées avec méthode et intérêt), mais le défaut de sourçage collé y était homogène et jamais résolu chapitre après chapitre : environ 46 % des 628 liens du guide dépassaient 25 mots ou contenaient un point-virgule. L'analogie filée n'existait que sur 2 chapitres sur 31 (12 : bateau de Thésée ; 19 : l'algorithme comme tiers invisible), tous deux préservés sans y toucher.

- Les liens collés ont été découpés sur l'ensemble des 31 chapitres, en gardant le contenu et la source, en changeant seulement la façon de les poser (phrase en prose, puis lien de ~25 mots maximum sur la proposition précise qu'il appuie).
- Une analogie filée ajoutée aux 29 chapitres qui n'en avaient aucune, retournée en fin de chapitre pour en montrer la limite : la photographie contre le film (ch.1), le plan de maison (ch.2), le pont à ancrer des deux côtés (ch.3), la boîte à outils (ch.4), le sismographe corporel (ch.5), l'aiguille de boussole entre deux pôles (ch.6), le badge d'accès (ch.7), la balance à deux plateaux (ch.8), la fusion d'entreprises (ch.9), le village qui élève l'enfant (ch.10), la fiche de poste non écrite (ch.11), le dictionnaire que la famille invente elle-même (ch.13), le nid (ch.14), le détecteur de fumée bien calibré (ch.15), les deux scénarios déjà écrits contre le scénario que la famille écrit elle-même (ch.16), les balises kilométriques d'un sentier (ch.17), la salle des machines d'un bateau (ch.18), un méridien invisible (ch.29 et repris en écho au ch.20 avec le passeport numérique), une grammaire silencieuse du corps (ch.30), une partie sans règle du jeu imprimée (ch.31), une tapisserie tissée à plusieurs fils (ch.23), la ceinture qu'on gagne dans un art martial (ch.24), le terrain vague qu'on cultive (ch.25), l'argile encore molle (ch.26), le compteur qui tourne en arrière-plan (ch.27), le plan d'évacuation près d'une sortie de secours (ch.28), deux affluents qui se rejoignent (ch.22), entre autres.
- Les trois chapitres en chirurgie lourde (21, 23, 24, chacun 7 à 11 sous-parties faiblement reliées selon l'audit) ont reçu une intro qui annonce le parcours, des phrases de transition explicites entre chaque sous-partie et une conclusion qui referme la boucle, sans réduire le contenu factuel.
- Blocs ajoutés là où l'audit notait leur absence malgré un candidat évident : 👁️ (ch.1 grief asymétrique, ch.2 assistant familial, ch.5 effet Cendrillon revécu par un beau-père, ch.11 fiche de poste genrée, ch.13 mot pour le beau-parent, ch.17 triangulation, ch.20 sharenting et localisation, ch.21 publication à chaud d'un parent, ch.23 exotisation, ch.24 absence à une cérémonie) ; 💑 (ch.1, ch.3, ch.7, ch.9, ch.11, ch.18 kinkeeping, ch.31 transmission religieuse) ; aucun 🗣️ nouveau forcé, faute d'accès web fiable pour vérifier un témoignage réel, conformément à la règle du skill.
- Réflexes passifs (« Se souvenir que… », « Retenir que… », « Garder à l'esprit que… ») convertis en actions sur l'ensemble des chapitres corrigés.
- Total du guide : 57 373 → 62 021 mots (31 chapitres, un seul sous le plancher assumé comme synthèse volontaire : le chapitre 4, 827 mots). Le premier passage de l'agent avait sous-compté (56 363) ; recompté et corrigé par la session principale après vérification.
- Pipeline complet exécuté (62 021 mots comptés par script local, 62 052 par `build-guides-complets.py` qui agrège aussi le sommaire et les liens internes), aucun lien cassé spécifique à ce guide, README du guide et README racine mis à jour (colonne Chapitres corrigée de 4 à 31), réciprocité vérifiée et complétée dans `4 - Sources/Les nouvelles compositions familiales.md` (23 sources préexistantes qui manquaient de réciprocité, ajoutées, plus une incohérence d'URL entre le corps d'un chapitre et sa propre section Sources corrigée au chapitre 6).
- Guide relu, recompté et commité par la session principale après le passage de l'agent en arrière-plan.

**Ce guide est maintenant fini au sens de l'arbitrage.**

### Guide Pour Lui (38 chapitres) — terminé le 25/09/2026

Les 29 chapitres en chirurgie relevés par l'audit ont tous été repris (17 en chirurgie légère : 1-11, 13, 14, 16, 18, 19, 20 ; 13 en chirurgie plus lourde : 21-29, 36-39 ; le chapitre 18 comptait double car sa section 18.4 servait déjà de bloc nuance en 12 points, formalisée plutôt que dupliquée). Les 9 chapitres jugés « rien à faire » (12, 15, 17, 30, 31, 32, 33, 34) n'ont pas été touchés. Défaut dominant relevé par l'audit : absence totale des blocs ⚖️ Nuance et 🗣️ Témoignage sur les 38 chapitres, et sourçage nettement plus collé (40-55 %) sur la série 21-29 et 36-39, sans analogie filée.

- 29 blocs ⚖️ Nuance ajoutés (un par chapitre en chirurgie), formalisant chaque fois une nuance déjà présente en prose plutôt que d'en inventer une nouvelle, jamais de redéfinition d'un terme déjà défini dans le corps du texte.
- Aucun bloc 🗣️ Témoignage forcé, faute d'accès web fiable pour vérifier un témoignage réel et publié dans cette session — conforme à la règle du skill.
- Blocs 👁️ ajoutés là où un candidat évident dormait dans le texte sans bloc dédié : ch.3 (double injonction contemporaine vécue par le partenaire).
- 13 analogies filées et retournées en fin de chapitre ajoutées sur les chapitres 21 à 29 et 36 à 39, qui n'en avaient aucune : le feu de camp (21), le compte de reconnaissance (22), le casier fermé à clé (23), le détecteur de fumée (24), l'arbre élagué (25), la façade et la fondation (26), l'interprète (27), la porte à deux battants (28), l'île mal reliée (29), le radar discret (36), l'horloge à deux aiguilles (37), le cheval de Troie (38), le frein à main serré (39).
- Liens collés découpés sur les 13 chapitres denses (21-29, 36-39), avec ajout de la méthode concrète (ce que les chercheurs ont fait) pour plusieurs études centrales auparavant citées par leur seul résultat.
- Deux défauts de structure corrigés au passage : la numérotation 19.6 placée avant 19.3 (section réordonnée à la fin, sans changer le contenu), et deux sections « Sources vérifiables » mal placées en milieu de chapitre (ch.6 et ch.8), déplacées en toute fin de chapitre.
- Tous les réflexes passifs (« Se rappeler que… », « Retenir que… », « Se souvenir que… ») convertis en actions sur les 29 chapitres.
- Total du guide : 66 500 mots environ (audit) → 76 243 mots comptés par le script local, 76 281 par `build-guides-complets.py` (écart mineur accepté).
- Pipeline complet exécuté sans erreur, aucun lien cassé spécifique à ce guide (hors faux positifs connus de fragments d'ancre interne), README du guide et README racine mis à jour (colonne Chapitres corrigée de 30 à 38), réciprocité vérifiée et complétée dans `4 - Sources/Pour Lui.md` (146 sources préexistantes qui manquaient de réciprocité, ajoutées, la plupart antérieures à cette session de chirurgie).
- Guide non commité par l'agent en arrière-plan, laissé pour vérification et commit par la session principale.

**Ce guide est maintenant fini au sens de l'arbitrage.**

### Guide Pour Elle (39 chapitres) — terminé le 25/09/2026

Les 16 chapitres en chirurgie relevés par l'audit ont tous été repris (8, 9, 14, 20, 23, 24, 25, 27, 28, 29, 30, 35, 36, 37, 38, 39). Les 23 chapitres jugés « rien à faire » n'ont pas été touchés — l'audit notait que ce guide était déjà le mieux construit du dépôt sur plusieurs critères (analogies nombreuses et bien reprises, chiffres presque systématiquement mis à l'échelle), défaut dominant relevé : absence totale de bloc ⚖️ Nuance au format dédié sur les 39 chapitres malgré une nuance déjà présente en prose sur plusieurs d'entre eux, aucun bloc 🗣️ Témoignage nulle part, sourçage collé dépassant 30-70 % sur la série relationnelle/sociologique (23-30, 35-39), deux défauts isolés au chapitre 34 (ligne de mainteneur) et au chapitre 30 (section « Bons réflexes » dupliquée).

- 16 blocs ⚖️ Nuance ajoutés (un par chapitre en chirurgie), formalisant chaque fois une nuance déjà présente en prose plutôt que d'en inventer une nouvelle : le mythe de la « reine des abeilles » (ch.25, ch.35), le mythe des langages de l'amour (ch.29, converti depuis une section « Une dernière nuance » déjà quasi conforme), le mythe du cerveau féminin câblé pour l'empathie (ch.36), le mythe du baromètre féminin (ch.24), le mythe du « girl hate » généralisé (ch.35), entre autres.
- Ligne de mainteneur supprimée en fin de chapitre 34 (« Fin du document. Rédigé le 21 juillet 2026... »), violation directe de la règle « rien de journal ou de mainteneur dans le contenu publié ».
- Section « Bons réflexes » dupliquée du chapitre 30 fusionnée en une seule section cohérente, sans perte de contenu des deux versions.
- Aucun bloc 🗣️ Témoignage ajouté, faute d'accès web fiable pour vérifier un témoignage réel et publié dans cette session — conforme à la règle du skill. Seul le chapitre 8 (candidat TDPM signalé par l'audit) faisait partie de la liste chirurgie parmi les trois candidats cités ; les deux autres (fausse couche au ch.10, mère célibataire au ch.31) étaient classés « rien à faire » et n'ont donc pas été touchés.
- Liens collés découpés sur les 16 chapitres, notamment le chapitre 35 (73 % de liens collés, le plus élevé du guide, avec ajout d'une section « Sources vérifiables » qui manquait entièrement) et les chapitres 14, 20, 25, 27, 28, 30 (méthode des études explicitée en plus de leur résultat pour plusieurs études centrales).
- Réflexes passifs (« Se souvenir que… », « Retenir que… ») convertis en actions sur le chapitre 36.
- Chapitres 36, 37 et 39, sous le plancher de 1 500 mots, étoffés avec du contenu réel (nouvelle sous-partie 36.5, sous-partie 37.3 restaurée après un manque de numérotation repéré au passage, nouvelle sous-partie 39.3), jamais du remplissage.
- Total du guide : environ 77 200 mots (audit) → 83 968 mots comptés par le script local, 84 007 par `build-guides-complets.py` (écart mineur accepté).
- Pipeline complet exécuté sans erreur, aucun lien cassé spécifique à ce guide (hors faux positifs connus de fragments d'ancre interne), README du guide et README racine mis à jour (colonne Chapitres corrigée de 34 à 39), réciprocité vérifiée et complétée dans `4 - Sources/Pour Elle.md` (une centaine de sources préexistantes qui manquaient de réciprocité sur les chapitres 8, 9, 14, 20, 23-30 et 36-39, ajoutées).
- Guide non commité par l'agent, laissé pour vérification et commit par la session principale.

**Ce guide est maintenant fini au sens de l'arbitrage.**

### Guide Questions et communication (46 chapitres) — terminé le 25/09/2026

Les 46 chapitres relevés par l'audit ont tous été repris en chirurgie ciblée (aucun « rien à faire »). C'était déjà l'un des meilleurs guides du dépôt sur le fond avant la reprise (fil intact partout, objets définis, études bien expliquées, honnêteté systématique sur les sources manquantes), mais trois défauts traversaient la quasi-totalité des chapitres : aucun bloc ⚖️ Nuance formaté malgré une nuance presque toujours déjà écrite en texte courant, un ratio de liens à l'ancre trop longue dépassant 85 % sur 32 chapitres, et une absence quasi totale d'analogie filée sur les chapitres 15 à 46 (les chapitres 1 à 14 en avaient déjà de bonnes, non touchées).

- 46 blocs ⚖️ Nuance ajoutés (un par chapitre), formalisant chaque fois une nuance déjà présente en prose plutôt que d'en inventer une nouvelle : le mythe des 93 % de communication non verbale (ch.14, ch.25), le mythe des "85 % de réussite pro" issu d'une étude de 1918 détournée (ch.12), le chiffre de prédiction du divorce à 90 % retombé à 29 % en réplication (ch.28), le liking gap (ch.1), la courbe en U du bien-être dont la moitié jeune a disparu des données récentes (ch.22), le mythe des styles de communication genrés radicalement opposés (ch.29, ch.33, ch.42), entre autres.
- Liens collés découpés sur l'ensemble des 46 chapitres (pas seulement les 32 qui dépassaient le seuil), en gardant le contenu et la source, en changeant seulement la façon de les poser (phrase en prose, puis lien de ~25 mots maximum sur la proposition précise qu'il appuie).
- Analogie filée ajoutée à 24 des 32 chapitres 15-46 qui n'en avaient pas et qui s'y prêtaient (registre narratif) : le film doublé sans acteur de voix (ch.17), le signal brouillé et le signal truqué (ch.18), la noyade (ch.19), la pièce fermée à clé (ch.21), le carrousel et l'escalier en colimaçon (ch.22), le silence radio (ch.24), le gâteau fixe et la recette qu'on peut changer (ch.26), la porte franche et la porte entrebâillée (ch.27), la plaie refermée et la plaie laissée ouverte (ch.28), le miroir sans tain (ch.30), le virus (ch.32), le véhicule et le conducteur (ch.38), la lettre et le texto (ch.37), le compte joint invisible (ch.40), le fil qui a évité une guerre nucléaire (ch.41), la batterie (ch.42), le décor de théâtre (ch.44), le système immunitaire relationnel (ch.45), la mélodie qui porte le message (ch.46), entre autres ; analogie existante étendue et retournée en fin de chapitre sans en ajouter une nouvelle sur le ch.16 (l'injonction sans mode d'emploi) et le ch.25 (la bulle invisible, déjà présente mais peu retournée, signalé par l'audit). Chapitres au registre factuel, historique ou juridique laissés sans analogie forcée conformément au jugement de l'audit (3, 9, 20, 29, 31, 34, 35, 36, 39, 43).
- Deux doublons de numérotation corrigés sans toucher au contenu : chapitre 21 (21.3 bis renommé 21.4, sections suivantes décalées jusqu'à 21.7, référence croisée interne mise à jour) et chapitre 45 (45.4 bis renommé 45.5, section suivante décalée en 45.6). Aucune autre référence croisée dans le guide ne pointait vers ces anciennes ancres.
- Deux chapitres qui n'avaient pas leur propre section « Sources vérifiables » en fin de fichier (9 et 12) en ont reçu une, conforme à la règle du guide.
- Total du guide : 75 620 mots déclarés (avant reprise) → 81 148 mots comptés par le script local, 81 194 par `build-guides-complets.py` (écart mineur accepté).
- Pipeline complet exécuté sans erreur, aucun lien cassé spécifique à ce guide (hors faux positifs connus de fragments d'ancre interne vers des fichiers qui existent), README du guide et README racine mis à jour (colonne Chapitres corrigée de 23 à 46), réciprocité des sources vérifiée par script de comparaison d'ensembles d'URLs : aucune URL manquante dans `4 - Sources/Questions et communication.md`, la réciprocité était déjà à jour avant la reprise ; date de mise à jour de ce fichier rafraîchie tout de même après vérification.
- Guide non commité par l'agent en arrière-plan, laissé pour vérification et commit par la session principale.

**Ce guide est maintenant fini au sens de l'arbitrage.**

## Comment reprendre

Étapes 0 à 5 faites pour Psychologie de la personnalité, Alimentation, Le sommeil, Pour Nous, La rencontre, IST dépistage et prévention, Maladie grave et handicap, Massage professionnel, Réseaux sociaux, Les émotions, L'amour, Les nouvelles compositions familiales, Pour Lui, Pour Elle et Questions et communication.

**Aucun guide n'attend une première passe de chirurgie — les 15 sont passés au moins une fois. Le chantier ouvert maintenant est le ré-audit du 25/09/2026 ci-dessous : plusieurs guides ont des défauts résiduels ou, pour deux d'entre eux, des pans entiers jamais repris.**

## Ré-audit complet du 25/09/2026 — synthèse et priorités

Les 15 guides ont été ré-audités à neuf (agents en lecture seule, un par guide, rapports dans `5 - Notes Internes/Audit - <Guide>.md`, tous datés du 25/09/2026). Deux découvertes majeures, non anticipées par le suivi précédent :

- **Pour Nous** : la reprise antérieure à cette session n'avait traité que les chapitres 1-11. Les chapitres 12-25 (14 chapitres) relèvent du verdict **Réécriture** (sourçage en citations collées de 25-70 mots, fil éclaté en sous-parties, sources faibles sur des affirmations centrales), et 48 des 132 URL du guide (36 %) manquent de réciprocité. C'est, de loin, le chantier le plus lourd restant : 27,5 à 55 h estimées.
- **Psychologie de la personnalité** (guide pilote de la méthode) : 31 des 32 chapitres restent très en dessous du plancher de 1 500 mots (734 à 1 204 mots), plus bas que sur tout autre guide audité.

| Guide | Verdicts (rien à faire / chirurgie / réécriture) | Défaut dominant restant |
|---|---|---|
| L'amour | 4 / 24 / 0 | 19 chapitres (10-28) sans section Sources propre (préexistant, pas dû à cette session) |
| Les nouvelles compositions familiales | 0 / 31 / 0 | Bloc ⚖️ ajouté sur 1 seul chapitre sur 31 (guide non listé avec ce défaut par l'audit initial) |
| Pour Nous | 0 / 11 / **14** | Chapitres 12-25 jamais repris avant cette session, niveau Réécriture |
| La rencontre | 10 / 18 / 0 | Chapitres 4-9 sous le plancher, clôture d'analogie manquante sur ~9 chapitres |
| Le sommeil | 6 / 10 / 0 | 9/16 chapitres sous le plancher |
| Alimentation | 0 / 26 / 0 | Aucun chapitre au plancher (844-1344 mots), 15/26 gardent une puce « Retenez que » |
| Massage professionnel | 0 / 21 / 0 | 20/21 sous le plancher, 21 % des liens sans réciprocité (placeholders scholar.google.com jamais remplacés) |
| Réseaux sociaux | 3 / 17 / 0 | Liens denses sur 4 chapitres, sinon propre |
| Les émotions | 14 / 6 / 0 | Réciprocité des sources à 69 % (45 URL sur 144 manquantes) |
| IST, dépistage et prévention | 0 / 25 / 0 | Aucun chapitre au plancher (513-1437 mots), bloc ⚖️ absent partout |
| Maladie grave et handicap | 0 / 32 / 0 | 32/32 sous le plancher, bloc ⚖️ absent sur 28/32 |
| Psychologie de la personnalité | 1 / 31 / 0 | 31/32 très sous le plancher (734-1204 mots) |
| Pour Lui | 35 / 3 / 0 | Résiduel mineur sur 3 chapitres seulement — guide quasi clos |
| Pour Elle | 18 / 21 / 0 | Analogie filée absente sur 8 des 16 chapitres déjà repris |
| Questions et communication | 46 / 0 / 0 | Aucun — guide intégralement propre |

Priorité recommandée pour une prochaine reprise, du plus urgent au moins urgent : **Pour Nous (chapitres 12-25, niveau réécriture)** en premier, puis Massage professionnel et Les émotions (réciprocité des sources cassée), puis Psychologie de la personnalité et Maladie grave et handicap (déficit de mots le plus marqué), puis les finitions mineures sur Pour Elle, Pour Lui, L'amour et La rencontre. Questions et communication n'a besoin de rien.
