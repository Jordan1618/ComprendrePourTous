---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-23
---

# Chantier — Psychologie de la personnalité (nouveau guide)

Fichier de suivi, **non publié**, pensé pour qu'une autre session Claude reprenne ce chantier sans accès à cette conversation.

## Demande d'origine, reformulée

Nouveau guide sur les différents types de psychologie/personnalité : façons d'être, points forts et faibles, origines, conséquences sur le travail, la santé, la vie quotidienne, la famille — estime de soi, perfectionnisme, conformisme, anticonformisme, juste milieu, solitude choisie ou subie, et l'impact de tous ces sujets sur les relations hommes-femmes (amicales ou de séduction). Jamais traité comme sujet à part entière dans le dépôt (35 fichiers en mention tangentielle : styles d'attachement dans *La rencontre*, profils féminins/masculins cadrés uniquement pour la séduction dans *Pour Elle*/*Pour Lui*). Élicitation complète déroulée dans la conversation le 23/09/2026 (grille des 10 familles, inventaire confirmant l'absence de doublon hormis la notion `Style d'attachement` à réutiliser, question de recoupement posée, deux exemples de 30 sous-thèmes chacun : scientifique/clinique et socioculturel/relationnel). Feu vert pour tout intégrer.

**Règle permanente rappelée** (déjà en mémoire `doublons-contenu-tolere-sources-notions-non`) : le contenu peut se recouper entre chapitres ou guides, mais les entrées de `4 - Sources/` et les notions de `2 - Notions/` ne doivent jamais être dupliquées — vérifier avant d'ajouter. La notion `Style d'attachement` existe déjà (développée dans *La rencontre* ch.02) : la réutiliser par renvoi, ne jamais la redire.

## Règles à respecter (rappel)

- Bandeau d'avertissement obligatoire en tête du README (texte exact dans MAINTENANCE.md).
- Chapitre : viser 800-1300 mots, ne jamais gonfler artificiellement.
- Sourçage par sous-partie, lien posé sur l'affirmation, jamais de `(source : ...)` nu, jamais d'URL/DOI fabriqué.
- Jamais présenter un test de personnalité non scientifiquement validé (MBTI, astrologie, etc.) comme fiable — nuance obligatoire.
- Créer `4 - Sources/Psychologie de la personnalité.md` dès le premier chapitre, réciprocité obligatoire.
- Vérifier `2 - Notions/README.md` avant de créer une notion — réutiliser `Style d'attachement` par renvoi.
- Pas de chapitre final « Sources vérifiables » agrégeant tout le guide.
- Neutralité de genre du lecteur, nuance systématique — en particulier sur les stéréotypes hommes/femmes de personnalité.
- `angle:` du frontmatter DOIT utiliser la taxonomie réelle du site (physiologie/psychologie/prévention/pratique/relation/repères/société) dès la rédaction.
- Ajouter "Psychologie de la personnalité" aux listes `DOSSIERS`/`ORDRE_GUIDES` codées en dur dans `build-guides-complets.py` et `build-index.py` **avant** de lancer le pipeline.
- Renvois croisés vers La rencontre (styles d'attachement), Pour Elle/Pour Lui (profils), Réseaux sociaux (image de soi) — pas de réécriture de leurs chapitres.
- Après la dernière modification : build complet + contrôle des liens cassés.
- Ajouter le guide au README racine (tableau `## Les guides`, frontmatter `guides:`).

## Plan de chapitres retenu (fusion des deux exemples de 30 sous-thèmes)

| # | Titre | Sous-thèmes des exemples couverts | Statut |
|---|---|---|---|
| 1 | Qu'est-ce que la personnalité : définition, stabilité et changement | Ex1 : 1 | fait (764 mots) |
| 2 | Histoire des typologies : des humeurs d'Hippocrate aux pseudosciences modernes | Ex2 : 1, 2, 3 | fait (1 144 mots) |
| 3 | Le modèle Big Five | Ex1 : 2 | fait (920 mots) |
| 4 | Les tests populaires passés au crible : MBTI et autres | Ex1 : 3 | fait (790 mots) |
| 5 | Introversion et extraversion | Ex1 : 4 | fait (807 mots) |
| 6 | Origines génétiques et environnementales de la personnalité | Ex1 : 9, 10, 11 | fait (866 mots) |
| 7 | Le perfectionnisme | Ex1 : 5, Ex2 : 7 | fait (996 mots) |
| 8 | L'estime de soi | Ex1 : 6, Ex2 : 8 | fait (967 mots) |
| 9 | Narcissisme et troubles de la personnalité | Ex1 : 7, 8 | fait (908 mots) |
| 10 | Le conformisme | Ex1 : 14, Ex2 : 5 | fait (1 013 mots) |
| 11 | L'anticonformisme | Ex1 : 15, Ex2 : 6 | fait (955 mots) |
| 12 | Le juste milieu : la modération comme compétence | Ex1 : 16 | fait (862 mots) |
| 13 | Solitude choisie, solitude subie, célibat volontaire | Ex1 : 17, 18, Ex2 : 14, 15, 16 | fait (978 mots) |
| 14 | Personnalité, santé physique et longévité | Ex1 : 12, 13 | fait (751 mots) |
| 15 | Personnalité et monde du travail : profils, burn-out, leadership | Ex1 : 19, 20, 21, Ex2 : 20, 21 | fait (890 mots) |
| 16 | Les tests de personnalité en entreprise : validité et éthique | Ex1 : 28 | fait (756 mots) |
| 17 | Personnalité à travers les cultures | Ex2 : 4 | fait (826 mots) |
| 18 | Personnalité et genre : stéréotypes sur les hommes et les femmes | Ex2 : 11, 12, 13 | fait (783 mots) |
| 19 | Différences de personnalité perçues entre hommes et femmes : mythe et réalité | Ex1 : 24 | fait (830 mots) |
| 20 | Personnalité et couple : compatibilité, complémentarité | Ex1 : 22, Ex2 : 19 | fait (866 mots) |
| 21 | Personnalité et amitié, y compris amitiés hommes-femmes | Ex1 : 23, Ex2 : 17 | fait (895 mots) |
| 22 | Personnalité et séduction : perçue vs réelle | Ex1 : 25, Ex2 : 18 | fait (883 mots) |
| 23 | Transmission familiale des traits, rôle de la fratrie | Ex2 : 9, 10 | fait (850 mots) |
| 24 | Famille, enfants et tempérament | Ex2 : 22, 23 | fait (842 mots) |
| 25 | La résilience comme trait de personnalité | Ex1 : 26 | fait (720 mots) |
| 26 | Le changement de personnalité à l'âge adulte | Ex1 : 27 | fait (705 mots) |
| 27 | Les personnalités « toxiques » : un terme galvaudé | Ex2 : 25 | fait (712 mots) |
| 28 | Le masque social : la persona | Ex2 : 26 | fait (896 mots) |
| 29 | Personnalité dans la fiction et la culture populaire | Ex2 : 24 | fait (780 mots) |
| 30 | Réseaux sociaux et polarisation des personnalités affichées | Ex2 : 28 | fait (816 mots) |
| 31 | L'authenticité : valeur culturelle récente | Ex1 : 29, Ex2 : 27 | fait (685 mots) |
| 32 | S'accepter, accepter l'autre | Ex1 : 30, Ex2 : 29, 30 | fait (821 mots) |

32 chapitres au total. Fusionner ou scinder en cours de rédaction si un chapitre s'avère trop mince ou trop chargé.

## Fichiers concernés

- `1 - Guides/Psychologie de la personnalité/01...` à `32...` + `README.md`
- `4 - Sources/Psychologie de la personnalité.md` (nouveau)
- `2 - Notions/` : réutiliser `Style d'attachement` par renvoi, vérifier avant toute autre création
- `README.md` racine : ajouter la ligne du guide au tableau, incrémenter `guides:`
- `build-guides-complets.py` et `build-index.py` : ajouter le guide aux listes codées en dur
- `3 - Transversal/` régénéré par script, ne pas éditer à la main

## Comment reprendre

Coller ce fichier, reprendre au premier chapitre « à faire ». Marquer chaque chapitre fait avec son nombre de mots avant de passer au suivant. Vérifier `2 - Notions/README.md` avant toute création de notion.

## État : chantier terminé (23/09/2026)

32 chapitres écrits, 27 277 mots. README du guide rempli avec le tableau complet des chapitres. `4 - Sources/Psychologie de la personnalité.md` complété avec une table par chapitre, réciprocité vérifiée. Notion `Style d'attachement` enrichie d'un renvoi vers le chapitre 20 plutôt que redite. `build-guides-complets.py` et `build-index.py` mis à jour, pipeline complet exécuté (`build-guides-complets.py` → `build-index.py` → `build.py`). Contrôle des liens cassés effectué : un seul lien concernait ce guide (accent manquant dans le lien vers l'intégrale du README racine), corrigé. README racine mis à jour (`guides: 15`, `chapitres: 313`, `mots: 411869`, nouvelle ligne de tableau).

Bug retrouvé et corrigé en cours de route : le chapitre 9 utilisait `angle: "psychiatrique"`, une valeur de la grille des 100 angles du skill, invalide dans la taxonomie réelle du site — corrigé en `psychologie` avant le build final.
