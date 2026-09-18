---
type: "interne"
mis_a_jour_le: 2026-09-18
---

# Chantier — La rencontre : étoffement complet

Fichier de travail, **non publié**, pensé pour être repris par une autre session sans accès à cette conversation.

## Demande d'origine (reformulée)

Étoffer le guide "La rencontre" (9 chapitres, 11 864 mots) avec l'intégralité des angles des 10 familles du skill Faiseur2Guide et l'intégralité des deux exemples de 30 sous-thèmes produits en élicitation (grille + inventaire + recoupement présentés et validés dans la conversation). Consigne explicite de méthode, donnée après un échange sur la consommation de tokens : moins d'agents en parallèle mais plus de travail chacun (2 au lieu de 4), effort de raisonnement réservé à l'orchestration (la fusion), pas à la rédaction elle-même, un guide à la fois, lecture des fichiers de règles une seule fois par agent, tâches mécaniques (comptage de mots, liens cassés, fusion de tables) faites par script Python plutôt que par un agent.

## Règles à respecter (rappel, détail complet dans CLAUDE.md / MAINTENANCE.md / skill)

- Chapitre : 1 500 à 3 500 mots.
- Sourçage réel par sous-partie, lien posé sur l'affirmation, jamais de `(source : ...)` nu, jamais d'URL/DOI fabriqué.
- Témoignage réel si vécu personnel fort (arnaque sentimentale, deuil, rupture) — jamais inventé.
- Réciprocité avec `4 - Sources/La rencontre.md`.
- Pas de chapitre final "Sources vérifiables".
- Neutralité de genre du lecteur, nuance systématique.
- Renvois croisés vers Réseaux sociaux (ch. 07, dérives amoureuses numériques), Pour Nous, Questions et communication, notion Contrôle coercitif — sans modifier leurs fichiers.
- `angle` du frontmatter dans le vocabulaire déjà utilisé par ce guide : physiologie, psychologie, repères, relation, prévention, pratique.

## Plan de chapitres (10-28)

### Partie A — exemple 1 : mécanismes et contextes (chapitres 10-16), agent 1

10. Homogamie et réseau social dans la formation du couple
11. L'effet miroir et l'échange social au premier contact
12. Ce que les applications de rencontre optimisent vraiment
13. Rencontrer après une rupture, un deuil, ou après 50 ans
14. Rencontres professionnelles et en contexte de vulnérabilité : consentement et cadre
15. Arnaques sentimentales et vérification avant un rendez-vous
16. Neuroatypie, anxiété sociale et applications de niche

### Partie B — exemple 2 : société, histoire et culture (chapitres 17-22), agent 1

17. Une histoire de la rencontre, du mariage arrangé au swipe
18. Le marché matrimonial : économie, droit et RGPD
19. Speed dating, jeux vidéo, communautés de passion : les rencontres de niche
20. La pickup culture et les coachs en rencontre, ce qui est vrai et dangereux
21. Rencontrer en mobilité, en crise, ou après 50 ans via clubs et associations
22. Ce que dix ans de recherche disent des couples formés en ligne

### Partie C — angles de la grille non couverts par 1-9 ni 10-22 (chapitres 23-28), agent 2

23. Le corps et la biologie du désir : phéromones, hormones et évolution (sciences du vivant restantes)
24. Philosophie et sens de la rencontre : hasard, destin et choix (philosophie et sens)
25. Corps, genre et intimité dans les premiers instants (corps et intimité restants)
26. Le décor de la rencontre : lieux, climat et territoire (contexte et environnement restants)
27. Ce que dit la donnée : statistiques, risques et normes (risque/données restants)
28. La rencontre dans l'art et la culture populaire (culture et expression restants)

## Répartition des agents (2 au lieu de 4)

- **Agent 1** : parties A + B, chapitres 10 à 22 (13 chapitres).
- **Agent 2** : partie C, chapitres 23 à 28 (6 chapitres).
- Chaque agent lit une seule fois CLAUDE.md, MAINTENANCE.md, le skill, et 2 chapitres d'exemple du guide, puis écrit tout son lot sans relire ces fichiers entre les chapitres.
- Aucun agent ne lance de script de build ni ne commit.
- Le comptage de mots, la vérification des liens et la fusion finale du README/`4 - Sources/` sont faits par script Python depuis la session principale, pas par les agents.

## État d'avancement

| Partie | Chapitres | Statut |
|---|---|---|
| A+B (agent 1) | 10-22 | fait (18/09/2026) |
| C (agent 2) | 23-28 | fait (18/09/2026) |

Guide passé de 9 chapitres/11 864 mots à 28 chapitres/44 591 mots. `4 - Sources/La rencontre.md` fusionné par script (deux ajouts indépendants depuis la même base, aucun chevauchement). README régénéré par script (tableau, frontmatter, section « Par où commencer »). Pipeline relancé, aucun lien cassé nouveau (le seul signalement est le même faux positif d'ancre déjà présent avant ce chantier). Pas encore commité.

Méthode appliquée suite aux conseils de sobriété token : 2 agents au lieu de 4 (un pour les deux exemples de 30 sous-thèmes, un pour les angles restants de la grille), chacun ne lisant les fichiers de règles qu'une fois, comptage de mots/vérification de liens/fusion faits en Python par la session principale plutôt que délégués.

## Comment reprendre

1. Lire ce fichier en entier.
2. Vérifier `git status` avant tout commit.
3. Une fois les deux agents terminés : régénérer le README (script Python, pas à la main), lancer `build-guides-complets.py`, `build-index.py`, `build.py`, vérifier les liens cassés, mettre à jour ce tableau, committer sur demande explicite.
