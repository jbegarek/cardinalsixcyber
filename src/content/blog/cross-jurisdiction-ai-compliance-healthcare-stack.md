---
title: "The Cross-Jurisdiction AI Compliance Stack for Healthcare Vendors"
description: "Six AI compliance instruments now apply to healthcare vendors. They overlap but do not harmonize. Here is how to build one AI dossier that satisfies all six."
publishDate: 2026-05-13
author: "Justin T. Begarek"
lane: research
topics:
  - Healthcare
  - AI
  - Compliance
  - HIPAA
  - Risk Management
featured: false
draft: false
citations: false
diagrams: false
---

A healthcare vendor that builds, deploys, or embeds AI in 2026 is not navigating one AI law. It is navigating six instruments simultaneously: NIST AI RMF, FDA Predetermined Change Control Plans, ONC HTI-1 algorithm transparency, the HIPAA Security Rule NPRM, the EU AI Act, and Colorado's AI Act. The instruments overlap on most of the questions a healthcare AI program has to answer, but they overlap without harmonizing. Each demands different evidence, different terminology, and different artifacts.

For a small healthcare cybersecurity team or a clinical-AI vendor with a lean compliance function, parallel evidence streams are not sustainable. The only economically defensible posture is single-artifact, multi-authority evidence — one AI use-case dossier that records what every regime needs, with fields tagged by which regime requires which.

This post walks through what each of the six instruments requires, where they overlap, and what fields a unified AI dossier needs to satisfy all six.

---

## The Six Instruments

### NIST AI Risk Management Framework 1.0

The NIST AI RMF organizes AI risk around four functions: Govern, Map, Measure, and Manage. It is voluntary federal guidance but is increasingly cited by procurement, insurers, and regulators as the operational baseline for AI risk management. The Generative AI Profile (NIST AI 600-1) extends the AI RMF for generative and dual-use foundation models with specific practices for confabulation, data leakage, harmful outputs, and synthetic content. NIST SP 800-218A applies the SSDF to generative and dual-use AI software.

Status: voluntary framework. Required artifacts: AI use-case inventory, risk register, model cards, decision records.

### FDA Predetermined Change Control Plan (PCCP) Guidance

FDA's August 18, 2025 PCCP guidance (originally issued December 4, 2024) covers AI-enabled device software functions whose behavior may be modified over time. A PCCP describes planned modifications, the methodology for developing and validating those modifications, and the impact assessment used to maintain reasonable assurance of safety and effectiveness. Where a PCCP is included in a marketing submission, the device may iterate along the planned envelope without resubmission.

Status: final FDA guidance, nonbinding but operationally controlling for AI-enabled medical devices. Required artifacts: PCCP protocol, modification log, validation evidence.

### ONC HTI-1 Final Rule

ONC's HTI-1 final rule (89 Fed. Reg. 1192, effective March 11, 2024) updates the Health IT Certification Program with decision-support intervention transparency, predictive-model attributes, standardized API expectations, and real-world testing. Certified health IT that supports DSI features must expose source attributes and related transparency information that customers can inspect.

Status: effective binding rule on certified health IT. Required artifacts: DSI source attributes, transparency record, certification artifacts.

### HIPAA Security Rule NPRM

The HIPAA Security Rule NPRM (90 Fed. Reg. 898) is proposed, not final. It expressly contemplates AI as an emerging technology and does not impose AI-specific safeguards directly. The relevance to AI compliance is indirect but consequential: any AI system that processes ePHI inherits the NPRM's proposed asset-inventory, MFA, encryption, audit-log, segmentation, and contingency-plan-testing requirements.

Status: proposed. Required artifacts: updated risk analysis, asset register, encryption inventory.

### EU AI Act

EU Regulation 2024/1689 takes a risk-tiered approach: prohibited, high-risk, limited-risk, minimal-risk. Most clinical and decision-influencing healthcare AI falls into the high-risk category. Applicability is phased under Article 113: prohibitions from February 2, 2025; general-purpose AI model rules and most enforcement provisions from August 2, 2026; high-risk obligations under Article 6(1) from August 2, 2027.

Status: in force, phased applicability. Required artifacts: conformity assessment, technical file, human-oversight policy, post-market monitoring, serious-incident reporting.

### Colorado AI Act (SB 24-205, modified by SB 25B-004)

Colorado's AI Act covers developers and deployers of high-risk AI systems making consequential decisions in employment, education, housing, healthcare, and access to financial or legal services. SB 25B-004 (signed August 28, 2025) moved the effective date from February 1, 2026 to June 30, 2026. Obligations include risk-management policies, impact assessments, annual reviews, and consumer notification.

Status: enacted, not yet effective; June 30, 2026. Required artifacts: risk-management program documentation, impact assessment, consumer notices.

---

## Where the Instruments Overlap

The six instruments converge on roughly the same questions. The vocabulary differs; the underlying inquiry does not.

