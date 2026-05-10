---
title: "EO 14110 to EO 14179: Why Federal AI Policy Is an Unstable Compliance Anchor"
description: "On October 30, 2023, EO 14110 set federal AI policy. On January 23, 2025, EO 14179 revoked it. Compliance programs that anchored to the wrong document spent 15 months building toward a moving target."
publishDate: 2026-05-10
author: "Justin T. Begarek"
lane: practical
topics:
  - AI
  - Compliance
  - Healthcare
  - Strategy
featured: false
draft: false
citations: false
diagrams: false
---

On October 30, 2023, President Biden issued Executive Order 14110, "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence." The order directed federal agencies to establish AI safety and security standards, including healthcare-relevant directions to HHS for AI assurance practices and AI safety programs. Compliance professionals who built AI governance programs to its specifications had reasonable confidence that they were tracking federal direction.

On January 23, 2025, President Trump issued Executive Order 14179, "Removing Barriers to American Leadership in Artificial Intelligence." EO 14179 revoked EO 14110 and reoriented federal AI policy toward removing perceived barriers to AI innovation.

Fifteen months. From "this is the federal AI compliance anchor" to "this is no longer federal AI policy at all."

Some agency-level work initiated under EO 14110 has continued — the NIST AI RMF, the Generative AI Profile, NIST SP 800-218A — but the executive direction is no longer the EO 14110 framework. Compliance programs that anchored to the executive order itself rather than to the durable agency outputs underneath spent 15 months building toward a moving target.

This post explains why executive orders are unstable compliance anchors, what the EO 14110 → EO 14179 thread tells us about federal AI policy, and how to anchor an AI compliance program to documents that survive policy transitions.

---

## What EO 14110 Did

EO 14110 was the most ambitious executive-branch AI directive in U.S. history. It directed federal agencies to:

- Establish AI safety and security standards, particularly for dual-use foundation models.
- Develop AI assurance practices for federal use of AI.
- Address algorithmic discrimination and civil rights protections.
- Coordinate AI workforce, immigration, and innovation policy.
- Direct healthcare-specific work through HHS.

Multiple agencies kicked off work in response. NIST accelerated the AI RMF, produced the Generative AI Profile, and developed NIST SP 800-218A for generative AI software development. HHS began work on AI assurance practices in healthcare. OMB issued AI guidance for federal agencies.

For healthcare AI compliance professionals, EO 14110 was the closest the federal government had come to a unifying AI governance direction. Compliance programs began referencing the EO directly in policy documents, training, and customer materials.

---

## What EO 14179 Did

EO 14179 revoked EO 14110 and replaced its policy direction. The substantive framing shifted from safety-and-security focus to barrier-removal focus. Specific EO 14110 directives that had not been completed were no longer required, and OMB and other agencies were directed to revise AI guidance consistent with the new framework.

What did not happen: NIST publications that were initiated under EO 14110 (AI RMF, GenAI Profile, SP 800-218A) were not retracted. They are voluntary, agency-issued documents whose authority does not depend on executive-order continuity. State and federal statutory requirements (HIPAA, FDA PCCP, ONC HTI-1, EU AI Act extraterritorial reach) were unaffected because they do not depend on executive-order direction.

The shift was real but bounded. The executive-direction frame moved. The agency-level documents and statutory requirements did not.

---

## Why Executive Orders Are Unstable Compliance Anchors

Three structural features make executive orders unreliable as compliance anchors.

**They can be revoked at any time by a successor administration.** This is the most direct issue. EO 14110 was operationally significant for 15 months. A compliance program anchored to it had a 15-month effective lifespan that no one announced in advance.

**They direct agencies, not regulated entities directly.** Even when an executive order is in force, regulated entities are not bound by the EO itself. They are bound by the agency rules, guidance, and standards that the EO directs agencies to develop. Some of those outputs survive EO revocation; others do not.

**Their policy direction can shift without changing the underlying technical work.** EO 14179 revoked EO 14110's policy framework but did not retract NIST AI RMF or the GenAI Profile. The technical documents were authored to outlast the executive order even when their initiation depended on it.

