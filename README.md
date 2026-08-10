---
projet: "Comprendre pour tous"
type: "collection"
guides: 9
chapitres: 121
mots: 145496
cree_le: 2026-07-21
mis_a_jour_le: 2026-08-10
licence: "CC BY 4.0"
auteur: "Jordan1618"
depot: "https://github.com/Jordan1618/ComprendrePourTous"
---

# Comprendre pour tous

**Le corps, les émotions et la relation, expliqués pour de vrai.**

Dépôt : https://github.com/Jordan1618/ComprendrePourTous
Site : https://www.comprendrepourtous.fr

## Pourquoi ce projet existe

On entend parler de beaucoup de choses sans jamais savoir ce qu'elles sont vraiment. Endométriose, dépression masculine, IST, papillomavirus, post-partum. On connaît les mots, on en a une idée vague, et cette idée vague suffit à croire qu'on a compris. Elle ne suffit jamais le jour où ça concerne quelqu'un autour de soi.

Ce projet vise un kit de base : de quoi se comprendre soi-même — dans son corps, ses émotions, ses schémas — et comprendre l'autre, pour construire une relation saine plutôt que la subir. Se connaître n'est pas la finalité ; c'est ce qui rend possible de construire sans se cogner aux mêmes murs, seul ou à deux. Aucun niveau de départ supposé : ça marche aussi bien pour combler un vide total que pour corriger un angle mort précis.

J'écris chaque guide dans les deux sens, pour que femmes et hommes puissent s'y reconnaître et évoluer par ce biais — celui sur le cycle féminin s'adresse autant aux femmes qui veulent comprendre leur propre corps qu'aux hommes qui veulent comprendre celui de leur partenaire, et l'inverse pour la santé émotionnelle masculine.

**Rien ici n'est un avis médical individualisé.** C'est dit une fois, et pas répété à chaque page. Pour toute situation concrète, un professionnel de santé reste irremplaçable.

## Les guides

