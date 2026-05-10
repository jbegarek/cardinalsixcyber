---
title: "Cross-Border Health Data Flows: When HIPAA Is Not Enough Because the Data Crossed a Border"
description: "EU GDPR, UK GDPR, China's PIPL, and the EU AI Act all have extraterritorial reach. A U.S. healthcare vendor with international users or vendors is in three regulatory regimes simultaneously."
publishDate: 2026-05-10
author: "Justin T. Begarek"
lane: practical
topics:
  - Healthcare
  - Privacy
  - HIPAA
  - GDPR
  - Compliance
featured: false
draft: false
citations: false
diagrams: false
---

A U.S. healthcare vendor in 2026 often assumes that if it complies with HIPAA, it has solved the health-data privacy problem. That assumption holds only as long as data, users, vendors, and AI models stay inside the United States. The moment any of them cross a border — an EU resident uses the platform, an EU vendor processes data, an AI model is trained in the EU, telehealth is offered to a UK consumer, a Chinese subsidiary touches the data — the regulatory environment expands.

This post walks through the cross-border regimes that apply to U.S. healthcare vendors, why they matter even for organizations that consider themselves domestic, and what a defensible cross-border data governance posture looks like. Xia et al. (2024), a peer-reviewed paper in *Risk Management and Healthcare Policy*, anchors much of the academic framing; the regulatory primary sources anchor the operational specifics.

---

## Why HIPAA Does Not Cover Cross-Border Flows

HIPAA is a U.S. federal statute. Its substantive obligations apply to covered entities and business associates regardless of where they operate, but its scope is defined by the data and the entity, not by the data subject's location. A U.S. covered entity that holds PHI for an EU resident must still comply with HIPAA. But HIPAA does not regulate that resident's data the way the EU regulates its own residents' personal data, and HIPAA does not address most of the cross-border concerns that EU and UK regulators care about.

The result is overlap without harmonization. A U.S. healthcare vendor serving EU residents must comply with HIPAA AND with EU GDPR AND, where AI is involved, with the EU AI Act. The substantive obligations differ in important ways: GDPR's lawful-basis requirements, data subject rights, cross-border transfer restrictions, and supervisory-authority enforcement do not have direct HIPAA equivalents.

Xia et al. (2024) frame this as a "paradigm transformation" in global health data regulation, with the EU's personal-data-protection model, the U.S.'s free-flow-for-trade model, and China's national-security model in fundamental tension. For practitioners, the academic framing matters less than the operational reality: a single dataset may be subject to three regimes simultaneously.

---

## EU GDPR Extraterritorial Reach

Article 3(2) of the GDPR extends its application to controllers and processors not established in the EU when they offer goods or services to data subjects in the EU or monitor their behavior. For a U.S. healthcare vendor, this typically captures:

- Telehealth services offered to EU residents, including travelers and expatriates.
- Patient-engagement platforms with EU-resident users.
- Wellness, fitness, and digital-health apps available in EU markets.
- Clinical-trial platforms with EU participants.
- Healthcare AI models trained on EU data or marketed to EU healthcare entities.

The substantive GDPR obligations include lawful basis for processing (Article 6), special-category protections for health data (Article 9), data subject rights (Articles 15-22), data protection by design and default (Article 25), records of processing (Article 30), data protection impact assessments (Article 35), and cross-border transfer restrictions (Articles 44-49). For U.S. recipients, the most operationally consequential restrictions are on transfers from the EU to the U.S. without an adequacy decision or appropriate safeguards (currently Standard Contractual Clauses or Binding Corporate Rules supplemented by transfer impact assessments).

UK GDPR retains substantively similar obligations under the post-Brexit UK regulatory framework, with separate enforcement by the Information Commissioner's Office.

---

## EU AI Act Extraterritorial Reach

The EU AI Act (Regulation (EU) 2024/1689) applies to providers placing AI systems on the EU market or putting them into service in the EU, and to deployers using AI systems in the EU. It also applies, under specified conditions, to providers and deployers established outside the EU when the output of the AI system is used in the EU. For healthcare AI specifically, this captures:

- AI-enabled medical devices CE-marked or placed on the EU market.
- Clinical decision support tools used in EU healthcare delivery.
- Healthcare AI models whose output is used to make decisions about EU residents.
- General-purpose AI models distributed to EU healthcare customers.

The Act applies in phases under Article 113: prohibited practices from February 2, 2025, general-purpose AI model rules and most enforcement provisions from August 2, 2026, and Article 6(1) high-risk system obligations from August 2, 2027. Most clinical and decision-influencing healthcare AI falls into the high-risk category.

For a U.S. healthcare AI vendor, Article 113's August 2, 2027 high-risk applicability is the operational planning horizon. Conformity assessment, technical documentation, post-market monitoring, and serious-incident reporting must be in place before that date for any system intended for the EU market.

See [The Cross-Jurisdiction AI Compliance Stack for Healthcare Vendors](/blog/cross-jurisdiction-ai-compliance-healthcare-stack) for the broader AI-specific framing.

---

## China's PIPL and Other Non-EU Regimes

China's Personal Information Protection Law (PIPL), effective November 1, 2021, regulates the processing of personal information of individuals located in the People's Republic of China. It includes cross-border transfer restrictions, sensitive-personal-information protections that overlap with health data, security assessments for certain data exports, and consent and notification requirements that are stricter than HIPAA's in several dimensions.

