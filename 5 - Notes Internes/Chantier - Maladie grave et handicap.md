---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-22
---

# Chantier — Maladie grave, handicap et douleur chronique (nouveau guide)

Fichier de suivi, **non publié**, pensé pour qu'une autre session Claude reprenne ce chantier sans accès à cette conversation.

## Demande d'origine, reformulée

Nouveau guide sur la maladie grave, le diagnostic, la douleur chronique et le handicap : prises en charge, accompagnement, santé mentale, handicap (gestion, acceptation, vivre avec, le lourd et le léger), paraplégie, incontinence, fauteuil roulant, rôle du partenaire. Jamais traité comme sujet à part entière dans le dépôt (15 fichiers avec mention tangentielle seulement, surtout *Pour Nous* ch.16 sous l'angle couple uniquement). Élicitation complète déroulée dans la conversation le 22/09/2026 (grille des 10 familles, inventaire confirmant l'absence de doublon, question de recoupement posée, deux exemples de 30 sous-thèmes chacun : clinique/pratique et psychologique/relationnel/sociétal). Feu vert pour tout intégrer.

**Règle permanente rappelée** (déjà en mémoire `doublons-contenu-tolere-sources-notions-non`) : le contenu peut se recouper entre chapitres ou guides, mais les entrées de `4 - Sources/` et les notions de `2 - Notions/` ne doivent jamais être dupliquées — vérifier avant d'ajouter.

## Règles à respecter (rappel)

- Bandeau d'avertissement obligatoire en tête du README (texte exact dans MAINTENANCE.md).
- Chapitre : viser 900-1500 mots, ne jamais gonfler artificiellement.
- Sourçage par sous-partie, lien posé sur l'affirmation, jamais de `(source : ...)` nu, jamais d'URL/DOI fabriqué.
- **Témoignages réels obligatoires** sur les sujets à vécu personnel fort (diagnostic, paraplégie, incontinence, deuil de la vie d'avant, aidant épuisé, fin de vie) — jamais inventés ; chercher sur des associations de patients, articles de presse, forums publics.
- Créer `4 - Sources/Maladie grave et handicap.md` dès le premier chapitre, réciprocité obligatoire.
- Vérifier `2 - Notions/README.md` avant de créer une notion (aucune notion handicap/maladie existante à ce jour).
- Pas de chapitre final « Sources vérifiables » agrégeant tout le guide.
- Neutralité de genre du lecteur, nuance systématique — sujet sensible, éviter tout ton misérabiliste ou au contraire minimisant.
- `angle:` du frontmatter DOIT utiliser la taxonomie réelle du site (physiologie/psychologie/prévention/pratique/relation/repères/société) dès la rédaction, jamais les labels bruts de la grille des 100 angles.
- Ajouter "Maladie grave et handicap" aux listes `DOSSIERS`/`ORDRE_GUIDES` codées en dur dans `build-guides-complets.py` et `build-index.py` **avant** de lancer le pipeline.
- Renvois croisés vers Pour Nous (ch.16, couple/maladie), Les émotions, Pour Elle/Pour Lui — pas de réécriture de leurs chapitres.
- Après la dernière modification : build complet + contrôle des liens cassés.
- Ajouter le guide au README racine (tableau `## Les guides`, frontmatter `guides:`).

## Plan de chapitres retenu (fusion des deux exemples de 30 sous-thèmes)

| # | Titre | Sous-thèmes des exemples couverts | Statut |
|---|---|---|---|
| 1 | Recevoir un diagnostic : le choc et ses phases | Ex1 : 1, Ex2 : 1 | fait (1 267 mots) |
| 2 | Le parcours de soin et les démarches en France | Ex1 : 2 | fait (810 mots) |
| 3 | La douleur chronique : mécanismes et traitements | Ex1 : 3, 4 | fait (946 mots) |
| 4 | Maladies invisibles | Ex1 : 5 | fait (841 mots) |
| 5 | Paraplégie, tétraplégie et rééducation | Ex1 : 6, 7 | fait (978 mots) |
| 6 | Le fauteuil roulant : choix et autonomie | Ex1 : 8 | fait (879 mots) |
| 7 | L'incontinence : gestion et tabou | Ex1 : 9 | fait (915 mots) |
| 8 | Deuil de la vie d'avant et reconstruction identitaire | Ex2 : 2, 3 | fait (914 mots) |
| 9 | L'acceptation et la résilience : ce que la recherche en dit | Ex2 : 4, 10 | fait (912 mots) |
| 10 | Validisme et modèle social du handicap (inclut validisme intériorisé) | Ex2 : 5, 6, 21 | fait (1 147 mots) |
| 11 | Histoire et représentation culturelle du handicap | Ex2 : 7, 8 | fait (951 mots) |
| 12 | Le langage du handicap | Ex2 : 9 | fait (869 mots) |
| 13 | Sexualité, désir et handicap | Ex1 : 10, Ex2 : 12 | fait (838 mots) |
| 14 | Le couple face à la maladie : pouvoir, charge, rupture | Ex2 : 11, 13, 14, 15 | fait (1 058 mots) |
| 15 | La solitude du malade et l'entourage | Ex2 : 16, 17 | fait (809 mots) |
| 16 | Le rôle de l'aidant familial et du partenaire | Ex1 : 11, 12 | fait (890 mots) |
| 17 | Les professionnels du parcours de soin | Ex1 : 13 | fait (854 mots) |
| 18 | Santé mentale du malade chronique | Ex2 : 18, 19 | fait (846 mots) |
| 19 | Logement, accessibilité, aides techniques | Ex1 : 14, 24 | fait (873 mots) |
| 20 | Emploi, droits et aides financières | Ex1 : 15, 16, Ex2 : 25 | fait (1 086 mots) |
| 21 | Fatigue chronique et gestion de l'énergie | Ex1 : 17 | fait (918 mots) |
| 22 | Cancer, rémission et après | Ex1 : 18, 26 | fait (793 mots) |
| 23 | Errance diagnostique et erreurs médicales | Ex1 : 25 | fait (854 mots) |
| 24 | Soins palliatifs et fin de vie | Ex1 : 19, Ex2 : 28 | fait (926 mots) |
| 25 | Rechutes et incertitude médicale au long cours | Ex1 : 20 | fait (951 mots) |
| 26 | Enfants et parentalité face à la maladie ou au handicap | Ex1 : 21, 22 | fait (966 mots) |
| 27 | Intersectionnalité (handicap × genre, précarité, racisme, LGBTQ+) | Ex2 : 22 | fait (1 048 mots) |
| 28 | Droits, luttes et associations de patients | Ex1 : 28, Ex2 : 23, 29 | fait (975 mots) |
| 29 | Spiritualité, sens et humour comme stratégies de survie | Ex2 : 20, 26 | fait (902 mots) |
| 30 | Le vécu des soignants | Ex2 : 27 | fait (813 mots) |
| 31 | Sport adapté, voyager et loisirs accessibles | Ex1 : 23, Ex2 : 24 | fait (948 mots) |
| 32 | Vivre léger malgré la gravité | Ex2 : 30 | fait (764 mots) |

32 chapitres au total. Fusionner ou scinder en cours de rédaction si un chapitre s'avère trop mince ou trop chargé (déjà arrivé sur d'autres chantiers).

