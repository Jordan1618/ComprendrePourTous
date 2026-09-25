---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-25
---

# Audit — Alimentation

## Synthèse

Ré-audit complet des 26 chapitres après la reprise sous `Redaction2Chapitre`, lecture intégrale de chacun (les 26 fichiers ont été ouverts en entier, pas seulement échantillonnés). Répartition des verdicts : **0 Rien à faire, 26 Chirurgie, 0 Réécriture**.

La reprise a clairement fonctionné sur le fond : dans les 26 chapitres, le fil tient de bout en bout (thème unique du titre au dernier paragraphe, aucun bloc autonome juxtaposé), chaque chapitre porte une analogie filée sur toute sa longueur et retournée en conclusion (le chantier au ch. 1, les petites pièces au ch. 2, l'élastique au ch. 14, le dictionnaire visuel au ch. 25, le conducteur automatisé au ch. 26, etc.), les objets centraux sont définis avant d'être cités, le bloc ⚖️ Nuance est présent et unique dans les 26/26 chapitres et nuance réellement plutôt que de redéfinir, et les chiffres sont systématiquement amenés par une question puis comparés pour leur donner une échelle. Aucun chapitre n'affiche le problème structurel qui justifierait une réécriture.

Deux défauts dominants, récurrents mais tous deux du registre chirurgical, ressortent malgré tout :

1. **Plancher de 1 500 mots jamais atteint.** Les 26 chapitres se situent entre 844 mots (ch. 13) et 1 344 mots (ch. 10), pour une moyenne autour de 1 010 mots. Aucun chapitre n'atteint le plancher fixé par `Redaction2Chapitre`. C'est le défaut le plus systématique du guide : chaque chapitre a la place d'être approfondi (plus d'exemples concrets, plus de mécanisme expliqué, un deuxième témoignage) sans rien casser de la structure actuelle.
2. **Bullet final « Retenez que... » / « Retenir que... » dans 15 chapitres sur 26** (01, 03, 08, 09, 10, 14, 15, 16, 17, 19 ×2, 20 ×2, 21, 22, 24, 25). C'est exactement le résumé déguisé en réflexe que le point 9 de la grille signale : la phrase récapitule un lien inter-chapitres ou un constat plutôt que de proposer une action. Les 11 autres chapitres (02, 04, 05, 06, 07, 11, 12, 13, 18, 23, 26) n'ont pas ce problème sur leur liste de réflexes.

Défaut secondaire, présent partout à des degrés divers : une part significative des hyperliens (5 à 11 par chapitre, généralement 6-8) portent un texte de plus de 25 mots ou un point-virgule, signe de résultats d'étude traduits et accrochés à la phrase plutôt que pleinement digérés. Le procédé reste globalement maîtrisé par rapport à l'ancien état du guide : les citations sont enchâssées dans un raisonnement continu, reliées par l'analogie filée, et la plupart du temps on explique ce qui ressort de l'étude et pourquoi c'est intéressant. Ce qui manque presque partout, c'est le « ce que les chercheurs ont fait » (méthode, échantillon) — les résultats sont donnés, la manière dont ils ont été obtenus rarement. Les chapitres 04, 10, 14, 17, 19, 20 et 25 sont les plus concernés (8 liens denses ou plus).

Les blocs 👁️ / 💑 / 🗣️ sont utilisés avec discernement plutôt que systématiquement : présents aux chapitres 02 (écart de genre sur les carences), 10 (regard masculin sur les TCA + témoignage), 16, 21 et 23 (couple), absents ailleurs à raison — aucun chapitre lu ne semblait appeler un tel bloc sans l'avoir.

## Réciprocité des sources

Vérification automatisée des URL citées en hyperlien dans les 26 chapitres contre `4 - Sources/Alimentation.md` : 138 URL distinctes citées, **3 absentes telles quelles du fichier Sources, soit 2,2 %**. Dans les trois cas, il ne s'agit pas d'une source manquante mais d'une variante d'URL du même article (miroir `pmc.ncbi.nlm.nih.gov` vs `ncbi.nlm.nih.gov/pmc/`, ou lien `/abs/` vs lien complet ScienceDirect) :

- ch. 11 : `https://pmc.ncbi.nlm.nih.gov/articles/PMC10180846/` cité dans le texte, alors que Sources référence `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10180846/` (même article PMC).
- ch. 16 : deux occurrences de `https://www.sciencedirect.com/science/article/pii/S0195666315300210` (sans `/abs/`) cité dans le texte, alors que Sources référence `.../article/abs/pii/S0195666315300210` (même article).
- ch. 23 : `https://pmc.ncbi.nlm.nih.gov/articles/PMC7742522/` cité dans le texte, alors que Sources référence `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7742522/` (même article PMC).

Pas de correction apportée (lecture seule) : à uniformiser sur l'URL canonique lors de la prochaine reprise de ces trois chapitres.

## Tableau détaillé