The right operational lesson: anchor AI compliance to durable outputs, not to executive-order text.

---

## What Survives Executive Order Transitions

Three categories of AI governance documents survive policy transitions reliably.

**Statutory requirements.** HIPAA, FDA PCCP guidance under section 524B's broader medical-device authority, ONC HTI-1 (which is a final rule under HHS rulemaking authority), the EU AI Act, the Colorado AI Act. These are statute-or-regulation-grounded; executive orders cannot revoke them.

**Agency-issued voluntary frameworks with established institutional momentum.** NIST AI RMF, the Generative AI Profile, NIST SP 800-218A, NIST CSF 2.0. These are NIST publications that agencies and procurement reference regardless of executive direction. EO 14179 did not retract them, and a successor EO 14110-like order would not need to recreate them.

**Procurement-driven expectations.** What customers, insurers, and partners ask for in vendor reviews. These shift more slowly than executive orders because they reflect risk-management consensus rather than political direction.

A healthcare AI compliance program anchored to these three categories is materially stable through executive-order transitions. A program anchored to executive-order text alone is not.

---

## What This Means for Healthcare AI Compliance

Three operational moves follow from the EO 14110 → EO 14179 thread.

**Cite NIST AI RMF, not EO 14110.** Compliance documents, training materials, customer collateral, and policy references should anchor to the durable agency outputs. The AI RMF and the GenAI Profile are the operational federal AI governance reference today.

**Track HIPAA NPRM and CMS/HHS AI work as the binding federal direction.** The HIPAA Security Rule NPRM is the most consequential current federal direction on AI in healthcare, expressly contemplating AI as an emerging issue. ONC HTI-1 is the binding rule on certified health IT AI transparency. These survive any executive-direction shift.

**Maintain compliance intelligence on executive-order changes specifically.** EO transitions create uncertainty about what survives and what does not. A compliance intelligence function should review executive-order revocations within days of issuance and produce a written "what changed, what survived, what to do" memo.

The [compliance status legend](/blog/compliance-status-legend-final-proposed-vacated) framing helps here. An executive order is a kind of "vacated, stayed, or rescinded" instrument when revoked. Tracking it explicitly prevents stale references from accumulating in compliance documentation.

---

## What This Says About Future AI Policy Volatility

Federal AI policy is likely to remain politically contested and therefore relatively unstable through 2028 and beyond. Three implications for healthcare AI compliance:

- Executive-order-level direction will likely shift again with future administrations.
- Statutory and regulatory direction will move more slowly but more durably (HIPAA NPRM, FDA guidance, state laws).
- International direction (EU AI Act) will likely create de facto floors for many U.S. healthcare AI vendors regardless of U.S. federal direction, because EU market access requires EU compliance.

The portfolio of AI governance documents that healthcare programs reference should reflect this. NIST AI RMF and statutory authorities at the top, executive-order references explicitly time-stamped, and international regimes treated as binding constraints rather than peripheral concerns.

---

## What to Track

Two signals matter through 2027:

- Any new executive orders that further reshape federal AI policy direction.
- HHS, FDA, and ONC AI work that proceeds under existing statutory authority regardless of executive direction.

The structural lesson generalizes beyond AI. Executive orders are the most volatile category in the [compliance status legend](/blog/compliance-status-legend-final-proposed-vacated). Treating them as such, rather than as durable compliance anchors, is the discipline that makes a compliance program survive policy transitions without rebuilding.

---

## Sources

- Executive Order 14110, 88 Fed. Reg. 75191 (October 30, 2023). *Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence*.
- Executive Order 14179, 90 Fed. Reg. 8741 (January 23, 2025). *Removing Barriers to American Leadership in Artificial Intelligence*.
- NIST. (2023). *AI Risk Management Framework 1.0*.
- NIST. (2024). *Generative AI Profile* (NIST AI 600-1).
- NIST. (2024). *Secure Software Development Practices for Generative AI* (SP 800-218A).
- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898.
- ONC. (2024). *HTI-1 Final Rule*. 89 Fed. Reg. 1192.
- FDA. (2025). *PCCP Guidance for AI-Enabled Device Software Functions*.