## Fichiers concernés

- `1 - Guides/Maladie grave et handicap/01...` à `32...` + `README.md`
- `4 - Sources/Maladie grave et handicap.md` (nouveau)
- `2 - Notions/` : vérifier avant toute création
- `README.md` racine : ajouter la ligne du guide au tableau, incrémenter `guides:`
- `build-guides-complets.py` et `build-index.py` : ajouter le guide aux listes codées en dur
- `3 - Transversal/` régénéré par script, ne pas éditer à la main

## État : chantier terminé (23/09/2026)

Les 32 chapitres sont rédigés (29 541 mots), `4 - Sources/Maladie grave et handicap.md` complet avec réciprocité vérifiée, README du guide rempli (tableau des chapitres, frontmatter `chapitres: 32` / `mots: 29541`), guide ajouté au README racine (`## Les guides`, `guides: 14`). Aucune notion nouvelle créée (aucune notion handicap/maladie pertinente n'existait, et aucun sujet de ce guide ne justifiait d'en créer une nouvelle plutôt qu'un simple renvoi croisé). Cross-lien ajouté vers *Pour Nous* (ch. 16, couple/maladie au long cours) et *Les émotions* dans le README ; plusieurs renvois internes tissés entre les 32 chapitres eux-mêmes (validisme ↔ langage ↔ intersectionnalité, aidant ↔ couple ↔ incertitude, etc.).

**Témoignages réels intégrés** (jamais inventés, conformément à la règle du skill) : errance diagnostique du lupus (ch.1), Joy Selak sur la maladie invisible (ch.4), April Ballentine sur la paraplégie (ch.5), un utilisateur de fauteuil électrique (ch.6), deux témoignages de scanxiety en rémission de cancer (ch.22), une participante à l'étude sur le voyage accessible à Bodrum (ch.31), la citation de Jennifer Keelan au Capitol Crawl (ch.28).

`build-guides-complets.py` et `build-index.py` avaient déjà été corrigés pour inclure le guide avant le lancement du pipeline (leçon retenue des chantiers « Le sommeil » et « Alimentation »). Tous les frontmatters `angle:` utilisent directement la taxonomie du site (physiologie/psychologie/prévention/pratique/relation/repères/société) dès la rédaction. Pipeline complet relancé (guides complets, index, site) et contrôle des liens cassés effectué : aucun lien cassé propre à ce guide.

Reste à faire, hors scope de ce chantier : rien d'identifié pour l'instant. Ne pas committer/pousser sans demande explicite.

## Comment reprendre (si chantier repris avant complétion)

Coller ce fichier, reprendre au premier chapitre « à faire ». Marquer chaque chapitre fait avec son nombre de mots avant de passer au suivant. Vérifier `2 - Notions/README.md` avant toute création de notion. Chercher un témoignage réel à chaque chapitre marqué comme sensible dans le tableau ci-dessus.
