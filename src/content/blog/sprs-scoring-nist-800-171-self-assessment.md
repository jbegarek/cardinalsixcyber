---
title: "SPRS Scoring: How to Self-Score Your NIST SP 800-171 Assessment"
description: "How the DoD SPRS scoring methodology works, what the -203 to 110 scale means, and what common scoring mistakes cost contractors at award time."
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

Every DoD contractor handling Controlled Unclassified Information must have a current NIST SP 800-171 assessment score posted in the Supplier Performance Risk System before contract award. That requirement comes from DFARS 252.204-7019, and it has been in place since November 2020.

The score is not a simple percentage. It runs from -203 to 110, and the methodology assigns different point weights to different controls. Understanding how it works is not optional — it determines your award eligibility, affects how program offices perceive your risk profile, and creates False Claims Act exposure if your posted score does not reflect your actual implementation.

*This post is part of the DFARS and CMMC compliance series. For the full clause context, see [The DFARS Clause Stack Explained](/blog/dfars-clause-stack-7012-7019-7020-7021). For how SPRS scoring fits into CMMC 2.0 certification, see [CMMC 2.0 Levels, Assessment Paths, and What Certification Costs](/blog/cmmc-2-levels-assessment-cost).*

---

## What the Scale Actually Means

A perfect score of 110 means all 110 NIST SP 800-171 requirements are fully implemented with no gaps. Most contractors are not at 110.

The starting point is 110. Every unimplemented or partially implemented requirement subtracts points — not 1 point each, but variable amounts based on the requirement's assigned weight in the DoD scoring methodology. Requirements worth more points penalize the score more heavily when missing.

The scale can go below zero because partial or missing controls are scored against their full weight. A contractor that has implemented nothing scores -203, not 0. A contractor that has implemented most controls but is missing several high-weight ones might score 40–70.

A score below 110 does not automatically disqualify you from award. DoD uses SPRS scores as a risk signal, not a hard pass/fail threshold at the Basic Assessment level. However, a score below roughly 70 is frequently flagged by contracting officers as requiring explanation, and some program offices apply informal floors. A conditional CMMC certification (the 80% threshold path) requires your score to reflect that 80% threshold, which translates to meeting controls worth at least 88 of the 110 points.

---

## The Three Assessment Types That Feed SPRS

SPRS holds scores from three types of assessments:

**Basic Assessment (Self):** The contractor scores its own implementation using the DoD methodology. Posted by the contractor in SPRS. This is what DFARS 7019 requires before award.

**Medium Assessment:** A DoD-conducted desk review of the contractor's System Security Plan and supporting documentation without a site visit. DoD posts this score; it overrides the contractor's self-assessment.

**High Assessment:** A DoD-conducted on-site review, typically by DCMA's DIBCAC. DoD posts this score; it overrides all prior scores. Under CMMC 2.0, a DIBCAC High Assessment can override even a C3PAO certification score.

When you post a Basic Assessment self-score, you are not done. DoD can come in at any time and conduct a Medium or High assessment that replaces your posted number. Your score should be defensible on the day you post it.

---

## How to Score Each Requirement

The DoD methodology assigns a point value to each of the 110 requirements. Not every requirement is documented in public-facing materials at the individual control level, but the methodology is described in the Assessment Guide for NIST SP 800-171 (NIST SP 800-171A).

For each requirement, you determine one of three states:

**Met:** The requirement is fully implemented. No adjustment to the score.

**Not Met:** The requirement is not implemented. The full point value is subtracted from 110.

**Partially Met (with POA&M):** The requirement is partially implemented and you have a documented Plan of Action and Milestones. Partial credit may apply in some assessment contexts, but for Basic Self-Assessment scoring purposes, a partially met control without full implementation is typically treated as not met.

The practical process:
1. Review each of the 110 requirements against your documented System Security Plan.
2. For each requirement, determine the implementation status with supporting evidence.
3. Calculate the score by subtracting the assigned weights of all unimplemented requirements from 110.
4. Post the score to SPRS along with the date of the assessment, the name of the assessing official, and the plan expiration date.

---

## Common Scoring Mistakes

**Scoring aspirational implementation as current.** The score must reflect what is implemented now, not what you plan to implement. If your multi-factor authentication rollout is 60% complete, the control is not met. Scoring it as met while the implementation is still in progress is the kind of gap that creates False Claims Act exposure.

**Ignoring subcontractor and cloud scope.** If a subcontractor handles CUI on your behalf, their systems are in scope. If you use a cloud provider for CUI storage or processing, that provider's environment is in scope — and must meet FedRAMP Moderate or equivalent. Excluding these from your SSP and scoring them as out of scope when they are not is a misrepresentation.

**Not documenting the basis for each score decision.** The SPRS score is a number, but the evidence behind it should exist in your SSP and supporting documentation. When DoD conducts a Medium or High assessment, assessors will ask for the evidence behind each "Met" determination. If it is not documented, the control is considered not met.

**Treating the posted score as permanent.** SPRS scores expire. Your Basic Assessment score should reflect a current assessment — typically within the past 12 months for self-assessments, or the assessment cycle timeline applicable to your CMMC level. An outdated score is still a risk signal even if the control implementation has improved.

**Scoring controls you cannot demonstrate.** If you claim a control is met because a vendor tool handles it, you must be able to demonstrate that the tool is configured and operating correctly in your environment. Vendor SaaS agreements do not satisfy control implementation without configuration evidence.

---

## What the Score Means at Award Time

Contracting officers check SPRS as part of source selection. They see your score, the date of your assessment, and whether there is a DoD-conducted assessment that has overridden your self-score.

A missing score can disqualify an otherwise competitive proposal before it is read. DFARS 7019 is a pre-award condition.

A low score (below 70) flags risk. Contracting officers may request explanation, require an accelerated remediation timeline, or escalate for program office review. Some program offices apply informal floors. None of this is published as a bright-line rule, which is why posting an accurate score — and having a clear remediation roadmap for gaps — is better than posting an inflated score that does not survive scrutiny.

A score that contradicts a DoD-conducted assessment creates a record of discrepancy. That discrepancy is the factual foundation for a False Claims Act case if the contractor has been billing under contracts where compliance was a condition of award.

---

## Practical Steps

If you have not yet posted a SPRS score:
1. Conduct a structured gap assessment against all 110 [NIST SP 800-171](/nist-800-171/) requirements.
2. Document your SSP — what systems are in scope, what controls are implemented, and where gaps exist.
3. Score each requirement honestly using the DoD methodology.
4. Create POA&Ms for every gap, with realistic completion dates.
5. Post the score to SPRS via the PIEE portal before any applicable solicitation closes.

If your posted score is more than 12 months old or you have made significant infrastructure changes, conduct a reassessment before your next proposal submission.

For control-level detail on each of the 110 requirements, the [NIST SP 800-171 requirements index](/nist-800-171/) and [CMMC practices index](/cmmc/) cover every control with practitioner notes.
