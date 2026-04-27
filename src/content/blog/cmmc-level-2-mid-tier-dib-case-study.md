---
title: "Inside a CMMC Level 2 Journey: A Mid-Tier DIB Contractor Case Study"
description: "A composite case study of a 350-person defense subcontractor with 47 suppliers and 15 months to reach CMMC Level 2 — and the scope-discipline strategy that makes it possible."
publishDate: 2026-04-26
author: "Justin T. Begarek"
lane: research
topics:
  - CMMC
  - NIST
  - Risk Management
  - DIB
  - Supply Chain
featured: true
draft: false
citations: false
diagrams: false
---

The hardest version of CMMC Level 2 is not the largest. The largest contractors have dedicated security staff, established control programs, and the budgets to absorb assessment cost without disruption. The hardest version is the mid-tier subcontractor: 200 to 500 employees, two or three IT staff who also run security, a flat network that grew organically over 15 years, dozens of suppliers feeding production, and a contracting officer who just told them their next solicitation will require Level 2.

This is a composite, fictional case study of one such organization. ForgeWorks Systems, Inc. — a hypothetical 350-person second-tier supplier producing machined subassemblies for defense aviation programs — does not exist. The profile is constructed from typical characteristics of mid-tier defense industrial base subprimes and is used here as a teaching vehicle. None of the technical or strategic details should be read as describing a real client engagement.

The question worth asking through the case is not whether ForgeWorks can implement 110 NIST SP 800-171 practices. It is whether the company can do that within 15 months, with two IT staff, while keeping production running, and produce evidence that a Certified Third-Party Assessment Organization will accept. The answer turns on two strategic moves before any control implementation begins.

---

## The ForgeWorks Profile

ForgeWorks holds active subcontracts with three prime contractors. Each prime flows down DFARS 252.204-7012, 7019, 7020, and 7021. The company receives Controlled Unclassified Information in the form of technical drawings, specifications, and program data. CUI lives on roughly 70 engineering workstations, a shared technical-data file server, an on-premises ERP system, and email. The remaining roughly 280 endpoints across operations, finance, sales, and the production floor handle non-CUI business data.

The current security posture is mixed. Microsoft 365 conditional access is in place with MFA. Endpoint antivirus is deployed and reasonably current. Patching follows a monthly cadence. The company's modeled Supplier Performance Risk System self-score is +85 — short of the +110 maximum but well above the floor — which signals real progress on basic hygiene but unfinished work in several control families.

The structural problems are harder. MFA is inconsistent across VPN and ERP access. Several administrator accounts are shared across the IT team rather than individually attributed. The System Security Plan and Plan of Action and Milestones exist as draft artifacts but are not maintained as living documents. The supplier base — 47 subcontractors that feed ForgeWorks production — has no formal cybersecurity attestation process beyond contractual flow-down language.

Two IT full-time employees divide their time across operations, user support, and security. There is no CISO and no compliance lead. The 15-month assessment runway assumes ForgeWorks adds one compliance-focused full-time employee during the period. If that hire does not happen, the same control set remains valid but the timeline shifts toward Conditional Level 2 certification before reaching Final Level 2.

---

## Threat Prioritization Drives Sequencing

NIST IR 8286A Revision 1 frames cybersecurity risk as the product of likelihood and impact, decomposed into sources, events, vulnerabilities, and predisposing conditions. For ForgeWorks, that framework yields five prioritized threats that drive the implementation sequence:

**Nation-state intrusion against CUI-bearing supply chains.** Verizon's 2025 Data Breach Investigations Report documented 1,607 confirmed manufacturing breaches and a sharp increase in espionage-motivated activity in the sector. For a defense subprime, the attack path is direct: adversaries exploit exposed remote services, weak supplier access, or stolen credentials, then move toward technical data used by prime contractors. Likelihood and impact both score high. Composite risk: 9 of 9.

**Supplier compromise.** With 47 subcontractors, each supplier connection represents a potential attack path. Cyber supply chain risk is governance-heavy and procurement-coupled — the procurement team sets the contractual frame, but security has to verify that flow-down language translates into actual control implementation downstream. Risk score: 6 to 9 depending on the supplier tier.

**Ransomware.** A production outage threatens availability even when espionage is not the attacker's motive. With assumed revenue of $95 million over 260 workdays, one lost production day exposes about $365,385 in revenue. A 10-day outage exposes about $3.65 million before penalties, rework, or recovery costs. Risk score: 6.

