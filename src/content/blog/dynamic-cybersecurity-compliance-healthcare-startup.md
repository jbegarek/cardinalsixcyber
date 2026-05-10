---
title: "Current and Expected Adjustments to Cybersecurity Compliance for a Healthcare-Sector Cybersecurity Startup"
description: "A research paper on why static, audit-cycle compliance no longer fits healthcare cybersecurity, and how a small startup operates compliance as a continuing capability."
publishDate: 2026-05-10
author: "Justin T. Begarek"
lane: research
topics:
  - Healthcare
  - HIPAA
  - AI
  - Cryptography
  - Compliance
  - Risk Management
featured: true
draft: false
citations: true
diagrams: false
---

*This is the full research paper from TIM-8720 (Industry Laws, Regulations, and Compliance) coursework, May 2026. Practitioner summaries derived from it include [The HIPAA Security Rule NPRM](/blog/hipaa-security-rule-nprm-control-roadmap), [Post-Quantum Cryptography for Healthcare](/blog/post-quantum-cryptography-healthcare-hndl-roadmap), [The Cross-Jurisdiction AI Compliance Stack](/blog/cross-jurisdiction-ai-compliance-healthcare-stack), [Single-Artifact Multi-Authority Evidence Engineering](/blog/single-artifact-multi-authority-evidence-engineering), [CIRCIA 72-Hour Reporting for Healthcare](/blog/circia-72-hour-reporting-healthcare), and [HICP and the Recognized Security Practices Safe Harbor](/blog/hicp-recognized-security-practices-ocr-safe-harbor).*

---

## Introduction

Cybersecurity compliance has become a moving target for organizations operating inside the Healthcare and Public Health critical-infrastructure sector. External influences continually alter the risk balance and force control updates even when an organization itself has not changed. For a healthcare-sector cybersecurity startup serving covered entities, business associates, and a small portfolio of defense-adjacent customers, the velocity of legal and standards change between 2024 and 2027 has outpaced the static, audit-cycle compliance model many small organizations still operate. Five recent regulatory items each illustrate the same pattern of co-evolution between law and technology. They are the HIPAA Security Rule Notice of Proposed Rulemaking (NPRM), the finalized National Institute of Standards and Technology (NIST) post-quantum cryptography (PQC) standards, the Cybersecurity and Infrastructure Security Agency (CISA) Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA) NPRM, the Department of Defense (DoD) Cybersecurity Maturity Model Certification (CMMC) rules, and a phased set of state and international artificial intelligence laws. Emerging technologies and the law that governs them are co-evolving faster than control baselines can be updated through annual policy review (U.S. Department of Health and Human Services [HHS], 2025).

The research problem this paper addresses is that small healthcare-sector cybersecurity providers cannot satisfy current and anticipated compliance obligations using the static, audit-cycle posture inherited from a slower-moving regulatory era. Three structural problems make that posture untenable. A velocity asymmetry has opened, where regulatory output exceeds annual review cadence so a frozen baseline is out of date by year-end. Authority fragmentation means overlapping but non-identical AI, privacy, and cybersecurity requirements from FDA, ONC, HHS, EU, Colorado, and Washington impose duplicate evidentiary burden without harmonization. Status ambiguity forces organizations to operate against three legal weights at once because proposed, anticipated, and vacated rules each produce real procurement and audit pressure even when none is yet binding.

A healthcare-sector cybersecurity startup must therefore operate compliance as a dynamic capability rather than a periodic audit event. Four emerging technology areas drive the argument: artificial intelligence and machine learning (AI/ML), the Internet of Medical Things (IoMT) with adjacent IoT, 5G, edge, and operational technology (OT), cloud and application programming interface (API) architectures with zero trust, and quantum-vulnerable cryptography. Across these areas, this paper maps current and anticipated compliance shifts, proposes a Control Adjustment Matrix (Appendix, Table 1) and a cross-jurisdiction AI comparison (Appendix, Table 2), sorts the relevant instruments by legal status (Appendix, Table 4), and frames the response as four named recommendations operationalized through a twelve-component dynamic plan (Appendix, Table 3). Sebastian (2021) anchors the privacy-directive framing.

## Organizational Context and Critical-Infrastructure Justification

The organization is a healthcare-sector cybersecurity startup delivering managed security, compliance engineering, and audit-readiness services to small and mid-size healthcare delivery organizations, business associates, and customers seeking CMMC Level 2 readiness. Healthcare and Public Health is one of sixteen CISA-recognized critical-infrastructure sectors, with HHS as the Sector Risk Management Agency. Customer scope means the HIPAA Security Rule (45 CFR Parts 160, 162, 164) applies directly to the customer base and indirectly to the startup as a downstream business associate (HHS, 2021), with NIST SP 800-66 Rev. 2 mapping those safeguards to cybersecurity activities (Marron, 2024). Where DoD-adjacent work brings controlled unclassified information (CUI) into scope, the 32 CFR Part 170 CMMC program rule and the 48 CFR DFARS rule are contractually operational (DoD, 2024, 2025).

## AI and Machine Learning in Healthcare

