---
title: "NIST SP 800-171 Revision 3 Is Published. Your CMMC Assessment Still Uses Revision 2."
description: "CMMC 2.0 and DFARS 252.204-7012 still point to Revision 2. NIST published Revision 3 in May 2024. Here is what the version gap means for contractors currently building their SSP, preparing for C3PAO assessment, or planning a multi-year compliance roadmap."
publishDate: 2026-04-19
author: "Justin T. Begarek"
lane: practical
topics:
  - CMMC
  - NIST
  - Compliance
  - DIB
featured: false
draft: false
citations: false
diagrams: false
---

The DFARS clause stack and the CMMC Final Rule at 32 C.F.R. Part 170 both point to NIST SP 800-171 Revision 2 as the technical baseline for defense contractor assessments. NIST published Revision 3 in May 2024. DoD has not updated the regulation to reflect it.

That version gap is not a paperwork technicality. It affects what controls a Certified Third-Party Assessment Organization (C3PAO) will measure you against, how you should build your System Security Plan, and what compliance planning looks like across a three-year assessment cycle. If you are implementing Revision 3 controls because your security team judged them stronger, you may be doing work that is not yet assessed — and missing credit for work you have already done under Revision 2.

This post explains the structural reason the gap exists, what changed between revisions, and what it means for contractors operating under DFARS today.

---

## Why the Gap Exists: Static Incorporation by Reference

Federal regulations do not update automatically when NIST publishes new guidance. DFARS 252.204-7012, the clause that requires contractors handling Covered Defense Information to implement NIST SP 800-171, incorporates specific published versions of NIST standards. When NIST releases a revision, that revision does not become binding on contractors until DoD amends the regulation.

This is a structural feature of how technical standards enter the federal regulatory system, not a mistake. It gives DoD control over when a new baseline takes effect and allows time for the contractor ecosystem to adapt. The problem is that the process is slow relative to how quickly NIST updates its guidance.

The May 2024 DoD OIG advisory put the implementation lag in concrete terms for a related standard: DoD itself was not expected to complete full deployment of NIST SP 800-53 Revision 5 until 2026 — six years after NIST published it. The compliance expectation for contractors through DFARS often outruns the government's own implementation capacity.

With NIST SP 800-171, the CMMC Final Rule codified at 32 C.F.R. Part 170 specifically references Revision 2 as the control baseline for Level 2 assessments. Until DoD amends the rule through rulemaking, Revision 2 is what counts for CMMC purposes.

---

## What Changed in Revision 3

Revision 3 is not a minor housekeeping update. The changes are substantive enough that contractors who implement it directly will find meaningful structural differences from what their C3PAO will assess.

**Control family reorganization.** Revision 2 has 14 control families covering 110 requirements. Revision 3 reorganizes those same functional areas but restructures how controls are grouped and labeled. The mapping between revisions is not always one-to-one.

**Supply chain and software integrity additions.** Revision 3 adds new requirements focused on software supply chain integrity and third-party component security — areas that were treated lightly in Revision 2 but gained regulatory attention after EO 14028 and subsequent guidance. Contractors operating under Rev 2 have no formal CMMC requirement to implement these controls yet.

**Organization-defined parameters.** Revision 3 introduces more organization-defined parameters in control statements, giving organizations more discretion in how certain controls are implemented. This is a departure from the more prescriptive framing in Revision 2 and will affect how C3PAOs eventually score implementation.

**Alignment with NIST SP 800-53 Rev 5.** NIST SP 800-171 derives from SP 800-53. Revision 3 reflects the updated parent standard's structure more closely, which means federal contractors who must comply with both frameworks will eventually see better alignment — but only once DFARS catches up to Rev 3.

---

## What This Means If You Are Preparing for Assessment Now

If your C3PAO assessment is scheduled within the next 12 to 18 months, you will be assessed against Revision 2. That is the baseline in the regulation. The practical implications:

**Your SSP should map to Revision 2.** A System Security Plan built around Revision 3's control structure may be harder to score and may not clearly demonstrate compliance with the 110 Rev 2 requirements. Build your SSP to Revision 2 and document it as such. If you have implemented controls that exceed Rev 2 requirements, note them — but do not use Rev 3 numbering as your primary reference.

**Revision 3 controls are not assessed, but not penalized.** Implementing stronger controls from Revision 3 does not hurt your CMMC score. You simply will not receive credit for controls that have no Rev 2 equivalent. If your organization has security reasons to implement Rev 3 additions, do it — just do not count on those controls to satisfy Rev 2 requirements that do not exist in Rev 3.