**Credential misuse and lateral movement.** Shared administrator accounts erase attribution. Inconsistent MFA on VPN and ERP creates exploitable seams. Combined with a flat internal network, the result is that initial compromise of any account can move laterally to CUI-handling systems. Risk score: 6.

**Legacy operational technology.** Production-floor endpoints — Windows 7 HMIs, PLC-adjacent systems — create policy and segmentation problems. They cannot be patched on the same cadence as office workstations and frequently have weaker authentication. Lateral movement from an office system into the OT zone is the highest-impact failure mode the company has not yet addressed. Risk score: 4 to 6.

The sequence of risk-reduction moves follows this prioritization, not the order of NIST SP 800-171 control families.

---

## Strategic Move 1: The CUI Enclave

The single highest-leverage decision in the ForgeWorks roadmap is architectural, not procedural. Rather than treating all 350 endpoints as in scope for CMMC Level 2 assessment, the company isolates CUI processing into a dedicated enclave: the 70 engineering workstations, the technical-data server, and the CUI-facing ERP functions. Everything else — operations, finance, the production floor business systems — moves out of scope.

NIST SP 800-207 anchors the design. Access decisions inside the enclave are made on identity, device posture, and session context rather than network location. Engineering workstations receive stricter access controls, full-disk encryption, enforced MFA, dedicated administrator credentials, and detailed logging. Network boundary protection separates the enclave from the rest of the corporate network. Remote access to enclave systems flows through MFA-protected, encrypted channels.

The scope reduction is the point. NIST SP 800-171 applies to systems that store, process, or transmit CUI. By concentrating CUI handling into roughly 70 endpoints rather than 350, ForgeWorks reduces the assessment surface by approximately 80 percent. The 110 practices still apply to the in-scope systems, but the volume of evidence to collect, the number of devices to harden, and the population of users to train all shrink in proportion.

A C3PAO assesses what is in scope. A defensible enclave with documented boundaries, validated isolation, and traceable data flows is the cheapest path to Level 2 readiness for any contractor whose CUI handling does not need to be enterprise-wide.

---

## Strategic Move 2: Supplier Governance

The second move addresses the 47-supplier attack surface. DFARS 252.204-7012 flow-down language is a contractual obligation but not, by itself, a control. The control is the verification process that turns flow-down into operational discipline downstream.

ForgeWorks builds a tiered supplier risk program over months 2 through 6. Each supplier handling CUI provides a current CMMC status attestation — self-assessed Level 1, self-assessed Level 2, or third-party-certified Level 2 — and confirms its understanding of DFARS flow-down terms. A questionnaire keyed to data sensitivity, remote access patterns, software dependencies, and incident reporting establishes a baseline for each supplier's posture.

The questionnaire output drives tier assignment. Tier 1 suppliers — those with direct CUI access or critical software dependencies — undergo annual review and incident-notification clauses. Tier 2 suppliers receive periodic attestation refreshes. Tier 3 suppliers — those with no CUI exposure — remain on the standard procurement cadence.

NIST SP 800-161 Rev 1 frames supplier governance as multilevel risk management rather than a single procurement gate. CISA's Cross-Sector Cybersecurity Performance Goals provide voluntary maturity guidance but do not replace DFARS flow-down requirements. The combined effect is that supplier-mediated compromise becomes a tracked, documented risk with a defined response process — rather than a contractual hope.

---

## The Twelve-Control Set

After the architectural and governance decisions, the controls themselves are a deliberate subset of the 110 NIST SP 800-171 practices, sequenced to address the prioritized threats. Twelve controls do most of the work:

**Access control and identification.** Privileged multifactor authentication, individual administrator accounts (no shared credentials), encrypted remote access through VPN with MFA, and password policy aligned to NIST SP 800-63B. These four controls treat credential theft, privilege misuse, and exposed-service compromise.

**System and communications protection.** Enclave boundary protection, encryption in transit for CUI, encryption at rest on enclave systems, and least-functionality plus application allowlisting for legacy operational technology. These four controls treat lateral movement, data exfiltration value, and unauthorized code execution.

**Incident response and awareness.** A formal incident-handling plan keyed to DFARS 7012 reporting requirements, recurring tabletop testing, DIBNet-aligned reporting procedures, and security-awareness training with quarterly phishing simulations. These four controls reduce containment time, shorten reporting latency, and reduce avoidable human-factor incidents.

