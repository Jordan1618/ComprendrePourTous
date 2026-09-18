---
type: "interne"
mis_a_jour_le: 2026-09-17
---

# Arborescence du dépôt

Repère rapide, **non publié**. But : trouver où est une chose sans ouvrir 10 fichiers ni relire tout le dépôt.

**Pour une IA** : ce fichier donne la structure et où chercher, pas le contenu. Pour la liste des chapitres d'un guide avec liens et mots, ouvrir directement son `README.md` (déjà à jour, pas dupliqué ici). Pour la liste des fichiers réelle et à jour à tout instant : `git ls-files | sort`.

## Dossiers de premier niveau

| Dossier | Rôle | Éditable à la main ? |
|---|---|---|
| `0 - Guides complets/` | 1 fichier par guide, assemblage de tous ses chapitres | **Non, généré** par `build-guides-complets.py` |
| `1 - Guides/` | Source de vérité : 1 sous-dossier par guide, chapitres numérotés + `README.md` | Oui |
| `2 - Notions/` | Fiches courtes, 1 concept par fichier, indexées dans son `README.md` | Oui |
| `3 - Transversal/` | `Par sujet.md` et `Par angle.md` générés par `build-index.py` ; `Glossaire général.md`, `Signaux d'alerte.md`, `Sources et dates de vérification.md` écrits à la main | Mixte |
| `4 - Sources/` | 1 fichier par guide (même nom), liste consolidée des sources citées dans ses chapitres, indexé dans son `README.md` | Oui, avec réciprocité stricte |
| `5 - Notes Internes/` | Jamais publié, voir détail plus bas | Oui |
| `assets/` | `app.js`, `style.css`, `favicon.svg` | Oui |
| `supabase/` | `functions/soumettre-avis/index.ts`, `schema.sql` — backend des avis | Oui |
| `.github/workflows/` | `deploy.yml`, pipeline GitHub Actions | Oui |

## Fichiers racine

| Fichier | Rôle |
|---|---|
| `README.md` | Page d'accueil du site ; table des 11 guides avec mots/chapitres à jour |
| `CLAUDE.md` | Instructions de session pour Claude Code |
| `MAINTENANCE.md` | Règles détaillées et chantiers ouverts |
| `ANALYSE.md` | Notes d'analyse du projet |
| `.claude/skills/Faiseur2Guide/SKILL.MD` | Méthode de création/enrichissement de guide, avec changelog versionné |
| `build-guides-complets.py`, `build-index.py`, `build.py` | Pipeline de génération, dans cet ordre |
| `LICENSE.md`, `CNAME`, `.gitattributes`, `.gitignore` | Divers |

## Les 11 guides (`1 - Guides/<nom>/`)

Nom de dossier exact, pour se repérer entre le nom affiché et le nom de fichier :

| Nom affiché | Dossier | README |
|---|---|---|
| IST, dépistage et prévention | `IST, depistage et prevention/` | ✓ |
| L'amour | `L amour/` | ✓ |
| La rencontre | `La rencontre/` | ✓ |
| Les émotions | `Les emotions/` | ✓ |
| Les nouvelles compositions familiales | `Les nouvelles compositions familiales/` | ✓ |
| Massage professionnel | `Massage professionnel/` | ✓ |
| Pour Elle | `Pour Elle/` | ✓ (modifié par une autre session, voir ci-dessous) |
| Pour Lui | `Pour Lui/` | ✓ (modifié par une autre session, voir ci-dessous) |
| Pour Nous | `Pour Nous/` | ✓ |
| Questions et communication | `Questions et communication/` | ✓ |
| Réseaux sociaux | `Reseaux sociaux/` | ✓ |

Chaque `README.md` de guide contient déjà : bandeau, résumé, table des chapitres avec liens et angle, "Par où commencer", total mots/chapitres. **Ouvrir ce fichier plutôt que chercher un chapitre à la main.**

## `2 - Notions/`, `4 - Sources/`, `3 - Transversal/`

Chacun a son propre `README.md` ou fichier d'index (`2 - Notions/README.md`, `4 - Sources/README.md`) qui liste tout son contenu avec liens. Ne pas dupliquer cette liste ici : elle change trop souvent.

## `5 - Notes Internes/` (détail, car sans index propre)

| Fichier | Rôle |
|---|---|
| `Historique des demandes.md` | Journal obligatoire, 1 ligne par demande utilisateur qui déclenche du travail |
| `Ce qu'il faut faire.md` | Tâches internes, idées de guides futurs |
| `Cadences de revision.md` | Calendrier de revérification des chiffres par guide |
| `Chantier - Refonte des guides transversaux.md` | Modèle de fichier de suivi pour un chantier multi-étapes |
| `Journal des modifications.md` | Historique technique |
| `Mise en place des avis.md` | Notes sur le système d'avis/commentaires |
| `Contexte portable - Generation de guides.md` | Brief à copier-coller dans une nouvelle session pour continuer la génération de guides |
| `Arborescence du depot.md` | Ce fichier |

## Point de vigilance au 17/09/2026

Une autre session travaille en parallèle sur **Pour Elle** et **Pour Lui**. Avant d'y toucher ou de committer quoi que ce soit : `git status` d'abord.

- Non suivi par git (nouveaux, pas encore commités) : `Pour Elle/35 - Les conflits entre femmes.md`, `Pour Lui/31 à 34` (recherche masculine 2026, FAQ, ressources et associations, glossaire médical).
- Modifiés localement : `build.py`, `README.md` racine, les `README.md` et `4 - Sources/` de Pour Elle et Pour Lui, plusieurs fiches de `2 - Notions/`.

Pour un état exact à l'instant T : `git status` et `git ls-files | sort`.
