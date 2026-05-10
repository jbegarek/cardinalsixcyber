---
title: "Reading the Compliance Status Legend: Why 'Emerging' Is a Useless Tag"
description: "Final, final guidance, voluntary, contractually binding, proposed, enacted-not-yet-effective, vacated. The legal weight of a rule changes everything about how you should treat it."
publishDate: 2026-05-10
author: "Justin T. Begarek"
lane: practical
topics:
  - Healthcare
  - Compliance
  - Strategy
  - HIPAA
  - Risk Management
featured: false
draft: false
citations: false
diagrams: false
---

A 2026 healthcare cybersecurity program operates against a regulatory environment that includes binding rules, nonbinding final guidance, voluntary frameworks, contractually flowed-down standards, proposed rulemakings, enacted-but-not-yet-effective state laws, phased international regulations, and rules that were briefly effective and have been vacated. Most lists of "emerging" requirements collapse all of these into one category and, in doing so, mislead the people responsible for prioritizing work.

The status of a compliance instrument changes how you should treat it. A proposed rule cannot be enforced. A final rule can. A vacated rule no longer exists. A voluntary framework cannot fine you, but it can lose you a contract. Conflating these categories produces both wasted work (preparing for vacated rules) and dangerous gaps (treating proposed rules as already binding and assuming you do not need to track final ones).

This post walks through a seven-category status legend, why each category warrants a different operational response, and how to apply it to the actual healthcare instruments in play in 2026.

---

## The Seven Categories

The legend below is the one Cardinal Six uses internally for healthcare compliance tracking. Other organizations use simpler legends, but seven categories is the smallest set that does not erase legally meaningful differences.

**Final / Effective binding law.** A regulation, statute, or rule that is currently effective and enforceable. Examples: the HIPAA Security Rule (45 CFR Parts 160, 162, 164), DFARS 252.204-7012, the 32 CFR Part 170 CMMC Program Rule, the 48 CFR DFARS rule effective November 10, 2025, the FTC Health Breach Notification Rule amendments effective July 29, 2024, ONC HTI-1 effective March 11, 2024, the SEC cybersecurity disclosure rule.

**Final Guidance (nonbinding, persuasive).** Final agency guidance that does not itself impose obligations but operationalizes the agency's interpretation of binding rules. Examples: FDA's 2026 medical-device cybersecurity guidance, FDA's 2025 PCCP guidance for AI-enabled device software, NIST SP 800-66 Rev. 2 HIPAA implementation guide.

**Voluntary Framework.** Federal or industry frameworks that are voluntary by design but increasingly cited by procurement, insurers, and regulators. Examples: NIST CSF 2.0, NIST AI RMF 1.0, NIST Generative AI Profile, HHS Healthcare and Public Health Cybersecurity Performance Goals, CISA Cross-Sector Cybersecurity Performance Goals v2.0, CIS Controls v8.

**Contractually Binding when Incorporated.** Standards that are voluntary in general but become binding through contract, procurement clause, or sector-specific incorporation. Examples: NIST SP 800-171 Rev. 3 (binding when DFARS 7012 or CMMC scopes apply), FIPS 203/204/205 (binding for federal information systems and cascading to contractors via FedRAMP and DFARS), NIST SP 800-218 SSDF (binding inside EO 14028 federal-software attestations).

**Proposed.** Published as a Notice of Proposed Rulemaking or equivalent. Cannot be enforced and may not finalize as written. Examples: HIPAA Security Rule NPRM (90 Fed. Reg. 898), CIRCIA Reporting Requirements NPRM (89 Fed. Reg. 23644).

**Enacted but not yet Effective.** Passed or finalized with future compliance dates. Compliance work can begin, but enforcement does not start until the effective date. Examples: Colorado AI Act per SB 24-205 and SB 25B-004, effective June 30, 2026; EU AI Act high-risk obligations under Article 6(1), applicable August 2, 2027.

**Vacated, stayed, or rescinded.** Once-effective rules that have been removed in whole or in part. Examples: the 2024 HIPAA reproductive-health privacy rule, mostly vacated nationwide on June 18, 2025 in *Carmen Purl, et al. v. U.S. Department of Health and Human Services* (N.D. Tex.). Executive Order 14110 (October 30, 2023) was revoked on January 23, 2025 by EO 14179.

---

## Why The Distinction Matters Operationally

A team that reads "HIPAA NPRM, FIPS 203, EU AI Act, Colorado AI Act, CIRCIA, FTC HBNR" as one undifferentiated list will allocate effort wrong in three predictable ways.

**They will under-prepare for proposed rules.** Proposed rules cannot be enforced today, so the temptation is to defer the work. But proposed rules with strong agency signal — like the HIPAA Security Rule NPRM and CIRCIA — almost always finalize within one to three years, and finalization sets compliance windows that may be shorter than the work. Map evidence to proposed rules now, knowing that the language may shift before finalization.

**They will over-commit to vacated rules.** A team that built reproductive-health privacy training in 2024 around the now-vacated rule wasted that investment. A team that confuses the vacated rule with the still-effective HIPAA Privacy Rule generally will produce contradictory training. Vacated rules need a written retirement step, not silence.

