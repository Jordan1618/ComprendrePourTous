// Edge Function Supabase : reçoit un avis (étoiles + commentaire), vérifie
// le honeypot et le jeton Cloudflare Turnstile, puis insère la ligne en
// base avec la clé service_role (la seule autorisée à écrire, RLS oblige).
// Envoie ensuite une notification par e-mail via Web3Forms (meme service
// et meme cle publique que le formulaire de contact, voir assets/app.js).
//
// Déploiement : `supabase functions deploy soumettre-avis`
// Secrets requis (supabase secrets set) : TURNSTILE_SECRET_KEY
// Voir "5 - Notes Internes/Mise en place des avis.md".

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

const WEB3FORMS_KEY = "daada50b-bc23-4a7b-b7f2-30632276cf6c";

async function notifierParMail(avis: {
  page_url: string; page_title: string; note: number; commentaire: string | null; nom: string | null;
}) {
  const corps = (avis.nom || "Un·e visiteur·se") + " a laissé " + avis.note + "/5" +
    (avis.commentaire ? " et a dit « " + avis.commentaire + " »" : " sans commentaire") +
    "\n\n---\nPage : " + avis.page_title + "\n" + avis.page_url +
    "\n\nÀ approuver dans Supabase > Table Editor > avis.";
  try {
    await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({
        access_key: WEB3FORMS_KEY,
        subject: "[Comprendre pour tous] Nouvel avis à modérer — " + avis.page_title,
        message: corps,
        from_name: "Comprendre pour tous",
      }),
    });
  } catch {
    // La notification est un confort, pas une garantie : un echec ici ne
    // doit jamais faire echouer l'enregistrement de l'avis lui-meme.
  }
}

function reponse(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
  });
}

async function verifierTurnstile(token: string, ip: string | null): Promise<boolean> {
  const secret = Deno.env.get("TURNSTILE_SECRET_KEY");
  if (!secret) return false;
  const form = new FormData();
  form.append("secret", secret);
  form.append("response", token);
  if (ip) form.append("remoteip", ip);
  const r = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
    method: "POST",
    body: form,
  });
  const data = await r.json();
  return data.success === true;
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS_HEADERS });
  if (req.method !== "POST") return reponse({ error: "Méthode non autorisée" }, 405);

  let payload;
  try {
    payload = await req.json();
  } catch {
    return reponse({ error: "Corps de requête invalide" }, 400);
  }

  const { page_url, page_title, note, commentaire, nom, honeypot, turnstile_token } = payload || {};

  // Champ piège rempli = robot. On simule un succès sans rien écrire, pour
  // ne pas lui apprendre que sa soumission a été détectée.
  if (honeypot) return reponse({ ok: true });

  if (typeof page_url !== "string" || !page_url || page_url.length > 300) {
    return reponse({ error: "Page invalide" }, 400);
  }
  if (typeof page_title !== "string" || !page_title || page_title.length > 200) {
    return reponse({ error: "Titre invalide" }, 400);
  }
  const noteNum = Number(note);
  if (!Number.isInteger(noteNum) || noteNum < 1 || noteNum > 5) {
    return reponse({ error: "Note invalide" }, 400);
  }
  if (commentaire != null && (typeof commentaire !== "string" || commentaire.length > 1000)) {
    return reponse({ error: "Commentaire trop long" }, 400);
  }
  if (nom != null && (typeof nom !== "string" || nom.length > 60)) {
    return reponse({ error: "Nom trop long" }, 400);
  }
  if (typeof turnstile_token !== "string" || !turnstile_token) {
    return reponse({ error: "Vérification anti-robot manquante" }, 400);
  }

  const ip = req.headers.get("x-forwarded-for");
  const humain = await verifierTurnstile(turnstile_token, ip);
  if (!humain) return reponse({ error: "Vérification anti-robot échouée" }, 403);

  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
  );

  const commentaireNet = commentaire ? commentaire.trim().slice(0, 1000) : null;
  const nomNet = nom ? nom.trim().slice(0, 60) : null;

  const { error } = await supabase.from("avis").insert({
    page_url,
    page_title,
    note: noteNum,
    commentaire: commentaireNet,
    nom: nomNet,
    approuve: false,
  });

  if (error) return reponse({ error: "Enregistrement impossible" }, 500);

  await notifierParMail({ page_url, page_title, note: noteNum, commentaire: commentaireNet, nom: nomNet });

  return reponse({ ok: true });
});
