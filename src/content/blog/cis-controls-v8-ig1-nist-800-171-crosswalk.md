---
title: "The CIS Controls v8 IG1 → NIST SP 800-171 Crosswalk for DIB Contractors"
description: "If your program runs on CIS Controls v8 IG1, here is what that gets you against the 110 NIST SP 800-171 practices a C3PAO assesses — and where the gaps are."
publishDate: 2026-04-26
author: "Justin T. Begarek"
lane: practical
topics:
  - CMMC
  - NIST
  - CIS Controls
  - Compliance
  - DIB
featured: false
draft: false
citations: false
diagrams: false
---

A common pattern among small and mid-tier defense contractors: the security program was built years ago around the CIS Critical Security Controls v8, the team adopted Implementation Group 1 as the baseline, and now a CMMC Level 2 obligation is on the contract roadmap. The natural question is how much of the 110-practice NIST SP 800-171 assessment is already covered by the 56 IG1 Safeguards the organization has been running.

The short answer is: a meaningful portion, but not all of it, and the gaps cluster in places that matter to a Certified Third-Party Assessment Organization. This post walks through what IG1 actually covers, where it maps cleanly to NIST SP 800-171, and where additional work is required before a C3PAO assessment.

*For background on which NIST SP 800-171 revision is currently assessable under CMMC — and why that matters for a crosswalk — see [NIST SP 800-171 Revision 3 Is Published. Your CMMC Assessment Still Uses Revision 2.](/blog/nist-800-171-revision-2-vs-revision-3-cmmc-gap) The crosswalk in this post uses the Revision 2 baseline that DFARS currently binds contractors to, with notes where Revision 3 reorganizes or adds requirements.*

---

## What IG1 Actually Is

CIS Controls v8 organizes 153 Safeguards under 18 Controls and divides them into three Implementation Groups. IG1 is the foundational tier — 56 Safeguards that the Center for Internet Security defines as "essential cyber hygiene," the baseline every enterprise should run regardless of size. IG2 adds 74 more Safeguards (130 total) for organizations with sensitive data and moderate resources. IG3 adds the remaining 23 (153 total) for mature organizations defending against sophisticated threats.

The IG1 design assumption is a small enterprise with limited IT staff and commercial-off-the-shelf systems. That profile fits a large share of the defense industrial base: roughly 100,000 firms, most of them under 100 employees. CIS frames IG1 as the controls that block the most common documented attacker techniques — credential theft, malware delivery, missing patches, exposed services — without requiring dedicated security staff to operate.

The 56 IG1 Safeguards span all 18 Controls but at varying depth. Asset and software inventory (Controls 1 and 2) are well-covered. Account and access management (Controls 5 and 6) include MFA for administrative and externally-exposed access. Data protection (Control 3) includes data inventory and basic encryption. Vulnerability management (Control 7) is at the patching level, not the scanning-and-prioritization level — that is mostly IG2.

---

## What NIST SP 800-171 Requires

NIST SP 800-171 Revision 2 organizes 110 security requirements across 14 control families: Access Control, Awareness and Training, Audit and Accountability, Configuration Management, Identification and Authentication, Incident Response, Maintenance, Media Protection, Personnel Security, Physical Protection, Risk Assessment, Security Assessment, System and Communications Protection, and System and Information Integrity. CMMC Level 2 assesses all 110 against the assessment objectives in NIST SP 800-171A, with scoring in the Supplier Performance Risk System using DoD's specific point methodology (5, 3, or 1 point per requirement).

Revision 3 reorganizes these families, adds new requirements focused on software supply chain integrity, and introduces more organization-defined parameters. The mapping between revisions is not one-to-one. Until DoD amends DFARS to incorporate Revision 3, the assessment baseline remains Revision 2 — so this crosswalk uses Revision 2 numbering.

---

## The Crosswalk by 800-171 Family

The table below shows how IG1 Safeguards cover each NIST SP 800-171 Rev 2 family. "Strong" means IG1 covers the family's intent at a level that maps cleanly to assessable practices. "Partial" means IG1 addresses some but not all requirements in the family. "Gap" means IG1 does not meaningfully cover the family and additional controls are needed.

