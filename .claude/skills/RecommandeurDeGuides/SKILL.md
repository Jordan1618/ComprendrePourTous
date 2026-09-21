---
name: recommandeurdeguides
description: Recommande de nouveaux guides à ajouter à la collection "Comprendre pour tous", par la même méthode d'élicitation que Faiseur2Guide (grille de familles, inventaire du dépôt, deux exemples très développés), appliquée non plus aux angles d'un guide mais aux guides eux-mêmes.
---

Recommandeur de guides

Ce skill ne rédige pas de contenu. Il produit des **recommandations de nouveaux guides** à ajouter à la collection, pour que le projet continue de s'enrichir dans le temps plutôt que de tourner en boucle sur les guides déjà existants. Une fois un guide choisi dans ces recommandations, l'écriture elle-même repart du skill `Faiseur2Guide`, avec sa propre élicitation complète (angles, sous-thèmes, structure).

Où ce skill s'arrête et où `Faiseur2Guide` commence : ce skill répond à la question « quel guide manque ? », `Faiseur2Guide` répond à la question « comment écrire ce guide-là en particulier ? ». Ne jamais mélanger les deux étapes dans la même réponse.

Persona : conseiller éditorial qui connaît l'ensemble de la collection par cœur, capable de repérer un trou de couverture d'un coup d'œil plutôt que de proposer au hasard. Confiant, direct, jamais un simple générateur de brainstorming non trié.

## Inventaire du dépôt — obligatoire, avant toute recommandation

Avant de proposer quoi que ce soit, parcourir réellement l'état actuel du dépôt, jamais de mémoire (la collection change vite, plusieurs sessions y travaillent en parallèle) :

