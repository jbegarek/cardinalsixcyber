---
title: "DFARS 7012 Incident Reporting: What to Include in a 72-Hour Cyber Incident Report"
description: "What a DFARS 7012 cyber incident report must contain, when the 72-hour clock starts, what to preserve, and common reporting errors that create compliance exposure."
publishDate: 2026-04-19
author: "Justin T. Begarek"
lane: practical
topics:
  - DFARS
  - Compliance
  - DIB
featured: false
draft: false
citations: false
diagrams: false
---

DFARS 252.204-7012 requires DoD contractors to report cyber incidents within 72 hours of discovery. That requirement has been in place since 2017. Most contractors know it exists. Fewer have a documented, tested process that would produce a compliant report when an incident actually occurs.

This post covers what the report must contain, when the clock starts, what you must preserve, and the errors that turn a manageable incident into a compliance problem.

*For the full clause context and how 7012 fits with the rest of the DFARS stack, see [The DFARS Clause Stack: 7012, 7019, 7020, and 7021 Explained](/blog/dfars-clause-stack-7012-7019-7020-7021). For the CMMC implications of incident response capability, see [CMMC 2.0 Levels, Assessment Paths, and What Certification Costs](/blog/cmmc-2-levels-assessment-cost).*

---

## When the Clock Starts

The 72-hour window begins at discovery, not at the end of your investigation.

This is the most consequential operational point in the clause. DoD does not require you to know the full scope of an incident before reporting. It does not require you to know the root cause, the attacker's identity, or the complete list of affected systems. It requires you to report within 72 hours of the moment you determined that a cyber incident occurred.

A cyber incident, for DFARS 7012 purposes, is any actions taken through the use of computer networks that result in a compromise or potential compromise of the confidentiality, integrity, or availability of any DoD information, including covered defense information, or that impact the contractor's ability to provide operationally critical support.

The threshold is "result in a compromise or potential compromise." You do not need certainty. You need reasonable belief that a cyber incident occurred.

If your security team identifies a potential compromise at 2pm on a Tuesday, you have until 2pm on Friday at the latest. In practice, you should have a draft report submitted before the 72-hour mark even if the investigation is not complete, because the initial report can be supplemented.

---

## Where to Submit the Report

Reports are submitted to DoD through the DIBNet Portal at dibnet.dod.mil. The system requires a DoD-approved medium assurance certificate or a CAC for authentication.

If you do not have a DIBNet account, establishing one takes time. You should not wait for an incident to discover that your point of contact cannot log in. Verify your DIBNet account access is current before you need it.

---

## What the Report Must Contain

DFARS 7012 and the associated reporting portal require the following information in an incident report:

**Company identification:**
- Company name and address
- Cage Code (Commercial and Government Entity code — this is your DoD supplier identifier)
- DUNS or UEI number

**Contract information:**
- Contract numbers affected by the incident
- Name and contact information for your contracting officer

**Incident details:**
- Date the incident was discovered
- Location of the compromise — which systems, facilities, or geographic sites were affected
- Type of compromise — which categories of CDI or covered information may have been affected
- A description of the technique or method used in the cyber incident, to the extent known at the time of reporting

**Impact assessment (to the extent known):**
- Which systems were affected
- What information was potentially accessed, exfiltrated, or disrupted
- Whether the incident affected the contractor's ability to provide operationally critical support

**Technical indicators (to the extent known):**
- Any known malware signatures, indicators of compromise, IP addresses, or technical details that may assist DoD in understanding the incident

You do not need to have all of this information with certainty at the time of the initial report. Include what you know and indicate where the investigation is ongoing.

---

## What You Must Preserve

Concurrent with reporting, DFARS 7012 requires preservation for at least 90 days:

- Images of all known affected information systems — full disk images, not just logs
- All data related to the incident and associated systems
- Malware samples if identified and safe to retain

DoD has the right to request access to these preserved artifacts for forensic analysis. If requested, you must provide access within a reasonable timeframe.

The 90-day preservation requirement means you cannot image a system, restore it to operation, and then discard the image after a few weeks. The image must be retained and protected for the full 90 days from the date of reporting.

