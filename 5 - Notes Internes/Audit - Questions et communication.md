---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-25
---

# Audit — Questions et communication (ré-audit après reprise complète)

## Synthèse

Ré-audit fait à neuf, sans présumer du résultat, sur l'état actuel des 46 chapitres après la reprise annoncée sous `Redaction2Chapitre` (46/46 en chirurgie ciblée). L'ancien rapport (daté du 24 septembre 2026, qui relevait deux défauts dominants : aucun bloc ⚖️ Nuance formaté, et un sourçage qui devenait « lien collé » à partir du chapitre 10) est remplacé par celui-ci. **Les deux défauts dominants de l'ancien audit ont disparu.**

**Verdict global : 46 chapitres sur 46 en « Rien à faire ».** C'est le résultat le plus rare que ce skill puisse produire, et il tient à la lecture intégrale des 46 chapitres, pas à un sondage.

Ce qui a changé depuis le dernier audit, vérifié chapitre par chapitre :

1. **Bloc ⚖️ Nuance : présent, unique et correctement formaté dans les 46 chapitres**, sous la forme `⚖️ **Nuance : ...**` suivie de 3 puces en gras qui corrigent une fausse évidence plutôt que de redéfinir un terme déjà posé plus haut. Vérifié par comptage automatique (`grep -c "⚖️ \*\*Nuance"` = 1 pour chacun des 46 fichiers) puis relu en contexte sur l'ensemble des chapitres : le bloc nuance à chaque fois, sans exception.
2. **Sourçage : le lien se pose sur la proposition qu'il appuie, jamais en tag nu.** Aucune occurrence de `(source : ...)` détectée. Les ancres de lien restent parfois longues (phrase complète plutôt qu'un segment court) sur une quinzaine de chapitres, mais dans tous les cas relus, l'étude est effectivement expliquée autour du lien (méthode, résultat, portée, limite), ce n'est jamais un résumé collé sans traitement. Ce n'est plus le défaut structurel relevé par l'audit précédent.
3. **Le fil est intact dans les 46 chapitres** : chaque chapitre se lit du haut vers le bas sur le sujet de son titre, aucun n'est une juxtaposition de blocs autonomes.
4. **Les objets centraux sont définis**, pas seulement cités et sourcés (ex. les six familles de questions au ch. 3, les quatre maximes de Grice au ch. 15, la différence injure/diffamation au ch. 41). Aucune liste annoncée puis jamais donnée.
5. **L'analogie est présente dans la quasi-totalité des chapitres**, filée et souvent retournée explicitement en fin de chapitre (requête/dump ch. 1, métronomes ch. 10, film doublé ch. 17, signal brouillé/signal truqué ch. 18, noyade ch. 19, silence radio ch. 24, gâteau ch. 26, porte franche/entrebâillée ch. 27, plaie refermée ch. 28, miroir sans tain ch. 30, virus ch. 32, batterie ch. 42, décor de théâtre ch. 44, système immunitaire relationnel ch. 45, mélodie ch. 46). Quelques chapitres à dominante « repères » (ex. 13, 16, 34, 36) tiennent sans image filée dédiée mais restent structurés et argumentés de bout en bout ; ce n'est pas un défaut au sens du skill, l'analogie n'étant pas obligatoire quand le fil tient autrement.
6. **Les études sont expliquées**, presque systématiquement avec méthode, résultat et portée, jamais un simple résultat balancé (voir par ex. 12.3 sur la négociation salariale, 18.2 sur la détection du mensonge, 32.1 sur la viralité des fake news).
7. **Les chiffres sont amenés par une question et suivis d'une échelle de comparaison** (ex. le coût de l'isolement social au ch. 10, l'écart de salaire au ch. 12, le taux de mortalité au ch. 44).
8. **Les blocs 👁️ 💑 🗣️ sont utilisés à bon escient**, jamais en remplissage systématique : présents là où il y a un écart de perception documentable, un enjeu de couple réel, ou un vécu personnel fort, absents sinon.
9. **Les réflexes sont formulés en actions concrètes.** Sur 46 chapitres, seuls 4 (31, 34, 36, 37) contiennent une puce commençant par « Se rappeler que » — mais dans chaque cas, c'est un item isolé noyé dans une liste de « Bons réflexes » par ailleurs entièrement actionnable, pas un bloc de résumé déguisé. Défaut résiduel mineur, cosmétique, ne justifiant pas à lui seul une chirurgie.

Aucun chapitre ne passe sous le plancher de 1 500 mots (minimum 1 566, README inclus ; minimum de contenu 1 584 au chapitre 35). Aucune trace de contenu journal ou de mainteneur dans le texte publié. Bandeau d'avertissement et pied de page du `README.md` conformes au texte de `MAINTENANCE.md`. Pas de chapitre final « Sources vérifiables » agrégeant le guide — chaque chapitre garde sa propre section de sources en fin de chapitre, l'agrégation complète existant seulement dans `4 - Sources/Questions et communication.md`, conformément à la règle v12.

## Réciprocité des sources

Vérification automatisée : extraction de tous les liens `https://` des 46 chapitres (249 liens au total) et comparaison avec l'ensemble des URL présentes dans `4 - Sources/Questions et communication.md`.

**Résultat : 0 URL manquante, soit 0 % de taux de manque.** Les 249 liens cités dans les chapitres figurent tous, avec le même lien direct, dans le fichier de sources du guide. La réciprocité est parfaite.

## Tableau