AI is the most consequential near-term emerging technology for the customer base. AI sits at the center of a compliance-liability shift from operators toward designers and often relies on inaccurate or fabricated inputs that complicate evidentiary review. Within the startup, AI exposure spans security operations, customer-facing clinical and administrative AI such as decision support, prior authorization, scribing, billing, fraud detection, imaging, and population health, plus embedded generative AI in software-as-a-service dependencies (NIST, 2024a). Currently effective instruments include the NIST AI RMF 1.0 (NIST, 2023), the Generative AI Profile (NIST, 2024a), the Office of the National Coordinator for Health Information Technology (ONC) HTI-1 final rule effective March 11, 2024 (ONC, 2024), and the U.S. Food and Drug Administration's August 18, 2025 final guidance on Predetermined Change Control Plans (PCCPs) for AI-enabled device software functions (FDA, 2025). Peer-reviewed work adds a context-dependent framework for when explainability is ethically required (Freyer et al., 2024).

Anticipated changes intensify this layer cake. Appendix Table 2 lays out the six instruments side by side because their overlap-without-harmonization is the core source of duplicated AI documentation effort. The HIPAA Security Rule NPRM remains *proposed* and expressly contemplates AI, quantum, and virtual or augmented reality (HHS, 2025). EU AI Act application is phased, with prohibitions effective February 2, 2025, general-purpose model rules August 2, 2026, and Article 6(1) high-risk obligations August 2, 2027 (European Parliament and Council of the European Union, 2024, art. 113). Colorado's AI Act, modified by SB 25B-004, takes effect June 30, 2026 while preserving risk-management, impact-assessment, and consumer-notification obligations (Colorado General Assembly, 2024, 2025).

## IoMT, IoT, 5G, Edge, and Operational Technology

IoT, industrial IoT, 5G, and the shifting locus of control are recognized drivers of compliance change. For the startup, these collapse into one operational reality. Customers are surrounded by connected medical devices, building systems, lab and pharmacy automation, home-monitoring devices, and an emerging 5G and edge layer that reshapes the network boundary (Ali et al., 2024). Currently effective standards span NIST SP 800-82 Rev. 3 for OT security (Stouffer et al., 2023), NIST SP 800-213 for IoT device cybersecurity capabilities (Fagan et al., 2021), NIST SP 800-161 Rev. 1 for cybersecurity supply-chain risk management (Boyens et al., 2022), FDA's 2026 medical-device cybersecurity guidance (FDA, 2026), the HHS HPH Cybersecurity Performance Goals (HHS, 2024), and the December 2025 CISA Cross-Sector CPGs Version 2.0 (CISA, 2025). Peer-reviewed evidence corroborates device authentication, microsegmentation, encryption, and proactive threat detection as the most-cited mitigations in healthcare IoT (Ali et al., 2024).

Anticipated changes include the HIPAA Security Rule NPRM's *proposed* asset-inventory, network-mapping, vulnerability-management, and segmentation requirements (HHS, 2025). CISA's NPRM and status page support a 72-hour CIRCIA reporting timeline once the final rule takes effect (CISA, 2024, 2026). FDA section 524B cyber-device submission expectations continue to mature (FDA, 2026). Per Appendix Table 1, IoMT/IoT/OT control adjustments converge on a unified asset register, microsegmentation per NIST SP 800-207 zero trust (Rose et al., 2020), clinical-safety-aware patching, and incident handling that treats clinical availability as a first-class severity dimension. Ransomware remains a sociotechnical patient-safety problem, and a 2025 systematic media-literature review documents cascading impacts on care, employees, and informatics systems (Avery et al., 2025).

## Cloud, APIs, Zero Trust, and Distributed Health Data

The locus-of-control question, combined with the migration of EHRs, portals, telehealth, identity, and analytics to multi-tenant cloud and API-driven services, defines this third area. Sebastian (2021) frames the same shift in privacy-directive terms. Compliance questions have shifted from "is the data encrypted" to "where does it live, who reaches it through which APIs, under what trust assumptions, with what evidence" (Marron, 2024). Currently effective guidance spans NIST SP 800-207 zero trust architecture (Rose et al., 2020), SP 800-228 API protection (Chandramouli & Butcher, 2025), SP 800-218 SSDF (Souppaya et al., 2022), SP 800-63-4 digital identity (Temoshok et al., 2025), SP 800-66 Rev. 2 HIPAA mapping (Marron, 2024), CSF 2.0 with its Govern function (NIST, 2024d), the FTC Health Breach Notification Rule amendments effective July 29, 2024 for non-HIPAA health apps (Federal Trade Commission, 2024), and the U.S. Securities and Exchange Commission (SEC) cybersecurity disclosure rule for public-company partners (SEC, 2023).

Anticipated changes add the HIPAA NPRM's *proposed* encryption, audit-log, segmentation, and contingency safeguards (HHS, 2025), CIRCIA finalization (CISA, 2024), and increased CSF 2.0 procurement adoption. Cross-border flows add EU GDPR, UK GDPR, and emerging state and international regimes (Xia et al., 2024). Per Appendix Table 1, cloud control adjustments center on shared-responsibility matrices, cloud configuration baselines with infrastructure-as-code scanning, API discovery and authentication, identity modernization to SP 800-63-4, vendor due diligence under SP 800-161 Rev. 1 (Boyens et al., 2022), and a unified data-flow inventory queryable by regulator, customer, and vendor scope.

## Quantum Computing and Post-Quantum Cryptography

