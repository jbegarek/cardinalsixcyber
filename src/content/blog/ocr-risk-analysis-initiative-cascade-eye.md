---
title: "OCR's Risk Analysis Initiative and the $250,000 Cascade Eye Settlement: What It Tells You About Current Enforcement"
description: "On September 26, 2024, OCR settled a ransomware case for $250,000 with a two-year corrective action plan. The findings tell you exactly what to fix in your program."
publishDate: 2026-05-15
author: "Justin T. Begarek"
lane: practical
topics:
  - HIPAA
  - Healthcare
  - Ransomware
  - Risk Management
  - Compliance
featured: false
draft: false
citations: false
diagrams: false
---

On September 26, 2024, the HHS Office for Civil Rights announced a $250,000 settlement with Cascade Eye and Skin Centers, P.C., a Washington State health-care provider, following an OCR investigation into a ransomware attack that affected approximately 291,000 ePHI files.

The settlement was OCR's fourth ransomware-related Security Rule resolution. In the same announcement, OCR reported a 264% increase in large breaches involving ransomware since 2018. Both data points are part of OCR's ongoing Risk Analysis Initiative — a focused enforcement effort grounded in HIPAA Security Rule risk-analysis failures.

For healthcare cybersecurity programs, the Cascade Eye case is more useful than most enforcement reading because the OCR findings are specific, the corrective action plan is public, and the deficiencies map almost cleanly to the kind of evidence a competent program already produces. This post walks through what OCR found, what the CAP requires, and what to do about it before you become the next case.

---

## What OCR Found

Two specific deficiencies anchor the resolution:

**Failure to conduct a compliant risk analysis.** OCR found that Cascade Eye and Skin Centers had not conducted a compliant risk analysis to determine the potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI. This is the most-cited finding in the Risk Analysis Initiative across multiple settlements, not just this one.

**Failure to monitor information system activity.** OCR found insufficient monitoring of information system activity sufficient to protect against a cyber-attack. Logging and review failures are the second most-cited finding across the Initiative.

The corrective action plan requires Cascade Eye to:

- Conduct an accurate and thorough risk analysis.
- Develop a risk management plan responsive to the analysis.
- Establish written processes for reviewing information system activity.
- Maintain emergency-response policies.
- Implement unique-identifier processes.
- Revise HIPAA policies and procedures.

The CAP runs for two years. The dollar amount ($250,000) is substantial for a small practice but reflects an OCR posture that emphasizes corrective action and documented program improvements over headline-driving fines.

---

## Why Risk Analysis Failures Are the Anchor

OCR has been clear about the priority. The Risk Analysis Initiative was launched specifically because risk-analysis deficiencies are the most reliable predictor of subsequent breach impact in OCR's investigation sample. A weak risk analysis means an organization does not know which systems hold ePHI, how they are exposed, or what controls are required. Every downstream Security Rule failure flows from that gap.

A defensible HIPAA risk analysis has six observable properties:

- It is dated and current. Risk analyses more than 12 to 18 months old are increasingly difficult to defend without a written rationale.
- It is scoped to the actual ePHI environment. Generic enterprise risk assessments do not satisfy the Security Rule. The risk analysis must address the systems, data flows, and vendors that actually touch ePHI.
- It traces threats and vulnerabilities to specific systems. Statements like "ransomware is a threat" do not satisfy. "Workstation X running OS Y in environment Z is exposed to threat T because of vulnerability V with likelihood L and impact I" does.
- It ties findings to a treatment plan with named owners and dates.
- It is updated when the environment changes — a new EHR, a new vendor, a new clinic, a new acquisition, a new ransomware variant in the threat landscape.
- It is supported by NIST SP 800-30 Rev. 1 methodology and NIST SP 800-66 Rev. 2 (Marron, 2024) HIPAA-specific application.

The Cascade Eye CAP makes the standard explicit: an "accurate and thorough" risk analysis. That language is from 45 CFR 164.308(a)(1)(ii)(A) itself. OCR is enforcing the rule as written.

---

## Why Information-System-Activity Review Is the Second Anchor

The second Cascade Eye deficiency — insufficient monitoring of information system activity — is also rule-text-driven. 45 CFR 164.308(a)(1)(ii)(D) requires implementation of procedures to regularly review records of information system activity such as audit logs, access reports, and security incident tracking reports.