| Question | NIST AI RMF | FDA PCCP | ONC HTI-1 | HIPAA NPRM | EU AI Act | Colo. AI Act |
|---|---|---|---|---|---|---|
| What is the use case? | Map | PCCP scope | DSI / predictive model attribute | Risk analysis scope | Annex III classification | High-risk listing |
| Who is affected? | Stakeholders | Patient population | Clinician / patient users | Affected ePHI population | Affected persons | Colorado consumers |
| How was it trained / validated? | Measure | Validation methods | Source attributes | Risk analysis input | Technical documentation | Impact assessment |
| How is it monitored? | Manage | Modification protocol | Real-world testing | Audit logs | Post-market monitoring | Annual review |
| When does a change require re-review? | Manage | PCCP envelope | Certification update | Risk analysis update | Substantial modification | Material modification |
| What does the user / patient see? | Govern transparency | Labeling | DSI transparency record | NPP and breach notice | Article 13 transparency | Consumer notice |
| What happens on incident? | Manage | MDR / serious AE | Information-blocking exception | Breach notification | Serious-incident report | Algorithmic discrimination notice |

The same AI use case generates the same factual answers. Only the format differs.

---

## The Unified AI Use-Case Dossier

A defensible cross-jurisdiction AI dossier captures one record per AI use case with the following sections. Each field is tagged by the regime that needs it; one record fills all six audiences.

**Identification.** System name, version, owner, date, regulatory tier (high-risk yes/no per EU AI Act and Colorado AI Act, FDA device classification, ONC certified-health-IT scope, HIPAA scope).

**Use-case description.** Decision context, population, clinical setting, intended use, prohibited uses, geography (matters for Colorado and EU exposure).

**Data lineage.** Training data sources, validation data sources, prompt or input data classes, ePHI exposure, CUI exposure, third-party data agreements.

**Model and validation.** Algorithm class, validation methodology, performance metrics, fairness/bias evaluation, validation date, validation rationale.

**Modification protocol.** Planned modifications, testing requirements, rollback procedures, version control. This is the FDA PCCP field and serves EU AI Act substantial-modification analysis simultaneously.

**Monitoring plan.** Drift metrics, abuse signals, real-world performance, retraining triggers, monitoring cadence, ownership.

**Human oversight and explainability.** Required oversight points, explainability mechanism, escalation path, override authority, documentation. Freyer et al. (2024) provide a peer-reviewed framework for when explainability is ethically required, which is a defensible reference for the Colorado AI Act and EU AI Act records.

**Stakeholder transparency.** What clinicians see, what patients see, what consumers in Colorado see, ONC DSI transparency record, EU AI Act Article 13 transparency.

**Incident handling.** AI-specific incident criteria, notification triggers, FDA serious-AE coordination, Colorado algorithmic discrimination notice, EU serious-incident report, HIPAA breach analysis.

**Risk register entry.** Risk-tiered impact assessment that satisfies Colorado AI Act risk-management documentation, EU AI Act Annex IV technical documentation, NIST AI RMF Map output, and HIPAA risk analysis update for the affected ePHI environment.

A small healthcare AI team can sustain one dossier per use case. It cannot sustain six.

---

## What This Means for Vendors and Buyers

The same dossier serves both sides of a healthcare AI procurement.

For an AI vendor, the dossier is the procurement collateral. Customers asking for HIPAA risk analysis evidence, EU AI Act conformity records, Colorado AI Act impact assessments, FDA PCCP documentation, and ONC certification evidence can be served from one record set. The vendor that maintains a unified dossier wins on procurement velocity even before it wins on AI quality.

For a healthcare buyer, the dossier is the diligence target. A vendor that cannot produce a current AI use-case dossier with these fields will not survive a 2027 procurement review at any large healthcare customer. The dossier is also the customer's own evidence when responding to OCR Risk Analysis Initiative inquiries that touch AI-related ePHI processing.

For a small healthcare cybersecurity firm, the dossier is a service-line opportunity. Standing up a customer's AI use-case dossier program — inventory, classification, dossier templates, vendor questionnaires, board reporting — fits in the same operating capability that produces HIPAA risk analyses and CMMC scoping diagrams.

---

## What to Track

Three signals will reshape this stack in 2026 and 2027:

- The HIPAA Security Rule final rule (HHS, 2025) and any AI-specific clarifications.
- Colorado AI Act effective-date and enforcement signals as June 30, 2026 approaches.
- EU AI Act guidance from the AI Office on high-risk system documentation expectations as the August 2, 2027 Article 6(1) date approaches.

State legislatures will likely add to this stack. Texas, California, and Connecticut all have AI-related work in progress. The dossier model holds up because it is structured around what AI use cases actually do, not around any single regime's vocabulary.

---

## Sources

- NIST. (2023). *AI Risk Management Framework 1.0* (NIST AI 100-1).
- NIST. (2024). *Generative AI Profile* (NIST AI 600-1).
- FDA. (2025). *PCCP Guidance for AI-Enabled Device Software Functions*.
- ONC. (2024). *HTI-1 Final Rule*. 89 Fed. Reg. 1192.
- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898.
- European Parliament and Council. (2024). *Regulation (EU) 2024/1689 (AI Act)*.
- Colorado General Assembly. (2024). *SB 24-205*. (2025). *SB 25B-004*.
- Freyer, N., Gross, D., & Lipprandt, M. (2024). *BMC Medical Ethics, 25*, Article 104.
