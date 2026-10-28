# P2 demand test: files

Local only. Nothing is published or deployed.

- `vorlage-abnahmeprotokoll.html`: free, printable German acceptance report template with photo documentation (A4 print CSS). Open in a browser, print, "Save as PDF". Contains a not-legal-advice note and a general reference to § 650g BGB and § 634a BGB (as in IDEEN.md, K8 result for P2).
- `index.html`: German landing page. One sentence, target group, link to the template, one price placeholder, one action ("Vormerken", e-mail). States plainly that the app is not built and that sign-up only means being informed at launch, no payment.

Both files are plain HTML + CSS. No external resources, no tracking, no third-party fonts, no images of people or animals, no music, no ads. The only script is the inline `window.print()` on the template's print button.

## Fill before publishing

1. Price: replace `[PREIS]` in `index.html`.
2. Impressum: German legal notice with the owner's real name and address; point the `[IMPRESSUM]` link at it.
3. Privacy notice (Datenschutzerklärung): must cover the e-mail sign-up and the form provider; point the `[DATENSCHUTZ]` link at it. Have the wording checked.
4. Form provider: set `action` (and method) on the form in `index.html` (TODO comment there). Pick a provider with EU data processing, sign a data processing agreement, add double opt-in if required.
5. Domain and hosting.
6. Review the template's legal note before use.

## Measurement plan (IDEEN.md section 9)

1. Free entry point: the template page, searchable in German.
2. Offer on the same page: one sentence, one price, one action. No payment yet, stated plainly.
3. Traffic: search content first (0 EUR); then up to 100 EUR in search ads on terms like "Abnahmeprotokoll Vorlage".
4. Measure: template downloads, sign-ups, sign-up rate per visitor. The owner sets the decision threshold before launch. No sign-ups, nothing gets built.
5. Counting without tracking scripts (rule 6): use hosting server logs or a cookie-less privacy-friendly counter, and disclose it in the privacy notice. Not included in these files.
