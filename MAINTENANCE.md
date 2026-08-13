---
type: "documentation"
mis_a_jour_le: 2026-08-13
---

# Maintenance

Comment ce projet fonctionne, pour ne pas casser la structure en le faisant vivre.

## La règle unique

`1 - Guides/` est la source de vérité. On corrige là, jamais ailleurs.

`0 - Guides complets/` est généré. Toute modification faite directement dedans sera écrasée.

Après toute correction dans un chapitre :

```powershell
python build-guides-complets.py
```

## Ajouter un guide

1. Sous 8 000 mots : un seul fichier posé dans `1 - Guides/`.
2. Au-delà : son propre dossier, un fichier par chapitre, plus un `README.md`.
3. Ajouter le frontmatter à chaque fichier (voir plus bas).
4. Ajouter la ligne dans le tableau du `README.md` racine.
5. Ajouter les entrées dans `3 - Transversal/Par sujet.md` et `Par angle.md`.
6. Ajouter le guide à la liste `DOSSIERS` de `build-guides-complets.py`, puis relancer le script.

Un guide qui grossit et franchit les 8 000 mots migre vers le format éclaté.

## Bandeau d'avertissement obligatoire

Chaque `README.md` de guide porte, juste après le titre `# Nom du guide` et avant le sous-titre en gras, un bandeau en citation (`>`), toujours le même texte de base :

```markdown
> ⚠️ **Un repère, pas une vérité à suivre.** Chaque situation est individuelle et mérite sa propre lecture : ce guide n'est qu'un agrégat de recherches scientifiques et de bons conseils de vie courante, pas un mode d'emploi à appliquer à 100 %. Pour tout ce qui est complexe, rien ne remplace un professionnel — médecin, psychologue, psychiatre, sexologue, thérapeute de couple, et les autres selon le sujet. Ce projet est un travail d'étudiant : j'ai sincèrement essayé d'y mettre le meilleur de ce que je sais faire, pour qu'il touche le plus de monde possible et serve aussi de vitrine à mes compétences en informatique et en intelligence artificielle. Il est ouvert à tous : n'importe qui peut le reprendre et proposer des suggestions.
```

La liste des professionnels cités peut s'adapter au sujet du guide (médecin, sage-femme, kinésithérapeute, médiateur, selon le cas). Une phrase de sécurité additionnelle (numéro d'urgence) peut être ajoutée à la fin du bandeau si le sujet le justifie (ex : le 3114 dans le guide Les émotions). Ce bandeau ne se répète nulle part ailleurs dans le guide : il est dit une fois, au bon endroit, pas martelé à chaque chapitre.

## Pieds de page : ne garder que l'essentiel

