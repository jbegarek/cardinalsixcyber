---
title: "Washington's My Health My Data Act and the Gap HIPAA Does Not Cover"
description: "HIPAA does not cover wellness apps, marketing analytics, or most consumer health data. Washington's MHMD Act does. With a private right of action."
publishDate: 2026-05-23
author: "Justin T. Begarek"
lane: practical
topics:
  - Healthcare
  - Privacy
  - HIPAA
  - Compliance
  - State Law
featured: false
draft: false
citations: false
diagrams: false
---

A common misconception in healthcare cybersecurity is that HIPAA covers all "health data." It does not. HIPAA covers protected health information held by covered entities and business associates. The vast and growing category of consumer health data — wellness apps, fitness trackers, mental-wellness platforms, telehealth intake forms, marketing analytics, lab home-testing kits, ovulation trackers, and consumer-generated health content — often falls entirely outside HIPAA.

Washington's My Health My Data Act (RCW 19.373), signed by Governor Inslee on April 27, 2023 and effective for regulated entities on March 31, 2024, was the first U.S. state law to comprehensively regulate consumer health data outside HIPAA. The Act covers any non-HIPAA health-related data inferred or collected about Washington consumers, imposes consent and transparency obligations, and carries a private right of action under the Washington Consumer Protection Act.

For healthcare-adjacent businesses, the MHMD Act has become operationally consequential because it answers questions HIPAA does not, attaches teeth HIPAA does not (litigation risk in addition to OCR enforcement), and applies to data flows that many compliance programs were not previously tracking.

This post explains what MHMD covers, why it matters even for HIPAA-regulated organizations, and how it interacts with the FTC Health Breach Notification Rule and other state privacy laws.

---

## What MHMD Covers

The MHMD Act regulates "consumer health data" defined more broadly than HIPAA's PHI. The statute reaches:

- Health condition or diagnosis information.
- Social, psychological, behavioral, and medical interventions.
- Health-related surgeries, procedures, medications, and treatments.
- Reproductive or sexual health information.
- Gender-affirming care information.
- Biometric data and genetic data.
- Precise location information that could reveal an attempt to acquire health services.
- Data identifying a consumer seeking healthcare services.
- Any data derived or inferred from any of the above.

Critically, the Act covers data inferred about a Washington consumer regardless of whether the consumer affirmatively provided it. A wellness app that infers pregnancy from purchase history is covered, even if the consumer never told the app she was pregnant.

The Act applies to any "regulated entity" that conducts business in Washington or produces products or services targeted to Washington consumers. The geographic scope is consumer-residency-based, not entity-headquarters-based. A Florida-based digital health vendor with Washington users is in scope.

---

## What MHMD Requires

Five categories of obligations apply:

**Consent.** Regulated entities must obtain consumer consent before collecting, using, or sharing consumer health data, with separate authorization required for sale of consumer health data. Consent must be specific and revocable.

**Transparency.** A consumer health data privacy policy must be prominently posted and must describe categories of data collected, sources, purposes, sharing, and consumer rights.

**Consumer rights.** Right to access, right to delete, right to withdraw consent. Regulated entities must build infrastructure to fulfill these requests within statutory timelines.

**Sales prohibition without authorization.** Unlawful sale of consumer health data carries elevated exposure under the Act and the underlying Washington Consumer Protection Act.

**Geofencing prohibition.** Regulated entities may not implement geofences around facilities that provide healthcare services for the purpose of identifying, tracking, or sending notifications to consumers regarding their consumer health data.

The private right of action under Washington CPA (RCW 19.86) is the operational difference from many state privacy laws. AG enforcement is one risk; individual consumer suits are another, and class-action exposure follows.

---

## Why HIPAA-Regulated Organizations Still Need to Care

A covered entity that thinks "we are HIPAA-covered, MHMD does not apply to us" is usually wrong on at least one data flow.

**Wellness and consumer-facing services.** A health system that operates a consumer wellness portal, a fitness program, a patient-engagement app, or a marketing newsletter typically collects data outside HIPAA's scope. The marketing analytics tied to a hospital's website that infer health interest from page views are consumer health data under MHMD even though the hospital is HIPAA-covered.

**Telehealth intake.** Pre-encounter intake forms collected before a HIPAA treatment relationship is established may be MHMD-covered consumer health data, not HIPAA PHI.

