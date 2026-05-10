---
title: "HICP and the Recognized Security Practices Safe Harbor: The OCR Enforcement Mitigation Most Programs Miss"
description: "A 2021 amendment to HITECH lets OCR consider 12 months of recognized security practices when assessing fines. HHS named HICP as one of those recognized practices. Most healthcare programs do not use it."
publishDate: 2026-05-16
author: "Justin T. Begarek"
lane: practical
topics:
  - HIPAA
  - Healthcare
  - Compliance
  - Risk Management
  - Ransomware
featured: false
draft: false
citations: false
diagrams: false
---

In January 2021, Congress passed Public Law 116-321 (HR 7898), an amendment to the HITECH Act. The amendment instructs HHS to consider whether a regulated entity had, for not less than the previous 12 months, "recognized security practices" in place when assessing HIPAA Security Rule fines, audits, and remedies.

That language matters. It is one of the few statutory mechanisms in U.S. healthcare cybersecurity that explicitly rewards investment ahead of an incident with reduced enforcement exposure after one.

HHS named the Health Industry Cybersecurity Practices (HICP), jointly developed under Section 405(d) of the Cybersecurity Act of 2015, as one of the categories of recognized security practices. The HICP 2023 Edition is the current healthcare-specific operating reference. It is also one of the most underused compliance assets in healthcare cybersecurity, in part because the safe-harbor mechanism is widely misunderstood.

This post explains what the safe harbor actually does, how HICP qualifies, what 12-month adoption looks like in evidence, and how this pairs with current OCR enforcement under the Risk Analysis Initiative.

---

## What Public Law 116-321 Actually Says

The statute does not eliminate fines. It does not create an absolute defense. It does direct HHS to consider, when investigating Security Rule deficiencies, whether the regulated entity had recognized security practices in place for at least the prior 12 months. In practice, this means a documented multi-year HICP adoption can:

- Reduce the dollar amount of a settlement or civil monetary penalty.
- Shorten or soften a corrective action plan.
- Influence OCR's selection of regulated entities for audit.
- Inform OCR's interpretation of "willful neglect" and other culpability findings.

The 12-month threshold is the critical operating detail. A program that stood up HICP-aligned controls last week does not yet qualify. A program with 12+ months of dated, documented HICP adoption does.

The mechanism is sometimes described as a "safe harbor." That phrase is convenient but slightly misleading. The statute creates a mitigating consideration, not an immunity. Programs that treat it as full immunity will be disappointed; programs that treat it as the meaningful enforcement-cost reduction that it is will benefit substantially.

---

## What Counts as Recognized Security Practices

HHS has identified several categories that qualify. The most operationally useful for healthcare are:

- **Section 405(d) Health Industry Cybersecurity Practices (HICP).** The healthcare-specific cybersecurity practices document, with technical volumes for small organizations (TV1) and medium-large organizations (TV2). Current edition: 2023.
- **NIST Cybersecurity Framework**. Now CSF 2.0 (NIST, 2024). Cross-sector voluntary framework with healthcare-relevant profiles.
- **Other equivalent programs developed under federal authority** — a deliberately flexible category that HHS can interpret.

For most healthcare organizations, HICP is the more operationally useful anchor because it is healthcare-specific, organized around the five top sector threats (social engineering, ransomware, equipment loss, insider threats, attacks on connected medical devices), and provides ten cybersecurity practices with sub-practices that scale by organization size.

A program that has adopted HICP for 12+ months has documented, healthcare-specific evidence of the kind OCR is most likely to credit during an investigation.

---

## What 12-Month Adoption Looks Like in Evidence

The 12-month threshold is enforced by evidence, not assertion. A defensible record includes:

**Dated policy and procedure documents** that explicitly reference HICP practices and sub-practices. The reference matters; OCR cannot infer HICP alignment from generic security policies.

**Implementation records that show practices in operation.** Logging configurations, MFA enrollment data, vulnerability scan reports, training completion records, vendor questionnaires, and incident response exercises, all dated and tied to specific HICP practices.

**Continuous monitoring evidence.** HICP adoption is not a one-time check. Practices must continue to operate. NIST SP 800-137 (Dempsey et al., 2011) supplies the federal continuous-monitoring frame; the same artifacts demonstrate ongoing HICP adoption.

**A written HICP adoption record.** A standing document that records which HICP practices the organization has adopted, when each was implemented, who owns it, what evidence supports it, and the most recent review date. This document is the single most useful artifact during an OCR inquiry.

The 12-month clock is measured at the start of the OCR investigation. Programs that begin the dated record now have a defensible 12-month posture by mid-2027. Programs that wait until OCR opens an inquiry will have an unfortunate posture indeed.

---

## Why This Matters Right Now

OCR's Risk Analysis Initiative has produced multiple ransomware-related Security Rule settlements in 2024 and 2025. The Cascade Eye and Skin Centers settlement on September 26, 2024 was $250,000 with a two-year corrective action plan. The Bryan County Ambulance Authority settlement on October 31, 2024 was $90,000.

