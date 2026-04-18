---
title: "CMMC 2.0 Levels, Assessment Paths, and What Certification Actually Costs"
description: "A plain-language breakdown of CMMC 2.0's three levels, two assessment paths, POA&M rules, phase-in schedule, and the real cost numbers from DoD's regulatory impact analysis."
publishDate: 2026-04-19
author: "Justin T. Begarek"
lane: practical
topics:
  - CMMC
  - Assessment
  - Compliance
  - DIB
featured: true
draft: false
citations: false
diagrams: false
---

CMMC 2.0 is codified. The final rule at 32 C.F.R. Part 170 took effect December 16, 2024. The companion DFARS acquisition rule — which gives contracting officers the authority to require CMMC as a condition of award — followed in September 2025. The program is no longer a draft. If you handle Controlled Unclassified Information on DoD contracts, this is the compliance requirement you need to understand.

This post breaks down what each level requires, how the assessment process works, what POA&Ms actually allow, when each phase kicks in, and what the numbers in DoD's regulatory impact analysis mean for a real business.

*For the policy and legal framework behind CMMC — why DoD built this structure and where it still underperforms — see [Federal Cybersecurity Law and the Defense Industrial Base](/blog/federal-cybersecurity-law-dib-fragmentation).*

---

## Three Levels, Three Different Situations

CMMC maps to the sensitivity of the information you handle. The level in your solicitation is determined by DoD, not by you.

### Level 1 — Foundational (Federal Contract Information)

Level 1 applies if you handle Federal Contract Information — essentially information provided by or generated for the government under a contract — but not Controlled Unclassified Information.

The requirement is 17 basic safeguarding practices drawn from FAR 52.204-21. These are not new. They were already required under the FAR basic safeguarding clause. What CMMC adds is an annual self-assessment posted to the Supplier Performance Risk System (SPRS) and an annual affirmation from a senior company official confirming continuous compliance.

If you have been ignoring the FAR safeguarding clause, Level 1 is your starting point. If you have been doing the basics, self-assessment should not be a major lift — but the documentation and the SPRS posting are now conditions of award, not suggestions.

### Level 2 — Advanced (Controlled Unclassified Information)

Level 2 applies if you handle CUI on DoD contracts. This is where most of the defense industrial base sits and where the bulk of CMMC compliance work is concentrated.

Level 2 requires all 110 security requirements from [NIST SP 800-171](/nist-800-171/), organized into 14 control families. These are the same requirements that have been binding through DFARS 252.204-7012 since 2017, so if you have been doing SP 800-171 compliance work, you already have a foundation.

The difference CMMC adds is a verified assessment rather than self-scored compliance. Level 2 has two assessment paths:

**Level 2 Self** — Annual self-assessment plus SPRS affirmation. DoD designates which contracts can use this path. It is a limited subset.

**Level 2 C3PAO** — Triennial assessment by a CMMC Third-Party Assessment Organization authorized by the Cyber-AB. Annual affirmations in between. Most CUI-handling contractors will fall under this path.

The C3PAO assessment is not a paper review. The assessor examines your implementation of all 110 controls, interviews personnel, tests technical configurations, and reviews documentation. The resulting score is posted to SPRS and governs your award eligibility for three years.

For the control-level detail — what each of the 110 requirements actually demands — the [NIST SP 800-171 requirements index](/nist-800-171/) and the [CMMC practices index](/cmmc/) cover each requirement with practitioner notes.

### Level 3 — Expert (Highest-Priority Programs)

Level 3 applies to a small number of contractors supporting DoD's most sensitive programs, where advanced persistent threats are an explicit concern.

You cannot go directly to Level 3. It requires prior Level 2 C3PAO certification, then adds a government-led assessment by DCMA's Defense Industrial Base Cybersecurity Assessment Center against 24 controls drawn from NIST SP 800-172. Only DIBCAC conducts Level 3 assessments. There is no private-sector equivalent.

---

## What POA&Ms Actually Allow

One of the most disputed questions in CMMC 2.0 was whether contractors could use Plans of Action and Milestones — partial compliance with a documented remediation plan — to qualify for certification.

The final rule resolves this with a conditional certification path, not a blanket waiver.

A contractor can receive conditional CMMC status valid for 180 days if:
- At least 80% of applicable controls are implemented (as scored against the SPRS methodology)
- No controls worth 5 or 3 points remain unimplemented
- A documented POA&M exists for the remaining controls

