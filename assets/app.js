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

  var LIBELLES = {
    utile:     ["Retour positif", "Cette page m'a ete utile.\n\nCe qui m'a servi :\n"],
    incomplet: ["Page incomplete", "Il me semble qu'il manque quelque chose sur cette page.\n\nCe que je cherchais :\n"],
    erreur:    ["Signalement d'une erreur", "Je crois avoir repere une erreur.\n\nPassage concerne :\n\nCe qui me semble inexact :\n"],
    ajout:     ["Proposition d'ajout", "Je propose un ajout sur cette page.\n\nSujet propose :\n\nPourquoi ce serait utile :\n"]
  };

  function brancherCompteur(textarea, compteur, max) {
    if (!textarea || !compteur) return;
    textarea.addEventListener("input", function () {
      compteur.textContent = String(Math.min(textarea.value.length, max));
    });
  }

  document.querySelectorAll(".feedback").forEach(function (bloc) {
    var panneau = bloc.querySelector(".feedback-panel");
    var texte = bloc.querySelector(".fb-msg");
    var nomChamp = bloc.querySelector(".fb-nom");
    var hp = bloc.querySelector(".fb-hp-input");
    var compteurN = bloc.querySelector(".fb-count-n");
    var note = bloc.querySelector(".feedback-note");
    var typeCourant = "utile";

    brancherCompteur(texte, compteurN, 2000);

    bloc.querySelectorAll(".fb").forEach(function (btn) {
      btn.addEventListener("click", function () {
        typeCourant = btn.getAttribute("data-avis") || "utile";
        var l = LIBELLES[typeCourant] || LIBELLES.utile;
        if (panneau) {
          panneau.hidden = false;
          if (texte) {
            texte.value = l[1];
            texte.focus();
            if (compteurN) compteurN.textContent = String(texte.value.length);
          }
        }
      });
    });

    var annuler = bloc.querySelector(".fb-cancel");
    if (annuler) {
      annuler.addEventListener("click", function () { panneau.hidden = true; });
    }

    if (panneau) {
      panneau.addEventListener("submit", function (e) {
        e.preventDefault();
        var titre = bloc.getAttribute("data-title") || document.title;
        var url = bloc.getAttribute("data-url") || location.pathname;
        var l = LIBELLES[typeCourant] || LIBELLES.utile;
        var nom = nomChamp ? nomChamp.value.trim() : "";
        var msg = texte ? texte.value.trim() : "";
        var corps = (nom || "Un\u00b7e visiteur\u00b7se") + " a dit \u00ab\u00a0" + msg + "\u00a0\u00bb"
          + "\n\n---\nType : " + l[0] + "\nPage : " + titre + "\n" + location.origin + url;
        envoyerFormulaire({
          subject: "[Comprendre pour tous] " + l[0] + " \u2014 " + titre,
          message: corps,
          nom: nom,
          honeypot: hp ? hp.value : ""
        }, function (ok, erreur) {
          if (note) {
            note.textContent = ok
              ? "Message envoy\u00e9, merci !"
              : (erreur || "Envoi impossible pour le moment.");
          }
          if (ok && panneau) { panneau.hidden = true; panneau.reset(); }
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
