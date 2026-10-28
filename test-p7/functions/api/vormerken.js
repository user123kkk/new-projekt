// Cloudflare Pages Function: POST /api/vormerken
// Stores a launch-notice sign-up in the KV namespace bound as VORMERKUNGEN.
// Privacy (GRUNDSATZ rule 6): no logging of e-mail addresses, no IP storage, no cookies.
// Do NOT add console.log of the request body or headers here.

const MAX_EMAIL = 254;
const EMAIL_RE = /^[^\s@<>"',;:\\()[\]]+@[^\s@<>"',;:\\()[\]]+\.[^\s@<>"',;:\\()[\]]{2,}$/;

const HEADERS = { "Cache-Control": "no-store" };

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...HEADERS, "Content-Type": "application/json; charset=utf-8" },
  });
}

function errorPage(text) {
  const html = `<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Vormerken nicht möglich</title><style>body{margin:0;padding:0 16px;font:17px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#1b1b1b;background:#fff}main{max-width:640px;margin:0 auto;padding:28px 0 40px}a{color:#1d4e7a}</style></head><body><main><h1>Vormerken nicht möglich</h1><p>${text}</p><p><a href="/#vormerken">Zurück zum Formular</a></p></main></body></html>`;
  return new Response(html, {
    status: 400,
    headers: { ...HEADERS, "Content-Type": "text/html; charset=utf-8" },
  });
}

function isTruthy(v) {
  if (v === true) return true;
  if (typeof v !== "string") return false;
  return ["on", "true", "1", "yes", "ja"].includes(v.toLowerCase());
}

export async function onRequestPost({ request, env }) {
  const type = (request.headers.get("Content-Type") || "").toLowerCase();
  const isJson = type.includes("application/json");

  let email = "", consent = false, honeypot = "";
  try {
    if (isJson) {
      const d = await request.json();
      email = typeof d.email === "string" ? d.email : "";
      consent = isTruthy(d.consent);
      honeypot = typeof d.website === "string" ? d.website : "";
    } else {
      const d = await request.formData();
      email = String(d.get("email") || "");
      consent = isTruthy(String(d.get("consent") || ""));
      honeypot = String(d.get("website") || "");
    }
  } catch (e) {
    return isJson ? json({ ok: false, error: "bad_request" }, 400)
                  : errorPage("Die Anfrage konnte nicht gelesen werden.");
  }

  const fail = (code, text) =>
    isJson ? json({ ok: false, error: code }, 400) : errorPage(text);
  const success = () =>
    isJson ? json({ ok: true })
           : new Response(null, { status: 303, headers: { ...HEADERS, Location: "/danke.html" } });

  // Honeypot: bots fill the hidden field. Pretend success, store nothing.
  if (honeypot.trim() !== "") return success();

  email = email.trim();
  if (!email || email.length > MAX_EMAIL || !EMAIL_RE.test(email)) {
    return fail("invalid_email", "Die E-Mail-Adresse scheint nicht gültig zu sein.");
  }
  if (!consent) {
    return fail("consent_required", "Bitte stimmen Sie zu, dass wir Ihre E-Mail-Adresse für die Startmitteilung nutzen dürfen.");
  }
  if (!env.VORMERKUNGEN) {
    // Configuration error (binding missing). Message contains no personal data.
    return isJson ? json({ ok: false, error: "server_config" }, 500)
                  : new Response("Server nicht konfiguriert.", { status: 500, headers: HEADERS });
  }

  const key = email.toLowerCase();
  // Duplicates: keep the first entry, answer identically (do not reveal existence).
  const existing = await env.VORMERKUNGEN.get(key);
  if (existing === null) {
    await env.VORMERKUNGEN.put(
      key,
      JSON.stringify({ email: key, created: new Date().toISOString(), source: "p7" })
    );
  }
  return success();
}

// Any other method: no data, no side effects.
export async function onRequest() {
  return new Response("Method Not Allowed", { status: 405, headers: { ...HEADERS, Allow: "POST" } });
}