| # | Chapitre | Mots | Défauts relevés | Verdict |
|---|---|---|---|---|
| 1 | Les macronutriments | 1 131 | Sous le plancher (1 131/1 500) ; 7 liens denses (résultats d'étude sans méthode) | Chirurgie |
| 2 | Micronutriments et carences | 1 003 | Sous le plancher ; 6 liens denses ; 👁️ présent et pertinent | Chirurgie |
| 3 | Calculer ses besoins | 917 | Sous le plancher (le plus court après le 13) ; 4 liens denses ; 1 bullet « Retenez » disguisé en 3.x | Chirurgie |
| 4 | Nutrition selon l'objectif | 1 031 | Sous le plancher ; 9 liens denses (le plus dense de la première moitié) | Chirurgie |
| 5 | Sportif vs sédentaire | 1 051 | Sous le plancher ; 7 liens denses | Chirurgie |
| 6 | Les régimes populaires passés au crible | 977 | Sous le plancher ; 8 liens denses | Chirurgie |
| 7 | Compléments alimentaires | 950 | Sous le plancher ; 6 liens denses | Chirurgie |
| 8 | Hydratation, IG, fibres, microbiote | 1 077 | Sous le plancher ; 7 liens denses ; 1 bullet « Retenez » disguisé | Chirurgie |
| 9 | Nutrition et maladies | 939 | Sous le plancher ; 7 liens denses ; 1 bullet « Retenez » disguisé | Chirurgie |
| 10 | Troubles du comportement alimentaire | 1 344 | Le plus long du guide, encore sous le plancher ; 10 liens denses ; 1 bullet « Retenir » disguisé ; 👁️ et 🗣️ présents et bien utilisés | Chirurgie |
| 11 | Allergies, intolérances, végétarisme, véganisme | 908 | Sous le plancher ; 6 liens denses ; URL de source en miroir non reprise à l'identique dans Sources (11.2) | Chirurgie |
| 12 | Nutrition selon l'âge et la situation | 1 102 | Sous le plancher ; 7 liens denses | Chirurgie |
| 13 | Lire une étiquette et le marketing | 844 | Chapitre le plus court du guide ; 6 liens denses | Chirurgie |
| 14 | Outils pratiques | 1 276 | Sous le plancher ; 9 liens denses ; 1 bullet « Retenir » disguisé en synthèse finale | Chirurgie |
| 15 | Une histoire longue de l'alimentation humaine | 912 | Sous le plancher ; 6 liens denses ; 1 bullet « Retenez » disguisé | Chirurgie |
| 16 | Le repas partagé | 917 | Sous le plancher ; 5 liens denses ; 1 bullet « Retenez » disguisé ; URL Bourdieu incohérente avec Sources (16.2) | Chirurgie |
| 17 | Religion, interdits et jeûnes | 1 157 | Sous le plancher ; 9 liens denses ; 1 bullet « Retenez » disguisé | Chirurgie |
| 18 | L'industrie agroalimentaire | 889 | Sous le plancher ; 7 liens denses | Chirurgie |
| 19 | Précarité, déserts alimentaires et gaspillage | 992 | Sous le plancher ; 8 liens denses ; 2 bullets « Retenez » disguisés en synthèse finale | Chirurgie |
| 20 | Écologie et géopolitique de l'alimentation | 940 | Sous le plancher ; 8 liens denses ; 2 bullets « Retenez » disguisés | Chirurgie |
| 21 | Diet culture, grossophobie et réseaux sociaux | 937 | Sous le plancher ; 6 liens denses ; 1 bullet « Retenez » disguisé ; 👁️/💑 présent et pertinent | Chirurgie |
| 22 | Alimentation émotionnelle et lien intestin-cerveau | 1 029 | Sous le plancher ; 8 liens denses ; 1 bullet « Retenir » disguisé | Chirurgie |
| 23 | Le couple et la famille à table | 907 | Sous le plancher ; 6 liens denses ; 💑 présent et bien utilisé ; URL de source en miroir non reprise à l'identique dans Sources (23.1) | Chirurgie |
| 24 | Cuisines du monde et éthique alimentaire | 986 | Sous le plancher ; 7 liens denses ; 1 bullet « Retenez » disguisé | Chirurgie |
| 25 | L'alimentation dans l'art et le folklore | 1 125 | Sous le plancher ; 11 liens denses (le plus dense du guide) ; 1 bullet « Retenez » disguisé | Chirurgie |
| 26 | Sortir de la culpabilité | 1 037 | Sous le plancher ; 5 liens denses (le moins dense du guide) | Chirurgie |

## Ce qui ne relève pas d'un défaut

- Bandeau d'avertissement et pied de page du `README.md` conformes à `MAINTENANCE.md` (bandeau exact, pas de section interdite, ligne de retour à l'accueil présente).
- Aucun chapitre ne porte de section « Sources et mise à jour », « Autour de ce guide », « La suite » ou de contenu de journal/mainteneur.
- Chaque chapitre garde sa propre section « Sources vérifiables » en fin de chapitre, conforme à la règle v12 (pas de chapitre agrégateur dédié).
- Guillemets français et gras d'emphase respectés dans les échantillons lus ; pas d'italique ni de tiret cadratin relevés.

## Estimation de coût de la reprise

26 chapitres en Chirurgie, aucun en Réécriture. Le travail principal par chapitre est homogène : approfondir jusqu'au plancher de 1 500 mots (ajouter environ 300 à 650 mots selon le chapitre), convertir le bullet « Retenez que... » en action quand il est présent (15 chapitres), et expliquer la méthode d'au moins une étude par chapitre plutôt que son seul résultat (surtout 04, 10, 14, 17, 19, 20, 25). Fourchette basse à moyenne pour une chirurgie de ce type : **26 chapitres × 15-25 minutes de reprise ≈ 6h30 à 11h de travail au total**, plus une passe finale de 10 minutes pour uniformiser les 3 URL en miroir avec `4 - Sources/Alimentation.md`.
