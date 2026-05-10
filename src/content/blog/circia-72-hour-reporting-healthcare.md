---
title: "CIRCIA 72-Hour Reporting for Healthcare: How It Layers on HIPAA, FTC HBNR, and State Breach Law"
description: "CIRCIA is not finalized, but healthcare incident response programs that wait until it is will not be ready. Here is how it stacks against HIPAA, state, and FTC notification."
publishDate: 2026-05-18
author: "Justin T. Begarek"
lane: practical
topics:
  - Healthcare
  - HIPAA
  - Incident Response
  - Compliance
  - CIRCIA
featured: false
draft: false
citations: false
diagrams: false
---

The Cyber Incident Reporting for Critical Infrastructure Act of 2022 directed CISA to write reporting rules for covered cyber incidents and ransom payments at critical-infrastructure entities. CISA published the proposed rule on April 4, 2024 (89 Fed. Reg. 23644). Mandatory reporting will not be required until the final rule takes effect, and CISA's status page through April 2026 confirms the final-rule timeline has slipped at least once.

That delay does not reduce CIRCIA's operational consequence for healthcare. It increases it. Healthcare entities are explicitly named as critical infrastructure, with HHS as the Sector Risk Management Agency. When CIRCIA finalizes, healthcare incidents will trigger a four- or five-way reporting obligation simultaneously: HIPAA breach notification, state breach notification, FTC Health Breach Notification Rule (where applicable), CIRCIA, and contractual BAA notifications.

This post explains how CIRCIA layers on top of healthcare's existing reporting stack, why a unified reporting decision tree is more useful than a CIRCIA-specific playbook, and what to build now while CIRCIA remains proposed.

---

## What CIRCIA Proposes

The CIRCIA NPRM proposes two reporting obligations for covered entities:

- **Covered cyber incidents** must be reported within 72 hours of a reasonable belief that a covered incident occurred.
- **Ransom payments** must be reported within 24 hours of payment.

Both reports must contain detailed factual content. CIRCIA also proposes preservation requirements for relevant data and a defined update cadence as facts develop. The covered-entity definition is broad, drawing from CISA's critical-infrastructure sector definitions, and most large and many mid-size healthcare delivery organizations and business associates would be in scope.

The Congressional Research Service's CIRCIA brief (CRS, 2024) is the cleanest secondary summary. The 89 Fed. Reg. 23644 NPRM and the CISA CIRCIA status page are the primary sources.

---

## Why Healthcare Already Has a Reporting Stack

Healthcare incident reporting is already a layered obligation. CIRCIA is the fifth layer, not the first.

**HIPAA breach notification.** Covered entities and business associates must notify affected individuals, HHS, and in some cases the media following a breach of unsecured PHI. Timelines are 60 days for individual notification, with HHS notification on the same window for breaches affecting 500 or more individuals (45 CFR Subpart D).

**State breach notification.** All 50 states have breach notification laws with varying timelines, content requirements, and AG-notice triggers. State law often runs alongside HIPAA, not under it.

**FTC Health Breach Notification Rule.** The FTC's 2024 amendments (89 Fed. Reg. 47028, effective July 29, 2024) cover non-HIPAA health apps, personal health record vendors, and PHR-related entities. Many digital-health, wellness, and consumer-facing healthcare services fall under FTC HBNR rather than HIPAA.

**Contractual BAA and customer notifications.** Business associate agreements typically contain customer-notification clauses with shorter timelines than HIPAA's statutory floor. Larger customers often require 24-hour or 48-hour notice of suspected incidents.

**SEC cybersecurity disclosure rule** (for public companies and certain partners). Material cybersecurity incidents must be disclosed on Form 8-K within four business days of materiality determination.

CIRCIA, when finalized, will overlay all of this with a 72-hour cyber incident timeline and a 24-hour ransom payment timeline, both with content requirements that may not align cleanly with HIPAA breach reports.

---

## The Decision-Tree Problem

The operational risk is not learning each rule. The operational risk is making contradictory decisions in the first hours of an incident.

A ransomware event at a covered entity that processes both HIPAA-covered care and consumer-facing telehealth could simultaneously generate:

- HIPAA breach analysis on a 60-day clock for individual notice.
- FTC HBNR notice for the consumer telehealth flow.
- State breach notification for residents of states with shorter clocks.
- CIRCIA covered-incident report at 72 hours (when finalized).
- CIRCIA ransom-payment report at 24 hours if the entity pays.
- BAA notice to upstream customers within 24 to 48 hours.
- SEC 8-K materiality assessment if the entity or a public-company partner is involved.
- DFARS 252.204-7012 incident report at 72 hours if any CUI is in scope.