Quantum computing is a long-term planning issue because long-lived healthcare data may remain sensitive when future cryptanalytic capacity improves. The harvest-now-decrypt-later (HNDL) threat works this way. Adversaries record encrypted traffic now and decrypt it once a cryptanalytically relevant quantum computer becomes available. Medical, genomic, mental-health, and longitudinal cohort data remain sensitive for decades, and CUI retains confidentiality requirements long after collection (SaberiKamarposhti et al., 2024). HHS sector framing reinforces this point (U.S. Department of Health and Human Services, Health Sector Cybersecurity Coordination Center [HHS HC3], 2022). NIST finalized FIPS 203 ML-KEM key encapsulation (NIST, 2024c), FIPS 204 ML-DSA lattice-based signature (NIST, 2024b), and FIPS 205 SLH-DSA hash-based backup signature (NIST, 2024e) on August 13, 2024. FIPS standards are mandatory for federal information systems and influence federal-adjacent procurement through FedRAMP, DoD, and DFARS clauses that reference FIPS-validated cryptography. The HIPAA Security Rule NPRM proposes more specific encryption requirements that would likely reference FIPS-validated modules (HHS, 2025), and NIST SP 800-57 Pt. 1 Rev. 5 governs the key-management lifecycle decisions that determine the difficulty of any PQC migration (Barker, 2020).

At federal policy scale, NSM-10 directs federal agencies to transition to quantum-resistant algorithms with a 2035 horizon (The White House, 2022). No healthcare-specific PQC mandate yet exists, but procurement, cyber insurance, and federal-adjacent partners are likely to request PQC roadmaps as the federal transition window narrows (HHS HC3, 2022). Per Appendix Table 1, PQC control adjustments center on a cryptographic inventory, long-lived-data classification, algorithm-agility design, and staged migration aligned to SP 800-57 Pt. 1 Rev. 5 (Barker, 2020).

## Current Compliance Environment

A multi-state status legend is essential because the legal weight of these instruments differs. Legend categories are (a) **Final/Effective** binding law, (b) **Final Guidance** that is nonbinding but persuasive, (c) **Voluntary Framework** adopted at organizational discretion, (d) **Contractually Binding when Incorporated**, (e) **Proposed**, (f) **Enacted but not yet Effective**, and (g) **Vacated, stayed, or rescinded**. A single "emerging" tag obscures legally meaningful differences across these categories. NIST SP 800 series publications (NIST, n.d.) anchor most cross-cutting controls.

Appendix Table 4 sorts the relevant instruments by status category. Two cross-cutting points carry from the table into the rest of the analysis. First, the 2024 HIPAA reproductive-health privacy rule should be treated with caveat rather than as straightforwardly current because it was vacated in 2025 federal litigation. Second, enforcement reality matters: through mid-2025, the Office for Civil Rights (OCR) Risk Analysis Initiative resolved multiple ransomware-related Security Rule investigations, including a $250,000 settlement with Cascade Eye and Skin Centers under a two-year corrective action plan (U.S. Department of Health and Human Services, Office for Civil Rights [HHS OCR], 2024). State health-data laws extend obligations beyond HIPAA, with Washington's My Health My Data Act covering non-HIPAA consumer health data (Washington State Legislature, 2023).

## Anticipated Compliance Changes

Appendix Table 4 sorts the proposed and phased changes by status. Two near-term items dominate. The HIPAA Security Rule NPRM is *proposed*, not final, but customer evidence should be mapped now to its asset-inventory, MFA, encryption, vulnerability-management, audit-log, segmentation, and contingency-plan testing requirements as a readiness measure (HHS, 2025). CIRCIA's 72-hour reporting becomes mandatory only when CISA finalizes the rule (CISA, 2024, 2026). State and international AI laws are the third *anticipated and phased* set, with Colorado's AI Act taking effect June 30, 2026 (Colorado General Assembly, 2024, 2025) and EU AI Act high-risk obligations August 2, 2027 (European Parliament and Council of the European Union, 2024). NSM-10 sets the federal cryptographic transition horizon at 2035 (The White House, 2022).

## Anticipated Control Adjustments and Control Adjustment Matrix

Appendix Table 1 maps each technology area to its regulatory shift, framework set, NIST SP 800-53 Rev. 5 control families and CMMC corollaries, recommended adjustment, evidence artifact, and implementation timeframe. AI/ML obligations are the most heterogeneous because federal guidance, state and international regimes, and FDA device guidance impose overlapping but non-identical documentation expectations. IoMT/IoT/OT obligations converge on asset register, segmentation, and SBOM-aware vendor diligence. Cloud and zero-trust obligations are broadest in control-family coverage and benefit most from a single data-flow inventory. PQC obligations are narrowest today but longest in horizon. Cross-cutting, enterprise risk analysis must integrate all four factors. Marron (2024) and Ross and Pillitteri (2024a) anchor the HIPAA risk-analysis and CMMC RA expectations. Nelson et al. (2025) anchors incident response per SP 800-61 Rev. 3. NIST (2024e) and Center for Internet Security (2021) anchor CSF 2.0 Govern alignment and training.

## Recommendations

Four named recommendations respond directly to the research problem and the three structural problems identified in the introduction. Each pairs a mechanism with the documented gap it closes and the realistic startup-scale constraint it must respect. The recommendations are intentionally few because a small startup compliance team can sustain only a small number of cross-authority programs in parallel.

