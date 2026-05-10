---
title: "Single-Artifact, Multi-Authority Evidence Engineering for Healthcare Compliance"
description: "Healthcare compliance has become a layered audit problem. The only way a small team survives it is to design four anchor artifacts that each satisfy multiple authorities."
publishDate: 2026-05-14
author: "Justin T. Begarek"
lane: research
topics:
  - Healthcare
  - Compliance
  - HIPAA
  - Risk Management
  - Strategy
featured: false
draft: false
citations: false
diagrams: false
---

A small healthcare cybersecurity team in 2026 is asked to satisfy HIPAA, the HIPAA Security Rule NPRM (when finalized), HHS Healthcare and Public Health Cybersecurity Performance Goals, the FTC Health Breach Notification Rule, ONC HTI-1, NIST CSF 2.0, NIST AI RMF, FDA PCCP guidance for AI-enabled devices, the EU AI Act, the Colorado AI Act, the SEC cybersecurity disclosure rule (for public-company partners), CIRCIA when it finalizes, CMMC Level 2 for any defense-adjacent work, customer contractual clauses, BAA flow-down, and SOC 2.

Some of these are voluntary. Most overlap. None harmonize.

A team that maintains separate evidence streams for each authority will not survive the calendar. The economically defensible response is not "do less compliance." It is to design the smallest set of anchor artifacts that can each satisfy multiple authorities, and to engineer evidence around those artifacts so a single body of work serves every audience.

This post explains the four anchor artifacts, why they were chosen, and how they map to current and anticipated healthcare compliance regimes.

---

## The Problem: Velocity, Fragmentation, and Status Ambiguity

Three structural pressures make the static, audit-cycle compliance model untenable for small healthcare teams.

**Velocity asymmetry.** Federal rulemaking output between 2024 and 2027 has outpaced annual-policy-review cadence. NIST CSF 2.0 (Feb 2024), ONC HTI-1 (Mar 2024), FTC HBNR amendments (Jul 2024), FIPS 203/204/205 (Aug 2024), the HIPAA Security Rule NPRM (Jan 2025), CMMC final rules (32 CFR Part 170 in 2024 and 48 CFR DFARS effective Nov 10, 2025), FDA AI PCCP (Aug 2025), CISA Cross-Sector CPGs v2.0 (Dec 2025), and FDA's 2026 medical-device cybersecurity guidance all landed inside roughly two years. A frozen policy baseline is materially out of date by year-end.

**Authority fragmentation.** AI alone now has six overlapping authority sources across federal, state, and international regimes. Healthcare cybersecurity has at least eight (HHS, OCR, FDA, ONC, FTC, CISA, SEC, state AGs). Each requires evidence in its own format. Maintaining parallel evidence streams produces audit-day scrambles and quality regressions.

**Status ambiguity.** A 2026 healthcare compliance program operates under three legal weights at once: rules that are final and binding, rules that are proposed (HIPAA NPRM, CIRCIA), rules that are enacted but not yet effective (Colorado AI Act, EU AI Act high-risk obligations), and rules that were briefly effective and have been vacated (the 2024 HIPAA reproductive-health privacy rule, mostly vacated June 18, 2025 in *Purl v. HHS*). Customers and procurement still ask about all of them.

The combination produces an evidence-engineering problem, not a control-selection problem. A small team cannot solve it by buying more tools or hiring more analysts. It can solve it by reducing the number of artifacts it must maintain to the smallest defensible set.

---

## The Four Anchor Artifacts

Four artifacts, designed once and maintained continuously, can serve almost every healthcare compliance authority a small team will encounter.

### 1. AI Use-Case Dossier

A single record per AI use case, structured to satisfy NIST AI RMF, FDA PCCP, ONC HTI-1, the EU AI Act, the Colorado AI Act, and HIPAA risk analysis simultaneously. Fields cover identification, use-case description, data lineage, model and validation, modification protocol, monitoring, human oversight, transparency, incident handling, and risk register entry. See the [cross-jurisdiction AI compliance stack](/blog/cross-jurisdiction-ai-compliance-healthcare-stack) for the full field structure.

The dossier replaces six parallel AI documentation streams with one. A small team can sustain one dossier per use case. It cannot sustain six.

### 2. Unified IoMT/IoT/OT Asset Register

A single asset register that includes connected medical devices, IoT, building systems, OT, and any device that produces or consumes ePHI or sits on a network with ePHI. The register draws from NIST SP 800-213 device cybersecurity capabilities (Fagan et al., 2021) and NIST SP 800-82 Rev. 3 OT security guidance (Stouffer et al., 2023). Each asset record carries device identity, segmentation context, patching status, vendor, SBOM availability, FDA 524B status (where applicable), and clinical-availability impact tier.

This single artifact satisfies HIPAA NPRM asset-inventory requirements, HHS HPH CPG essentials, FDA medical-device cybersecurity expectations, CMMC asset categorization where defense-adjacent CUI is in scope, and CIRCIA-readiness scoping. It also feeds the IoMT segmentation diagrams that customer audits and OCR investigations now request.

