/* Comprendre pour tous — thème clair/sombre + recherche plein texte. */
(function () {
  "use strict";

  /* ------------------------------------------------------------- thème */
  var root = document.documentElement;
  var btn = document.querySelector(".theme-btn");
  if (btn) {
    btn.addEventListener("click", function () {
      var dark = root.dataset.theme
        ? root.dataset.theme === "dark"
        : window.matchMedia("(prefers-color-scheme: dark)").matches;
      var next = dark ? "light" : "dark";
      root.dataset.theme = next;
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  /* ------------------------------- fermeture du menu mobile au clic ---- */
  var toggle = document.getElementById("nav-toggle");
  if (toggle) {
    document.querySelectorAll(".sidebar a").forEach(function (a) {
      a.addEventListener("click", function () { toggle.checked = false; });
    });
  }

  /* --------------------------- garder l'entrée active bien visible ---- */
  var active = document.querySelector(".nav-root a.active");
  if (active && window.innerWidth > 820) {
    var side = document.querySelector(".sidebar");
    if (side) {
      var top = active.offsetTop - side.clientHeight / 2;
      if (top > 0) side.scrollTop = top;
    }
  }

  /* ------------------------------- avis et contact (sans serveur) ----- */
  /* Le site reste statique : aucun compte, aucune base de donnees. Le
     formulaire et les boutons d'avis envoient directement le message par
     e-mail via Web3Forms (https://web3forms.com), qui ne fait que relayer
     vers l'adresse verifiee de l'auteur. Voir /confidentialite/#formulaire. */
  var MAIL = ["jordan.poncetpro", "gmail.com"].join("@");
  /* Cle publique Web3Forms, decoupee pour ne pas apparaitre en clair dans le
     texte source. Elle n'autorise que l'envoi vers l'adresse verifiee lors
     de la creation du compte Web3Forms, jamais la lecture des messages :
     ce n'est pas un secret a proteger, juste une valeur qu'on evite de
     laisser trivialement recopiable par un robot. */
  var WEB3FORMS_KEY = ["daada50b", "bc23", "4a7b", "b7f2", "30632276cf6c"].join("-");
  var WEB3FORMS_URL = "https://api.web3forms.com/submit";
  var RATE_LIMIT_MS = 30000; /* un envoi toutes les 30 secondes maximum */

  function peutEnvoyer() {
    try {
      var dernier = parseInt(localStorage.getItem("cpt_last_send") || "0", 10);
      return (Date.now() - dernier) > RATE_LIMIT_MS;
    } catch (e) { return true; }
  }
  function noterEnvoi() {
    try { localStorage.setItem("cpt_last_send", String(Date.now())); } catch (e) {}
  }

  /* Envoie un message via Web3Forms. `champHoneypot` doit rester vide : s'il
     est rempli, c'est un robot, et on simule un succes sans rien envoyer. */
  function envoyerFormulaire(opts, onDone) {
    if (opts.honeypot) { onDone(true); return; }
    if (!opts.message) { onDone(false, "Ecrivez d'abord un message."); return; }
    if (!peutEnvoyer()) {
      onDone(false, "Merci de patienter quelques secondes avant un nouvel envoi.");
      return;
    }
    if (WEB3FORMS_KEY.indexOf("REMPLACER") === 0) {
      onDone(false, "Formulaire pas encore relie (cle manquante). Ecrivez directement a " + MAIL + ".");
      return;
    }
    noterEnvoi();
    fetch(WEB3FORMS_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify({
        access_key: WEB3FORMS_KEY,
        subject: opts.subject,
        message: opts.message,
        from_name: opts.nom || "Site Comprendre pour tous"
      })
    }).then(function (r) { return r.json(); })
      .then(function (data) { onDone(!!data.success, data.success ? null : "Envoi impossible pour le moment."); })
      .catch(function () { onDone(false, "Envoi impossible (hors ligne ?). Ecrivez a " + MAIL + "."); });
  }

  function brancherCompteur(textarea, compteur, max) {
    if (!textarea || !compteur) return;
    textarea.addEventListener("input", function () {
      compteur.textContent = String(Math.min(textarea.value.length, max));
    });
  }

  /* Bloc d'amelioration en bas de page : un commentaire, envoye
     directement, sans etape de selection prealable. */
  document.querySelectorAll(".feedback").forEach(function (bloc) {
    var panneau = bloc.querySelector(".feedback-panel");
    var texte = bloc.querySelector(".fb-msg");
    var hp = bloc.querySelector(".fb-hp-input");
    var compteurN = bloc.querySelector(".fb-count-n");
    var note = bloc.querySelector(".feedback-note");

    brancherCompteur(texte, compteurN, 2000);

    if (panneau) {
      panneau.addEventListener("submit", function (e) {
        e.preventDefault();
        var titre = bloc.getAttribute("data-title") || document.title;
        var url = bloc.getAttribute("data-url") || location.pathname;
        var msg = texte ? texte.value.trim() : "";
        var corps = "Un\u00b7e visiteur\u00b7se a dit \u00ab\u00a0" + msg + "\u00a0\u00bb"
          + "\n\n---\nPage : " + titre + "\n" + location.origin + url;
        envoyerFormulaire({
          subject: "[Comprendre pour tous] Am\u00e9lioration ou signalement \u2014 " + titre,
          message: corps,
          honeypot: hp ? hp.value : ""
        }, function (ok, erreur) {
          if (note) {
            note.textContent = ok
              ? "Message envoy\u00e9, merci !"
              : (erreur || "Envoi impossible pour le moment.");
          }
          if (ok && panneau) { panneau.reset(); if (compteurN) compteurN.textContent = "0"; }
        });
      });
    }
  });

  var cf = document.getElementById("contact-form");
  if (cf) {
    brancherCompteur(document.getElementById("cf-message"), document.getElementById("cf-count-n"), 4000);
    cf.addEventListener("submit", function (e) {
      e.preventDefault();
      var sujet = document.getElementById("cf-sujet").value;
      var page = document.getElementById("cf-page").value.trim();
      var nom = document.getElementById("cf-nom").value.trim();
      var msg = document.getElementById("cf-message").value.trim();
      var hp = document.getElementById("cf-hp");
      var info = document.getElementById("cf-fallback");
      var corps = (nom || "Un\u00b7e visiteur\u00b7se") + " a dit \u00ab\u00a0" + msg + "\u00a0\u00bb"
        + (page ? "\n\n---\nPage concernee : " + page : "");
      envoyerFormulaire({
        subject: "[Comprendre pour tous] " + sujet + (page ? " \u2014 " + page : ""),
        message: corps,
        nom: nom,
        honeypot: hp ? hp.value : ""
      }, function (ok, erreur) {
        info.textContent = ok
          ? "Message envoy\u00e9, merci ! Vous pouvez fermer cette page."
          : (erreur || "Envoi impossible pour le moment.");
        if (ok) cf.reset();
      });
    });
  }

  /* --------------------------------------- avis publics (Supabase) ---- */
  /* Contrairement au bloc d'amelioration ci-dessus (envoi direct par
     e-mail, jamais stocke), les avis sont conserves et affiches
     publiquement, mais seulement apres relecture manuelle (colonne
     "approuve" dans Supabase). Voir /confidentialite/#avis. */
  var SUPABASE_URL = "https://zufscjxwnbkadcygvzcp.supabase.co";
  var SUPABASE_ANON_KEY = "sb_publishable_zshz05tNZomvbt5JGHQkXQ_gvukztL3";
  var AVIS_FUNCTION_URL = SUPABASE_URL + "/functions/v1/swift-handler";
  var pasConfigure = SUPABASE_URL.indexOf("REMPLACER") !== -1;

  function supabaseGet(chemin) {
    return fetch(SUPABASE_URL + "/rest/v1/" + chemin, {
      headers: { apikey: SUPABASE_ANON_KEY, Authorization: "Bearer " + SUPABASE_ANON_KEY }
    }).then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); });
  }

  function formaterAvis(a) {
    var etoiles = "★".repeat(a.note) + "☆".repeat(5 - a.note);
    var auteur = a.nom ? esc2(a.nom) : "Un·e lecteur·rice";
    var com = a.commentaire ? "<p>" + esc2(a.commentaire) + "</p>" : "";
    return '<li><div class="avis-item-head"><span class="avis-stars-ro" aria-hidden="true">' + etoiles +
           '</span><strong>' + auteur + '</strong></div>' + com + '</li>';
  }
  function esc2(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  document.querySelectorAll(".avis").forEach(function (bloc) {
    var url = bloc.getAttribute("data-url") || location.pathname;
    var titre = bloc.getAttribute("data-title") || document.title;
    var liste = bloc.querySelector(".avis-liste");
    var form = bloc.querySelector(".avis-form");
    var stars = bloc.querySelectorAll(".star-btn");
    var noteInput = bloc.querySelector(".avis-note");
    var texte = bloc.querySelector(".avis-msg");
    var nomChamp = bloc.querySelector(".avis-nom");
    var hp = bloc.querySelector(".avis-hp-input");
    var compteur = bloc.querySelector(".avis-count-n");
    var noteMsg = bloc.querySelector(".avis-note-msg");
    var turnstileDiv = bloc.querySelector(".cf-turnstile");
    var dejaNote = false;
    try { dejaNote = !!localStorage.getItem("cpt_avis_" + url); } catch (e) {}

    brancherCompteur(texte, compteur, 1000);

    if (pasConfigure) {
      if (liste) liste.innerHTML = '<p class="muted">Avis pas encore activés sur ce site.</p>';
      if (form) form.hidden = true;
      return;
    }

    /* affichage des avis approuves + moyenne */
    var champAvis = "page_url=eq." + encodeURIComponent(url) +
      "&approuve=eq.true&select=note,commentaire,nom,cree_le&order=cree_le.desc&limit=20";
    supabaseGet("avis?" + champAvis).then(function (avis) {
      if (!liste) return;
      if (!avis.length) {
        liste.innerHTML = '<p class="muted">Aucun avis publié pour l’instant. Soyez le premier·ère.</p>';
        return;
      }
      var moyenne = avis.reduce(function (s, a) { return s + a.note; }, 0) / avis.length;
      liste.innerHTML = '<p class="avis-moyenne"><strong>' + moyenne.toFixed(1) + '/5</strong> sur ' +
        avis.length + (avis.length > 1 ? ' avis' : ' avis') + '</p><ul class="avis-items">' +
        avis.map(formaterAvis).join("") + '</ul>';
    }).catch(function () {
      if (liste) liste.innerHTML = '<p class="muted">Avis indisponibles pour le moment.</p>';
    });

    /* etoiles cliquables */
    stars.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var v = parseInt(btn.getAttribute("data-valeur"), 10);
        if (noteInput) noteInput.value = String(v);
        stars.forEach(function (b) {
          b.classList.toggle("is-active", parseInt(b.getAttribute("data-valeur"), 10) <= v);
        });
      });
    });

    if (dejaNote && form) {
      form.hidden = true;
      if (noteMsg) noteMsg.textContent = "Vous avez déjà envoyé un avis pour cette page, merci !";
    }

    if (form && !dejaNote) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (hp && hp.value) return; /* robot : on ne fait rien, silencieusement */
        var note = noteInput ? parseInt(noteInput.value, 10) : 0;
        if (!note) {
          if (noteMsg) noteMsg.textContent = "Choisissez une note avant d'envoyer.";
          return;
        }
        var tokenInput = turnstileDiv ? turnstileDiv.querySelector('[name="cf-turnstile-response"]') : null;
        var token = tokenInput ? tokenInput.value : "";
        if (!token) {
          if (noteMsg) noteMsg.textContent = "Merci de valider la vérification anti-robot.";
          return;
        }
        fetch(AVIS_FUNCTION_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json", apikey: SUPABASE_ANON_KEY },
          body: JSON.stringify({
            page_url: url,
            page_title: titre,
            note: note,
            commentaire: texte ? texte.value.trim() : "",
            nom: nomChamp ? nomChamp.value.trim() : "",
            honeypot: hp ? hp.value : "",
            turnstile_token: token
          })
        }).then(function (r) { return r.json(); })
          .then(function (data) {
            if (data.ok) {
              try { localStorage.setItem("cpt_avis_" + url, "1"); } catch (e) {}
              form.hidden = true;
              if (noteMsg) noteMsg.textContent = "Merci, votre avis sera publié après relecture.";
            } else {
              if (noteMsg) noteMsg.textContent = data.error || "Envoi impossible pour le moment.";
              if (window.turnstile && turnstileDiv) window.turnstile.reset(turnstileDiv);
            }
          })
          .catch(function () {
            if (noteMsg) noteMsg.textContent = "Envoi impossible (hors ligne ?).";
          });
      });
    }
  });

  /* carte "Vos tops" de l'accueil */
  var topCard = document.getElementById("top-pages-card");
  if (topCard && !pasConfigure) {
    supabaseGet("avis_stats?select=page_url,page_title,moyenne,nombre&order=moyenne.desc&limit=5")
      .then(function (tops) {
        if (!tops.length) return;
        var liste = topCard.querySelector(".top-pages-list");
        liste.innerHTML = tops.map(function (t) {
          return '<li><a href="' + t.page_url + '">' + esc2(t.page_title) + '</a> — ' +
            Number(t.moyenne).toFixed(1) + '/5 (' + t.nombre + ')</li>';
        }).join("");
        topCard.hidden = false;
      })
      .catch(function () {});
  }

  /* --------------------------------------------------------- recherche */
  var input = document.getElementById("q");
  var results = document.getElementById("results");
  var status = document.getElementById("search-status");
  if (!input || !results) return;

  var form = document.getElementById("search-form");
  if (form) form.addEventListener("submit", function (e) { e.preventDefault(); });

  var index = null;

  function normalize(s) {
    return (s || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function highlight(text, terms) {
    var out = escapeHtml(text);
    terms.forEach(function (t) {
      if (t.length < 2) return;
      var norm = normalize(out);
      var at = norm.indexOf(t);
      if (at === -1) return;
      out = out.slice(0, at) + "<mark>" + out.slice(at, at + t.length) +
            "</mark>" + out.slice(at + t.length);
    });
    return out;
  }

  function snippet(content, terms) {
    var norm = normalize(content);
    var at = -1;
    for (var i = 0; i < terms.length; i++) {
      at = norm.indexOf(terms[i]);
      if (at !== -1) break;
    }
    if (at === -1) return content.slice(0, 170) + "…";
    var start = Math.max(0, at - 70);
    var text = (start > 0 ? "…" : "") + content.slice(start, start + 210) + "…";
    return highlight(text, terms);
  }

  function search(query) {
    var terms = normalize(query).split(/\s+/).filter(function (t) { return t.length > 1; });
    if (!terms.length) { results.innerHTML = ""; status.textContent = ""; return; }

    var hits = [];
    index.forEach(function (page) {
      var title = normalize(page.t);
      var body = normalize(page.c);
      var score = 0;
      var all = true;
      terms.forEach(function (t) {
        var inTitle = title.indexOf(t) !== -1;
        var inBody = body.indexOf(t) !== -1;
        if (!inTitle && !inBody) { all = false; return; }
        if (inTitle) score += title === t ? 120 : 40;
        if (inBody) {
          var n = body.split(t).length - 1;
          score += Math.min(n, 12);
        }
      });
      if (all && score > 0) hits.push({ page: page, score: score });
    });

    hits.sort(function (a, b) { return b.score - a.score; });

    if (!hits.length) {
      results.innerHTML = "";
      status.textContent = "Aucun résultat pour « " + query + " ».";
      return;
    }
    status.textContent = hits.length + (hits.length > 1 ? " résultats" : " résultat") +
                         " pour « " + query + " »";

    results.innerHTML = hits.slice(0, 40).map(function (h) {
      var p = h.page;
      return '<li><h3><a href="' + p.u + '">' + highlight(p.t, terms) + "</a></h3>" +
             (p.s ? '<span class="where">' + escapeHtml(p.s) + "</span>" : "") +
             "<p>" + snippet(p.c || p.x, terms) + "</p></li>";
    }).join("");
  }

  var pending = new URLSearchParams(window.location.search).get("q") || "";
  if (pending) input.value = pending;

  fetch("/search-index.json")
    .then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    })
    .then(function (data) {
      index = data;
      status.textContent = index.length + " pages indexées. Tapez pour chercher.";
      var timer;
      input.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(function () { search(input.value); }, 120);
      });
      if (pending) search(pending);
      input.focus();
    })
    .catch(function () {
      status.textContent = "L'index de recherche n'a pas pu être chargé.";
    });
})();