**Recommendation 1.** Single-artifact, multi-authority evidence engineering. Design four anchor artifacts (AI use-case dossier, unified IoMT/IoT/OT asset register, single data-flow inventory, cryptographic inventory) so each is produced once and submitted against AI RMF, FDA PCCP, ONC HTI-1, EU AI Act, Colorado AI Act, HIPAA risk-analysis, CMMC, and FTC HBNR audiences without re-authoring. Marron (2024) maps HIPAA safeguards to cybersecurity activities, but the startup still needs its own crosswalk to connect HIPAA evidence with AI, FDA, CMMC, FTC, EU, and Colorado demands. The artifact catalog must be small, stable, and deeply mapped because small teams cannot maintain parallel evidence universes (NIST, 2024d).

**Recommendation 2.** Compliance intelligence as a continuing capability. Stand up daily intake, weekly triage, and quarterly direction reports across HHS, OCR, HC3, Federal Register, CMS, OIG, CISA, DoD CIO, NIST, FDA, FTC, SEC, EU Commission, state attorneys general, and H-ISAC, with bi-weekly counsel review of pending NPRMs. Velocity asymmetry named in the introduction means an annual policy review is materially out of date by the date it is signed (HHS, 2025). Low-effort but disciplined cadence is the constraint, since a small startup cannot dedicate a full-time regulatory analyst, and every cycle produces a written compliance-change log.

**Recommendation 3.** Anticipatory readiness for proposed and phased rules. Map customer evidence now to HIPAA Security Rule NPRM safeguards (HHS, 2025), CIRCIA 72-hour reporting (CISA, 2024), Colorado AI Act readiness before June 30, 2026 (Colorado General Assembly, 2025), and EU AI Act high-risk obligations before August 2, 2027 (European Parliament and Council of the European Union, 2024), while labeling the NPRMs as nonfinal. Post-effective-date scrambles create non-compliance windows that expose the organization to OCR enforcement and customer-contractual penalties. OCR's Risk Analysis Initiative resolved a $250,000 Cascade Eye and Skin Centers settlement under the existing Security Rule (HHS OCR, 2024). Readiness must be tied to status-legend categories distinguishing *Proposed* from *Enacted-but-not-yet-Effective* and *Vacated* (Center for Internet Security, 2021).

**Recommendation 4.** Cryptographic agility and a long-horizon PQC migration plan. Maintain a cryptographic inventory across applications, infrastructure, vendors, and devices, classify long-lived datasets exposed to harvest-now-decrypt-later, design new systems for algorithm agility, and stage migration starting with TLS key encapsulation and code-signing aligned to FIPS 203, 204, and 205 and SP 800-57 Pt. 1 Rev. 5 (NIST, 2024b, 2024c, 2024e). No healthcare-specific PQC mandate yet exists, but federal, procurement, and cyber-insurance partners are likely to request PQC roadmaps as the federal transition window narrows, and HHS sector framing treats quantum as a serious planning concern (HHS HC3, 2022). Peer-reviewed evidence corroborates the urgency for healthcare data sensitivity windows (SaberiKamarposhti et al., 2024). Re-encryption of TLS, code-signing, and archival data carries real cost, so the staged migration runs on a 2027 to 2035 horizon rather than at federal-target speed (The White House, 2022). Key-management lifecycle decisions follow Barker (2020).

## Dynamic Compliance Plan of Action

Twelve continuing capabilities operationalize the four recommendations and are summarized in Appendix Table 3 with cadence, outputs, and source linkage. They span compliance intelligence monitoring, legal and regulatory review, control mapping, risk assessment refresh, vendor and supply chain review, policy updates, technical control implementation, audit evidence collection, board and executive reporting, workforce training, incident reporting readiness, and continuous improvement. Two design choices warrant body-level emphasis. First, control mapping is built once as a harmonization matrix that lets a single internal control trace to HIPAA, CMMC, CSF 2.0, CIS Controls v8, and customer contractual clauses simultaneously, which is the operational mechanism behind Recommendation 1. Second, incident reporting is implemented as a single handling process plus a layered reporting decision tree per NIST SP 800-61 Rev. 3 (Nelson et al., 2025), so that one incident produces the correct cascade of HIPAA, state, FTC HBNR, DFARS, CIRCIA, SEC, CMMC, and BAA notifications without re-engineering.

## Conclusion

The healthcare-sector cybersecurity startup operates inside a compliance environment whose rate of change is no longer commensurate with annual policy review. AI/ML, IoMT/IoT/5G/OT, cloud/API/zero trust, and quantum-relevant cryptography each generate predictable classes of control adjustment governed by a mix of binding rules, final guidance, voluntary frameworks, contractually binding standards, proposed rules, enacted-but-not-yet-effective laws, and vacated provisions. A static compliance posture cannot navigate this environment, but a four-recommendation program operationalized through twelve continuing capabilities, anchored in industry best practices such as quarterly phishing simulations, immutable backup validation, and privileged access recertification (Center for Internet Security, 2021), can. Shared evidence artifacts (an AI use-case dossier, a unified asset register, a single data-flow inventory, and a cryptographic inventory) let one set of work satisfy multiple authorities, the only economically defensible approach for a small startup. This synthesis reframed an initial assumption that compliance velocity is primarily a documentation problem. The structural problem is evidence engineering, and the research problem this paper has framed is therefore capability design rather than control selection. Compliance, in this view, is a continuous capability measured by artifact production and mean-time-to-control-update rather than by periodic audit pass/fail.

---

## Appendix

### Table 1 — Control Adjustment Matrix for the Healthcare Cybersecurity Startup