The operational test for this requirement is concrete. Three observable artifacts demonstrate compliance:

- Audit logs are being generated across systems that touch ePHI.
- Logs are being retained long enough to support investigation (NIST SP 800-66 Rev. 2 references multi-year retention as defensible).
- Someone is reviewing those logs on a defined cadence and producing review records.

The third artifact is where most healthcare programs fail. Logs that nobody reviews do not satisfy 164.308(a)(1)(ii)(D). The CAP's requirement to "establish written processes for reviewing information system activity" is exactly the gap most ransomware investigations surface.

---

## How This Connects to the HIPAA NPRM

The HIPAA Security Rule NPRM (HHS, 2025) proposes more explicit safeguards for asset inventory, audit logs, network maps, vulnerability management, and contingency-plan testing. Almost every NPRM proposal lines up with a Risk Analysis Initiative finding.

This is not a coincidence. The NPRM is, in part, a codification of what OCR has been enforcing. A program that is ready for the Risk Analysis Initiative is materially ready for the NPRM. A program that cannot survive the Risk Analysis Initiative will not survive the NPRM either.

See [The HIPAA Security Rule NPRM: A Control Roadmap](/blog/hipaa-security-rule-nprm-control-roadmap) for the full NPRM mapping.

---

## What to Build, Specifically

Three artifacts cover most of what OCR is enforcing today.

**A current, defensible HIPAA risk analysis.** Scoped to the actual ePHI environment, dated within the last 12 months, with named owners on every finding, methodologically anchored in NIST SP 800-30 Rev. 1 (Joint Task Force, 2012). NIST SP 800-66 Rev. 2 supplies the HIPAA-specific application.

**Written, executed information-system-activity review procedures.** Defined log scope, retention duration, review cadence, reviewer identity, and review-record output. The output matters as much as the input — review records are the evidence OCR will request.

**A risk management plan that closes the loop between analysis and treatment.** Findings without owners and dates are not a risk management plan. A spreadsheet with finding, severity, treatment decision, owner, due date, and current status is.

These three artifacts also serve [the four anchor artifacts](/blog/single-artifact-multi-authority-evidence-engineering) framework: the risk analysis depends on the asset register and data-flow inventory, and the risk management plan plugs into the broader continuous compliance capability.

---

## What the 264% Statistic Means

OCR's reported 264% increase in large ransomware-related breaches since 2018 is the most useful board-level statistic in healthcare cybersecurity right now. It is the kind of number that turns risk-analysis funding decisions in 30 minutes.

Two cautions on how to use it:

- It is OCR's own enforcement-trend statistic, not a clinical-outcome statistic. Cite it for "what OCR is seeing," not for "what is happening to patients."
- It comes from the press release accompanying the Cascade Eye settlement; for clinical impact framing, pair it with peer-reviewed work like the JMIR systematic media literature review on ransomware impacts (Avery et al., 2025) which is methodologically careful about what it does and does not measure.

The combined picture for board reporting: OCR enforcement has accelerated, the deficiencies are predictable, and the remediation is well-understood.

---

## What to Track

Three signals will shape the Risk Analysis Initiative through 2027:

- Additional OCR ransomware settlements. The Bryan County Ambulance Authority $90,000 settlement on October 31, 2024 is the most recent companion case at the time of writing.
- The HIPAA Security Rule final rule and any explicit alignment between Initiative findings and final-rule safeguards.
- Whether OCR expands the Initiative to non-ransomware Security Rule deficiencies, particularly around vendor management and cloud configuration.

The Cascade Eye case is the cleanest current view of what OCR is enforcing today. Programs that respond to it now will not be the next case.

---

## Sources

- HHS Office for Civil Rights. (2024, September 26). *$250,000 Cascade Eye and Skin Centers ransomware settlement* [press release].
- 45 CFR § 164.308(a)(1)(ii)(A) and (D).
- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898.
- Marron, J. (2024). *NIST SP 800-66 Rev. 2*.
- Joint Task Force. (2012). *NIST SP 800-30 Rev. 1*.
- Avery et al. (2025). *Journal of Medical Internet Research, 27*, e59231.
