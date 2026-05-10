---
title: "FDA Predetermined Change Control Plans for AI-Enabled Medical Devices: What a PCCP Actually Is"
description: "FDA's August 2025 PCCP guidance lets AI-enabled medical devices iterate without resubmission. What a PCCP must contain, when it makes sense, and how it interacts with HIPAA."
publishDate: 2026-05-19
author: "Justin T. Begarek"
lane: practical
topics:
  - Healthcare
  - AI
  - FDA
  - Compliance
  - Medical Devices
featured: false
draft: false
citations: false
diagrams: false
---

AI-enabled medical devices have a problem that traditional medical devices do not. Their behavior is supposed to change after deployment. Models retrain on new data. Decision thresholds get tuned against real-world performance. Underlying foundation models update underneath the device. Each of those changes can shift the device's safety and effectiveness profile.

The traditional FDA model — premarket review, then a new submission for any modification — does not handle this well. AI-enabled devices that need to iterate would otherwise face a choice between freezing model behavior (defeating the purpose of AI) or filing repeated supplements (commercially impractical).

FDA's Predetermined Change Control Plan (PCCP) framework, finalized August 18, 2025 (originally issued December 4, 2024 as draft), gives AI-enabled device manufacturers a structured way out. A PCCP describes planned modifications, the methodology used to develop and validate them, and the impact assessment used to maintain reasonable assurance of safety and effectiveness. Where a PCCP is included in a marketing submission and FDA agrees to it, the device may iterate within the PCCP envelope without a new submission.

This post explains what a PCCP must contain, when one is appropriate, and how PCCP evidence intersects with HIPAA risk analysis, NIST AI RMF, ONC HTI-1, and the EU AI Act.

---

## What a PCCP Must Contain

A PCCP is a structured document with three required components.

**Description of planned modifications.** What changes the manufacturer plans to make to the AI-enabled device software function over the device's lifecycle. Examples include retraining frequency, performance threshold adjustments, expansion of input data sources, addition of new clinical use cases within the same intended use, or updates to underlying foundation models. The description must be specific enough that FDA can evaluate whether the modifications stay within an acceptable safety envelope.

**Modification protocol.** The methodology the manufacturer will use to develop, validate, and implement each planned modification. This includes the data the modification will be trained or evaluated on, the validation methods that will be used, the performance metrics that will be tracked, the rollback procedures if performance degrades, the version control approach, and the documentation generated for each modification cycle.

**Impact assessment.** An analysis of how the planned modifications could affect safety and effectiveness, including risk identification, mitigation strategies, and the rationale for the manufacturer's belief that modifications within the PCCP envelope maintain reasonable assurance of safety and effectiveness.

The three components together form an evidentiary structure: planned scope (what), method (how), and risk control (why it stays safe). FDA review focuses on whether the protocol and impact assessment make the planned scope defensible.

---

## When a PCCP Is Appropriate

PCCP is not required for every AI-enabled device. It is most useful when three conditions are met:

The device's intended use includes ongoing modification. Devices whose AI component is genuinely static do not need a PCCP. Many AI-enabled devices are static after release; the AI was used in development, but the deployed device behavior is fixed.

The planned modifications can be specified in advance with enough rigor that FDA can evaluate them. PCCP is not a license for unbounded model evolution. It is a structured commitment to stay within a described envelope.

The safety profile is sensitive enough to modification that a structured update process is preferable to repeated supplements. For high-risk devices, the upfront PCCP investment pays off across multiple modification cycles.

Devices whose AI is incidental to the device function, devices whose modifications would substantively change intended use, and devices whose modifications cannot be specified in advance generally do not benefit from PCCP and should plan for traditional supplement pathways.

---

## How PCCP Evidence Reuses Across Other AI Authorities

PCCP documentation is the most rigorous AI lifecycle evidence required by any U.S. healthcare AI authority today. That same documentation can be reused, with field tagging, to satisfy other authorities.

**NIST AI RMF.** PCCP's modification protocol maps to AI RMF Manage function activities. PCCP's impact assessment maps to Map and Measure functions. A device manufacturer maintaining a PCCP is materially producing AI RMF documentation already.

**ONC HTI-1 algorithm transparency.** PCCP's description of planned modifications and validation methodology can populate ONC HTI-1 decision-support intervention source attributes for any device that is also certified health IT or interfaces with certified health IT.

**EU AI Act.** For AI-enabled medical devices that fall under EU AI Act high-risk classification (most clinical AI devices), PCCP impact assessment supports the EU AI Act Annex IV technical documentation, post-market monitoring, and substantial-modification analysis. The vocabulary differs, but the underlying evidence is the same.