### 3. Single Data-Flow Inventory

One queryable inventory that records every flow of regulated data — ePHI, CUI, consumer health data, EU resident data — between systems, vendors, APIs, and jurisdictions. Each flow records source, destination, data classes, regulatory regime, retention, encryption posture, vendor relationship, and data-residency scope.

This artifact satisfies HIPAA risk analysis scoping (per NIST SP 800-66 Rev. 2; Marron, 2024), CMMC scoping (per the CMMC Scoping Guide), shared-responsibility analysis for cloud and SaaS, FTC HBNR coverage analysis, EU AI Act and GDPR cross-border records, Colorado AI Act records, ONC HTI-1 API inventory, and CIRCIA-readiness scoping. Cross-border data flow scholarship (Xia et al., 2024) supports the inventory's structural design.

A data-flow inventory also resolves the most common procurement gap: questions about where data lives and who reaches it cannot be answered from policy. They can be answered from a current inventory.

### 4. Cryptographic Inventory

One inventory of every cryptographic dependency across applications, infrastructure, vendors, and devices, with algorithm, key length, protocol context, data sensitivity tier, ownership, and PQC migration status. NIST SP 800-57 Pt. 1 Rev. 5 (Barker, 2025) and SP 800-131A Rev. 3 (NIST, 2025) anchor the methodology.

This artifact satisfies HIPAA encryption controls, the HIPAA NPRM's proposed FIPS-aligned encryption posture, CMMC SC family controls, FedRAMP cryptographic transition, NSM-10 federal alignment, and PQC vendor-roadmap collection. It is also the foundation for any defensible 2027 to 2035 migration plan to FIPS 203/204/205. See [post-quantum cryptography for healthcare](/blog/post-quantum-cryptography-healthcare-hndl-roadmap) for the migration framing.

---

## Why These Four

The selection is constrained by a small-team operating reality: each artifact must be (a) sustainable by a non-dedicated team, (b) updated by routine operations rather than audit prep, (c) reusable across at least four compliance authorities, and (d) the foundation of multiple other downstream artifacts.

The four artifacts pass that test. Risk analyses, segmentation diagrams, audit-log retention proofs, vendor packets, training records, and incident reports can all be derived from these four anchors. Without the anchors, every downstream artifact is built independently, and the work compounds.

A larger team can maintain more artifacts. A small team needs ruthless artifact discipline.

---

## How This Connects to Continuous Compliance

The four anchors only work inside a continuing compliance capability. NIST SP 800-137 (Dempsey et al., 2011) supplies the federal continuous-monitoring model, NIST CSF 2.0 (NIST, 2024d) supplies the Govern function that makes evidence engineering an organizational responsibility, and NIST SP 800-30 Rev. 1 (Joint Task Force, 2012) supplies the methodological backbone for the risk analyses that the data-flow and asset inventories feed.

Twelve operating components — compliance intelligence monitoring, legal review cadence, control mapping, risk assessment refresh, vendor and supply chain review, policy updates, technical control implementation, audit evidence collection, board and executive reporting, workforce training, incident reporting readiness, and continuous improvement — together produce and consume the four anchors on a sustainable cadence.

The artifacts are the load-bearing structure. The capabilities are the operating tempo.

---

## What This Replaces

Three operating habits should be retired by a small healthcare cybersecurity team adopting this model.

**Per-customer evidence packets built from scratch.** A new customer should pull from existing anchors, not generate a parallel set.

**Per-authority documentation streams.** AI documentation, HIPAA documentation, CMMC documentation, and SOC 2 documentation should not be separate filing systems. They should be different views of the same anchors.

**Annual policy reviews as the primary update mechanism.** The compliance environment moves faster than annual review. The anchors get updated continuously; policy review becomes a reconciliation event, not a discovery event.

This is not a maturity-model graduation. It is a structural shift from compliance-as-event to compliance-as-capability.

---

## What to Track

The hardest part of this model is sustaining the anchors when the underlying regimes change. Three signals matter most:

- HIPAA Security Rule final rule and associated NIST SP 800-66 updates.
- EU AI Act high-risk obligation guidance from the AI Office through 2027.
- CMMC assessment guide revisions and DoD CIO scoping updates.

Anchors that are not updated against these signals decay. Anchors that are updated continuously become the most valuable artifact a small healthcare cybersecurity team owns.

---

## Sources

- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898.
- HHS. (2024). *HPH Cybersecurity Performance Goals*.
- NIST. (2024). *Cybersecurity Framework 2.0* (CSWP 29).
- Marron, J. (2024). *NIST SP 800-66 Rev. 2*.
- Fagan et al. (2021). *NIST SP 800-213*.
- Stouffer et al. (2023). *NIST SP 800-82 Rev. 3*.
- Barker, E. (2025). *NIST SP 800-57 Pt. 1 Rev. 5*.
- NIST. (2024). *FIPS 203, 204, 205*.
- Dempsey et al. (2011). *NIST SP 800-137*.
- Xia, L., Cao, Z., & Zhao, Y. (2024). *Risk Management and Healthcare Policy, 17*, 3115-3132.
