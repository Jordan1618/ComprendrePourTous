---
type: "note-interne"
sujet: "chantier"
mis_a_jour_le: 2026-09-25
---

# Audit - Le sommeil (ré-audit post-Redaction2Chapitre)

Ré-audit intégral des 16 chapitres, sans présumer du résultat ni reprendre le tableau de l'ancien rapport (remplacé entièrement). Verdict global : la reprise a fonctionné. **6 chapitres « rien à faire », 10 en « chirurgie », aucun en « réécriture ».** Le fil unique et l'analogie filée (portée de bout en bout puis retournée en fin de chapitre avec sa propre limite nommée) sont présents dans les 16 chapitres, sans exception. Le bloc ⚖️ Nuance est présent dans 14/16 chapitres, absent seulement en 8 et 15. Aucun réflexe en « Retenir/Garder à l'esprit/Se rappeler » sur l'ensemble du guide (0 occurrence) : les réflexes sont systématiquement des actions. Les chiffres cités sont presque toujours amenés par une échelle de comparaison concrète (« soit l'équivalent de… », « pour donner une échelle à ce chiffre… »). Les études mobilisées sont expliquées (qui, quoi, pourquoi c'est intéressant), pas seulement citées pour leur résultat — y compris dans les chapitres aux liens les plus longs.

**Le défaut dominant qui subsiste est la longueur : 9 chapitres sur 16 sont sous le plancher de 1 500 mots** (comptage officiel du README), certains de peu (16 : 1 488 mots), d'autres nettement (8 et 14 : environ 1 160 mots). Dans tous les cas la structure et le fond tiennent ; il s'agit d'étoffer, pas de refondre. Deux défauts ponctuels s'y ajoutent : le chapitre 2 saute sa numérotation interne (2.2 puis 2.4, sans 2.3) ; les chapitres 8 et 15 n'ont pas de bloc ⚖️ Nuance alors que le reste du guide en pose systématiquement un.

**Réciprocité des sources (chapitres ↔ `4 - Sources/Le sommeil.md`) : quasi totale.** Sur 124 URL uniques citées dans les 16 chapitres, 122 figurent dans le fichier de sources central. Un seul écart réel : le chapitre 2 source le chiffre « 30 millions de travailleurs postés aux États-Unis » sur `onlinelibrary.wiley.com/doi/10.1155/2018/8576890`, absent du fichier de sources, qui attribue cette même ligne (repère 2.4) à un autre article (PMC5828540) au lieu du lien réellement posé dans le chapitre — **soit 0,8 % des URL du guide sans réciprocité réelle**, très en dessous du seuil qui justifierait une correction en urgence. Un second écart (PMC10735476 côté chapitre 14 vs son miroir `ncbi.nlm.nih.gov/pmc/articles/PMC10735476` côté sources) n'est qu'une variante d'URL du même article, pas une absence de source. Aucune correction n'a été appliquée : signalé pour action ultérieure, conformément au mode lecture seule du skill.

| # | Chapitre | Mots | Défauts relevés | Verdict |
|---|---|---|---|---|
| 1 | Ce que le sommeil fait vraiment | 2 121 | Aucun défaut significatif relevé | Rien à faire |
| 2 | L'horloge interne | 1 847 | Numérotation interne saute de 2.2 à 2.4 (pas de 2.3) ; 1 lien source (stat. « 30 millions ») absent de `4 - Sources` | Chirurgie |
| 3 | Les troubles les plus fréquents | 1 810 | Aucun défaut significatif relevé | Rien à faire |
| 4 | Le sommeil à chaque âge | 2 183 | Aucun défaut significatif relevé | Rien à faire |
| 5 | Ce qui aide vraiment | 1 585 | Aucun défaut significatif relevé | Rien à faire |
| 6 | Sommeil et corps | 1 279 | 221 mots sous le plancher | Chirurgie |
| 7 | Sommeil et santé mentale | 1 818 | Aucun défaut significatif relevé | Rien à faire |
| 8 | Métiers à risque | 1 166 | 334 mots sous le plancher ; aucun bloc ⚖️ Nuance | Chirurgie |
| 9 | Une histoire longue du sommeil | 1 292 | 208 mots sous le plancher | Chirurgie |
| 10 | Le sommeil ailleurs | 1 337 | 163 mots sous le plancher | Chirurgie |
| 11 | Ce que le manque de sommeil coûte | 1 307 | 193 mots sous le plancher | Chirurgie |
| 12 | L'industrie du sommeil | 1 423 | 77 mots sous le plancher (léger) | Chirurgie |
| 13 | Le sommeil en couple et en famille | 1 718 | Aucun défaut significatif relevé | Rien à faire |
| 14 | Sommeil, précarité et contrôle coercitif | 1 158 | 342 mots sous le plancher | Chirurgie |
| 15 | Le sommeil dans l'art et la culture | 1 288 | 212 mots sous le plancher ; aucun bloc ⚖️ Nuance | Chirurgie |
| 16 | Rituels, sport et alimentation | 1 488 | 12 mots sous le plancher (marginal) | Chirurgie |

## Estimation de coût de reprise

10 chapitres en chirurgie (2, 6, 8, 9, 10, 11, 12, 14, 15, 16), fourchette basse de 10 à 15k tokens par chapitre selon le précédent utilisé sur d'autres guides (« Pour Lui », « Les nouvelles compositions familiales ») : **environ 100 à 150k tokens** pour l'ensemble, l'essentiel du travail consistant à étoffer les sections existantes (pas de nouvelle recherche de fond attendue, sauf pour les deux blocs ⚖️ Nuance manquants en 8 et 15) plutôt qu'à reformuler des citations collées ou reconstruire une analogie absente, contrairement aux guides encore non repris. Aucun chapitre en réécriture, donc pas de fourchette haute à appliquer ici.

## Conclusion

La reprise sous Redaction2Chapitre a globalement fonctionné : les défauts structurels lourds identifiés sur d'autres guides non repris (liens collés non expliqués, absence d'analogie filée, réflexes déguisés en résumés) n'apparaissent plus nulle part dans « Le sommeil ». Ce qui reste à corriger est mineur et localisé — de la longueur à ajouter sur 9 chapitres et deux blocs Nuance à poser — pas une nouvelle passe de fond.
