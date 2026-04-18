---
title: "CMMC POA&M Rules: The 80 Percent Threshold, 5/3-Point Restriction, and 180-Day Window"
description: "How Plans of Action and Milestones work under the CMMC 2.0 final rule — the 80% implementation floor, which controls block conditional certification, and what happens at day 180."
publishDate: 2026-04-19
author: "Justin T. Begarek"
lane: practical
topics:
  - CMMC
  - Compliance
  - DIB
featured: false
draft: false
citations: false
diagrams: false
---

One of the most contested design questions in CMMC 2.0 was whether contractors could use Plans of Action and Milestones to certify before reaching full compliance. The earlier CMMC 1.0 framework prohibited POA&Ms entirely — you either met every control or you did not certify. That position proved untenable for the contractor population.

The final rule at 32 C.F.R. Part 170 resolves this with a conditional certification path. It is not a lenient POA&M regime. It is a narrow exception with a hard floor, a specific list of excluded controls, and a 180-day countdown that ends in either a completed certification or a lapsed status.

*For the full CMMC level structure and cost breakdown, see [CMMC 2.0 Levels, Assessment Paths, and What Certification Costs](/blog/cmmc-2-levels-assessment-cost). For the broader DFARS context, see [The DFARS Clause Stack: 7012, 7019, 7020, and 7021 Explained](/blog/dfars-clause-stack-7012-7019-7020-7021).*

---

## What a POA&M Is — and What It Is Not

A Plan of Action and Milestones is a documented remediation plan for controls that are not yet implemented. It identifies the control gap, the planned remediation activity, the responsible party, and the target completion date.

A POA&M is not a compliance deferral. It does not grant permission to leave controls unimplemented indefinitely. Under CMMC 2.0, it is the documented evidence that supports a conditional certification during a bounded remediation window.

Before the final rule, contractors routinely submitted POA&Ms with multi-year completion timelines in their SPRS assessments. DoD recognized that approach as contrary to the intent of DFARS 252.204-7012, which requires adequate security now, not in 18 months. The final rule closes that gap.

---

## The Three Requirements for Conditional Certification

To receive conditional CMMC status — meaning a CMMC certification that is valid for 180 days rather than three years — a contractor must meet all three of the following requirements at the time of assessment:

**Requirement 1: At least 80 percent of controls implemented.**
The 80% threshold is calculated against the SPRS scoring methodology — not a simple count of 110 controls. Because controls have different point weights, 80% of the scored value (110 points) means the contractor must have implemented controls accounting for at least 88 points. A contractor at a SPRS score of 87 does not qualify.

**Requirement 2: No 5-point or 3-point controls unimplemented.**
The SPRS methodology assigns 5 points to a small set of high-weight controls and 3 points to another group. A contractor with any 5-point or 3-point control unimplemented does not qualify for conditional certification regardless of their overall score. These controls represent requirements DoD considers foundational — leaving them open is not a timing issue, it is a program-disqualifying gap.

The specific 5-point and 3-point controls are identified in the DoD assessment scoring tables in [NIST SP 800-171A](https://csrc.nist.gov/pubs/sp/800/171/a/final) (Assessment Guide). Contractors preparing for CMMC assessment should identify these controls early and prioritize their implementation above all others.

**Requirement 3: A documented POA&M for each remaining gap.**
Every unimplemented control must have a corresponding POA&M entry with: the control identifier, description of the gap, planned remediation activity, responsible party, and target completion date. The target date must fall within the 180-day conditional window.

All three requirements must be met simultaneously. Meeting the 80% threshold without eliminating 5/3-point gaps does not qualify. Having a POA&M without meeting the 80% floor does not qualify.

---

## The 180-Day Window

Once conditional certification is granted, the clock starts. The contractor has 180 days to close every open POA&M item and achieve full implementation.

At day 180, a closeout assessment occurs. This is not a paper review. The assessor — C3PAO for Level 2, DIBCAC for Level 3 — examines the implementation status of every control that was in POA&M at the time of conditional certification.

**If the closeout assessment confirms full implementation:** The certification status converts from conditional to final. The three-year certification period begins.

**If the closeout assessment finds remaining gaps:** The conditional certification lapses. The contractor no longer has a current CMMC status. Contract performance on CMMC-required contracts becomes non-compliant, and new awards cannot be obtained until a full certification assessment is completed and passed.

There is no extension mechanism described in the final rule. The 180-day window is fixed.

---

## What This Means Practically

**Conditional certification is not a business strategy.** A contractor that plans to use conditional certification as a cost-deferral mechanism — get certified now, fix controls later — is assuming the closeout assessment will go well and that their remediation will be complete in 180 days. That is not a plan; it is optimism. The controls that require the most time and resources to implement (identity management, audit logging, incident response, configuration management) are exactly the ones that will not be closed out in 180 days if implementation has not already started.

**The 5/3-point controls must be addressed before assessment.** There is no conditional path through these controls. A contractor that enters a C3PAO assessment with any 5-point or 3-point control unimplemented will not receive conditional certification — they will receive a failed assessment and need to reschedule after remediation. C3PAO time is scarce and expensive. Identify these controls and close them before scheduling your assessment.

**Identify your 88-point floor before engaging a C3PAO.** Run your SSP through the SPRS scoring methodology before your assessment. If your calculated score is below 88, you are not eligible for conditional certification and should not schedule a C3PAO assessment until additional controls are implemented. Spending $50,000–$100,000 on an assessment that results in a failed outcome is avoidable with pre-assessment scoring.

**Document remediation progress continuously.** The 180-day window is not the time to start your remediation work — it is the window in which you must complete it. Every POA&M item should have active remediation in progress before the conditional assessment occurs.

---

## The Controls Most Likely to Block Conditional Certification

Based on the SPRS weighting structure, the categories of controls most likely to carry 5-point or 3-point weights include:

- **Access Control (AC):** User account management, least privilege enforcement, remote access controls
- **Identification and Authentication (IA):** Multi-factor authentication requirements
- **Configuration Management (CM):** Baseline configuration establishment and enforcement
- **Incident Response (IR):** Incident handling capability and reporting
- **Audit and Accountability (AU):** Audit log generation, review, and protection

These are not exotic controls. They are foundational. If your organization has not implemented MFA, cannot demonstrate a tested incident response capability, or lacks a maintained system baseline, you will not qualify for conditional certification — and you may not pass a full assessment either.

The [CMMC practices index](/cmmc/) and [NIST SP 800-171 requirements index](/nist-800-171/) on this site detail each control with practitioner implementation notes. Use them to identify your 5/3-point control status before any C3PAO engagement.

---

## Before You Schedule a C3PAO Assessment

Run through this checklist:

- [ ] Have I calculated my SPRS score using the DoD methodology? Is it 88 or above?
- [ ] Have I identified all 5-point controls? Are they all implemented?
- [ ] Have I identified all 3-point controls? Are they all implemented?
- [ ] Does every remaining gap have a POA&M with a realistic 180-day completion date?
- [ ] Can I demonstrate each implemented control to an assessor with documented evidence?
- [ ] Is my System Security Plan current and does it accurately describe my environment?

If any of these answers is no, schedule remediation time before scheduling an assessor.

C3PAO availability is constrained. Fewer than 100 authorized C3PAOs have completed the joint surveillance process. Assessment slots are booked weeks to months in advance. A failed assessment does not simply reset — you lose your slot, pay for the failed assessment, and rejoin the queue. The investment in pre-assessment readiness pays for itself.