**They will treat voluntary frameworks as discretionary.** NIST CSF 2.0 is voluntary, but HHS HPH CPGs that align to it are increasingly required by customer contracts and cited by OCR enforcement. Voluntary at the federal level is often required at the contract level. Treating "voluntary" as "optional" is how procurement reviews surface gaps that did not exist last year.

The status legend is a forcing function. It makes a team explicitly classify each instrument, which exposes assumptions that would otherwise hide.

---

## A Concrete Example: AI Compliance

The current AI compliance stack illustrates every category at once.

- NIST AI RMF and Generative AI Profile: **voluntary framework**.
- FDA PCCP guidance: **final guidance** (nonbinding, persuasive).
- ONC HTI-1: **final / effective binding law**.
- HIPAA Security Rule NPRM (the AI-relevant safeguards): **proposed**.
- EU AI Act prohibitions: **final / effective binding law** (since February 2, 2025).
- EU AI Act high-risk Article 6(1) obligations: **enacted but not yet effective** (August 2, 2027).
- Colorado AI Act: **enacted but not yet effective** (June 30, 2026).

A "list of AI compliance requirements" that fails to distinguish these is not a useful artifact. The list of evidence the team should produce now to satisfy them differs by category. NIST AI RMF inputs are voluntary but should anchor any defensible AI program because procurement will ask. FDA PCCP applies to AI-enabled medical devices today. ONC HTI-1 must be in production for certified health IT. The HIPAA NPRM AI-relevant safeguards should be mapped now but not enforced internally as if final. EU prohibitions apply now; high-risk obligations have a planning window. Colorado has a planning window with a hard date.

The same logic applies to PQC, IoMT, and cloud/API compliance. The cost of running compliance without a status legend is paid in misallocation that may not be visible until an audit or procurement review.

---

## Where Status Information Lives

The most reliable status sources are also the most authoritative sources. For healthcare:

- **HIPAA NPRM and final rule status.** HHS press releases and the Federal Register.
- **CIRCIA status.** The CISA CIRCIA status page (cisa.gov/circia), which CISA updates as the rulemaking progresses.
- **CMMC status.** DoD CIO CMMC page and the Federal Register for the 32 CFR Part 170 and 48 CFR DFARS rules.
- **FDA AI and cyber-device guidance.** FDA's media library and the FDA-TRACK program.
- **State AI laws.** State legislative records (e.g., the Colorado General Assembly bill page for SB 24-205 and SB 25B-004) rather than law-firm summaries.
- **EU AI Act phased applicability.** Article 113 of Regulation (EU) 2024/1689 itself, not third-party summaries.
- **Vacatur and litigation.** Federal court dockets and the issuing agency's authoritative statement (e.g., HHS's own Reproductive Health page acknowledging *Purl v. HHS*).

A compliance intelligence function reviews these sources on a defined cadence and updates the team's tracker. NIST SP 800-137 (Dempsey et al., 2011) supplies the continuous-monitoring frame; CSF 2.0 Govern function (NIST, 2024d) supplies the organizational accountability.

---

## What Not to Do

Three habits create the most damage in healthcare compliance tracking.

**Citing "guidance" without specifying which kind.** "FDA guidance," "HHS guidance," and "OCR guidance" cover a range from final binding rules to informal blog posts. Specify which document, which date, which status.

**Citing "the rule" when the rule has been amended.** SB 24-205 alone misstates the Colorado AI Act effective date; the citation needs SB 25B-004 alongside it. The HIPAA Security Rule citation alone misses the NPRM-driven anticipated changes; the NPRM citation alone misses the still-effective 2003-era rule. Pair citations when both matter.

**Citing law-firm aggregations as primary sources.** Law-firm summaries are useful navigational aids and dangerous citation targets. The compendium behind this post records every primary source's URL and DOI so claims do not depend on secondary summaries.

---

## What to Track

A small healthcare cybersecurity team should maintain a simple tracker with one row per instrument and columns for status category, effective date (or proposed date), last reviewed, owner, and customer impact. A monthly review of the tracker, with a quarterly direction-setting memo, is enough to keep the legend current. NIST SP 800-137 and CSF 2.0 Govern supply the federal frame; the discipline is in the cadence.

The legend is not glamorous. It is also the difference between a compliance program that absorbs change and a compliance program that gets surprised by it.

---

## Sources

- HHS. (2025). *HIPAA Security Rule NPRM*. 90 Fed. Reg. 898.
- CISA. (2024). *CIRCIA NPRM*. 89 Fed. Reg. 23644; (2026) *CIRCIA status page*.
- DoD. (2024). *32 CFR Part 170 CMMC Program Rule*; (2025) *48 CFR DFARS rule*.
- FTC. (2024). *Health Breach Notification Rule Final Amendments*. 89 Fed. Reg. 47028.
- ONC. (2024). *HTI-1 Final Rule*. 89 Fed. Reg. 1192.
- NIST. (2024). *Cybersecurity Framework 2.0* (CSWP 29).
- European Parliament and Council. (2024). *Regulation (EU) 2024/1689 (AI Act)*, art. 113.
- Colorado General Assembly. (2024). *SB 24-205*; (2025) *SB 25B-004*.
- Dempsey et al. (2011). *NIST SP 800-137*.
- *Carmen Purl, et al. v. HHS*, No. 2:24-cv-00228-Z (N.D. Tex. June 18, 2025).
