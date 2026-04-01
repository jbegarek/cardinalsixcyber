#!/usr/bin/env python3
"""
seed-glossary-data.py — Cardinal Six Cyber glossary data seeder.

Generates data/glossary.json containing 250+ cybersecurity glossary terms
with definitions written for non-technical business owners, related resources
cross-linked from CMMC practices, NIST 800-171 requirements, and NIST 800-53
controls.

Usage:
    python scripts/seed-glossary-data.py
"""

import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")


def slug(term: str) -> str:
    """Convert a term to a URL-safe slug."""
    # Remove special chars except hyphens and spaces, keep alphanumeric
    s = term.lower()
    # Strip content in parentheses but keep abbreviation text
    # e.g., "Authority to Operate (ATO)" -> "authority-to-operate-ato"
    s = re.sub(r"[()]", " ", s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


# ---------------------------------------------------------------------------
# All glossary terms
# ---------------------------------------------------------------------------
TERMS = [
    # ===== CMMC Terms (~35) =====
    {
        "term": "CMMC",
        "definition": "<p>The Cybersecurity Maturity Model Certification (CMMC) is the Department of Defense's framework for verifying that defense contractors have adequate cybersecurity protections in place before they can win or keep DoD contracts. Think of it as a cybersecurity inspection program — the DoD wants proof that your company protects sensitive information, not just a promise.</p><p>CMMC replaced the old system where contractors could simply self-certify their security. Now, depending on the sensitivity of data you handle, you may need an independent third-party assessor to verify your protections. The framework has three levels, each requiring progressively stronger security measures.</p><p>For most small and mid-size defense contractors, CMMC Level 2 is the target — it aligns with the 110 security requirements in NIST SP 800-171 and covers the protection of Controlled Unclassified Information (CUI).</p>",
        "whyItMatters": "<p>If you hold or pursue DoD contracts that involve CUI, you will need CMMC certification to remain eligible. Without it, you risk losing existing work and being disqualified from future contract opportunities.</p>",
    },
    {
        "term": "Controlled Unclassified Information (CUI)",
        "definition": "<p>Controlled Unclassified Information, or CUI, is sensitive government information that isn't classified (not Secret or Top Secret) but still requires protection. Examples include technical drawings, engineering data, export-controlled information, personnel records, and contract performance data that the government shares with contractors.</p><p>CUI is marked or designated by the government and must be handled according to specific rules. If your company receives information marked as CUI, you're legally obligated to protect it — storing it securely, limiting who can access it, and ensuring it isn't leaked or stolen.</p><p>The entire CMMC framework exists primarily to protect CUI. If you handle CUI, you need CMMC Level 2 certification, which requires implementing all 110 security requirements from NIST SP 800-171.</p>",
        "whyItMatters": "<p>Understanding what CUI is and whether your company handles it determines your entire CMMC compliance path. Misidentifying or failing to protect CUI can lead to contract loss, financial penalties, and potential legal liability under the False Claims Act.</p>",
    },
    {
        "term": "Federal Contract Information (FCI)",
        "definition": "<p>Federal Contract Information (FCI) is information provided by or generated for the government under a contract that is not intended for public release. It's a step below CUI in sensitivity — think of routine contract correspondence, delivery schedules, and basic project management data that the government doesn't want published but that isn't formally designated as CUI.</p><p>FCI requires a baseline level of protection under CMMC Level 1, which involves 15 fundamental cybersecurity practices like using passwords, limiting physical access, and keeping antivirus software current. These are basic hygiene measures that most businesses should already have in place.</p>",
        "whyItMatters": "<p>If your contracts involve only FCI (no CUI), you qualify for the simpler CMMC Level 1 self-assessment path. Correctly determining whether you handle FCI versus CUI is critical for scoping your compliance effort and budget.</p>",
    },
    {
        "term": "System Security Plan (SSP)",
        "definition": "<p>A System Security Plan (SSP) is a formal document that describes how your company's information systems are set up and what security measures are in place to protect sensitive data. Think of it as the master blueprint of your cybersecurity program — it documents every security control, who is responsible for it, and how it works in your specific environment.</p><p>The SSP covers your network architecture, hardware and software inventory, user access policies, data flow diagrams, and the specific steps you take to meet each security requirement. For CMMC, your SSP must address all applicable NIST SP 800-171 requirements and accurately describe your current security posture.</p><p>Assessors will use your SSP as their primary reference during a CMMC assessment. If your SSP doesn't match reality — if it says you do something you actually don't — that's a finding that can prevent certification.</p>",
        "whyItMatters": "<p>Your SSP is the single most important document in your CMMC journey. It must be accurate, complete, and kept up to date. A poorly written or inaccurate SSP will derail your assessment before it even begins.</p>",
    },
    {
        "term": "Plan of Action and Milestones (POA&M)",
        "definition": "<p>A Plan of Action and Milestones (POA&M, sometimes written POAM) is a document that lists the security weaknesses or gaps your company knows about but hasn't fully fixed yet, along with your plan and timeline for addressing each one. It's essentially your remediation to-do list with deadlines.</p><p>When you identify a security requirement you don't fully meet — say you haven't implemented multi-factor authentication everywhere — the POA&M records that gap, describes what you plan to do about it, who is responsible, and when it will be completed. Under CMMC 2.0, some POA&M items are allowed at the time of assessment, but they must be closed within 180 days.</p>",
        "whyItMatters": "<p>A well-maintained POA&M shows assessors that you're aware of your gaps and actively working to close them. However, not all gaps can be POA&M'd — certain critical requirements must be fully met at the time of assessment.</p>",
    },
    {
        "term": "POAM",
        "definition": "<p>POAM is a common shorthand for Plan of Action and Milestones (POA&M). It refers to the same document — a formal tracking list of known security gaps, the planned remediation steps, responsible parties, and target completion dates.</p><p>You'll see both \"POAM\" and \"POA&M\" used interchangeably in DoD and cybersecurity contexts. The document serves as your roadmap for closing security gaps and demonstrating continuous improvement to assessors and auditors.</p>",
        "whyItMatters": "<p>Whether written as POAM or POA&M, this document is mandatory for CMMC compliance. Having a realistic, well-managed POAM with achievable deadlines demonstrates organizational maturity and commitment to security.</p>",
    },
    {
        "term": "C3PAO",
        "definition": "<p>A C3PAO (CMMC Third-Party Assessment Organization) is an independent company authorized by the CyberAB to conduct official CMMC assessments of defense contractors. Think of them as the certified inspectors — they send assessors to your company to verify that your cybersecurity practices actually meet CMMC requirements.</p><p>C3PAOs must themselves be certified and meet rigorous standards. They employ trained CMMC assessors who review your documentation, interview your staff, and test your systems to verify compliance. You choose and hire your own C3PAO, but they work independently — their job is to give an honest assessment, not to help you pass.</p>",
        "whyItMatters": "<p>For CMMC Level 2 certification, you must engage a C3PAO. Selecting the right one and being fully prepared before they arrive can save significant time and money — failed assessments mean starting over.</p>",
    },
    {
        "term": "CMMC-AB",
        "definition": "<p>CMMC-AB was the original name for the CMMC Accreditation Body, the organization responsible for overseeing the CMMC ecosystem including training assessors and accrediting C3PAOs. It has since been renamed to the CyberAB (Cyber Accreditation Body).</p><p>The CyberAB manages the marketplace of authorized assessors and assessment organizations, maintains training and certification standards for CMMC professionals, and operates the CMMC ecosystem on behalf of the Department of Defense.</p>",
        "whyItMatters": "<p>Understanding who governs the CMMC ecosystem helps you identify legitimate assessors and training providers versus unaccredited organizations. Always verify that your C3PAO is listed on the CyberAB marketplace.</p>",
    },
    {
        "term": "CyberAB",
        "definition": "<p>The CyberAB (Cyber Accreditation Body) is the organization authorized by the Department of Defense to manage the CMMC assessment ecosystem. They accredit the C3PAOs that perform assessments, certify individual assessors, and maintain the official marketplace where you can find authorized assessment organizations.</p><p>Previously known as the CMMC-AB, the CyberAB ensures quality and consistency across all CMMC assessments. They set the standards for assessor training, manage conflicts of interest, and provide oversight of the entire certification process.</p>",
        "whyItMatters": "<p>The CyberAB marketplace is your authoritative source for finding legitimate C3PAOs and certified CMMC professionals. Using their directory protects you from unqualified consultants claiming to offer CMMC assessments.</p>",
    },
    {
        "term": "DIBCAC",
        "definition": "<p>DIBCAC stands for the Defense Industrial Base Cybersecurity Assessment Center. It's the DoD organization within DCMA (Defense Contract Management Agency) responsible for conducting high-level CMMC assessments — specifically, CMMC Level 3 (expert) assessments and oversight of the overall CMMC assessment process.</p><p>While C3PAOs handle Level 2 assessments, DIBCAC conducts the Level 3 assessments directly. DIBCAC also performs DCMA DIBCAC High assessments of contractors' cybersecurity programs and has the authority to verify that contractors are meeting their cybersecurity obligations.</p>",
        "whyItMatters": "<p>If your contracts require CMMC Level 3 or if you're subject to DCMA oversight, DIBCAC will be directly involved in your assessment. Understanding their role helps you prepare for the highest tier of DoD cybersecurity scrutiny.</p>",
    },
    {
        "term": "Organization Seeking Certification (OSC)",
        "definition": "<p>An Organization Seeking Certification (OSC) is the formal CMMC term for a company that is going through the CMMC assessment process. If you're a defense contractor preparing for or undergoing a CMMC assessment, you are the OSC.</p><p>The term is used in official CMMC documentation and assessment guides to distinguish between the company being assessed and the organizations performing or overseeing the assessment (C3PAOs, CyberAB, DIBCAC).</p>",
        "whyItMatters": "<p>Knowing this terminology helps you navigate CMMC documentation and assessment procedures. When guides and policies reference the 'OSC,' they're talking about your company and your responsibilities in the certification process.</p>",
    },
    {
        "term": "SPRS",
        "definition": "<p>SPRS (Supplier Performance Risk System) is the DoD's online system where defense contractors submit their cybersecurity self-assessment scores. When you evaluate your company against the 110 NIST SP 800-171 requirements and calculate a score (ranging from -203 to 110), you enter that score into SPRS.</p><p>Contracting officers check your SPRS score before awarding contracts. A perfect score of 110 means you fully meet all requirements. Most companies start well below that and use a POA&M to track their path to full compliance. Your SPRS score, along with the date of your assessment and a brief description of your system, must be current and accurate.</p>",
        "whyItMatters": "<p>Your SPRS score is visible to every contracting officer evaluating your proposals. A low or missing score can disqualify you from contract awards, while an inflated score carries False Claims Act risk if the DoD audits your actual implementation.</p>",
    },
    {
        "term": "CMMC Level 1",
        "definition": "<p>CMMC Level 1 is the foundational tier of the Cybersecurity Maturity Model Certification. It requires implementing 15 basic cybersecurity practices drawn from FAR 52.204-21, covering fundamental protections like using passwords, installing antivirus software, and limiting physical access to systems.</p><p>Level 1 applies to contractors who handle Federal Contract Information (FCI) but not Controlled Unclassified Information (CUI). It can be satisfied through an annual self-assessment — no third-party assessor is required. The practices are basic security hygiene that most businesses should already follow.</p>",
        "whyItMatters": "<p>If your contracts only involve FCI, Level 1 is your target. The self-assessment path keeps costs low, but you must still document compliance and submit your results to SPRS annually.</p>",
    },
    {
        "term": "CMMC Level 2",
        "definition": "<p>CMMC Level 2 is the middle tier and the most common target for defense contractors. It requires implementing all 110 security requirements from NIST SP 800-171, covering areas like access control, incident response, system protection, and audit logging.</p><p>Level 2 applies to contractors who handle Controlled Unclassified Information (CUI). Depending on the contract, you may need either a self-assessment or a third-party assessment by a C3PAO. The third-party assessment path is more rigorous and results in a formal certification valid for three years.</p>",
        "whyItMatters": "<p>Level 2 is where most defense contractors will land. Achieving certification requires significant investment in security controls, documentation, and organizational change — starting early gives you the best chance of passing your assessment on the first attempt.</p>",
    },
    {
        "term": "CMMC Level 3",
        "definition": "<p>CMMC Level 3 is the highest tier, designed for contractors handling the most sensitive CUI where Advanced Persistent Threats (APTs) are a significant concern. It builds on Level 2 by adding enhanced security requirements drawn from NIST SP 800-172.</p><p>Level 3 assessments are conducted by DIBCAC (the government itself), not by C3PAOs. This level applies to a relatively small number of contractors working on the most sensitive defense programs. The additional requirements focus on advanced threat detection, incident response, and security architecture.</p>",
        "whyItMatters": "<p>Most contractors will not need Level 3, but if your contracts involve critical programs or highly sensitive CUI, you should understand that this level requires government-led assessment and significantly more advanced security capabilities.</p>",
    },
    {
        "term": "Self-Assessment",
        "definition": "<p>A self-assessment in the CMMC context means your company evaluates its own cybersecurity practices against the required security controls without an external assessor. For CMMC Level 1, self-assessment is the standard path. For some Level 2 scenarios, self-assessment may also be permitted depending on the contract requirements.</p><p>Self-assessment doesn't mean casual or optional — you must rigorously evaluate each requirement, document your findings, calculate your SPRS score, and submit the results. A senior company official must affirm the accuracy of the assessment, creating personal accountability.</p>",
        "whyItMatters": "<p>Self-assessment reduces costs compared to third-party assessment, but it carries the same legal obligations for accuracy. Submitting a false or inflated self-assessment score to SPRS can trigger False Claims Act liability.</p>",
    },
    {
        "term": "Third-Party Assessment",
        "definition": "<p>A third-party assessment is an independent evaluation of your cybersecurity practices conducted by a C3PAO — an organization authorized by the CyberAB to perform CMMC assessments. The C3PAO sends trained assessors to review your documentation, interview your team, and verify that your security controls are properly implemented and effective.</p><p>This is required for CMMC Level 2 when the contract involves prioritized CUI, and for all Level 3 assessments (conducted by DIBCAC). The assessment results in a formal certification that is valid for three years, after which you must be reassessed.</p>",
        "whyItMatters": "<p>Third-party assessment is the gold standard for CMMC compliance. Preparing thoroughly before the assessors arrive is critical — a failed assessment means significant additional cost and delay before you can attempt certification again.</p>",
    },
    {
        "term": "CMMC Practice",
        "definition": "<p>In CMMC terminology, a practice is a specific cybersecurity activity or capability that your organization must implement. Each practice maps to a security requirement — for example, 'Limit system access to authorized users' is a practice. Practices are organized by domain (like Access Control, Incident Response) and by level (Level 1, 2, or 3).</p><p>Each practice has a unique identifier like AC.L2-3.1.1, which tells you the domain (AC = Access Control), the level (L2 = Level 2), and the corresponding NIST requirement number (3.1.1).</p>",
        "whyItMatters": "<p>Understanding how practices are structured helps you navigate your compliance checklist. Each practice must be demonstrably implemented — meaning you need evidence, not just a policy on paper.</p>",
    },
    {
        "term": "CMMC Domain",
        "definition": "<p>A CMMC domain is a grouping of related cybersecurity practices. The CMMC framework organizes its requirements into 14 domains such as Access Control (AC), Incident Response (IR), System and Communications Protection (SC), and Risk Assessment (RA). Each domain covers a specific area of cybersecurity.</p><p>Domains help you organize your compliance efforts by topic area. Rather than tackling 110 requirements randomly, you can work through them domain by domain — completing all Access Control requirements, then moving to Audit and Accountability, and so on.</p>",
        "whyItMatters": "<p>Organizing your CMMC implementation by domain makes the effort more manageable and ensures you don't miss related requirements. It also helps you assign responsibilities — your network team handles one set of domains, your HR handles another.</p>",
    },
    {
        "term": "Assessment Objective",
        "definition": "<p>An assessment objective is a specific, testable statement that an assessor uses to determine whether you've properly implemented a CMMC practice. Each practice may have multiple assessment objectives — these are the individual checkboxes an assessor must verify during your CMMC assessment.</p><p>For example, a practice about account management might have assessment objectives like: 'accounts are disabled when no longer needed,' 'account managers are notified when users are terminated,' and 'access authorizations are specified for each account.' Each objective must be individually satisfied.</p>",
        "whyItMatters": "<p>Understanding assessment objectives helps you prepare evidence packages for each requirement. Knowing exactly what assessors will check allows you to verify your own readiness before the official assessment.</p>",
    },
    {
        "term": "Enclave",
        "definition": "<p>An enclave is a defined portion of your network that is isolated and protected at a specific security level. In CMMC terms, many companies create a CUI enclave — a segregated network segment where all Controlled Unclassified Information is processed and stored, surrounded by additional security controls.</p><p>Creating an enclave allows you to limit the scope of your CMMC assessment. Instead of bringing your entire enterprise network up to CMMC Level 2 standards, you can isolate CUI handling into a smaller, more controlled environment and focus your security investment there.</p>",
        "whyItMatters": "<p>Properly scoping an enclave can dramatically reduce the cost and complexity of CMMC compliance. However, the enclave must be genuinely isolated — if CUI leaks into your broader network, your entire enterprise may be in scope.</p>",
    },
    {
        "term": "Scoping",
        "definition": "<p>Scoping is the process of determining which parts of your organization, networks, and systems fall under CMMC assessment requirements. Proper scoping identifies the boundaries of your CUI environment — which systems process, store, or transmit CUI, and which systems can be excluded from the assessment.</p><p>Scoping involves categorizing your assets: CUI assets (directly handle CUI), security protection assets (provide security for CUI assets), contractor risk-managed assets (can but don't process CUI), and out-of-scope assets. Getting this right early saves enormous time and money.</p>",
        "whyItMatters": "<p>Scoping is one of the first and most consequential steps in your CMMC journey. Over-scoping wastes resources securing systems that don't need it. Under-scoping creates gaps that assessors will find, leading to failed assessments.</p>",
    },
    {
        "term": "CMMC 2.0",
        "definition": "<p>CMMC 2.0 is the current version of the Cybersecurity Maturity Model Certification framework, streamlined from the original CMMC 1.0. Key changes include reducing the number of levels from five to three, aligning Level 2 directly with NIST SP 800-171, allowing self-assessment for some Level 2 scenarios, and introducing POA&M allowances.</p><p>CMMC 2.0 was designed to reduce the compliance burden on small businesses while maintaining the security rigor the DoD needs. It eliminated the maturity processes and unique CMMC practices from version 1.0, making the requirements more straightforward and aligned with existing NIST standards.</p>",
        "whyItMatters": "<p>CMMC 2.0 is the version being implemented in DoD contracts through the CMMC Program Final Rule (32 CFR Part 170). Understanding the 2.0 framework ensures you're preparing for the correct set of requirements.</p>",
    },
    {
        "term": "Provisional Authorization",
        "definition": "<p>In cybersecurity frameworks, a provisional authorization is a temporary or conditional approval to operate a system while certain security conditions are still being met. In the CMMC context, this relates to conditional certification where a contractor may receive a provisional status while closing out POA&M items within the allowed 180-day window.</p><p>This concept also applies in FedRAMP, where cloud service providers receive a Provisional Authority to Operate (P-ATO) from the Joint Authorization Board before individual agencies grant their own ATOs.</p>",
        "whyItMatters": "<p>Understanding provisional authorization helps you plan your compliance timeline. You may be able to win contracts with a provisional status, but you must close all remaining gaps within the specified timeframe or risk losing your certification.</p>",
    },
    {
        "term": "Maturity",
        "definition": "<p>In cybersecurity frameworks, maturity refers to how well-established and repeatable your security practices are. It's not just about having the right tools — it's about having documented processes, trained staff, consistent execution, and continuous improvement. A mature cybersecurity program runs reliably without depending on any single person's knowledge.</p><p>CMMC 1.0 included explicit maturity processes, but CMMC 2.0 simplified this. However, assessors still look for evidence that your practices are institutionalized — meaning they're documented, followed consistently, and reviewed regularly, not just implemented once and forgotten.</p>",
        "whyItMatters": "<p>Even under CMMC 2.0, demonstrating maturity in your security practices builds assessor confidence and reduces the risk of findings. A well-documented, consistently followed process is far more likely to pass assessment than an ad-hoc approach.</p>",
    },

    # ===== RMF/ATO Terms (~25) =====
    {
        "term": "Risk Management Framework (RMF)",
        "definition": "<p>The Risk Management Framework (RMF) is the structured process the federal government and DoD use to manage cybersecurity risk for information systems. It provides a disciplined, step-by-step approach: categorize your system, select security controls, implement them, assess their effectiveness, authorize the system to operate, and continuously monitor.</p><p>RMF replaced the older Certification and Accreditation (C&A) process and is defined in NIST SP 800-37. Every DoD and federal system must go through RMF before it can be used in production — it's the gateway to receiving an Authority to Operate (ATO).</p><p>For defense contractors, understanding RMF matters when your systems connect to DoD networks or when you're building systems that the government will operate. The RMF process determines what security controls apply and verifies they work.</p>",
        "whyItMatters": "<p>If you develop or operate systems for the DoD, RMF is the process that governs their security authorization. Understanding RMF steps and terminology ensures you can support the authorization process efficiently and speak the same language as your government customers.</p>",
    },
    {
        "term": "Authority to Operate (ATO)",
        "definition": "<p>An Authority to Operate (ATO) is the formal authorization from a senior official (the Authorizing Official) that permits an information system to operate in a production environment. It means the system's security risks have been evaluated and accepted — the system is approved for use.</p><p>An ATO is the end goal of the RMF process. It's granted after security controls have been assessed and any remaining risks have been formally accepted by the Authorizing Official. ATOs typically have an expiration period and must be renewed through continuous monitoring and periodic reassessment.</p><p>Without an ATO, a system cannot be connected to DoD or federal networks. Operating without authorization is a serious compliance violation.</p>",
        "whyItMatters": "<p>If you're building or maintaining systems for the government, understanding ATOs is essential. Delays in the ATO process can delay contract deliverables and milestone payments — getting it right the first time saves significant time and cost.</p>",
    },
    {
        "term": "Interim Authority to Test (IATT)",
        "definition": "<p>An Interim Authority to Test (IATT) is a temporary, limited authorization that allows a system to operate in a controlled environment for testing purposes before it has received a full ATO. It permits evaluation of the system's functionality and security in a real or near-real environment while final security controls are still being implemented or assessed.</p><p>IATTs have strict conditions — they specify what testing is allowed, for how long, and under what constraints. They're commonly used during system development when you need to connect to live networks for integration testing but haven't completed the full RMF process yet.</p>",
        "whyItMatters": "<p>IATTs can keep your project timeline on track by allowing testing to proceed while the full ATO process continues. However, they come with restrictions that must be carefully followed — violating IATT conditions is a serious compliance issue.</p>",
    },
    {
        "term": "Authority to Connect (ATC)",
        "definition": "<p>An Authority to Connect (ATC) is an approval that permits a system to connect to another system or network, typically a DoD network. While an ATO authorizes a system to operate, an ATC specifically authorizes the network connection between systems.</p><p>ATCs are common when a contractor-owned system needs to connect to a DoD network. Even if your system has its own ATO, you still need an ATC to plug into the government's infrastructure. The ATC process verifies that your system won't introduce unacceptable risk to the network you're connecting to.</p>",
        "whyItMatters": "<p>If your deliverable requires connecting to DoD networks, plan for the ATC process in your project timeline. It's a separate approval from the ATO and can add weeks or months if not anticipated early.</p>",
    },
    {
        "term": "Denial of Authority to Operate (DATO)",
        "definition": "<p>A Denial of Authority to Operate (DATO) is the formal decision by an Authorizing Official that a system's security risks are too high to allow it to operate. A DATO means the system must be shut down or disconnected until the identified security issues are resolved.</p><p>DATOs are serious — they indicate fundamental security failures that cannot be accepted or mitigated at the current time. A system under DATO cannot process data or connect to networks until the issues are remediated and the system is reassessed.</p>",
        "whyItMatters": "<p>A DATO on a system you operate or maintain means immediate operational disruption. Understanding what triggers a DATO helps you prioritize the security controls that Authorizing Officials consider most critical.</p>",
    },
    {
        "term": "Information System Security Manager (ISSM)",
        "definition": "<p>An Information System Security Manager (ISSM) is the person responsible for managing the cybersecurity program for one or more information systems. The ISSM ensures security policies are implemented, monitors compliance, coordinates with the Authorizing Official, and oversees the day-to-day security operations of the system.</p><p>In DoD environments, the ISSM is a formally designated role with specific training and certification requirements. They serve as the primary point of contact for all security matters related to their assigned systems and must be knowledgeable about RMF, the system's security posture, and applicable policies.</p>",
        "whyItMatters": "<p>If your company operates DoD systems, you need a qualified ISSM. This role is critical for maintaining your ATO and ensuring continuous compliance — it's not a collateral duty that can be assigned casually.</p>",
    },
    {
        "term": "Information System Security Officer (ISSO)",
        "definition": "<p>An Information System Security Officer (ISSO) works under the ISSM to handle the day-to-day security operations of an information system. The ISSO monitors system activity, manages security configurations, responds to security events, and maintains security documentation.</p><p>While the ISSM manages the program at a higher level, the ISSO is hands-on with the system — running scans, reviewing logs, applying patches, and ensuring that security controls remain effective on a daily basis. In smaller organizations, one person may fill both the ISSM and ISSO roles.</p>",
        "whyItMatters": "<p>Having a dedicated ISSO ensures someone is actively watching your systems every day. Without this role filled, security monitoring gaps develop quickly and your compliance posture degrades between assessments.</p>",
    },
    {
        "term": "Information Systems Security Engineer (ISSE)",
        "definition": "<p>An Information Systems Security Engineer (ISSE) is the technical expert responsible for designing and implementing security architectures and solutions for information systems. While the ISSM and ISSO focus on management and operations, the ISSE focuses on engineering — building secure systems from the ground up.</p><p>ISSEs evaluate security requirements, design network architectures, select security technologies, and ensure systems are built to meet RMF requirements. They work closely with system engineers and developers to integrate security into the system design rather than bolting it on afterward.</p>",
        "whyItMatters": "<p>Security problems are cheapest to fix during design. Having an ISSE involved early in system development prevents costly rework and reduces the risk of security findings during the RMF assessment process.</p>",
    },
    {
        "term": "Authorizing Official (AO)",
        "definition": "<p>The Authorizing Official (AO) is the senior government official who has the authority to formally accept the security risks of an information system and grant (or deny) its Authority to Operate. The AO takes personal responsibility for the decision to allow a system to operate, accepting any residual risk.</p><p>AOs are typically senior leaders — flag officers, SES civilians, or other designated officials. They rely on security assessments, risk analyses, and recommendations from their security teams to make authorization decisions, but the final responsibility rests with them personally.</p>",
        "whyItMatters": "<p>Understanding what the AO needs to make their decision helps you prepare better RMF packages. The AO wants clear risk information, not technical jargon — presenting security findings in business risk terms helps your authorization package move faster.</p>",
    },
    {
        "term": "Security Control Assessor (SCA)",
        "definition": "<p>A Security Control Assessor (SCA) is an independent evaluator who tests and verifies whether security controls are properly implemented and effective. The SCA conducts the formal assessment that the Authorizing Official relies on to make the ATO decision.</p><p>The SCA reviews documentation, interviews system administrators, and tests security controls to produce a Security Assessment Report (SAR). Their independence is important — they should not be the same people who implemented the controls, ensuring an objective evaluation.</p>",
        "whyItMatters": "<p>The SCA's findings directly influence your ATO decision. Preparing thorough evidence packages and ensuring your team can explain how controls work during interviews makes the assessment process smoother and faster.</p>",
    },
    {
        "term": "Security Control Assessment Report (SCAR)",
        "definition": "<p>A Security Control Assessment Report (SCAR), also called a Security Assessment Report (SAR), is the formal document produced by the Security Control Assessor after evaluating a system's security controls. It details which controls were tested, how they were tested, what was found, and the assessor's overall risk findings.</p><p>The SCAR is a key input to the ATO decision. It identifies weaknesses, recommends mitigations, and provides the Authorizing Official with the information needed to determine whether the system's residual risk is acceptable.</p>",
        "whyItMatters": "<p>The SCAR drives your POA&M — every finding in the report becomes a gap you must address. Understanding how to read and respond to a SCAR helps you prioritize remediation efforts and maintain your authorization.</p>",
    },
    {
        "term": "Security Control Assessment",
        "definition": "<p>A security control assessment is the formal process of evaluating whether the security controls implemented on an information system are working correctly, producing the desired outcome, and meeting security requirements. It's a systematic evaluation — not just checking boxes, but verifying that controls actually function as intended in your specific environment.</p><p>Assessments involve examining documentation, interviewing personnel, and testing controls through hands-on verification. The results feed into the Security Assessment Report and ultimately inform the authorization decision.</p>",
        "whyItMatters": "<p>Regular security control assessments — not just during initial authorization but as part of continuous monitoring — are how you maintain confidence that your security posture hasn't degraded. Finding problems yourself is always better than having an assessor find them.</p>",
    },
    {
        "term": "Continuous Monitoring",
        "definition": "<p>Continuous monitoring is the ongoing process of maintaining awareness of your security posture, vulnerabilities, and threats. Rather than treating security as a one-time assessment, continuous monitoring ensures you're always aware of changes that could affect your system's security — new vulnerabilities, configuration changes, emerging threats, and evolving compliance requirements.</p><p>In practice, continuous monitoring includes automated vulnerability scanning, log analysis, configuration monitoring, regular security assessments, and ongoing risk evaluation. For DoD systems with ATOs, continuous monitoring is required to maintain authorization — it's how the AO knows the system remains secure between formal reassessments.</p>",
        "whyItMatters": "<p>Continuous monitoring is both a CMMC requirement and an RMF requirement. Building automated monitoring into your operations reduces the manual effort of compliance and helps you catch security issues before they become breaches or audit findings.</p>",
    },
    {
        "term": "Authorization Boundary",
        "definition": "<p>The authorization boundary defines exactly what is included in a system's security authorization — which hardware, software, networks, people, and processes are 'inside' the boundary and subject to the system's security controls. Everything inside the boundary is covered by the ATO; everything outside is not.</p><p>Drawing the authorization boundary is a critical early step in the RMF process. It determines the scope of your security controls, your assessment, and your documentation. A well-defined boundary makes everything downstream clearer and more manageable.</p>",
        "whyItMatters": "<p>A poorly defined authorization boundary creates confusion during assessments and can leave critical systems unprotected. Take time to define clear, defensible boundaries early — it affects every subsequent step of your compliance journey.</p>",
    },
    {
        "term": "Risk Assessment Report (RAR)",
        "definition": "<p>A Risk Assessment Report (RAR) is a formal document that identifies and evaluates the security risks facing an information system. It catalogs threats, vulnerabilities, the likelihood of exploitation, and the potential impact if a security incident occurs. The RAR provides the Authorizing Official with a clear picture of the risk landscape.</p><p>The RAR is a required artifact in the RMF process. It goes beyond listing technical vulnerabilities — it contextualizes risks in terms of mission impact, helping decision-makers understand not just what could go wrong, but what it would mean for operations if it did.</p>",
        "whyItMatters": "<p>A well-written RAR helps your AO make informed decisions quickly. Presenting risks in terms of business and mission impact — rather than just technical severity — demonstrates mature risk management and builds confidence in your security program.</p>",
    },

    # ===== NIST Framework Terms (~20) =====
    {
        "term": "NIST",
        "definition": "<p>The National Institute of Standards and Technology (NIST) is the U.S. federal agency that develops the cybersecurity standards, guidelines, and frameworks used throughout government and industry. NIST doesn't enforce compliance — it creates the standards that other agencies (like the DoD) incorporate into their requirements.</p><p>For defense contractors, NIST is the source of the security requirements you must implement. NIST SP 800-171 defines the controls for protecting CUI, NIST SP 800-53 provides the comprehensive control catalog used in RMF, and NIST SP 800-37 describes the Risk Management Framework process.</p>",
        "whyItMatters": "<p>NIST publications are the foundation of virtually all federal cybersecurity compliance requirements. Understanding which NIST publications apply to your situation helps you navigate the compliance landscape and find authoritative guidance for implementation.</p>",
    },
    {
        "term": "NIST SP 800-53",
        "definition": "<p>NIST Special Publication 800-53 is the comprehensive catalog of security and privacy controls used to protect federal information systems. It contains over 1,000 controls organized into 20 families covering everything from access control to system integrity. Think of it as the master list of every security measure the government has defined.</p><p>While NIST SP 800-171 (used for CMMC) draws from 800-53, the full 800-53 catalog is much broader and is primarily used in the RMF process for federal systems. Each control includes a description, supplemental guidance, and related controls.</p><p>Defense contractors encounter 800-53 when working on government systems that go through RMF, or when the 800-171 requirements reference their parent 800-53 controls for additional context.</p>",
        "whyItMatters": "<p>If you operate or develop DoD information systems, 800-53 controls are your security blueprint. Understanding the full control catalog also helps you understand the intent behind the 800-171 requirements used in CMMC.</p>",
    },
    {
        "term": "NIST SP 800-171",
        "definition": "<p>NIST Special Publication 800-171 defines the security requirements for protecting Controlled Unclassified Information (CUI) in non-federal systems — meaning your systems, as a contractor. It contains 110 security requirements organized into 14 families, and it is the direct basis for CMMC Level 2.</p><p>The requirements in 800-171 are derived from NIST SP 800-53 but tailored for the contractor environment. They cover access control, awareness training, audit logging, configuration management, identification and authentication, incident response, maintenance, media protection, personnel security, physical protection, risk assessment, security assessment, system protection, and system integrity.</p><p>If your company handles CUI, implementing all 110 requirements of NIST SP 800-171 is your compliance target. Your SPRS score is calculated based on how many of these requirements you fully meet.</p>",
        "whyItMatters": "<p>NIST SP 800-171 is THE standard for CUI protection in contractor environments and the direct basis for CMMC Level 2 certification. Every requirement you don't fully meet reduces your SPRS score and represents a gap you must close.</p>",
    },
    {
        "term": "NIST SP 800-37",
        "definition": "<p>NIST Special Publication 800-37 is the guide for applying the Risk Management Framework (RMF) to information systems. It describes the step-by-step process for preparing your system, categorizing it, selecting controls, implementing them, assessing their effectiveness, authorizing the system, and monitoring it continuously.</p><p>This publication is the RMF playbook — it tells you what to do at each step, what documents to produce, and who is responsible. If you're involved in getting a system through the ATO process, 800-37 is your guide.</p>",
        "whyItMatters": "<p>Understanding the RMF process described in 800-37 helps you support your government customers more effectively and ensures your deliverables align with the authorization process they must follow.</p>",
    },
    {
        "term": "NIST SP 800-53A",
        "definition": "<p>NIST Special Publication 800-53A provides guidance for assessing the security controls defined in SP 800-53. It describes the methods, procedures, and depth of assessment for each control — essentially telling assessors how to test whether your security controls actually work.</p><p>For each control, 800-53A defines assessment objectives (specific things to verify), assessment methods (examine, interview, test), and assessment objects (what to look at — documents, people, or systems). This publication is what Security Control Assessors use to structure their evaluations.</p>",
        "whyItMatters": "<p>Understanding how controls will be assessed helps you prepare better evidence and ensure your implementations will hold up under scrutiny. Studying 800-53A for your applicable controls lets you self-assess before the official evaluation.</p>",
    },
    {
        "term": "OSCAL",
        "definition": "<p>The Open Security Controls Assessment Language (OSCAL) is a standardized, machine-readable format for representing security control information. Developed by NIST, OSCAL allows security plans, assessment results, and control catalogs to be expressed in structured data formats (JSON, XML, YAML) rather than Word documents and spreadsheets.</p><p>OSCAL is designed to automate much of the compliance documentation burden. Instead of manually creating and updating security plans, you can maintain machine-readable artifacts that tools can process, validate, and report on automatically.</p>",
        "whyItMatters": "<p>OSCAL adoption is growing across the federal compliance landscape. Tools supporting OSCAL can dramatically reduce the manual effort of maintaining SSPs, POA&Ms, and assessment documentation — an investment that pays off across multiple compliance cycles.</p>",
    },
    {
        "term": "FIPS 199",
        "definition": "<p>FIPS 199 (Federal Information Processing Standard 199) establishes the categories for classifying federal information and information systems based on the potential impact of a security breach. It defines three impact levels — Low, Moderate, and High — across three security objectives: confidentiality, integrity, and availability.</p><p>The categorization from FIPS 199 drives everything downstream in the RMF process — it determines which security controls apply to your system, how rigorously they must be implemented, and how thoroughly they'll be assessed. A system categorized as High impact gets significantly more security scrutiny than one categorized as Low.</p>",
        "whyItMatters": "<p>System categorization under FIPS 199 determines the security baseline for your system. Getting the categorization right is crucial — over-categorizing wastes resources, while under-categorizing leaves your system insufficiently protected and out of compliance.</p>",
    },
    {
        "term": "FIPS 200",
        "definition": "<p>FIPS 200 (Federal Information Processing Standard 200) specifies the minimum security requirements for federal information systems across 17 security-related areas. After a system is categorized using FIPS 199, FIPS 200 tells you the minimum security areas that must be addressed — access control, awareness and training, audit and accountability, and so on.</p><p>FIPS 200 works hand-in-hand with NIST SP 800-53, which provides the specific controls to meet those minimum requirements. Together, they form the control selection foundation for the RMF process.</p>",
        "whyItMatters": "<p>FIPS 200 establishes the minimum bar for security. Understanding these minimum requirements helps you ensure your security program covers all required areas, even as you tailor specific controls to your system's needs.</p>",
    },
    {
        "term": "Security Controls",
        "definition": "<p>Security controls are the safeguards or countermeasures your organization implements to protect information systems and data. They can be technical (firewalls, encryption, access controls), operational (procedures, training, monitoring), or management (policies, risk assessments, planning). Together, they form your defense against cyber threats.</p><p>In the NIST and CMMC frameworks, security controls are defined, categorized, and assessed systematically. Each control addresses a specific aspect of security, and collectively they create a layered defense that protects your systems from multiple angles.</p>",
        "whyItMatters": "<p>Security controls are the concrete actions you take to achieve compliance. Understanding the difference between technical, operational, and management controls helps you assign responsibility and budget appropriately across your organization.</p>",
    },
    {
        "term": "Control Family",
        "definition": "<p>A control family is a grouping of related security controls that address a common security topic. For example, the Access Control (AC) family contains all controls related to managing who can access your systems and what they can do. NIST SP 800-53 organizes its controls into 20 families, while NIST SP 800-171 uses 14 families.</p><p>Control families help you organize your security program and ensure comprehensive coverage. Each family represents a distinct area of security that requires attention — from personnel security to incident response to system maintenance.</p>",
        "whyItMatters": "<p>Working through compliance family by family ensures nothing is overlooked. It also helps you assign subject-matter experts — your network team owns certain families, your HR team owns others, and your management owns the governance families.</p>",
    },
    {
        "term": "Control Enhancement",
        "definition": "<p>A control enhancement is an additional capability or specification that extends a base security control. Think of the base control as the minimum requirement and enhancements as optional add-ons that provide stronger security. For example, the base Access Control (AC-2) control requires account management, while its enhancements add requirements like automated enforcement and account monitoring.</p><p>Not all enhancements apply to every system — they're selected based on the system's security categorization and risk profile. Higher-impact systems typically require more enhancements.</p>",
        "whyItMatters": "<p>Understanding control enhancements helps you interpret your security baseline correctly. Some enhancements are required for your system's impact level, while others are optional — knowing the difference prevents over- or under-investing in security measures.</p>",
    },
    {
        "term": "Security Baseline",
        "definition": "<p>A security baseline is the starting set of security controls recommended for a system based on its impact level (Low, Moderate, or High). NIST SP 800-53 defines three baselines — each one is a curated list of controls and enhancements appropriate for that impact level. Higher impact levels include more controls and more stringent enhancements.</p><p>The baseline is a starting point, not the final answer. Organizations tailor the baseline by adding controls for specific threats, removing controls that don't apply, or applying overlays for their specific environment. The tailored baseline becomes the system's security requirements.</p>",
        "whyItMatters": "<p>Starting from the correct baseline ensures your security program is neither over-engineered (wasting resources) nor under-engineered (leaving gaps). For CMMC, the 'baseline' is effectively the 110 requirements of NIST SP 800-171.</p>",
    },
    {
        "term": "Overlay",
        "definition": "<p>A security overlay is a set of additional or modified security controls that address the unique requirements of a specific community, technology, or environment. Overlays are applied on top of the standard security baseline to customize it for special circumstances.</p><p>For example, the DoD has overlays for classified systems, cloud environments, and specific mission areas. Overlays can add controls not in the standard baseline, increase the rigor of existing controls, or provide specific implementation guidance for a particular context.</p>",
        "whyItMatters": "<p>If your system falls under a specific DoD community or uses particular technologies, an overlay may apply additional requirements beyond the standard baseline. Identifying applicable overlays early prevents surprises during assessment.</p>",
    },

    # ===== DoD/Federal Terms (~30) =====
    {
        "term": "DISA",
        "definition": "<p>The Defense Information Systems Agency (DISA) is the DoD agency responsible for providing and protecting the department's IT infrastructure. DISA manages the DoD's networks, develops security standards (including STIGs), provides cybersecurity tools (like ACAS), and operates critical enterprise services.</p><p>For defense contractors, DISA is the source of many security tools and standards you'll encounter. STIGs (Security Technical Implementation Guides) from DISA define how systems must be configured, and DISA's vulnerability scanning tools are the standard for DoD security assessments.</p>",
        "whyItMatters": "<p>DISA's standards and tools — particularly STIGs and ACAS — are the benchmarks against which DoD systems are secured and assessed. Familiarity with DISA resources is essential for anyone working on DoD information systems.</p>",
    },
    {
        "term": "Security Technical Implementation Guide (STIG)",
        "definition": "<p>A Security Technical Implementation Guide (STIG) is a configuration standard developed by DISA that specifies exactly how a particular technology — an operating system, application, network device, or database — must be configured to meet DoD security requirements. STIGs contain hundreds of specific settings, each categorized as a finding severity (CAT I, CAT II, CAT III).</p><p>Every piece of technology running on a DoD network must be configured according to its applicable STIG. This means specific registry keys, group policy settings, file permissions, service configurations, and feature enablement/disablement — all prescribed in detail.</p><p>STIG compliance is verified through automated scanning tools like SCAP and manual checklist review. Non-compliance findings must be documented and remediated or formally accepted through a risk acceptance process.</p>",
        "whyItMatters": "<p>If you operate or deliver systems for the DoD, STIG compliance is non-negotiable. Understanding STIGs helps you build compliant systems from the start rather than spending time and money remediating findings after deployment.</p>",
    },
    {
        "term": "ACAS",
        "definition": "<p>ACAS (Assured Compliance Assessment Solution) is the DoD's enterprise vulnerability scanning and management tool suite. Built on Tenable technology (Nessus and Tenable Security Center), ACAS identifies vulnerabilities, misconfigurations, and compliance issues across DoD networks and systems.</p><p>ACAS scans produce findings that must be tracked, prioritized, and remediated. The scan results feed into the system's risk posture and are reviewed during CORA inspections and RMF assessments. Regular ACAS scanning is required for all DoD systems.</p>",
        "whyItMatters": "<p>ACAS scan results are a primary input to your system's security posture. Maintaining clean ACAS scans demonstrates that you're actively managing vulnerabilities — a key indicator assessors and inspectors look for.</p>",
    },
    {
        "term": "Endpoint Security Solution (ESS)",
        "definition": "<p>The Endpoint Security Solution (ESS) is the DoD's mandated endpoint protection platform. ESS replaced the older Host Based Security System (HBSS) and is built on Trellix (formerly McAfee/FireEye) technology. It provides antivirus, host intrusion prevention, application control, and endpoint detection and response capabilities for DoD endpoints.</p><p>ESS is a required component on DoD systems — it must be installed, properly configured, and actively monitored. The platform provides both prevention (stopping known threats) and detection (identifying suspicious behavior) capabilities.</p>",
        "whyItMatters": "<p>ESS deployment and management is a fundamental requirement for DoD systems. If you manage endpoints on DoD networks, ensuring ESS is properly configured and maintained is essential for both security and compliance.</p>",
    },
    {
        "term": "Trellix",
        "definition": "<p>Trellix is the cybersecurity company (formed from the merger of McAfee Enterprise and FireEye) whose products power the DoD's Endpoint Security Solution (ESS). In DoD environments, you'll encounter Trellix tools including endpoint protection, host intrusion prevention, data loss prevention, and endpoint detection and response.</p><p>Trellix replaced references to 'McAfee' and 'HBSS' in DoD terminology. When someone references Trellix in a DoD context, they're typically talking about the endpoint security tools installed on government workstations and servers.</p>",
        "whyItMatters": "<p>Understanding the Trellix product suite helps you manage endpoint security on DoD systems effectively. Proper Trellix/ESS configuration is routinely inspected during CORA assessments and cybersecurity inspections.</p>",
    },
    {
        "term": "CORA",
        "definition": "<p>CORA (Cybersecurity Operational Readiness Assessment) is the DoD's inspection process for evaluating the cybersecurity posture of military commands and their information systems. CORA replaced the older CCRI (Command Cyber Readiness Inspection) process and assesses whether an organization's networks, systems, and personnel meet DoD cybersecurity standards.</p><p>During a CORA, inspectors evaluate vulnerability management, STIG compliance, account management, physical security, training compliance, and overall cybersecurity program maturity. The assessment covers both technical controls and organizational processes.</p>",
        "whyItMatters": "<p>If you support DoD network operations, CORA results directly impact your customer's cybersecurity grades. Understanding the CORA process helps you ensure the systems you manage are inspection-ready at all times.</p>",
    },
    {
        "term": "SCAP",
        "definition": "<p>The Security Content Automation Protocol (SCAP) is a standardized approach for automating security configuration checks and vulnerability assessments. SCAP tools use machine-readable security checklists (like STIGs) to automatically scan systems and identify non-compliant configurations without manual review.</p><p>In DoD environments, SCAP-compliant tools are the primary method for verifying STIG compliance. The DISA SCAP Compliance Checker (SCC) is the standard tool — it reads STIG benchmarks and automatically checks systems against hundreds of configuration requirements, producing reports that identify findings by severity category.</p>",
        "whyItMatters": "<p>SCAP automation dramatically reduces the time needed to verify STIG compliance. Using SCAP tools regularly helps you catch configuration drift before inspectors do, keeping your systems in a ready state.</p>",
    },
    {
        "term": "Information Assurance Vulnerability Management (IAVM)",
        "definition": "<p>Information Assurance Vulnerability Management (IAVM) is the DoD's program for managing cybersecurity vulnerabilities across the department. When critical vulnerabilities are discovered, the DoD issues alerts and bulletins through the IAVM program requiring affected organizations to patch or mitigate the vulnerabilities within specified timeframes.</p><p>IAVM notices come in three categories: IAVAs (alerts for critical vulnerabilities requiring urgent action), IAVBs (bulletins for significant vulnerabilities), and IAVTs (technical advisories for awareness). Each has mandated response timelines that must be tracked and reported.</p>",
        "whyItMatters": "<p>IAVM compliance is tracked and inspected during CORA assessments. Missing IAVM deadlines results in compliance findings. Having a reliable patch management process ensures you can meet IAVM timelines consistently.</p>",
    },
    {
        "term": "IAVA",
        "definition": "<p>An Information Assurance Vulnerability Alert (IAVA) is the highest-priority IAVM notice, issued for critical vulnerabilities that require immediate attention. IAVAs typically mandate that affected systems be patched or mitigated within 21 days (or sometimes sooner for the most critical issues).</p><p>IAVAs represent vulnerabilities that pose a serious risk to DoD systems if left unpatched — often actively exploited vulnerabilities or those affecting widely deployed technologies. Compliance with IAVA mandates is tracked at the command level and reported upward.</p>",
        "whyItMatters": "<p>IAVA compliance is one of the first things inspectors check during cybersecurity assessments. Having outstanding IAVAs is a significant finding that reflects poorly on your organization's vulnerability management maturity.</p>",
    },
    {
        "term": "IAVB",
        "definition": "<p>An Information Assurance Vulnerability Bulletin (IAVB) is a mid-level IAVM notice for significant but not critical vulnerabilities. IAVBs typically have longer compliance windows than IAVAs (often 30 days) and address vulnerabilities that are important but not as immediately exploitable.</p><p>Like IAVAs, IAVBs require acknowledgment, tracking, and remediation within the specified timeframe. Organizations must report their compliance status and document any systems that require an exception or extension.</p>",
        "whyItMatters": "<p>While less urgent than IAVAs, outstanding IAVBs still represent compliance gaps. A consistent process for tracking and patching both IAVAs and IAVBs demonstrates mature vulnerability management to assessors.</p>",
    },
    {
        "term": "IAVT",
        "definition": "<p>An Information Assurance Vulnerability Technical Advisory (IAVT) is the lowest-priority IAVM notice, providing awareness of vulnerabilities that may affect DoD systems but don't require mandatory patching within a specified timeframe. IAVTs are informational — they help system administrators stay aware of emerging vulnerabilities.</p><p>While IAVTs don't carry mandatory compliance deadlines like IAVAs and IAVBs, they represent good intelligence about your threat landscape. Smart organizations track IAVTs and incorporate relevant patches into their regular maintenance cycles.</p>",
        "whyItMatters": "<p>Proactively addressing IAVTs shows mature vulnerability management. While they won't generate compliance findings on their own, unpatched IAVT vulnerabilities can still be exploited by adversaries.</p>",
    },
    {
        "term": "eMASS",
        "definition": "<p>eMASS (Enterprise Mission Assurance Support Service) is the DoD's official web-based application for managing the Risk Management Framework process. It's the system of record for RMF packages — you use eMASS to document your system's security controls, upload artifacts, track POA&M items, and move through the authorization workflow.</p><p>eMASS is where your System Security Plan, assessment results, risk acceptance decisions, and ATO documentation all live. If you're involved in getting a DoD system authorized, you'll spend significant time in eMASS entering data, uploading evidence, and managing the authorization workflow.</p>",
        "whyItMatters": "<p>eMASS proficiency is essential for anyone managing DoD system authorizations. Understanding the workflow and data requirements upfront prevents delays and rework in the authorization process.</p>",
    },
    {
        "term": "DITPR",
        "definition": "<p>DITPR (DoD Information Technology Portfolio Repository) is the DoD's enterprise database for registering and tracking IT systems. Every DoD information system must be registered in DITPR with details about its mission, architecture, funding, and security status.</p><p>DITPR registration is a prerequisite for the RMF process — your system must exist in DITPR before you can begin its security authorization in eMASS. The system record includes information about the system's operational status, connected networks, and responsible personnel.</p>",
        "whyItMatters": "<p>If your system isn't registered in DITPR, you can't start the RMF process. Ensuring accurate DITPR registration early prevents administrative delays in your authorization timeline.</p>",
    },
    {
        "term": "SNAP",
        "definition": "<p>SNAP (System Network Approval Process) is the DoD Navy's process for approving systems to connect to Navy networks. It ensures that systems meet security requirements before being granted connectivity to Navy IT infrastructure.</p><p>The SNAP process involves documenting your system's architecture, security controls, and network connectivity requirements. It's a gateway process — you must complete SNAP before your system can communicate on Navy networks.</p>",
        "whyItMatters": "<p>If you're a contractor delivering systems to the Navy, understanding the SNAP process is essential for planning your deployment timeline. SNAP approvals can take weeks or months, so early engagement is critical.</p>",
    },
    {
        "term": "JFHQ-DODIN",
        "definition": "<p>JFHQ-DODIN (Joint Force Headquarters - Department of Defense Information Networks) is the DoD organization responsible for operating and defending the department's information networks. They direct the day-to-day operations and cybersecurity defense of the DoDIN (DoD Information Network).</p><p>JFHQ-DODIN issues operational directives, manages cyber defense responses, and oversees network security across the DoD. They're the operational arm that ensures DoD networks remain secure and available.</p>",
        "whyItMatters": "<p>JFHQ-DODIN directives can impact systems connected to DoD networks. Understanding their role helps you anticipate and respond to operational security requirements that may affect your systems or services.</p>",
    },
    {
        "term": "CYBERCOM",
        "definition": "<p>United States Cyber Command (CYBERCOM) is the unified combatant command responsible for the DoD's cyberspace operations. CYBERCOM directs, synchronizes, and coordinates cyberspace operations in defense of DoD networks and, when directed, conducts offensive cyber operations in support of national objectives.</p><p>While defense contractors don't interact directly with CYBERCOM, the command's directives and priorities flow down through the DoD and influence the cybersecurity requirements that contractors must meet.</p>",
        "whyItMatters": "<p>CYBERCOM's priorities shape the DoD's cybersecurity focus areas. Understanding their strategic direction helps you anticipate where compliance requirements are heading and what capabilities the DoD will value in its contractors.</p>",
    },
    {
        "term": "SIPRNet",
        "definition": "<p>SIPRNet (Secret Internet Protocol Router Network) is the DoD's classified network for transmitting information up to the Secret level. It's a completely separate network from the internet and from NIPRNet — physically and logically isolated to protect classified information.</p><p>Access to SIPRNet requires a security clearance, and systems connected to SIPRNet must meet stringent security requirements. If your contract requires access to classified information, you may need SIPRNet connectivity, which involves additional security infrastructure and oversight.</p>",
        "whyItMatters": "<p>If your work involves classified data, understanding SIPRNet requirements helps you plan for the additional security infrastructure, personnel clearances, and facility requirements needed to access and protect classified information.</p>",
    },
    {
        "term": "NIPRNet",
        "definition": "<p>NIPRNet (Non-classified Internet Protocol Router Network) is the DoD's network for transmitting unclassified but sensitive information. While not used for classified data, NIPRNet is still a controlled environment with security requirements — it's not the open internet.</p><p>Many DoD applications and services run on NIPRNet, and contractors frequently need NIPRNet access to interact with DoD systems, submit deliverables, or access government-furnished resources. NIPRNet connectivity requires compliance with DoD connection approval processes.</p>",
        "whyItMatters": "<p>NIPRNet access is common for defense contractors. Understanding the connection requirements and security obligations helps you plan for the approvals and security measures needed to connect your systems to DoD unclassified networks.</p>",
    },
    {
        "term": "Public Key Infrastructure (PKI)",
        "definition": "<p>Public Key Infrastructure (PKI) is the system of digital certificates, certificate authorities, and registration authorities that enables secure electronic communications. In the DoD, PKI is the backbone of identity verification — it's what makes your Common Access Card (CAC) work for authentication, email signing, and document encryption.</p><p>DoD PKI uses digital certificates issued to people, systems, and devices to verify identities and protect communications. When you use your CAC to log into a DoD system or digitally sign an email, PKI is the technology making that possible.</p>",
        "whyItMatters": "<p>PKI-based authentication is mandatory for DoD systems. If you develop or operate systems for the DoD, they must support CAC/PKI authentication — username and password alone is not sufficient for most DoD environments.</p>",
    },
    {
        "term": "Common Access Card (CAC)",
        "definition": "<p>The Common Access Card (CAC) is the standard identification card for active-duty military, DoD civilians, and eligible contractors. Beyond physical identification, the CAC contains digital certificates that enable two-factor authentication to DoD networks and systems, email encryption, and digital signatures.</p><p>The CAC is a smart card — it contains a chip with your PKI certificates. When you insert your CAC into a reader and enter your PIN, the system verifies your identity through the certificates on the card. This provides much stronger authentication than passwords alone.</p>",
        "whyItMatters": "<p>If your employees need access to DoD systems or facilities, they'll need CACs. Understanding CAC issuance requirements and planning for CAC-enabled infrastructure (card readers, middleware) is essential for contract execution.</p>",
    },
    {
        "term": "RMF Technical Advisory (RMF TA)",
        "definition": "<p>An RMF Technical Advisory (RMF TA) is guidance issued to clarify, update, or provide additional direction on RMF implementation. RMF TAs address specific technical questions, process changes, or policy updates that affect how organizations implement the Risk Management Framework.</p><p>RMF TAs are important because they represent the latest official guidance on RMF processes. They may introduce new requirements, modify existing processes, or provide clarification on ambiguous areas of the RMF framework.</p>",
        "whyItMatters": "<p>Staying current with RMF TAs ensures your authorization packages reflect the latest requirements and guidance. Missing an RMF TA update can lead to rework when assessors identify outdated processes or documentation.</p>",
    },
    {
        "term": "CCRI",
        "definition": "<p>CCRI (Command Cyber Readiness Inspection) was the DoD's former cybersecurity inspection program, now replaced by CORA (Cybersecurity Operational Readiness Assessment). CCRIs evaluated a command's cybersecurity posture, including vulnerability management, STIG compliance, and overall program maturity.</p><p>While the CCRI term is still sometimes used informally, the official process is now CORA. The core objectives remain similar — verifying that DoD organizations maintain effective cybersecurity programs — but the assessment methodology has been updated.</p>",
        "whyItMatters": "<p>If you hear 'CCRI' in conversation, understand it now refers to CORA. Using current terminology (CORA, not CCRI) demonstrates awareness of current DoD cybersecurity processes and builds credibility with your government customers.</p>",
    },
    {
        "term": "Helix",
        "definition": "<p>Helix is the DoD's IT Service Management (ITSM) platform, replacing the former BMC Remedy system. Built on the BMC Helix platform, it manages IT service requests, incident tickets, change management, and asset tracking across DoD organizations.</p><p>Helix is where you submit and track IT support requests, report incidents, manage changes to production systems, and maintain configuration records. If you provide IT services to the DoD, you'll likely interface with Helix for service management workflows.</p>",
        "whyItMatters": "<p>Understanding Helix workflows is important if you manage IT services for DoD customers. Proper use of the ticketing and change management systems demonstrates process discipline that assessors and inspectors expect to see.</p>",
    },

    # ===== General Cybersecurity Terms (~80+) =====
    {
        "term": "Multi-Factor Authentication (MFA)",
        "definition": "<p>Multi-Factor Authentication (MFA) requires users to provide two or more verification factors to access a system — something you know (password), something you have (phone, security key, CAC), or something you are (fingerprint, face scan). MFA makes it dramatically harder for attackers to access your accounts, even if they steal your password.</p><p>In practice, MFA typically means entering your password and then confirming your identity through a second method — a code sent to your phone, a push notification on an authenticator app, or inserting a hardware security key. The DoD's CAC is a form of MFA: it combines something you have (the card) with something you know (your PIN).</p>",
        "whyItMatters": "<p>MFA is one of the most effective security controls available and is required under CMMC. Implementing MFA across all remote access and privileged accounts significantly reduces your risk of account compromise.</p>",
    },
    {
        "term": "Zero Trust",
        "definition": "<p>Zero Trust is a cybersecurity strategy that assumes no user, device, or network connection should be automatically trusted — even if they're inside your network perimeter. Instead of the traditional 'castle and moat' approach where everything inside the firewall is trusted, Zero Trust requires continuous verification of every access request.</p><p>The core principle is 'never trust, always verify.' Every time a user or device tries to access a resource, their identity, device health, and authorization are verified before access is granted. Access is given with the minimum privileges needed and only for the duration required.</p><p>The DoD has adopted Zero Trust as a strategic priority, and its principles are increasingly reflected in compliance requirements. While full Zero Trust implementation is complex, adopting its principles — least privilege, micro-segmentation, continuous verification — strengthens your overall security posture.</p>",
        "whyItMatters": "<p>The DoD is moving toward Zero Trust architecture, and this shift will increasingly influence contractor requirements. Understanding and beginning to adopt Zero Trust principles positions your company ahead of evolving compliance expectations.</p>",
    },
    {
        "term": "Phishing",
        "definition": "<p>Phishing is a type of social engineering attack where attackers send deceptive emails, messages, or create fake websites to trick people into revealing sensitive information like passwords, financial data, or personal details. Phishing is the most common way cyber attacks begin — it's far easier to trick a person than to hack a system.</p><p>Phishing attacks range from mass-produced spam to highly targeted 'spear phishing' emails crafted specifically for one person using information gathered from social media and public sources. Business Email Compromise (BEC) is a sophisticated phishing variant where attackers impersonate executives to authorize fraudulent wire transfers.</p>",
        "whyItMatters": "<p>Phishing is the number one attack vector against defense contractors. Regular security awareness training and phishing simulations are CMMC requirements — training your employees to recognize and report phishing attempts is one of your most impactful security investments.</p>",
    },
    {
        "term": "Ransomware",
        "definition": "<p>Ransomware is malicious software that encrypts your files and data, making them inaccessible until you pay a ransom to the attackers. Modern ransomware often includes 'double extortion' — attackers steal your data before encrypting it and threaten to publish it publicly if you don't pay, even if you can restore from backups.</p><p>Ransomware attacks can shut down entire organizations for days or weeks. For defense contractors, a ransomware attack isn't just a business disruption — it may also compromise CUI, triggering notification requirements and potentially jeopardizing your contracts and security clearances.</p>",
        "whyItMatters": "<p>Ransomware represents an existential business risk for defense contractors. Implementing the controls required by CMMC — regular backups, endpoint protection, access controls, security awareness training — directly reduces your ransomware risk.</p>",
    },
    {
        "term": "Encryption",
        "definition": "<p>Encryption is the process of converting readable data into an unreadable format using mathematical algorithms, so that only authorized parties with the correct decryption key can access the original information. It protects data both 'at rest' (stored on drives) and 'in transit' (moving across networks).</p><p>For defense contractors, encryption is a fundamental requirement for protecting CUI. FIPS 140-2 validated encryption must be used — this means you can't use any encryption software; it must be cryptographic modules that have been tested and certified by NIST to meet federal standards.</p>",
        "whyItMatters": "<p>CMMC requires FIPS-validated encryption for protecting CUI both at rest and in transit. Using non-validated encryption methods — even strong ones — does not satisfy this requirement. Verify that your encryption solutions carry FIPS 140-2 (or 140-3) validation certificates.</p>",
    },
    {
        "term": "Firewall",
        "definition": "<p>A firewall is a network security device (hardware or software) that monitors and controls incoming and outgoing network traffic based on predetermined security rules. Think of it as a security guard at the entrance to your network — it checks every connection attempt and either allows or blocks it based on your policies.</p><p>Modern firewalls go beyond simple port-based filtering. Next-generation firewalls (NGFWs) can inspect the content of network traffic, identify applications, detect malware, and prevent intrusions — all at the network perimeter. Properly configured firewalls are a foundational defense for any network.</p>",
        "whyItMatters": "<p>Firewalls are a fundamental security control required by CMMC. Proper configuration — not just having a firewall, but maintaining tight rules that follow least-privilege principles — is what assessors will verify during your assessment.</p>",
    },
    {
        "term": "Virtual Private Network (VPN)",
        "definition": "<p>A Virtual Private Network (VPN) creates an encrypted tunnel between your device and a remote network, protecting your data as it travels across the internet. For businesses, VPNs allow employees to securely access company resources from remote locations as if they were physically in the office.</p><p>VPNs are critical for remote work security — without one, data transmitted between remote workers and your network can be intercepted. For CUI protection, VPN connections should use FIPS-validated encryption and require multi-factor authentication.</p>",
        "whyItMatters": "<p>If your employees access CUI remotely, a properly configured VPN with MFA and FIPS-validated encryption is required. CMMC assessors will verify that remote access is secured and that VPN configurations meet security requirements.</p>",
    },
    {
        "term": "Security Operations Center (SOC)",
        "definition": "<p>A Security Operations Center (SOC) is a centralized team — and often a physical facility — responsible for monitoring, detecting, analyzing, and responding to cybersecurity threats around the clock. The SOC watches your security systems, investigates alerts, and takes action when threats are detected.</p><p>For many small and mid-size defense contractors, building an internal 24/7 SOC isn't practical. Managed SOC services (often called MDR — Managed Detection and Response) provide this capability through a third-party provider who monitors your systems and responds to threats on your behalf.</p>",
        "whyItMatters": "<p>Continuous security monitoring is a CMMC requirement. Whether you build an internal capability or use a managed service, you need someone watching your systems and able to respond to security events in a timely manner.</p>",
    },
    {
        "term": "Security Information and Event Management (SIEM)",
        "definition": "<p>A Security Information and Event Management (SIEM) system collects, correlates, and analyzes log data from across your IT environment — servers, firewalls, endpoints, applications — to detect suspicious activity and security incidents. It's the central nervous system of your security monitoring, bringing together data from dozens of sources into one place where patterns and anomalies can be identified.</p><p>SIEMs enable you to meet audit logging and monitoring requirements by providing a centralized platform for log collection, retention, and analysis. Modern SIEMs include automated alerting, threat intelligence integration, and compliance reporting capabilities.</p>",
        "whyItMatters": "<p>CMMC requires audit logging, log review, and security monitoring. A SIEM is the most practical way to meet these requirements at scale, providing the centralized logging, correlation, and alerting capabilities that assessors expect to see.</p>",
    },
    {
        "term": "Intrusion Detection System (IDS)",
        "definition": "<p>An Intrusion Detection System (IDS) monitors network traffic or system activity for signs of malicious activity or policy violations. When suspicious activity is detected, the IDS generates an alert so security personnel can investigate. An IDS watches and warns — it detects threats but doesn't automatically block them.</p><p>IDS systems use signature-based detection (matching known attack patterns) and anomaly-based detection (identifying unusual behavior) to identify potential threats. They're a critical component of network security monitoring.</p>",
        "whyItMatters": "<p>Network monitoring and intrusion detection are requirements under CMMC. Having an IDS helps you detect attacks early, potentially before they can access or exfiltrate CUI from your systems.</p>",
    },
    {
        "term": "Intrusion Prevention System (IPS)",
        "definition": "<p>An Intrusion Prevention System (IPS) is similar to an IDS but goes a step further — it not only detects suspicious network activity but automatically takes action to block or prevent the threat. An IPS sits inline with your network traffic and can drop malicious packets, reset connections, or block attacking IP addresses in real time.</p><p>Most modern next-generation firewalls include IPS functionality built in. The key advantage over a standalone IDS is the automated response — threats are blocked without waiting for a human to review an alert and take manual action.</p>",
        "whyItMatters": "<p>Automated threat prevention reduces your response time from minutes or hours to milliseconds. IPS capabilities are expected as part of a mature network defense architecture under CMMC requirements.</p>",
    },
    {
        "term": "Endpoint Detection and Response (EDR)",
        "definition": "<p>Endpoint Detection and Response (EDR) is advanced security software that runs on individual computers and servers (endpoints) to continuously monitor for suspicious activity, detect threats that bypass traditional antivirus, and provide tools for investigating and responding to security incidents.</p><p>EDR goes far beyond traditional antivirus — it records detailed activity on each endpoint, uses behavioral analysis to detect novel threats, and provides security teams with the ability to investigate incidents, isolate compromised machines, and remediate threats remotely. Think of it as having a security camera and alarm system on every computer in your organization.</p>",
        "whyItMatters": "<p>Traditional antivirus alone is no longer sufficient to meet CMMC endpoint protection requirements. EDR provides the advanced detection and response capabilities needed to protect against modern threats targeting defense contractors.</p>",
    },
    {
        "term": "Extended Detection and Response (XDR)",
        "definition": "<p>Extended Detection and Response (XDR) expands on EDR by integrating security data from multiple sources — endpoints, networks, email, cloud services, and identity systems — into a unified platform for threat detection and response. Instead of managing separate security tools that each see only their piece of the picture, XDR correlates data across your entire environment.</p><p>XDR platforms provide security teams with a comprehensive view of threats as they move through an organization, from the initial phishing email to lateral movement across the network to data exfiltration. This integrated view enables faster, more accurate detection and response.</p>",
        "whyItMatters": "<p>XDR represents the evolution of security monitoring. While not explicitly required by CMMC, the integrated visibility XDR provides helps you meet multiple monitoring and detection requirements more effectively than siloed tools.</p>",
    },
    {
        "term": "Vulnerability",
        "definition": "<p>A vulnerability is a weakness in a system, software, process, or configuration that could be exploited by a threat actor to gain unauthorized access, disrupt operations, or steal data. Vulnerabilities can exist in software code (bugs), system configurations (misconfigurations), business processes (procedural gaps), or people (susceptibility to social engineering).</p><p>Vulnerabilities are identified through scanning, penetration testing, and vendor advisories. Once discovered, they're typically tracked using CVE identifiers and scored using CVSS to prioritize remediation. Managing vulnerabilities — finding them, prioritizing them, and fixing them — is a core cybersecurity activity.</p>",
        "whyItMatters": "<p>Vulnerability management is a fundamental CMMC requirement. Regularly scanning for and remediating vulnerabilities demonstrates that you're actively managing your security posture rather than waiting for an attacker to find your weaknesses.</p>",
    },
    {
        "term": "Threat",
        "definition": "<p>A threat is any circumstance or event with the potential to adversely impact your organization through unauthorized access, destruction, disclosure, or modification of information, or denial of service. Threats can come from external attackers (hackers, nation-states, criminal organizations), insiders (disgruntled employees, negligent staff), or natural events (disasters, power failures).</p><p>Understanding the threats your organization faces helps you prioritize your security investments. Not all threats are equal — a defense contractor faces different threats than a retail store. Nation-state actors actively target the defense industrial base to steal sensitive technology and military information.</p>",
        "whyItMatters": "<p>The DoD requires defense contractors to protect CUI specifically because of the threats facing the defense industrial base. Understanding that you are a target — not just theoretically, but actively — motivates the investment needed to meet compliance requirements.</p>",
    },
    {
        "term": "Risk",
        "definition": "<p>In cybersecurity, risk is the potential for loss or damage when a threat exploits a vulnerability. Risk is typically expressed as a combination of the likelihood that something bad will happen and the impact if it does. Risk management is about making informed decisions about which risks to mitigate, accept, transfer, or avoid.</p><p>Not every vulnerability needs to be fixed immediately, and not every threat needs the same level of defense. Risk assessment helps you prioritize — focusing your limited resources on the vulnerabilities most likely to be exploited and the threats that would cause the greatest harm to your business and your customers' missions.</p>",
        "whyItMatters": "<p>CMMC and RMF are risk-based frameworks. Demonstrating that you understand your risks and make informed security decisions — rather than just checking compliance boxes — shows maturity that assessors value and that genuinely protects your business.</p>",
    },
    {
        "term": "Incident Response",
        "definition": "<p>Incident response is the organized approach to detecting, containing, eradicating, and recovering from cybersecurity incidents. An incident response plan defines the roles, responsibilities, procedures, and communication protocols your organization follows when a security event occurs — who does what, when, and how.</p><p>A good incident response plan covers preparation (training, tools, contacts), detection and analysis (identifying what happened), containment (stopping the damage), eradication (removing the threat), recovery (restoring normal operations), and lessons learned (improving for next time). For defense contractors, the plan must also address DoD notification requirements for CUI incidents.</p>",
        "whyItMatters": "<p>CMMC requires a documented incident response capability and specific notification timelines for incidents involving CUI. Having a tested plan means the difference between a controlled response and organizational chaos when an incident occurs.</p>",
    },
    {
        "term": "Penetration Testing",
        "definition": "<p>Penetration testing (pen testing) is an authorized simulated cyber attack against your systems to identify security weaknesses before real attackers do. Professional penetration testers use the same tools and techniques as malicious hackers — but with your permission and under controlled conditions — to find vulnerabilities in your networks, applications, and physical security.</p><p>Pen tests go beyond automated vulnerability scanning by chaining multiple vulnerabilities together and using creative approaches to breach your defenses, just as a real attacker would. The results show you not just individual vulnerabilities, but how they could be exploited together to compromise your systems.</p>",
        "whyItMatters": "<p>While not explicitly required at CMMC Level 2, penetration testing is a best practice that reveals gaps automated tools miss. It provides real-world validation of your security controls and helps prioritize remediation based on actual exploitability.</p>",
    },
    {
        "term": "Red Team",
        "definition": "<p>A red team is a group of security professionals who simulate adversary tactics, techniques, and procedures to test an organization's defenses. Unlike penetration testing, which typically focuses on finding technical vulnerabilities, red teaming takes a broader approach — testing people, processes, and technology together, often using social engineering, physical intrusion, and sophisticated multi-stage attack scenarios.</p><p>Red team exercises evaluate how well your entire security program performs under realistic attack conditions, including how quickly your team detects the intrusion, how effectively they respond, and whether your security controls work as intended.</p>",
        "whyItMatters": "<p>Red team exercises provide the most realistic test of your security program. While expensive, they reveal systemic weaknesses that individual control assessments miss and validate whether your security investments actually work against real-world attack techniques.</p>",
    },
    {
        "term": "Blue Team",
        "definition": "<p>A blue team is the defensive side of cybersecurity — the people responsible for maintaining and improving an organization's security defenses, detecting threats, and responding to incidents. In a red team/blue team exercise, the blue team defends against the red team's simulated attacks.</p><p>In everyday operations, the blue team includes your security analysts, incident responders, and system administrators who monitor networks, analyze alerts, patch vulnerabilities, and maintain security controls. They're the people keeping your systems secure day to day.</p>",
        "whyItMatters": "<p>Your blue team capabilities — whether internal staff or managed services — determine how quickly you can detect and respond to real threats. Investing in blue team skills and tools is investing in your operational security posture.</p>",
    },
    {
        "term": "Purple Team",
        "definition": "<p>A purple team combines red team (offensive) and blue team (defensive) activities in a collaborative exercise where both sides work together. Instead of the red team secretly attacking and the blue team trying to detect them, purple teaming involves the attackers and defenders sharing information in real time to maximize learning and improve defenses.</p><p>Purple team exercises are highly efficient for improving security — the red team demonstrates specific attack techniques, and the blue team immediately works on detection and prevention, with both sides iterating together. This collaborative approach builds capability faster than adversarial exercises alone.</p>",
        "whyItMatters": "<p>Purple teaming is a cost-effective way to improve your security capabilities, especially for smaller organizations that can't afford separate red and blue team exercises. The collaborative approach accelerates security improvement and builds team skills simultaneously.</p>",
    },
    {
        "term": "Access Control",
        "definition": "<p>Access control is the security discipline of managing who can access your systems, data, and facilities — and what they can do once they have access. It encompasses policies, procedures, and technical mechanisms that ensure only authorized users can access specific resources, and only to the extent required for their job function.</p><p>Access control includes user authentication (verifying identity), authorization (determining what a user is allowed to do), and accountability (tracking what users actually did). Technical implementations include user accounts, group policies, file permissions, network access controls, and physical access systems like badge readers.</p>",
        "whyItMatters": "<p>Access Control is the largest domain in both CMMC and NIST SP 800-171, with the most requirements. Getting access control right — knowing who has access to what and ensuring it's only what they need — is foundational to protecting CUI.</p>",
    },
    {
        "term": "Least Privilege",
        "definition": "<p>Least privilege is the security principle that every user, program, and system process should have only the minimum access rights needed to perform their specific job function — nothing more. If an employee doesn't need administrator access to do their work, they shouldn't have it. If a system doesn't need access to CUI data, it shouldn't be able to reach it.</p><p>Implementing least privilege means regularly reviewing access rights, removing unnecessary permissions, using standard user accounts for daily work (not admin accounts), and segmenting access to sensitive data. It limits the damage an attacker can do if they compromise any single account or system.</p>",
        "whyItMatters": "<p>Least privilege is a core requirement across CMMC and NIST frameworks. Many breaches escalate because compromised accounts had more access than needed. Enforcing least privilege is one of the most effective ways to limit the blast radius of a security incident.</p>",
    },
    {
        "term": "Defense in Depth",
        "definition": "<p>Defense in depth is the strategy of layering multiple security controls so that if one fails, others continue to protect your systems and data. Rather than relying on a single defensive measure (like just a firewall), you implement multiple overlapping protections — firewalls, endpoint protection, access controls, encryption, monitoring, training, and physical security.</p><p>The idea comes from military strategy: multiple defensive lines are harder to breach than a single wall. In cybersecurity, this means an attacker who gets past your firewall still faces endpoint protection, who then faces access controls, who then faces encryption, and so on. No single control is perfect, but together they create a formidable defense.</p>",
        "whyItMatters": "<p>CMMC's comprehensive set of security requirements embodies the defense-in-depth philosophy. Understanding this principle helps you see how individual controls work together as a system and why no single security product can replace a layered security program.</p>",
    },
    {
        "term": "Demilitarized Zone (DMZ)",
        "definition": "<p>A DMZ (Demilitarized Zone) is a network segment that sits between your internal network and the internet, providing an additional layer of security for systems that need to be accessible from outside your organization. Web servers, email servers, and VPN gateways are typically placed in the DMZ, where they can serve external users without giving those users direct access to your internal network.</p><p>The DMZ is protected by firewalls on both sides — one facing the internet and one facing your internal network. If a system in the DMZ is compromised, the attacker still has to breach the inner firewall to reach your internal systems and data.</p>",
        "whyItMatters": "<p>Proper network segmentation, including DMZ architecture, is part of the system and communications protection requirements under CMMC. Keeping internet-facing services isolated from your CUI environment reduces the attack surface significantly.</p>",
    },
    {
        "term": "TLS/SSL",
        "definition": "<p>TLS (Transport Layer Security) and its predecessor SSL (Secure Sockets Layer) are cryptographic protocols that encrypt data transmitted over networks. When you see 'https://' in a web address or a lock icon in your browser, TLS is protecting that connection. It ensures that data traveling between your browser and a website (or between any two systems) cannot be read or tampered with by anyone intercepting the traffic.</p><p>TLS protects data 'in transit' — while it's moving across networks. For compliance purposes, you should use TLS 1.2 or higher (older versions have known vulnerabilities) and ensure that the underlying cryptographic implementation is FIPS-validated when protecting CUI.</p>",
        "whyItMatters": "<p>CMMC requires encryption of CUI in transit using FIPS-validated cryptography. Ensuring all network communications carrying CUI use TLS 1.2+ with FIPS-validated implementations is a concrete, auditable requirement.</p>",
    },
    {
        "term": "Patch Management",
        "definition": "<p>Patch management is the process of identifying, testing, and applying software updates (patches) to fix security vulnerabilities and bugs across your systems. Software vendors regularly release patches to address newly discovered vulnerabilities — applying these patches promptly prevents attackers from exploiting known weaknesses.</p><p>Effective patch management requires an inventory of all software in your environment, a process for identifying available patches, a testing procedure to ensure patches don't break critical systems, and a deployment timeline that balances speed against operational risk. For DoD environments, IAVM notices drive specific patching deadlines.</p>",
        "whyItMatters": "<p>Timely patch management is a core CMMC requirement. Unpatched systems are one of the most common attack vectors — attackers actively scan for known vulnerabilities. A reliable patch management process is fundamental to your security posture.</p>",
    },
    {
        "term": "Endpoint Protection",
        "definition": "<p>Endpoint protection refers to the security solutions deployed on individual devices (endpoints) — laptops, desktops, servers, mobile devices — to protect them from malware, unauthorized access, and other threats. Modern endpoint protection has evolved far beyond traditional antivirus to include behavioral detection, application control, device control, and automated response capabilities.</p><p>Endpoint protection platforms (EPPs) and endpoint detection and response (EDR) solutions work together to prevent known threats, detect novel attacks, and provide tools for investigation and remediation. Every endpoint in your CUI environment needs adequate protection.</p>",
        "whyItMatters": "<p>CMMC requires malicious code protection on all organizational systems. Deploying and properly managing endpoint protection across every device that handles CUI is a fundamental compliance requirement that assessors will verify.</p>",
    },
    {
        "term": "Data Loss Prevention (DLP)",
        "definition": "<p>Data Loss Prevention (DLP) refers to tools and strategies that prevent sensitive data from leaving your organization through unauthorized channels. DLP solutions monitor data in motion (network traffic), data at rest (stored files), and data in use (clipboard, screen capture) to detect and block unauthorized transfers of sensitive information.</p><p>For defense contractors, DLP helps prevent CUI from being emailed to personal accounts, uploaded to unauthorized cloud services, copied to USB drives, or otherwise leaving your controlled environment. DLP policies can warn users, block transfers, or alert security teams depending on the severity.</p>",
        "whyItMatters": "<p>Preventing unauthorized CUI disclosure is a core CMMC objective. DLP tools provide technical enforcement of your data handling policies, helping you demonstrate that you actively prevent data exfiltration rather than relying solely on policy and training.</p>",
    },
    {
        "term": "Identity and Access Management (IAM)",
        "definition": "<p>Identity and Access Management (IAM) is the framework of policies, processes, and technologies for managing digital identities and controlling access to resources. IAM encompasses user provisioning (creating accounts), authentication (verifying identity), authorization (granting permissions), and deprovisioning (removing access when it's no longer needed).</p><p>A mature IAM program ensures that every person in your organization has exactly the access they need — no more, no less — and that access is promptly adjusted when roles change or employment ends. IAM systems often integrate with HR systems to automate access lifecycle management.</p>",
        "whyItMatters": "<p>Strong IAM is foundational to multiple CMMC domains. Knowing who has access to your systems and CUI, ensuring access is appropriate, and removing it promptly when no longer needed are requirements assessors will thoroughly evaluate.</p>",
    },
    {
        "term": "Privileged Access Management (PAM)",
        "definition": "<p>Privileged Access Management (PAM) focuses specifically on controlling, monitoring, and auditing accounts with elevated privileges — administrator accounts, service accounts, and root accounts that have broad access to systems and data. Because privileged accounts can do the most damage if compromised, they require extra security measures.</p><p>PAM solutions typically include privileged credential vaulting (storing admin passwords securely), just-in-time access (granting privileges only when needed and automatically revoking them), session recording (capturing what administrators do), and behavioral analytics to detect misuse of privileged accounts.</p>",
        "whyItMatters": "<p>Protecting privileged accounts is critical under CMMC. Compromised admin credentials give attackers the keys to your kingdom. PAM controls demonstrate that you manage your most powerful accounts with the extra rigor they require.</p>",
    },
    {
        "term": "Supply Chain Risk Management (SCRM)",
        "definition": "<p>Supply Chain Risk Management is the discipline of identifying, assessing, and mitigating cybersecurity risks introduced through your vendors, suppliers, and service providers. Your security is only as strong as the weakest link in your supply chain — a compromised vendor can provide an attacker with a path into your systems.</p><p>SCRM involves vetting vendors' security practices, including cybersecurity requirements in contracts, monitoring vendor security posture, and having contingency plans if a vendor is compromised. The SolarWinds attack demonstrated how devastating supply chain compromises can be.</p>",
        "whyItMatters": "<p>CMMC includes supply chain risk management requirements, and the DoD increasingly scrutinizes contractor supply chains. Understanding and managing the cybersecurity risks your vendors introduce is both a compliance requirement and a practical business necessity.</p>",
    },
    {
        "term": "Insider Threat",
        "definition": "<p>An insider threat is a security risk that comes from within your organization — employees, contractors, or business partners who have legitimate access to your systems and data. Insider threats can be malicious (intentional data theft, sabotage) or unintentional (accidental data exposure, falling for phishing, negligent handling of CUI).</p><p>Insider threats are particularly dangerous because insiders already have authorized access, making their activities harder to detect than external attacks. An effective insider threat program combines technical monitoring (user activity monitoring, DLP) with organizational measures (background checks, security awareness, reporting mechanisms).</p>",
        "whyItMatters": "<p>The DoD considers insider threat a significant risk to CUI protection. CMMC includes requirements for personnel security, awareness training, and monitoring that address insider threat. Having an insider threat program demonstrates mature security governance.</p>",
    },
    {
        "term": "Social Engineering",
        "definition": "<p>Social engineering is the use of psychological manipulation to trick people into making security mistakes or giving away sensitive information. Rather than attacking technical systems directly, social engineers exploit human nature — trust, helpfulness, urgency, fear, curiosity — to bypass security controls.</p><p>Social engineering attacks include phishing emails, pretexting (creating a fabricated scenario), baiting (leaving infected USB drives), tailgating (following someone through a secure door), and vishing (voice phishing over the phone). These attacks target the human element — often the weakest link in any security program.</p>",
        "whyItMatters": "<p>Security awareness training is a CMMC requirement because technology alone cannot stop social engineering. Teaching your employees to recognize and resist manipulation attempts is essential for protecting CUI from human-targeted attacks.</p>",
    },
    {
        "term": "Malware",
        "definition": "<p>Malware (malicious software) is any software designed to harm, exploit, or otherwise compromise computer systems. The term encompasses viruses, worms, ransomware, spyware, trojans, rootkits, and other malicious programs. Malware can steal data, encrypt files for ransom, spy on users, or give attackers remote control of infected systems.</p><p>Malware reaches your systems through email attachments, malicious websites, infected USB drives, compromised software updates, and exploitation of unpatched vulnerabilities. Defending against malware requires layered protections: email filtering, endpoint protection, application whitelisting, patch management, and user awareness training.</p>",
        "whyItMatters": "<p>Malware protection is explicitly required by CMMC. Implementing and maintaining effective anti-malware defenses — and keeping them updated — is a fundamental security control that assessors will verify on every endpoint in your CUI environment.</p>",
    },
    {
        "term": "Spyware",
        "definition": "<p>Spyware is a type of malware that secretly monitors and collects information about a user's activities without their knowledge or consent. Spyware can record keystrokes (keyloggers), capture screenshots, monitor web browsing, access webcams and microphones, and exfiltrate collected data to attackers.</p><p>For defense contractors, spyware poses a particularly severe threat because it can capture CUI as it's being viewed, typed, or discussed. Spyware can be installed through phishing, drive-by downloads, or bundled with seemingly legitimate software.</p>",
        "whyItMatters": "<p>Spyware can silently capture CUI even from systems with strong access controls. Endpoint protection solutions that detect behavioral indicators of spyware — not just known signatures — are essential for protecting sensitive defense information.</p>",
    },
    {
        "term": "Trojan",
        "definition": "<p>A Trojan (or Trojan horse) is malware disguised as legitimate software. Unlike viruses and worms, Trojans don't self-replicate — they rely on tricking users into installing them by appearing to be useful programs, documents, or updates. Once installed, a Trojan can give attackers remote access, steal data, install additional malware, or perform other malicious actions.</p><p>Trojans are commonly delivered through phishing emails with attachments, fake software download sites, or malicious links. Remote Access Trojans (RATs) are particularly dangerous because they give attackers full, hidden control of compromised systems.</p>",
        "whyItMatters": "<p>Trojans often bypass basic security controls because users willingly install them. Application whitelisting, email filtering, and user training — all CMMC requirements — work together to prevent Trojan infections in your environment.</p>",
    },
    {
        "term": "Rootkit",
        "definition": "<p>A rootkit is a particularly insidious type of malware designed to hide its presence and the presence of other malicious software on a system. Rootkits modify the operating system itself to conceal malicious processes, files, and network connections from security tools and system administrators.</p><p>Rootkits are difficult to detect because they operate at a deep level within the operating system, often hiding from antivirus software and standard security tools. Detection typically requires specialized tools or analysis from a clean, trusted system. Some rootkits infect the boot process or firmware, surviving even operating system reinstallation.</p>",
        "whyItMatters": "<p>Rootkits represent an advanced threat that can persist undetected for extended periods. Advanced endpoint protection with behavioral analysis and boot-level integrity checking helps detect rootkits before they can silently exfiltrate CUI.</p>",
    },
    {
        "term": "Botnet",
        "definition": "<p>A botnet is a network of compromised computers (bots or zombies) controlled remotely by an attacker. Infected computers — which can include servers, desktops, IoT devices, and even phones — receive commands from a central control server and carry out coordinated malicious activities like DDoS attacks, spam campaigns, or credential stuffing attacks.</p><p>Your systems can become part of a botnet without your knowledge if they're infected with bot malware. The bot software runs quietly in the background, waiting for commands from the attacker while using your systems' resources and network bandwidth for malicious purposes.</p>",
        "whyItMatters": "<p>If your systems are recruited into a botnet, they're compromised — meaning CUI may also be at risk. Network monitoring and endpoint protection required by CMMC help detect the command-and-control communications that characterize botnet infections.</p>",
    },
    {
        "term": "Distributed Denial of Service (DDoS)",
        "definition": "<p>A Distributed Denial of Service (DDoS) attack overwhelms a system, network, or service with massive amounts of traffic from many sources simultaneously, making it unavailable to legitimate users. Unlike a simple denial of service (DoS) attack from a single source, DDoS attacks use thousands or millions of compromised systems (a botnet) to generate traffic that's difficult to filter or block.</p><p>DDoS attacks don't steal data — they disrupt operations. For defense contractors, service disruption can mean missed deadlines, inability to access critical systems, and potential contract performance issues.</p>",
        "whyItMatters": "<p>While CMMC focuses primarily on confidentiality, availability is also part of the security triad. Understanding DDoS risks helps you plan for business continuity and ensure critical services remain accessible during an attack.</p>",
    },
    {
        "term": "SQL Injection",
        "definition": "<p>SQL Injection is a web application attack where an attacker inserts malicious database commands into input fields (login forms, search boxes, URL parameters) to manipulate the application's database. If successful, the attacker can read, modify, or delete data, bypass authentication, or even take control of the database server.</p><p>SQL Injection has been one of the most common and dangerous web application vulnerabilities for decades. It's preventable through proper coding practices — primarily using parameterized queries instead of building SQL statements from user input.</p>",
        "whyItMatters": "<p>If your company develops web applications that handle CUI, protecting them from injection attacks is critical. Application security testing and secure coding practices are part of your overall security program under CMMC.</p>",
    },
    {
        "term": "Cross-Site Scripting (XSS)",
        "definition": "<p>Cross-Site Scripting (XSS) is a web application vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. When a user visits the compromised page, the malicious script runs in their browser, potentially stealing session cookies, capturing credentials, or redirecting users to phishing sites.</p><p>XSS attacks exploit the trust a user's browser places in the website. There are several types: stored XSS (malicious script saved on the server), reflected XSS (script included in a link or request), and DOM-based XSS (script manipulates the page's document object model).</p>",
        "whyItMatters": "<p>If you develop web applications for DoD or that handle CUI, protecting them from XSS and other injection attacks is part of your security responsibility. Regular application security testing helps identify and fix these vulnerabilities before attackers find them.</p>",
    },
    {
        "term": "OWASP",
        "definition": "<p>The Open Web Application Security Project (OWASP) is a nonprofit organization that produces freely available tools, documentation, and standards for web application security. OWASP is best known for the OWASP Top 10 — a regularly updated list of the most critical web application security risks.</p><p>OWASP resources include testing guides, secure coding practices, security tools, and educational materials. The OWASP Top 10 is widely used as a baseline for web application security programs and is referenced by many compliance frameworks.</p>",
        "whyItMatters": "<p>If your company develops web applications, OWASP resources provide practical guidance for building secure code. Using the OWASP Top 10 as a minimum testing baseline demonstrates application security diligence to assessors and customers.</p>",
    },
    {
        "term": "Common Vulnerabilities and Exposures (CVE)",
        "definition": "<p>CVE (Common Vulnerabilities and Exposures) is a standardized system for identifying and naming publicly known cybersecurity vulnerabilities. Each vulnerability receives a unique CVE identifier (like CVE-2024-12345) that allows security professionals, vendors, and tools to reference the same vulnerability unambiguously.</p><p>CVE identifiers are assigned by CVE Numbering Authorities (CNAs) and maintained in the CVE database. When a vendor releases a security patch, they reference the CVE(s) it addresses, and vulnerability scanners use CVE identifiers to report which known vulnerabilities affect your systems.</p>",
        "whyItMatters": "<p>CVE identifiers are the common language of vulnerability management. When your scanning tools report CVE findings, you can quickly research the vulnerability, determine its severity, and find remediation guidance — all essential activities for CMMC compliance.</p>",
    },
    {
        "term": "Common Vulnerability Scoring System (CVSS)",
        "definition": "<p>The Common Vulnerability Scoring System (CVSS) provides a standardized way to rate the severity of security vulnerabilities on a scale of 0 to 10. The score considers factors like how easy the vulnerability is to exploit, whether it requires user interaction, what access an attacker needs, and the potential impact on confidentiality, integrity, and availability.</p><p>CVSS scores help you prioritize which vulnerabilities to fix first. A CVSS 9.8 (Critical) vulnerability that's remotely exploitable deserves immediate attention, while a CVSS 3.1 (Low) that requires physical access might be addressed during your regular patch cycle.</p>",
        "whyItMatters": "<p>CVSS scores are central to vulnerability prioritization under CMMC. Using CVSS to triage and prioritize remediation demonstrates a risk-based approach to vulnerability management that assessors expect to see.</p>",
    },
    {
        "term": "National Vulnerability Database (NVD)",
        "definition": "<p>The National Vulnerability Database (NVD) is the U.S. government's comprehensive repository of vulnerability information, maintained by NIST. The NVD builds on the CVE system by adding CVSS severity scores, affected product information, fix references, and detailed technical analysis for each vulnerability.</p><p>The NVD is a free, publicly accessible resource that security professionals use to research vulnerabilities, understand their impact, and find remediation guidance. Vulnerability scanning tools reference the NVD to provide context about the findings they report.</p>",
        "whyItMatters": "<p>The NVD is an authoritative source for vulnerability intelligence. Referencing NVD data when managing your vulnerability program demonstrates use of a trusted, government-backed resource for security decision-making.</p>",
    },
    {
        "term": "Exploit",
        "definition": "<p>An exploit is a piece of code, technique, or method that takes advantage of a vulnerability to cause unintended behavior in a system — typically to gain unauthorized access, escalate privileges, or execute malicious code. Exploits are the 'how' of an attack: the vulnerability is the weakness, the exploit is the tool or technique used to take advantage of it.</p><p>Exploits range from simple scripts to sophisticated multi-stage attack chains. They can target software bugs, configuration errors, or design flaws. Once a vulnerability is discovered and an exploit is developed, the window for defenders to patch before attackers strike begins — making timely patch management critical.</p>",
        "whyItMatters": "<p>When vulnerability scanners identify issues in your environment, the existence of known exploits dramatically increases the urgency of remediation. Vulnerabilities with active exploits are the ones attackers are most likely to use against you.</p>",
    },
    {
        "term": "Zero-Day",
        "definition": "<p>A zero-day is a vulnerability that is unknown to the software vendor and for which no patch exists. The name comes from the fact that developers have had 'zero days' to fix the problem when it's first discovered or exploited. Zero-day attacks exploit these unknown vulnerabilities, making them particularly dangerous because no specific defense exists yet.</p><p>Zero-day vulnerabilities are valuable to attackers (and to some governments) because they can't be blocked by signature-based security tools that rely on knowing about specific threats. Defense against zero-days requires behavioral detection, application whitelisting, network segmentation, and defense-in-depth strategies.</p>",
        "whyItMatters": "<p>Zero-day attacks highlight why defense in depth is essential — you can't patch what you don't know about. The layered security controls required by CMMC help protect against zero-day exploits by providing multiple defensive barriers beyond just patching.</p>",
    },
    {
        "term": "Advanced Persistent Threat (APT)",
        "definition": "<p>An Advanced Persistent Threat (APT) is a sophisticated, prolonged cyber attack campaign — typically conducted by nation-state actors or well-funded criminal groups — that targets a specific organization over an extended period. APTs combine advanced technical skills, significant resources, and patient, methodical approaches to infiltrate, persist, and extract information from target networks.</p><p>Unlike opportunistic attacks, APTs are targeted and persistent. Attackers may spend months or years inside a network, carefully avoiding detection while systematically accessing and exfiltrating sensitive data. Defense contractors are prime APT targets because of the military and technological intelligence they hold.</p>",
        "whyItMatters": "<p>APTs are the primary threat driving CMMC requirements. Nation-state actors actively target the defense industrial base to steal CUI. Understanding that your company faces this level of threat motivates the comprehensive security program CMMC requires.</p>",
    },
    {
        "term": "Indicator of Compromise (IOC)",
        "definition": "<p>An Indicator of Compromise (IOC) is a piece of forensic evidence that suggests a system or network has been breached. IOCs include suspicious IP addresses, unusual file hashes, malicious domain names, unexpected registry changes, abnormal network traffic patterns, and other artifacts that indicate malicious activity has occurred.</p><p>Security teams use IOCs to detect breaches, investigate incidents, and hunt for threats in their environment. Sharing IOCs between organizations — through threat intelligence feeds and information sharing communities — helps everyone detect threats faster.</p>",
        "whyItMatters": "<p>The ability to detect and respond to IOCs is part of the monitoring and incident response capabilities CMMC requires. Integrating threat intelligence feeds with IOC data into your security monitoring improves your ability to detect compromises early.</p>",
    },
    {
        "term": "Tactics, Techniques, and Procedures (TTPs)",
        "definition": "<p>Tactics, Techniques, and Procedures (TTPs) describe the behavior patterns of cyber threat actors — how they operate, what methods they use, and the specific steps they follow during attacks. Tactics are the high-level goals (initial access, persistence, exfiltration), techniques are the general methods used to achieve those goals, and procedures are the specific implementations.</p><p>Understanding TTPs is more valuable than knowing specific IOCs because TTPs represent the adversary's playbook — they change less frequently than specific indicators and provide deeper insight into how to defend against particular threat actors.</p>",
        "whyItMatters": "<p>Understanding the TTPs used against the defense industrial base helps you focus your defenses on the attack methods you're most likely to face. This threat-informed approach to security makes your CMMC implementation more effective at actually stopping real attacks.</p>",
    },
    {
        "term": "MITRE ATT&CK",
        "definition": "<p>MITRE ATT&CK is a comprehensive knowledge base of adversary tactics, techniques, and procedures based on real-world observations of cyber attacks. It provides a common language and framework for describing how attackers operate — from initial access through persistence, privilege escalation, defense evasion, lateral movement, and data exfiltration.</p><p>Security teams use ATT&CK to evaluate their defenses against known attack techniques, identify coverage gaps, and improve detection capabilities. Many security products now map their detection capabilities to ATT&CK techniques, making it easier to understand what threats your tools can and cannot detect.</p>",
        "whyItMatters": "<p>Using ATT&CK to evaluate your security controls against real-world attack techniques helps ensure your CMMC implementation actually works — not just on paper, but against the specific methods adversaries use to target defense contractors.</p>",
    },
    {
        "term": "Cyber Kill Chain",
        "definition": "<p>The Cyber Kill Chain is a framework developed by Lockheed Martin that describes the stages of a cyber attack from initial reconnaissance through achieving the attacker's objective. The seven stages are: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, and Actions on Objectives.</p><p>The kill chain concept helps defenders understand that attacks are multi-stage processes, and disrupting any stage prevents the attack from succeeding. Your security controls should provide detection and prevention at multiple stages, creating multiple opportunities to stop an attack before the attacker achieves their goal.</p>",
        "whyItMatters": "<p>The kill chain framework helps you evaluate whether your security controls provide coverage at each attack stage. CMMC requirements span the entire kill chain — from perimeter defenses to monitoring to incident response — creating layered opportunities to detect and stop attacks.</p>",
    },
    {
        "term": "Threat Intelligence",
        "definition": "<p>Threat intelligence is evidence-based knowledge about existing or emerging cyber threats — including the actors, their motivations, capabilities, indicators of compromise, and tactics. Threat intelligence transforms raw data about threats into actionable information that helps you make better security decisions and prioritize your defenses.</p><p>Threat intelligence comes in several forms: strategic (high-level trends and risks for leadership), tactical (TTPs and attack methods for security teams), operational (details about specific campaigns), and technical (IOCs for security tools). For defense contractors, industry-specific threat intelligence about APT groups targeting the DIB is particularly valuable.</p>",
        "whyItMatters": "<p>Integrating threat intelligence into your security program helps you focus on the threats most relevant to defense contractors. This threat-informed approach makes your security investments more effective and demonstrates risk management maturity to assessors.</p>",
    },
    {
        "term": "Incident Handling",
        "definition": "<p>Incident handling is the operational execution of your incident response plan — the actual process of detecting, analyzing, containing, eradicating, and recovering from a security incident when it occurs. While incident response is the broader program (planning, preparation, policy), incident handling is the hands-on work of managing a specific incident.</p><p>Effective incident handling requires clear procedures, trained personnel, appropriate tools, and pre-established communication channels. For CUI incidents, handling procedures must include notifications to the DoD within 72 hours and preservation of forensic evidence.</p>",
        "whyItMatters": "<p>CMMC requires not just an incident response plan but demonstrated capability to handle incidents. Practicing incident handling through tabletop exercises and simulations ensures your team can execute effectively when a real incident occurs.</p>",
    },
    {
        "term": "Digital Forensics",
        "definition": "<p>Digital forensics is the process of collecting, preserving, analyzing, and presenting digital evidence from computers, networks, and other electronic devices. In the context of cybersecurity, forensics is used to investigate security incidents — determining what happened, how it happened, what was affected, and who was responsible.</p><p>Forensic investigations follow strict procedures to maintain evidence integrity, ensuring findings can withstand legal scrutiny. For defense contractors, forensic capabilities are important for investigating CUI breaches and providing the DoD with accurate incident reports.</p>",
        "whyItMatters": "<p>When a security incident involves CUI, you may need forensic evidence to determine the scope of the breach and fulfill DoD reporting requirements. Having forensic capabilities — or a relationship with a forensic provider — ensures you can investigate incidents thoroughly.</p>",
    },
    {
        "term": "Business Continuity",
        "definition": "<p>Business continuity planning ensures your organization can continue operating during and after a significant disruption — whether a cyber attack, natural disaster, infrastructure failure, or pandemic. A business continuity plan (BCP) identifies critical business functions, the resources needed to support them, and the procedures for maintaining or quickly restoring operations.</p><p>For defense contractors, business continuity is about ensuring you can continue to perform on your contracts even when things go wrong. This includes having backup systems, alternative work locations, communication plans, and recovery procedures that keep your mission-critical operations running.</p>",
        "whyItMatters": "<p>Business continuity directly impacts your ability to perform on DoD contracts. A cyber attack that takes you offline for weeks doesn't just affect your security — it affects your contractual obligations, your reputation, and potentially national security missions that depend on your deliverables.</p>",
    },
    {
        "term": "Disaster Recovery",
        "definition": "<p>Disaster recovery (DR) is the set of policies, tools, and procedures for recovering technology infrastructure and systems after a significant disruption. While business continuity focuses on keeping operations going, disaster recovery focuses specifically on restoring IT systems — servers, networks, data, and applications — to their normal operating state.</p><p>Key elements of disaster recovery include regular data backups, backup testing (proving you can actually restore from backups), recovery time objectives (how fast you need systems back), and recovery point objectives (how much data loss is acceptable). Your DR plan should be tested regularly through tabletop exercises and actual recovery drills.</p>",
        "whyItMatters": "<p>CMMC requires system backup and recovery capabilities. Having a tested disaster recovery plan ensures you can restore your CUI environment after a ransomware attack, hardware failure, or other destructive event — protecting both your business and the sensitive data you handle.</p>",
    },
    {
        "term": "Backup",
        "definition": "<p>A backup is a copy of your data stored separately from the original so it can be restored if the original is lost, corrupted, or destroyed. Effective backup strategies follow the 3-2-1 rule: maintain at least 3 copies of your data, on 2 different types of media, with 1 copy stored offsite or in the cloud.</p><p>For defense contractors handling CUI, backups must be protected with the same security controls as the original data — encryption, access controls, and secure storage. Backups are your last line of defense against ransomware and data destruction attacks.</p>",
        "whyItMatters": "<p>CMMC requires regular system backups. But a backup is only useful if it works — regular backup testing and verified restores are essential. An untested backup is a backup you can't trust when you need it most.</p>",
    },
    {
        "term": "Compliance",
        "definition": "<p>Compliance is the state of meeting the requirements set by laws, regulations, standards, or contractual obligations. In the cybersecurity context for defense contractors, compliance primarily involves meeting CMMC requirements, NIST standards, DFARS clauses, and other DoD cybersecurity mandates.</p><p>Compliance is important but it's a floor, not a ceiling. Meeting compliance requirements doesn't guarantee security — it means you've implemented a minimum set of controls deemed necessary by the governing body. True security goes beyond compliance to address your specific threats and risks.</p>",
        "whyItMatters": "<p>For defense contractors, compliance isn't optional — it's a contractual requirement and increasingly a prerequisite for winning new work. But view compliance as the starting point, not the finish line. A compliant organization that doesn't actually practice good security is one incident away from catastrophe.</p>",
    },
    {
        "term": "Audit",
        "definition": "<p>A security audit is a systematic evaluation of an organization's security program, policies, and controls against established criteria. Audits can be internal (conducted by your own team) or external (conducted by independent auditors), and they evaluate whether your security program meets specific standards and is operating effectively.</p><p>Audits examine documentation, processes, and technical implementations. Unlike assessments that may be collaborative, audits are typically more formal and produce findings that require documented corrective actions. Regular internal audits help you identify and fix issues before external auditors or assessors find them.</p>",
        "whyItMatters": "<p>Regular security audits are part of CMMC's ongoing assessment requirements. Conducting internal audits between official assessments helps you maintain continuous compliance and catch drift before it becomes a significant gap.</p>",
    },
    {
        "term": "Governance",
        "definition": "<p>Security governance is the framework of policies, roles, responsibilities, and oversight that ensures your cybersecurity program aligns with your business objectives and regulatory requirements. It's the management layer that directs and controls your security program — setting strategy, allocating resources, defining accountability, and ensuring compliance.</p><p>Good governance means leadership is engaged in cybersecurity decisions, policies are documented and enforced, roles and responsibilities are clearly defined, and the security program is regularly reviewed and improved. Without governance, even well-funded security programs lack direction and accountability.</p>",
        "whyItMatters": "<p>CMMC assessors evaluate not just your technical controls but your organizational governance. Having clear policies, defined roles, leadership engagement, and regular program reviews demonstrates the management commitment needed to sustain a security program long-term.</p>",
    },
    {
        "term": "CIA Triad",
        "definition": "<p>The CIA Triad — Confidentiality, Integrity, and Availability — is the foundational model for information security. Confidentiality means ensuring information is accessible only to authorized people. Integrity means ensuring information is accurate, complete, and hasn't been tampered with. Availability means ensuring information and systems are accessible when needed.</p><p>Every security decision, control, and assessment ultimately maps back to protecting one or more of these three properties. The CIA Triad provides a simple framework for evaluating security risks and prioritizing controls based on which properties are most important for specific data and systems.</p>",
        "whyItMatters": "<p>The CIA Triad is the conceptual foundation of your entire security program. For defense contractors, confidentiality of CUI is paramount, but you must also ensure data integrity (it hasn't been altered) and availability (systems work when needed for mission support).</p>",
    },
    {
        "term": "Authentication",
        "definition": "<p>Authentication is the process of verifying that a user, device, or system is who or what it claims to be. It answers the question 'Are you really who you say you are?' The most common form is username and password, but stronger methods include multi-factor authentication (MFA), biometrics, and certificate-based authentication (like the DoD's CAC).</p><p>Authentication is distinct from authorization (which determines what you're allowed to do after your identity is verified). Strong authentication prevents unauthorized individuals from accessing your systems by ensuring only verified identities gain entry.</p>",
        "whyItMatters": "<p>CMMC requires strong authentication mechanisms, including multi-factor authentication for remote access and privileged accounts. Weak authentication — simple passwords, shared accounts, no MFA — is one of the most common and easily exploited security weaknesses.</p>",
    },
    {
        "term": "Authorization",
        "definition": "<p>Authorization is the process of determining what a verified user is permitted to do — what resources they can access, what actions they can perform, and what data they can view or modify. Authorization happens after authentication: first the system confirms your identity, then it checks what permissions your identity has been granted.</p><p>Authorization is implemented through access control mechanisms like role-based access control (RBAC), where permissions are assigned based on job roles, or attribute-based access control (ABAC), where access decisions consider multiple factors like user role, time of day, location, and data sensitivity.</p>",
        "whyItMatters": "<p>Proper authorization controls — ensuring users can only access what they need for their job — are a CMMC requirement under access control and least privilege principles. Overly permissive authorization is a common finding during assessments.</p>",
    },
    {
        "term": "Non-Repudiation",
        "definition": "<p>Non-repudiation ensures that a party cannot deny having performed a specific action — such as sending a message, signing a document, or authorizing a transaction. It provides proof of the origin and integrity of data, preventing someone from later claiming 'I didn't do that' or 'I didn't send that.'</p><p>Non-repudiation is typically achieved through digital signatures, audit logs, and timestamps. When a user digitally signs a document with their PKI certificate, there's cryptographic proof that they signed it — they can't later deny it. Similarly, detailed audit logs with user identification provide evidence of who did what and when.</p>",
        "whyItMatters": "<p>Non-repudiation supports the audit and accountability requirements in CMMC. Having reliable audit trails that can prove who performed specific actions helps you investigate incidents and demonstrate accountability to assessors.</p>",
    },
    {
        "term": "Hashing",
        "definition": "<p>Hashing is a mathematical process that converts data of any size into a fixed-length string of characters (a hash value or digest). Unlike encryption, hashing is a one-way process — you can create a hash from data, but you can't reconstruct the original data from the hash. Hash values are unique to the input data — even a tiny change in the input produces a completely different hash.</p><p>Hashing is used to verify data integrity (confirming files haven't been modified), store passwords securely (storing hashes instead of plain text passwords), and create digital signatures. Common hash algorithms include SHA-256 and SHA-3.</p>",
        "whyItMatters": "<p>Hashing supports integrity verification required by CMMC. Using hashes to verify that critical files, configurations, and software haven't been tampered with is a practical implementation of integrity controls.</p>",
    },
    {
        "term": "Digital Signature",
        "definition": "<p>A digital signature is a cryptographic mechanism that provides authentication (verifying the signer's identity), integrity (proving the content hasn't been modified), and non-repudiation (the signer can't deny signing). It works by creating a hash of the document and encrypting it with the signer's private key — anyone can verify the signature using the signer's public key.</p><p>In the DoD, digital signatures are commonly created using certificates on a CAC card. Digitally signed emails and documents carry legal weight and provide stronger assurance than a typed name or scanned signature.</p>",
        "whyItMatters": "<p>Digital signatures support multiple CMMC requirements including authentication, integrity, and non-repudiation. Using CAC-based digital signatures for important documents and communications is a standard practice in DoD environments.</p>",
    },
    {
        "term": "Certificate Authority (CA)",
        "definition": "<p>A Certificate Authority (CA) is a trusted organization that issues digital certificates — electronic credentials that verify the identity of websites, people, devices, or organizations. When your browser shows a green padlock for a website, a CA has verified that website's identity and issued it a certificate.</p><p>In the DoD, the DoD PKI Certificate Authorities issue certificates for CAC cards, server certificates, and other digital credentials. The trust chain starts with root CAs and extends through intermediate CAs, creating a hierarchy of trust that underpins all PKI-based security.</p>",
        "whyItMatters": "<p>Understanding CAs and PKI is important for managing DoD systems that require certificate-based authentication. Ensuring your systems trust the correct CAs and properly validate certificates is essential for secure communications.</p>",
    },

    # ===== Cloud/Modern Terms (~20) =====
    {
        "term": "FedRAMP",
        "definition": "<p>FedRAMP (Federal Risk and Authorization Management Program) is the government-wide program that provides a standardized approach for security assessment, authorization, and continuous monitoring of cloud products and services. If a cloud service provider wants to sell to the federal government, their offering must be FedRAMP authorized.</p><p>FedRAMP authorization involves rigorous security assessment against a baseline of NIST SP 800-53 controls. Once authorized, the cloud service can be reused by any federal agency without duplicating the assessment — saving time and money across government. FedRAMP authorization levels (Low, Moderate, High) correspond to the sensitivity of data the service can handle.</p>",
        "whyItMatters": "<p>If you use cloud services to process, store, or transmit CUI, those services should be FedRAMP authorized at the Moderate level or higher. Using non-FedRAMP cloud services for CUI is a compliance risk that CMMC assessors will flag.</p>",
    },
    {
        "term": "Cloud Security",
        "definition": "<p>Cloud security encompasses the technologies, policies, controls, and processes used to protect data, applications, and infrastructure in cloud computing environments. As organizations move more workloads to the cloud, understanding the unique security considerations — shared responsibility, data sovereignty, identity management, and configuration — becomes essential.</p><p>Cloud security challenges include ensuring proper configuration (misconfigured cloud storage has caused many breaches), managing identity and access across cloud services, maintaining visibility into cloud-based data, and understanding which security responsibilities belong to you versus the cloud provider (the shared responsibility model).</p>",
        "whyItMatters": "<p>If you're using or considering cloud services for CUI-related work, understanding cloud security is essential. Cloud doesn't eliminate security requirements — it changes where and how they're implemented. CMMC requirements still apply to your cloud environment.</p>",
    },
    {
        "term": "Software as a Service (SaaS)",
        "definition": "<p>Software as a Service (SaaS) is a cloud delivery model where applications are hosted by a provider and accessed over the internet — you use the software through a web browser rather than installing it on your own computers. Examples include Microsoft 365, Google Workspace, Salesforce, and Slack.</p><p>With SaaS, the provider manages the application, infrastructure, and most security — but you remain responsible for your data, your user accounts, and your configuration. For defense contractors, the key question with any SaaS tool is: Does it handle CUI, and if so, is it FedRAMP authorized at the appropriate level?</p>",
        "whyItMatters": "<p>SaaS tools are convenient but can create CUI leakage risks if employees use unauthorized services. Maintaining an inventory of approved SaaS tools and ensuring CUI never reaches unauthorized cloud services is a practical compliance requirement.</p>",
    },
    {
        "term": "Infrastructure as a Service (IaaS)",
        "definition": "<p>Infrastructure as a Service (IaaS) is a cloud delivery model where the provider supplies virtualized computing resources — servers, storage, and networking — over the internet. You rent the infrastructure instead of buying and maintaining physical hardware, but you manage everything running on it: operating systems, applications, data, and security configurations.</p><p>Popular IaaS providers include AWS, Microsoft Azure, and Google Cloud. With IaaS, you have more control but also more security responsibility than with SaaS. You must secure everything from the operating system up, including patching, hardening, access controls, and monitoring.</p>",
        "whyItMatters": "<p>If you use IaaS to host CUI workloads, your security responsibilities are significant. The cloud provider secures the physical infrastructure, but you are responsible for everything else — and CMMC assessors will evaluate your cloud security just as they would an on-premises environment.</p>",
    },
    {
        "term": "Platform as a Service (PaaS)",
        "definition": "<p>Platform as a Service (PaaS) is a cloud delivery model that provides a platform for developing, running, and managing applications without the complexity of managing the underlying infrastructure. PaaS sits between SaaS and IaaS — the provider manages the infrastructure and platform components while you manage the applications and data running on top.</p><p>PaaS offerings include database services, application hosting platforms, and development environments. Security responsibility in PaaS is shared — you handle application security, data protection, and user access, while the provider handles platform and infrastructure security.</p>",
        "whyItMatters": "<p>Understanding the PaaS shared responsibility model is important when your development teams use cloud platforms. Ensuring that applications developed on PaaS platforms meet CMMC requirements for data protection and access control is your responsibility.</p>",
    },
    {
        "term": "Shared Responsibility Model",
        "definition": "<p>The Shared Responsibility Model defines which security responsibilities belong to the cloud service provider and which belong to you, the customer. The exact division depends on the service type: in IaaS, you're responsible for most security above the physical infrastructure; in PaaS, the provider handles more; in SaaS, the provider handles almost everything except data and user access management.</p><p>The key principle is that moving to the cloud doesn't transfer your security obligations to the provider. You're always responsible for your data, your user accounts, your access policies, and your compliance. The provider secures their infrastructure, but your security configuration decisions determine whether your data is actually protected.</p>",
        "whyItMatters": "<p>Misunderstanding the shared responsibility model is one of the most common causes of cloud security breaches. For CMMC compliance, you must clearly understand which controls are your responsibility versus the cloud provider's and implement yours fully.</p>",
    },
    {
        "term": "Container Security",
        "definition": "<p>Container security addresses the protection of containerized applications — software packaged in lightweight, portable units (containers) that run consistently across different computing environments. Container security covers the entire container lifecycle: securing container images, managing container registries, protecting the runtime environment, and monitoring container behavior.</p><p>Containers introduce unique security considerations including image vulnerabilities (using base images with known flaws), configuration risks (running containers with excessive privileges), and orchestration security (protecting the systems that manage containers, like Kubernetes).</p>",
        "whyItMatters": "<p>If your development or operations teams use containers, those environments must meet the same security requirements as traditional infrastructure. Container-specific security scanning and hardening are necessary to maintain CMMC compliance in containerized environments.</p>",
    },
    {
        "term": "DevSecOps",
        "definition": "<p>DevSecOps integrates security practices into every phase of the software development lifecycle — from planning and coding through testing, deployment, and operations. Rather than treating security as a separate phase at the end of development, DevSecOps makes it a shared responsibility throughout the process.</p><p>DevSecOps practices include automated security testing in development pipelines, infrastructure as code security scanning, container image scanning, dependency vulnerability checking, and security-focused code reviews. The goal is to find and fix security issues early, when they're cheapest to address, rather than discovering them during assessment or after deployment.</p>",
        "whyItMatters": "<p>If your company develops software for the DoD, adopting DevSecOps practices aligns with the DoD's own software development strategy and ensures security is built into your products rather than bolted on — reducing the risk of security findings during acceptance and deployment.</p>",
    },
    {
        "term": "Software Bill of Materials (SBOM)",
        "definition": "<p>A Software Bill of Materials (SBOM) is a detailed inventory of all components, libraries, and dependencies that make up a piece of software. Think of it as an ingredients list for software — it tells you exactly what's inside, including third-party and open-source components that your developers may have incorporated.</p><p>SBOMs are increasingly important for software supply chain security. When a vulnerability is discovered in a widely used library (like the Log4j vulnerability in 2021), having an SBOM lets you quickly determine whether your software is affected. Executive Order 14028 mandates SBOM requirements for software sold to the federal government.</p>",
        "whyItMatters": "<p>If you deliver software to the DoD, SBOM requirements are becoming standard. Maintaining accurate SBOMs demonstrates software supply chain transparency and enables rapid response when component vulnerabilities are discovered.</p>",
    },
    {
        "term": "API Security",
        "definition": "<p>API (Application Programming Interface) security focuses on protecting the interfaces that allow different software systems to communicate with each other. APIs are the connectors between applications — they enable data exchange, integration, and automation, but they also represent potential attack surfaces if not properly secured.</p><p>API security concerns include authentication and authorization (ensuring only authorized systems and users can call the API), input validation (preventing injection attacks), rate limiting (preventing abuse), encryption (protecting data in transit), and monitoring (detecting suspicious API usage patterns).</p>",
        "whyItMatters": "<p>As more defense systems use APIs for integration and data exchange, securing those interfaces becomes a compliance requirement. Unsecured APIs can expose CUI to unauthorized access, making API security a practical concern for CMMC compliance.</p>",
    },
    {
        "term": "Configuration Management",
        "definition": "<p>Configuration management is the discipline of establishing and maintaining consistent settings, configurations, and baselines across your systems throughout their lifecycle. It involves documenting your approved configurations, controlling changes through a formal process, and monitoring for unauthorized deviations.</p><p>For cybersecurity, configuration management ensures systems remain in a known, secure state. It covers hardware inventories, software inventories, baseline configurations (like STIGs), change control processes, and configuration monitoring. Without configuration management, systems drift from secure baselines over time, introducing vulnerabilities.</p>",
        "whyItMatters": "<p>Configuration management is an entire CMMC domain with multiple requirements. Maintaining documented baselines, controlling changes, and verifying configurations are fundamental activities that assessors will thoroughly evaluate during your assessment.</p>",
    },
    {
        "term": "Audit Logging",
        "definition": "<p>Audit logging is the process of recording events and activities on your systems so you can track what happened, when it happened, and who did it. Audit logs capture user logins, file access, configuration changes, security events, and other activities that are important for security monitoring, incident investigation, and compliance verification.</p><p>Effective audit logging requires not just turning on logs, but defining what to log, protecting log integrity (preventing tampering), retaining logs for an appropriate period, and actually reviewing them regularly. Logs are useless if nobody looks at them — regular log review is essential for detecting suspicious activity.</p>",
        "whyItMatters": "<p>Audit and accountability is a full CMMC domain. Assessors will verify that you're logging the right events, protecting your logs, retaining them appropriately, and reviewing them regularly. Without audit logs, you have no visibility into what's happening on your systems.</p>",
    },
    {
        "term": "Security Awareness Training",
        "definition": "<p>Security awareness training educates employees about cybersecurity risks, organizational security policies, and their individual responsibilities for protecting information. Effective training covers topics like phishing recognition, password management, physical security, data handling procedures, social engineering awareness, and incident reporting.</p><p>Training should be ongoing — not just annual compliance checkboxes — and should include practical exercises like phishing simulations. The goal is to build a security-conscious culture where employees are part of the defense, not the weakest link.</p>",
        "whyItMatters": "<p>Security awareness training is a CMMC requirement with specific obligations for role-based training and regular refreshers. Well-trained employees are your first line of defense against phishing and social engineering — the most common attack vectors targeting defense contractors.</p>",
    },
    {
        "term": "Physical Security",
        "definition": "<p>Physical security encompasses the measures taken to protect facilities, equipment, and personnel from physical threats — unauthorized physical access, theft, vandalism, natural disasters, and environmental hazards. In cybersecurity, physical security is a critical layer because physical access to systems often bypasses technical controls entirely.</p><p>Physical security measures include access controls (badge readers, locks, guards), surveillance (cameras, monitoring), environmental controls (fire suppression, climate control), visitor management, and secure areas for sensitive equipment and data storage.</p>",
        "whyItMatters": "<p>Physical protection is a CMMC domain with specific requirements for controlling physical access to systems that process CUI. An attacker with physical access to your server room can bypass your best technical controls — physical security cannot be overlooked.</p>",
    },
    {
        "term": "Media Protection",
        "definition": "<p>Media protection covers the security measures for managing removable and portable storage media — USB drives, external hard drives, CDs, tapes, and printed materials — that contain sensitive information. It includes controlling who can use removable media, encrypting data on portable devices, tracking media throughout its lifecycle, and securely destroying media when it's no longer needed.</p><p>For defense contractors, media protection is particularly important because removable media is a common vector for both data exfiltration (copying CUI to a USB drive) and malware introduction (plugging in infected media). Many organizations restrict or prohibit removable media in CUI environments.</p>",
        "whyItMatters": "<p>Media protection is a CMMC domain. Assessors will verify your policies and technical controls for removable media — including how you prevent unauthorized use, how you encrypt portable CUI, and how you destroy media when it's no longer needed.</p>",
    },
    {
        "term": "Personnel Security",
        "definition": "<p>Personnel security encompasses the screening, oversight, and management of people with access to organizational systems and sensitive information. It includes background checks before granting access, ongoing assessment of personnel trustworthiness, and security procedures when employees leave or change roles.</p><p>For defense contractors, personnel security also involves managing security clearances, need-to-know determinations, and ensuring that access is promptly revoked when employees are terminated, transferred, or no longer require it. The insider threat program overlaps significantly with personnel security.</p>",
        "whyItMatters": "<p>Personnel security is a CMMC domain. Assessors will verify that you screen personnel before granting access to CUI, revoke access promptly upon termination or transfer, and have processes for managing the human element of your security program.</p>",
    },
    {
        "term": "Risk Assessment",
        "definition": "<p>A risk assessment is the process of identifying potential threats and vulnerabilities that could affect your organization, analyzing the likelihood and impact of each risk, and determining appropriate measures to manage those risks. It's how you systematically identify what could go wrong and prioritize what to do about it.</p><p>Risk assessments should be performed regularly and whenever significant changes occur — new systems, new threats, organizational changes, or new compliance requirements. The results drive your security investment decisions, helping you allocate limited resources to the risks that matter most.</p>",
        "whyItMatters": "<p>Risk assessment is a CMMC domain. Conducting and documenting risk assessments demonstrates that your security decisions are informed by actual risk analysis rather than guesswork. Assessors expect to see risk-based decision-making in your security program.</p>",
    },
    {
        "term": "System and Information Integrity",
        "definition": "<p>System and information integrity is the security objective of ensuring that systems operate correctly, software is free from unauthorized modifications, and data remains accurate and complete. It covers flaw remediation (patching), malware protection, security monitoring, software integrity verification, and information input validation.</p><p>Maintaining integrity means your systems do what they're supposed to do, your data is accurate, and unauthorized changes are detected quickly. This includes monitoring for unauthorized software installations, verifying the integrity of critical files, and ensuring security tools are functioning correctly.</p>",
        "whyItMatters": "<p>System and information integrity is a CMMC domain with requirements for patching, malware protection, monitoring, and alerting. Assessors will verify that you're actively maintaining the integrity of your systems and detecting when something changes unexpectedly.</p>",
    },
    {
        "term": "Identification and Authentication",
        "definition": "<p>Identification and authentication (I&A) is the security process of claiming an identity (identification — 'I am Jane Smith') and proving it (authentication — 'here is my password and my CAC'). Together, they ensure that only verified, known individuals gain access to systems and data.</p><p>I&A requirements under CMMC include uniquely identifying each user (no shared accounts), implementing multi-factor authentication for remote and privileged access, managing authenticators (passwords, tokens, certificates), and re-authenticating users when sessions expire or when required by policy.</p>",
        "whyItMatters": "<p>Identification and authentication is a CMMC domain with specific requirements that assessors will test. Unique user identification, strong password policies, and MFA for remote access are among the most scrutinized controls during assessment.</p>",
    },
    {
        "term": "System and Communications Protection",
        "definition": "<p>System and communications protection covers the security measures that protect information as it's transmitted across networks and ensure that systems enforce security boundaries. This includes encryption of communications, network segmentation, boundary protection (firewalls), session management, and protection of cryptographic keys.</p><p>For defense contractors, this domain is particularly important because it governs how CUI is protected as it moves across networks — between your systems, to your subcontractors, and in communications with the government.</p>",
        "whyItMatters": "<p>System and communications protection is one of the most technical CMMC domains. Requirements include FIPS-validated encryption for CUI in transit, network segmentation, and boundary protection — these often require significant technical investment to implement correctly.</p>",
    },
    {
        "term": "Maintenance",
        "definition": "<p>In the CMMC context, maintenance refers to the controlled processes for performing maintenance on organizational systems — both routine maintenance (updates, repairs) and maintenance performed by external parties (vendors, service providers). The security concern is that maintenance activities often require elevated access and can introduce vulnerabilities if not properly controlled.</p><p>Maintenance requirements cover controlling who can perform maintenance, supervising maintenance activities by external personnel, ensuring maintenance tools are properly managed, and performing maintenance from approved locations using secure connections.</p>",
        "whyItMatters": "<p>Maintenance is a CMMC domain. Assessors will verify that you control maintenance activities, supervise external maintenance personnel, and ensure that maintenance doesn't introduce security vulnerabilities — particularly when vendor technicians need access to CUI-containing systems.</p>",
    },

    # ===== Additional terms for 250+ total =====
    {
        "term": "DFARS 252.204-7012",
        "definition": "<p>DFARS 252.204-7012 is the Defense Federal Acquisition Regulation Supplement clause titled 'Safeguarding Covered Defense Information and Cyber Incident Reporting.' This contract clause is the legal mechanism that requires defense contractors to implement NIST SP 800-171 security requirements and report cyber incidents to the DoD within 72 hours.</p><p>This clause has been included in DoD contracts since 2017 and is the contractual basis for the cybersecurity requirements that CMMC formalizes. It applies when contractors process, store, or transmit Covered Defense Information (CDI) — which is essentially CUI in the defense context.</p>",
        "whyItMatters": "<p>DFARS 7012 is the contractual requirement that makes CUI protection legally binding for defense contractors. If this clause is in your contract, you're already required to implement NIST SP 800-171 — CMMC adds verification. Non-compliance carries False Claims Act risk.</p>",
    },
    {
        "term": "DFARS 252.204-7021",
        "definition": "<p>DFARS 252.204-7021 is the contract clause titled 'Cybersecurity Maturity Model Certification Requirements.' This clause specifies the CMMC level required for a particular contract and requires contractors to maintain the specified certification level as a condition of contract award and performance.</p><p>This clause works alongside DFARS 7012 — while 7012 establishes the security requirements, 7021 establishes the certification verification requirement. Together, they create the contractual framework for CMMC compliance.</p>",
        "whyItMatters": "<p>When DFARS 7021 appears in a solicitation, it means CMMC certification at the specified level is a go/no-go requirement for contract award. You cannot win the contract without the required certification, making CMMC preparation a business-critical activity.</p>",
    },
    {
        "term": "Covered Defense Information (CDI)",
        "definition": "<p>Covered Defense Information (CDI) is the term used in DFARS 252.204-7012 for the information that requires protection. CDI includes CUI that is provided to the contractor by or on behalf of DoD in connection with the contract, or collected, developed, received, transmitted, used, or stored by the contractor in support of the contract.</p><p>CDI and CUI are closely related — in practice, CDI in the defense contracting context is essentially CUI. The term CDI is specific to the DFARS clause, while CUI is the broader government-wide designation.</p>",
        "whyItMatters": "<p>If your contract references CDI, you're handling information that triggers CMMC requirements. Understanding what constitutes CDI in your specific contract helps you accurately scope your CUI environment and compliance obligations.</p>",
    },
    {
        "term": "False Claims Act",
        "definition": "<p>The False Claims Act is a federal law that imposes liability on companies and individuals who defraud the government. In the cybersecurity context, submitting a false or inflated SPRS score, or claiming compliance with NIST SP 800-171 when you know you're not compliant, can constitute a False Claims Act violation.</p><p>False Claims Act cases can result in penalties of three times the government's damages plus additional fines per false claim. Several defense contractors have already faced enforcement actions for misrepresenting their cybersecurity compliance status.</p>",
        "whyItMatters": "<p>The False Claims Act adds real legal teeth to cybersecurity compliance. Inflating your SPRS score or misrepresenting your security posture isn't just a compliance issue — it's a legal liability that can result in substantial financial penalties and debarment from government contracting.</p>",
    },
    {
        "term": "Managed Security Service Provider (MSSP)",
        "definition": "<p>A Managed Security Service Provider (MSSP) is a third-party company that provides outsourced monitoring and management of security systems and processes. MSSPs offer services like 24/7 security monitoring, vulnerability management, firewall management, intrusion detection, and incident response — capabilities that many small and mid-size contractors can't build internally.</p><p>For defense contractors without large security teams, an MSSP can help meet CMMC monitoring and response requirements cost-effectively. However, you must ensure your MSSP handles CUI appropriately and that their services are included in your assessment scope.</p>",
        "whyItMatters": "<p>Using an MSSP can help you meet CMMC monitoring requirements without building a full internal SOC. However, your MSSP's security practices also matter — they become part of your CUI ecosystem and may need to meet CMMC requirements themselves.</p>",
    },
    {
        "term": "Managed Detection and Response (MDR)",
        "definition": "<p>Managed Detection and Response (MDR) is a service that combines security technology with human expertise to detect, investigate, and respond to threats on your behalf. Unlike traditional MSSP services that primarily alert you to issues, MDR providers actively investigate alerts, hunt for threats, and take response actions — providing a more complete security operations capability.</p><p>MDR services typically include 24/7 monitoring, threat hunting, incident investigation, and guided or automated response actions. For small defense contractors, MDR fills the gap between having basic security tools and having a fully staffed security operations center.</p>",
        "whyItMatters": "<p>MDR services provide the continuous monitoring and incident response capabilities required by CMMC without the cost of building a full internal team. For small contractors, MDR is often the most practical path to meeting monitoring and response requirements.</p>",
    },
    {
        "term": "Role-Based Access Control (RBAC)",
        "definition": "<p>Role-Based Access Control (RBAC) is an access management approach where permissions are assigned to roles (like 'Project Manager' or 'System Administrator') rather than to individual users. Users are then assigned to roles, inheriting the permissions associated with those roles. When someone changes jobs, you change their role assignment rather than individually adjusting dozens of permissions.</p><p>RBAC simplifies access management, reduces errors, and supports the principle of least privilege. It's particularly effective in organizations with well-defined job functions, making it easier to ensure everyone has exactly the access they need — no more, no less.</p>",
        "whyItMatters": "<p>RBAC is a practical way to implement the least privilege and access control requirements in CMMC. Defining clear roles with appropriate permissions and assigning users to roles makes access management auditable and easier to demonstrate to assessors.</p>",
    },
    {
        "term": "Data at Rest",
        "definition": "<p>Data at rest refers to data that is stored and not currently being transmitted or processed — files on hard drives, records in databases, documents in cloud storage, and data on backup media. Protecting data at rest means ensuring stored data is encrypted and access-controlled so that even if a storage device is lost or stolen, the data remains protected.</p><p>For CUI, FIPS-validated encryption of data at rest is a CMMC requirement. This means using full-disk encryption on laptops, encrypting databases containing CUI, and ensuring cloud storage is properly encrypted — all using FIPS 140-2 or 140-3 validated cryptographic modules.</p>",
        "whyItMatters": "<p>CMMC requires encryption of CUI at rest. A lost or stolen laptop without encryption is a CUI breach that must be reported. Implementing FIPS-validated encryption on all storage locations for CUI is a concrete, verifiable requirement.</p>",
    },
    {
        "term": "Data in Transit",
        "definition": "<p>Data in transit refers to data that is being transmitted across a network — between your systems, to cloud services, between offices, or to external parties. Protecting data in transit means encrypting it so that anyone intercepting the network traffic cannot read the content.</p><p>For CUI, FIPS-validated encryption of data in transit is a CMMC requirement. This is typically achieved through TLS 1.2+ for web traffic, VPN tunnels for remote access, and encrypted email for CUI transmitted via email. The encryption must use FIPS-validated cryptographic modules.</p>",
        "whyItMatters": "<p>CUI transmitted without encryption is exposed to interception. CMMC assessors will verify that all pathways where CUI travels — between systems, to the cloud, over VPN, via email — are protected with FIPS-validated encryption.</p>",
    },
    {
        "term": "FIPS 140-2",
        "definition": "<p>FIPS 140-2 (Federal Information Processing Standard Publication 140-2) specifies the security requirements for cryptographic modules — the hardware, software, and firmware that perform encryption and other cryptographic functions. A FIPS 140-2 validated module has been tested by an accredited laboratory and certified by NIST to meet specific security requirements.</p><p>FIPS 140-2 validation is being superseded by FIPS 140-3, but both are currently accepted. The key point is that for protecting CUI, you can't use any encryption — it must be implemented through modules that carry FIPS validation certificates. Using strong encryption that isn't FIPS-validated doesn't satisfy the requirement.</p>",
        "whyItMatters": "<p>FIPS-validated encryption is a specific CMMC requirement for protecting CUI. Verifying that your encryption solutions — disk encryption, VPN, TLS, email encryption — use FIPS-validated modules is a concrete compliance step. Check the NIST CMVP database to verify validation.</p>",
    },
    {
        "term": "Tabletop Exercise",
        "definition": "<p>A tabletop exercise is a simulated cybersecurity scenario that brings together key personnel to walk through their response to a hypothetical security incident. Participants discuss their roles, responsibilities, decisions, and actions in a facilitated group setting — no actual systems are affected. It's a low-cost, low-risk way to test your incident response plan and identify gaps.</p><p>Effective tabletop exercises use realistic scenarios relevant to your organization — like a ransomware attack, CUI data breach, or phishing compromise — and challenge participants to work through detection, containment, communication, and recovery procedures.</p>",
        "whyItMatters": "<p>CMMC requires incident response capability, and tabletop exercises are the most practical way to test and improve your plan without waiting for a real incident. Regular tabletop exercises build team readiness and identify plan weaknesses before they matter.</p>",
    },
    {
        "term": "Change Management",
        "definition": "<p>Change management in cybersecurity is the formal process for requesting, reviewing, approving, implementing, and documenting changes to your information systems and network. It ensures that changes — software updates, configuration modifications, new hardware, architectural changes — are evaluated for security impact before they're made.</p><p>A proper change management process prevents unauthorized or poorly planned changes from introducing vulnerabilities. Each change goes through a request, review (including security impact assessment), approval, implementation, and verification cycle — creating an auditable record of what changed, when, and why.</p>",
        "whyItMatters": "<p>Change management is part of the configuration management requirements in CMMC. Assessors will verify that you have a documented change management process and that changes to CUI systems are properly reviewed, approved, and documented.</p>",
    },
    {
        "term": "Network Segmentation",
        "definition": "<p>Network segmentation divides your network into smaller, isolated segments to control traffic flow and limit the spread of security incidents. By separating your CUI environment from your general corporate network, guest network, and internet-facing services, you reduce the attack surface and contain potential breaches to a smaller area.</p><p>Effective segmentation uses firewalls, VLANs, and access control lists to enforce boundaries between segments. In a well-segmented network, an attacker who compromises a workstation on the general network cannot directly reach systems in the CUI enclave without passing through additional security controls.</p>",
        "whyItMatters": "<p>Network segmentation is both a security best practice and a scoping strategy for CMMC. Properly segmenting your CUI environment reduces your assessment scope and provides a strong technical boundary that assessors can verify.</p>",
    },
    {
        "term": "Vulnerability Scanning",
        "definition": "<p>Vulnerability scanning is the automated process of examining your systems, networks, and applications to identify known security weaknesses. Scanning tools compare your systems' configurations and software versions against databases of known vulnerabilities, producing reports that prioritize findings by severity.</p><p>Regular vulnerability scanning is essential for maintaining visibility into your security posture. Scans should cover all systems in your CUI environment, be performed on a regular schedule (and after significant changes), and results should be tracked and remediated systematically.</p>",
        "whyItMatters": "<p>Regular vulnerability scanning is a specific CMMC requirement. Assessors will want to see your scanning schedule, recent scan results, and evidence that you're actively remediating findings. Unscanned systems are systems with unknown risk.</p>",
    },
    {
        "term": "Two-Factor Authentication (2FA)",
        "definition": "<p>Two-Factor Authentication (2FA) is a specific form of multi-factor authentication that requires exactly two verification factors — typically a password (something you know) plus a one-time code from an authenticator app or hardware token (something you have). While often used interchangeably with MFA, 2FA specifically means two factors rather than two or more.</p><p>2FA significantly reduces the risk of account compromise because an attacker who steals your password still can't log in without the second factor. For defense contractors, 2FA should be implemented on all remote access, privileged accounts, and any system that handles CUI.</p>",
        "whyItMatters": "<p>MFA (of which 2FA is the most common implementation) is a CMMC requirement for remote access and privileged accounts. Implementing 2FA is one of the most effective single actions you can take to protect your accounts from compromise.</p>",
    },
    {
        "term": "Cyber Incident Reporting",
        "definition": "<p>Cyber incident reporting for defense contractors refers to the obligation under DFARS 252.204-7012 to report cyber incidents affecting CUI to the DoD within 72 hours of discovery. Reports are submitted through the DIBNet portal and must include information about the incident, affected systems, and compromised data.</p><p>The 72-hour clock starts when you discover the incident, not when you've completed your investigation. This means you need detection capabilities to discover incidents promptly and pre-established reporting procedures so you can meet the timeline. Contractors must also preserve images of affected systems and relevant monitoring data for at least 90 days.</p>",
        "whyItMatters": "<p>Failure to report cyber incidents within the required timeframe is a contract violation. Having detection capabilities, an incident response plan with clear reporting triggers, and knowledge of the DIBNet reporting process ensures you can meet this obligation.</p>",
    },
    {
        "term": "DIBNet",
        "definition": "<p>DIBNet is the DoD's web portal where defense contractors report cyber incidents as required by DFARS 252.204-7012. The portal is managed by DC3 (DoD Cyber Crime Center) and provides a structured process for submitting incident reports, uploading evidence, and communicating with the DoD about cyber incidents affecting CUI.</p><p>Access to DIBNet requires a DoD-approved medium assurance certificate. Contractors should establish DIBNet access before they need it — waiting until an incident occurs to set up access wastes precious time from your 72-hour reporting window.</p>",
        "whyItMatters": "<p>Having DIBNet access pre-established and key personnel trained on the reporting process is essential for meeting your 72-hour incident reporting obligation. Set up access and practice the reporting workflow before you need it.</p>",
    },
    {
        "term": "Security Clearance",
        "definition": "<p>A security clearance is a formal determination that a person is eligible to access classified national security information at a specific level — Confidential, Secret, or Top Secret. Clearances are granted after a thorough background investigation that evaluates the individual's trustworthiness, loyalty, and reliability.</p><p>Security clearances are granted to individuals, not companies. A company that needs cleared employees must first have a facility clearance (FCL). The clearance process involves completing an SF-86 questionnaire, undergoing investigation by DCSA (Defense Counterintelligence and Security Agency), and adjudication of the results.</p>",
        "whyItMatters": "<p>If your contracts require access to classified information, your employees will need appropriate security clearances and your facility will need an FCL. The clearance process takes months to over a year — plan accordingly when staffing classified programs.</p>",
    },
    {
        "term": "Facility Clearance (FCL)",
        "definition": "<p>A Facility Clearance (FCL) is the organizational equivalent of a personal security clearance — it's the determination that a company's facility meets the security requirements to access, store, and process classified information. An FCL is required before any company employees can receive personal security clearances or access classified materials.</p><p>Obtaining an FCL requires sponsorship (typically through a classified contract), a facility security officer (FSO), compliance with the National Industrial Security Program (NISPOM), and a security inspection by DCSA. The process establishes that your physical facility, personnel, and procedures meet the standards for protecting classified information.</p>",
        "whyItMatters": "<p>If your business growth plans include classified work, obtaining an FCL is a significant undertaking that requires planning, investment, and time. Starting the process early — before you need it for a specific contract — gives you a competitive advantage.</p>",
    },
    {
        "term": "Cybersecurity Framework (CSF)",
        "definition": "<p>The NIST Cybersecurity Framework (CSF) is a voluntary framework that provides organizations with a structured approach to managing cybersecurity risk. It organizes cybersecurity activities into five core functions: Identify, Protect, Detect, Respond, and Recover. Unlike prescriptive standards like 800-171, the CSF is flexible — it helps organizations assess their current state and set goals for improvement.</p><p>The CSF is widely used across industries as a common language for cybersecurity. While it's not a compliance requirement for defense contractors (CMMC and NIST 800-171 are the requirements), the CSF's structure helps organizations understand where their security program stands and where it needs to go.</p>",
        "whyItMatters": "<p>While CMMC is your primary compliance target, the NIST CSF provides a useful lens for evaluating your overall security program maturity. Many organizations use the CSF alongside CMMC to build a comprehensive, risk-based security program.</p>",
    },
    {
        "term": "Incident Response Plan (IRP)",
        "definition": "<p>An Incident Response Plan (IRP) is a documented set of procedures that your organization follows when a cybersecurity incident occurs. It defines what constitutes an incident, who is responsible for each aspect of the response, communication procedures (internal and external), technical response steps, and recovery processes.</p><p>An effective IRP addresses the full incident lifecycle: preparation, detection and analysis, containment, eradication, recovery, and post-incident review. For defense contractors, the IRP must include procedures for the 72-hour DoD reporting requirement and evidence preservation obligations under DFARS 7012.</p>",
        "whyItMatters": "<p>A documented and tested IRP is a specific CMMC requirement. The plan must be more than a document on a shelf — it should be tested through tabletop exercises and known by all personnel with incident response responsibilities.</p>",
    },
    {
        "term": "Data Classification",
        "definition": "<p>Data classification is the process of categorizing your organization's data based on its sensitivity level and the protection it requires. Classification schemes typically include levels like Public, Internal, Confidential, and Restricted (or government equivalents like Unclassified, CUI, Confidential, Secret, Top Secret).</p><p>Proper data classification is the foundation of effective data protection — you can't protect data appropriately if you don't know how sensitive it is. Classification drives security controls: CUI requires specific protections under CMMC, classified data requires even stricter controls, and public data needs minimal protection.</p>",
        "whyItMatters": "<p>You can't meet CMMC requirements if you don't know where your CUI is. Data classification — identifying what data you have, how sensitive it is, and where it lives — is a prerequisite for scoping your CUI environment and applying appropriate protections.</p>",
    },
    {
        "term": "Cyber Hygiene",
        "definition": "<p>Cyber hygiene refers to the fundamental cybersecurity practices that every organization should maintain as a baseline — the basic 'housekeeping' that keeps your systems healthy and secure. Like personal hygiene prevents illness, cyber hygiene prevents the most common and preventable security incidents.</p><p>Core cyber hygiene practices include keeping software updated (patching), using strong and unique passwords with MFA, maintaining current antivirus protection, backing up data regularly, controlling user access, and training employees to recognize phishing. CMMC Level 1 essentially codifies these basic practices.</p>",
        "whyItMatters": "<p>Most successful cyber attacks exploit basic hygiene failures — unpatched systems, weak passwords, lack of MFA, untrained users. Getting the fundamentals right through consistent cyber hygiene prevents the majority of attacks, regardless of their sophistication.</p>",
    },
    {
        "term": "Privileged User",
        "definition": "<p>A privileged user is anyone with elevated system access rights beyond those of a standard user — system administrators, database administrators, network engineers, and anyone with admin-level credentials. Privileged users can install software, change configurations, access all files, and perform other actions that standard users cannot.</p><p>Because privileged accounts have such broad access, they're prime targets for attackers and require extra security measures: dedicated admin accounts (separate from daily-use accounts), multi-factor authentication, session monitoring, and just-in-time access where possible.</p>",
        "whyItMatters": "<p>CMMC includes specific requirements for managing privileged accounts. Assessors will verify that privileged users have dedicated admin accounts, use MFA, and that privileged activities are logged and monitored.</p>",
    },
    {
        "term": "Separation of Duties",
        "definition": "<p>Separation of duties is the security principle that no single individual should have enough access or authority to commit fraud or cause significant harm alone. Critical tasks are divided among multiple people so that no one person controls an entire process — creating checks and balances that prevent abuse and catch errors.</p><p>In cybersecurity, separation of duties means that the person who writes code shouldn't be the same person who deploys it to production, the person who requests access shouldn't be the same person who approves it, and the person who manages security logs shouldn't be the same person whose activities are being logged.</p>",
        "whyItMatters": "<p>Separation of duties is a CMMC access control requirement. While challenging for small organizations with limited staff, demonstrating some level of duty separation — particularly for critical security and administrative functions — is important for assessment.</p>",
    },
    {
        "term": "Sanitization",
        "definition": "<p>Sanitization (or media sanitization) is the process of making data on storage media unrecoverable before the media is reused, repurposed, or disposed of. Simple deletion doesn't actually remove data — it just marks the space as available. Sanitization ensures that sensitive data, including CUI, cannot be recovered from decommissioned equipment.</p><p>Sanitization methods include clearing (overwriting data), purging (degaussing or cryptographic erasure), and destroying (shredding, disintegrating, incinerating). The appropriate method depends on the sensitivity of the data and whether the media will be reused or destroyed.</p>",
        "whyItMatters": "<p>Media sanitization is a CMMC requirement. Improperly disposed equipment containing CUI is a data breach. Having a documented sanitization process and maintaining records of media disposition protects you from compliance findings and data exposure.</p>",
    },
    {
        "term": "Boundary Protection",
        "definition": "<p>Boundary protection refers to the security controls at the edges of your network — where your internal network meets the internet, connects to partner networks, or interfaces with other security zones. Boundary protection devices include firewalls, routers with access control lists, web application firewalls, email gateways, and proxy servers.</p><p>Effective boundary protection involves monitoring and controlling traffic at each network boundary, denying traffic by default and only allowing what's explicitly authorized, inspecting traffic for malicious content, and logging all boundary crossing attempts for security analysis.</p>",
        "whyItMatters": "<p>Boundary protection is a core requirement in the System and Communications Protection domain of CMMC. Assessors will evaluate your network boundaries, the controls protecting them, and your ability to monitor and control traffic flow into and out of your CUI environment.</p>",
    },
    {
        "term": "Account Management",
        "definition": "<p>Account management is the lifecycle management of user accounts on your systems — from creation through modification to eventual removal. It encompasses establishing accounts for new users, modifying access when roles change, disabling accounts when no longer needed, and removing accounts for terminated employees.</p><p>Effective account management requires clear processes for each stage, timely execution (especially for terminations), regular access reviews to identify stale or excessive permissions, and documentation that demonstrates compliance with your policies.</p>",
        "whyItMatters": "<p>Account management is a fundamental CMMC requirement. Stale accounts, orphaned accounts from former employees, and accounts with excessive permissions are common findings during assessments. Regular access reviews and prompt termination processing prevent these issues.</p>",
    },
    {
        "term": "Session Management",
        "definition": "<p>Session management controls how user sessions are created, maintained, and terminated on your systems. Security requirements include automatically locking or terminating sessions after a period of inactivity, requiring re-authentication when sessions expire, limiting the number of concurrent sessions per user, and protecting session identifiers from theft.</p><p>For CUI systems, session management ensures that unattended workstations don't remain logged in and accessible, that session tokens can't be hijacked by attackers, and that users must periodically re-verify their identity during long sessions.</p>",
        "whyItMatters": "<p>Session management requirements under CMMC include screen lock after inactivity and session termination. These controls prevent unauthorized access to CUI through unattended workstations — a common and easily preventable security gap.</p>",
    },
    {
        "term": "Wireless Security",
        "definition": "<p>Wireless security encompasses the measures taken to protect wireless networks and the data transmitted over them from unauthorized access, eavesdropping, and attack. It includes using strong encryption (WPA3 or WPA2-Enterprise), implementing authentication controls, monitoring for rogue access points, and restricting wireless access in areas where CUI is processed.</p><p>Wireless networks are inherently more exposed than wired networks because signals travel through the air and can be intercepted from outside your facility. Extra precautions are needed, particularly in environments handling sensitive data.</p>",
        "whyItMatters": "<p>CMMC includes specific requirements for wireless access protection. Assessors will verify your wireless encryption, authentication methods, and any restrictions on wireless access to CUI systems. Weak wireless security is a common and easily exploitable vulnerability.</p>",
    },
    {
        "term": "Mobile Device Management (MDM)",
        "definition": "<p>Mobile Device Management (MDM) is a technology and set of policies for managing, securing, and monitoring mobile devices (smartphones, tablets, laptops) used to access organizational resources. MDM solutions enforce security policies on mobile devices — requiring encryption, strong passcodes, remote wipe capability, and application controls.</p><p>For defense contractors, MDM is important when employees use mobile devices that may access email or systems containing CUI. Without MDM, a lost or stolen phone with access to your corporate email could expose CUI with no way to remotely remove the data.</p>",
        "whyItMatters": "<p>If mobile devices access your CUI environment, CMMC requires appropriate security controls on those devices. MDM provides the technical enforcement needed to ensure mobile devices meet your security requirements and can be remotely wiped if lost or stolen.</p>",
    },
    {
        "term": "Cyber Insurance",
        "definition": "<p>Cyber insurance is a type of insurance policy that provides financial protection against losses resulting from cyber attacks and data breaches. Coverage can include incident response costs, forensic investigation expenses, legal fees, notification costs, regulatory fines, business interruption losses, and ransom payments (though this is increasingly debated).</p><p>Cyber insurance doesn't replace good security — insurers increasingly require evidence of security controls (like MFA, endpoint protection, and backups) before issuing policies. Think of it as a financial safety net, not a security strategy.</p>",
        "whyItMatters": "<p>While not a CMMC requirement, cyber insurance provides financial protection for the costs associated with a breach — which can be devastating for small contractors. Importantly, meeting CMMC requirements often helps you qualify for better insurance terms and lower premiums.</p>",
    },
    {
        "term": "Log Retention",
        "definition": "<p>Log retention refers to how long you keep audit logs and security event records before they're archived or deleted. Retention policies balance storage costs against the need to have historical data available for incident investigation, compliance verification, and forensic analysis.</p><p>For defense contractors, DFARS 7012 requires preserving security monitoring data for at least 90 days following a cyber incident. Many frameworks and best practices recommend retaining security logs for at least one year, with some organizations maintaining them for longer based on their risk assessment and regulatory requirements.</p>",
        "whyItMatters": "<p>CMMC requires audit log retention sufficient to support incident investigation and compliance verification. If a breach is discovered months after it occurred, you need the historical logs to understand what happened. Define and document your log retention policy.</p>",
    },
    {
        "term": "Least Functionality",
        "definition": "<p>Least functionality is the security principle of configuring systems to provide only the capabilities required for their intended purpose — disabling or removing all unnecessary functions, ports, protocols, services, and software. A system should do what it needs to do and nothing more.</p><p>In practice, least functionality means disabling unused services, removing unnecessary software, closing unneeded network ports, restricting available system functions based on user role, and preventing the installation of unauthorized programs. This reduces your attack surface by eliminating potential entry points that aren't needed for business operations.</p>",
        "whyItMatters": "<p>Least functionality is a specific CMMC requirement under configuration management. Every unnecessary service or application on a system is a potential vulnerability. Assessors will verify that your systems are configured to minimum functionality needed for their mission.</p>",
    },
    {
        "term": "Spillage",
        "definition": "<p>In cybersecurity, spillage (also called a data spill) occurs when classified or sensitive information is placed on a system that is not authorized to handle that level of information. For example, if CUI ends up on a system outside your CUI enclave, or if classified information ends up on an unclassified system — that's a spillage incident.</p><p>Spillage requires immediate containment and remediation — the affected systems may need to be isolated, cleaned, or even destroyed depending on the sensitivity of the spilled data. Spillage incidents must be reported through appropriate channels and are taken very seriously in the DoD.</p>",
        "whyItMatters": "<p>CUI spillage outside your controlled environment is a security incident that may require DoD notification. Understanding what constitutes spillage and having procedures to detect, contain, and report it demonstrates mature data handling practices to assessors.</p>",
    },
    {
        "term": "Whitelisting",
        "definition": "<p>Whitelisting (also called allowlisting) is a security approach where only specifically approved items — applications, email addresses, IP addresses, or websites — are permitted, and everything else is blocked by default. This is the opposite of blacklisting, where known bad items are blocked but everything else is allowed.</p><p>Application whitelisting is particularly effective against malware because only pre-approved software can run on a system. Even if an attacker manages to place malware on the system, it can't execute because it's not on the approved list. This provides strong protection against zero-day threats that antivirus might not detect.</p>",
        "whyItMatters": "<p>Application whitelisting supports CMMC requirements for restricting software installation and controlling what can execute on CUI systems. While more restrictive than traditional antivirus, whitelisting provides stronger protection against advanced malware threats.</p>",
    },
    {
        "term": "Blacklisting",
        "definition": "<p>Blacklisting (also called denylisting) is a security approach where known malicious items — applications, email addresses, IP addresses, or websites — are specifically blocked, while everything else is allowed by default. Traditional antivirus software uses blacklisting: it maintains a database of known malware signatures and blocks those, but allows everything else to run.</p><p>Blacklisting is easier to implement and less disruptive than whitelisting, but it's inherently reactive — it can only block threats it knows about. New malware, zero-day exploits, and novel attack tools won't be blocked until they're identified and added to the blocklist.</p>",
        "whyItMatters": "<p>While blacklisting alone may not satisfy all CMMC requirements for software restriction, it remains a useful defense layer. Combining blacklisting (block known bad) with whitelisting (allow only known good) provides the strongest protection for CUI systems.</p>",
    },
    {
        "term": "Cyber Threat Hunting",
        "definition": "<p>Cyber threat hunting is the proactive practice of searching through your networks and systems for hidden threats that have evaded your automated security tools. Unlike reactive monitoring (waiting for alerts), threat hunting involves skilled analysts forming hypotheses about potential attacker presence and actively investigating — looking for subtle indicators of compromise that automated tools missed.</p><p>Threat hunting assumes that attackers may already be in your environment and works to find them before they achieve their objectives. It uses threat intelligence, behavioral analytics, and expert analysis to identify sophisticated threats that slip past signature-based defenses.</p>",
        "whyItMatters": "<p>While not explicitly required by CMMC Level 2, threat hunting represents a mature security capability. APTs targeting defense contractors often evade automated detection — proactive hunting increases your chances of discovering a compromise before critical CUI is exfiltrated.</p>",
    },
    {
        "term": "Security Assessment",
        "definition": "<p>A security assessment is a broad evaluation of an organization's security posture, policies, and controls to identify strengths, weaknesses, and areas for improvement. It can take many forms — vulnerability assessments, penetration tests, compliance audits, control assessments, or comprehensive program reviews.</p><p>In the CMMC context, security assessment refers specifically to the evaluation of your security controls against the requirements in NIST SP 800-171. CMMC assessments are conducted either as self-assessments or by authorized C3PAOs, and the results determine your certification status.</p>",
        "whyItMatters": "<p>Security assessment is both a CMMC domain and the process through which you achieve certification. Regular self-assessments between formal evaluations help you maintain continuous compliance and catch degradation before it becomes a significant gap.</p>",
    },
    {
        "term": "Flaw Remediation",
        "definition": "<p>Flaw remediation is the process of identifying, reporting, and correcting security flaws (bugs, vulnerabilities, weaknesses) in your software and systems. It encompasses the entire lifecycle from vulnerability discovery through patch deployment and verification that the fix worked.</p><p>Effective flaw remediation requires a defined process: vulnerability identification (through scanning, vendor advisories, or threat intelligence), prioritization (based on severity and exploitability), testing (ensuring patches don't break critical functions), deployment (timely application of fixes), and verification (confirming the vulnerability is resolved).</p>",
        "whyItMatters": "<p>Flaw remediation is a specific CMMC requirement under system and information integrity. Assessors will verify that you have a process for identifying, prioritizing, and remediating security flaws — and that you follow it consistently.</p>",
    },
    {
        "term": "Security Information Sharing",
        "definition": "<p>Security information sharing is the practice of exchanging cybersecurity threat intelligence, vulnerability data, and incident information between organizations to improve collective defense. Information sharing organizations like ISACs (Information Sharing and Analysis Centers) and ISAOs (Information Sharing and Analysis Organizations) facilitate this exchange.</p><p>For defense contractors, the DIB-ISAC (Defense Industrial Base Information Sharing and Analysis Center) provides threat intelligence specific to the defense sector. Participating in information sharing gives you early warning about threats targeting your industry.</p>",
        "whyItMatters": "<p>Participating in cybersecurity information sharing helps you stay ahead of threats targeting the defense industrial base. The intelligence you receive can improve your detection capabilities and inform your security priorities.</p>",
    },
    {
        "term": "Cryptography",
        "definition": "<p>Cryptography is the science and practice of securing information through mathematical techniques — encoding data so that only authorized parties can read it. Modern cryptography includes encryption (protecting confidentiality), hashing (verifying integrity), digital signatures (providing authentication and non-repudiation), and key management (securely generating, distributing, and storing cryptographic keys).</p><p>For defense contractors, the critical requirement is using FIPS-validated cryptographic modules. This means the specific software or hardware performing the cryptography has been tested and certified by an accredited laboratory to meet federal security standards.</p>",
        "whyItMatters": "<p>Cryptography is the technical foundation of CUI protection under CMMC. Ensuring your cryptographic implementations are FIPS-validated is a specific, verifiable requirement — not just 'use encryption,' but 'use validated encryption.'</p>",
    },
    {
        "term": "Key Management",
        "definition": "<p>Key management encompasses the policies, procedures, and technical mechanisms for generating, distributing, storing, rotating, and destroying cryptographic keys. Encryption is only as strong as its key management — even the best encryption is useless if the keys are poorly protected, shared insecurely, or never rotated.</p><p>Proper key management includes generating keys using approved methods, protecting keys with access controls and encryption, distributing keys securely, rotating keys on a defined schedule, and destroying keys properly when they're no longer needed.</p>",
        "whyItMatters": "<p>CMMC requires proper cryptographic key management as part of system and communications protection. Assessors may ask how your encryption keys are generated, stored, and managed — having documented key management procedures demonstrates cryptographic maturity.</p>",
    },
    {
        "term": "Remote Access",
        "definition": "<p>Remote access refers to the ability of users to connect to organizational systems and resources from locations outside the physical office — through VPNs, remote desktop solutions, cloud services, or other connectivity methods. Remote access is essential for modern work but introduces significant security risks if not properly controlled.</p><p>Securing remote access requires encrypted connections (VPN with FIPS-validated encryption), multi-factor authentication, session monitoring, and access limitations based on the sensitivity of the data being accessed. Remote access to CUI systems requires particularly stringent controls.</p>",
        "whyItMatters": "<p>Remote access is one of the most scrutinized areas in CMMC assessments. MFA, encrypted connections, and session controls for remote access are specific requirements. With remote work now standard, ensuring your remote access infrastructure meets these requirements is critical.</p>",
    },
    {
        "term": "System Hardening",
        "definition": "<p>System hardening is the process of reducing a system's attack surface by removing unnecessary software, disabling unused services, applying security patches, configuring security settings, and implementing the principle of least functionality. A hardened system has been stripped down to only what's needed for its specific purpose.</p><p>Hardening standards like DISA STIGs and CIS Benchmarks provide detailed configuration guides for specific technologies. Following these standards ensures consistent, documented security configurations across your environment.</p>",
        "whyItMatters": "<p>System hardening supports multiple CMMC requirements across configuration management, system protection, and access control. Assessors expect to see evidence that your systems are hardened according to defined standards, not running in default configurations.</p>",
    },
    {
        "term": "CIS Benchmarks",
        "definition": "<p>CIS (Center for Internet Security) Benchmarks are community-developed, consensus-based security configuration guidelines for operating systems, applications, network devices, and cloud platforms. They provide specific, step-by-step hardening recommendations that complement DISA STIGs and are widely used across both government and commercial environments.</p><p>CIS Benchmarks come in two profile levels: Level 1 (basic hardening with minimal operational impact) and Level 2 (stronger security that may restrict some functionality). They're available free for personal use and cover virtually every major technology platform.</p>",
        "whyItMatters": "<p>CIS Benchmarks provide a practical starting point for system hardening when STIGs aren't available for specific technologies. Using established benchmarks demonstrates that your configurations are based on industry consensus, not arbitrary decisions.</p>",
    },
    {
        "term": "Worm",
        "definition": "<p>A worm is a type of malware that spreads automatically across networks without requiring user interaction. Unlike viruses (which attach to files and need someone to open them), worms exploit network vulnerabilities to propagate from system to system on their own, often spreading rapidly across entire networks in minutes or hours.</p><p>Historical worms like WannaCry and NotPetya caused billions of dollars in damage by spreading through networks at machine speed, encrypting or destroying data on every reachable system. Worms exploit unpatched vulnerabilities, making timely patch management the primary defense.</p>",
        "whyItMatters": "<p>Worms highlight why timely patching and network segmentation are critical CMMC requirements. A single unpatched system can allow a worm to spread throughout your network — segmentation limits the blast radius while patching eliminates the vulnerability.</p>",
    },
    {
        "term": "Virus",
        "definition": "<p>A computer virus is a type of malware that attaches itself to legitimate programs or files and spreads when those infected files are executed or shared. Like biological viruses, computer viruses need a host (a file or program) and require user action (opening the infected file) to activate and spread.</p><p>Viruses can cause various types of damage — corrupting data, stealing information, consuming system resources, or providing backdoor access to attackers. While worms and ransomware dominate headlines today, viruses remain a persistent threat, particularly through infected email attachments and downloaded files.</p>",
        "whyItMatters": "<p>Antivirus protection is a fundamental CMMC requirement. Maintaining updated antivirus/anti-malware solutions across all endpoints — and ensuring they can't be disabled by users — is a baseline security control assessors will verify.</p>",
    },
    {
        "term": "Adware",
        "definition": "<p>Adware is software that displays unwanted advertisements on your computer, often installed without full user awareness alongside other software. While not always malicious, adware can track browsing habits, slow system performance, and serve as a vector for more serious malware by displaying malicious ads.</p><p>Adware on business systems is a security concern because it indicates a lack of software control — unauthorized software was installed on the system. It may also collect and transmit data about system usage, potentially exposing sensitive information about your work activities.</p>",
        "whyItMatters": "<p>Adware on CUI systems indicates gaps in software installation controls — a CMMC requirement. Preventing unauthorized software installation through application whitelisting or strict software policies eliminates adware and the broader risks it represents.</p>",
    },
    {
        "term": "Keylogger",
        "definition": "<p>A keylogger is a type of malware or hardware device that records every keystroke typed on a computer, capturing passwords, email content, documents, and anything else the user types. Software keyloggers run invisibly in the background, while hardware keyloggers are physical devices connected between the keyboard and the computer.</p><p>Keyloggers are a severe threat to CUI because they capture data as it's being typed — before encryption or access controls can protect it. They can capture credentials, allowing attackers to access systems as legitimate users, and they can record sensitive content being typed into documents and emails.</p>",
        "whyItMatters": "<p>Keyloggers can defeat many security controls by capturing data at the source. Endpoint protection with behavioral detection, regular system inspections, and physical security measures are essential for detecting both software and hardware keyloggers.</p>",
    },
    {
        "term": "Backdoor",
        "definition": "<p>A backdoor is a hidden method of bypassing normal authentication or security controls to gain unauthorized access to a system. Backdoors can be intentionally installed by attackers who have already compromised a system (to maintain persistent access) or they can be hidden in software by malicious developers.</p><p>Once a backdoor is installed, attackers can return to the compromised system at any time, often without triggering security alerts. Backdoors are commonly installed by APT actors to maintain long-term access to target networks — they compromise the system, install a backdoor, and then use it for ongoing data theft.</p>",
        "whyItMatters": "<p>Backdoors represent persistent unauthorized access — exactly the kind of threat CMMC's monitoring and integrity requirements are designed to detect. Continuous monitoring, file integrity checking, and network analysis help identify backdoor communications.</p>",
    },
    {
        "term": "Man-in-the-Middle Attack (MitM)",
        "definition": "<p>A Man-in-the-Middle (MitM) attack occurs when an attacker secretly positions themselves between two communicating parties, intercepting and potentially modifying the data flowing between them. The attacker can eavesdrop on sensitive communications, steal credentials, or alter data in transit — all while both parties believe they're communicating directly with each other.</p><p>MitM attacks exploit unencrypted or poorly encrypted communications. Using TLS/SSL for web traffic, VPNs for remote access, and certificate validation helps prevent MitM attacks by ensuring communications are encrypted and the identity of each endpoint is verified.</p>",
        "whyItMatters": "<p>Encryption of CUI in transit — a CMMC requirement — directly prevents MitM attacks from capturing sensitive data. Ensuring all communications carrying CUI are encrypted with FIPS-validated cryptography closes this attack vector.</p>",
    },
    {
        "term": "Credential Stuffing",
        "definition": "<p>Credential stuffing is an automated attack where stolen username/password combinations from one data breach are tried against other websites and services. Because many people reuse passwords across multiple accounts, attackers can often gain access to new accounts using credentials stolen from completely unrelated breaches.</p><p>Credential stuffing attacks use automated tools to test thousands or millions of stolen credentials against target login pages. They exploit the human habit of password reuse — if your employee uses the same password for their personal email and their work VPN, a breach of the email provider gives the attacker access to your corporate network.</p>",
        "whyItMatters": "<p>MFA requirement under CMMC directly mitigates credential stuffing — even if an attacker has valid stolen credentials, they can't access your systems without the second authentication factor. Password policies that prohibit known-breached passwords also help.</p>",
    },
    {
        "term": "Brute Force Attack",
        "definition": "<p>A brute force attack is a trial-and-error method of guessing passwords or encryption keys by systematically trying every possible combination until the correct one is found. Simple brute force tries every combination sequentially, while more sophisticated variants use dictionaries of common passwords, known patterns, or previously leaked passwords to speed up the process.</p><p>Defenses against brute force include account lockout policies (locking accounts after a number of failed attempts), multi-factor authentication, strong password requirements, and rate limiting on login attempts.</p>",
        "whyItMatters": "<p>CMMC requires mechanisms to limit repeated failed login attempts — directly defending against brute force attacks. Implementing account lockout or throttling policies, combined with MFA, makes brute force attacks impractical against your systems.</p>",
    },
    {
        "term": "Denial of Service (DoS)",
        "definition": "<p>A Denial of Service (DoS) attack attempts to make a system, network, or service unavailable to its intended users by overwhelming it with traffic, exploiting vulnerabilities to crash it, or consuming its resources. Unlike DDoS (distributed), a basic DoS attack comes from a single source.</p><p>DoS attacks target the availability component of the CIA triad. While they don't typically steal data, they can disrupt critical business operations, prevent legitimate users from accessing systems, and serve as a distraction while attackers pursue other objectives elsewhere on your network.</p>",
        "whyItMatters": "<p>System availability is part of your security posture under CMMC. While CUI confidentiality is the primary concern, ensuring your systems remain available to support DoD missions is also important. DDoS mitigation and redundancy planning help address this risk.</p>",
    },
    {
        "term": "Spear Phishing",
        "definition": "<p>Spear phishing is a targeted form of phishing where attackers craft personalized messages aimed at specific individuals or organizations. Unlike mass phishing campaigns, spear phishing emails are researched and customized — they may reference the target's name, company, role, recent activities, or business relationships to appear legitimate.</p><p>Spear phishing is the preferred attack method of APT groups targeting the defense industrial base. Attackers research their targets using LinkedIn, company websites, and other public information to create convincing emails that are much harder to detect than generic phishing.</p>",
        "whyItMatters": "<p>Defense contractors are frequent targets of spear phishing by nation-state actors seeking CUI. Security awareness training that includes realistic spear phishing simulations helps employees recognize these sophisticated attacks.</p>",
    },
    {
        "term": "Business Email Compromise (BEC)",
        "definition": "<p>Business Email Compromise (BEC) is a sophisticated social engineering attack where attackers impersonate executives, vendors, or trusted partners via email to trick employees into transferring money, sharing sensitive data, or taking other harmful actions. BEC attacks often involve compromised email accounts or convincingly spoofed email addresses.</p><p>BEC costs organizations billions of dollars annually and is one of the most financially damaging cybercrime types. Common scenarios include CEO fraud (impersonating an executive to request wire transfers), vendor impersonation (redirecting payments to attacker-controlled accounts), and data theft (requesting employee tax or payroll information).</p>",
        "whyItMatters": "<p>BEC attacks can lead to financial losses and potential CUI exposure. Email authentication controls (DMARC, DKIM, SPF), multi-person authorization for financial transactions, and security awareness training are practical defenses that support CMMC objectives.</p>",
    },
    {
        "term": "Watering Hole Attack",
        "definition": "<p>A watering hole attack targets a specific group of users by compromising a website they frequently visit. Instead of attacking the targets directly, the attacker identifies websites commonly used by the target group, compromises those sites, and plants malware that infects visitors. The name comes from predators waiting at watering holes where prey gathers.</p><p>Watering hole attacks are particularly effective against well-defended organizations because the malware comes from a trusted source — a website the user visits regularly for work. Defense industry forums, professional association websites, and sector-specific resources can all be targeted.</p>",
        "whyItMatters": "<p>Watering hole attacks bypass email-based defenses by delivering malware through web browsing. Web filtering, endpoint protection, and network monitoring — all part of CMMC requirements — help detect and prevent compromise from these sophisticated attacks.</p>",
    },
    {
        "term": "Vishing",
        "definition": "<p>Vishing (voice phishing) is a social engineering attack conducted over the phone where callers impersonate trusted entities — IT support, bank representatives, government officials, or company executives — to trick victims into revealing sensitive information, transferring funds, or granting system access.</p><p>Vishing attacks have become increasingly sophisticated, sometimes using spoofed caller IDs to appear to come from legitimate numbers. Attackers may have done extensive research on the target, making the call seem genuine by referencing real names, projects, or organizational details.</p>",
        "whyItMatters": "<p>Security awareness training under CMMC should cover phone-based social engineering. Employees need to verify caller identity through callback procedures before sharing sensitive information or granting access requests received by phone.</p>",
    },
    {
        "term": "Smishing",
        "definition": "<p>Smishing (SMS phishing) is a social engineering attack delivered through text messages. Attackers send text messages containing malicious links or urgent requests designed to trick recipients into revealing credentials, installing malware, or taking other harmful actions.</p><p>Smishing exploits the trust people place in text messages and the tendency to act quickly on mobile devices. Messages often create urgency — fake delivery notifications, account warnings, or IT alerts — to pressure recipients into clicking links before thinking critically about the message.</p>",
        "whyItMatters": "<p>As mobile devices increasingly access corporate resources, smishing becomes a relevant threat. Security awareness training should cover SMS-based attacks alongside email phishing to protect the full range of communication channels employees use.</p>",
    },
    {
        "term": "Pretexting",
        "definition": "<p>Pretexting is a social engineering technique where the attacker creates a fabricated scenario (the pretext) to engage a target and manipulate them into providing information or access. The attacker assumes a false identity or role — IT support, auditor, law enforcement, new employee — and builds a plausible story to justify their request.</p><p>Pretexting often precedes other attacks: an attacker might call claiming to be from IT support, establish trust through the pretext, and then ask the target to reveal their password or install software. The more detailed and believable the pretext, the more likely the target is to comply.</p>",
        "whyItMatters": "<p>Pretexting is one of the most effective social engineering techniques because it exploits helpfulness and trust. Training employees to verify identities through independent channels before complying with unusual requests helps defend against these attacks.</p>",
    },
    {
        "term": "Tailgating",
        "definition": "<p>Tailgating (or piggybacking) is a physical security breach where an unauthorized person follows an authorized person through a secured door or entrance. The unauthorized person may simply walk closely behind someone who badges in, hold the door and claim they forgot their badge, or carry items that make it seem rude not to hold the door open.</p><p>Tailgating bypasses access control systems that rely on badges or key cards. It exploits social norms — people generally feel uncomfortable refusing to hold a door for someone, especially in a professional setting.</p>",
        "whyItMatters": "<p>Physical access controls are a CMMC requirement. Tailgating defeats electronic access controls, so additional measures — security awareness, mantrap doors, or security guards — may be needed to prevent unauthorized physical access to CUI areas.</p>",
    },
    {
        "term": "Baiting",
        "definition": "<p>Baiting is a social engineering attack where the attacker leaves malware-infected media — USB drives, CDs, or external hard drives — in locations where targets are likely to find them. The bait might be labeled enticingly ('Employee Bonuses 2026,' 'Confidential') to encourage the finder to plug it into their computer.</p><p>When the bait device is connected to a computer, it can automatically install malware, capture credentials, or establish a backdoor. Famous examples include the Stuxnet attack, which used infected USB drives to penetrate air-gapped systems.</p>",
        "whyItMatters": "<p>CMMC includes requirements for controlling removable media. Policies restricting or disabling USB ports on CUI systems, combined with user training about the dangers of found media, prevent baiting attacks from compromising your environment.</p>",
    },
    {
        "term": "Threat Modeling",
        "definition": "<p>Threat modeling is a structured approach to identifying and prioritizing potential threats to your systems by analyzing your architecture, identifying assets worth protecting, enumerating potential attack vectors, and determining which threats pose the greatest risk. Common methodologies include STRIDE, PASTA, and attack trees.</p><p>Threat modeling should be performed during system design and updated when the system or threat landscape changes. It provides the analytical foundation for security architecture decisions — helping you focus your defenses on the threats most relevant to your specific environment and data.</p>",
        "whyItMatters": "<p>While not a specific CMMC checklist item, threat modeling supports the risk assessment requirements and helps you make informed decisions about where to invest your security resources. Understanding your threats helps you implement controls that actually address your specific risks.</p>",
    },
    {
        "term": "Security Architecture",
        "definition": "<p>Security architecture is the design framework that describes how security controls are positioned within your IT environment to protect systems and data. It encompasses network topology, security zones, data flow patterns, authentication systems, encryption deployment, and the integration of security tools into a cohesive defensive system.</p><p>A well-designed security architecture implements defense in depth, segments sensitive data environments, places controls at appropriate boundaries, and ensures that security tools work together rather than as isolated components. Your security architecture should be documented and reviewed as part of your System Security Plan.</p>",
        "whyItMatters": "<p>Your security architecture is the foundation that assessors evaluate during CMMC assessments. A thoughtfully designed architecture that demonstrates defense in depth, proper segmentation, and aligned security controls gives assessors confidence in your overall security posture.</p>",
    },
    {
        "term": "Data Flow Diagram",
        "definition": "<p>A data flow diagram (DFD) in the cybersecurity context maps how sensitive data — particularly CUI — moves through your organization's systems, networks, and processes. It shows where CUI enters your environment, where it's stored, how it's processed, who accesses it, and where it's transmitted — both internally and to external parties.</p><p>CUI data flow diagrams are essential components of your System Security Plan. They help assessors understand the scope of your CUI environment and verify that appropriate security controls are in place at every point where CUI is stored, processed, or transmitted.</p>",
        "whyItMatters": "<p>Assessors use data flow diagrams to understand your CUI environment and verify that controls are applied everywhere CUI exists. Inaccurate or incomplete data flow diagrams can lead to missed controls and assessment findings.</p>",
    },
    {
        "term": "Air Gap",
        "definition": "<p>An air gap is a security measure where a computer or network is physically isolated from unsecured networks, including the internet. Air-gapped systems have no wired or wireless connections to outside networks, making remote attacks extremely difficult. Air gaps are used to protect the most sensitive systems and data.</p><p>While air gaps provide strong protection against remote attacks, they're not impervious — removable media, supply chain attacks, and sophisticated techniques can potentially bridge air gaps. Air-gapped systems also create operational challenges for updates, data transfer, and system management.</p>",
        "whyItMatters": "<p>While most defense contractors don't need air-gapped systems for CUI (CMMC covers CUI protection on connected systems), understanding air gaps helps you appreciate the spectrum of network isolation options for protecting your most sensitive data and systems.</p>",
    },
    {
        "term": "Micro-Segmentation",
        "definition": "<p>Micro-segmentation is a network security technique that divides the network into very small, isolated segments — potentially down to individual workloads or applications — each with its own security policies. Unlike traditional segmentation that creates broad network zones, micro-segmentation provides granular control over traffic between individual systems.</p><p>Micro-segmentation is a core component of Zero Trust architecture. It limits lateral movement — even if an attacker compromises one system, they can't move freely to other systems because each connection must pass through security controls and be explicitly authorized.</p>",
        "whyItMatters": "<p>Micro-segmentation supports CMMC requirements for system and communications protection. As the DoD moves toward Zero Trust, the ability to implement granular network controls will become increasingly valuable for defense contractors.</p>",
    },
    {
        "term": "Lateral Movement",
        "definition": "<p>Lateral movement refers to an attacker's ability to move from one compromised system to other systems within your network after gaining initial access. Once inside your network, attackers use stolen credentials, exploit trust relationships between systems, and leverage internal vulnerabilities to access additional systems and data.</p><p>Lateral movement is how attackers escalate from a foothold on one workstation to accessing your most sensitive servers and data. APT actors are particularly skilled at lateral movement, patiently moving through networks over weeks or months to reach their ultimate targets.</p>",
        "whyItMatters": "<p>Preventing lateral movement is why CMMC requires network segmentation, least privilege, and monitoring. These controls work together to detect and contain attackers who breach your perimeter, limiting their ability to reach CUI even if they compromise an initial system.</p>",
    },
    {
        "term": "Privilege Escalation",
        "definition": "<p>Privilege escalation occurs when an attacker exploits a vulnerability, design flaw, or misconfiguration to gain elevated access beyond what they're authorized for. Vertical escalation means gaining higher privileges (e.g., moving from a standard user to administrator). Horizontal escalation means gaining access to another user's resources at the same privilege level.</p><p>Attackers typically start with limited access — perhaps through a phished user account — and then use privilege escalation to gain the administrative access needed to access sensitive data, install persistent backdoors, or move freely through the network.</p>",
        "whyItMatters": "<p>Privilege escalation is a critical attack step that CMMC controls aim to prevent. Properly implementing least privilege, keeping systems patched, and monitoring for suspicious privilege changes all help contain attackers who gain initial access to your environment.</p>",
    },
    {
        "term": "Data Exfiltration",
        "definition": "<p>Data exfiltration is the unauthorized transfer of data from your organization to an external destination controlled by an attacker. This is often the attacker's ultimate objective — after gaining access and moving through your network, they identify valuable data (like CUI) and transfer it out through various channels: encrypted connections, cloud storage, email, DNS tunneling, or even physical media.</p><p>Detecting data exfiltration requires monitoring outbound network traffic for anomalies, implementing DLP solutions, and watching for unusual data access patterns. Advanced attackers use slow, encrypted exfiltration to avoid triggering volume-based alerts.</p>",
        "whyItMatters": "<p>Preventing CUI exfiltration is the ultimate objective of CMMC. All the access controls, encryption, monitoring, and security measures required by CMMC work together to prevent adversaries from stealing the sensitive defense information your company handles.</p>",
    },
    {
        "term": "Indicators of Attack (IOA)",
        "definition": "<p>Indicators of Attack (IOAs) are behavioral patterns that suggest an active attack is underway, as opposed to Indicators of Compromise (IOCs) which suggest a breach has already occurred. IOAs focus on attacker behavior in real-time — reconnaissance activity, exploitation attempts, lateral movement patterns, or data staging for exfiltration.</p><p>IOAs are more proactive than IOCs because they can detect attacks while they're happening, potentially before the attacker achieves their objective. Security tools that analyze behavior patterns rather than just matching known signatures are better at detecting IOAs.</p>",
        "whyItMatters": "<p>Detecting IOAs gives you the opportunity to stop attacks in progress before CUI is compromised. The continuous monitoring and incident detection capabilities required by CMMC should include behavioral analysis that can identify attack patterns in real time.</p>",
    },
    {
        "term": "Threat Actor",
        "definition": "<p>A threat actor is any individual, group, or organization that conducts or has the intent to conduct malicious cyber activities. Threat actors range from individual hackers and cybercriminal organizations to nation-state intelligence agencies and hacktivists. Each type has different motivations, capabilities, and methods.</p><p>For defense contractors, the primary threat actors are nation-state APT groups (seeking military and technological intelligence), cybercriminals (seeking financial gain through ransomware or fraud), and insider threats (employees who intentionally or accidentally compromise security).</p>",
        "whyItMatters": "<p>Understanding your threat actors helps you prioritize defenses against the most likely and most dangerous attacks. Defense contractors face nation-state adversaries — a higher-capability threat than most commercial organizations face — which is why CMMC requirements are comprehensive.</p>",
    },
    {
        "term": "Attack Surface",
        "definition": "<p>Your attack surface is the total set of points where an attacker could attempt to enter or extract data from your environment. It includes every network connection, public-facing service, user account, wireless access point, removable media port, and even your employees (who can be targeted through social engineering).</p><p>Reducing your attack surface is a core security strategy — the fewer entry points you expose, the fewer opportunities attackers have. This is achieved through network segmentation, disabling unnecessary services, removing unused accounts, restricting physical access, and minimizing the number of systems that interact with external networks.</p>",
        "whyItMatters": "<p>Many CMMC requirements — least functionality, access control, network segmentation, media protection — directly reduce your attack surface. Understanding your attack surface helps you identify which controls have the greatest security impact and where your biggest exposures are.</p>",
    },
    {
        "term": "Security Operations (SecOps)",
        "definition": "<p>Security Operations (SecOps) refers to the ongoing, day-to-day activities of monitoring, detecting, analyzing, and responding to cybersecurity threats across your organization. SecOps encompasses the people, processes, and technology that keep your security program running — from monitoring dashboards and investigating alerts to patching systems and responding to incidents.</p><p>SecOps is typically performed by a Security Operations Center (SOC) team, whether internal or outsourced to an MSSP/MDR provider. It's the operational engine that makes your security controls effective on an ongoing basis.</p>",
        "whyItMatters": "<p>Implementing security controls is only half the battle — operating them effectively every day is what actually protects your CUI. CMMC's continuous monitoring requirements necessitate ongoing security operations, not just initial implementation.</p>",
    },
    {
        "term": "Acceptable Use Policy (AUP)",
        "definition": "<p>An Acceptable Use Policy (AUP) defines the rules and guidelines for how employees and other users may use organizational IT resources — computers, networks, email, internet access, and data. It establishes what's permitted, what's prohibited, and the consequences of policy violations.</p><p>A well-written AUP covers topics like appropriate use of company equipment, email and internet usage guidelines, social media policies, handling of sensitive data, password requirements, removable media restrictions, and requirements for reporting security incidents.</p>",
        "whyItMatters": "<p>An AUP supports multiple CMMC requirements by establishing documented rules of behavior for system users. Assessors expect to see that users acknowledge and agree to acceptable use policies before being granted system access.</p>",
    },
    {
        "term": "Security Policy",
        "definition": "<p>A security policy is a formal document that defines your organization's approach to cybersecurity — what you protect, how you protect it, who is responsible, and what happens when policies are violated. Security policies set the direction and requirements for your security program, with specific procedures and standards providing the implementation details.</p><p>A comprehensive security policy framework includes overarching policy (organizational commitment and direction), topic-specific policies (access control, incident response, media protection), standards (specific required configurations), procedures (step-by-step instructions), and guidelines (recommended practices).</p>",
        "whyItMatters": "<p>Documented security policies are required by CMMC. Assessors will verify that you have policies addressing each CMMC domain and that those policies are communicated to users, reviewed regularly, and actually followed in practice.</p>",
    },
    {
        "term": "Security Posture",
        "definition": "<p>Security posture is the overall strength and readiness of your organization's cybersecurity defenses at any given point in time. It encompasses your security policies, controls, tools, training, incident response capabilities, and how effectively they all work together. Think of it as a holistic measure of how well-protected your organization is.</p><p>Your security posture is not static — it changes as you implement new controls, as threats evolve, as systems are added or changed, and as people join or leave. Continuous monitoring exists to maintain awareness of your security posture over time.</p>",
        "whyItMatters": "<p>Your SPRS score is a numeric representation of your security posture. But true security posture goes beyond a number — it's about whether your controls actually work, your people are trained, and your processes are followed. CMMC assessment evaluates your real security posture, not just your documentation.</p>",
    },
    {
        "term": "Cyber Resilience",
        "definition": "<p>Cyber resilience is your organization's ability to anticipate, withstand, recover from, and adapt to cyber attacks and other adverse conditions. While traditional cybersecurity focuses on preventing breaches, cyber resilience acknowledges that breaches will occur and focuses on ensuring your organization can continue operating and quickly recover when they do.</p><p>Cyber resilience combines security (preventing attacks), business continuity (maintaining operations during attacks), and disaster recovery (restoring operations after attacks) into a comprehensive approach that ensures organizational survival even under sustained cyber pressure.</p>",
        "whyItMatters": "<p>True cyber resilience goes beyond meeting CMMC checklist requirements. Building the ability to operate through and recover from attacks ensures you can continue supporting DoD missions even when adversaries succeed in their attacks.</p>",
    },
    {
        "term": "Threat Vector",
        "definition": "<p>A threat vector is the method or pathway an attacker uses to gain access to your systems or deliver a malicious payload. Common threat vectors include email (phishing), web browsers (drive-by downloads), remote access services (VPN exploitation), removable media (USB attacks), supply chain (compromised software updates), and social engineering (manipulating people).</p><p>Understanding your threat vectors helps you prioritize defenses. If most attacks against defense contractors come through email (they do), then investing in email security, phishing training, and email authentication provides high-impact protection.</p>",
        "whyItMatters": "<p>CMMC requirements address all major threat vectors — email filtering, web security, access controls, media protection, and security training. Understanding which vectors are most commonly exploited helps you prioritize implementation and focus on the highest-risk areas first.</p>",
    },
    {
        "term": "Multi-Tenancy",
        "definition": "<p>Multi-tenancy is a cloud architecture where multiple customers (tenants) share the same infrastructure, platforms, or applications while keeping their data logically separated. Most cloud services — SaaS, IaaS, and PaaS — use multi-tenant architectures to achieve economies of scale.</p><p>The security concern with multi-tenancy is ensuring proper isolation between tenants. If the cloud provider's isolation mechanisms fail, one tenant might be able to access another tenant's data. For CUI, you need assurance that the cloud provider's tenant isolation is strong enough to meet CMMC requirements.</p>",
        "whyItMatters": "<p>When evaluating cloud services for CUI workloads, understanding the provider's multi-tenancy model and tenant isolation mechanisms is important. FedRAMP authorization provides assurance that these isolation controls have been independently assessed.</p>",
    },
    {
        "term": "Encryption at Rest",
        "definition": "<p>Encryption at rest protects data that is stored on physical media — hard drives, SSDs, databases, backup tapes, and cloud storage. Even if an attacker gains physical access to the storage media (through theft, improper disposal, or insider access), encryption prevents them from reading the data without the encryption key.</p><p>Common implementations include full-disk encryption (like BitLocker or FileVault), database encryption, file-level encryption, and cloud storage encryption. For CUI, the encryption must use FIPS 140-2 or FIPS 140-3 validated cryptographic modules.</p>",
        "whyItMatters": "<p>CMMC requires FIPS-validated encryption for CUI at rest. This is a concrete, verifiable requirement — assessors will confirm that storage locations containing CUI are encrypted and that the encryption uses validated modules. Verify your solutions against the NIST CMVP database.</p>",
    },
    {
        "term": "Encryption in Transit",
        "definition": "<p>Encryption in transit protects data as it moves across networks — between your systems, to cloud services, over VPN connections, via email, and to external parties. It prevents anyone intercepting network traffic from reading the encrypted content. TLS/SSL is the most common protocol for encrypting data in transit.</p><p>For CUI, all network paths where CUI travels must be encrypted using FIPS-validated cryptography. This includes internal network traffic between CUI systems, not just external connections. Common implementations include TLS 1.2+ for web traffic, IPsec VPNs, and S/MIME for encrypted email.</p>",
        "whyItMatters": "<p>CMMC requires FIPS-validated encryption for CUI in transit on all network paths. Assessors will trace CUI data flows and verify encryption at each point. Unencrypted CUI transmission — even on internal networks — is a compliance finding.</p>",
    },
    {
        "term": "Defense Industrial Base (DIB)",
        "definition": "<p>The Defense Industrial Base (DIB) is the worldwide industrial complex that enables research and development, design, production, delivery, and maintenance of military weapons systems, subsystems, and components. It includes over 300,000 companies — from major defense primes to small machine shops — that contribute to the DoD's supply chain.</p><p>As a defense contractor, you are part of the DIB. The sector is a high-value target for nation-state cyber actors because it holds critical technology, military intelligence, and sensitive information that adversaries want to steal. CMMC exists specifically to raise the cybersecurity baseline across the entire DIB.</p>",
        "whyItMatters": "<p>Being part of the DIB means you're a target for sophisticated nation-state cyber attacks. Understanding that CMMC requirements exist to protect the entire defense supply chain — not just your individual company — provides context for why the requirements are comprehensive.</p>",
    },
    {
        "term": "NIST SP 800-172",
        "definition": "<p>NIST Special Publication 800-172 provides enhanced security requirements for protecting CUI in nonfederal systems and organizations when the CUI is associated with critical programs or high-value assets. These requirements go beyond 800-171 and are designed to defend against Advanced Persistent Threats (APTs).</p><p>The enhanced requirements in 800-172 focus on penetration-resistant architecture, damage-limiting operations, cyber resiliency, and security-focused system design. They form the basis for CMMC Level 3 requirements. Most defense contractors won't need 800-172 compliance, but those working on the most sensitive programs will.</p>",
        "whyItMatters": "<p>If your contracts require CMMC Level 3, you'll need to implement the enhanced requirements from NIST SP 800-172 in addition to the base 800-171 requirements. Understanding whether 800-172 applies to your work helps you plan your compliance investment.</p>",
    },
    {
        "term": "DCSA",
        "definition": "<p>The Defense Counterintelligence and Security Agency (DCSA) is the DoD agency responsible for personnel security investigations (background checks for security clearances), industrial security oversight (ensuring contractor facilities protect classified information), and counterintelligence support. DCSA administers the National Industrial Security Program (NISPOM).</p><p>If your company has or seeks a facility clearance, DCSA is the agency that conducts security inspections of your facility, processes clearance investigations for your employees, and ensures you meet the requirements for handling classified information.</p>",
        "whyItMatters": "<p>DCSA is a key agency for defense contractors involved in classified work. If your business growth strategy includes classified programs, understanding DCSA's role and building a relationship with your assigned DCSA representative is important for facility clearance and personnel clearance processes.</p>",
    },
    {
        "term": "NISPOM",
        "definition": "<p>The National Industrial Security Program Operating Manual (NISPOM) — now titled 32 CFR Part 117 — establishes the rules for how cleared defense contractors must protect classified information. It covers personnel security, physical security, information security, and the overall management of classified programs within contractor facilities.</p><p>While CMMC focuses on CUI (unclassified but sensitive information), NISPOM covers classified information at the Confidential, Secret, and Top Secret levels. Companies with facility clearances must comply with NISPOM requirements in addition to any CUI/CMMC requirements.</p>",
        "whyItMatters": "<p>If your company holds or pursues a facility clearance for classified work, NISPOM compliance is mandatory. Understanding the distinction between NISPOM (for classified) and CMMC (for CUI) helps you manage both compliance programs effectively.</p>",
    },
    {
        "term": "Controlled Technical Information (CTI)",
        "definition": "<p>Controlled Technical Information (CTI) is a category of CUI that includes technical information with military or space application that is subject to controls on access, use, reproduction, modification, performance, display, release, or disclosure. CTI is one of the most commonly encountered CUI categories for defense contractors.</p><p>CTI includes research and engineering data, engineering drawings, specifications, standards, process sheets, manuals, technical reports, and similar technical data. If you work with technical drawings, specifications, or engineering data for defense projects, you're likely handling CTI.</p>",
        "whyItMatters": "<p>CTI is CUI, which means it triggers CMMC requirements. Recognizing that your technical drawings, specifications, and engineering data likely qualify as CTI/CUI helps you properly scope your CMMC environment and ensure this data is protected.</p>",
    },
    {
        "term": "Export-Controlled Information",
        "definition": "<p>Export-controlled information is data, technology, or software that the U.S. government restricts from being shared with foreign persons or governments without proper authorization. Export controls are administered through the International Traffic in Arms Regulations (ITAR) for defense articles and the Export Administration Regulations (EAR) for dual-use items.</p><p>Export-controlled information is often also CUI. If you handle ITAR-controlled technical data, you must protect it from unauthorized foreign access — which means restricting access to U.S. persons, using secure storage and transmission, and potentially segregating foreign national employees from this data.</p>",
        "whyItMatters": "<p>Export-controlled information adds compliance requirements beyond CMMC. If you handle ITAR or EAR-controlled data, you need controls that restrict access based on citizenship in addition to standard CUI protections — a dimension assessors and regulators will verify.</p>",
    },
    {
        "term": "Mean Time to Detect (MTTD)",
        "definition": "<p>Mean Time to Detect (MTTD) is a security metric that measures the average time it takes for your organization to discover a security incident or breach after it occurs. A lower MTTD means you find breaches faster, reducing the time attackers have to operate in your environment and limiting the potential damage.</p><p>Industry studies consistently show that organizations with longer detection times suffer significantly more damage — attackers use the extra time to move laterally, escalate privileges, and exfiltrate more data. Reducing MTTD through improved monitoring, better alerting, and proactive threat hunting is a key security improvement goal.</p>",
        "whyItMatters": "<p>While CMMC doesn't specify MTTD targets, the continuous monitoring and audit requirements exist to reduce detection time. Tracking MTTD helps you measure whether your monitoring investments are actually improving your ability to catch incidents quickly.</p>",
    },
    {
        "term": "Mean Time to Respond (MTTR)",
        "definition": "<p>Mean Time to Respond (MTTR) is a security metric that measures the average time between detecting a security incident and containing or resolving it. A lower MTTR means your organization responds to threats faster, limiting the impact and reducing recovery costs.</p><p>Improving MTTR requires documented response procedures, trained response teams, appropriate response tools, and regular practice through tabletop exercises and drills. Automation can also reduce response times for common incident types.</p>",
        "whyItMatters": "<p>CMMC's incident response requirements exist to ensure your organization can respond effectively when incidents occur. Tracking MTTR provides a concrete measure of your incident response capability and helps you identify where your response process needs improvement.</p>",
    },
    {
        "term": "Security Token",
        "definition": "<p>A security token is a physical or digital device used as part of multi-factor authentication. Physical tokens include hardware devices that generate one-time codes (like RSA tokens or YubiKeys), while software tokens include authenticator apps on smartphones that generate time-based codes. The token provides 'something you have' as a second authentication factor.</p><p>Hardware security tokens provide stronger protection than SMS-based codes because they can't be intercepted through SIM swapping or phone compromise. FIDO2 security keys (like YubiKeys) provide the strongest token-based authentication, resistant to phishing attacks.</p>",
        "whyItMatters": "<p>Security tokens support CMMC's MFA requirements. Choosing the right type of token — hardware keys for highest security, authenticator apps for broader deployment — helps you balance security strength with usability for your organization.</p>",
    },
    {
        "term": "Single Sign-On (SSO)",
        "definition": "<p>Single Sign-On (SSO) is an authentication mechanism that allows users to log in once and gain access to multiple related systems and applications without re-entering credentials. SSO improves user experience (fewer passwords to remember) and can improve security (one strong authentication event replaces multiple weak ones) when properly implemented.</p><p>SSO works through identity federation protocols like SAML, OAuth, and OpenID Connect. When combined with MFA, SSO provides strong authentication across your application portfolio while reducing password fatigue and the associated security risks of password reuse.</p>",
        "whyItMatters": "<p>SSO supports CMMC authentication requirements by providing a centralized, consistent authentication experience. When combined with MFA, SSO reduces the number of credential sets users manage while maintaining strong security.</p>",
    },
    {
        "term": "Cybersecurity Maturity",
        "definition": "<p>Cybersecurity maturity describes how well-developed, institutionalized, and effective your security program is. A mature cybersecurity program has documented policies, trained personnel, tested procedures, automated monitoring, regular assessments, continuous improvement processes, and leadership engagement — not just security tools.</p><p>Maturity isn't just about having controls in place — it's about how consistently they're executed, how well they're documented, how regularly they're reviewed, and how effectively the organization learns from incidents and assessments. Moving from ad-hoc security to a mature program is a journey that requires sustained commitment.</p>",
        "whyItMatters": "<p>CMMC assessment evaluates not just whether controls exist, but whether they're practiced maturely. Demonstrating documented, consistent, and continuously improving security practices is what separates organizations that pass assessments from those that don't.</p>",
    },
    {
        "term": "Cybersecurity Incident",
        "definition": "<p>A cybersecurity incident is an event that actually or potentially jeopardizes the confidentiality, integrity, or availability of an information system or the information it processes, stores, or transmits, or that constitutes a violation of security policies. Not every security event is an incident — incidents are events that require a response.</p><p>For defense contractors, incidents involving CUI have specific reporting obligations under DFARS 252.204-7012, including notification to the DoD within 72 hours. The definition of what constitutes a reportable incident is important — it includes not just confirmed breaches but also events where CUI may have been compromised.</p>",
        "whyItMatters": "<p>Understanding what constitutes a cybersecurity incident — and particularly a reportable incident involving CUI — is essential for meeting your DFARS and CMMC obligations. Having clear incident classification criteria prevents both under-reporting (compliance risk) and over-reporting (operational disruption).</p>",
    },
    {
        "term": "Supply Chain Attack",
        "definition": "<p>A supply chain attack targets an organization by compromising a less-secure element in its supply chain — a software vendor, service provider, hardware supplier, or managed service provider. Instead of attacking the target directly, the adversary compromises a trusted vendor and uses that relationship to deliver malware or gain access to the target's environment.</p><p>High-profile supply chain attacks like SolarWinds (2020) and Kaseya (2021) demonstrated the devastating potential of this attack vector. Thousands of organizations were compromised through trusted software updates from their vendors. These attacks are particularly dangerous because the malware comes from a trusted source that security tools may not scrutinize closely.</p>",
        "whyItMatters": "<p>Supply chain risk management is addressed in CMMC requirements, and the DoD increasingly scrutinizes contractor supply chains. Evaluating your vendors' security practices, monitoring for supply chain compromises, and having incident response plans for vendor-related breaches are practical necessities.</p>",
    },
    {
        "term": "Penetration Test Report",
        "definition": "<p>A penetration test report is the formal document delivered after a penetration test, detailing the scope of testing, methodology used, vulnerabilities discovered, how they were exploited, the potential impact, and prioritized remediation recommendations. A good pen test report translates technical findings into business risk that leadership can understand.</p><p>The report typically categorizes findings by severity (Critical, High, Medium, Low, Informational), provides proof-of-concept evidence for each finding, and includes specific steps for remediation. Executive summaries present the high-level risk picture while technical details serve the remediation team.</p>",
        "whyItMatters": "<p>While penetration testing isn't specifically required at CMMC Level 2, pen test reports provide valuable evidence of your security program's effectiveness. The remediation actions from pen test findings directly improve your security posture and CMMC readiness.</p>",
    },
    {
        "term": "Security Awareness",
        "definition": "<p>Security awareness is the knowledge and attitude that members of your organization possess regarding the protection of physical and digital assets. It goes beyond formal training — it's the day-to-day consciousness that makes employees think twice before clicking a suspicious link, question an unusual request, or report something that doesn't seem right.</p><p>Building a security-aware culture requires consistent messaging, regular training, practical exercises (like phishing simulations), positive reinforcement for security-conscious behavior, and leadership that visibly prioritizes security. Security awareness transforms employees from potential vulnerabilities into active defenders.</p>",
        "whyItMatters": "<p>CMMC requires security awareness training for all system users. But true security awareness goes beyond annual training — it's about building a culture where security is everyone's responsibility and where employees are your first line of defense against social engineering and insider threats.</p>",
    },
    {
        "term": "Network Access Control (NAC)",
        "definition": "<p>Network Access Control (NAC) is a security approach that restricts which devices can connect to your network based on their identity, security posture, and compliance status. Before a device is granted network access, NAC checks whether it meets your security requirements — is it a known device, is its antivirus current, is it properly patched, does it meet your configuration standards?</p><p>Devices that don't meet requirements can be quarantined to a restricted network segment, given limited access, or blocked entirely. NAC helps prevent unauthorized or compromised devices from connecting to your CUI environment.</p>",
        "whyItMatters": "<p>NAC supports CMMC requirements for controlling system access and ensuring devices meet security standards. Preventing non-compliant or unauthorized devices from accessing your CUI network is a practical way to enforce multiple access control and configuration management requirements.</p>",
    },
]

def load_json(filename):
    """Load a JSON file from the data directory."""
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.isfile(filepath):
        print(f"  Warning: {filepath} not found, skipping.")
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_search_term(term_name: str) -> list[str]:
    """Extract the primary term and any abbreviation for matching."""
    terms = []
    # Full term without parenthetical
    base = re.sub(r"\s*\(.*?\)\s*", " ", term_name).strip()
    if base:
        terms.append(base.lower())
    # Abbreviation inside parentheses
    m = re.search(r"\(([^)]+)\)", term_name)
    if m:
        abbr = m.group(1).strip()
        if len(abbr) <= 12:  # Only use short abbreviations
            terms.append(abbr.lower())
    # Also add the full term as-is
    terms.append(term_name.lower())
    return list(set(terms))


def find_related_resources(term_name: str, cmmc_data, nist171_data, nist53_data):
    """Find related resources from compliance data files."""
    resources = []
    search_terms = extract_search_term(term_name)

    # Search CMMC practices
    if cmmc_data and "practices" in cmmc_data:
        for practice in cmmc_data["practices"]:
            title = (practice.get("title") or "").lower()
            domain = (practice.get("domain") or "").lower()
            for st in search_terms:
                if st in title or st in domain:
                    display_id = practice.get("displayId", practice["id"])
                    resources.append({
                        "label": f"CMMC: {display_id}",
                        "url": f"/cmmc/{practice['id']}"
                    })
                    break
            if len(resources) >= 8:
                break

    # Search NIST 800-171 requirements
    if nist171_data and "requirements" in nist171_data and len(resources) < 8:
        for req in nist171_data["requirements"]:
            title = (req.get("title") or "").lower()
            family = (req.get("family") or "").lower()
            for st in search_terms:
                if st in title or st in family:
                    display_id = req.get("displayId", req["id"])
                    resources.append({
                        "label": f"NIST 800-171: {display_id}",
                        "url": f"/nist-800-171/{req['id']}"
                    })
                    break
            if len(resources) >= 8:
                break

    # Search NIST 800-53 controls
    if nist53_data and "controls" in nist53_data and len(resources) < 8:
        for ctrl in nist53_data["controls"]:
            title = (ctrl.get("title") or "").lower()
            family = (ctrl.get("family") or "").lower()
            for st in search_terms:
                if st in title or st in family:
                    display_id = ctrl.get("displayId", ctrl["id"])
                    resources.append({
                        "label": f"NIST 800-53: {display_id}",
                        "url": f"/nist-800-53/{ctrl['id']}"
                    })
                    break
            if len(resources) >= 8:
                break

    # Deduplicate
    seen = set()
    unique = []
    for r in resources:
        key = r["url"]
        if key not in seen:
            seen.add(key)
            unique.append(r)
    return unique[:8]


def main():
    print("seed-glossary-data.py — Cardinal Six Cyber")
    print("=" * 50)

    # Load reference data
    print("\nLoading reference data...")
    cmmc_data = load_json("cmmc-practices.json")
    nist171_data = load_json("nist-800-171.json")
    nist53_data = load_json("nist-800-53.json")

    # Build glossary entries
    print(f"\nProcessing {len(TERMS)} terms...")
    glossary = []
    for entry in TERMS:
        term_name = entry["term"]
        term_id = slug(term_name)

        related = find_related_resources(
            term_name, cmmc_data, nist171_data, nist53_data
        )

        glossary.append({
            "id": term_id,
            "term": term_name,
            "definition": entry["definition"],
            "whyItMatters": entry["whyItMatters"],
            "relatedResources": related,
        })

    # Sort alphabetically by term
    glossary.sort(key=lambda x: x["term"].lower())

    # Write output
    os.makedirs(DATA_DIR, exist_ok=True)
    output_path = os.path.join(DATA_DIR, "glossary.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"terms": glossary}, f, indent=2, ensure_ascii=False)

    # Stats
    terms_with_resources = sum(1 for t in glossary if t["relatedResources"])
    total_resources = sum(len(t["relatedResources"]) for t in glossary)

    print(f"\n{'=' * 50}")
    print(f"Output: {output_path}")
    print(f"Total terms:                {len(glossary)}")
    print(f"Terms with resources:       {terms_with_resources}")
    print(f"Total related resources:    {total_resources}")
    print(f"Avg resources per term:     {total_resources / len(glossary):.1f}")
    print()

    # Verify
    if len(glossary) < 250:
        print(f"WARNING: Only {len(glossary)} terms — target is 250+")
    else:
        print(f"OK: {len(glossary)} terms meets 250+ target")


if __name__ == "__main__":
    main()
