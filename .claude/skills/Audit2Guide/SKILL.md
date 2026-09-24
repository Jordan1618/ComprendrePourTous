---
name: audit2guide
description: Auditer un ou plusieurs guides existants en lecture seule et produire un rapport de défauts par chapitre avec un verdict.
---

Auditer un guide sans y toucher

Ce skill lit, il ne corrige jamais. Sa sortie est un rapport dans `5 - Notes Internes/`, qui sert ensuite à décider quoi reprendre et comment. Toute correction passe par `Redaction2Chapitre`, dans un second temps.

**Lecture seule, sans exception.** Aucune modification d'un fichier de `1 - Guides/`, `2 - Notions/`, `3 - Transversal/` ou `4 - Sources/` pendant un audit. Un audit qui corrige au passage rend son propre rapport faux.

## Invocation

* `/Audit2Guide Le sommeil` : un guide.
* `/Audit2Guide Le sommeil, Alimentation, Maladie grave et handicap` : plusieurs guides, un agent en lecture seule par guide, lancés en parallèle. Chaque agent renvoie un rapport court. C'est le seul usage des agents qui économise du contexte au lieu d'en coûter, parce que le gros de la lecture ne remonte jamais dans la fenêtre principale.

Trois à quatre guides par commande au maximum. Au-delà, les rapports arrivent trop nombreux pour être exploités.

## La grille, par chapitre

Neuf points, repris de `Redaction2Chapitre`. Pour chacun, relever le défaut en une ligne, avec le numéro de sous-partie concerné.

1. **Le fil.** Le chapitre se lit-il du haut vers le bas sur le sujet de son titre, ou est-ce une juxtaposition de blocs autonomes ?
2. **L'objet défini.** Les termes centraux sont-ils définis dans le chapitre, ou seulement cités et sourcés ? Signaler tout modèle dont on énumère les composantes sans dire ce qu'il affirme, et toute liste annoncée puis jamais donnée (« les neuf dimensions » sans les neuf dimensions).
3. **L'analogie.** Présente, portée de bout en bout, retournée en fin de chapitre ? Ou absente, ou décorative dans un titre ?
4. **Le sourçage.** Compter les liens dont le texte dépasse 25 mots ou contient un point-virgule : ce sont des résumés d'étude traduits et collés. Signaler aussi les sources faibles (blogs de wellness, sites de tests commerciaux) sur des affirmations centrales.
5. **Les études expliquées.** Pour chaque étude mobilisée : dit-on ce que les chercheurs ont fait, ce qui en est sorti, et pourquoi c'est intéressant ? Ou seulement le résultat ?
6. **Les chiffres.** Chaque valeur est-elle amenée par une question et suivie d'une comparaison qui lui donne son échelle ?
7. **Le bloc ⚖️ Nuance.** Présent là où il faut, unique, et nuance-t-il réellement au lieu de définir ?
8. **Les blocs 👁️ 💑 🗣️.** Y avait-il un écart de perception documentable, un enjeu de couple, un vécu personnel fort qui appelait un témoignage ? Si oui, le bloc est-il là ?
9. **Les réflexes.** Combien de puces commencent par « Retenir », « Garder à l'esprit » ou « Se rappeler » ? Ce sont des résumés déguisés, pas des actions.

Relever aussi la longueur, le plancher étant de 1 500 mots.

## Les trois verdicts

* **Rien à faire.** Le chapitre tient. Rare, et c'est normal.
* **Chirurgie.** La structure et le fond tiennent, il manque des éléments ajoutables sans tout reprendre : définition d'un objet, bloc Nuance, échelle des chiffres, réflexes à convertir. C'est le cas le plus fréquent et le moins cher.
* **Réécriture.** Le fil est cassé, ou le chapitre est une suite de résumés d'études collés. Réécrire coûte environ trois fois plus cher que la chirurgie : ne prononcer ce verdict que lorsque la chirurgie ne peut rien sauver.

## Le rapport

Un fichier par guide, dans `5 - Notes Internes/Audit - <Guide>.md`, avec le frontmatter des notes internes (`type: "note-interne"`, `sujet: "chantier"`, `mis_a_jour_le:`). Jamais dans un dossier publié.

Structure : un paragraphe de synthèse (combien de chapitres dans chaque verdict, quels défauts dominent sur ce guide en particulier), puis un tableau.

| # | Chapitre | Mots | Défauts relevés | Verdict |
|---|---|---|---|---|

La colonne des défauts reste courte et actionnable : « objet non défini en 3.1, aucune analogie, 4 liens collés, 3 réflexes en Retenir ». Pas de prose, pas de recommandation développée : le rapport sert à planifier, pas à convaincre.

Terminer par l'estimation de coût : nombre de chapitres en chirurgie multiplié par une fourchette basse, nombre de chapitres en réécriture multiplié par une fourchette haute, pour que la décision de lancer la reprise se prenne en connaissance de cause.

## Ce qu'un audit ne fait pas

Il ne réécrit rien, ne renomme rien, ne touche pas aux index ni au pipeline. Il ne juge pas non plus la justesse scientifique du contenu : vérifier qu'une étude dit bien ce qu'on lui fait dire est un travail distinct, plus lourd, à demander explicitement quand il est voulu.
