---
title: "The HIPAA Security Rule NPRM: A Control Roadmap Before the Final Rule Lands"
description: "HHS proposed the most consequential HIPAA Security Rule rewrite in 20 years. Here is what to map to your controls now, before the final rule sets the clock."
publishDate: 2026-05-10
author: "Justin T. Begarek"
lane: practical
topics:
  - HIPAA
  - Healthcare
  - NIST
  - Risk Management
  - Compliance
featured: false
draft: false
citations: false
diagrams: false
---

On January 6, 2025, HHS published a Notice of Proposed Rulemaking that would rewrite the HIPAA Security Rule for the first time since 2003 (90 Fed. Reg. 898). The proposal is the most consequential healthcare cybersecurity rule change in two decades. It is also, today, still proposed.

That distinction matters. A proposed rule is not enforceable. But for any organization that handles ePHI, the NPRM has already changed the operational standard of care. Customers reference it. Carriers reference it. OCR investigators reference it. And when the final rule lands, organizations that started mapping early will be ready, and organizations that waited will run a non-compliance window of their own making.

This post walks through what the NPRM proposes, why it lines up with what you should already be building, and how to start mapping evidence now without overcommitting to provisions that may shift before finalization.

---

## What the NPRM Actually Proposes

The 2003 Security Rule is technology-neutral, scalable, and famously flexible. Many of its specifications are "addressable," which has been read for years as "optional with a written rationale." The NPRM rebuilds the rule around explicit, prescriptive cybersecurity safeguards. The most operationally consequential proposed requirements include:

- **Asset inventory and network maps** kept current and reviewed at least annually.
- **Multi-factor authentication** for systems that maintain ePHI, with limited exceptions.
- **Encryption of ePHI** at rest and in transit, with FIPS-validated modules expected.
- **Vulnerability management** with defined patch cadence and scanning expectations.
- **Audit log generation, protection, and review** with retention.
- **Network segmentation** with explicit isolation of ePHI environments.
- **Contingency plan testing** on a defined cadence, not just a written plan.
- **Restoration drills** for systems that maintain ePHI.

The proposal also expressly contemplates AI, quantum computing, and virtual or augmented reality as emerging technologies the rule must accommodate. The mechanism is not technology-specific paragraphs. The mechanism is more rigorous risk analysis and asset-aware safeguards that can absorb new technology categories without amendment.

---

## Why This NPRM Is Different

Three structural shifts make this NPRM operationally different from past HIPAA changes.

The NPRM removes most of the "addressable vs. required" distinction. Specifications that were treated as risk-based in practice would become baseline expectations. Risk-based deviation would still be permitted, but as a documented and defensible exception, not as a default operating posture.

The NPRM aligns more tightly with NIST SP 800-66 Rev. 2 and SP 800-53 Rev. 5. Many of the proposed safeguards appear almost verbatim in those documents. NIST SP 800-66 Rev. 2 (Marron, 2024) is now the operational reference for translating Security Rule expectations into controls.

The NPRM aligns with active OCR enforcement. The Risk Analysis Initiative has produced multiple ransomware-related Security Rule settlements grounded in risk-analysis failures and information-system-activity monitoring failures. The NPRM is, in part, a codification of what OCR has already been enforcing.

---

## Mapping the NPRM to Existing Frameworks

Most organizations do not need to invent new controls to be NPRM-ready. They need to map existing controls to NPRM language so that one set of evidence answers multiple authorities. The cleanest crosswalk uses three anchors.

NIST SP 800-53 Revision 5 supplies the master control catalog. NPRM expectations land in identifiable families: AC for access control and MFA, AU for audit logging, CM for configuration and asset baselines, IR for incident response and contingency, RA for risk analysis, SC for segmentation and encryption, SI for vulnerability management, and SR for vendor and supply chain.

The HHS Healthcare and Public Health Cybersecurity Performance Goals (HPH CPGs) translate this into healthcare-specific Essential and Enhanced tiers. A customer that has already adopted Essential CPGs is materially aligned with the NPRM, and an Enhanced CPG posture covers most of the proposed safeguards.

CIS Controls v8 supplies the prioritized implementation layer. The first six controls — asset inventory, software inventory, data protection, secure configuration, account management, access control management — track directly to the NPRM's most prescriptive requirements.