The honest framing: these twelve controls do not eliminate nation-state or ransomware risk. They reduce probability and impact. They also produce the kind of repeatable, evidenced operating practice that a C3PAO can validate. The remaining 98 of the 110 practices still need to be addressed, but most fall into supporting roles around these twelve — policy documentation, configuration baseline standards, audit log retention, periodic review cadences. The twelve are where the protective value concentrates.

---

## Implementation Timeline and Cadence

The 15-month runway breaks into three phases.

**Months 1–3: Foundation.** Asset inventory, enclave scope definition, privileged-access cleanup, MFA enrollment across all enclave users (target 95 percent or higher by month 3), and completion of the SSP and POA&M baseline. The objective is to have a documented and defensible enclave perimeter, individually attributed administrator accounts, and current self-assessment evidence in SPRS.

**Months 4–9: Build.** Boundary protection deployment, encryption rollout, supplier attestation collection, OT segmentation pilots, log management capability, and incident response plan testing. By month 9, the company should be able to demonstrate, not just assert, control implementation across the 110 practices.

**Months 10–15: Validate.** Tabletop exercises against realistic scenarios, evidence testing against NIST SP 800-171A assessment objectives, mock assessment with the chosen C3PAO, and remediation of any findings. The C3PAO assessment occurs in month 15 or shortly after.

The monitoring cadence is what turns implementation into operating practice. Monthly reviews track privileged accounts, POA&M closure, and any drift in in-scope asset count. Quarterly reviews examine supplier attestation status, firewall rules, phishing simulation results, endpoint alerts, and deny-log trends. Annual reviews include tabletop exercises and executive acceptance of residual risk. OT segmentation receives semiannual review because production-floor controls have different change-management constraints than office IT.

The economic logic is conservative but durable. If enclave scope reduction and incident response maturity reduce the modeled 10-day ransomware exposure by 20 percent, the avoided first-order revenue exposure equals about $730,770. That is not a guaranteed return on investment — it is a measured estimate of how much risk the program needs to retire to justify itself. Even at half that rate, the implementation cost is recovered in a single avoided incident.

---

## Why This Approach Generalizes

ForgeWorks is fictional, but the strategic shape of its CMMC Level 2 path applies to most mid-tier defense subprimes. Three patterns recur:

**Scope discipline beats catalog completeness.** Most contractors who fail CMMC assessments do not fail because they implemented the wrong controls. They fail because the controls were not implemented across all in-scope systems consistently, or because evidence of implementation could not be produced. Concentrating CUI into a smaller enclave makes both consistency and evidence achievable for organizations without enterprise-scale security teams.

**Supplier governance is a control, not a contract clause.** Flow-down language is necessary and not sufficient. The contractors who manage supply chain risk effectively are the ones who treat it as an ongoing operational practice with attestation tracking, tiered review, and incident-notification expectations — not as a clause that goes into the procurement template and then sits unmonitored.

**Twelve controls do most of the protective work.** Of the 110 NIST SP 800-171 practices, a relatively small subset — concentrated in access control, system and communications protection, and incident response — produces most of the actual risk reduction. The remaining practices are necessary for assessment but largely supporting. Recognizing this lets a small team prioritize where their hours go.

CMMC Level 2 is not the endpoint of a defensible cybersecurity program. It is the floor that allows a defense contractor to remain eligible for work involving CUI. ForgeWorks reaching Level 2 in 15 months is plausible because it treats the assessment as scope discipline and risk prioritization rather than as a checklist exercise. That posture is what generalizes.

For the broader CMMC program structure and assessment mechanics, see [CMMC 2.0 Levels, Assessment Paths, and What Certification Actually Costs](/blog/cmmc-2-levels-assessment-cost). For the specific DFARS clauses ForgeWorks operates under, see [The DFARS Clause Stack: 7012, 7019, 7020, and 7021 Explained](/blog/dfars-clause-stack-7012-7019-7020-7021). For the policy framework behind it all, see [Federal Cybersecurity Law and the Defense Industrial Base](/blog/federal-cybersecurity-law-dib-fragmentation).

---

*Justin T. Begarek is an IT Cybersecurity Specialist and PhD candidate in Cybersecurity. This analysis reflects the author's independent research and academic work. ForgeWorks Systems, Inc. is a composite, fictional case study and does not describe a real engagement.*
