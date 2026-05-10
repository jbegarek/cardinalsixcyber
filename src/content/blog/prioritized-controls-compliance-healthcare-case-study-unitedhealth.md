---
title: "Prioritized Controls for Compliance: A Healthcare Case Study of UnitedHealth Group"
description: "A full research paper applying NIST SP 800-66r2 and SP 800-53r5 to healthcare compliance after Change Healthcare."
publishDate: 2026-05-04
author: "Justin T. Begarek"
lane: research
topics:
  - HIPAA
  - NIST
  - Healthcare
  - Risk Management
  - Supply Chain
featured: false
draft: false
citations: true
diagrams: false
---

*This is the full research paper adapted from TIM-8720 coursework. Practitioner summaries derived from it include [Why HIPAA Compliance Is Not Enough](/blog/hipaa-nist-control-roadmap-change-healthcare), [NIST vs HITRUST, ISO 27001, COBIT, and CIS](/blog/nist-vs-hitrust-iso-cobit-cis-healthcare), [Change Healthcare and Business Associate Risk](/blog/change-healthcare-supply-chain-risk-business-associates), and [Healthcare Ransomware Control Priorities](/blog/healthcare-ransomware-control-priorities-nist-800-53).*
## Introduction

UnitedHealth Group is the largest publicly traded healthcare company in the United States, with nearly 400,000 employees and 2024 revenue of approximately $400.3 billion (UnitedHealth Group, 2025). Operating divisions include UnitedHealthcare, Optum, and the recently acquired Change Healthcare. On February 21, 2024, ransomware actors compromised Change Healthcare's systems, disrupted United States medical-payment processing, and exposed protected health information for an estimated 100 million individuals at first disclosure, later revised to approximately 192.7 million as of July 31, 2025 (HHS OCR, 2025; Jiang et al., 2025). By record count, the incident is the largest healthcare cybersecurity event in history and the principal case study from 2024 to 2026 for HIPAA business-associate liability and supply-chain risk.

For UnitedHealth Group, HIPAA compliance requires a control catalog deep enough to cover healthcare, public-company, payment, banking, privacy, and international obligations at the same time. A research problem drives the analysis because statutory minimum compliance with the HIPAA Security Rule is necessary but not sufficient for an organization of this scale. The research problem is not whether to comply, but which control catalog best operationalizes compliance depth above the regulatory floor. NIST Special Publication 800-66 Revision 2 (Marron, 2024), operationalized through NIST Special Publication 800-53 Revision 5 (Joint Task Force, 2020a), supplies that depth. Appendix Table A1 maps twenty unified compliance needs to the recommended stack, and Appendix Table A2 evaluates that stack against four widely cited alternatives.

## 1. Unified Compliance Needs

**Federal healthcare statutes.** Under 45 C.F.R. pt. 164, subpt. C, the HIPAA Security Rule imposes administrative, physical, and technical safeguard requirements on covered entities and business associates handling electronic protected health information (U.S. Department of Health and Human Services, Office for Civil Rights [HHS OCR], 2021). Companion provisions in 45 C.F.R. pt. 164, subpt. E govern protected health information through the HIPAA Privacy Rule. HITECH extends Security Rule liability to business associates and creates the Breach Notification Rule (111th Congress, 2009). The U.S. Department of Health and Human Services (HHS) issued a January 2025 Notice of Proposed Rulemaking that would convert addressable specifications to required and add new technical controls (HHS, 2025).

**Federal cybersecurity guidance.** UnitedHealth Group operates in the Healthcare and Public Health critical-infrastructure sector (Biden, 2024), where HHS sector-specific Cybersecurity Performance Goals and HHS 405(d) Health Industry Cybersecurity Practices shape control expectations (HHS, 2023a, 2023b). CISA-hosted FedVTE control-selection guidance ties federal risk categorization to FIPS 199, FIPS 200, and NIST SP 800-53 baselines (Carnegie Mellon University, 2019). HICP carries safe-harbor recognition under HITECH § 13412, mitigating HHS OCR penalty exposure for entities demonstrating twelve months of adoption.

**Healthcare-specific federal regulations.** The Office of the National Coordinator for Health Information Technology (ONC) information-blocking regulation at 45 C.F.R. pt. 171 prohibits practices that interfere with electronic health information exchange (ONC, 2024). Parallel requirements apply to UnitedHealthcare as a payer regulated by the Centers for Medicare & Medicaid Services (CMS) under the CMS Interoperability and Patient Access Final Rule (CMS, 2020). Non-HIPAA wellness applications Optum operates fall under the Federal Trade Commission (FTC) Health Breach Notification Rule (FTC, 2026).

