---
title: "CUI vs FCI: What the Difference Means for Your DFARS and CMMC Obligations"
description: "CUI vs FCI explained — how each category determines your CMMC level, which DFARS clauses apply, and what scoping errors create the most compliance exposure."
publishDate: 2026-04-19
author: "Justin T. Begarek"
lane: practical
topics:
  - CMMC
  - DFARS
  - Compliance
  - DIB
featured: false
draft: false
citations: false
diagrams: false
---

The most common question that precedes a CMMC scoping exercise is this: which information do we actually handle? The answer determines your CMMC level, the DFARS clauses that apply, and the assessment path you need to follow.

Two categories matter: Federal Contract Information (FCI) and Controlled Unclassified Information (CUI). They are not the same, they are not interchangeable, and the obligations that attach to each are different enough that misidentifying your information type is a compliance error before you write a single policy.

*For how these categories map to the DFARS clause stack, see [The DFARS Clause Stack: 7012, 7019, 7020, and 7021 Explained](/blog/dfars-clause-stack-7012-7019-7020-7021). For how they determine your CMMC level and assessment path, see [CMMC 2.0 Levels, Assessment Paths, and What Certification Costs](/blog/cmmc-2-levels-assessment-cost).*

---

## Federal Contract Information

FCI is information provided by or generated for the government under a contract to develop or deliver a product or service to the government. It is not intended for public release.

The definition comes from FAR 52.204-21, the basic safeguarding clause. FCI does not require a formal classification or designation. If you receive it from the government under a contract, or if your contract performance generates it, it is FCI.

Examples:
- Performance work statements
- Contract deliverables not publicly released
- Vendor-submitted pricing under an active procurement
- Design requirements shared for contract performance

FCI handling requires implementation of the 17 basic safeguarding requirements in FAR 52.204-21. Under CMMC 2.0, this maps to Level 1. The conformity mechanism is annual self-assessment and an SPRS affirmation. No third-party assessment is required.

---

## Controlled Unclassified Information

CUI is a broader and more complex category. It is defined by the CUI Registry, maintained by the National Archives and Records Administration, which lists over 100 authorized categories of information requiring safeguarding under law, regulation, or government-wide policy.

CUI is not classified. It is not secret. But it is information that carries legal protection requirements that are more demanding than FCI's basic safeguarding floor.

In the DoD context, common CUI categories include:
- Controlled Technical Information (CTI) — technical documents with military or space application that are directly related to a defense article
- Export Controlled information under the International Traffic in Arms Regulations (ITAR) or Export Administration Regulations (EAR)
- Privacy Act information
- Law enforcement sensitive information
- DoD critical infrastructure security information

When a contract involves CUI, DFARS 252.204-7012 applies. That clause requires adequate security implemented through [NIST SP 800-171](/nist-800-171/) (all 110 requirements), 72-hour cyber incident reporting, and 90-day system image preservation. Under CMMC 2.0, CUI handling maps to Level 2, which for most contractors means triennial third-party assessment by a C3PAO.

---

## Covered Defense Information: The Legacy Term

You will encounter "Covered Defense Information" (CDI) in older DFARS documentation and in the text of DFARS 252.204-7012 itself. CDI is not a third separate category — it is a DoD-specific term that encompasses two types of information that require protection under DFARS:

**Controlled Technical Information (CTI):** A subset of CUI consisting of technical information with military or space application that is subject to controls on access, use, reproduction, modification, performance, display, release, disclosure, or dissemination.

**Other information described in a DoD contract:** The contract itself may designate specific information as CDI requiring protection.

For practical purposes: if you see CDI in a clause, think CUI with a DoD-specific scope. The [NIST SP 800-171](/nist-800-171/) requirements that apply to CDI are the same ones that apply to CUI broadly.

---

## How the Distinction Changes Your Obligations

| | **FCI Only** | **CUI (and CDI)** |
|---|---|---|
| CMMC Level | Level 1 | Level 2 (most cases) |
| Required controls | 17 (FAR 52.204-21) | 110 ([NIST SP 800-171](/nist-800-171/)) |
| Assessment method | Annual self-assessment | Triennial C3PAO (usually) |
| SPRS requirement | Basic Assessment score | Basic Assessment score |
| Incident reporting | Not required by DFARS 7012 | 72-hour report to DoD |
| Image preservation | Not required by DFARS 7012 | 90-day requirement |
| Cloud safeguards | Not specified in FAR 52.204-21 | [FedRAMP](/fedramp/) Moderate or equivalent |

If you handle both FCI and CUI — which most Level 2 contractors do — the more demanding CUI requirements govern your entire program. You do not maintain two separate compliance tracks for two information types.

---

## Scoping: How to Determine What You Have

DoD does not always tell you explicitly which information in a contract is CUI. Some contracts include a CUI designation in the performance work statement or contract data requirements list. Others do not.

The scoping process:

**Step 1 — Review the contract documents.** Look for any reference to CUI, CTI, CDI, ITAR/EAR controls, Controlled Technical Information, or privacy data. A DD Form 254 (Department of Defense Contract Security Classification Specification) may appear on classified programs, but it also sometimes indicates CUI handling requirements.

**Step 2 — Apply the CUI Registry categories.** If you are uncertain whether specific information you handle qualifies as CUI, compare it against the NARA CUI Registry categories. If it falls into a listed category, it is CUI.

**Step 3 — Ask the contracting officer.** Contracting officers can designate information as CUI and should be the authoritative source if the contract is ambiguous. Document their response.

**Step 4 — Scope your system boundary.** Once you know what information you handle, identify which systems, personnel, and processes touch that information. That boundary defines your assessment scope for SPRS scoring and CMMC certification.

---

## The Scoping Problem That Creates the Most Risk

The most common scoping error is under-scoping — identifying a narrow system boundary that excludes systems or personnel that actually touch CUI, then scoring or certifying only that narrow scope while the rest of the organization handles CUI outside the assessed boundary.

A contractor that processes CUI in a segregated enclave but also sends CUI in email from a corporate account that was not in scope has not implemented adequate security for the information — only for the enclave. DoD assessors and the DoJ's Civil Cyber-Fraud Initiative both look for exactly this pattern.

The scope of your System Security Plan should match the actual flow of information, not the most convenient boundary.

---

## Subcontractor Scoping

The scoping obligation extends to your supply chain. Under DFARS 252.204-7012, you must flow the clause down to subcontractors performing operationally critical support or handling CDI. Under DFARS 252.204-7020, you cannot award a subcontract unless the sub has a current SPRS score. Under CMMC 2.0 (DFARS 7021), you must flow CMMC requirements to subs at the level applicable to the information they handle.

If your sub handles only FCI, they need Level 1. If they handle CUI, they need Level 2 with appropriate assessment. Primes are responsible for verifying this before subcontract award.

For control-level detail on the 110 requirements that apply to CUI, the [NIST SP 800-171 requirements index](/nist-800-171/) and [CMMC practices index](/cmmc/) cover each control with practitioner notes.