Each of these has different content requirements, different recipient agencies, and different "reasonable belief" or "discovery" triggers. Trying to handle them as separate playbooks during an active incident is how reporting gaps and contradictory disclosures get created.

The right model is a single incident handling process aligned to NIST SP 800-61 Rev. 3 (Cichonski et al., 2025) plus a layered reporting decision tree that maps incident facts to all applicable reporting regimes simultaneously.

---

## What to Build Before CIRCIA Finalizes

Three artifacts pay off whether CIRCIA finalizes in 2026, 2027, or later.

**A unified incident handling process.** SP 800-61 Rev. 3 supplies the lifecycle: preparation, detection and analysis, containment, eradication and recovery, post-incident activity. Healthcare-specific tailoring should add clinical-availability impact as a first-class severity dimension and a defined patient-safety escalation path.

**A layered reporting decision tree.** A flowchart that takes incident facts (data type, affected populations, contractual relationships, public-company exposure, ransom payment status) and outputs which reporting regimes apply, what the timeline is, what content the report needs, and who the named recipient is. The decision tree is updated when each underlying rule changes, including when CIRCIA finalizes.

**A CIRCIA-readiness drill.** A tabletop that exercises the 72-hour CIRCIA timeline against the existing HIPAA/state/FTC/BAA stack, even though CIRCIA is not yet enforceable. Drills surface coordination problems, content gaps, and contradictory disclosure risks that no policy review will find.

NIST SP 800-61 Rev. 3 is the federal reference for the underlying capability. The CIRCIA NPRM and CISA's status page are the inputs to the decision tree. The HIPAA Security Rule NPRM (HHS, 2025) proposes contingency-testing expectations that this drill satisfies.

---

## Where CIRCIA Conflicts With HIPAA

A few specific tensions deserve attention now.

CIRCIA reports go to CISA. HIPAA breach reports go to HHS OCR. The two agencies coordinate but their content needs differ. A CIRCIA-style technical incident description is not the same artifact as an OCR breach analysis.

CIRCIA's "reasonable belief" trigger is operationally earlier than HIPAA's "discovery of breach" standard. Organizations may need to file a CIRCIA report before they have completed the HIPAA breach analysis that determines whether OCR notice is required.

CIRCIA's 72-hour clock starts on reasonable belief. HIPAA's 60-day individual notice clock starts on discovery. State clocks vary. The first-hours decisions about what to communicate, to whom, in what format, are the highest-stakes part of the response and they cannot be improvised.

The CISA CIRCIA status page is the canonical source for the current rulemaking status; check it before any customer-facing readiness commitments.

---

## What This Means for Business Associates

Business associates handling ePHI for covered entities will face CIRCIA exposure on two paths. Some BAs will themselves meet the covered-entity definition. Others will be downstream of covered customers who will demand earlier and more detailed notice in BAA renewals.

The practical consequence is that BAA notification clauses will tighten. A BA that today receives a HIPAA-style 60-day window from a customer should expect 24-hour or 48-hour notification clauses to become standard, with explicit CIRCIA-aligned content. Reviewing existing BAAs and DPAs against likely CIRCIA-driven clauses is a 2026 task, not a post-finalization task.

For broader BA framing, see [Change Healthcare and Business Associate Risk](/blog/change-healthcare-supply-chain-risk-business-associates).

---

## What to Track

- The CIRCIA final-rule publication date and effective date (CISA status page).
- Whether the final rule preserves the 72/24-hour structure or modifies thresholds and content.
- Coordination guidance between CISA and HHS OCR on healthcare incident reporting.
- BAA template updates from major healthcare procurement organizations and large covered entities.

CIRCIA is the kind of compliance change that produces non-compliance windows for organizations that wait. The cost of preparing while it remains proposed is a tabletop and a decision tree. The cost of waiting is paid in the first 72 hours of the next incident.

---

## Sources

- CISA. (2024). *CIRCIA Reporting Requirements NPRM*. 89 Fed. Reg. 23644.
- CISA. (2026). *CIRCIA status page*. [cisa.gov/circia](https://www.cisa.gov/circia)
- Congressional Research Service. (2024). *CIRCIA NPRM In Brief* (R48025).
- Cichonski et al. (2025). *NIST SP 800-61 Rev. 3*.
- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898.
- FTC. (2024). *Health Breach Notification Rule Final Amendments*. 89 Fed. Reg. 47028.