**Public-company federal regulations.** Securities and Exchange Commission (SEC) registrant status subjects UnitedHealth Group to the SEC's 2023 Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure Final Rule, requiring Form 8-K Item 1.05 disclosure within four business days of any material cybersecurity incident and annual Form 10-K Item 1C disclosure (SEC, 2023). Sarbanes-Oxley §§ 302 and 404 require management certification of internal controls over financial reporting, including IT general controls supporting Change Healthcare (107th Congress, 2002).

**State and local law.** UnitedHealth Group operates in all fifty states. State-level obligations include the California Consumer Privacy Act, New York's SHIELD Act, Texas's Medical Records Privacy Act, and additional state privacy laws beyond HIPAA. Lively's (2022) International Association of Privacy Professionals (IAPP) tracker forms the baseline state-privacy source, and the April 2026 IAPP update identifies twenty-three current state privacy laws (IAPP, 2026). Local procurement, public-health reporting, and consumer-protection workflows map to IR-6 Incident Reporting and SA-9 External System Services. FTC Section 5 enforcement supplements state attorney general action where deceptive privacy promises or unfair data practices occur (FTC, n.d.).

**Industry standards and contractual obligations.** Optum and Change Healthcare payment-processing operations invoke PCI Data Security Standard v4.0.1 for cardholder data (PCI Security Standards Council, 2024). ISO/IEC 27000 encompasses international standards used by external auditors as a comparative framework (ISO 27001 Security, 2022). Examination guidance from the Federal Financial Institutions Examination Council (FFIEC) II.C.4 confirms the multi-source authority pattern, under which institutions may select among NIST 800 series, COBIT, ITIL, ISO/IEC 27000 series, and industry publications (FFIEC, 2016). The Federal Deposit Insurance Corporation (FDIC) RMS Manual offers a complementary internal-controls framework drawn from COSO that informs the audit-and-monitoring posture relevant to Optum Bank, where Gramm-Leach-Bliley Act safeguards also apply (FDIC, n.d.).

**International.** International operations expose UnitedHealth Group to the European Union General Data Protection Regulation for European Union resident data (European Parliament & Council of the European Union, 2016). Article 3(2) extends GDPR to non-EU controllers offering services to EU residents, capturing UnitedHealth Group's cross-border insurance and digital-health offerings. Compliance maps to the Personally Identifiable Information Processing and Transparency family added in NIST SP 800-53 Revision 5.

Together, these seven regimes produce a unified needs taxonomy organized around eight functional categories, including governance and risk management, identity and access management, asset and configuration management, vulnerability and patch management, audit logging and monitoring, incident response and breach notification, business-associate and supply-chain risk management, and data protection. Change Healthcare materializes risks across all eight. The taxonomy then drives the prioritization order in Appendix Table A1, where families with the strongest enforcement-evidence base appear first.

## 2. The Best Control Source

A single-source approach is preferable here to blending catalogs. For UnitedHealth Group, that source is NIST Special Publication 800-66 Revision 2 (Marron, 2024) operationalized through NIST Special Publication 800-53 Revision 5 (Joint Task Force, 2020a). Together, the two publications function as one coherent stack. SP 800-66r2 maps every HIPAA Security Rule standard and implementation specification to specific SP 800-53r5 controls, eliminating the independent-crosswalk burden that anchoring on any other catalog imposes.

FFIEC II.C.4 examination guidance authorizes more than one recognized framework, so the choice among catalogs deserves explicit comparison. Appendix Table A2 places the recommended NIST stack alongside ISO/IEC 27001:2022, HITRUST Common Security Framework version 11, COBIT 2019, and CIS Controls version 8 across HIPAA crosswalk directness, FISMA statutory authority, SEC Item 1C disclosure compatibility, license cost, sector-specific tailoring, and certification mechanism. Section 4 explains the decisive patterns the table reveals.

Six grounds defend the selection. First, FFIEC II.C.4 examination guidance authorizes multi-source framework selection while explicitly naming NIST publications as recognized control frameworks (FFIEC, 2016). Carnegie Mellon University's (2019) FedVTE module operationalized the FIPS 199 / FIPS 200 / SP 800-53 baseline-selection methodology that NIST SP 800-53r5 expects. Both sources converge on the NIST chain.

Second, NIST SP 800-66r2 carries FISMA statutory authority and explicitly maps to HIPAA Security Rule standards (Marron, 2024). No alternative catalog provides the same authoritative HIPAA-to-control-ID crosswalk. HITRUST Common Security Framework offers similar coverage but carries certification cost and licensing restrictions, as Appendix Table A2 documents.

Third, the SEC 2023 cybersecurity-disclosure rule is compatible with NIST-based framework adoption in Form 10-K Item 1C disclosures (SEC, 2023). In a preprint of a forthcoming *Computers & Security* study, Adams and Moore (2025) documented through analysis of 7,681 cyber-related statements across 314 Form 10-K filings that recognized-framework adoption establishes a basis for more standardized risk-management disclosures. UnitedHealth Group's existing NIST alignment therefore reduces the marginal effort needed to satisfy Item 1C narrative requirements.