**Vendor analytics.** Marketing pixel data, conversion tracking, and ad-tech integrations on healthcare websites often produce consumer health data flows that HIPAA's covered-entity boundary does not capture. The FTC has separately enforced against this category under the Health Breach Notification Rule (Federal Trade Commission, 2024).

**Inferred data.** Even where HIPAA applies to the underlying clinical record, inferred data about Washington consumers held outside HIPAA-covered systems can be MHMD-covered.

The right operational test: does the data flow involve health information about a Washington consumer that is not held under HIPAA? If yes, MHMD likely applies.

---

## How MHMD Interacts With HIPAA, FTC HBNR, and Other State Laws

MHMD does not replace HIPAA. It overlays HIPAA at the boundary where HIPAA ends.

The cleanest framing: HIPAA covers PHI held by covered entities and business associates. FTC's Health Breach Notification Rule covers non-HIPAA-covered health apps, personal health record vendors, and PHR-related entities at the federal level (effective July 29, 2024). MHMD covers consumer health data about Washington residents at the state level, with a private right of action and broader inferred-data scope than FTC HBNR.

For incident notification specifically:

- A breach of HIPAA-covered PHI triggers HIPAA breach notification.
- A breach of non-HIPAA health-app data may trigger FTC HBNR.
- A breach of MHMD consumer health data about Washington residents triggers state breach notification under Washington law and may trigger private litigation under WA CPA.

Many incidents trigger more than one regime simultaneously. The [CIRCIA reporting](/blog/circia-72-hour-reporting-healthcare) decision-tree framing applies here too: the reporting analysis happens once, against all applicable regimes, in a structured way.

Other states are following Washington. Nevada, Connecticut, and California have or are developing analogous protections. The state-by-state tracker is becoming a required artifact for healthcare-adjacent businesses.

---

## What to Build

Three artifacts handle most of MHMD's operational requirements.

**A data classification that identifies consumer health data flows.** The classification needs to distinguish HIPAA PHI, FTC HBNR consumer health data, MHMD consumer health data (Washington residents), and analogous categories under other state laws. The single data-flow inventory described in [single-artifact, multi-authority evidence engineering](/blog/single-artifact-multi-authority-evidence-engineering) is the natural home.

**A consent infrastructure.** Consent capture, audit-able consent records, revocation mechanism, and proof-of-consent retrievable per consumer. Many existing healthcare consent systems were not built for MHMD's specificity-and-revocability standard.

**A consumer-rights fulfillment process.** Right-to-access and right-to-delete request intake, identity verification, fulfillment within statutory timelines, and audit logs of every fulfillment. This same infrastructure can serve CCPA, CPRA, and other state consumer-rights regimes with minor adaptation.

A geofencing prohibition compliance review is also a one-time exercise: any marketing or location-targeting feature that intersects healthcare facilities needs review against the prohibition.

---

## What to Track

Three signals matter for MHMD and consumer-health-data compliance generally:

- Washington AG enforcement actions and private litigation under MHMD. As of mid-2026, both have begun and the pattern is forming.
- New state consumer-health-data laws in Nevada, Connecticut, and California. The state tracker is now part of healthcare compliance intelligence, not an optional add.
- Federal preemption arguments and any federal consumer health privacy legislation. There is no comprehensive federal consumer-health-data statute today, which is why state laws like MHMD are filling the gap.

For healthcare-adjacent businesses, MHMD is not the most consequential single law in the compliance stack. It is, however, the most consequential current example of the principle that "HIPAA covers it" is no longer a complete answer to the consumer-health-data question.

---

## Sources

- Washington State Legislature. (2023). *My Health My Data Act* (Ch. 19.373 RCW).
- FTC. (2024). *Health Breach Notification Rule Final Amendments*. 89 Fed. Reg. 47028.
- HHS. (2021). *Summary of the HIPAA Security Rule*.
- Sebastian, G. (2021). Privacy directive compliance relating to increased adoption of emerging technologies. *ISSA Journal, 19*(12), 15-18.
- Xia, L., Cao, Z., & Zhao, Y. (2024). Paradigm transformation of global health data regulation. *Risk Management and Healthcare Policy, 17*, 3115-3132.