**SPRS scoring still uses Rev 2.** Your Supplier Performance Risk System score is a self-assessment of NIST SP 800-171 Rev 2 implementation against DoD's methodology. Revision 3 practices that have no direct Rev 2 equivalent do not factor into SPRS. If your score reflects controls you have implemented but mapped only to Rev 3, revisit your scoring documentation.

**Plan for a transition when DFARS updates.** DoD will eventually amend the regulation to incorporate Revision 3. When that happens, there will be a transition period, but the implementation burden will be real — particularly for the new supply chain and software integrity requirements. Contractors who understand what Rev 3 adds now will have a shorter ramp-up when the rule changes.

---

## The Assessor Capacity Problem Running in Parallel

The version gap is one compliance planning issue. A second one compounds it: the C3PAO assessor market has not scaled to meet projected demand.

CMMC Level 2 requires most contractors handling Controlled Unclassified Information to obtain a triennial third-party assessment from an accredited C3PAO. The Cybersecurity Maturity Model Certification Accreditation Body (Cyber AB) accredits these organizations. The available C3PAO count and assessor throughput lag the estimated number of contractors who will need Level 2 certification once CMMC is fully phased in.

For small defense industrial base contractors, this creates two compounding problems. First, certification timelines may extend beyond what a solicitation requires, creating award eligibility risk. Second, assessment costs — estimated by DoD in its regulatory impact analysis at several hundred thousand dollars for a mid-size organization — are a meaningful market-entry barrier. DoD estimated roughly $4 billion in ten-year industry compliance costs across the DIB.

The practical implication: do not assume you can schedule a C3PAO assessment when you want one. The assessor ecosystem is developing, but contractors who wait until a solicitation requires CMMC certification before engaging an assessor may find their timeline constrained by market availability, not just their own readiness.

---

## Planning Across Both the Version Gap and the Phase-In Schedule

CMMC's phased implementation means not every contract requires certification immediately. Phase 1, which began with the Final Rule's effective date, allows Level 1 and Level 2 self-assessments in solicitations that include DFARS 252.204-7021. Third-party assessments for Level 2 become broadly required as DoD phases them in over the four-phase schedule described in 32 C.F.R. Part 170.

Against that backdrop, a reasonable compliance posture:

**Near term (pre-assessment):** Implement and document Revision 2 controls. Complete your SPRS self-assessment. Close critical gaps. Engage a C3PAO early if you anticipate a solicitation with CMMC Level 2 requirements.

**During assessment:** Be prepared to demonstrate Revision 2 implementation. Your evidence and SSP should map clearly to Rev 2 control families and requirements. Do not expect assessors to accept Rev 3 mappings as substitutes.

**Medium term (post-assessment):** Track DFARS rulemaking for the Revision 3 update. When the proposed rule publishes, read the transition provisions carefully. The implementation requirements and timelines will be in the rule. Organizations that understand Rev 3 now will be able to gap-assess quickly once the requirement becomes formal.

---

## The Larger Structural Problem

The version gap between NIST SP 800-171 Rev 2 and Rev 3 is one instance of a broader problem: federal cybersecurity law incorporates technical standards statically, while the technical environment evolves continuously. Once DFARS locks in a NIST revision, contractors and DoD alike are bound to that baseline until rulemaking changes it. NIST updates its guidance on a schedule driven by the threat landscape. The regulatory update cycle does not match.

This creates a persistent misalignment in which contractors may be implementing outdated controls because the regulation has not caught up, while simultaneously facing compliance obligations tied to standards that their own security programs have already surpassed. Managing that gap requires tracking both what the regulation currently requires and what NIST guidance says, and being clear about which baseline governs your formal compliance obligations.

For the broader legal framework that produces this problem — including how FISMA, DFARS, and CIRCIA interact across DoD, CISA, and critical infrastructure sectors — see [Federal Cybersecurity Law and the Defense Industrial Base](/blog/federal-cybersecurity-law-dib-fragmentation).

For the CMMC level structure and assessment mechanics, see [CMMC 2.0 Levels, Assessment Paths, and What Certification Actually Costs](/blog/cmmc-2-levels-assessment-cost).

For the specific DFARS clause requirements that flow from these standards, see [The DFARS Clause Stack: 7012, 7019, 7020, and 7021 Explained](/blog/dfars-clause-stack-7012-7019-7020-7021).

---

*Justin T. Begarek is an IT Cybersecurity Specialist and PhD candidate in Cybersecurity. This analysis reflects the author's independent research and academic work.*