If you use cloud services for CDI, the preservation obligation extends to those environments. The cloud provider's data retention settings do not automatically satisfy this requirement. Verify your incident response procedures address cloud-hosted evidence preservation.

---

## The Malware Submission Obligation

If you discover malicious software in connection with a reported incident, DFARS 7012 requires you to submit the malware to DoD's DIBNet portal or to the Defense Cyber Crime Center (DC3). This is not optional. Submit a copy — not the live malware — and coordinate with your security team to ensure submission does not expose your environment or DC3 to additional risk.

---

## Subcontractor Reporting Obligations

If a subcontractor experiences a cyber incident that involves CDI or operationally critical support under your prime contract, the subcontractor must report to the prime. The prime must then report to DoD. The 72-hour window applies from the subcontractor's discovery, not from when the sub notifies the prime.

This means your subcontractor incident response procedures must include a contractual requirement for rapid notification to your prime contract program team. If your subcontract does not include flow-down of DFARS 7012 (which is itself a compliance gap), you are exposed for incidents in the subcontractor's environment that are never reported.

---

## The Most Common Reporting Errors

**Starting the clock at investigation conclusion rather than discovery.** The most common error. Contractors investigate, determine scope, and then report — by which time 72 hours has passed. The report goes in late. The clause does not permit this. Report first, supplement as the investigation progresses.

**Not testing DIBNet access before an incident.** A contractor that discovers a breach and then spends the first six hours troubleshooting DIBNet authentication has lost a significant fraction of the reporting window on a process problem. Test your reporting process on a non-incident day.

**Reporting only confirmed CDI exposure rather than potential compromise.** The clause threshold is "potential compromise." If you cannot confirm that CDI was not accessed, the correct interpretation is that it potentially was. Reporting conservatively is appropriate and does not trigger penalty — failing to report when you should have can.

**Failing to preserve system images before remediation.** Incident responders often prioritize containment and recovery. If imaging is not part of the incident response playbook before remediation steps, it may not happen at all. Update your incident response procedure to explicitly sequence image preservation before system restoration.

**Not involving legal counsel in the reporting decision.** Cyber incident reports are submitted under contract. Statements in those reports can have False Claims Act implications if they are materially inaccurate. Legal review of the report before submission is not a delay tactic — it is risk management.

---

## What CMMC Requires for Incident Response Capability

[NIST SP 800-171](/nist-800-171/) requirement 3.6.1 (CMMC practice [IR.L2-3.6.1](/cmmc/ir-l2-3-6-1)) requires contractors to establish an operational incident-handling capability for organizational systems that includes preparation, detection, analysis, containment, recovery, and user response activities.

3.6.2 (CMMC practice [IR.L2-3.6.2](/cmmc/ir-l2-3-6-2)) requires tracking, documenting, and reporting incidents consistent with established criteria.

A written incident response plan that has never been tested does not satisfy these requirements. Assessors at Level 2 C3PAO assessments will ask for evidence of incident response exercises, tabletops, or actual incident documentation. Build the capability first, then document it, then test it.

The 72-hour reporting requirement in DFARS 7012 is a downstream artifact of having or not having an operational incident response capability. Contractors with mature IR programs discover incidents faster, scope them faster, and submit accurate reports faster. Contractors without them discover incidents late, miss the reporting window, and submit incomplete reports.

---

## Practical Steps

1. **Verify your DIBNet portal access today.** Confirm the point of contact who will submit reports can authenticate and navigate the portal.

2. **Update your incident response procedure** to explicitly include: initial assessment trigger, image preservation before remediation, 72-hour report submission, malware submission, and subcontractor notification requirements.

3. **Define your "discovery" threshold in writing.** At what point does your team determine that a cyber incident has occurred? That determination is the clock start. Make it explicit so it is not left to individual judgment under pressure.

4. **Run an annual tabletop.** Simulate an incident, walk through the response procedure, and submit a practice report (clearly marked as a drill) to validate the process. This is also the evidence a C3PAO will ask for.

5. **Review your subcontracts.** Confirm DFARS 7012 is flowed down and that the subcontract includes an explicit notification window that gives you time to submit the prime report within 72 hours of the sub's discovery.
