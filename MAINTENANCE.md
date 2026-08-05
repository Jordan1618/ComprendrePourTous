---
type: "documentation"
mis_a_jour_le: 2026-08-02
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

Chaque affirmation chiffrée porte sa source et sa date, au format `(source : X ; vérification du [date])`. Un chiffre sans date est un chiffre à revérifier.

Quand une donnée est débattue, donner une fourchette et le dire. Jamais de fausse précision.

Cadence de revue : tous les six mois, guide par guide, en ne touchant qu'aux chiffres et aux recommandations officielles. Voir `3 - Transversal/Sources et dates de vérification.md`.

## Chantiers ouverts

1. **Revérification des chiffres.** Prioritaire avant toute diffusion large. Commencer par le guide IST, le plus exposé aux données périmées.
2. **Dégenrer le guide sur la santé émotionnelle masculine.** Certains passages présupposent encore une lectrice en couple avec un homme.
3. **Convertir les renvois internes** du type "voir 4.4" en liens cliquables. Plusieurs centaines, scriptable, à faire une fois le contenu stabilisé.
4. **Étoffer les notions.** Quatre existent, la liste est faite pour s'allonger.

## Licence

CC BY 4.0. Utilisation, modification et rediffusion libres, y compris commerciales, à condition de citer le projet. Voir `LICENSE.md`.
