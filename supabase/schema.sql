-- Schema pour le systeme d'avis (etoiles + commentaire) du site.
-- A executer une seule fois dans Supabase : SQL Editor > New query > coller > Run.
-- Voir "5 - Notes Internes/Mise en place des avis.md" pour le pas-a-pas complet.

create table if not exists avis (
  id bigint generated always as identity primary key,
  page_url text not null,
  page_title text not null,
  note smallint not null check (note between 1 and 5),
  commentaire text check (char_length(commentaire) <= 1000),
  nom text check (char_length(nom) <= 60),
  approuve boolean not null default false,
  cree_le timestamptz not null default now()
);

create index if not exists avis_page_url_idx on avis (page_url);
create index if not exists avis_approuve_idx on avis (approuve);

alter table avis enable row level security;

-- Lecture publique : uniquement les avis approuves. Les visiteurs ne
-- peuvent jamais lire les avis en attente de moderation des autres.
create policy "lecture avis approuves" on avis
  for select
  to anon
  using (approuve = true);

-- Aucune politique d'insertion pour "anon" : les nouveaux avis passent
-- exclusivement par l'Edge Function "soumettre-avis", qui utilise la cle
-- service_role (contourne RLS) apres avoir verifie Turnstile. Ca empeche
-- un robot d'ecrire directement dans la table via l'API REST publique.

-- Vue agregee, utilisee pour le bloc "Tops" de la page d'accueil.
-- Ne remonte une page que si elle a au moins 3 avis approuves, pour
-- eviter qu'une seule note (bonne ou mauvaise) ne fasse un "top".
create or replace view avis_stats as
select
  page_url,
  page_title,
  count(*) as nombre,
  round(avg(note)::numeric, 2) as moyenne
from avis
where approuve = true
group by page_url, page_title
having count(*) >= 3
order by moyenne desc, nombre desc;

-- La vue herite du RLS de la table sous-jacente (avis) : un visiteur ne
-- voit donc que les stats calculees sur les avis approuves.