| 800-171 Family | Practices | IG1 Coverage | Primary IG1 Safeguards | Notes |
|---|---|---|---|---|
| 3.1 Access Control | 22 | Partial | 3.3, 5.1–5.4, 6.1–6.5, 12.1, 12.4 | IG1 covers account management and MFA basics. Session lock, remote access controls, and CUI flow control are partial. |
| 3.2 Awareness and Training | 3 | Strong | 14.1, 14.2 | IG1 establishes a security awareness program with role-relevant content. CMMC adds insider-threat training depth. |
| 3.3 Audit and Accountability | 9 | Gap | 8.1, 8.2 | IG1 only requires log collection and time synchronization. Audit content, review, retention, and protection are mostly IG2 (8.5–8.11). |
| 3.4 Configuration Management | 9 | Strong | 1.1, 2.1–2.3, 4.1–4.7 | Asset inventory, software allowlisting, and secure configuration baselines map well. Change control formality is partial. |
| 3.5 Identification and Authentication | 11 | Partial | 5.2, 6.3–6.5 | MFA for admin and remote access is covered. FIPS-validated cryptography for password storage and replay-resistant authentication are gaps. |
| 3.6 Incident Response | 3 | Partial | 17.1–17.3 | IG1 establishes an IR program, designates personnel, and defines reporting. Tabletop exercises and forensic capability are mostly IG2 (17.4–17.9). |
| 3.7 Maintenance | 6 | Gap | — | IG1 does not address maintenance controls directly. CMMC requires controlled maintenance, sanitization of equipment, and supervision of external maintenance personnel. |
| 3.8 Media Protection | 9 | Partial | 3.1, 3.4 | IG1 covers data inventory and basic disposal. Media marking, transport, and access controls for CUI are gaps. |
| 3.9 Personnel Security | 2 | Gap | — | IG1 does not address personnel screening or termination procedures. Both are required for CMMC Level 2. |
| 3.10 Physical Protection | 6 | Gap | — | IG1 does not cover facility access controls, visitor logs, or alternate work-site protections. |
| 3.11 Risk Assessment | 3 | Partial | 7.1, 7.3 | IG1 includes vulnerability management process and patching. Periodic risk assessment and vulnerability scanning depth are mostly IG2 (7.5–7.7). |
| 3.12 Security Assessment | 4 | Gap | — | CMMC-specific. Requires SSP, POA&M, periodic control assessment, and continuous monitoring strategy. IG1 has no direct equivalent. |
| 3.13 System and Communications Protection | 16 | Partial | 4.4, 12.1, 12.2, 12.4, 13.1 | IG1 covers boundary protection and network segmentation basics. FIPS-validated cryptography, mobile code controls, and CUI-specific transmission protections are gaps. |
| 3.14 System and Information Integrity | 7 | Strong | 7.3, 10.1, 10.2, 13.6 | Malware defenses, patching, and anti-malware update mechanisms map cleanly. Security alert monitoring and information input validation are partial. |

Across all 14 families, IG1 provides strong coverage in 3, partial coverage in 6, and meaningful gaps in 5. The scope of work to close the gaps is what determines whether your IG1 program is six weeks from a C3PAO-ready posture or six months.

---

## What IG1 Covers Well

Five areas come over from IG1 with relatively little additional work:

**Asset and software inventory.** Safeguards 1.1 and 2.1 establish enterprise asset and software inventories. NIST SP 800-171 builds on these for configuration management (3.4.1, 3.4.2) and supports several other control families that depend on knowing what is in scope.

**Account and access management.** Safeguards 5.1 through 5.4 plus 6.1 through 6.5 cover account inventory, disabling dormant accounts, separation of administrative privileges, MFA for administrative access, and MFA for externally-exposed applications. This maps to the core of NIST 3.1 (Access Control) and 3.5 (Identification and Authentication).

**Software allowlisting and secure configuration.** Safeguards 2.5 through 2.7 and 4.1 through 4.7 establish allowlisting, secure configurations for assets and software, and automated update mechanisms. This satisfies most of NIST 3.4 (Configuration Management).

**Malware defenses and patching.** Safeguards 10.1, 10.2, and 7.3 cover anti-malware deployment, signature updates, and remediation of detected vulnerabilities. These map cleanly to 3.14 (System and Information Integrity).

**Security awareness program.** Safeguards 14.1 and 14.2 establish a security awareness training program with role-relevant content. With minor extensions for insider threat awareness, this satisfies 3.2 (Awareness and Training).

For a contractor running IG1 cleanly, these five areas typically require documentation work — mapping evidence to NIST control objectives — rather than implementation work.

---

## Where the Gaps Are

The five families where IG1 leaves meaningful gaps are predictable, and they are the ones that show up in CMMC assessment failures most often.

**Audit and accountability (3.3).** IG1 collects logs but does not require auditable content, regular review, retention periods, or protection of audit information. NIST SP 800-171 has nine practices in this family. Most contractors need to add a log management capability — centralized collection, defined retention, scheduled review, and audit log protection — before assessment.

