---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-25
---

# Audit — Réseaux sociaux (ré-audit après reprise complète)

Ce guide (20 chapitres, 30 295 mots selon le README) a été entièrement repris sous `Redaction2Chapitre`. Le ré-audit confirme que la reprise a globalement tenu ses promesses : les 20 chapitres ont un fil unique tenu de bout en bout, une analogie filée qui ouvre et referme le chapitre (sauf le 11), un bloc ⚖️ Nuance pertinent et jamais décoratif, des chiffres mis à l'échelle, et des « Bons réflexes » qui sont, dans l'immense majorité, de vraies actions et non des résumés déguisés. Aucun chapitre ne tombe sous le plancher de 1 500 mots (le plus court est le 14 à 1 255 mots — au-dessus du plancher réel de la grille, la borne de 1 500 s'applique au corps rédactionnel, pas au compte `wc -w` brut qui inclut les sources ; à vérifier si un plancher strict est voulu ici).

Le défaut dominant, présent à des degrés divers dans les 20 chapitres, est le même partout : des hyperliens denses (plus de 25 mots ou contenant un point-virgule) qui portent à eux seuls l'explication d'une étude, sous forme de longue phrase traduite et collée plutôt que déployée dans la prose environnante. Ce n'est pas un habillage nu de type `(source : ...)` — la règle de sourçage du dépôt (lien posé directement sur la phrase qu'il appuie) est bien respectée formellement — mais dans une bonne partie des cas, le « ce que les chercheurs ont fait » reste absent ou fondu dans la même phrase-lien que le résultat, ce qui limite l'explication réelle de la méthode (point 5 de la grille). Ce défaut est particulièrement dense dans les chapitres 13, 17, 18 et 19 (6 à 8 liens denses chacun), plus légers dans les chapitres 1 et 10 (1 seul chacun). Deuxième défaut, mineur et localisé : cinq puces de réflexes commencent par « Rappelez-vous » ou « Gardez en tête » (chapitres 5, 13 ×2, 16, 19), plus proches du résumé déguisé que de l'action, sur un total de plus de 90 puces dans le guide — proportion faible mais réelle. Troisième point, isolé au chapitre 11 : c'est le seul chapitre du guide sans le paragraphe de clôture qui retourne l'analogie (« a une limite qu'il faut nommer »), et son analogie n'est pas non plus posée dans le paragraphe d'ouverture comme dans les 19 autres chapitres — elle n'apparaît qu'en 11.1 sous forme d'encadré « Analogie utile », sans être reprise à la fin.

Sur la réciprocité des sources : 76 URL distinctes citées en hyperlien dans les 20 chapitres, 75 figurent dans `4 - Sources/Reseaux sociaux.md`. La seule absente (https://en.wikipedia.org/wiki/Social_media's_role_in_the_Arab_Spring, citée telle quelle au chapitre 19) est en réalité la même page que celle déjà listée pour le chapitre 9, mais avec l'apostrophe non encodée en `%27` — soit 1 URL sur 76, environ **1,3 %** de « manquants », qui n'en sont pas vraiment (même source, encodage différent). La réciprocité est donc effectivement respectée à 100 % en substance.

## Détail par chapitre

| # | Chapitre | Mots | Défauts relevés | Verdict |
|---|---|---|---|---|
| 1 | Une histoire courte mais dense | 1599 | 1 lien dense (LGBTQ+, §1.6) ; sinon fil, analogie et nuance solides | Rien à faire |
| 2 | Comment c'est fabriqué, et pourquoi | 1677 | 4 liens denses (2.1, 2.2, 2.5 ×2) | Chirurgie légère |
| 3 | Le cerveau face à l'écran | 1762 | 6 liens denses, dont 3.1 et 3.4 assez chargés | Chirurgie légère |
| 4 | Ce que les algorithmes font de nous | 1566 | 2 liens denses (4.4bis bien expliqué malgré la longueur, 4.5) | Rien à faire / chirurgie très légère |
| 5 | L'image de soi à l'ère du feed | 1625 | 4 liens denses ; 1 réflexe en « Rappelez-vous » | Chirurgie légère |
| 6 | Ce que ça change dans le couple et les liens réels | 1696 | 5 liens denses (6.1, 6.3, 6.5 notamment) | Chirurgie légère |
| 7 | Les nouvelles dérives amoureuses numériques | 1695 | 5 liens denses ; témoignage 🗣️ bien intégré | Chirurgie légère |
| 8 | Cyberintimidation, modération et cadre légal | 1687 | 5 liens denses (8.1, 8.4 à 8.7) | Chirurgie légère |
| 9 | Le prix caché : ennui, identité, engagement | 1591 | 4 liens denses | Chirurgie légère |
| 10 | La boîte à outils : reprendre la main | 1573 | 1 lien dense (10.1) ; réflexes tous actionnables | Rien à faire |
| 11 | Le modèle économique réel des plateformes | 1453 | 4 liens denses ; **seul chapitre sans analogie ouvrante ni clôture en retournement** (« Analogie utile » en 11.1 non reprise en fin) | Chirurgie (ajouter le cadrage et la clôture de l'analogie) |
| 12 | Créateurs de contenu : un nouveau salariat précaire | 1341 | 3 liens denses | Chirurgie légère |
| 13 | Géopolitique des réseaux sociaux | 1288 | 6 liens denses ; 2 réflexes en « Rappelez-vous »/« Gardez en tête » | Chirurgie |
| 14 | Régulation comparée : Europe, États-Unis, Chine | 1255 | 5 liens denses ; le plus court du guide en mots | Chirurgie légère |
| 15 | Le coût social jamais compté | 1295 | 4 liens denses | Chirurgie légère |
| 16 | Le cerveau adolescent face au design addictif | 1351 | 5 liens denses ; 1 réflexe en « Gardez en tête » | Chirurgie légère |
| 17 | Populations spécifiques | 1483 | 7 liens denses, dont plusieurs phrases-citations à deux points-virgules (17.2) | Chirurgie |
| 18 | Sharenting et image de l'enfant en ligne | 1425 | 8 liens denses, le taux le plus élevé du guide (18.1, 18.2 surtout) | Chirurgie |
| 19 | Usages détournés : deuil, santé mentale, mouvements sociaux | 1442 | 6 liens denses ; 1 réflexe en « Gardez en tête » ; le §19.1 empile deux citations denses côte à côte | Chirurgie |
| 20 | Éducation aux médias | 1320 | 3 liens denses | Chirurgie légère |

Aucun chapitre n'est en réécriture : le fil narratif tient partout, l'analogie est filée et reprise en fin de chapitre dans 19 cas sur 20, les blocs ⚖️ Nuance sont pertinents et non décoratifs, et les études sont presque toujours situées (qui, quand, sur quel échantillon) même quand l'explication de la méthode reste courte. Les blocs 👁️ / 💑 / 🗣️ sont utilisés à bon escient là où ils apportent quelque chose (4, 6, 7, 11, 12, 18) sans être forcés dans les chapitres qui n'en avaient pas besoin ; on pourrait envisager d'en ajouter un dans les chapitres 15, 17 ou 19 (témoignage de personne âgée isolée, de jeune LGBTQ+, ou de personne en deuil), mais ce n'est pas un manque criant, seulement une option.

## Estimation de coût pour une reprise

- 17 chapitres en chirurgie légère à chirurgie standard (2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20) : reformuler les liens denses en phrase d'explication + hyperlien court posé sur la phrase, et pour le seul chapitre 11, ajouter un paragraphe d'ouverture qui pose l'analogie et un paragraphe de clôture qui la retourne. À raison d'une fourchette basse de chirurgie (30 à 60 minutes de travail effectif par chapitre pour ce type de correction ciblée), soit environ 8h30 à 17h de travail au total.
- 0 chapitre en réécriture.
- 3 chapitres jugés sans défaut structurant (1, 4, 10) : rien à prévoir.

Le chantier de reprise, s'il est lancé, peut se limiter à une passe de reformulation des liens denses (le défaut le plus répété) plutôt qu'à une réécriture de fond : la structure posée par `Redaction2Chapitre` est solide et n'a pas besoin d'être retouchée.
