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
**Concept:** Fraud casefile / network investigation with explainable decision paths.

- [ ] Audit implementation and live-demo limitations.
- [ ] Design original graph-investigation hero.
- [ ] Map relationships → features → risk score → explanation → investigation.
- [ ] Build a distinct casefile-style README with evidence-linked modules.
- [ ] Add real screenshots or clearly labeled diagrams and review setup.
- [ ] Verify README assets and remove unsupported performance claims.

### 03 — [FleetFlow](https://github.com/HuLaxx/FleetFlow) · **The Dispatch Atlas**
**Concept:** Operations map / control tower with route optimization and live events.

- [ ] Audit roadmap against actual implementation, particularly planned Kafka/Flink/optimization features.
- [ ] Create original route-and-telemetry hero.
- [ ] Show order → constraints → solver → proposed route → feedback data flow.
- [ ] Rewrite README around operational decisions and clear local-vs-hosted states.
- [ ] Verify commands and qualify unsubstantiated efficiency metrics.
- [ ] Inspect asset rendering and commit only documented improvements.

### 04 — [Shiftify](https://github.com/HuLaxx/Shiftify) · **Your Music, Your Data**
**Concept:** Music library as a constellation of records, not a streaming-service clone.

- [ ] Inspect current frontend and supported export workflows.
- [ ] Create refined kinetic music-library banner.
- [ ] Explain how privacy, sessions and exports actually work.
- [ ] Add readable product journey and real screenshots where available.
- [ ] Review privacy claims and README install instructions.
- [ ] Validate links and final visual layout.

### 05 — [my-portfolio](https://github.com/HuLaxx/my-portfolio) · **HuLaX Experiments**
**Concept:** A digital design laboratory and architecture atlas.

- [ ] Audit pages, constellation, interaction features and existing README.
- [ ] Build editorial visual identity emphasizing selected experiments.
- [ ] Create truthful frontend/CMS/AI capability diagram.
- [ ] Improve navigation and case study links; remove stale references.
- [ ] Verify visual assets, build and deployed route (if accessible).

### 06 — [BCPD](https://github.com/HuLaxx/BCPD) · **Regime Shift Observatory**
**Concept:** Statistical research notebook / changepoint timeline.

- [ ] Inspect files and assess whether executable research code or results are present.
- [ ] Create clearly labeled illustrative changepoint SVG.
- [ ] Document research question, methodology, datasets and limitations **only where evidenced**.
- [ ] Add reproducibility steps when runnable source becomes available.
- [ ] Validate scientific claims; never invent results or benchmarks.

### 07 — [HuLaxx](https://github.com/HuLaxx/HuLaxx) · **The Constellation Hub**
**Concept:** Your public-facing personal identity, linking the distinct project worlds.

- [x] Animated hero and original Project Constellation established.
- [x] Featured-project overview, engineering approach and secondary-build cards.
- [ ] Align language, status and links with each improved repository.
- [ ] Verify automated constellation updates and rendering after each redesign.
- [ ] Final cross-repository accessibility / coherence pass.

## More owned repos — connection required for direct edits

These appear on the public owner listing but **are not currently among repositories accessible to the GitHub integration**. Do not mark any edits complete without adding them to the installation.

### 08 — [Xchange](https://github.com/HuLaxx/Xchange) · **Campus Exchange**
- [ ] Grant repository access for edits.
- [ ] Audit source and define marketplace identity.
- [ ] Produce original discovery / exchange workflow art and README.
- [ ] Verify links and avoid claiming unimplemented payment flows.

### 09 — [TestVeh](https://github.com/HuLaxx/TestVeh) · **The Systems Workshop**
- [ ] Grant repository access for edits.
- [ ] Inspect Django / React authentication modules and dependencies.
- [ ] Create a systems-lab architecture illustration and technical README.
- [ ] Audit tracked build artifacts, local environments and sensitive files.

### 10 — [Calendar-In-C](https://github.com/HuLaxx/Calendar-In-C) · **Retro Terminal**
- [ ] Grant repository access for edits.
- [ ] Inspect source (may be empty) before writing features.
- [ ] Create ANSI-terminal-inspired illustration.
- [ ] Add actual compilation or usage examples if source supports them.

---

**Checklist convention:** `[x]` means the stated work was actually performed or verified. `[ ]` means not yet complete. Static artwork and docs are not proof that a deployed service works.
