Fichier de travail, **non publié**. Pas-à-pas pour activer le système de notes et
commentaires publics (étoiles + Supabase + Turnstile). Tant que ces étapes ne sont pas
faites, le bloc d'avis affiche "Avis pas encore activés sur ce site." (voir `pasConfigure`
dans `assets/app.js`) et le formulaire reste caché.

## 1. Créer le projet Supabase (gratuit)

1. Aller sur [supabase.com](https://supabase.com), créer un compte, puis "New project".
2. Choisir un nom, un mot de passe de base de données (à garder de côté), une région
   proche (Europe).
3. Une fois le projet créé, ouvrir **SQL Editor > New query**, coller le contenu de
   `supabase/schema.sql`, et cliquer sur **Run**. Ça crée la table `avis`, les règles de
   sécurité (RLS) et la vue `avis_stats`.
4. Dans **Project Settings > API**, noter :
   - **Project URL** (ex. `https://xxxx.supabase.co`)
   - **anon public key** (clé publique, sans risque à exposer côté client — c'est le RLS
     qui protège les données, pas le secret de cette clé)

## 2. Créer le site Cloudflare Turnstile (gratuit)

1. Aller sur [dash.cloudflare.com](https://dash.cloudflare.com) (compte Cloudflare
   gratuit si besoin), section **Turnstile**.
2. "Add site", domaine du site (`comprendrepourtous.fr` ou équivalent), type de widget
   "Managed".
3. Noter les deux clés générées :
   - **Site key** (publique, va dans le HTML)
   - **Secret key** (privée, va uniquement dans les secrets Supabase, jamais dans le code)

## 3. Déployer l'Edge Function

Nécessite la [CLI Supabase](https://supabase.com/docs/guides/cli) installée localement.

```
supabase login
supabase link --project-ref <ref-du-projet>
supabase secrets set TURNSTILE_SECRET_KEY=<secret-key-turnstile>
supabase functions deploy soumettre-avis
```

La fonction est alors joignable sur
`https://<ref-du-projet>.supabase.co/functions/v1/soumettre-avis`.

## 4. Coller les clés dans le site

Dans `assets/app.js`, section "avis publics (Supabase)" :

```js
var SUPABASE_URL = "https://<ref-du-projet>.supabase.co";
var SUPABASE_ANON_KEY = "<anon public key>";
```

Dans `build.py`, fonction `avis_block()`, remplacer `REMPLACER_TURNSTILE_SITE_KEY` par la
**site key** Turnstile (celle de l'étape 2, pas la secret key).

Relancer le pipeline de génération (`python build.py` ou équivalent), vérifier
qu'un chapitre affiche bien les étoiles et le champ Turnstile, envoyer un avis de test,
et le retrouver dans Supabase **Table Editor > avis** avec `approuve = false`.

## 5. Modérer

Chaque avis reçu reste invisible sur le site tant qu'il n'est pas approuvé. Pour
approuver : Supabase **Table Editor > avis**, cocher `approuve` sur la ligne concernée.
Rien d'autre à faire — le site le récupère au prochain chargement de la page.