| Technology | Regulatory shift (status) | Frameworks | Controls | Adjustment | Artifact | Timeframe |
|---|---|---|---|---|---|---|
| AI/ML | HIPAA NPRM *(Proposed)*, FDA PCCP *(Final Guidance, 2025)*, ONC HTI-1 *(Effective)*, EU AI Act *(phased, high-risk Aug 2, 2027)*, Colo. AI Act *(Enacted, Jun 30, 2026)* | AI RMF, GenAI Profile, SP 800-218A, FDA PCCP, ONC HTI-1, EU AI Act, Colo. AI Act | AC, AU, CA, CM, IR, PL, RA, SA, SC, SI, SR | Use-case inventory and risk-tiered impact assessments, explainability and human-oversight policy, PCCP-style modification protocols, AI acceptable-use policy, vendor AI questionnaires | AI use-case dossier, model card, PCCP protocol, DSI transparency record, AI vendor packets | Inventory and policy by Q3 2026, Colo. readiness before Jun 30, 2026 |
| IoMT/IoT/5G/OT | HIPAA NPRM *(Proposed)*, CIRCIA *(Proposed)*, FDA cyber medical-device *(Final Guidance, 2026)* | HIPAA, FDA, SP 800-82r3, SP 800-213, SP 800-161r1, HHS HPH CPGs, CISA CPGs v2.0 | AC, AU, CM, IA, IR, MA, RA, SC, SI, SR | Unified IoMT/IoT/OT asset register, microsegmentation, clinical-safety-aware patching, vendor cyber questionnaires, secure remote vendor access | Asset register, segmentation diagrams, SBOM and CMP evidence, vendor risk packets, medical-device risk register | Inventory and segmentation by end of 2026, CIRCIA-readiness drill before final-rule date |
| Cloud / APIs / Zero Trust | HIPAA NPRM *(Proposed)*, FTC HBNR *(Effective)*, ONC HTI-1 *(Effective)*, SEC disclosure *(Effective)*, CIRCIA *(Proposed)* | HIPAA, FTC HBNR, ONC HTI-1, SP 800-66r2, SP 800-207, SP 800-228, SP 800-218/218A, SP 800-63-4, SP 800-161r1, CSF 2.0 | AC, AU, CA, CM, IA, IR, RA, SA, SC, SI, SR | Shared-responsibility matrix, cloud configuration baselines, API discovery and authn, identity to SP 800-63-4, envelope encryption, HIPAA + CMMC audit logging, data-flow inventory | Shared-responsibility matrices, cloud baselines, API attestations, identity attestations, audit-log retention proofs, data-flow diagrams, SBOMs | Inventory and baselines by Q4 2026, API gaps closed with HIPAA NPRM final rule |
| Quantum / PQC | NIST FIPS 203/204/205 *(Final, binding for federal info systems)*, HIPAA NPRM *(Proposed)*, NSM-10 *(2035 federal horizon)* | FIPS 203/204/205, SP 800-57 Pt. 1 r5, SP 800-131A r3, HIPAA NPRM, HHS HC3 quantum guidance | SC, CM, SA, SR | Cryptographic inventory, long-lived-data classification, algorithm-agility design, vendor PQC questionnaire, staged migration, updated key-management policy | Crypto inventory, long-lived-data classification, PQC roadmap, vendor PQC attestations, key-management policy and rotation logs | Crypto inventory by mid-2027, PQC pilots in 2027 to 2028 aligned with federal timelines |

*Note.* Status labels follow the multi-state legend introduced in the body. Adapted from author's synthesis of NIST, HHS, FDA, ONC, FTC, DoD, CISA, EU, and Colorado primary sources cited in this paper.

### Table 2 — Cross-Jurisdiction Comparison of AI Compliance Obligations Affecting the Healthcare Cybersecurity Startup

| Instrument | Jurisdiction | Status | Effective or applicable date | Scope of obligations | Required artifacts |
|---|---|---|---|---|---|
| HIPAA Security Rule NPRM | U.S. federal | Proposed | Final rule pending | Risk analysis, asset inventory, encryption, audit logs, segmentation, contingency testing for ePHI environments incl. AI components | Updated risk analysis, asset register, encryption inventory (HHS, 2025) |
| FDA PCCP Guidance | U.S. federal | Final Guidance | Aug 18, 2025 | Predetermined Change Control Plans for AI-enabled device software functions | PCCP protocol, modification log, validation evidence (FDA, 2025) |
| ONC HTI-1 Final Rule | U.S. federal | Effective | Mar 11, 2024 | Decision-support intervention transparency, certification updates, algorithm transparency | DSI source attributes, transparency record, certification artifacts (ONC, 2024) |
| EU AI Act | European Union | Phased | Prohibitions Feb 2, 2025, GPAI Aug 2, 2026, high-risk Aug 2, 2027 | Risk classification, conformity assessment, human oversight, technical docs for high-risk and GPAI systems | Conformity assessment, technical file, human-oversight policy (European Parliament and Council of the European Union, 2024) |
| Colorado AI Act (SB 24-205, SB 25B-004) | Colorado, U.S. | Enacted, not yet effective | Jun 30, 2026 | Risk-management program, impact assessments, consumer notice, anti-discrimination duties for high-risk AI systems | Risk-management program documentation, impact assessment, consumer notices (Colorado General Assembly, 2024, 2025) |
| NIST AI RMF and Generative AI Profile | U.S. federal | Voluntary Framework | Effective | Govern, map, measure, manage activities, generative AI risk profile | AI use-case inventory, AI risk register, model cards (NIST, 2023, 2024a) |

