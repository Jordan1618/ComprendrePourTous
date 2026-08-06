# Site (Apollon)

Version web du projet, générée avec [Apollon](https://gohugo.io/). Design
et layouts maison dans `site/layouts/` et `site/static/css/style.css` —
pas de thème tiers.

## Comment ça marche

`site/content/` est un artefact **généré**, à ne jamais éditer à la main
(même logique que `0 - Guides complets/` généré par `build-guides-complets.py`
à la racine du dépôt). La source de vérité reste `1 - Guides/`, `2 - Notions/`
et `3 - Transversal/` à la racine.

```
python site/scripts/sync_content.py   # régénère site/content/ depuis les sources
```

Ce script convertit le frontmatter, recalcule l'ordre des chapitres et
réécrit les liens internes entre fichiers Markdown en shortcodes `{{< ref >}}`
Apollon (résolus au build, ce qui fait échouer la build si un lien pointe dans
le vide).

## Design

- `site/layouts/baseof.html` : squelette de page (en-tête, sidebar, pied de page).
- `site/layouts/_partials/nav.html` : arbre de navigation, généré depuis les
  sections du contenu (pas de fichier de menu à maintenir à la main).
- `site/layouts/index.html` : accueil (hero + cartes des 4 sections).
- `site/layouts/_default/single.html` : page d'article (fil d'ariane, tags,
  sommaire, précédent/suivant).
- `site/layouts/_default/list.html` : page de section (guides, notions...).
- `site/static/css/style.css` : toute la mise en forme, en CSS pur (variables
  pour le thème clair/sombre, pas de dépendance externe).

## Prévisualiser en local

```
hugo server -s site
```

Puis ouvrir http://localhost:1313/.

## Déploiement

Le déploiement sur GitHub Pages est automatique via
`.github/workflows/hugo.yml` à chaque push sur `main` : le workflow
régénère `0 - Guides complets/` puis `site/content/`, build le site avec
Apollon, et publie sur Pages.

À activer une seule fois côté dépôt : **Settings → Pages → Source : GitHub
Actions**.

Le site est ensuite disponible à :
https://www.comprendrepourtous.fr
