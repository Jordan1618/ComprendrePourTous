---
title: "Comprendre pour tous"
weight: 0
type: "collection"
mis_a_jour_le: "2026-08-05"
licence: "CC BY 4.0"
---

# Comprendre pour tous

**Le corps, les émotions et la relation, expliqués pour de vrai.**

Dépôt : https://github.com/Jordan1618/ComprendrePourTous
Site : https://www.comprendrepourtous.fr

## Pourquoi ce projet existe

On entend parler de beaucoup de choses sans jamais savoir ce qu'elles sont vraiment. Endométriose, dépression masculine, IST, papillomavirus, post-partum. On connaît les mots, on en a une idée vague, et cette idée vague suffit à croire qu'on a compris. Elle ne suffit jamais le jour où ça concerne quelqu'un autour de soi.

L'objectif de cette collection est éducatif : comprendre pour de vrai, avec des mécanismes expliqués plutôt que des définitions, des chiffres sourcés et datés plutôt que des impressions, et ce que ça change concrètement dans une relation plutôt que de la théorie.

Chaque guide est écrit dans les deux sens. Celui sur le cycle féminin s'adresse autant aux femmes qui veulent comprendre leur propre corps qu'aux hommes qui veulent comprendre celui de leur partenaire. Celui sur la santé émotionnelle masculine fait exactement l'inverse. C'est la colonne vertébrale du projet : comprendre le corps et le fonctionnement de l'autre, ce n'est pas de la curiosité, c'est la condition pour s'y intéresser autrement qu'en surface.

**Rien ici n'est un avis médical individualisé.** C'est dit une fois, et pas répété à chaque page. Pour toute situation concrète, un professionnel de santé reste irremplaçable.

## Comment c'est classé

Deux axes, portés par le frontmatter de chaque chapitre plutôt que par des dossiers, parce qu'un même sujet relève souvent de plusieurs catégories à la fois.

**Sujet** : corps féminin, corps masculin, ou commun.

**Angle** : physiologie (comment le corps fonctionne), psychologie (comment le fonctionnement mental se construit), prévention (dépistage, protection, risque), pratique (quoi faire concrètement), relation (ce que ça change à deux), repères (chiffres, glossaires, ressources).

Les deux index correspondants sont dans [Par sujet]({{< ref "/transversal/par-sujet.md" >}}) et [Par angle]({{< ref "/transversal/par-angle.md" >}}).

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
└── 3 - Transversal/                index, glossaire, signaux d'alerte, sources
```

**Les deux formats contiennent exactement le même texte.** Le dossier `1 - Guides` est la source de vérité : c'est là qu'on corrige, chapitre par chapitre. Le dossier `0 - Guides complets` est généré à partir de lui par `build-guides-complets.py`, et ne doit jamais être édité à la main. Une correction faite au mauvais endroit serait écrasée à la génération suivante.

Choisir selon l'usage : le fichier complet pour lire d'une traite, imprimer, ou partager un guide entier ; les chapitres pour chercher un point précis, faire un lien vers lui, ou corriger.

Trois entrées possibles selon ce que vous cherchez :

- **Une question précise** (qu'est-ce que le SMOP, comment se transmet le HPV) : passer par le [glossaire général]({{< ref "/transversal/glossaire-general.md" >}}) ou par [les notions]({{< ref "/notions/_index.md" >}}).
- **Un sujet entier** : passer par le README du guide concerné, qui liste les chapitres, ou ouvrir directement sa version intégrale dans `0 - Guides complets`.
- **Une situation inquiétante maintenant** : aller directement aux [signaux d'alerte]({{< ref "/transversal/signaux-d-alerte.md" >}}).

## Comment c'est écrit

Ce projet est écrit et maintenu par une seule personne, Jordan1618, qui n'est ni médecin, ni psychologue, ni sexologue. C'est important de le dire au début plutôt que de le laisser deviner.

La méthode est la suivante : rédaction assistée par intelligence artificielle, avec recherche de sources à chaque affirmation chiffrée, vérification datée, et relecture. Quand une donnée est incertaine ou débattue, le texte donne une fourchette et le dit, plutôt que d'inventer une précision qui n'existe pas. Quand une source manque, l'absence est signalée.

Ce que ça vaut : une synthèse honnête, sourcée et lisible, qui va nettement plus loin qu'une fiche grand public. Ce que ça ne vaut pas : l'avis d'un professionnel qui a examiné une personne réelle.

Toute erreur signalée est corrigée. C'est le meilleur service à rendre au projet.

## Signaux d'alerte

Certaines situations décrites dans ces guides nécessitent une réaction immédiate, pas une lecture. Elles sont rassemblées sur une page unique : [Signaux d'alerte]({{< ref "/transversal/signaux-d-alerte.md" >}}).

Deux numéros à connaître, gratuits et disponibles en permanence :

- **15** (SAMU) pour une urgence médicale.
- **3114** pour la prévention du suicide, accessible aussi bien à la personne concernée qu'à un proche inquiet.

## Licence

Textes publiés sous licence Creative Commons **CC BY 4.0**.

Tout le monde peut utiliser, copier, traduire, modifier et rediffuser ce contenu, y compris à des fins commerciales. La seule condition est de citer le projet et son auteur, avec un lien vers la licence, et d'indiquer si des modifications ont été apportées.

C'est un choix assumé : ce projet existe pour être utile, et une licence restrictive limiterait la seule chose qui compte ici, c'est-à-dire que l'information circule. Voir [LICENSE](https://github.com/Jordan1618/ComprendrePourTous/blob/main/LICENSE.md) pour la mention d'attribution à reprendre.

## Suite

Cette collection est faite pour grandir. Un guide de moins de 8 000 mots reste un fichier unique. Au-delà, il prend son propre dossier et se découpe par chapitre, comme les quatre premiers.

Dernière mise à jour de cette page : 5 août 2026.