Fourth, peer-reviewed empirical evidence shows that HIPAA-floor compliance leaves measurable enforcement risk untouched. A fourteen-year difference-in-differences study of HHS OCR breach data found no significant breach-rate reduction from the 2013 HIPAA Omnibus Rule (*P* = .50) (Subramanian et al., 2024). Reviewed 2024 to 2025 HHS OCR Resolution Agreements repeatedly cite Security Rule risk-analysis, risk-management, and activity-review failures, and all reviewed agreements call for risk-analysis or security-management remediation (HHS OCR, 2018-2025). NIST SP 800-53r5 delivers the implementation depth, at the level of specific control identifiers, that the Security Rule's general language leaves open.

Fifth, ransomware evidence makes the recommended families nonoptional for UnitedHealth Group. From 2010 to 2024, ransomware accounted for 39% of affected healthcare records, and since 2020 it affected more than half of patients annually, reaching 69% in 2024 (Jiang et al., 2025). Between 2016 and 2021, 374 ransomware attacks affected 41.99 million patients across U.S. healthcare organizations (Neprash et al., 2022), and adjacent facilities saw 15% emergency-department census increases after nearby hospitals were compromised (Dameff et al., 2023). NIST SP 800-53r5 elaborates the SR (Supply Chain Risk Management) and IR (Incident Response) families that the Change Healthcare vector demands.

Sixth, NIST publications are freely available and patent-unencumbered. ISO/IEC 27001:2022, a defensible alternative for organizations seeking external attestation, carries licensing costs that NIST SP 800-53r5 does not (ISO 27001 Security, 2022). FTC's enforcement record under Section 5 against companies failing to safeguard consumer data demonstrates that documentary evidence of recognized-framework adoption is material to enforcement defense (FTC, n.d.).

## 3. Selection Process and Prioritization Methodology

**Step 1. Categorize.** Under FIPS 199 and FIPS 200 (Carnegie Mellon University, 2019), UnitedHealth Group's electronic protected health information warrants High impact for confidentiality and integrity and Moderate-to-High impact for availability. Change Healthcare's 2024 disruption demonstrated that availability impact reaches catastrophic levels when payment processing fails across the United States healthcare delivery network.

**Step 2. Select baseline.** NIST SP 800-53B's High baseline (Joint Task Force, 2020b) constitutes the starting control set, augmented by the Privacy Baseline because UnitedHealth Group processes personally identifiable information beyond protected health information. The High baseline preselects approximately 370 controls under SP 800-53B that examiners and auditors recognize (Joint Task Force, 2020b). Privacy Baseline overlay then activates the PT family controls needed for the twenty-three-state environment described in Section 1.

**Step 3. Apply HIPAA crosswalk.** Under SP 800-66r2, each HIPAA standard at §§ 164.308, 164.310, 164.312, 164.314, and 164.316 maps to specific NIST SP 800-53r5 controls (Marron, 2024). Every regulatory need is anchored in a verifiable control identifier, satisfying the HHS OCR risk-analysis-and-risk-management requirement at § 164.308(a)(1)(ii)(A)-(B) (HHS OCR, 2021).

**Step 4. Prioritize.** This paper draws on the fuzzy Analytical Hierarchy Process logic developed by Tariq et al. (2020), which ranked priorities from pairwise judgment rather than uniform weighting. The qualitative principle applies here rather than the full numerical procedure, which would require an expert respondent panel beyond the scope of a single-organization case study. For UnitedHealth Group, priority emphasis falls on the SR family because of the Change Healthcare business-associate dimension, followed by IR, IA (Identification and Authentication), and AU (Audit and Accountability). A synthesis of 175 cyber-supply-chain risk-management studies confirms the SR-family priority (Afifi et al., 2026), and internal-controls auditing principles drawn from the FDIC's RMS Manual reinforce the audit-and-monitoring priority (FDIC, n.d.).

**Step 5. Augment.** HHS 405(d) HICP 2023 Edition offers healthcare-tailored implementation guidance for each Security Rule standard (HHS, 2023b). The 2025 HIPAA Security Rule Notice of Proposed Rulemaking calls for forward-looking augmentation because anticipated changes from addressable to required would tighten the implementation depth that any compliant program is expected to demonstrate (HHS, 2025).

**Step 6. Integrate empirical evidence.** Westland (2020) found empirically that SOX-404 IT general controls reporting carries information about subsequent breach risk, supporting depth above statutory minimum. Kabanov and Madnick (2021) identified nineteen distinct control failures in the 2017 Equifax breach across executive, organizational, operational, and external regulatory layers, producing the multi-layer pattern UnitedHealth Group should adopt. A sociotechnical framework integrating technology, humans, and processes complements the technical NIST control set (Ewoh et al., 2025). Lively (2022) anchored the state-privacy tracker, and IAPP's 2026 update maintains visibility into the twenty-three-state environment (IAPP, 2026).