*Note.* Compiled from cited primary sources. Status labels follow the multi-state legend introduced in the body. GPAI = general-purpose AI. ePHI = electronic protected health information. DSI = decision-support intervention.

### Table 3 — Twelve-Component Dynamic Compliance Capability Plan

| # | Capability | Cadence | Outputs and evidence (with source linkage) |
|---|---|---|---|
| 1 | Compliance Intelligence Monitoring | Daily intake, weekly triage, quarterly direction reports | Compliance-change log sourced from HHS, OCR, HC3, Federal Register, CMS, OIG, CISA, DoD CIO, NIST, FDA, FTC, SEC, EU Commission, state AGs, and H-ISAC (NIST, n.d.) |
| 2 | Legal and Regulatory Review | Bi-weekly counsel, quarterly cross-jurisdictional | Legal memos, contract clause libraries, CIRCIA reporting decision tree updated when final-rule effective date is set (CISA, 2024, 2026) |
| 3 | Control Mapping | Continuous, change-driven | Harmonization matrix linking HIPAA, HHS HPH CPGs, CISA CPGs v2.0, CSF 2.0, SP 800-53 r5, SP 800-171 r3, CMMC L2, CIS Controls v8, customer contractual clauses, SOC 2 TSC (NIST, 2024d) |
| 4 | Risk Assessment Refresh | Annual full, quarterly partial, event-driven | Enterprise risk assessment per SP 800-30 r1 (Joint Task Force Transformation Initiative, 2012) |
| 5 | Vendor and Supply Chain Review | Annual recertification, tiered intake | Cyber, AI, IoMT, 5G, cloud, PQC, privacy questionnaires, SOC 2, HITRUST, FedRAMP, and SBOM evidence, BAA, DPA, and DFARS flowdown review (Boyens et al., 2022) |
| 6 | Policy Updates | Annual scheduled, off-cycle triggered | Updated information security, privacy, AI acceptable-use, IR, vendor risk, asset and config, change management, cryptography with PQC-readiness clause, training, and clinical safety policies (NIST, 2024d) |
| 7 | Technical Control Implementation | Continuous, maturity-tracked | Identity per SP 800-63-4 (Temoshok et al., 2025), cloud and API per SP 800-207 (Rose et al., 2020) and SP 800-228 (Chandramouli & Butcher, 2025), SSDF (Souppaya et al., 2022), cryptography per FIPS 203, 204, 205 (NIST, 2024b, 2024c, 2024e) and SP 800-57 (Barker, 2020), OT per SP 800-82 r3 (Stouffer et al., 2023) and SP 800-213 (Fagan et al., 2021), monitoring per SP 800-137 (Dempsey et al., 2011) |
| 8 | Audit Evidence Collection | Continuous output | Risk analyses, asset inventories, identity attestations, vulnerability and patch reports, audit-log retention proofs, incident logs, vendor reviews, training completion, contingency-test reports, policy version history (Marron, 2024) |
| 9 | Board and Executive Reporting | Quarterly with monthly updates and immediate notice on material events | Risk register, CSF 2.0 posture, OCR enforcement implications, pending regulatory changes, AI governance status, PQC milestones (NIST, 2024d), SEC disclosure framing (SEC, 2023) |
| 10 | Workforce Training | At hire, annual, role-change, event-driven | General security, HIPAA, CMMC, AI acceptable use, SSDF, clinical safety, phishing simulation, role-based content (Center for Internet Security, 2021), patient-safety stakes (Avery et al., 2025) |
| 11 | Incident Reporting Readiness | Continuous, annual tabletop | Single handling process per SP 800-61 Rev. 3 (Nelson et al., 2025), layered reporting decision tree spanning HIPAA breach, state breach, FTC HBNR (Federal Trade Commission, 2024), DFARS (DoD, 2025), CIRCIA (CISA, 2024), SEC disclosure (SEC, 2023), CMMC, BAA notification |
| 12 | Continuous Improvement | Quarterly maturity reviews, annual external assessments | After-action reviews, CSF 2.0 (NIST, 2024d) and CIS Controls v8 (Center for Internet Security, 2021) maturity, HITRUST, SOC 2, CMMC L2 assessments, rolling 24-month improvement plan with milestones, owners, evidence, and budget envelopes |

*Note.* Compiled from cited primary sources. Cadence column reads as the default operating tempo. Off-cycle triggers apply on regulatory change, customer onboarding, or incident.

### Table 4 — Compliance Instruments Sorted by Multi-State Status Legend