Both cases turned on risk-analysis deficiencies and information-system-activity monitoring deficiencies. Both are the kind of finding HICP adoption directly addresses. HICP Practice 1 (Email Protection Systems), Practice 3 (Access Management), Practice 5 (IT Asset Management), Practice 7 (Vulnerability Management), and Practice 8 (Security Operations Center and Incident Response) all map to the deficiencies OCR is currently citing.

A regulated entity that had 12+ months of dated HICP adoption when those investigations opened would have entered with a meaningfully different enforcement profile. The dollar amounts in those settlements are not enormous in absolute terms, but the corrective action plans are operationally expensive, and the public framing has competitive consequences. Both are softened, in OCR's discretion, by recognized security practices adoption.

For the Risk Analysis Initiative framing, see [OCR's Risk Analysis Initiative and the Cascade Eye Settlement](/blog/ocr-risk-analysis-initiative-cascade-eye).

---

## Why Programs Miss This

Three reasons most healthcare programs do not currently leverage the safe harbor.

**HICP is not a regulation.** It is voluntary practice. Programs scoped to "what is required" miss it. Programs scoped to "what reduces enforcement exposure" do not.

**The 12-month threshold requires forward planning.** A control adopted today does not produce safe-harbor evidence until 12 months from now. Programs that respond to incidents reactively cannot retroactively claim the benefit.

**The evidence is mostly already produced.** Many healthcare cybersecurity programs already implement most HICP practices through HIPAA, HHS HPH CPGs, CIS Controls v8, or NIST CSF alignment. The gap is documentation, not control implementation. The HICP adoption record is largely a re-tagging exercise on existing artifacts, not new work.

The combination — voluntary status, 12-month lead time, and largely pre-existing evidence — produces a high-leverage compliance investment that programs frequently overlook because nothing forces them to.

---

## How HICP Pairs With HHS HPH CPGs and the HIPAA NPRM

HICP is one of three healthcare-specific practice references that increasingly converge.

The HHS Healthcare and Public Health Cybersecurity Performance Goals (HPH CPGs) supply prioritized, healthcare-specific goals organized into Essential and Enhanced tiers (HHS, 2024). HICP supplies the practice and sub-practice catalog beneath those goals. The HIPAA Security Rule NPRM (HHS, 2025), if finalized as proposed, would codify many of the same safeguards.

A program aligned to HICP TV2 practices is materially aligned with HPH CPGs Essential and Enhanced tiers and with most of the HIPAA NPRM proposed safeguards. The same evidence body serves all three audiences.

For the broader artifact-engineering framing, see [single-artifact, multi-authority evidence engineering](/blog/single-artifact-multi-authority-evidence-engineering).

---

## What to Build, Specifically

Three steps capture most of the safe-harbor value at low operational cost.

**Stand up an HICP adoption record now.** A simple table with HICP practice number, sub-practice, current implementation status, owner, evidence pointer, and date of last review. Even if existing controls already cover many practices, the explicit reference to HICP is what unlocks the safe-harbor consideration.

**Choose TV1 or TV2 by organization size.** Small organizations (e.g., independent practices, small clinics) work to TV1. Medium and large organizations work to TV2. Mixed organizations (a health system with a small affiliated clinic network) may run both.

**Add the HICP adoption record to board reporting.** A quarterly board update that includes HICP coverage and the 12-month adoption duration converts a compliance artifact into a governance artifact and supports the enterprise risk integration that NIST CSF 2.0 Govern function expects (NIST, 2024).

The investment in an HICP adoption record is small. The reduction in enforcement-cost expected value, when paired with active controls, is substantial. The asymmetry is rarely this favorable in healthcare compliance.

---

## What to Track

Two signals matter for the safe harbor through 2027:

- HHS implementing language and any updates to the recognized-security-practices categories.
- OCR enforcement actions where the safe harbor is explicitly considered. As of mid-2026, public settlements have not consistently announced safe-harbor consideration in their press materials, but it is reasonable to assume OCR is applying the framework internally.

The HICP 2023 Edition is the current operational reference. A 2026 or later update is plausible; the practice-and-sub-practice structure is stable enough that updates will be incremental rather than disruptive.

---

## Sources

- Public Law No. 116-321. (2021). *HR 7898* (signed January 5, 2021). [congress.gov](https://www.congress.gov/bill/116th-congress/house-bill/7898)
- HHS 405(d) Program. (2023). *Health Industry Cybersecurity Practices (HICP)*. [405d.hhs.gov](https://405d.hhs.gov/Documents/HICP-Main-508.pdf)
- HHS. (2024). *Healthcare and Public Health Cybersecurity Performance Goals*.
- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898.
- NIST. (2024). *Cybersecurity Framework 2.0* (CSWP 29).
- Dempsey et al. (2011). *NIST SP 800-137*.
- HHS Office for Civil Rights. (2024). *Cascade Eye and Skin Centers and Bryan County Ambulance Authority resolution agreements*.