## 4. Needs-to-Controls Mapping

Appendix Table A1 operationalizes the analysis by translating the twenty unified compliance needs from Section 1 into specific NIST SP 800-53 Revision 5 control identifiers, demonstrating that a single catalog satisfies the multi-jurisdictional compliance footprint without resort to a second source. The table is significant for three reasons. First, it shows the recommendation is implementable at the control-identifier level, anchoring each regulatory need in verifiable controls auditors and HHS OCR examiners trace through the SP 800-66 Revision 2 crosswalk (Marron, 2024; HHS OCR, 2021). Second, prioritization order encodes empirical evidence: rows addressing recurring HHS OCR risk-analysis findings appear first, rows addressing the Change Healthcare ransomware vector follow, and rows addressing SEC 2023 disclosure obligations close the table, mirroring the highest-consequence enforcement record. Third, several rows group related controls within a single family, demonstrating that the multi-jurisdictional footprint operates through consolidated families rather than dispersed catalogs.

Three patterns surface from Appendix Table A1 that justify the prioritization. RA, PM, IR, and SR families carry the highest priority because HHS OCR enforcement records and the Change Healthcare incident concentrate failures in risk analysis, supply-chain risk management, and incident response. AU supports both HIPAA § 164.312(b) audit controls and SEC Item 1C disclosure capability through a single control set, reducing duplicate investment for an organization carrying both healthcare and public-company obligations. PT, added in NIST SP 800-53 Revision 5, addresses the twenty-three-state privacy environment that earlier-revision catalogs could not have anchored.

Appendix Table A2 carries equal weight by demonstrating that the NIST recommendation is defensible against the four most serious alternatives. The table is significant because it forces comparison onto the dimensions that drive the choice for this organization rather than generic catalog properties: HIPAA crosswalk directness, FISMA statutory authority, SEC Item 1C disclosure compatibility, license cost, sector-specific tailoring, and certification mechanism. Selection of these dimensions reflects the regulatory environment of a publicly traded U.S. healthcare organization; a firm weighting global certifiability or third-party assurance more heavily might select differently. NIST is the only catalog that simultaneously satisfies the first four. The table also documents that ISO/IEC 27001 and HITRUST retain accredited-certification advantages, identifying when an organization should pair certification programs with NIST rather than substitute. Taken together, the comparison answers the central research problem by showing that no alternative single source matches the convergent regulatory authority NIST delivers.

## 5. Justification, Next Steps, and Implications

**Justification.** Selection rests on convergent authority. NIST publications carry FISMA statutory authority and OMB Circular A-130 weight, FFIEC's IT Examination Handbook authorizes NIST as a recognized control framework (FFIEC, 2016), and SEC's 2023 disclosure rule treats NIST adoption as compatible with Item 1C narrative disclosure (SEC, 2023). NIST SP 800-66r2 supplies the canonical HIPAA-to-NIST crosswalk no alternative catalog matches (Marron, 2024), and SP 800-53A Revision 5 supplies the assessment methodology auditors recognize (Joint Task Force, 2022). Enterprise Risk Management theory anchors integration into board-level governance through NIST IR 8286 (Stine et al., 2025), and HHS 405(d) guidance aligns with prioritized SP 800-53r5 families (HHS, 2023b).

Three structural problems sharpen the justification. A HIPAA-floor enforcement gap appears in Subramanian et al.'s (2024) *P* = .50 result and recurring HHS OCR remediation terms (HHS OCR, 2018-2025). Supply-chain liability fragmentation appears because HITECH extends business-associate liability, yet Change Healthcare showed how a vendor compromise can disrupt national workflows. A NIST-to-certification gap remains because SP 800-53r5 lacks a central certification body, so where HITRUST validation is contractually mandated, UnitedHealth Group should add it alongside NIST. Shahzadi et al.'s (2025) systematic review of 60 healthcare-ransomware studies documented that HIPAA's general-rules language has not produced ransomware-specific control prescriptions, leaving covered entities to derive ransomware controls from external frameworks.

**Next steps.** Implementation proceeds through five phases. Phase 1, covering months 1 to 3, completes risk analysis under NIST SP 800-30 Revision 1 (Joint Task Force Transformation Initiative, 2012). Highest-priority controls come online in months 3 to 9, including risk management (PM-9, PM-28), multifactor authentication (IA-2(1)), audit-log generation (AU-12), and incident-response capability (IR-1, IR-4, IR-8). Months 6 to 18 cover supply-chain risk management. Months 12 to 24 establish continuous monitoring (CA-7) and SEC Item 1C disclosure capability. Phase 5 sustains the program through annual risk-analysis updates, biennial assessments under NIST SP 800-53A Revision 5 (Joint Task Force, 2022), and integration through the NIST IR 8286 series (Stine et al., 2025).