| Status category | Instruments and citations |
|---|---|
| Final/Effective binding law | HIPAA Security, Breach Notification, and Privacy Rules (HHS, 2021), DFARS 252.204-7012 and the 48 CFR DFARS rule operational since November 10, 2025 (DoD, 2025), 32 CFR Part 170 CMMC Program Rule (DoD, 2024), FTC Health Breach Notification Rule amendments effective July 29, 2024 (Federal Trade Commission, 2024), ONC HTI-1 final rule effective March 11, 2024 (ONC, 2024), SEC cybersecurity disclosure rule (SEC, 2023) |
| Final Guidance (nonbinding, persuasive) | FDA 2026 medical-device cybersecurity guidance (FDA, 2026), FDA 2025 PCCP guidance for AI-enabled device software (FDA, 2025), NIST SP 800-66 Rev. 2 HIPAA implementation (Marron, 2024) |
| Voluntary Framework | NIST CSF 2.0 (NIST, 2024d), NIST AI RMF 1.0 (NIST, 2023), NIST Generative AI Profile (NIST, 2024a), HHS HPH Cybersecurity Performance Goals (HHS, 2024), CISA Cross-Sector CPGs v2.0 (CISA, 2025), CIS Controls v8 (Center for Internet Security, 2021) |
| Contractually Binding when Incorporated | NIST SP 800-171 Rev. 3 (Ross & Pillitteri, 2024a), FIPS 203, 204, 205 (NIST, 2024b, 2024c, 2024e), SP 800-218 SSDF (Souppaya et al., 2022) |
| Proposed | HIPAA Security Rule NPRM (HHS, 2025), CIRCIA reporting requirements NPRM (CISA, 2024) |
| Enacted but not yet Effective | Colorado AI Act per SB 24-205 and SB 25B-004, effective June 30, 2026 (Colorado General Assembly, 2024, 2025), EU AI Act, phased through August 2, 2027 (European Parliament and Council of the European Union, 2024) |
| Vacated, stayed, or rescinded | 2024 HIPAA reproductive-health privacy rule, vacated in 2025 federal litigation |

*Note.* Status assignments reflect the legal weight of each instrument as of May 2026. NPRM = Notice of Proposed Rulemaking. CIRCIA = Cyber Incident Reporting for Critical Infrastructure Act. PCCP = Predetermined Change Control Plan.

---

## References

Ali, T. E., Ali, F. I., Dakić, P., & Zoltan, A. D. (2024). Trends, prospects, challenges, and security in the healthcare Internet of Things. *Computing, 107*, Article 28. https://doi.org/10.1007/s00607-024-01352-4

Avery, A., Baker, E. W., Wright, B., Avery, I., & Gomez, D. (2025). Media framing and portrayals of ransomware impacts on informatics, employees, and patients: Systematic media literature review. *Journal of Medical Internet Research, 27*, Article e59231. https://doi.org/10.2196/59231

Barker, E. (2020). *Recommendation for key management: Part 1 – General* (NIST SP 800-57 Pt. 1 Rev. 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-57pt1r5

Boyens, J., Smith, A., Bartol, N., Winkler, K., Holbrook, A., & Fallon, M. (2022). *Cybersecurity supply chain risk management practices for systems and organizations* (NIST SP 800-161 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-161r1

Center for Internet Security. (2021). *CIS critical security controls: Version 8*. https://www.cisecurity.org/controls/v8

Chandramouli, R., & Butcher, Z. (2025). *Guidelines for API protection for cloud-native systems* (NIST SP 800-228, Update 1, March 13, 2026). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-228-upd1

Colorado General Assembly. (2024). *Concerning consumer protections in interactions with artificial intelligence systems* (SB 24-205). https://leg.colorado.gov/sites/default/files/2024a_205_signed.pdf

Colorado General Assembly. (2025). *Concerning the artificial intelligence act effective date* (SB 25B-004). https://leg.colorado.gov/bills/sb25b-004

Cybersecurity and Infrastructure Security Agency. (2024). *Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA) reporting requirements: Notice of proposed rulemaking*. 89 Fed. Reg. 23644. https://www.govinfo.gov/content/pkg/FR-2024-04-04/pdf/2024-06526.pdf

Cybersecurity and Infrastructure Security Agency. (2025). *Cross-sector cybersecurity performance goals (Version 2.0)*. https://www.cisa.gov/cross-sector-cybersecurity-performance-goals

Cybersecurity and Infrastructure Security Agency. (2026). *CIRCIA status page*. https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia

Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information security continuous monitoring (ISCM) for federal information systems and organizations* (NIST SP 800-137). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-137

Department of Defense. (2024). *Cybersecurity Maturity Model Certification (CMMC) program* (32 CFR Part 170). 89 Fed. Reg. 83092. https://www.govinfo.gov/content/pkg/FR-2024-10-15/pdf/2024-22905.pdf

Department of Defense. (2025). *Defense Federal Acquisition Regulation Supplement: Assessing contractor implementation of Cybersecurity Maturity Model Certification* (DFARS Case 2019-D041; 48 CFR). https://www.govinfo.gov/content/pkg/FR-2025-09-10/pdf/2025-17379.pdf

European Parliament and Council of the European Union. (2024). *Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)*. Official Journal of the European Union. http://data.europa.eu/eli/reg/2024/1689/oj

Fagan, M., Marron, J., Brady, K., Cuthill, B., Megas, K., Herold, R., Lemire, D., & Hoehn, B. (2021). *IoT device cybersecurity guidance for the federal government: Establishing IoT device cybersecurity requirements* (NIST SP 800-213). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-213

Federal Trade Commission. (2024). *Health Breach Notification Rule: Final rule*. 89 Fed. Reg. 47028. https://www.govinfo.gov/content/pkg/FR-2024-05-30/pdf/2024-10855.pdf

Food and Drug Administration. (2025). *Marketing submission recommendations for a predetermined change control plan for artificial intelligence-enabled device software functions: Guidance for industry and Food and Drug Administration staff*. U.S. Department of Health and Human Services. https://www.fda.gov/media/166704/download

Food and Drug Administration. (2026). *Cybersecurity in medical devices: Quality management system considerations and content of premarket submissions: Guidance for industry and Food and Drug Administration staff*. U.S. Department of Health and Human Services. https://www.fda.gov/media/119933/download