At day 180, a closeout assessment must confirm full implementation. If it does not, conditional status lapses and new contract awards are blocked.

The practical meaning: you do not have to be 100% complete to get certified, but the bar is high (80%+, no major gaps), the window is short (180 days), and the consequence of missing the closeout is immediate. This is not the lenient POA&M regime that existed before the final rule. Treat conditional status as an emergency option, not a strategy.

---

## Phase-In Timeline

The CMMC implementation is phased over three years from the effective date of the companion DFARS acquisition rule (September 2025):

**Phase 1 (Year 1, starting September 2025):** DoD may require Level 1 self or Level 2 self as a condition of award in solicitations. Level 2 C3PAO may be required at DoD's discretion.

**Phase 2 (Year 2):** Level 2 C3PAO required in applicable solicitations.

**Phase 3 (Year 3):** Level 3 DIBCAC required in applicable solicitations.

**Phase 4 (Full implementation, end of Year 3 forward):** All CMMC requirements appear in all applicable solicitations. Steady state.

The phased schedule reflects two constraints DoD acknowledged explicitly: the limited near-term capacity of the C3PAO ecosystem and the cost burden on small-business contractors. Fewer than 100 C3PAO firms had completed the Joint Surveillance Voluntary Assessment process at the time of rule publication — a significant bottleneck against an 80,000-plus contractor DIB population that will eventually need Level 2 assessments.

---

## The Real Cost Numbers

DoD's regulatory impact analysis is the most reliable source for cost estimates because it used contractor survey data and modeled the C3PAO assessment market directly. Here are the figures from the analysis:

| Assessment Type | Per-Cycle Cost |
|---|---|
| Level 1 self-assessment | ~$6,000 |
| Level 2 self-assessment | ~$37,000 |
| Level 2 C3PAO certification (every 3 years) | ~$104,000 |
| Level 3 DIBCAC certification (every 3 years) | ~$220,000 |

These are assessment costs only. They do not include the cost of implementing the controls.

For a small business achieving Level 2 C3PAO compliance for the first time, practitioners commonly estimate $300,000–$600,000 in year one (implementation plus assessment), dropping to $100,000–$200,000 per year in steady state. The spread is wide because it depends heavily on your starting point — a contractor at a 50-point SPRS score faces a very different investment than one at 95.

DoD estimated aggregate ten-year industry cost at approximately $4 billion.

---

## The Rev. 2 / Rev. 3 Problem

CMMC 2.0 incorporates NIST SP 800-171 Revision 2 by reference. NIST published Revision 3 in May 2024 with a substantially restructured control set aligned to SP 800-53 Rev. 5.

The binding contractual obligation is Revision 2. The current NIST publication is Revision 3. DoD has indicated it will issue a rule update to migrate to Rev. 3, but timing is uncertain.

For now: implement and document against Revision 2. Understand what Revision 3 changes so you are not surprised when the update arrives. Do not attempt to substitute Rev. 3 language in a C3PAO assessment; assessors evaluate against the incorporated revision.

This is an example of a broader structural problem in federal cybersecurity law — static incorporation by reference in regulations that age faster than the technical standards they incorporate. For context on why this pattern exists and what reforms might fix it, see [Federal Cybersecurity Law and the Defense Industrial Base](/blog/federal-cybersecurity-law-dib-fragmentation).

---

## What to Do Now

If you handle CUI on DoD contracts and have not started:

1. **Conduct a gap assessment against SP 800-171 Rev. 2.** All 110 requirements, documented honestly. Your SPRS score should reflect actual implementation, not aspiration.

2. **Post an accurate score to SPRS.** The DoJ's Civil Cyber-Fraud Initiative has used the False Claims Act against contractors who misrepresented their SP 800-171 compliance. Self-attestation has legal teeth.

3. **Identify which contracts will require Level 2 C3PAO.** Review solicitations and contract modifications for CMMC level designations. If you are a subcontractor, ask your prime.

4. **Build a realistic remediation timeline.** If you are at 60-point SPRS and need Level 2 C3PAO, 90 days is not enough. Budget accordingly.

5. **Find a C3PAO early.** Assessor capacity is constrained. The firms that have completed the JSVA process are on the Cyber-AB Marketplace. Expect lead times.

The [CMMC practices index](/cmmc/) and [NIST SP 800-171 requirements index](/nist-800-171/) on this site cover every requirement. Use them to map your current implementation gaps before you engage an assessor.
