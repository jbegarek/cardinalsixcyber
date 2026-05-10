---
title: "Post-Quantum Cryptography for Healthcare: Why Harvest-Now-Decrypt-Later Means You Start the Inventory Now"
description: "Quantum computing is a decade away. Long-lived health records are not. Here is why FIPS 203, 204, and 205 already shape healthcare procurement, and what to inventory first."
publishDate: 2026-05-12
author: "Justin T. Begarek"
lane: practical
topics:
  - Healthcare
  - Cryptography
  - NIST
  - Risk Management
  - Compliance
featured: false
draft: false
citations: false
diagrams: false
---

A cryptographically relevant quantum computer does not exist today. Most credible projections place it somewhere between 2030 and 2040. Healthcare leaders sometimes use this distance as a reason to defer post-quantum cryptography work.

That reasoning has a hole in it.

Adversaries do not need a quantum computer today to start exploiting one tomorrow. They need to capture encrypted data today and decrypt it once the capability exists. This is the harvest-now-decrypt-later (HNDL) threat. For healthcare, where medical records, genomic data, mental-health notes, and longitudinal cohort data remain sensitive for decades, the threat is not in 2035. The threat is in everything the adversary is recording right now.

This post explains why post-quantum cryptography is already a healthcare cybersecurity issue, what NIST has finalized, and how to build a defensible inventory and migration plan starting in 2026 without overcommitting to a specific timeline.

---

## What Changed in 2024

NIST finalized the first three post-quantum cryptographic standards on August 13, 2024:

- **FIPS 203** — ML-KEM, the primary key-encapsulation mechanism, derived from CRYSTALS-Kyber.
- **FIPS 204** — ML-DSA, the primary lattice-based digital signature, derived from CRYSTALS-Dilithium.
- **FIPS 205** — SLH-DSA, a hash-based backup digital signature, derived from SPHINCS+.

FIPS standards are mandatory for federal information systems under FISMA. They cascade into federal contractors through FedRAMP, DoD, and DFARS clauses. Healthcare entities are not directly required to use FIPS-validated cryptography by HIPAA today, but two adjacent forces are already producing PQC pressure:

The HIPAA Security Rule NPRM proposes more specific encryption requirements that, if finalized, would likely reference FIPS-validated modules (HHS, 2025).

National Security Memorandum 10 (NSM-10) directs federal agencies to transition national security systems to quantum-resistant cryptography "by 2035," with the NSA's Commercial National Security Algorithm Suite 2.0 specifying the exact algorithms (ML-KEM-1024, ML-DSA-87) for those systems.

The combined signal is unambiguous. Federal cryptographic policy is on a fixed migration path. Procurement, cyber insurance, and federal-adjacent customers are starting to ask vendors for PQC roadmaps. Healthcare is downstream, not exempt.

---

## Why HNDL Is a Healthcare Problem Specifically

The HNDL window is a function of two variables: how long the data remains sensitive, and how long it takes for cryptanalytically relevant quantum computers to emerge. Most data has a short sensitivity window — payment card data revolves on credit-card replacement cycles, transient identifiers expire, session tokens roll over.

Healthcare data does not behave that way.

A 35-year-old patient's mental-health note remains sensitive when they are 65. A genomic dataset never depreciates because genomes do not change. A pediatric oncology record has a 70-year sensitivity tail. Longitudinal research cohorts and substance-use treatment records carry similar long horizons. Defense-adjacent CUI handled by healthcare contractors retains confidentiality requirements far past collection.

The literature confirms this framing. SaberiKamarposhti et al. (2024) provide a peer-reviewed PQC roadmap specifically for medical data and identify integration, budget, interoperability, and training as the dominant adoption barriers. HHS Health Sector Cybersecurity Coordination Center (HC3) has published sector-specific guidance framing quantum cryptography as a near-term planning concern even though no healthcare-specific PQC mandate yet exists.

The point: an adversary who captures encrypted clinical traffic today, even traffic that uses today's strongest encryption, may decrypt a meaningful portion of it once a CRQC arrives. The cost of doing nothing now is paid in the 2030s in a currency healthcare cannot replenish.

---

## What to Inventory First

Most healthcare organizations will not migrate any cryptography in 2026. They will inventory it. The inventory is the foundation of every defensible PQC plan.

A useful cryptographic inventory captures four dimensions for each cryptographic dependency:

**Where the cryptography lives.** Applications, infrastructure (load balancers, VPNs, TLS terminators), endpoint devices, IoMT and connected medical devices, identity providers, code-signing pipelines, certificate authorities, hardware security modules, archival storage, and vendor SaaS that handles ePHI.

**What algorithms and key lengths are in use.** RSA-2048, ECDSA-P256, AES-256, SHA-256, and the protocol contexts (TLS 1.2, TLS 1.3, IPsec, S/MIME, CMS code signing).

**What data the cryptography protects, and how long that data must remain confidential.** A 30-year retention horizon implies a different urgency than a 90-day session token. NIST SP 800-57 Part 1 Rev. 5 (Barker, 2025) is the federal reference for these key-management decisions.