**Maintenance (3.7).** IG1 does not address maintenance at all. Six 800-171 practices require controlled maintenance, equipment sanitization before off-site service, supervision of external maintenance personnel, and approval of remote maintenance. These are administrative controls that need policy, procedure, and evidence.

**Physical protection (3.10).** IG1 does not cover physical security. Six 800-171 practices require facility access controls, visitor procedures, and protection at alternate work sites. For contractors operating from a single office, this is a documentation exercise. For contractors with multiple sites or significant remote work, it is more substantial.

**Personnel security (3.9).** IG1 does not address screening or termination. The two 800-171 practices in this family require personnel screening before granting access to CUI and procedures for handling access on termination.

**Security assessment (3.12).** This family is CMMC-specific. The four practices require a System Security Plan, a Plan of Action and Milestones for any unmet requirements, periodic control assessment, and a continuous monitoring strategy. An IG1 program will not have these documents in CMMC-required form.

The gap in audit and accountability is the most common cause of low SPRS scores during self-assessment. The gaps in maintenance, physical protection, and personnel security are usually closeable through policy and process, not technology purchases. The security assessment family is where the real work of CMMC documentation lives — SSP and POA&M discipline are where most contractors spend the largest share of their preparation time.

---

## What IG2 Adds That Closes the Largest Gaps

Several IG2 Safeguards directly close 800-171 gaps and may justify expanding from IG1 to selected IG2 controls:

- **Safeguard 8.5 (collect detailed audit logs)** and **8.11 (conduct audit log reviews)** address most of the 3.3 audit and accountability shortfall.
- **Safeguard 7.5 (perform automated vulnerability scans of internal enterprise assets)** and **7.6 (perform automated vulnerability scans of externally-exposed enterprise assets)** address the scanning depth that 3.11.2 and 3.12.2 expect.
- **Safeguard 17.4 (establish and maintain an incident response process)** and **17.5 through 17.9** address the IR maturity that 3.6 expects beyond basic program existence.
- **Safeguard 13.1 (centralize security event alerting)** addresses elements of 3.14.6 (monitor system security alerts) and 3.14.7 (identify unauthorized use).

For a contractor whose only obstacle to CMMC Level 2 is the audit, vulnerability, and incident response maturity gaps, adding selected IG2 Safeguards is often more cost-effective than buying point solutions.

---

## Practical Sequencing

For an organization sitting on a clean IG1 implementation today and planning a CMMC Level 2 assessment in the next 12 to 18 months, a defensible sequence:

1. **Document what you have.** Map each IG1 Safeguard to the NIST SP 800-171 practices it satisfies. This becomes the bones of the SSP. Where one IG1 Safeguard partially satisfies a NIST practice, document what is and is not yet covered.
2. **Score yourself.** Run a NIST SP 800-171 self-assessment using DoD's scoring methodology. Post the score in SPRS as required by DFARS 252.204-7019. The IG1 baseline alone typically produces a score in the +50 to +75 range out of 110, depending on how many practices the organization has extended beyond IG1.
3. **Close the structural gaps first.** Audit and accountability, maintenance, physical protection, personnel security, and security assessment are usually closeable with policy, procedure, and existing tooling. Address these before buying new technology.
4. **Pick targeted IG2 additions.** Rather than expanding to full IG2 (74 more Safeguards), select the IG2 Safeguards that close specific 800-171 gaps. The list above is a starting point.
5. **Build SSP and POA&M discipline.** Even when controls are implemented, the assessment hinges on whether you can demonstrate them. SSP narrative quality and POA&M tracking are where C3PAOs make their judgment.

For the broader CMMC program structure, level definitions, and what assessment actually involves, see [CMMC 2.0 Levels, Assessment Paths, and What Certification Actually Costs](/blog/cmmc-2-levels-assessment-cost). For the SPRS scoring mechanics, see [SPRS Scoring: How to Self-Score Your NIST SP 800-171 Assessment](/blog/sprs-scoring-nist-800-171-self-assessment). For why your assessment will use Revision 2 even though Revision 3 is published, see [NIST SP 800-171 Revision 3 Is Published. Your CMMC Assessment Still Uses Revision 2.](/blog/nist-800-171-revision-2-vs-revision-3-cmmc-gap)

---

*Justin T. Begarek is an IT Cybersecurity Specialist and PhD candidate in Cybersecurity. This analysis reflects the author's independent research and academic work.*