Freyer, N., Gross, D., & Lipprandt, M. (2024). The ethical requirement of explainability for AI-DSS in healthcare: A systematic review of reasons. *BMC Medical Ethics, 25*, Article 104. https://doi.org/10.1186/s12910-024-01103-2

Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1

Marron, J. (2024). *Implementing the Health Insurance Portability and Accountability Act (HIPAA) Security Rule: A cybersecurity resource guide* (NIST SP 800-66 Rev. 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-66r2

National Institute of Standards and Technology. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* (NIST AI 100-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.100-1

National Institute of Standards and Technology. (2024a). *Artificial Intelligence Risk Management Framework: Generative artificial intelligence profile* (NIST AI 600-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.600-1

National Institute of Standards and Technology. (2024b). *Module-lattice-based digital signature standard* (FIPS 204). U.S. Department of Commerce. https://doi.org/10.6028/NIST.FIPS.204

National Institute of Standards and Technology. (2024c). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). U.S. Department of Commerce. https://doi.org/10.6028/NIST.FIPS.203

National Institute of Standards and Technology. (2024d). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29

National Institute of Standards and Technology. (2024e). *Stateless hash-based digital signature standard* (FIPS 205). U.S. Department of Commerce. https://doi.org/10.6028/NIST.FIPS.205

National Institute of Standards and Technology. (n.d.). *SP 800 series*. Computer Security Resource Center. https://csrc.nist.gov/publications/sp800

Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident response recommendations and considerations for cybersecurity risk management* (NIST SP 800-61 Rev. 3). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r3

Office of the National Coordinator for Health Information Technology. (2024). *Health data, technology, and interoperability: Certification program updates, algorithm transparency, and information sharing (HTI-1) final rule*. 89 Fed. Reg. 1192. https://www.govinfo.gov/content/pkg/FR-2024-01-09/pdf/2023-28857.pdf

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207

Ross, R., & Pillitteri, V. (2024a). *Protecting controlled unclassified information in nonfederal systems and organizations* (NIST SP 800-171 Rev. 3). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-171r3

SaberiKamarposhti, M., Ng, K.-W., Chua, F.-F., Abdullah, J., Yadollahi, M., Moradi, M., & Ahmadpour, S. (2024). Post-quantum healthcare: A roadmap for cybersecurity resilience in medical data. *Heliyon, 10*(10), Article e31406. https://doi.org/10.1016/j.heliyon.2024.e31406

Sebastian, G. (2021). Privacy directive compliance relating to increased adoption of emerging technologies. *ISSA Journal, 19*(12), 15–18.

Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure software development framework (SSDF) version 1.1: Recommendations for mitigating the risk of software vulnerabilities* (NIST SP 800-218). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-218

Stouffer, K., Pease, M., Tang, C., Zimmerman, T., Pillitteri, V., Lightman, S., Hahn, A., Saravia, S., Sherule, A., & Thompson, M. (2023). *Guide to operational technology (OT) security* (NIST SP 800-82 Rev. 3). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-82r3

Temoshok, D., Proud-Madruga, D., Choong, Y.-Y., Galluzzo, R., Gupta, S., LaSalle, C., Lefkovitz, N., & Regenscheid, A. (2025). *Digital identity guidelines* (NIST SP 800-63-4). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-63-4

U.S. Department of Health and Human Services. (2021). *Summary of the HIPAA Security Rule*. https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html

U.S. Department of Health and Human Services. (2024). *Healthcare and Public Health (HPH) sector cybersecurity performance goals*. https://hphcyber.hhs.gov/performance-goals.html

U.S. Department of Health and Human Services. (2025). *HIPAA Security Rule to strengthen the cybersecurity of electronic protected health information: Notice of proposed rulemaking*. 90 Fed. Reg. 898. https://www.govinfo.gov/content/pkg/FR-2025-01-06/pdf/2024-30983.pdf

U.S. Department of Health and Human Services, Health Sector Cybersecurity Coordination Center. (2022, July 7). *Quantum cryptography and the health sector*. https://www.hhs.gov/sites/default/files/quantum-cryptography-and-health-sector.pdf

U.S. Department of Health and Human Services, Office for Civil Rights. (2024, September 26). *HHS Office for Civil Rights settles ransomware cybersecurity investigation under the HIPAA Security Rule for $250,000* [Press release]. https://www.hhs.gov/about/news/2024/09/26/hhs-office-civil-rights-settles-ransomware-cybersecurity-investigation-under-hipaa-security-rule-250-000.html

U.S. Securities and Exchange Commission. (2023). *Cybersecurity risk management, strategy, governance, and incident disclosure: Final rule*. 88 Fed. Reg. 51896. https://www.govinfo.gov/content/pkg/FR-2023-08-04/pdf/2023-16194.pdf

Washington State Legislature. (2023). *My Health My Data Act* (RCW 19.373). https://app.leg.wa.gov/RCW/default.aspx?cite=19.373

The White House. (2022). *National security memorandum on promoting United States leadership in quantum computing while mitigating risks to vulnerable cryptographic systems* (NSM-10). https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2022/05/04/national-security-memorandum-on-promoting-united-states-leadership-in-quantum-computing-while-mitigating-risks-to-vulnerable-cryptographic-systems/

Xia, L., Cao, Z., & Zhao, Y. (2024). Paradigm transformation of global health data regulation: Challenges in governance and human rights protection of cross-border data flows. *Risk Management and Healthcare Policy, 17*, 3291–3304. https://doi.org/10.2147/RMHP.S450082