For U.S. healthcare vendors with Chinese operations, Chinese subsidiaries, Chinese vendor relationships, or Chinese-resident users, PIPL is operationally relevant. Many U.S. healthcare AI models trained on data sourced through Chinese partners face sensitive-personal-information transfer questions that HIPAA does not address.

Beyond the EU, UK, and China, regimes worth tracking include Canada's PIPEDA, Brazil's LGPD, India's DPDP Act, and the proliferating set of bilateral and multilateral data-flow agreements that create regime-specific obligations for healthcare data.

---

## The Operational Problem

The hardest part of cross-border compliance is not understanding any single regime. It is maintaining accurate awareness of which regimes apply to which data flows in real time. A U.S. healthcare vendor's compliance posture is rarely uniform across its data set:

- The EHR data of U.S. patients is HIPAA-covered.
- The same vendor's patient-engagement platform may have EU-resident users whose data is GDPR-covered.
- The vendor's clinical AI model may have been trained on data sourced from a Brazilian research partner, putting LGPD into play for the training data lineage.
- The vendor's marketing analytics may include Washington State residents, putting MHMD into play for inferred consumer health data.

Each data flow lives in its own regulatory weather. A program that does not maintain a current data-flow inventory cannot answer "which laws apply to this dataset" in less than a day, which is the kind of answer that procurement and breach-response timelines now demand in hours.

---

## What to Build

Three artifacts handle most of the cross-border compliance posture.

**A unified data-flow inventory** tagged with regulatory regime per flow. This is anchor artifact #3 in the [single-artifact, multi-authority evidence engineering](/blog/single-artifact-multi-authority-evidence-engineering) framing. Each flow records source, destination, data subjects' jurisdictions, applicable regimes (HIPAA, GDPR, UK GDPR, PIPL, MHMD, FTC HBNR, etc.), lawful basis, transfer mechanism, retention, and incident-notification regime.

**Cross-border transfer mechanisms.** For EU-to-U.S. transfers, current practice is Standard Contractual Clauses with transfer impact assessments, with attention to evolving EU adequacy decisions and the EU-U.S. Data Privacy Framework. For other regimes, transfer mechanisms vary; the inventory should record which applies to each flow.

**A multi-regime breach notification decision tree.** When an incident occurs, the team must answer in hours: what regimes require notification, what content, to what authority, on what timeline. HIPAA breach notification, EU GDPR Article 33/34 notifications, UK GDPR notifications, PIPL notifications, state breach laws, FTC HBNR, and CIRCIA (when finalized) can all apply to a single incident. The decision tree handles this cascade once, not from scratch under pressure.

The [CIRCIA reporting](/blog/circia-72-hour-reporting-healthcare) decision-tree framing applies here too, extended to cross-border regimes.

---

## What This Means for AI Specifically

Cross-border AI compliance is the most operationally complex layer in healthcare today. A single AI use case may be subject to:

- HIPAA (because it processes ePHI).
- NIST AI RMF (because procurement asks).
- FDA PCCP guidance (if it is an AI-enabled device).
- ONC HTI-1 (if it is in certified health IT).
- HIPAA Security Rule NPRM (when finalized).
- EU AI Act high-risk obligations (if it is offered or its output is used in the EU).
- EU GDPR (if it processes EU resident data).
- Colorado AI Act (if it is used to make consequential decisions about Colorado residents).
- China PIPL (if training data was sourced from Chinese operations).

The unified AI use-case dossier described in the cross-jurisdiction AI compliance post handles this. The dossier records data lineage, jurisdictional scope, and applicable regimes alongside the AI-specific fields, so one record satisfies the AI compliance authorities and the cross-border data compliance authorities simultaneously.

---

## What to Track

Three signals matter for cross-border health data compliance through 2027:

- EU adequacy decisions affecting U.S. transfers and any successor framework to the EU-U.S. DPF if challenged.
- EU AI Act high-risk implementation guidance and August 2, 2027 applicability.
- Continued state-level expansion of consumer-health-data laws (Washington MHMD model, Connecticut, Nevada, California) which functionally create another layer of data-residency complexity inside the U.S.

Cross-border compliance is not a niche concern for niche vendors. It is increasingly a default condition for U.S. healthcare vendors that operate any cloud platform, AI model, or telehealth service with international reach.

---

## Sources

- Xia, L., Cao, Z., & Zhao, Y. (2024). Paradigm transformation of global health data regulation. *Risk Management and Healthcare Policy, 17*, 3115-3132.
- European Parliament and Council. (2016). *General Data Protection Regulation* (Regulation (EU) 2016/679).
- European Parliament and Council. (2024). *Regulation (EU) 2024/1689 (AI Act)*, art. 113.
- Standing Committee of the National People's Congress. (2021). *Personal Information Protection Law of the People's Republic of China*.
- HHS. (2021). *Summary of the HIPAA Security Rule*.
- Federal Trade Commission. (2024). *Health Breach Notification Rule Final Amendments*. 89 Fed. Reg. 47028.
- Washington State Legislature. (2023). *My Health My Data Act* (Ch. 19.373 RCW).