| Guide | Sujet | Chapitres | Contenu | Intégrale |
|---|---|---|---|---|
| [Pour Elle](<1 - Guides/Pour Elle/README.md>) | corps féminin | 26 | Cycle, contraception, pathologies, sexualité, grossesse, profils psychologiques, âges de la vie, couple, limites| [lire](<0 - Guides complets/Pour Elle.md>) |
| [Pour Lui](<1 - Guides/Pour Lui/README.md>) | corps masculin | 21 | Émotions, dépression, corps, cycle, contraception, sexualité, couple, santé long terme| [lire](<0 - Guides complets/Pour Lui.md>) |
| [IST, dépistage et prévention](<1 - Guides/IST, depistage et prevention/README.md>) | commun | 6 | Transmission, chlamydia, gonorrhée, syphilis, herpès, VIH, HPV | [lire](<0 - Guides complets/IST, dépistage et prévention.md>) |
| [Massage professionnel](<1 - Guides/Massage professionnel/README.md>) | commun | 12 | Cadre, techniques, zones du corps, produits, contre-indications | [lire](<0 - Guides complets/Massage professionnel.md>) |
| [Questions et communication](<1 - Guides/Questions et communication/README.md>) | commun | 9 | Ce qu'une question fait, comment elles se classent, celles qui changent une vie | [lire](<0 - Guides complets/Questions et communication.md>) |
| [Les émotions](<1 - Guides/Les emotions/README.md>) | commun | 11 | Fabrication, origines, nommer, décoder, réguler, troubles, parcours de soin, tabous | [lire](<0 - Guides complets/Les émotions.md>) |
| [La rencontre](<1 - Guides/La rencontre/README.md>) | commun | 10 | Attirance, attachement, biais, applications, signaux d'alerte, sécurité | [lire](<0 - Guides complets/La rencontre.md>) |
| [L'amour](<1 - Guides/L amour/README.md>) | commun | 9 | Les trois systèmes, ce qu'on rejoue, scripts culturels, désir, engagement | [lire](<0 - Guides complets/L'amour.md>) |
| [Pour Nous](<1 - Guides/Pour Nous/README.md>) | commun | 12 | Trauma, quotidien et charge, projets de vie, épreuves, deuil, histoire du couple| [lire](<0 - Guides complets/Pour Nous.md>) |

Environ 145 300 mots au total.

Un document à part condense le meilleur de chaque guide, 15 items maximum par guide, pour un premier aperçu avant de plonger dans l'intégrale : [Le meilleur de chaque guide](<0 - Guides complets/Le meilleur de chaque guide.md>). C'est une synthèse tenue à la main, pas un artefact généré par `build-guides-complets.py`.

## Comment c'est classé

Deux axes, portés par le frontmatter de chaque chapitre plutôt que par des dossiers, parce qu'un même sujet relève souvent de plusieurs catégories à la fois.

**Sujet** : corps féminin, corps masculin, ou commun.

**Angle** : physiologie (comment le corps fonctionne), psychologie (comment le fonctionnement mental se construit), prévention (dépistage, protection, risque), pratique (quoi faire concrètement), relation (ce que ça change à deux), repères (chiffres, glossaires, ressources).

Les deux index correspondants sont dans [Par sujet](<3 - Transversal/Par sujet.md>) et [Par angle](<3 - Transversal/Par angle.md>).

## Comment naviguer

```
ComprendrePourTous/
├── README.md                       cette page
├── LICENSE.md                      CC BY 4.0
├── MAINTENANCE.md                  comment faire vivre le projet sans casser la structure
├── build-guides-complets.py        régénère le dossier 0 depuis le dossier 1
├── 0 - Guides complets/            chaque guide en un seul fichier, pour lire d'une traite
├── 1 - Guides/                     les mêmes guides découpés, un fichier par chapitre
├── 2 - Notions/                    notes courtes par concept, avec liens vers les développements
├── 3 - Transversal/                index, glossaire, signaux d'alerte
└── 4 - Sources/                    toutes les sources, avec un lien vers l'original
```

**Les deux formats contiennent exactement le même texte.** Le dossier `1 - Guides` est la source de vérité : c'est là qu'on corrige, chapitre par chapitre. Le dossier `0 - Guides complets` est généré à partir de lui par `build-guides-complets.py`, et ne doit jamais être édité à la main. Une correction faite au mauvais endroit serait écrasée à la génération suivante.

Choisir selon l'usage : le fichier complet pour lire d'une traite, imprimer, ou partager un guide entier ; les chapitres pour chercher un point précis, faire un lien vers lui, ou corriger.

Trois entrées possibles selon ce que vous cherchez :

- **Une question précise** (qu'est-ce que le SMOP, comment se transmet le HPV) : passer par le [glossaire général](<3 - Transversal/Glossaire général.md>) ou par [les notions](<2 - Notions/README.md>).
- **Un sujet entier** : passer par le README du guide concerné, qui liste les chapitres, ou ouvrir directement sa version intégrale dans `0 - Guides complets`.
- **Une situation inquiétante maintenant** : aller directement aux [signaux d'alerte](<3 - Transversal/Signaux d'alerte.md>).

## Comment c'est écrit

Ce projet est écrit et maintenu par une seule personne, Jordan1618, c'est-à-dire moi. Mais je ne suis ni médecin, ni psychologue, ni sexologue, et je préfère le dire tout de suite plutôt que de vous le laisser deviner.

Ma méthode est la suivante : rédaction assistée par intelligence artificielle, avec recherche de sources à chaque affirmation chiffrée, vérification datée, et relecture. Quand une donnée est incertaine ou débattue, je donne une fourchette et je le dis, plutôt que d'inventer une précision qui n'existe pas. Quand une source me manque, je signale l'absence au lieu de la passer sous silence.

Ce que ça vaut : une synthèse honnête, sourcée et lisible, qui va nettement plus loin qu'une fiche grand public. Ce que ça ne vaut pas : l'avis d'un professionnel qui a examiné une personne réelle.

Si vous trouvez une erreur, signalez-la moi : je la corrige. C'est le meilleur service à rendre à ce projet, et vous pouvez me joindre sur [GitHub](https://github.com/Jordan1618/ComprendrePourTous/issues) ou sur [LinkedIn](https://www.linkedin.com/in/jordan-p-77a697228).

## Signaux d'alerte

Certaines situations décrites dans ces guides nécessitent une réaction immédiate, pas une lecture. Elles sont rassemblées sur une page unique : [Signaux d'alerte](<3 - Transversal/Signaux d'alerte.md>).

Deux numéros à connaître, gratuits et disponibles en permanence :

- **15** (SAMU) pour une urgence médicale.
- **3114** pour la prévention du suicide, accessible aussi bien à la personne concernée qu'à un proche inquiet.

## Licence

Textes publiés sous licence Creative Commons **CC BY 4.0**.

Tout le monde peut utiliser, copier, traduire, modifier et rediffuser ce contenu, y compris à des fins commerciales. La seule condition est de citer le projet et son auteur, avec un lien vers la licence, et d'indiquer si des modifications ont été apportées.

C'est un choix assumé : ce projet existe pour être utile, et une licence restrictive limiterait la seule chose qui compte ici, c'est-à-dire que l'information circule. Voir [LICENSE](<LICENSE.md>) pour la mention d'attribution à reprendre.

## Suite

Cette collection est faite pour grandir. Un guide de moins de 8 000 mots reste un fichier unique. Au-delà, il prend son propre dossier et se découpe par chapitre, comme les quatre premiers.

