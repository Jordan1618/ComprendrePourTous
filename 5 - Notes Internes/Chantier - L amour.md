---
type: "interne"
mis_a_jour_le: 2026-09-21
---

# Chantier — L'amour : étoffement complet

Fichier de travail, **non publié**, pensé pour être repris par une autre session sans accès à cette conversation.

## Demande d'origine (reformulée)

Étoffer le guide "L'amour" (9 chapitres, 10 119 mots) avec l'intégralité des angles des 10 familles du skill Faiseur2Guide et l'intégralité des deux exemples de 30 sous-thèmes produits en élicitation (grille + inventaire + recoupement présentés et validés dans la conversation). Méthode identique au chantier "La rencontre" : 2 agents maximum au lieu de 4, chacun lisant les fichiers de règles une seule fois avant d'écrire tout son lot, mécanique (comptage de mots, liens cassés, régénération du README) faite par script Python depuis la session principale.

## Règles à respecter (rappel, détail complet dans CLAUDE.md / MAINTENANCE.md / skill)

- Chapitre : 1 500 à 3 500 mots.
- Sourçage réel par sous-partie, lien posé sur l'affirmation, jamais de `(source : ...)` nu, jamais d'URL/DOI fabriqué.
- Témoignage réel si vécu personnel fort (deuil amoureux, rupture, dépendance affective) — jamais inventé.
- Réciprocité avec `4 - Sources/L amour.md`.
- Pas de chapitre final "Sources vérifiables".
- Neutralité de genre du lecteur, nuance systématique.
- Renvois croisés vers Pour Nous (construction à deux), La rencontre (attirance/attachement), Les émotions, notion `Désir spontané et désir réactif`, notion `Contrôle coercitif` (ch. dépendance affective/jalousie) — sans modifier leurs fichiers.
- `angle` du frontmatter dans le vocabulaire déjà utilisé par ce guide : physiologie, psychologie, repères, relation, pratique.

## Plan de chapitres (10-28)

### Partie A — exemple 1 : mécanismes et vécu de l'amour (chapitres 10-16)

10. Le rejet et la rupture, ce que dit la neurobiologie
11. Dépendance affective, jalousie et attachement à risque
12. Amour et santé mentale : dépression, TOC, stress post-traumatique
13. Amour asexuel, aromantique et neuroatypique
14. L'amour parental et hormonal comparé à l'amour romantique
15. Amour et âge : enfance, vieillissement, ménopause et andropause
16. Mesurer l'amour : théories et échelles de la recherche

### Partie B — exemple 2 : société, culture et sens (chapitres 17-22)

17. Une histoire et une géographie de l'amour, du courtois au polyamour
18. L'amour, l'argent et le droit
19. L'amour dans le mythe, la littérature, le cinéma et la chanson
20. Les philosophies de l'amour, de Platon aux penseuses contemporaines
21. Rituels, lieux et objets de l'amour à travers les cultures
22. L'amour et les grands mouvements du monde : guerre, diplomatie, démographie, écologie

### Partie C — angles de la grille non couverts par 1-9 ni 10-22 (chapitres 23-28)

23. Le corps de l'amour : génétique, immunité, pharmacologie et rythmes
24. Ce que l'amour coûte et rapporte : économie, sociologie et anthropologie comparée
25. Pouvoir et institutions de l'amour : politique, stratégie et diplomatie du sentiment
26. Corps, genre et sensorialité de l'amour
27. Parler d'amour : langage, génération et interculturalité
28. Risques et données de l'amour : statistiques, prévention et sécurité (renvoi vers La rencontre pour les arnaques sentimentales, vers IST pour l'épidémiologie, vers Contrôle coercitif pour la prévention des dérives)

## Répartition des agents (2 au lieu de 4)

- **Agent 1** : parties A + B, chapitres 10 à 22 (13 chapitres).
- **Agent 2** : partie C, chapitres 23 à 28 (6 chapitres).
- Chaque agent lit CLAUDE.md, MAINTENANCE.md, le skill, et 2 chapitres d'exemple du guide une seule fois, puis écrit tout son lot sans relire.
- Aucun agent ne lance de script de build ni ne commit. Chaque agent AJOUTE ses sources à la fin de `4 - Sources/L amour.md` sans rien écraser.
- Comptage de mots, vérification des liens, fusion des worktrees et régénération du README faits en Python par la session principale.

## État d'avancement

| Partie | Chapitres | Statut |
|---|---|---|
| A+B (agent 1) | 10-22 | fait (21/09/2026) |
| C (agent 2) | 23-28 | fait (21/09/2026) |

Guide passé de 9 chapitres/10 119 mots à 28 chapitres/39 760 mots. `4 - Sources/L amour.md` fusionné par script (deux ajouts indépendants depuis la même base, aucun chevauchement). README régénéré par script. Pipeline relancé, aucun lien cassé nouveau (les deux signalements du script sont le même faux positif d'ancre déjà présent ailleurs dans le dépôt, sans rapport avec ce chantier). Un agent a rencontré une erreur de lancement (worktree verrouillé/corrompu) et a dû être relancé après nettoyage manuel du worktree cassé. Pas encore commité.

## Comment reprendre

1. Lire ce fichier en entier.
2. Vérifier `git status` avant tout commit.
3. Une fois les deux agents terminés : fusionner les worktrees, régénérer le README (script), lancer `build-guides-complets.py`, `build-index.py`, `build.py`, vérifier les liens cassés, mettre à jour ce tableau, committer sur demande explicite.