Map once, evidence many. That is the only economically defensible posture for a small or mid-size healthcare organization.

---

## What to Build Now

Three streams of work pay off whether the final rule lands as proposed, softened, or hardened.

**Asset and data-flow inventory.** A unified asset register that includes ePHI systems, IoMT devices, cloud services, and APIs is the foundation for almost every NPRM safeguard. Without it, MFA scoping, encryption coverage, segmentation, and audit-log retention become guesses. With it, every other proposed control becomes scopable. NIST SP 800-213 supplies a defensible vocabulary for IoMT and connected-device entries (Fagan et al., 2021).

**Risk analysis evidence that survives a Risk Analysis Initiative inquiry.** OCR has settled multiple cases on risk-analysis deficiencies. A defensible risk analysis is dated, scoped to the actual ePHI environment, traces threats and vulnerabilities to specific systems, ties findings to a treatment plan, and is updated when the environment changes. NIST SP 800-30 Rev. 1 supplies the methodology and NIST SP 800-66 Rev. 2 supplies the HIPAA-specific application.

**Audit logging, segmentation, and contingency testing.** These are the three NPRM areas where most healthcare environments are weakest. Logs that nobody reviews, flat networks where ePHI sits next to lab equipment and HVAC, and contingency plans that have never been exercised are the most common Risk Analysis Initiative findings. Proving these capabilities now, in evidence rather than in policy, is the highest-leverage investment.

---

## What Not to Build Now

A proposed rule is not a final rule. Two categories of work should wait.

Do not buy point tools whose only justification is the NPRM's specific language. Encryption tooling, MFA enforcement, log aggregation, and segmentation all hold up under any plausible final rule. Tools that solve narrow NPRM-specific phrasing risk obsolescence if the final rule rewords or softens that phrase.

Do not commit to deadlines that the NPRM does not yet set. The final rule will set compliance dates that depend on entity size and safeguard category. Communicating internal deadlines as if those dates were fixed creates planning churn when the final rule shifts them.

The right framing: the NPRM is the most credible signal of the next decade of healthcare cybersecurity expectations. Build to the signal, not to the specific words that may still change.

---

## Why This Matters for Business Associates

The NPRM is not just a covered-entity rule. Business associates carry direct Security Rule liability under HITECH, and the NPRM proposes more explicit obligations on BA risk analysis, vendor flow-down, and verification.

For business associates, the NPRM raises the floor on what customers can require contractually. A BA that cannot produce a current asset inventory, MFA evidence, segmentation diagram, and log-retention proof will lose contracts to one that can. This is already happening in procurement reviews tied to Change Healthcare, and the NPRM will accelerate it.

See [Change Healthcare and Business Associate Risk](/blog/change-healthcare-supply-chain-risk-business-associates) for the BA-side framing.

---

## What to Track

Three signals will determine the NPRM's operational impact:

- The final rule's effective date and entity-size compliance windows.
- Whether OCR's Risk Analysis Initiative continues to produce settlements that anticipate the NPRM safeguards. The September 26, 2024 Cascade Eye and Skin Centers settlement ($250,000, two-year corrective action plan) is the clearest current signal.
- How the FTC Health Breach Notification Rule, ONC HTI-1, and state laws (notably Washington's My Health My Data Act) interact with the NPRM at the boundary of HIPAA-covered and non-HIPAA-covered health data.

The NPRM will not be the last regulatory change of this cycle. It is the most consequential one likely to land in 2026, and it will reshape what healthcare cybersecurity programs are expected to demonstrate.

---

## Sources

- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898. [govinfo.gov](https://www.govinfo.gov/content/pkg/FR-2025-01-06/pdf/2024-30983.pdf)
- Marron, J. (2024). *Implementing the HIPAA Security Rule* (NIST SP 800-66 Rev. 2). [doi.org/10.6028/NIST.SP.800-66r2](https://doi.org/10.6028/NIST.SP.800-66r2)
- HHS. (2024). *Healthcare and Public Health Cybersecurity Performance Goals*. [hphcyber.hhs.gov](https://hphcyber.hhs.gov/performance-goals.html)
- HHS Office for Civil Rights. (2024, September 26). *$250,000 Cascade Eye and Skin Centers ransomware settlement* [press release].