**Residual risk.** Even a well-designed control program cannot eliminate breach risk. Subramanian et al.'s (2024) *P* = .50 finding confirms that statutory compliance has not historically translated into proportional breach-rate reduction. UnitedHealth Group must expect future incidents and design the control program to limit incident impact through segmentation, recovery-time-objective compression, and offline-backup verification (Barker et al., 2022).

**Policy implications.** HHS's January 2025 HIPAA Security Rule Notice of Proposed Rulemaking signals a federal shift from addressable to required implementation specifications (HHS, 2025). The NIST-anchored control program will satisfy the proposed requirements with limited modification because SP 800-53 Revision 5 already adds depth beyond the current Security Rule baseline. Change Healthcare has accelerated congressional and HHS attention to business-associate liability and may produce additional regulatory action. Recommended control-source adoption positions UnitedHealth Group ahead of regulatory developments. Compliance operates as an external influence on enterprise risk evaluation, with mitigation expressed through controls, and an organization of UnitedHealth Group's scale needs depth that exceeds the regulatory floor.

## References

Adams, M., & Moore, T. (2025). *How informative are cybersecurity risk disclosures? Empirical analysis of firms targeted by ransomware* [Preprint of forthcoming *Computers & Security* article]. University of Tulsa. https://tylermoore.utulsa.edu/cose25.pdf

Afifi, Y. A. M., Hashem, A. E. A. E., & Younis, R. A. A. (2026). Cyber supply chain risk management: A systematic review. *Sustainability*, *18*(3), 1151. https://doi.org/10.3390/su18031151

Barker, W. C., Fisher, W., Scarfone, K., & Souppaya, M. (2022). *Ransomware risk management: A cybersecurity framework profile* (NIST Internal Report 8374). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.IR.8374

Biden, J. R. (2024, April 30). *National Security Memorandum on Critical Infrastructure Security and Resilience* (NSM-22). White House. https://bidenwhitehouse.archives.gov/briefing-room/presidential-actions/2024/04/30/national-security-memorandum-on-critical-infrastructure-security-and-resilience/

Carnegie Mellon University. (2019). *Selecting security controls* [Training handout]. Federal Virtual Training Environment, Fundamentals of Cyber Risk Management training (Day 3, Session 1, Topic 1). U.S. Cybersecurity and Infrastructure Security Agency. https://web.archive.org/web/20240221050104/https://fedvte.usalearning.gov/publiccourses/FCRM/course/videos/pdf/FCRM_D03_S01_T01_STEP.pdf

Center for Internet Security. (2021). *CIS Critical Security Controls Version 8*. https://www.cisecurity.org/controls/v8

Centers for Medicare & Medicaid Services. (2020). *Medicare and Medicaid programs; Patient Protection and Affordable Care Act; Interoperability and Patient Access for Medicare Advantage Organization and Medicaid Managed Care Plans, State Medicaid Agencies, CHIP Agencies and CHIP Managed Care Entities, Issuers of Qualified Health Plans on the Federally-facilitated Exchanges, and Health Care Providers* (Final Rule, CMS-9115-F). *Federal Register*, *85*(85), 25510–25640. https://www.cms.gov/files/document/cms-9115-f.pdf

Dameff, C., Tully, J., Chan, T. C., Castillo, E. M., Savage, S., Maysent, P., Hemmen, T. M., Clay, B. J., & Longhurst, C. A. (2023). Ransomware attack associated with disruptions at adjacent emergency departments in the US. *JAMA Network Open*, *6*(5), e2312270. https://doi.org/10.1001/jamanetworkopen.2023.12270

European Parliament & Council of the European Union. (2016). *Regulation (EU) 2016/679 of 27 April 2016 (General Data Protection Regulation)*. *Official Journal of the European Union*, L 119/1. https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

Ewoh, P., Vartiainen, T., & Mantere, T. (2025). Sociotechnical cybersecurity framework for securing health care from vulnerabilities and cyberattacks: Scoping review. *Journal of Medical Internet Research*, *27*, e75584. https://doi.org/10.2196/75584

Federal Deposit Insurance Corporation. (n.d.). Internal routine and controls. In *RMS manual of examination policies* (Section 4.2). https://www.fdic.gov/regulations/safety/manual/section4-2.pdf

Federal Financial Institutions Examination Council. (2016, September). II.C.4 Control implementation. In *FFIEC information technology examination handbook: Information security booklet*. https://ithandbook.ffiec.gov/

Federal Trade Commission. (n.d.). *Privacy and security enforcement*. https://www.ftc.gov/news-events/topics/protecting-consumer-privacy-security/privacy-security-enforcement

