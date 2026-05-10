---
title: "Change Healthcare and Business Associate Risk: What Healthcare Supply Chains Need to Prove"
description: "The Change Healthcare incident made business-associate cybersecurity a board-level healthcare risk. Contract language is not enough."
publishDate: 2026-05-04
author: "Justin T. Begarek"
lane: practical
topics:
  - HIPAA
  - Healthcare
  - Supply Chain
  - Incident Response
  - Risk Management
featured: false
draft: false
citations: false
diagrams: false
---

The Change Healthcare incident exposed a hard truth in healthcare cybersecurity: business-associate risk is not a legal appendix. It is an operational dependency.

When a vendor or acquired business sits inside claims processing, payment workflows, data exchange, or clinical operations, its security posture becomes part of the healthcare system's availability posture. A compromise can disrupt care delivery, revenue cycle operations, breach notification timelines, patient trust, and public-company disclosure.

For covered entities and large healthcare enterprises, the lesson is direct. A business associate agreement is not a control. It is a contract. The control is the process that verifies, monitors, and responds to supplier risk before and after an incident.

This post is adapted from the full research paper [Prioritized Controls for Compliance: A Healthcare Case Study of UnitedHealth Group](/blog/prioritized-controls-compliance-healthcare-case-study-unitedhealth).

---

## Business Associate Risk Is System Risk

HIPAA and HITECH already make business-associate obligations clear. Covered entities must obtain appropriate assurances from business associates, and business associates can carry direct Security Rule liability. But the Change Healthcare event demonstrated something broader than legal exposure.

A business associate can become a single point of operational failure.

That is especially true when the vendor handles payment processing, identity services, health information exchange, claims routing, patient engagement, analytics, revenue-cycle support, or managed technology operations. The vendor may not be a hospital, but its failure can create hospital consequences.

Security teams should therefore treat high-impact business associates as part of the risk surface, not as external paperwork.

---

## The NIST Controls That Matter

NIST SP 800-53 Revision 5 gives healthcare organizations a better way to make supplier risk concrete. Four control areas are especially important.

**SR-2: Supply Chain Risk Management Plan.** The organization needs a written, maintained plan for how supply-chain cybersecurity risk is governed. The plan should define roles, supplier tiers, review cadence, risk acceptance, escalation, and integration with procurement and legal.

**SR-3: Supply Chain Controls and Processes.** Supplier controls should be embedded into acquisition, contracting, onboarding, monitoring, and offboarding. This is where security requirements become procurement behavior rather than after-the-fact review.

**SR-6: Supplier Assessments and Reviews.** High-risk suppliers should be assessed periodically. The assessment should not be one generic questionnaire for everyone. It should reflect data access, remote access, operational criticality, subcontractor dependencies, and incident history.

**SA-9: External System Services.** If an external service stores, processes, transmits, or materially affects ePHI, the organization needs defined security requirements, monitoring expectations, and accountability for those services.

Those controls do not eliminate vendor risk. They make it governable.

---

## Tier Suppliers By Consequence

Healthcare supplier programs often fail because they treat every vendor the same. That produces too much review for low-risk vendors and too little review for the vendors that can actually damage operations.

A useful supplier tiering model starts with five questions:

- Does the supplier store, process, or transmit ePHI?
- Does the supplier have remote access into production systems?
- Would supplier downtime interrupt clinical care, claims processing, pharmacy operations, payment processing, or patient access?
- Does the supplier rely on subcontractors that touch the same data or workflow?
- Would a supplier incident trigger OCR, state, contractual, SEC, or customer notification obligations?

Suppliers with "yes" answers across several of those categories belong in the highest review tier. They need stronger due diligence, clearer incident-notification terms, recurring reassessment, evidence requests, and executive visibility.

Lower-risk suppliers still need basic contractual safeguards, but they should not consume the same review energy.

---

## What The Contract Should Trigger

Contract language matters, but only if it triggers operational behavior.

For high-risk business associates, the agreement should support:

- Defined security requirements mapped to recognized controls.
- Timely incident notification and escalation paths.
- Cooperation during forensic investigation and breach analysis.
- Requirements for subcontractor oversight.
- Evidence of risk analysis, access control, logging, backup, incident response, and vulnerability management.
- Termination or remediation rights when control failures are material.

The security team should know which vendors have those terms. Legal should know which vendors lack them. Procurement should know when a new vendor cannot be onboarded without additional review.

That is the difference between contractual compliance and supplier risk management.

---

## Incident Response Has To Include The Vendor

Vendor risk is often handled during procurement and forgotten during incident response planning. That is a mistake.

The incident response plan should define what happens when the incident begins outside the organization but affects internal operations or regulated data. That means contact paths, evidence expectations, privilege revocation procedures, alternate processing plans, breach notification coordination, and executive decision points.

For healthcare organizations, this is not abstract. A supplier outage can become a patient-access problem. A supplier breach can become a covered-entity notification problem. A supplier ransomware event can become a public-company materiality question.

IR-6 and IR-8 should therefore connect to SR and SA controls. Supplier incident response is not a separate discipline. It is part of the same control program.

---

## The Bottom Line

The Change Healthcare incident made clear that business-associate cybersecurity is not a back-office compliance issue. It is a resilience issue.

Healthcare organizations need to prove more than the existence of business associate agreements. They need evidence that critical suppliers are identified, tiered, assessed, monitored, contractually bound, and integrated into incident response.

That is where NIST supply-chain controls add practical value: they turn vendor risk from a legal assumption into an operating program.
