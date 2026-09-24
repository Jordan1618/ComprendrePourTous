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
| 1.1 | Chapitre pilote : refaire entièrement `03 - Le modele Big Five.md` sous les nouvelles règles, faire valider par l'utilisateur | à faire |
| 1.2 | Créer le skill `Redaction2Chapitre` (craft, court, avec le bloc ⚖️ Nuance et la liste de vérification) | à faire, après validation du pilote |
| 1.3 | Alléger `Faiseur2Guide` : ne garder que l'élicitation, le plan de chapitres et la checklist de livraison | à faire |
| 1.4 | Créer le skill `Audit2Guide` (lecture seule, renvoie un rapport de défauts par chapitre) | à faire |
| 1.5 | Ajouter dans `CLAUDE.md` trois lignes de renvoi vers les nouveaux skills | à faire |

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

## Comment reprendre

Commencer par 1.1 (le pilote). Ne pas graver les règles dans les skills avant que l'utilisateur ait validé le pilote — coder une méthode non validée reproduirait la même erreur en plus solennel.