Federal Trade Commission. (2026). *Health Breach Notification Rule* (16 C.F.R. pt. 318). Electronic Code of Federal Regulations. https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-318

HITRUST Alliance. (2025). *HITRUST CSF version 11.7.0: Common Security Framework* [Public release package]. https://hitrustalliance.net/product-tool/hitrust-csf/ (The public release package reviewed locally is not the full CSF package, and controls cited here are at the framework-level summary.)

Information Systems Audit and Control Association. (2018). *COBIT 2019 framework: Introduction and methodology* [Overview]. ISACA. https://www.isaca.org/resources/cobit

International Association of Privacy Professionals. (2026, April 20). *U.S. state privacy legislation tracker*. https://iapp.org/resources/article/us-state-privacy-legislation-tracker/

ISO 27001 Security. (2022). *ISO27k information security*. IsecT Limited. https://www.iso27001security.com/

Jiang, J. X., Ross, J. S., & Bai, G. (2025). Ransomware attacks and data breaches in US health care systems. *JAMA Network Open*, *8*(5), e2510180. https://doi.org/10.1001/jamanetworkopen.2025.10180

Joint Task Force. (2020a). *Security and privacy controls for information systems and organizations* (NIST Special Publication 800-53, Revision 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5

Joint Task Force. (2020b). *Control baselines for information systems and organizations* (NIST Special Publication 800-53B). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53B

Joint Task Force. (2022). *Assessing security and privacy controls in information systems and organizations* (NIST Special Publication 800-53A, Revision 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53Ar5

Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST Special Publication 800-30, Revision 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1

Kabanov, I., & Madnick, S. (2021). Applying the lessons from the Equifax cybersecurity incident to build a better defense. *MIS Quarterly Executive*, *20*(2), 109-125. https://aisel.aisnet.org/misqe/vol20/iss2/4

Lively, T. (2022, March 24). *U.S. state privacy legislation tracker*. International Association of Privacy Professionals. https://iapp.org/resources/article/us-state-privacy-legislation-tracker/

Marron, J. A. (2024). *Implementing the Health Insurance Portability and Accountability Act (HIPAA) security rule: A cybersecurity resource guide* (NIST Special Publication 800-66, Revision 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-66r2

Neprash, H. T., McGlave, C. C., Cross, D. A., Virnig, B. A., Puskarich, M. A., Huling, J. D., Rozenshtein, A. Z., & Nikpay, S. S. (2022). Trends in ransomware attacks on US hospitals, clinics, and other health care delivery organizations, 2016–2021. *JAMA Health Forum*, *3*(12), e224873. https://doi.org/10.1001/jamahealthforum.2022.4873

Office of the National Coordinator for Health Information Technology. (2024). *Information blocking* (45 C.F.R. pt. 171). Electronic Code of Federal Regulations. https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-171

PCI Security Standards Council. (2024). *Payment Card Industry Data Security Standard: Requirements and testing procedures, version 4.0.1*. https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf

Securities and Exchange Commission. (2023). *Cybersecurity risk management, strategy, governance, and incident disclosure* (Final Rule, Release Nos. 33-11216; 34-97989), 17 C.F.R. pts. 229, 232, 239, 240, 249. https://www.sec.gov/files/rules/final/2023/33-11216.pdf

Shahzadi, A., Ishaq, K., Dogar, A. B., Khan, J. A., Mylonas, A., Nawaz, N. A., Yasin, A., & Khan, F. A. (2025). Safeguarding the healthcare sector from ransomware attacks: Insights from a literature review. *PeerJ Computer Science*, *11*, e3073. https://doi.org/10.7717/peerj-cs.3073

Stine, K., Quinn, S., Witte, G., & Gardner, R. K. (2025). *Integrating cybersecurity and enterprise risk management (ERM)* (NIST Internal Report 8286, Revision 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.IR.8286r1

Subramanian, H., Sengupta, A., & Xu, Y. (2024). Patient health record protection beyond the Health Insurance Portability and Accountability Act: Mixed methods study. *Journal of Medical Internet Research*, *26*, e59674. https://doi.org/10.2196/59674

Tariq, M. I., Ahmed, S., Memon, N. A., Tayyaba, S., Ashraf, M. W., Nazir, M., Hussain, A., Balas, V. E., & Balas, M. M. (2020). Prioritization of information security controls through fuzzy AHP for cloud computing networks and wireless sensor networks. *Sensors*, *20*(5), 1310. https://doi.org/10.3390/s20051310

U.S. Department of Health and Human Services. (2023a). *Healthcare and Public Health Sector-Specific Cybersecurity Performance Goals*. ASPR TRACIE. https://asprtracie.hhs.gov/technical-resources/resource/12863/healthcare-and-public-health-sector-specific-cybersecurity-performance-goals

U.S. Department of Health and Human Services. (2023b). *Health Industry Cybersecurity Practices: Managing threats and protecting patients (HICP)*, 2023 Edition. 405(d) Program. https://405d.hhs.gov/Documents/HICP-Main-508.pdf

U.S. Department of Health and Human Services. (2025, January 6). *HIPAA Security Rule to strengthen the cybersecurity of electronic protected health information* (Proposed Rule, RIN 0945-AA22). *Federal Register*, *90*(3), 898–1022. https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information

U.S. Department of Health and Human Services, Office for Civil Rights. (2018-2025). *HIPAA Resolution Agreements and Corrective Action Plans* [Bundled enforcement-evidence corpus]. https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/index.html

U.S. Department of Health and Human Services, Office for Civil Rights. (2025, July 31). *Change Healthcare cybersecurity incident frequently asked questions*. https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html

U.S. Department of Health and Human Services, Office for Civil Rights. (2021, May 17). *Summary of the HIPAA security rule*. https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html

UnitedHealth Group. (2025). *Annual report on Form 10-K for the fiscal year ended December 31, 2024*. U.S. Securities and Exchange Commission. https://www.sec.gov/Archives/edgar/data/731766/000073176625000063/unh-20241231.htm

Westland, J. C. (2020). The information content of Sarbanes-Oxley in predicting security breaches. *Computers & Security*, *90*, 101687. https://doi.org/10.1016/j.cose.2019.101687

107th Congress. (2002). *Sarbanes-Oxley Act of 2002* (Public Law 107-204). U.S. Government Publishing Office. https://www.govinfo.gov/app/details/PLAW-107publ204

111th Congress. (2009). *American Recovery and Reinvestment Act of 2009 (Public Law 111-5)*, including Title XIII Health Information Technology for Economic and Clinical Health (HITECH) Act. U.S. Government Publishing Office. https://www.govinfo.gov/app/details/PLAW-111publ5

---

## Appendix

**Table A1**

*Prioritized Needs-to-Controls Mapping for UnitedHealth Group*

| # | Compliance Need (Regulatory Citation) | NIST SP 800-53r5 Family | Specific Control IDs |
|---|---|---|---|
| 1 | Risk analysis of ePHI threats and vulnerabilities (45 C.F.R. § 164.308(a)(1)(ii)(A)) | RA - Risk Assessment | RA-3 Risk Assessment, RA-5 Vulnerability Monitoring and Scanning, RA-7 Risk Response |
| 2 | Risk management to reasonable and appropriate level (§ 164.308(a)(1)(ii)(B)) | PM, CA - Program Management and Assessment | PM-9 Risk Management Strategy, PM-28 Risk Framing, CA-2 Control Assessments, CA-7 Continuous Monitoring |
| 3 | Workforce security and access management (§§ 164.308(a)(3), 164.308(a)(4), 164.312(a)) | AC, PS - Access Control and Personnel Security | AC-2 Account Management, AC-3 Access Enforcement, AC-6 Least Privilege, PS-3 Personnel Screening, PS-4 Personnel Termination |
| 4 | Authentication for ePHI access (§ 164.312(d)) | IA - Identification and Authentication | IA-2 Identification and Authentication, IA-2(1) Multifactor for Privileged Accounts, IA-5 Authenticator Management |
| 5 | Audit controls, record and examine system activity (§ 164.312(b)) | AU - Audit and Accountability | AU-2 Event Logging, AU-3 Content of Audit Records, AU-6 Audit Record Review, AU-12 Audit Record Generation |
| 6 | Security awareness and training (§ 164.308(a)(5)) | AT, SI - Awareness Training and System Integrity | AT-2 Literacy Training, AT-3 Role-Based Training, SI-3 Malicious Code Protection |
| 7 | Transmission and at-rest encryption of ePHI (§§ 164.312(a)(2)(iv), 164.312(e)(2)(ii)) | SC, MP - System and Communications Protection and Media Protection | SC-8 Transmission Confidentiality, SC-13 Cryptographic Protection, SC-28 Protection of Information at Rest, MP-7 Media Use |
| 8 | Contingency plan including backup, disaster recovery, emergency-mode operation (§ 164.308(a)(7)) | CP - Contingency Planning | CP-2 Contingency Plan, CP-4 Contingency Plan Testing, CP-9 System Backup, CP-10 System Recovery |
| 9 | Security incident procedures (§ 164.308(a)(6)) | IR - Incident Response | IR-1 Policy and Procedures, IR-4 Incident Handling, IR-6 Incident Reporting, IR-8 Incident Response Plan |
| 10 | Business associate / supply-chain risk management (§§ 164.308(b), 164.314(a), HITECH § 13401) | SR, SA - Supply Chain RM and System and Services Acquisition | SR-2 SCRM Plan, SR-3 Supply Chain Controls, SR-6 Supplier Assessments, SA-9 External System Services |
| 11 | Configuration and change management for clinical systems | CM - Configuration Management | CM-2 Baseline Configuration, CM-3 Configuration Change Control, CM-7 Least Functionality |
| 12 | Vulnerability management and patching | RA, SI | RA-5 Vulnerability Monitoring, SI-2 Flaw Remediation |
| 13 | Documentation retention (§ 164.316(b)(2)) | AU, PM | AU-11 Audit Record Retention, PM-1 Information Security Program Plan |
| 14 | SEC Item 1.05 four-business-day incident disclosure (17 C.F.R. § 240.13a-11) | IR | IR-6 Incident Reporting, IR-8 Incident Response Plan |
| 15 | SEC Item 1C annual risk-management and governance disclosure (17 C.F.R. § 229.106) | PM, CA | PM-1 Program Plan, PM-2 Senior Information Security Officer, CA-7 Continuous Monitoring |
| 16 | API security for ONC information-blocking compliance (45 C.F.R. § 171.203) | IA, AC, AU, SC | IA-8 Identification and Authentication (Non-Organizational Users), AC-21 Information Sharing, AU-2, SC-8 |
| 17 | OCR breach-notification timing (45 C.F.R. §§ 164.404-164.408) | IR | IR-6 Incident Reporting, IR-8 Incident Response Plan |
| 18 | State-law privacy compliance (CCPA/CPRA, others) | PT - PII Processing and Transparency | PT-1 Policy and Procedures, PT-2 Authority to Process, PT-3 PII Processing Purposes |
| 19 | SOX § 404 ICFR for systems supporting financial reporting | CA, AU, AC, CM | CA-2, AU-6, AC-6, CM-3 |
| 20 | Ransomware-specific controls (NIST IR 8374 alignment) | SI, CP, IR, IA | SI-3, SI-4 System Monitoring, CP-9, IR-4(1) Automated Incident Handling, IA-2(1) |

*Note.* Twenty unified compliance needs map to NIST SP 800-53 Revision 5 control families using the SP 800-66 Revision 2 HIPAA crosswalk (Marron, 2024). Several rows group multiple controls within a single family. ePHI denotes electronic protected health information, ICFR denotes internal control over financial reporting, and SCRM denotes supply chain risk management.

**Table A2**

*Comparative Evaluation of Candidate Control Sources for UnitedHealth Group*

| Attribute | NIST SP 800-66r2 to SP 800-53r5 | ISO/IEC 27001:2022 | HITRUST CSF v11 | COBIT 2019 | CIS Controls v8 |
|---|---|---|---|---|---|
| HIPAA crosswalk directness | Direct, HHS-recognized canonical mapping | Indirect, requires third-party crosswalk | Direct, healthcare-tailored mapping | Indirect, governance-level only | Indirect, defensive-control level only |
| FISMA / federal statutory authority | Yes (FISMA, OMB A-130) | No | No | No | No |
| SEC 2023 Item 1C disclosure compatibility | Disclosure-compatible (NIST framework) | Disclosure-compatible | Less commonly used in Item 1C framing | Less commonly used in Item 1C framing | Less commonly used in Item 1C framing |
| License cost | Free, public domain | Licensed (purchase + annual fee) | Licensed (subscription + assessor fee) | Licensed | Free for end users |
| Sector-specific tailoring | Healthcare via SP 800-66r2, HHS 405(d) HICP overlay | Generic, sector annexes available | Healthcare-specific by design | Process-governance focus | Sector-neutral defensive baseline |
| Certification mechanism | Third-party assessment under SP 800-53A, no central certification body | Accredited certification under ISO/IEC 17021 | HITRUST validated assessment + certification | Self-attestation | Self-attestation, community implementation |
| Primary strength for UnitedHealth Group | Convergent regulatory authority + canonical HIPAA crosswalk + zero cost | International acceptance for global subsidiaries | Healthcare-tailored audit artifacts | Board-level IT governance language | Practical baseline for low-resource business units |
| Principal limitation for UnitedHealth Group | No central certification mark | No HHS-issued HIPAA crosswalk, license cost | Proprietary licensing, assessment cost, and dependence on NIST as the underlying catalog | Insufficient control-catalog depth at § 164.308 enforcement granularity | No HIPAA crosswalk, lacks PT family equivalent |

*Note.* Sources used in this comparison include Joint Task Force (2020a, 2020b), Marron (2024), ISO 27001 Security (2022), HITRUST Alliance (2025), Information Systems Audit and Control Association (2018), and Center for Internet Security (2021). CSF denotes Common Security Framework, ICFR denotes internal control over financial reporting, and PT denotes the Personally Identifiable Information Processing and Transparency control family.