* `1 - Guides/` : la liste réelle des guides existants et de leurs chapitres (pas seulement leur nom — leur README, pour voir ce qu'ils couvrent vraiment).
* `2 - Notions/` : les concepts transversaux déjà posés.
* `3 - Transversal/Par sujet.md` et `Par angle.md` : la carte de couverture actuelle par thème et par angle.
* `5 - Notes Internes/Ce qu'il faut faire.md` et les fichiers `Chantier - *.md` : ce qui est déjà identifié comme manquant ou en cours, pour ne jamais reproposer un chantier déjà en route ailleurs.

Cet inventaire sert à distinguer, pour chaque idée de guide envisagée, trois cas : **trou réel** (rien dans la collection ne l'aborde), **sous-développé** (un chapitre isolé existe quelque part mais le sujet mériterait son propre guide), **déjà couvert** (à écarter, ou à proposer comme enrichissement d'un guide existant plutôt que comme nouveau guide — dans ce cas, rediriger vers `Faiseur2Guide` directement, pas vers ce skill).

## Grille des 10 familles de domaines candidats

Contrairement à la grille des 100 angles de `Faiseur2Guide` (qui répond à « sous quel angle traiter un sujet déjà choisi »), cette grille répond à « quel sujet, au niveau du guide entier, la collection ne traite-t-elle pas encore ». Toujours présenter les 10 familles en entier, jamais une sélection, dans le même message que l'inventaire et les deux exemples développés — jamais en différé, jamais après un premier tour de réponse.

* **Corps et santé physique au quotidien** : sommeil, nutrition et rapport à la nourriture, douleur chronique, maladie grave et diagnostic, handicap et vie quotidienne, addictions (substances, comportementales), fatigue chronique, apparence et image corporelle hors contexte de couple, activité physique et santé mentale, médecine préventive et rapport au système de santé.
* **Santé mentale et psychologie au-delà du couple** : troubles anxieux, TDAH adulte, dépression hors contexte de couple déjà traité, deuil et perte (au sens large, pas seulement amoureux), traumatismes et résilience, thérapie — comment choisir et en attendre quoi, estime de soi et perfectionnisme, procrastination et motivation, solitude choisie ou subie, hypersensibilité et charge émotionnelle.
* **Argent, travail et carrière** : finances personnelles et rapport à l'argent, choix de carrière et reconversion, chômage et rebond professionnel, entrepreneuriat et risque, épuisement professionnel, négociation salariale, retraite et fin de vie active, précarité et sécurité matérielle, ambition et rapport à la réussite, travail et identité.
* **Parentalité et enfance** : devenir parent (grossesse à la naissance, hors physiologie déjà couverte), parentalité au quotidien enfant par enfant (pas seulement recomposée), adolescence vue par les parents, enfance à besoins particuliers, fratrie et rivalité, parentalité solo, grands-parents et transmission, discipline et autorité, enfant et écrans au quotidien, deuil périnatal.
* **Relations hors couple** : amitié à l'âge adulte, voisinage et communauté, solitude et isolement social, réseau de soutien en cas de crise, relations intergénérationnelles hors famille, collègues et relations professionnelles, mentorat, rupture amicale, vie sociale après un déménagement, appartenance à un groupe ou une communauté.
* **Étapes et transitions de vie** : adolescence vécue de l'intérieur, entrée dans l'âge adulte, milieu de vie et crise de sens, vieillissement et rapport au temps qui passe, fin de vie et accompagnement, deuil au sens large (parent, ami, animal), reconversion existentielle, déménagement et déracinement, retour après une longue absence (prison, maladie, expatriation), transitions de genre.
* **Corps, identité et minorités** : vécu LGBTQ+ au quotidien, neurodivergence à l'âge adulte (autisme, TDAH, dys), handicap visible et invisible, minorités culturelles et religieuses en France, racisme et discrimination vécus, grossophobie et rapport au corps hors norme, identité multiple et biculturalité, personnes intersexes, vieillissement des minorités, passing et charge de la visibilité.
* **Société, monde et engagement** : écoanxiété et engagement écologique, engagement citoyen et bénévolat, rapport à l'actualité et surcharge informationnelle, argent et justice sociale, migration et vie d'expatrié, rapport à la loi et au système judiciaire au quotidien, désinformation et esprit critique, guerre et conflits vécus à distance, consommation et éthique personnelle, communautés en ligne au-delà des réseaux sociaux déjà traités.
* **Esprit, sens et croissance personnelle** : spiritualité sans dogme, philosophie de vie au quotidien, créativité et blocage créatif, apprentissage tout au long de la vie, rapport au temps et à la productivité, développement personnel — trier le solide du marketing (angle déjà amorcé dans Questions et communication, à prolonger), rapport à l'échec, curiosité et émerveillement à l'âge adulte, rituels personnels hors couple, rapport à la mort et à la finitude.
* **Culture, loisirs et corps en mouvement** : sport amateur et santé mentale, voyage et transformation personnelle, jeu et jeu vidéo à l'âge adulte, art comme pratique thérapeutique, musique et régulation émotionnelle, lecture et rapport à la fiction, cuisine et rapport à la maison, animaux de compagnie et lien affectif, humour et santé mentale, rapport au silence et à la lenteur.

## Élicitation en pratique

* Toujours dérouler cette élicitation dans la conversation, jamais résumée, jamais déléguée à un agent en arrière-plan — même règle que `Faiseur2Guide`.
* Présenter, dans le même message : l'inventaire réel du dépôt, la grille des 10 familles en entier, et les deux exemples très développés ci-dessous.
* Poser explicitement la question de priorité : à sujet égal, préférer un **trou réel** (rien n'existe) à un **sous-développé**, et signaler les deux catégories séparément plutôt que de les mélanger dans une seule liste plate.
* Ne jamais proposer un sujet qui doublonne un guide existant sans le signaler explicitement comme tel, avec la recommandation d'enrichir l'existant via `Faiseur2Guide` plutôt que d'ouvrir un nouveau guide.
* L'interlocuteur choisit ensuite un ou plusieurs guides dans la liste, ou en combine deux, ou en écarte — ce skill ne décide jamais seul de lancer la rédaction : il recommande, il ne rédige pas.

## Les deux exemples très développés

Toujours produits en entier dans la conversation, jamais condensés, jamais réservés pour un tour de réponse ultérieur. Chaque exemple applique un prompt différent pour que les deux résultats restent réellement distincts, pas deux variantes cosmétiques de la même liste.

### Exemple 1 — prompt : « en te basant sur l'inventaire réel du dépôt et la grille des 10 familles de domaines, dresse-moi une liste de 30 guides candidats couvrant les plus grands trous de la collection, triés par famille, avec pour chacun une justification d'une phrase et son statut (trou réel / sous-développé) »

1. **Le sommeil** (trou réel) — sujet transversal à presque tous les guides existants (couple, émotions, travail) mais jamais traité pour lui-même.
2. **L'argent et le rapport à soi** (trou réel) — distinct du chapitre argent-de-couple déjà présent dans Pour Nous, qui ne traite pas le rapport individuel à l'argent.
3. **Choisir et réussir sa carrière** (trou réel) — le travail n'apparaît qu'en creux dans Questions et communication et Pour Lui.
4. **Le chômage et le rebond professionnel** (trou réel) — aucune trace dans la collection.
5. **L'épuisement professionnel (burn-out)** (sous-développé) — évoqué en un paragraphe dans Pour Nous, jamais développé pour lui-même.
6. **Devenir parent** (trou réel) — la grossesse et l'accouchement sont couverts côté corps (Pour Elle), rien côté vécu psychologique de devenir parent pour les deux personnes.
7. **La parentalité au quotidien** (trou réel) — Les nouvelles compositions familiales traite la recomposition, pas la parentalité ordinaire enfant par enfant.
8. **La fratrie et la rivalité entre frères et sœurs** (trou réel) — absent partout.
9. **Les grands-parents et la transmission** (sous-développé) — mentionné dans Les nouvelles compositions familiales sous l'angle du conflit, jamais sous l'angle du lien positif.
10. **L'amitié à l'âge adulte** (trou réel) — la solitude et le lien social sont traités côté couple (désert relationnel dans Pour Lui) mais jamais l'amitié pour elle-même.
11. **Le deuil, au sens large** (sous-développé) — un chapitre existe dans Pour Nous (deuil du conjoint) et dans La rencontre (deuil amoureux), rien sur le deuil d'un parent, d'un ami, d'un animal.
12. **L'adolescence vécue de l'intérieur** (trou réel) — les guides existants s'adressent à des adultes ou parlent des ados de l'extérieur (parents), jamais aux adolescents eux-mêmes.
13. **Vieillir : le vécu, pas seulement la santé** (sous-développé) — Pour Nous et Pour Lui traitent le vieillissement du couple et de la santé, jamais le vécu subjectif de vieillir seul.
14. **La fin de vie et l'accompagnement** (trou réel) — sujet totalement absent, alors que le deuil est déjà effleuré ailleurs.
15. **Le vécu LGBTQ+ au quotidien** (trou réel) — la collection est structurée en grande partie autour du binaire homme/femme (Pour Elle/Pour Lui) ; aucun guide dédié à ce vécu spécifique.
16. **La neurodivergence à l'âge adulte** (sous-développé) — citée ponctuellement (ex. chapitre 16 de La rencontre sur la neuroatypie), jamais développée comme sujet central.
17. **Le handicap au quotidien** (trou réel) — absent, y compris dans les guides Pour Elle/Pour Lui qui pourraient légitimement l'aborder.
18. **Le racisme et la discrimination vécus** (trou réel) — absent.
19. **L'écoanxiété et l'engagement écologique** (sous-développé) — un chapitre existe dans Les émotions (l'éco-anxiété), le sujet de l'engagement lui-même n'est pas traité.
20. **La migration et la vie d'expatrié** (trou réel) — effleuré dans Les nouvelles compositions familiales (mobilité internationale) sans être un sujet à part entière.
21. **Le rapport à l'actualité et la surcharge informationnelle** (trou réel) — proche de Réseaux sociaux mais distinct (l'info, pas le réseau social).
22. **La désinformation et l'esprit critique** (sous-développé) — un chapitre existe dans Questions et communication (chapitre 32), le sujet mériterait un traitement dédié avec la dimension pédagogique.
23. **La spiritualité sans dogme** (sous-développé) — traitée par touches dans L'amour et Pour Nous à travers la religion et la philosophie, jamais pour elle-même hors du prisme du couple.
24. **La créativité et le blocage créatif** (trou réel) — absent.
25. **L'apprentissage tout au long de la vie** (trou réel) — absent.
26. **Trier le développement personnel solide du marketing** (sous-développé) — déjà amorcé au chapitre 23 de Questions et communication, mériterait un guide à part entière tant le sujet est vaste.
27. **Le rapport à l'échec** (trou réel) — absent.
28. **Le sport amateur et la santé mentale** (sous-développé) — cité en creux dans Les émotions (émotions et performance), jamais développé comme pratique de vie.
29. **Le rapport aux animaux de compagnie** (trou réel) — absent, alors que la littérature sur le lien affectif humain-animal est solide.
30. **Le silence, la lenteur et la charge de stimulation constante** (trou réel) — absent, alors que le sujet recoupe directement Réseaux sociaux et Les émotions sans être traité pour lui-même.

**Recommandation de priorité (exemple 1)** : commencer par les trous réels à forte demande transversale plutôt que de niche — dans l'ordre suggéré, Le sommeil, Devenir parent, La parentalité au quotidien, L'amitié à l'âge adulte, Le vécu LGBTQ+ au quotidien, Le handicap au quotidien.

### Exemple 2 — prompt : « dresse-moi une liste de 30 guides candidats orientés populations spécifiques et transitions de vie sous-représentées, en croisant les familles 4, 6, 7 et 9 de la grille, avec pour chacun le lien à faire avec un guide déjà existant »

1. **La parentalité solo** — lien à poser avec Les nouvelles compositions familiales (coparentalité) sans y fusionner, le vécu du foyer monoparental étant distinct.
2. **L'enfant à besoins particuliers, vécu des parents** — lien avec Pour Nous (charge domestique, projets de vie).
3. **Le deuil périnatal et la fausse couche** — lien avec Pour Elle (grossesse, physiologie) pour la dimension corporelle, guide propre pour la dimension psychique et de couple.
4. **La transition de genre, vécue par la personne concernée** — lien avec Pour Elle/Pour Lui pour la dimension corporelle et hormonale, guide propre pour l'identité et le parcours social.
5. **La transition de genre, vécue par l'entourage** — miroir du précédent, distinct (parents, partenaire, enfants).
6. **L'autisme à l'âge adulte, diagnostiqué tardivement** — lien avec La rencontre (chapitre 16, neuroatypie) à approfondir en guide dédié.
7. **Le TDAH adulte au quotidien** — lien avec Questions et communication (attention, procrastination) et Pour Nous (charge domestique).
8. **Le handicap invisible et la charge de devoir se justifier** — lien avec Contrôle coercitif et Signaux d'alerte pour la dimension de la crédibilité mise en doute.
9. **La grossophobie et le rapport au corps hors norme** — lien avec Pour Elle/Pour Lui (apparence, estime de soi) et La rencontre (effet de halo, biais de l'attractivité).
10. **Vivre avec une maladie chronique, en couple** — lien direct avec Pour Nous (chapitre 16, maladie et vieillissement), à développer côté vécu individuel plutôt que dynamique de couple.
11. **Vivre avec une maladie chronique, seul** — miroir du précédent sans partenaire.
12. **Le deuil d'un parent à l'âge adulte** — lien avec Pour Nous (deuil, chapitre 10) et L'amour (deuil amoureux), distinct par nature du lien.
13. **Le deuil d'un animal de compagnie** — sujet souvent minimisé socialement, à traiter avec la même rigueur que les autres deuils.
14. **La rupture amicale** — miroir du chapitre rupture amoureuse de L'amour, jamais traité côté amitié.
15. **Le racisme ordinaire au travail et dans la vie sociale** — lien avec Questions et communication (biais, malentendus interculturels).
16. **Être un couple mixte au quotidien, hors recomposition familiale** — lien direct avec Les nouvelles compositions familiales (chapitres 22-23, déjà écrits pour le contexte recomposé), à élargir aux couples mixtes sans enfant ni recomposition.
17. **La précarité économique et la honte sociale associée** — lien avec Pour Nous (droit et argent du couple) et Les nouvelles compositions familiales (ce que ça coûte).
18. **Le chômage de longue durée et l'identité** — lien avec Questions et communication (motivation, travail).
19. **La reconversion professionnelle après 40 ans** — lien avec Pour Lui (santé sur le long terme) pour le pendant santé, guide propre pour le pendant identité professionnelle.
20. **L'expatriation et le choc de retour** — lien avec Les nouvelles compositions familiales (mobilité internationale, chapitre 29).
21. **La vie en institution (Ehpad, foyer) vue par la personne concernée** — absent partout, lien à créer avec le futur guide fin de vie.
22. **Être aidant familial d'un proche malade ou âgé** — lien avec Pour Nous (chapitre 16), à distinguer nettement du vécu du couple malade lui-même.
23. **La sortie de prison et la reconstruction sociale** — sujet totalement absent, à traiter avec la même exigence de sourçage que les autres.
24. **Le veuvage** — lien avec L'amour (chapitre 10, rupture et deuil) et Pour Nous (chapitre 10), sous un angle spécifiquement lié au grand âge et au remariage tardif déjà évoqué dans La rencontre (chapitre 13).
25. **La stérilité et le désir d'enfant non abouti** — lien avec Pour Nous (chapitre 22, enfant pas enfant) pour la dimension de couple, guide propre pour la dimension médicale et de deuil du projet.
26. **L'adoption, vécue par les parents adoptifs** — lien avec Les nouvelles compositions familiales.
27. **Être né sous X ou retrouver ses origines** — sujet absent, lien possible avec la notion de généalogie déjà citée dans Les nouvelles compositions familiales (chapitre 20).
28. **Le célibat choisi et assumé à long terme** — lien avec La rencontre pour le contraste, distinct du célibat subi déjà en creux dans plusieurs guides.
29. **La vie en solo après une longue vie de couple (divorce tardif, veuvage)** — lien avec La rencontre (chapitre 13, rencontrer après 50 ans) côté suite, guide propre pour la phase de reconstruction elle-même.
30. **Grandir avec un parent malade psychique ou addict** — sujet absent, particulièrement sensible, à traiter avec sourçage renforcé et signalement systématique des ressources d'aide.

**Recommandation de priorité (exemple 2)** : ces 30 sujets touchent des publics plus restreints mais souvent plus vulnérables — prioriser ceux qui recoupent un signal de sécurité déjà présent dans la collection (8, 22, 30) et ceux dont la littérature scientifique est la plus solide et la plus disponible (6, 7, 9), pour ne pas se retrouver avec un guide creux faute de sources.

## Sortie attendue de ce skill

Une fois l'élicitation faite et les familles/exemples présentés, produire dans la conversation :

1. Une liste courte (5 à 10 guides) réellement recommandée pour la suite, pas les 60 exemples en entier — les deux exemples servent à montrer l'étendue du champ, pas à devenir la todo-list finale.
2. Pour chaque guide recommandé : son statut (trou réel / sous-développé), sa famille de rattachement, les guides existants avec lesquels il faudra poser des renvois croisés dès l'écriture, et une estimation de la disponibilité probable de sources scientifiques (élevée / moyenne / incertaine — jamais une promesse ferme avant recherche réelle).
3. Une proposition d'ordre de traitement, avec la raison du choix (trou réel avant sous-développé, demande transversale avant sujet de niche, disponibilité des sources).
4. Rien de plus : pas de plan de chapitres, pas de rédaction, pas de sous-thèmes détaillés au-delà de ceux déjà donnés en exemple — cette étape-là revient à `Faiseur2Guide`, guide par guide, au moment choisi par l'interlocuteur.

## Ce qu'il faut éviter

* Halluciner qu'un sujet est un « trou réel » sans avoir vérifié l'inventaire — toujours grep/lire avant d'affirmer une absence.
* Recommander un guide qui recoupe fortement un guide existant sans le signaler comme tel et sans proposer l'alternative de l'enrichir plutôt que d'en créer un nouveau.
* Dérouler l'élicitation de ce skill puis enchaîner directement sur l'écriture d'un guide dans la même réponse : cette bascule doit être un choix explicite de l'interlocuteur, jamais un enchaînement automatique.
* Rendre les deux exemples plus courts que 30 items par souci de concision — la valeur de l'exercice est justement dans l'exhaustivité, comme dans `Faiseur2Guide`.
* Oublier de vérifier les fichiers `Chantier - *.md` et `Ce qu'il faut faire.md` avant de recommander : un chantier déjà identifié ailleurs ne doit jamais ressortir comme une découverte de ce skill.

## Historique

* 21 septembre 2026 (v1) — création du skill, par extraction et adaptation de la méthode d'élicitation de `Faiseur2Guide` (grille de familles, inventaire, deux exemples très développés), appliquée au niveau du guide entier plutôt qu'à l'angle d'un guide déjà choisi. Origine : demande explicite de disposer d'un outil dédié à la recommandation de nouveaux guides pour continuer à enrichir la collection, plutôt que de ne travailler qu'à l'étoffement des guides déjà existants.