**Colorado AI Act.** PCCP impact assessment supports Colorado AI Act risk-management documentation and impact assessments for healthcare consequential decisions.

**HIPAA risk analysis.** Where the AI device processes ePHI, PCCP modification cycles trigger HIPAA risk analysis updates for the affected systems. The PCCP modification protocol becomes the input to the HIPAA risk analysis cadence.

A manufacturer that designs PCCP documentation with cross-authority field tagging produces one set of evidence that serves five regimes simultaneously. This is the [single-artifact, multi-authority](/blog/single-artifact-multi-authority-evidence-engineering) model applied to AI devices specifically.

---

## What a Healthcare Customer Should Ask

Healthcare buyers of AI-enabled medical devices should ask two PCCP-related questions in procurement.

**Does this device have a PCCP, and may we review it?** A PCCP is part of the marketing submission and is generally not public, but manufacturers can share the PCCP structure and modification cadence with customers under appropriate agreements. Customers that integrate AI-enabled devices into clinical workflows have a legitimate operational need to understand the modification cadence so they can plan training, validation, and risk-analysis updates.

**What modifications are planned, and how will we be notified?** Modifications that occur within a PCCP envelope are not new submissions, but they may still affect customer training, integration testing, and clinical workflow. A vendor that cannot describe its modification cadence is a vendor whose device may surprise the customer mid-deployment.

For customers maintaining their own AI use-case dossiers, the vendor's PCCP structure feeds the customer's modification protocol section.

---

## What This Is Not

PCCP is not a general AI governance framework. It applies specifically to AI-enabled device software functions regulated by FDA. The boundary matters in two directions.

AI used outside FDA-regulated devices — billing AI, clinical-documentation scribing, prior-authorization automation, fraud detection, security operations, generative AI tools — is not subject to PCCP. It is still subject to NIST AI RMF, HIPAA, EU AI Act, Colorado AI Act, and (where ONC-certified health IT is involved) HTI-1 algorithm transparency. PCCP is one tool in a larger AI compliance toolkit, not a universal substitute.

PCCP is also not a license for unbounded AI evolution within a regulated device. The PCCP envelope is bounded by what the modification protocol can defensibly cover. Modifications outside the envelope require traditional submissions.

---

## Why This Matters Strategically

PCCP is one of the clearest examples of regulatory evolution catching up to a technology shift. AI-enabled devices needed an iteration pathway, FDA built one, and the resulting framework is now being used as a template for AI compliance evidence in adjacent regimes.

Three implications follow:

- AI vendors that have invested in defensible PCCP structures are better positioned for cross-jurisdiction AI compliance generally, not just for FDA submissions.
- Healthcare buyers should treat PCCP rigor as a quality signal in vendor selection, even for non-device AI systems where PCCP itself does not formally apply.
- Healthcare cybersecurity programs should integrate vendor PCCP structures into their AI vendor questionnaires, modification-tracking processes, and risk-analysis update cadences.

PCCP is also the evidence model that the HIPAA Security Rule NPRM (HHS, 2025) implicitly anticipates for AI-touching ePHI systems. Documenting AI lifecycle changes is increasingly the table-stakes expectation for any AI system in a healthcare environment, regulated medical device or not.

---

## What to Track

Three signals will shape PCCP practice through 2027:

- FDA's published PCCP examples and any sector-specific updates.
- Cross-coordination guidance between FDA, ONC, and HHS on AI-enabled device transparency expectations.
- EU AI Act implementing regulations on substantial-modification analysis for medical-device AI, particularly as the August 2, 2027 high-risk obligation date approaches.

PCCP is mature enough today to be the operational reference for AI-enabled device lifecycle compliance. It is also new enough that practice and FDA expectations will continue to evolve through 2027.

---

## Sources

- FDA. (2025, August 18). *Marketing submission recommendations for a predetermined change control plan for artificial intelligence-enabled device software functions* (originally issued December 4, 2024).
- FDA. (2026). *Cybersecurity in medical devices* (final guidance).
- NIST. (2023). *AI Risk Management Framework 1.0*.
- ONC. (2024). *HTI-1 Final Rule*. 89 Fed. Reg. 1192.
- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898.
- European Parliament and Council. (2024). *Regulation (EU) 2024/1689 (AI Act)*.
- Colorado General Assembly. (2024). *SB 24-205*; (2025) *SB 25B-004*.
