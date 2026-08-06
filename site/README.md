# Site (Apollon)

Version web du projet, générée avec [Apollon](https://gohugo.io/) et le thème
[hugo-book](https://github.com/alex-shpak/hugo-book).

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

## Prévisualiser en local

```
hugo server -s site
```

Puis ouvrir http://localhost:1313/ComprendrePourTous/.

## Déploiement

Le déploiement sur GitHub Pages est automatique via
`.github/workflows/hugo.yml` à chaque push sur `main` : le workflow
régénère `site/content/`, build le site avec Apollon, et publie sur Pages.

À activer une seule fois côté dépôt : **Settings → Pages → Source : GitHub
Actions**.

Le site est ensuite disponible à :
https://jordan1618.github.io/ComprendrePourTous/