Un `README.md` de guide se termine par la dernière section de contenu utile (« Une note sur la sécurité », etc. s'il y en a une), suivie directement de la ligne de retour :

```markdown
Retour à [l'accueil de Comprendre pour tous](<../../README.md>).
```

**Ne jamais ajouter** les sections suivantes, qui ont existé par le passé et ont été retirées parce qu'elles ne faisaient que répéter une information déjà donnée dans le paragraphe d'introduction :

- `## Autour de ce guide` / `## La suite` (renvois vers les guides voisins — à mentionner une fois, dans l'intro, pas deux fois)
- `## Le guide jumeau` (le lien vers le guide miroir peut tenir en une ligne simple si vraiment utile, jamais une section entière)
- `## Sources et mise à jour` (la date de vérification est déjà dans le frontmatter et dans le chapitre Sources vérifiables ; ne pas la répéter ici)

`## Par où commencer` reste autorisée et encouragée : c'est une aide à la navigation réelle, pas une répétition.

## Frontmatter

Chaque chapitre :

```yaml
---
guide: "Nom du guide"
chapitre: "4"
titre: "Titre complet du chapitre"
sujet: "corps féminin"        # corps féminin | corps masculin | commun
angle: "physiologie"          # physiologie | psychologie | prévention | pratique | relation | repères
verifie_le: 2026-07-27
licence: "CC BY 4.0"
---
```

Les deux axes de classement vivent ici, pas dans l'arborescence. Un sujet relève souvent de plusieurs catégories, donc les dossiers seraient un mauvais support.

## Ajouter une notion

Une notion mérite sa note quand le concept traverse au moins deux guides.

Format : cinq à quinze lignes, une définition, pourquoi ça compte, puis les liens vers les chapitres où c'est développé. **Une notion ne recopie jamais le contenu d'un chapitre**, elle oriente vers lui.

Si une notion dépasse une page, c'est qu'elle mérite de devenir un chapitre.

## Liens

Format markdown relatif, pas wikilink :

```markdown
[Texte du lien](<../1 - Guides/Dossier/04 - Chapitre.md>)
```

Les chevrons sont nécessaires à cause des espaces dans les chemins. Ce format fonctionne dans Obsidian, sur GitHub et dans un générateur de site statique, contrairement aux wikilinks.

Réglage Obsidian à faire une fois : Paramètres, Fichiers et liens, format de lien sur "Chemin relatif au fichier", et désactiver "Utiliser le format Wikilink".

Contrôle de tous les liens :

```powershell
python -c "import pathlib,re; [print('CASSE',f,m.group(1)) for f in pathlib.Path('.').rglob('*.md') for m in re.finditer(r'\]\(<([^>]+)>\)', f.read_text(encoding='utf-8')) if not (f.parent/m.group(1)).resolve().exists()]"
```

## Typographie

Deux règles, sans exception :

- Pas d'italiques. Gras pour l'emphase, guillemets pour les titres d'ouvrages et les noms propres.
- Pas de tirets cadratins. Virgule, point-virgule ou deux-points selon ce qui se lit le mieux.

## Sources

**Format obligatoire : l'hyperlien, pas la parenthèse seule.** Chaque affirmation sourcée est un lien cliquable qui enveloppe la portion de phrase qu'elle appuie, suivi d'une attribution courte entre parenthèses :

```markdown
[Le fait de nommer une émotion réduit l'activité de l'amygdale](https://pubmed.ncbi.nlm.nih.gov/17576282/) (Lieberman et coll., *Psychological Science*, 2007 ; vérification du 8 août 2026).
```

L'ancien format `(source : Auteur, « Titre », Revue, Année ; vérification du [date])`, sans lien, est obsolète et doit être converti dès qu'on retouche un chapitre qui le porte encore. Un chiffre sans date est un chiffre à revérifier.

**Ne jamais fabriquer une URL ni un DOI.** Chercher la source réellement avant d'écrire le lien. Quand aucune source vérifiable n'a été retrouvée pour une affirmation, le dire explicitement dans le texte (« aucune étude vérifiable retrouvée à cette date ») plutôt que de garder une référence invérifiée ou d'en inventer une. Une citation dont le titre, la revue ou l'éditeur ne correspond pas exactement à ce qui est trouvé en recherchant doit être corrigée pour refléter la vraie source, pas laissée telle quelle.

Quand une donnée est débattue, donner une fourchette et le dire. Jamais de fausse précision.

**Réciprocité obligatoire avec `4 - Sources/`.** Toute source hyperliée dans un chapitre doit aussi exister dans le fichier `4 - Sources/<Nom du guide>.md` correspondant, avec le même lien vérifié (jamais un lien de recherche Google Scholar générique quand un lien direct a été trouvé et utilisé dans le chapitre). Réciproquement, toute entrée de `4 - Sources/` doit se retrouver citée dans le guide. Après une conversion de citations, relire le fichier de sources du guide et remplacer les liens de recherche générique par les mêmes liens directs que ceux utilisés dans les chapitres.

**Pas de chapitre « Sources vérifiables » dans le guide lui-même.** Chaque chapitre porte déjà ses sources en hyperliens directs dans le texte ; `4 - Sources/<Nom du guide>.md` en tient la liste consolidée. Un chapitre final qui reliste toutes les sources du guide ferait doublon avec les deux à la fois — ne pas en créer un pour un nouveau guide, et le retirer d'un guide existant si on en retrouve un (retirer le chapitre, pas renuméroter les autres puisqu'il est toujours en dernière position).

Après toute conversion de citations dans un guide, contrôler qu'aucun lien n'est cassé (voir la commande plus bas), puis committer.

Cadence de revue : tous les six mois, guide par guide, en ne touchant qu'aux chiffres et aux recommandations officielles. Voir `3 - Transversal/Sources et dates de vérification.md`.

## Nuance et exceptions

Une affirmation générale doit tenir compte des cas qui s'en écartent légitimement, plutôt que de se présenter comme une règle universelle. Par exemple, une observation valable « dans la plupart des familles » ou « souvent » ne doit jamais être formulée comme une règle qui s'appliquerait partout : le dire explicitement (« ce n'est qu'un des équilibres possibles », « dans d'autres configurations... ») évite de heurter les lecteurs dont la situation ne correspond pas au cas majoritaire décrit.

Un domaine transversal à toujours renforcer, dans n'importe quel guide : l'importance de communiquer explicitement et de savoir s'exprimer dans le couple ou la famille, plutôt que de supposer que les choses se disent d'elles-mêmes.

## Chantiers ouverts

1. **Finir la conversion des citations en hyperliens sur Pour Elle** (le seul guide encore au format ancien à cette date).
2. **Revérification des chiffres.** Prioritaire avant toute diffusion large. Commencer par le guide IST, le plus exposé aux données périmées.
3. **Dégenrer le guide sur la santé émotionnelle masculine.** Certains passages présupposent encore une lectrice en couple avec un homme.
4. **Convertir les renvois internes** du type "voir 4.4" en liens cliquables. Plusieurs centaines, scriptable, à faire une fois le contenu stabilisé.
5. **Étoffer les notions.** La liste s'est déjà allongée, mais chaque nouveau guide introduit des concepts (masculinité précaire, alliance thérapeutique, homogamie...) qui méritent d'être vérifiés contre `2 - Notions/` et complétés si absents.
6. **Passe de nuance globale.** Relire les guides déjà terminés pour repérer les formulations encore trop absolues et les assouplir, à la manière de la correction faite dans Pour Nous (chapitre sur la belle-famille).

## Licence

CC BY 4.0. Utilisation, modification et rediffusion libres, y compris commerciales, à condition de citer le projet. Voir `LICENSE.md`.

## Vérifier les correspondances après chaque ajout

C'est le contrôle le plus facile à oublier, et celui qui fait le plus de dégâts silencieux : un guide ajouté que rien ne référence, ou une notion récente qu'aucun guide ancien ne cite. Le texte est bon, il est en ligne, et personne n'y arrive.

À faire après **tout** ajout ou renommage de chapitre, de notion ou de guide.

### 1. Régénérer les artefacts, dans cet ordre

```
python build-index.py             regenere Par sujet et Par angle depuis le frontmatter
python build-guides-complets.py   regenere les versions integrales du dossier 0
python build.py                   regenere le site dans _site/
```

`build.py` signale les liens internes qui pointent dans le vide : un build propre vaut donc vérification des liens.

### 2. Les notions récentes doivent être citées par les guides anciens

C'est le point le plus souvent manqué. Une notion créée pour un guide récent est presque toujours pertinente dans un guide plus ancien, qui l'évoque sans la nommer. Chercher le terme dans tout le dépôt, puis ajouter le renvoi là où il manque :

```
grep -ril "granularite emotionnelle" "1 - Guides"
```

Si un chapitre ancien parle du sujet sans lien vers la notion, ajouter le lien. L'inverse compte autant : chaque notion doit avoir sa section **Où c'est développé** à jour, pointant vers *tous* les chapitres qui la traitent, pas seulement le premier écrit.

### 3. Les renvois croisés entre guides

Un guide neuf doit être **cité par** les guides voisins, pas seulement les citer. Après avoir écrit un guide, relire les guides proches et ajouter les renvois manquants dans les deux sens. Un lien à sens unique est un lien à moitié fait.

### 4. La checklist

- [ ] Le guide apparaît dans le tableau du `README.md` racine.
- [ ] Il apparaît dans `Par sujet` et `Par angle` (automatique via `build-index.py`).
- [ ] Il est listé dans `Sources et dates de vérification.md`.
- [ ] Ses termes nouveaux existent dans `2 - Notions/` et dans le glossaire général.
- [ ] Les termes et notions ajoutés existent bien dans `3 - Transversal`
- [ ] Chaque notion citée a sa section « Où c'est développé » complète.
- [ ] Les guides voisins le citent en retour, **sans** section dédiée type « Autour de ce guide » — une mention dans le paragraphe d'intro suffit.
- [ ] Le `README.md` du guide porte le bandeau d'avertissement obligatoire, juste sous le titre.
- [ ] Toutes les citations du guide sont au format hyperlien, et chaque source a son miroir dans `4 - Sources/<Guide>.md`.
- [ ] `GUIDE_ORDER` et `GUIDE_HUE` dans `build.py`, `DOSSIERS` dans `build-guides-complets.py`, `ORDRE_GUIDES` dans `build-index.py`.
- [ ] En cas de renommage : les anciennes URL figurent dans `REDIRECTS` (`build.py`).

### 5. Un renommage se fait toujours avec redirection

Renommer un guide change son URL. Sans entrée dans `REDIRECTS`, tous les liens déjà partagés tombent en 404, y compris ceux qui circulent hors du site.
