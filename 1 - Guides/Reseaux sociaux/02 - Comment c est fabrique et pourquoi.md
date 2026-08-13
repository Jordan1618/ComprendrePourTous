---
guide: "Réseaux sociaux"
chapitre: "2"
titre: "Comment c'est fabriqué, et pourquoi"
sujet: "commun"
angle: "repères"
verifie_le: 2026-08-13
licence: "CC BY 4.0"
---

# Comment c'est fabriqué, et pourquoi

### 2.1 Le bouton "j'aime" : une brique sociale devenue métrique

Le bouton "j'aime" de Facebook est déployé sur l'ensemble du site le 9 février 2009, après avoir été prototypé en interne dès 2007 par l'ingénieur Justin Rosenstein et la responsable produit Leah Pearlman, dans l'idée de faire circuler ce qu'ils décrivaient comme de "petites doses de positivité" entre utilisateurs. [Rosenstein a par la suite exprimé un regret explicite sur l'usage qu'en a fait l'écosystème publicitaire, évoquant une économie de l'attention qu'il juge nocive](https://www.timesofisrael.com/years-on-creators-of-facebook-like-button-give-idea-thumbs-down/) (Times of Israel, entretien avec Rosenstein et Pearlman ; vérification du 13 août 2026).

L'intention de départ était sociale : donner un moyen rapide de dire "j'ai vu, j'apprécie" sans avoir à écrire de commentaire. Ce que le bouton est devenu ensuite est différent : une métrique publique, comptée, comparée, qui transforme une interaction sociale en chiffre affiché sous chaque publication. Ce glissement de l'usage social vers l'usage de mesure est au cœur du chapitre 5 sur l'image de soi.

### 2.2 Le scroll infini : supprimer le seul moment où on pouvait s'arrêter

Le défilement infini, qui charge automatiquement du nouveau contenu quand on arrive en bas de l'écran, est généralement attribué à Aza Raskin, designer qui en développe le principe en 2006 (une revendication de paternité disputée, une équipe de Microsoft ayant déposé un brevet similaire la même année). Sa motivation de départ était ergonomique et non manipulatrice : éviter à l'utilisateur un clic "page suivante" jugé superflu, au nom d'un principe de design qu'il résume ainsi, chaque choix inutile imposé à l'utilisateur est un échec de conception.

[Raskin a depuis exprimé un regret marqué, estimant que l'humanité perd collectivement l'équivalent de plusieurs centaines de milliers de vies humaines par mois à faire défiler des fils sans fin](https://mastersofscale.com/video/he-invented-infinite-scroll-and-says-he-regrets-it/) (Masters of Scale, entretien avec Aza Raskin ; vérification du 13 août 2026). Le mécanisme retenu par les plateformes n'est pas le clic supprimé en soi : c'est la suppression de tout point d'arrêt naturel. Un livre a une dernière page, un journal a une dernière colonne ; un fil social n'en a pas, ce qui déplace la décision d'arrêter entièrement sur l'utilisateur, sans aucun repère externe pour l'aider.

### 2.3 Les stories : l'éphémère comme moteur de fréquentation

Le format "story", contenu visible 24 heures puis disparu, est introduit par Snapchat en 2013 puis généralisé par Instagram en 2016, Facebook et WhatsApp ensuite. Le principe technique est simple ; l'effet comportemental l'est moins. Un contenu permanent peut être consulté n'importe quand, donc reporté indéfiniment. Un contenu qui expire crée une fenêtre de consultation obligatoire, ce qui augmente mécaniquement la fréquence de retour sur l'application, indépendamment de la valeur du contenu lui-même. C'est un design qui joue directement sur ce qui sera développé au chapitre 3 sous le nom de FOMO : la peur de rater quelque chose avant qu'il ne disparaisse.

### 2.4 Les notifications push : la sollicitation qui vient à soi

Contrairement au bouton et au scroll, la notification push ne demande aucune action de l'utilisateur pour se déclencher : elle interrompt, en dehors de l'application, sur l'écran verrouillé. Elle transforme une plateforme d'usage volontaire en flux qui vient chercher l'attention plutôt que l'inverse.

La recherche sur l'effet de ces interruptions distingue deux régimes : les notifications constantes et celles regroupées à heures fixes. [Une expérience contrôlée a montré qu'un regroupement des notifications trois fois par jour réduisait le stress et augmentait le sentiment de contrôle sur son téléphone, par rapport à un flux continu, alors qu'une coupure totale des notifications augmentait au contraire l'anxiété et la peur de rater quelque chose](https://www.sciencedirect.com/science/article/abs/pii/S0747563219302596) (Fitz, Kushlev et coll., "Batching smartphone notifications can improve well-being", *Computers in Human Behavior*, 2019 ; vérification du 13 août 2026). Ce résultat nuance d'emblée toute lecture binaire du sujet : ni la sollicitation permanente ni la coupure totale ne sont la réponse, un point repris en détail dans la boîte à outils du chapitre 10.

### 2.5 La captologie : quand la persuasion devient une discipline d'ingénierie

Ces choix de conception ne sont pas isolés : ils s'inscrivent dans un champ de recherche que le psychologue B.J. Fogg nomme la "captologie" (computers as persuasive technologies), défini comme l'étude des ordinateurs conçus intentionnellement pour changer les attitudes ou les comportements de leurs utilisateurs. [Fogg formalise ce champ à Stanford et le documente dans son ouvrage de référence, où il détaille les mécanismes par lesquels un objet numérique peut influencer un comportement humain de façon mesurable et reproductible](https://dl.acm.org/doi/10.5555/2821581) (Fogg, *Persuasive Technology: Using Computers to Change What We Think and Do*, Morgan Kaufmann, 2003 ; vérification du 13 août 2026).

Un vocabulaire plus récent et plus opérationnel affine cette discipline : les "dark patterns" (motifs sombres), terme forgé en 2010 par le spécialiste en expérience utilisateur Harry Brignull, désignent spécifiquement les choix d'interface conçus pour pousser l'utilisateur vers une action qu'il n'aurait pas choisie s'il en avait eu une compréhension claire, s'abonner sans le vouloir vraiment, partager plus de données que prévu, ou avoir plus de mal à fermer un compte qu'à l'ouvrir. [Brignull a catalogué et nommé ces motifs sur un site dédié, une classification depuis reprise dans la législation européenne via le Digital Services Act ainsi que dans les lignes directrices de l'autorité américaine de la concurrence](https://en.wikipedia.org/wiki/Dark_pattern) (Brignull, H., *Deceptive Patterns*, 2023, et catalogue en ligne deceptive.design ; vérification du 13 août 2026). La captologie de Fogg décrit l'intention de persuader ; les dark patterns en décrivent la version la plus contestable, quand la persuasion devient tromperie active plutôt que simple influence.

Le point important n'est pas qu'un individu malveillant ait dessiné un piège : c'est qu'une discipline entière, enseignée, documentée et employée par les plus grandes entreprises technologiques, s'est constituée autour de l'ingénierie du comportement humain à grande échelle. Comprendre cela change la lecture des chapitres suivants : ce qui suit n'est pas une accumulation de mauvaises habitudes individuelles, mais la rencontre entre un cerveau humain ordinaire et des systèmes conçus, par des équipes entières, pour capter et retenir son attention le plus longtemps possible.

### 2.6 La gamification : transformer une relation en compteur à ne pas casser

Un exemple précis illustre bien comment un mécanisme de jeu, en apparence anodin, peut se substituer à l'échange qu'il était censé faciliter. Les "streaks" (séries) de Snapchat, introduites en 2015, comptent le nombre de jours consécutifs pendant lesquels deux utilisateurs se sont envoyé un message, affiché sous forme de chiffre et d'emoji à côté de leur conversation. [La recherche montre que cette mécanique de jeu conduit une partie des adolescents à envoyer des messages quasiment vides de contenu, une image noire ou un simple "bonjour", dans le seul but de maintenir le chiffre, ce que les auteurs qualifient de détournement de la fonction sociale de l'échange par sa propre gamification](https://ceur-ws.org/Vol-2637/paper13.pdf) (Hristova, D., Dumit, J., Lieberoth, A. & Slunecko, T., "Snapchat Streaks: How Adolescents Metagame Gamification in Social Media", GamiFIN, 2020 ; vérification du 13 août 2026).

Le mécanisme est révélateur au-delà du cas précis de Snapchat : dès qu'une interaction sociale est convertie en métrique visible et cumulative, la métrique elle-même peut devenir l'objectif poursuivi, indépendamment de la qualité de ce qu'elle était censée mesurer. C'est le même glissement, à une autre échelle, que celui décrit au 2.1 pour le bouton "j'aime".

**Nuance nécessaire.** Ces designs ne produisent pas les mêmes effets chez tout le monde. La recherche distingue de façon croissante un usage actif, qui consiste à publier, échanger et entretenir des liens réels, d'un usage passif, qui consiste à faire défiler sans interagir : c'est ce deuxième usage qui est le plus systématiquement associé à des effets négatifs, quand l'usage actif reste souvent neutre voire positif. Cette distinction, développée au chapitre 3, doit accompagner toute lecture de ce chapitre : le mécanisme est le même pour tous, l'effet ne l'est pas.

## Sources vérifiables

- Times of Israel, "Years on, creators of Facebook 'Like' button give idea thumbs down", [entretien avec Rosenstein et Pearlman](https://www.timesofisrael.com/years-on-creators-of-facebook-like-button-give-idea-thumbs-down/) — origine et regret sur le bouton "j'aime" ; vérification du 13 août 2026.
- Masters of Scale, ["He invented infinite scroll and says he regrets it"](https://mastersofscale.com/video/he-invented-infinite-scroll-and-says-he-regrets-it/) — Aza Raskin sur l'origine du défilement infini ; vérification du 13 août 2026.
- Fitz, N., Kushlev, K. et coll. (2019), [Batching smartphone notifications can improve well-being](https://www.sciencedirect.com/science/article/abs/pii/S0747563219302596), *Computers in Human Behavior* — effet du regroupement des notifications ; vérification du 13 août 2026.
- Fogg, B.J. (2003), [Persuasive Technology: Using Computers to Change What We Think and Do](https://dl.acm.org/doi/10.5555/2821581), Morgan Kaufmann — définition de la captologie ; vérification du 13 août 2026.
- Hristova, D., Dumit, J., Lieberoth, A. & Slunecko, T. (2020), [Snapchat Streaks: How Adolescents Metagame Gamification in Social Media](https://ceur-ws.org/Vol-2637/paper13.pdf), GamiFIN — gamification et détournement de l'échange social ; vérification du 13 août 2026.
- Brignull, H., [Dark pattern](https://en.wikipedia.org/wiki/Dark_pattern), *Deceptive Patterns*, 2023 — origine et définition des motifs d'interface trompeurs ; vérification du 13 août 2026.
