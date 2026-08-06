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
  /* Le site est statique : il ne peut rien enregistrer ni envoyer. Les
     boutons composent un message pre-rempli dans la messagerie du visiteur.
     L'adresse est assemblee ici plutot qu'ecrite dans le HTML, pour ne pas
     etre aspiree telle quelle par les robots collecteurs. */
  var MAIL = ["jordan.poncetpro", "gmail.com"].join("@");

  function ouvrirMessage(sujet, corps) {
    window.location.href = "mailto:" + MAIL +
      "?subject=" + encodeURIComponent(sujet) +
      "&body=" + encodeURIComponent(corps);
  }

  var LIBELLES = {
    utile:     ["Retour positif", "Cette page m'a ete utile.\n\nCe qui m'a servi :\n"],
    incomplet: ["Page incomplete", "Il me semble qu'il manque quelque chose sur cette page.\n\nCe que je cherchais :\n"],
    erreur:    ["Signalement d'une erreur", "Je crois avoir repere une erreur.\n\nPassage concerne :\n\nCe qui me semble inexact :\n"],
    ajout:     ["Proposition d'ajout", "Je propose un ajout sur cette page.\n\nSujet propose :\n\nPourquoi ce serait utile :\n"]
  };

  document.querySelectorAll(".feedback .fb").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var bloc = btn.closest(".feedback");
      var titre = bloc.getAttribute("data-title") || document.title;
      var url = bloc.getAttribute("data-url") || location.pathname;
      var l = LIBELLES[btn.getAttribute("data-avis")] || LIBELLES.utile;
      ouvrirMessage(
        "[Comprendre pour tous] " + l[0] + " \u2014 " + titre,
        l[1] + "\n\n---\nPage : " + titre + "\n" + location.origin + url + "\n"
      );
      var note = bloc.querySelector(".feedback-note");
      if (note) {
        note.textContent = "Un message vient de s'ouvrir dans votre messagerie. "
          + "S'il ne s'ouvre pas, ecrivez a " + MAIL + ".";
      }
    });
  });

  var cf = document.getElementById("contact-form");
  if (cf) {
    cf.addEventListener("submit", function (e) {
      e.preventDefault();
      var sujet = document.getElementById("cf-sujet").value;
      var page = document.getElementById("cf-page").value.trim();
      var msg = document.getElementById("cf-message").value.trim();
      var info = document.getElementById("cf-fallback");
      if (!msg) {
        info.textContent = "Ecrivez d'abord un message.";
        return;
      }
      ouvrirMessage("[Comprendre pour tous] " + sujet,
                    msg + (page ? "\n\n---\nPage concernee : " + page : ""));
      info.textContent = "Un message vient de s'ouvrir dans votre messagerie. "
        + "S'il ne s'ouvre pas, ecrivez directement a " + MAIL + ".";
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