| # | Chapitre | Mots | Défauts relevés | Verdict |
|---|---|---|---|---|
| 1 | Ce qu'une question fait vraiment | 2223 | Aucun | Rien à faire |
| 2 | L'anatomie d'une question | 1944 | Aucun | Rien à faire |
| 3 | Les six familles de questions | 1789 | Aucun | Rien à faire |
| 4 | Les questions qui changent une vie | 1730 | Aucun | Rien à faire |
| 5 | Les émotions en jeu | 1726 | Aucun | Rien à faire |
| 6 | Le cadre | 1653 | Aucun | Rien à faire |
| 7 | Les questions difficiles avec les proches | 1668 | Aucun | Rien à faire |
| 8 | Recevoir la réponse | 1667 | Aucun | Rien à faire |
| 9 | Boîte à outils | 1738 | Aucun | Rien à faire |
| 10 | Pourquoi on communique, la science derrière | 1686 | Aucun | Rien à faire |
| 11 | Communiquer pour se développer, soi-même et les autres | 1645 | Aucun | Rien à faire |
| 12 | Motivation, travail, négociation et réussite | 1659 | Aucun | Rien à faire |
| 13 | Une histoire courte, pourquoi la communication est devenue si centrale | 1853 | Pas d'analogie filée dédiée (angle repères) | Rien à faire |
| 14 | Le corps, base de toute communication | 1926 | Aucun | Rien à faire |
| 15 | Transmettre, linguistique, storytelling et l'art de se faire comprendre | 1709 | Aucun | Rien à faire |
| 16 | La communication dans la culture | 1709 | Pas d'analogie filée dédiée (angle repères) | Rien à faire |
| 17 | Bien communiquer par message, les conversations privées à l'ère numérique | 1923 | Aucun | Rien à faire |
| 18 | L'écart entre la formule et l'intention | 1847 | Aucun | Rien à faire |
| 19 | Désamorcer et écouter vraiment | 1700 | Aucun | Rien à faire |
| 20 | Se poser des questions à soi-même, une histoire de l'introspection | 1638 | Aucun | Rien à faire |
| 21 | Les questions qu'on évite, et ce qu'elles révèlent | 1805 | Aucun | Rien à faire |
| 22 | Rumination ou introspection, et les âges des questions | 1806 | Aucun | Rien à faire |
| 23 | Vrai développement personnel ou marketing bien-être | 1646 | Aucun | Rien à faire |
| 24 | Ce que dit le silence | 1761 | Aucun | Rien à faire |
| 25 | Le corps qui parle | 1697 | Aucun | Rien à faire |
| 26 | Rhétorique et négociation | 1852 | Aucun | Rien à faire |
| 27 | Dire non sans rompre | 1797 | Aucun | Rien à faire |
| 28 | Ghosting, stonewalling, et les ruptures de communication | 1774 | Aucun | Rien à faire |
| 29 | Communiquer à travers les cultures | 1602 | Aucun | Rien à faire |
| 30 | Visioconférence et communication asynchrone | 1691 | Aucun | Rien à faire |
| 31 | Le pouvoir de nommer et de faire taire | 1647 | 1 puce « Se rappeler que » sur 5 dans les bons réflexes (31.5) | Rien à faire |
| 32 | Rhétorique politique, propagande et désinformation | 1718 | Aucun | Rien à faire |
| 33 | La communication au travail, du management au feedback | 1635 | Aucun | Rien à faire |
| 34 | Générations et codes de communication | 1646 | 1 puce « Se rappeler que » sur 5 dans les bons réflexes (34.5) | Rien à faire |
| 35 | Médiation, justice et droit de se taire | 1584 | Aucun | Rien à faire |
| 36 | Une histoire de la parole publique | 1703 | 1 puce « Se rappeler que » sur 5 dans les bons réflexes (36.6) ; pas d'analogie filée dédiée (angle repères) | Rien à faire |
| 37 | Ce que coûte une mauvaise communication | 1795 | 1 puce « Se rappeler que » sur 5 dans les bons réflexes (37.5) | Rien à faire |
| 38 | Le cerveau et le corps de la conversation | 2143 | Aucun | Rien à faire |
| 39 | Quand la communication devient un symptôme | 1933 | Aucun | Rien à faire |
| 40 | Ce que la communication coûte et rapporte | 1670 | Aucun | Rien à faire |
| 41 | Le droit et la force de la parole | 1778 | Aucun | Rien à faire |
| 42 | Le corps qu'on ne regarde pas assez | 1850 | Aucun | Rien à faire |
| 43 | Pourquoi on parle, le sens derrière les mots | 1630 | Aucun | Rien à faire |
| 44 | Le décor de la conversation | 1668 | Aucun | Rien à faire |
| 45 | Ce qui peut mal tourner, et comment le voir venir | 1744 | Aucun | Rien à faire |
| 46 | La parole dans l'art et la culture populaire | 1769 | Aucun | Rien à faire |

## Estimation de coût

Zéro chapitre en chirurgie, zéro en réécriture : **coût de reprise nul**. Le seul point à surveiller, s'il devait être traité un jour par souci de perfection plutôt que par nécessité, est cosmétique : reformuler les 4 puces « Se rappeler que » (31.5, 34.5, 36.6, 37.5) en actions, à la marge d'une chirurgie déjà en cours sur un autre chapitre du guide, jamais comme chantier dédié.

## Conclusion

La reprise sous `Redaction2Chapitre` a fonctionné : les deux défauts dominants et quasi universels de l'audit précédent (absence de bloc ⚖️ Nuance formaté, sourçage en lien collé sur plus de 30 chapitres) ont été corrigés sur l'intégralité du guide, sans régression détectée ailleurs sur la grille des neuf points. C'est aujourd'hui l'un des guides les plus propres du dépôt.

---

Retour à [l'accueil de Comprendre pour tous](<../README.md>).