**Who owns the migration path.** In-house engineering owns code-signing pipelines and internal services. Vendors own SaaS encryption. Manufacturers own IoMT firmware. The inventory should record the decision boundary so vendor questionnaires can be scoped.

NIST SP 800-131A Rev. 3 (2025) is the operational complement to FIPS 203/204/205. It specifies acceptable, deprecated, and disallowed algorithms over time and is the federal mechanism for orderly cryptographic transition.

---

## Long-Lived Data Classification

The second artifact is a classification of long-lived sensitive datasets. This is not a HIPAA risk analysis and not a data-flow inventory. It is a narrower question: which datasets, if recorded encrypted today, would still be sensitive when an HNDL adversary could decrypt them?

The shortlist almost always includes:

- Mental-health, substance-use, and behavioral health records.
- Genomic and genetic test results.
- Pediatric records (long sensitivity tail by patient age).
- HIV, oncology, and reproductive-health data.
- Longitudinal research cohort data.
- CUI handled by healthcare-adjacent defense contractors.
- Long-retention claims data and provider credentialing records.

The classification informs which transport channels and storage tiers should migrate first. TLS-protected traffic that carries genomic data is a higher PQC priority than a session cookie on a public marketing site.

---

## Vendor PQC Questionnaires

The third artifact is a vendor questionnaire. Healthcare's PQC migration is overwhelmingly a vendor migration — EHR vendors, cloud providers, identity providers, CA vendors, HSM vendors, and IoMT manufacturers control most of the cryptographic surface.

Defensible questions to add to vendor reviews:

- What is your published roadmap for adopting FIPS 203, 204, and 205?
- Do you support hybrid algorithms (classical + PQC) in TLS or other protocols today?
- How do your code-signing and certificate authority chains plan to migrate?
- What is your timeline for offering PQC-capable hardware (HSMs, smartcards, embedded device firmware)?
- Will you contractually commit to a PQC migration date that aligns with our long-lived data classification?

NIST SP 800-161 Rev. 1 (Boyens et al., 2022) provides the supply-chain risk management framing that makes these questions defensible rather than speculative.

---

## What Not to Build Now

Three categories of work are premature in 2026.

**Do not migrate production cryptography to a single PQC algorithm yet.** ML-KEM and ML-DSA are the primary federal selections, but cryptographic agility — the ability to swap algorithms — is more valuable today than algorithm choice. SLH-DSA exists as a backup for exactly this reason: cryptographic diversity hedges against algorithm-specific failures.

**Do not promise customers a fixed PQC migration date.** Healthcare PQC timelines will be set by federal cryptographic transition cascading through FedRAMP, DoD, and procurement, plus the eventual HIPAA Security Rule final rule. Committing to dates ahead of those signals creates churn.

**Do not buy quantum-resistant tooling for environments that do not yet protect long-lived data.** A genomic data lake warrants early action. A marketing analytics platform does not.

The right posture for 2026: inventory, classify, ask, design. Migration runs on a 2027 to 2035 horizon for most healthcare environments and tracks federal cryptographic transition rather than leading it.

---

## How This Connects to the HIPAA NPRM

The HIPAA Security Rule NPRM proposes more specific encryption requirements and expressly contemplates quantum computing as an emerging issue (HHS, 2025). The proposed rule does not mandate FIPS 203/204/205 by name today, but the rule's direction is unmistakable. A healthcare organization with a current cryptographic inventory and a documented PQC roadmap is materially aligned with where the rule is going. An organization without those artifacts will inherit a rushed transition under whatever deadline the final rule sets.

See [The HIPAA Security Rule NPRM: A Control Roadmap](/blog/hipaa-security-rule-nprm-control-roadmap) for the broader NPRM context.

---

## Sources

- NIST. (2024). *FIPS 203, ML-KEM*. [doi.org/10.6028/NIST.FIPS.203](https://doi.org/10.6028/NIST.FIPS.203)
- NIST. (2024). *FIPS 204, ML-DSA*. [doi.org/10.6028/NIST.FIPS.204](https://doi.org/10.6028/NIST.FIPS.204)
- NIST. (2024). *FIPS 205, SLH-DSA*. [doi.org/10.6028/NIST.FIPS.205](https://doi.org/10.6028/NIST.FIPS.205)
- Barker, E. (2025). *NIST SP 800-57 Pt. 1 Rev. 5*. [doi.org/10.6028/NIST.SP.800-57pt1r5](https://doi.org/10.6028/NIST.SP.800-57pt1r5)
- NIST. (2025). *NIST SP 800-131A Rev. 3*. [doi.org/10.6028/NIST.SP.800-131Ar3](https://doi.org/10.6028/NIST.SP.800-131Ar3)
- SaberiKamarposhti et al. (2024). Post-quantum healthcare. *Heliyon, 10*(10), e31406.
- HHS HC3. (2022). *Quantum cryptography and the health sector*.
- The White House. (2022). *NSM-10*.
