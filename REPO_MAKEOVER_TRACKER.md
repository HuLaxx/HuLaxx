# HuLaX Repository Makeover — Master Checklist

> A shared design quality standard, **not** a shared template. Each repository gets its own visual identity, credible product story and appropriately scoped documentation.
>
> Last reviewed: 2026-11-06. Checkboxes record verified repository changes, not plans or untested performance claims.

## Quality bar for every repository

- [ ] Audit actual repository files, existing screenshots, setup instructions, demo URLs and maturity.
- [ ] Define a distinct creative concept and a single-line value proposition.
- [ ] Design or refine an original, self-hosted SVG hero with useful alt text.
- [ ] Add a meaningful diagram or real screenshots, clearly labeling conceptual illustrations.
- [ ] Restructure README: hook → why → how → evidence → setup → trade-offs → next steps.
- [ ] Make all repo links, demos and documentation references accurate.
- [ ] Remove misleading claims and decorative tests/coverage badges without verifiable sources.
- [ ] Verify GitHub markdown displays and files exist; test builds/CI when tools permit.
- [ ] Summarize changes and record remaining gaps.

## Repo-by-repo progress

### 01 — [Sentinance](https://github.com/HuLaxx/Sentinance) · **The Signal Atlas**

**Visual/documentation pass published.** [Open refreshed README](https://github.com/HuLaxx/Sentinance) · [Detailed checklist](https://github.com/HuLaxx/Sentinance/blob/main/docs/CREATIVE_CHECKLIST.md)
**Concept:** An AI market observatory: radar, streaming signals, prediction paths, and reasoning. Palette: midnight / sea-glass cyan / restrained amber.

- [x] Audit README, app stack, technical status inventory, existing artwork and architecture assets.
- [x] Establish bespoke **Signal Atlas** creative direction.
- [x] Find original [animated hero](https://github.com/HuLaxx/Sentinance/blob/main/docs/assets/signal-atlas-hero.svg) and [system map](https://github.com/HuLaxx/Sentinance/blob/main/docs/assets/signal-architecture.svg) already in repository.
- [x] Publish the redesigned README with both local assets and clear links.
- [x] Replace unsupported success statistics with evidence links or explicit verification requirements.
- [x] Add transparent deployed-vs-local-vs-optional capability status.
- [x] Verify README assets and all 34 local Markdown link targets exist.
- [ ] Review browser rendering and workflow status; these are not yet verified.
- [ ] Confirm actual end-to-end behaviour by running the system and tests (not verified from README inspection).

### 02 — [GraphGuard](https://github.com/HuLaxx/GraphGuard) · **The Evidence Graph**

**Visual/editorial pass published.** [Open redesigned README](https://github.com/HuLaxx/GraphGuard) · [Detailed checklist](https://github.com/HuLaxx/GraphGuard/blob/main/docs/CREATIVE_CHECKLIST.md)

**Concept:** A forensic investigation dossier: dark network casefile plus a contrasting paper evidence trail. Designed around the actual code paths and the question: *what does this transaction connect to?*

- [x] Audit source, mock-data cases, documented integration boundaries and historical evidence.
- [x] Create original animated [casefile hero](https://github.com/HuLaxx/GraphGuard/blob/main/docs/assets/evidence-graph-hero.svg).
- [x] Create contrasting [evidence trail](https://github.com/HuLaxx/GraphGuard/blob/main/docs/assets/investigation-trail.svg) from intake → graph → XGBoost → SHAP → investigation.
- [x] Publish a bespoke investigative README with linked implementation evidence and original demo GIF.
- [x] Explicitly distinguish mock/frontend cases, dated testing evidence, optional local stack and planned deployment.
- [x] Verify both SVG files and all 33 local README links exist.
- [ ] Validate actual GitHub mobile/desktop rendering and current CI, live demo and full local integration.

### 03 — [FleetFlow](https://github.com/HuLaxx/FleetFlow) · **The Dispatch Atlas**

**Visual/editorial pass published.** [Open redesigned README](https://github.com/HuLaxx/FleetFlow) · [Detailed checklist](https://github.com/HuLaxx/FleetFlow/blob/main/docs/CREATIVE_CHECKLIST.md)

**Concept:** A dispatch operations log with an animated city-grid route study and a paper-style routing decision sheet. No recycled casefile or observatory layout.

- [x] Audit solver and FastAPI route proposal, frontend tRPC bridge, sample map geometry, WebSocket/event modules and local-readiness criteria.
- [x] Publish original [animated Dispatch Atlas hero](https://github.com/HuLaxx/FleetFlow/blob/main/docs/dispatch-atlas.svg).
- [x] Publish original [dispatch decision worksheet](https://github.com/HuLaxx/FleetFlow/blob/main/docs/dispatch-decision-sheet.svg) centered on manifest → constraints → route proposal.
- [x] Rewrite README as a dispatcher's operational story with evidence-linked implementation, rather than a technology checklist.
- [x] Replace unsupported efficiency percentages/latency claims and explicitly document demo fixtures, optional local services and route preview.
- [x] Confirm both SVGs have sound tag structure and all 34 local README references exist.
- [ ] Run tests/local validation and independently inspect mobile GitHub rendering and the hosted demo.

### 04 — [Shiftify](https://github.com/HuLaxx/Shiftify) · **The Music Passport**

**Visual/editorial pass published.** [Open redesigned README](https://github.com/HuLaxx/Shiftify) · [Detailed checklist](https://github.com/HuLaxx/Shiftify/blob/master/docs/CREATIVE_CHECKLIST.md)

**Concept:** A playful vinyl-record sleeve and fold-out liner notes, focused on **portability and honest trust boundaries**—not a recycled dashboard.

- [x] Audit Next.js import/normalize/review/CSV reporting, YouTube Music account adapter, SQLite and optional party mode.
- [x] Publish custom [animated record sleeve](https://github.com/HuLaxx/Shiftify/blob/master/docs/music-passport.svg).
- [x] Publish custom [liner-notes workflow](https://github.com/HuLaxx/Shiftify/blob/master/docs/liner-notes.svg) distinguishing server-backed imports from cookie-based transfer.
- [x] Publish an original README with real source links and clearly qualified feature status.
- [x] Correct inaccurate browser-only/privacy marketing and show a visible cookie-handling warning in the transfer interface.
- [x] Verify all 13 local README paths and both SVGs' basic accessibility and syntax.
- [x] Add Shiftify to the portfolio projects and publish a bespoke illustrated case study in the portfolio source.
- [ ] Independently verify deployment and builds; security audit/auth on import and transfer APIs remains essential.

### 05 — [my-portfolio](https://github.com/HuLaxx/my-portfolio) · **HuLaX Studio / The Making Of**

**Visual/editorial pass published.** [Studio journal source](https://github.com/HuLaxx/my-portfolio/tree/master/src/app/studio) · [Live-route target](https://portfolio.hulax.uk/studio) · [Detailed checklist](https://github.com/HuLaxx/my-portfolio/blob/master/docs/CREATIVE_CHECKLIST.md)

**Concept:** An open field journal and animated editorial contact sheet explaining how the portfolio is constructed—not another product dashboard or a generic README.

- [x] Audit the homepage, case studies, Three.js and motion layers, optional Sanity content, AI endpoint and GitHub integration.
- [x] Create the original [Studio Contact Sheet](https://github.com/HuLaxx/my-portfolio/blob/master/public/studio/studio-contact-sheet.svg) and [exploded architecture study](https://github.com/HuLaxx/my-portfolio/blob/master/public/studio/exploded-system.svg).
- [x] Publish a responsive **Making Of** studio page, link it from Projects and rewrite the GitHub README as a creative journal.
- [x] Curate four distinct original SVG project posters in their portfolio case studies.
- [x] Correct stale graduation/Next.js/LinkedIn claims in README, align canonical metadata and remove misleading AI terminal prompts.
- [x] Replace unsupported project benchmark numbers in case-study fallback content with clearly qualified implementation facts.
- [x] Verify 13 local README links, 9 checklist links, four poster assets, 36 CSS module classes and both new SVG structures.
- [ ] Run lint/build and verify the deployed Studio route, mobile rendering, accessibility, performance and media licenses.

### 06 — [BCPD](https://github.com/HuLaxx/BCPD) · **Regime Shift Laboratory**

**Functional application committed and independently deployed.** [Source code](https://github.com/HuLaxx/BCPD) · [Live BCPD laboratory](https://hulax-bcpd-regime-lab.vercel.app)

**Concept:** An interactive Bayesian research workbench, not just an infographic or research poster.

- [x] Replace the previously empty repo with a complete static application on main.
- [x] Implement Gaussian-mean Bayesian online change-point detection, normalized run-length posterior and a change-point probability plot.
- [x] Add editable and CSV observations, seeded sample data, visualizations and result CSV export.
- [x] Commit Node unit tests, local-running instructions and a Vercel static deployment configuration.
- [x] Deploy directly to Vercel; deployment dpl_BUTyrqEiyQsPQm7KnVvePXK8kkWE reported READY.
- [ ] Independently exercise all user flows in a live browser and validate current scientific test outcomes.
- [ ] Connect the Vercel project to GitHub for future automatic redeploys; GitHub Login Connection is currently missing.

### 07 — [HuLaxx](https://github.com/HuLaxx/HuLaxx) · **The Constellation Hub**
**Concept:** Your public-facing personal identity, linking the distinct project worlds.

- [x] Animated hero and original Project Constellation established.
- [x] Featured-project overview, engineering approach and secondary-build cards.
- [ ] Align language, status and links with each improved repository.
- [ ] Verify automated constellation updates and rendering after each redesign.
- [ ] Final cross-repository accessibility / coherence pass.

## Other applications / functional rebuilds

### 08 — [Xchange](https://github.com/HuLaxx/Xchange) · **Pass the Story On**

- [x] Audit legacy React/Express frontend and local MySQL/MongoDB assumptions.
- [x] Build a separate functional local-first book marketplace with listing forms, filters, favourites, validation and request drafts.
- [x] Run the local model/unit tests (2 passing).
- [x] Prepare standalone Vercel static deployment settings and source package.
- [ ] Publish files into the original Xchange repo; GitHub integration currently rejects write operations (403).
- [ ] Deploy to Vercel and validate an actual public URL.
- [ ] Add authenticated shared storage and messaging before calling this a multi-user service.

### 09 — [TestVeh](https://github.com/HuLaxx/TestVeh) · **Vehicle Registry Studio**

- [x] Audit the legacy Django/React authentication app and tracked virtual environment.
- [x] Build a new functional local-first vehicle registry with record CRUD, search, validations, document review statuses and CSV export.
- [x] Run local model/unit tests (4 passing).
- [x] Prepare Vercel static deployment settings and source package.
- [ ] Publish into the original TestVeh repo; GitHub integration currently rejects write operations (403).
- [ ] Deploy to Vercel and validate an actual public URL.
- [ ] Add identity checks, server-side authorization and audit trails before using real registration data.

**Calendar-In-C has been removed from the public makeover/showcase plan.** Its repository has not been deleted.


---

**Checklist convention:** `[x]` means the stated work was actually performed or verified. `[ ]` means not yet complete. Static artwork and docs are not proof that a deployed service works.
