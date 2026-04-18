"""
Practitioner notes for NIST 800-53 Rev 5 controls — Batch 4:
Program Management (PM), Personnel Security (PS),
PII Processing & Transparency (PT), Risk Assessment (RA),
and System & Services Acquisition (SA).

Keys match the control `id` field from nist-800-53.json.
Values are HTML strings rendered on the control detail pages.
"""

NOTES = {
    # ── Program Management (PM) ────────────────────────────────────────

    "pm-1": (
        "<p>This control requires your organization to have a written information security program "
        "plan — a single document that describes how you protect information across the entire "
        "company, not just one system. Think of it as your master playbook for cybersecurity.</p>"
        "<p><strong>Example 1:</strong> Create a security program plan document in SharePoint that "
        "covers your security goals, roles (who is responsible for what), the controls you have in "
        "place, and your timeline for improving. Use the NIST Cybersecurity Framework as your "
        "outline and update it annually or after any major incident.</p>"
        "<p><strong>Example 2:</strong> In Microsoft 365 Compliance Center, go to <em>Compliance "
        "Manager</em> and use it to track your overall security posture. The dashboard gives you a "
        "compliance score and maps your actions to specific control families, which feeds directly "
        "into your program plan documentation.</p>"
    ),

    "pm-2": (
        "<p>Someone senior in your organization must be formally designated as the information "
        "security program lead. In federal agencies this is the CISO or Senior Agency Information "
        "Security Officer (SAISO). For small businesses, it might be the owner or a designated IT "
        "manager — but it must be documented.</p>"
        "<p><strong>Example 1:</strong> Write an appointment memo signed by the CEO that names a "
        "specific person as the security program lead, outlines their authority to make security "
        "decisions, and confirms they have budget and staff support. Keep this memo in your "
        "governance folder.</p>"
        "<p><strong>Example 2:</strong> In your organizational chart, add the security program "
        "lead role with a direct reporting line to senior leadership. In M365 Admin Center, assign "
        "this person the <em>Security Administrator</em> and <em>Compliance Administrator</em> "
        "roles so they have visibility into the security posture of your tenant.</p>"
    ),

    "pm-3": (
        "<p>You need to plan and budget for security and privacy — it cannot be an afterthought. "
        "This means including cybersecurity line items in your capital planning and making sure "
        "security staff, tools, and training are funded each fiscal year.</p>"
        "<p><strong>Example 1:</strong> During annual budgeting, create a dedicated cybersecurity "
        "budget line that covers tool licenses (antivirus, SIEM, vulnerability scanner), training "
        "(Security+ certifications, annual awareness training), and any planned hardware upgrades "
        "like firewalls or encrypted drives.</p>"
        "<p><strong>Example 2:</strong> Use a spreadsheet or project management tool to track "
        "security investments against your Plan of Action and Milestones (POA&M). If your POA&M "
        "says you need to implement MFA by Q3, the budget should show the M365 E5 license cost "
        "that enables Azure AD Conditional Access with MFA enforcement.</p>"
    ),

    "pm-4": (
        "<p>A POA&M is your official to-do list for fixing security weaknesses. Every finding from "
        "audits, assessments, or scans should be tracked with a responsible person, a target "
        "completion date, and the resources needed to fix it.</p>"
        "<p><strong>Example 1:</strong> After a vulnerability scan, export the findings into a "
        "POA&M spreadsheet with columns for: weakness description, risk level, responsible party, "
        "estimated completion date, milestones, and current status. Review this document monthly "
        "with leadership.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Planner or Azure DevOps Boards to manage "
        "your POA&M items as tasks. Each task gets assigned to a team member, tagged with the "
        "control family it addresses, and tracked through stages (Open, In Progress, Mitigated, "
        "Closed). Generate a monthly status report from the board for leadership review.</p>"
    ),

    "pm-5": (
        "<p>You must maintain an up-to-date inventory of all the information systems your "
        "organization operates or relies on. If you do not know what systems you have, you cannot "
        "protect them.</p>"
        "<p><strong>Example 1:</strong> Create a system inventory spreadsheet listing every system "
        "by name, owner, classification level, authorization status, and the data types it "
        "processes. Include cloud services like M365, AWS instances, and SaaS tools your staff "
        "uses daily.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Defender for Cloud Apps, go to <em>Cloud "
        "Discovery</em> to automatically detect all cloud applications your employees are using. "
        "This catches shadow IT — services people signed up for without approval — and feeds "
        "your system inventory with real usage data.</p>"
    ),

    "pm-5-1": (
        "<p>This enhancement focuses specifically on tracking which of your systems handle "
        "personally identifiable information (PII). You need a dedicated inventory that maps where "
        "PII lives across your organization.</p>"
        "<p><strong>Example 1:</strong> Conduct a data mapping exercise where each department "
        "identifies what PII they collect (names, SSNs, addresses), where it is stored (database, "
        "file share, email), and who has access to it. Document this in a PII inventory matrix "
        "and review it annually.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Purview, use <em>Data Classification → "
        "Content Explorer</em> to scan your M365 environment for documents containing sensitive "
        "information types like Social Security numbers, credit card numbers, or health records. "
        "The results automatically feed your PII inventory.</p>"
    ),

    "pm-6": (
        "<p>You need metrics to know whether your security program is actually working. This "
        "control requires you to define, track, and report measurable security indicators to "
        "leadership on a regular basis.</p>"
        "<p><strong>Example 1:</strong> Track metrics like: percentage of systems with current "
        "authorization, average time to patch critical vulnerabilities, number of overdue POA&M "
        "items, phishing simulation click rate, and percentage of staff who completed security "
        "training. Report these monthly to leadership.</p>"
        "<p><strong>Example 2:</strong> In Microsoft 365 Defender, use the <em>Secure Score</em> "
        "dashboard as a baseline performance metric. Track your score over time and set quarterly "
        "improvement goals. Export the recommended actions list and use it to prioritize security "
        "improvements that measurably increase your score.</p>"
    ),

    "pm-7": (
        "<p>Your enterprise architecture — the overall design of your IT environment — must "
        "include security as a core consideration, not a bolt-on. Security requirements should "
        "shape how you design and build your technology infrastructure.</p>"
        "<p><strong>Example 1:</strong> When planning a network redesign, include security "
        "segmentation in the architecture diagrams. Place CUI-processing systems in a dedicated "
        "VLAN, put a firewall between your corporate and guest networks, and document these "
        "decisions in your enterprise architecture documentation.</p>"
        "<p><strong>Example 2:</strong> In Azure, use <em>Azure Landing Zones</em> to structure "
        "your cloud architecture with security built in from the start. This includes network "
        "segmentation, identity management through Azure AD, and centralized logging — all "
        "documented as part of your enterprise architecture blueprint.</p>"
    ),

    "pm-7-1": (
        "<p>Offloading means moving certain security functions or services to another organization "
        "or provider. If your company lacks the resources to run a 24/7 security operations "
        "center, you might offload that function to a managed security service provider (MSSP).</p>"
        "<p><strong>Example 1:</strong> Contract with an MSSP to handle your SIEM monitoring, "
        "incident detection, and initial triage. Document in your security plan which functions "
        "are offloaded, who the provider is, and what SLAs govern their performance (e.g., "
        "15-minute response time for critical alerts).</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Sentinel as your cloud SIEM and engage a "
        "Microsoft partner for managed detection and response. Document the shared responsibility "
        "model — what the partner monitors, what triggers they escalate, and what your internal "
        "team handles — in your security program plan.</p>"
    ),

    "pm-8": (
        "<p>If your organization operates or supports critical infrastructure, you need a plan "
        "that addresses how you protect those assets. This ties your security program to sector-"
        "specific requirements from DHS, CISA, or your industry regulator.</p>"
        "<p><strong>Example 1:</strong> If you are a defense contractor, document how your "
        "systems support the Defense Industrial Base (DIB) sector. Map your critical assets to "
        "the services they enable and identify single points of failure. Include this analysis "
        "in your security program plan.</p>"
        "<p><strong>Example 2:</strong> Register with CISA's Cybersecurity Assessments program "
        "and complete their Cyber Resilience Review (CRR) self-assessment. The results will "
        "identify gaps in your critical infrastructure protection plan and give you a structured "
        "roadmap for improvement.</p>"
    ),

    "pm-9": (
        "<p>Your risk management strategy defines how your organization identifies, assesses, "
        "and responds to risk at the enterprise level. This is the high-level framework that "
        "drives all your individual risk decisions.</p>"
        "<p><strong>Example 1:</strong> Write a one-page risk management strategy memo that "
        "defines your risk tolerance (e.g., 'We accept low risks, mitigate moderate risks, and "
        "avoid or transfer high risks'), the risk assessment methodology you will use (NIST "
        "RMF, FAIR), and how often you will reassess risks (annually and after major changes).</p>"
        "<p><strong>Example 2:</strong> Create a risk register in Excel or a GRC tool that "
        "categorizes each risk by likelihood and impact, assigns a risk owner, and tracks the "
        "chosen response (accept, mitigate, transfer, avoid). Review the register quarterly "
        "with leadership and update it whenever new threats emerge or your environment changes.</p>"
    ),

    "pm-10": (
        "<p>Every system that processes, stores, or transmits organizational data needs a formal "
        "authorization to operate (ATO). This control establishes the process for granting, "
        "reviewing, and revoking those authorizations.</p>"
        "<p><strong>Example 1:</strong> Define an authorization process where each system owner "
        "submits a security package (system security plan, risk assessment, POA&M) to an "
        "authorizing official. The AO reviews the package, accepts residual risk, and issues "
        "a signed ATO letter with a defined duration (typically 3 years with annual reviews).</p>"
        "<p><strong>Example 2:</strong> Use a GRC platform like eMASS, Xacta, or even a "
        "structured SharePoint site to manage authorization packages. Track each system's "
        "authorization status (Pre-ATO, ATO, DATO, ATO Expired) and set automated reminders "
        "90 days before expiration so reauthorization starts on time.</p>"
    ),

    "pm-11": (
        "<p>You need to define your mission and business processes clearly enough to identify "
        "which ones depend on information security. This ensures security resources are focused "
        "on what matters most to your operations.</p>"
        "<p><strong>Example 1:</strong> Map your key business processes (contract management, "
        "proposal development, engineering design) and identify the information systems each one "
        "depends on. Then rank them by criticality so you know which systems need the strongest "
        "protections and fastest recovery times.</p>"
        "<p><strong>Example 2:</strong> Conduct a Business Impact Analysis (BIA) that documents "
        "each critical process, the maximum tolerable downtime, and the data classification of "
        "information involved. Use the BIA results to justify security investments and set "
        "recovery time objectives for your backup and disaster recovery planning.</p>"
    ),

    "pm-12": (
        "<p>An insider threat program helps you detect, deter, and respond to risks from people "
        "inside your organization — employees, contractors, or partners who might misuse their "
        "access, whether intentionally or accidentally.</p>"
        "<p><strong>Example 1:</strong> Establish an insider threat working group that includes "
        "HR, legal, IT security, and management. Define behavioral indicators to watch for "
        "(mass file downloads, after-hours access to sensitive data, resignation followed by "
        "unusual data transfers) and create response procedures for each scenario.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Purview, enable <em>Insider Risk "
        "Management</em> policies to detect risky user activities like data exfiltration, "
        "security policy violations, or departing employee data theft. Configure alerts to "
        "go to your insider threat team for investigation and resolution.</p>"
    ),

    "pm-13": (
        "<p>Your security program is only as good as the people running it. This control requires "
        "you to build and maintain a workforce with the skills and certifications needed to "
        "protect your organization.</p>"
        "<p><strong>Example 1:</strong> Create a security workforce plan that identifies the "
        "roles you need (system admin, security analyst, compliance officer), the certifications "
        "each role requires (Security+, CISSP, CISM), and your plan for filling gaps through "
        "hiring, training, or contracting.</p>"
        "<p><strong>Example 2:</strong> Budget for annual training and certification renewals. "
        "Send your IT staff to SANS courses or use platforms like Cybrary or NICCS for "
        "role-based training. Track certifications in a spreadsheet and set renewal reminders "
        "so nobody lapses. Document DoD 8140 compliance if working on federal contracts.</p>"
    ),

    "pm-14": (
        "<p>This control ties together your security testing, training, and monitoring programs. "
        "You need to regularly test your controls, train your people, and monitor your "
        "environment — and these three activities should inform each other.</p>"
        "<p><strong>Example 1:</strong> Build an annual calendar that schedules quarterly "
        "vulnerability scans, annual penetration testing, monthly phishing simulations, and "
        "annual security awareness training. After each activity, feed the results into your "
        "POA&M and update training content to address weaknesses found.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Defender for Endpoint to continuously "
        "monitor your devices and Microsoft 365 Attack Simulator for phishing tests. When "
        "the phishing tests show high click rates in a department, schedule targeted training "
        "for that group. Use Defender's Threat and Vulnerability Management dashboard to "
        "prioritize patching based on real exposure data.</p>"
    ),

    "pm-15": (
        "<p>Staying informed about cybersecurity threats and best practices means joining "
        "relevant professional groups and information-sharing organizations. You do not have "
        "to figure everything out alone.</p>"
        "<p><strong>Example 1:</strong> Join the Defense Industrial Base Cybersecurity (DIB CS) "
        "program and sign up for CISA alerts and advisories. These give you early warning about "
        "threats targeting your sector and practical guidance on how to respond.</p>"
        "<p><strong>Example 2:</strong> Subscribe to your sector's Information Sharing and "
        "Analysis Center (ISAC) — for defense contractors, that is the DIB ISAC. For healthcare "
        "organizations, join Health-ISAC. These organizations share threat intelligence, "
        "indicators of compromise, and best practices specific to your industry.</p>"
    ),

    "pm-16": (
        "<p>A threat awareness program keeps your organization informed about current threats "
        "targeting your sector, your technology stack, or organizations like yours. This goes "
        "beyond generic awareness training — it is about operational threat intelligence.</p>"
        "<p><strong>Example 1:</strong> Subscribe to threat intelligence feeds like CISA's "
        "Automated Indicator Sharing (AIS), AlienVault OTX, or a commercial feed. Designate "
        "someone to review weekly threat briefings and distribute relevant alerts to system "
        "administrators and security staff.</p>"
        "<p><strong>Example 2:</strong> Configure Microsoft Sentinel to ingest threat "
        "intelligence indicators and automatically correlate them against your log data. When "
        "a known malicious IP or domain appears in your logs, Sentinel generates an alert. "
        "Brief leadership quarterly on the threat landscape and any incidents detected.</p>"
    ),

    "pm-16-1": (
        "<p>This enhancement requires using automated tools to share and consume threat "
        "intelligence rather than relying solely on manual processes like email alerts or "
        "PDF reports.</p>"
        "<p><strong>Example 1:</strong> Implement STIX/TAXII feeds in your SIEM so threat "
        "indicators (malicious IPs, domains, file hashes) are automatically ingested and "
        "correlated against your network traffic and endpoint telemetry without human "
        "intervention.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Sentinel, go to <em>Threat Intelligence "
        "→ Data Connectors</em> and enable the TAXII or Microsoft Defender Threat Intelligence "
        "connector. This automatically pulls in threat indicators and creates detection rules "
        "that fire when those indicators are seen in your environment.</p>"
    ),

    "pm-17": (
        "<p>When your CUI or other controlled information is processed on external systems — "
        "contractor laptops, cloud services, partner networks — you need policies and controls "
        "to protect it even though you do not own those systems.</p>"
        "<p><strong>Example 1:</strong> Include CUI protection clauses in all contracts and "
        "service agreements. Require subcontractors to meet NIST 800-171 requirements and "
        "provide evidence of compliance before granting them access to your controlled "
        "information.</p>"
        "<p><strong>Example 2:</strong> In Microsoft 365, use <em>Sensitivity Labels</em> to "
        "mark CUI documents. Configure Data Loss Prevention (DLP) policies that prevent labeled "
        "documents from being shared externally without encryption. This protects CUI even when "
        "it travels outside your direct control to partner organizations.</p>"
    ),

    "pm-18": (
        "<p>Just like your security program plan (PM-1), you need a separate privacy program "
        "plan that describes how your organization protects personally identifiable information "
        "across all systems and processes.</p>"
        "<p><strong>Example 1:</strong> Write a privacy program plan that covers what PII you "
        "collect, why you collect it, how long you keep it, who can access it, and how you "
        "dispose of it. Include your legal basis for processing (consent, contract, legal "
        "obligation) and your breach notification procedures.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Purview Compliance Manager, use the "
        "<em>Privacy</em> assessment templates to track your privacy controls. The dashboard "
        "shows your privacy compliance score and identifies gaps in your program. Use the "
        "recommended improvement actions as your privacy program roadmap.</p>"
    ),

    "pm-19": (
        "<p>Appoint someone with authority and resources to lead your privacy program. For "
        "federal agencies this is the Senior Agency Official for Privacy (SAOP). For private "
        "companies, this might be a privacy officer, DPO, or a senior manager with privacy "
        "responsibilities.</p>"
        "<p><strong>Example 1:</strong> Issue a formal memo designating your privacy program "
        "lead. Define their responsibilities: overseeing PII inventories, approving privacy "
        "impact assessments, managing breach response, and reporting privacy metrics to "
        "leadership.</p>"
        "<p><strong>Example 2:</strong> Assign your designated privacy lead the <em>Privacy "
        "Management</em> role in Microsoft Purview so they have access to privacy dashboards, "
        "data subject request tools, and compliance reports. This gives them the technical "
        "visibility needed to manage the program effectively.</p>"
    ),

    "pm-20": (
        "<p>Make your privacy program information available to the public and to your employees. "
        "People should be able to easily find out how you handle their personal information.</p>"
        "<p><strong>Example 1:</strong> Publish a clear, plain-language privacy policy on your "
        "website that explains what data you collect, why, how you protect it, and how people "
        "can exercise their privacy rights (access, correction, deletion). Update it whenever "
        "your data practices change.</p>"
        "<p><strong>Example 2:</strong> Create an internal privacy page on your company intranet "
        "or SharePoint site with FAQs for employees: how to handle customer PII, what to do if "
        "they suspect a data breach, and who the privacy contact is. Make this part of new "
        "employee onboarding.</p>"
    ),

    "pm-20-1": (
        "<p>Your websites, apps, and digital services must prominently display privacy policies "
        "that explain your data collection and use practices. This is especially important for "
        "public-facing services.</p>"
        "<p><strong>Example 1:</strong> Add a privacy policy link in the footer of every page "
        "on your website. If your site uses cookies or analytics, include a cookie consent "
        "banner that lets visitors opt in or out. Make sure the privacy policy specifically "
        "describes what each cookie and tracker does.</p>"
        "<p><strong>Example 2:</strong> For any web forms that collect personal information "
        "(contact forms, account signups), include a brief privacy notice directly on the form "
        "explaining what data is collected and why. Link to the full privacy policy. Use "
        "Microsoft Clarity or Google Analytics with anonymized IP settings and disclose this "
        "in your privacy policy.</p>"
    ),

    "pm-21": (
        "<p>You must track when you disclose PII to third parties and be able to account for "
        "those disclosures if an individual asks. This is a Privacy Act requirement for federal "
        "agencies and a best practice for any organization handling PII.</p>"
        "<p><strong>Example 1:</strong> Maintain a disclosure log that records every time PII "
        "is shared with an outside party — who received it, what data was shared, the date, "
        "the purpose, and the legal authority. Review this log quarterly with your privacy "
        "officer.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Purview, use <em>Data Subject Requests</em> "
        "to track and respond to individuals asking what disclosures have been made about their "
        "data. Automate the search across Exchange, SharePoint, and Teams to compile a complete "
        "picture of where a person's data has been shared.</p>"
    ),

    "pm-22": (
        "<p>PII must be accurate, relevant, timely, and complete for the purpose it is being "
        "used. Bad data leads to bad decisions that affect real people — wrong addresses, "
        "incorrect records, or outdated information.</p>"
        "<p><strong>Example 1:</strong> Implement a data quality review process where records "
        "containing PII are verified periodically. For employee records, require annual "
        "self-verification where each employee confirms their contact information, emergency "
        "contacts, and other personal details are current.</p>"
        "<p><strong>Example 2:</strong> If you maintain a customer database, build data "
        "validation rules into your forms (valid email format, address verification) and run "
        "quarterly duplicate and stale-record reports. Use tools like Power Automate to flag "
        "records that have not been updated in 12+ months for manual review.</p>"
    ),

    "pm-23": (
        "<p>A data governance body is a group within your organization responsible for making "
        "decisions about how data is managed, shared, protected, and disposed of. It ensures "
        "data practices are consistent and compliant across the organization.</p>"
        "<p><strong>Example 1:</strong> Form a data governance committee that includes your "
        "privacy officer, CISO, legal counsel, and representatives from major business units. "
        "Meet quarterly to review data policies, approve new data collection activities, and "
        "resolve data-sharing disputes.</p>"
        "<p><strong>Example 2:</strong> Charter the committee with a formal terms of reference "
        "document that defines their scope, decision authority, and escalation path. Use "
        "Microsoft Purview's <em>Data Catalog</em> to give the committee visibility into data "
        "assets, classifications, and lineage across the organization.</p>"
    ),

    "pm-24": (
        "<p>A data integrity board is specifically responsible for overseeing computer matching "
        "programs — activities that compare records from different systems to find matches. This "
        "is primarily a federal requirement under the Privacy Act.</p>"
        "<p><strong>Example 1:</strong> If your organization conducts computer matching (comparing "
        "personnel records against contractor databases, for instance), establish a board that "
        "reviews and approves each matching agreement, ensures proper notice is given, and "
        "verifies that matches are accurate before action is taken.</p>"
        "<p><strong>Example 2:</strong> Document each matching program in a formal agreement "
        "that specifies what data is matched, the purpose, retention periods, and safeguards. "
        "The data integrity board should review these agreements annually and ensure they are "
        "published in the Federal Register if required.</p>"
    ),

    "pm-25": (
        "<p>When you use data for testing, training, or research, you should minimize or "
        "eliminate real PII. Use synthetic, de-identified, or anonymized data instead so that "
        "a breach of test data does not expose real people's information.</p>"
        "<p><strong>Example 1:</strong> Before using production data in a test environment, run "
        "it through a data masking tool that replaces real names, SSNs, and addresses with "
        "realistic but fake values. Tools like Redgate Data Masker or open-source Faker "
        "libraries can generate convincing test data without real PII.</p>"
        "<p><strong>Example 2:</strong> Write a policy that prohibits using production databases "
        "in development or training environments without data sanitization. In Azure SQL, use "
        "<em>Dynamic Data Masking</em> to automatically obscure sensitive columns so developers "
        "see masked values while the application still functions normally.</p>"
    ),

    "pm-26": (
        "<p>You need a process for receiving, tracking, and responding to privacy complaints "
        "from individuals. When someone believes their personal information has been mishandled, "
        "they need a clear path to raise the concern.</p>"
        "<p><strong>Example 1:</strong> Publish a privacy complaint email address and form on "
        "your website. Create a complaint tracking spreadsheet or ticketing system that logs "
        "each complaint, the date received, assigned investigator, resolution, and response "
        "date. Target a 30-day resolution window.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Forms to create a privacy complaint "
        "intake form, then connect it to a Power Automate flow that creates a task in Planner, "
        "assigns it to your privacy officer, and sends an acknowledgment email to the "
        "complainant within 48 hours.</p>"
    ),

    "pm-27": (
        "<p>Your privacy program must produce regular reports for leadership and oversight "
        "bodies on the state of privacy within your organization — what is working, what "
        "needs attention, and any incidents that occurred.</p>"
        "<p><strong>Example 1:</strong> Create a quarterly privacy report that covers: number "
        "of data subject requests received and completed, privacy incidents and breaches, "
        "status of privacy impact assessments, training completion rates, and any new data "
        "collection activities approved by the governance body.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Purview, export the <em>Data Subject "
        "Request</em> reports and <em>Compliance Score</em> trends. Combine these with your "
        "manual tracking data into a dashboard (Power BI works well) that leadership can "
        "review at a glance during governance meetings.</p>"
    ),

    "pm-28": (
        "<p>Risk framing sets the context for how your organization thinks about and evaluates "
        "risk. It defines your risk assumptions, constraints, tolerance levels, and priorities "
        "before you start assessing individual risks.</p>"
        "<p><strong>Example 1:</strong> Develop a risk framing document that defines your "
        "organization's risk appetite in plain terms: 'We will not accept any risk that could "
        "result in loss of CUI,' or 'We will accept low-impact operational risks if mitigation "
        "costs exceed the potential loss by 5x.' Get leadership sign-off.</p>"
        "<p><strong>Example 2:</strong> Use the NIST RMF 'Prepare' step to create your risk "
        "framing. Document your threat assumptions (what adversaries are likely to target you), "
        "your vulnerability assumptions (where you know you are weak), and your impact "
        "definitions (what constitutes low, moderate, or high impact to your business).</p>"
    ),

    "pm-29": (
        "<p>This control ensures that senior leaders across your organization — not just the "
        "CISO — have defined roles in the risk management program. Risk management is a "
        "leadership responsibility, not just an IT function.</p>"
        "<p><strong>Example 1:</strong> Define risk management roles for the CEO (risk "
        "acceptance authority), CFO (risk financing and insurance), CISO (technical risk "
        "management), and business unit leads (operational risk owners). Document these roles "
        "in your risk management strategy and communicate them organization-wide.</p>"
        "<p><strong>Example 2:</strong> Create a RACI chart (Responsible, Accountable, "
        "Consulted, Informed) for your risk management program that maps each major risk "
        "activity to the appropriate leader. Post this chart in your governance documentation "
        "and reference it during risk review meetings.</p>"
    ),

    "pm-30": (
        "<p>Supply chain risk management (SCRM) means understanding and managing the risks "
        "that come from your suppliers, vendors, and service providers. A compromised vendor "
        "can become your organization's biggest vulnerability.</p>"
        "<p><strong>Example 1:</strong> Write an SCRM strategy that defines how you evaluate "
        "vendors before signing contracts (security questionnaires, SOC 2 reports, penetration "
        "test results), how you monitor them during the relationship, and how you handle a "
        "vendor security incident. Apply more scrutiny to vendors with access to sensitive data.</p>"
        "<p><strong>Example 2:</strong> Maintain a vendor risk register that categorizes each "
        "supplier by criticality (how dependent are you on them) and risk (what data or systems "
        "they can access). Use a vendor risk management platform or a structured spreadsheet to "
        "track each vendor's compliance status, contract renewal dates, and last assessment.</p>"
    ),

    "pm-30-1": (
        "<p>This enhancement focuses specifically on vendors who supply critical or mission-"
        "essential items — components, software, or services without which your operations "
        "would stop. These suppliers need the most scrutiny.</p>"
        "<p><strong>Example 1:</strong> Identify your single-source suppliers and components "
        "that have no viable alternatives. For each one, develop a contingency plan: an "
        "alternate supplier, a stockpile of spare parts, or an internal capability to "
        "replicate the function if the supplier is compromised or unavailable.</p>"
        "<p><strong>Example 2:</strong> Require critical suppliers to provide a Software Bill "
        "of Materials (SBOM) for any software they deliver. Review the SBOM for known "
        "vulnerabilities using tools like OWASP Dependency-Check or Snyk, and include SBOM "
        "requirements in your procurement contracts.</p>"
    ),

    "pm-31": (
        "<p>Continuous monitoring means you are watching your security posture all the time, "
        "not just during annual assessments. This control requires a documented strategy for "
        "how you will monitor controls, vulnerabilities, and threats on an ongoing basis.</p>"
        "<p><strong>Example 1:</strong> Write a continuous monitoring strategy that defines: "
        "what you monitor (network traffic, endpoint health, configuration compliance, "
        "vulnerability scan results), how often (real-time, daily, weekly, monthly), and who "
        "reviews the results. Map each monitoring activity to the controls it validates.</p>"
        "<p><strong>Example 2:</strong> Deploy Microsoft Sentinel as your continuous monitoring "
        "platform. Configure data connectors for Azure AD sign-in logs, Defender for Endpoint "
        "alerts, firewall logs, and vulnerability scan results. Create analytic rules that "
        "automatically detect control failures and trigger incidents for your security team.</p>"
    ),

    "pm-32": (
        "<p>Purposing means ensuring that systems are used only for their intended and "
        "authorized purposes. Every system should have a clearly defined purpose, and usage "
        "outside that purpose should be detected and addressed.</p>"
        "<p><strong>Example 1:</strong> In each system security plan, clearly state the "
        "system's authorized purpose and the types of data it is approved to process. During "
        "annual reviews, verify that the system is still being used as documented and that "
        "no unauthorized data types have crept in.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Purview Data Loss Prevention (DLP) "
        "policies to detect when sensitive data types appear in systems not authorized to "
        "process them. For example, if a file share is approved for general business data "
        "only, a DLP rule can alert you when someone stores documents containing SSNs or "
        "CUI markings there.</p>"
    ),

    # ── Personnel Security (PS) ────────────────────────────────────────

    "ps-1": (
        "<p>You need documented personnel security policies and procedures that cover the "
        "entire employee lifecycle — from hiring through termination. These policies govern "
        "how you screen, onboard, manage, and offboard people with access to your systems.</p>"
        "<p><strong>Example 1:</strong> Write a personnel security policy that covers "
        "background checks, access agreements, security training requirements, personnel "
        "transfer procedures, and termination checklists. Store it in SharePoint and require "
        "annual review and leadership signature.</p>"
        "<p><strong>Example 2:</strong> Create a personnel security procedures document that "
        "walks HR and IT through each step: how to request a background check, what forms new "
        "employees sign, how access is provisioned in Azure AD, and the exact steps to disable "
        "accounts and collect equipment when someone leaves.</p>"
    ),

    "ps-2": (
        "<p>Every position in your organization that involves access to information systems "
        "must be assigned a risk designation (low, moderate, or high) based on the potential "
        "damage someone in that position could cause. This determines the level of background "
        "screening required.</p>"
        "<p><strong>Example 1:</strong> Review every job description and assign a risk level. "
        "A system administrator with root access to servers is high risk. A general office "
        "worker with email-only access is low risk. Document these designations in a position "
        "risk matrix and use it to determine background check requirements.</p>"
        "<p><strong>Example 2:</strong> Work with HR to embed risk designations into your "
        "position description templates. When creating or modifying a position in your HRIS "
        "(Workday, ADP, BambooHR), include a required field for the IT risk designation so "
        "it is always documented and drives the appropriate screening process.</p>"
    ),

    "ps-3": (
        "<p>Everyone who will have access to your information systems must be screened "
        "(background checked) before they get access. The depth of the screening should match "
        "the risk level of their position.</p>"
        "<p><strong>Example 1:</strong> For low-risk positions, run a basic criminal background "
        "check and verify employment history. For moderate-risk positions, add a credit check "
        "and reference checks. For high-risk positions or those requiring access to classified "
        "information, initiate an investigation through the Defense Counterintelligence and "
        "Security Agency (DCSA).</p>"
        "<p><strong>Example 2:</strong> Use a background check provider like Sterling, HireRight, "
        "or GoodHire integrated with your HR system. Set up rules so that when HR creates a new "
        "hire record, the system automatically triggers the appropriate level of screening based "
        "on the position risk designation. No screening result, no system access.</p>"
    ),

    "ps-3-1": (
        "<p>Personnel who will access classified information must be screened and cleared at "
        "the appropriate level before access is granted. This goes beyond standard background "
        "checks to formal security clearance investigations.</p>"
        "<p><strong>Example 1:</strong> Submit personnel security investigation requests through "
        "DCSA's National Background Investigation Services (NBIS) system. Track clearance "
        "status for all personnel in a clearance tracking database and verify that no one "
        "accesses classified systems before their investigation is favorably adjudicated.</p>"
        "<p><strong>Example 2:</strong> Maintain a facility clearance and personnel clearance "
        "log that records each person's clearance level, investigation type (T3, T5), "
        "adjudication date, and reinvestigation due date. In your classified environment, "
        "configure access controls so that only personnel with current clearances listed in "
        "DISS (Defense Information System for Security) can log in.</p>"
    ),

    "ps-3-2": (
        "<p>Formal indoctrination means that before someone accesses information requiring "
        "special protections (like SCI — Sensitive Compartmented Information), they must go "
        "through a formal briefing that explains their responsibilities and the consequences "
        "of unauthorized disclosure.</p>"
        "<p><strong>Example 1:</strong> Conduct a formal indoctrination briefing for all "
        "personnel being read into a special access program. Cover the program's security "
        "requirements, handling procedures, reporting obligations, and penalties for "
        "unauthorized disclosure. Have each person sign an indoctrination acknowledgment form.</p>"
        "<p><strong>Example 2:</strong> Maintain a signed SF-312 (Classified Information "
        "Nondisclosure Agreement) for every cleared employee. Store these forms in a secure, "
        "locked file cabinet and track execution dates in your security database. No signed "
        "NDA, no access — enforce this without exception.</p>"
    ),

    "ps-3-3": (
        "<p>Some information requires protective measures beyond standard classification — "
        "things like nuclear information, intelligence sources and methods, or critical "
        "infrastructure vulnerability data. Personnel accessing this information need "
        "additional screening.</p>"
        "<p><strong>Example 1:</strong> Identify which information in your environment requires "
        "special protective measures (e.g., NATO Restricted, COMSEC material, nuclear data) "
        "and document the additional screening requirements for personnel who will handle it.</p>"
        "<p><strong>Example 2:</strong> Implement a formal access request process where the "
        "data owner certifies the need-to-know before granting access to specially protected "
        "information. Log all access approvals and denials and review the access list "
        "semiannually.</p>"
    ),

    "ps-3-4": (
        "<p>Certain positions may require U.S. citizenship or specific citizenship status. "
        "This is common in defense, intelligence, and federal contractor environments where "
        "access to classified or export-controlled information is restricted by law.</p>"
        "<p><strong>Example 1:</strong> For positions that require access to classified "
        "information or ITAR-controlled technical data, verify U.S. citizenship before "
        "granting access. Acceptable documentation includes a U.S. passport, birth "
        "certificate, or naturalization certificate.</p>"
        "<p><strong>Example 2:</strong> Work with HR to flag positions with citizenship "
        "requirements in your job postings and HRIS. Verify citizenship documentation as part "
        "of the onboarding process and store verification records in the employee's security "
        "file, separate from their general HR file.</p>"
    ),

    "ps-4": (
        "<p>When someone leaves your organization — whether they resign, retire, or are "
        "terminated — you must immediately revoke their access and recover all organizational "
        "assets. Speed matters, especially for involuntary separations.</p>"
        "<p><strong>Example 1:</strong> Create a termination checklist that HR and IT execute "
        "together: disable Active Directory account within 1 hour of departure, disable M365 "
        "account, revoke VPN credentials, collect laptop and badges, change shared passwords "
        "they knew, and remove them from distribution lists and shared mailboxes.</p>"
        "<p><strong>Example 2:</strong> In Azure AD, configure <em>Lifecycle Workflows</em> "
        "to automatically disable accounts and revoke sessions when HR marks an employee as "
        "terminated in your HRIS. Set up an integration between your HR system and Azure AD "
        "so the moment a termination date is entered, access revocation begins automatically.</p>"
    ),

    "ps-4-1": (
        "<p>Some departing employees may have post-employment obligations — things like "
        "nondisclosure agreements that continue after they leave, or restrictions on working "
        "for competitors. These need to be clearly communicated during exit processing.</p>"
        "<p><strong>Example 1:</strong> During the exit interview, review continuing "
        "obligations with the departing employee: nondisclosure agreements, non-compete clauses, "
        "restrictions on using proprietary information, and requirements to return all copies "
        "of sensitive data. Have them sign an acknowledgment of these ongoing obligations.</p>"
        "<p><strong>Example 2:</strong> Maintain a post-employment obligations tracker that "
        "records each former employee's name, departure date, and the specific agreements "
        "that remain in effect. Set calendar reminders for when restrictions expire so your "
        "legal team can follow up if needed.</p>"
    ),

    "ps-4-2": (
        "<p>Automate the access revocation process for terminated employees rather than relying "
        "on manual steps. People forget checklists; automated systems do not.</p>"
        "<p><strong>Example 1:</strong> Integrate your HRIS with Azure AD using SCIM provisioning "
        "so that when HR changes an employee's status to 'terminated,' their accounts are "
        "automatically disabled across all connected applications within minutes.</p>"
        "<p><strong>Example 2:</strong> In Azure AD, set up <em>Access Reviews</em> that "
        "automatically remove access when a reviewer does not respond within the review period, "
        "and configure <em>Lifecycle Workflows</em> to trigger account disablement, session "
        "revocation, and manager notification when a termination event is detected.</p>"
    ),

    "ps-5": (
        "<p>When employees transfer to a different role or department, their access needs to "
        "change. They should get access appropriate to their new role and lose access they no "
        "longer need. Without this, people accumulate excessive privileges over time.</p>"
        "<p><strong>Example 1:</strong> Create a transfer checklist that requires the old and "
        "new manager to review and approve access changes. The old manager confirms what "
        "access should be removed; the new manager requests what access is needed. IT "
        "implements both changes simultaneously.</p>"
        "<p><strong>Example 2:</strong> In Azure AD, use <em>Access Packages</em> in Identity "
        "Governance to assign access by role. When someone transfers, remove them from the old "
        "access package and add them to the new one. This automatically adjusts their group "
        "memberships, app assignments, and SharePoint permissions in one action.</p>"
    ),

    "ps-6": (
        "<p>Before granting access to your systems, require every user to read and sign an "
        "access agreement that explains their responsibilities — acceptable use policies, "
        "security rules, and the consequences of violations.</p>"
        "<p><strong>Example 1:</strong> Draft an access agreement that covers acceptable use, "
        "password responsibilities, data handling rules, monitoring consent, and consequences "
        "of misuse. Require every new employee and contractor to sign it before receiving their "
        "account credentials. Re-sign annually.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Entra ID <em>Terms of Use</em> policies "
        "to require users to accept your access agreement every time they log in or at defined "
        "intervals. If they decline, access is blocked. Entra tracks acceptance status so you "
        "have an auditable record of who agreed and when.</p>"
    ),

    "ps-6-1": (
        "<p>For information that requires special protection beyond your standard access "
        "agreement, require an additional, more specific agreement that addresses the unique "
        "handling requirements of that information.</p>"
        "<p><strong>Example 1:</strong> If employees access CUI, have them sign a CUI handling "
        "agreement that specifically addresses marking, storage, transmission, and destruction "
        "requirements. This supplements the general access agreement with CUI-specific "
        "obligations.</p>"
        "<p><strong>Example 2:</strong> For personnel with access to trade secrets or "
        "proprietary technical data, require a supplemental nondisclosure agreement that "
        "specifically names the types of information covered and the legal penalties for "
        "unauthorized disclosure. Track these agreements separately from general access "
        "agreements.</p>"
    ),

    "ps-6-2": (
        "<p>Access to classified information requires specific nondisclosure agreements beyond "
        "standard access agreements. These are typically government-mandated forms with legal "
        "force behind them.</p>"
        "<p><strong>Example 1:</strong> Ensure every person with access to classified "
        "information has a signed SF-312 (Classified Information Nondisclosure Agreement) on "
        "file. The agreement must be signed before access is granted and a copy provided to the "
        "individual. The original goes in their security file.</p>"
        "<p><strong>Example 2:</strong> For compartmented access (SCI, SAP), execute program-"
        "specific nondisclosure agreements in addition to the SF-312. Track each agreement in "
        "your security management database and verify at least annually that all personnel with "
        "classified access have current agreements on file.</p>"
    ),

    "ps-6-3": (
        "<p>Nondisclosure and access agreements should include clauses that extend obligations "
        "beyond employment. When someone leaves, they must understand that their duty to protect "
        "information continues.</p>"
        "<p><strong>Example 1:</strong> Include post-employment nondisclosure clauses in all "
        "access agreements. During exit processing, conduct a debriefing that reminds departing "
        "personnel of their continuing obligations and have them sign a separation statement "
        "acknowledging those obligations.</p>"
        "<p><strong>Example 2:</strong> For personnel leaving positions with access to classified "
        "information, conduct a formal security debriefing using the SF-312 as the reference "
        "document. Remind them that the nondisclosure obligation is permanent and have them "
        "sign the debriefing acknowledgment. File it in their security record.</p>"
    ),

    "ps-7": (
        "<p>When external personnel — contractors, consultants, or partner staff — need access "
        "to your systems, they must meet the same security requirements as your employees. "
        "Their sponsoring organization must agree to your security terms.</p>"
        "<p><strong>Example 1:</strong> Include personnel security requirements in all contracts: "
        "background check requirements, access agreement signing, security training completion, "
        "and termination notification timelines. Require the contractor company to notify you "
        "within 24 hours when one of their employees assigned to your contract is terminated.</p>"
        "<p><strong>Example 2:</strong> In Azure AD, create external contractor accounts as "
        "<em>Guest Users</em> with Conditional Access policies that require MFA and compliant "
        "devices. Assign them to Access Packages with automatic expiration dates aligned to "
        "their contract period. When the contract ends, access expires automatically.</p>"
    ),

    "ps-8": (
        "<p>You must have a formal process for sanctioning (disciplining) employees who violate "
        "security policies. Without consequences, policies are just suggestions.</p>"
        "<p><strong>Example 1:</strong> Define a progressive discipline process for security "
        "violations in your personnel security policy: verbal warning for first minor offense, "
        "written warning for repeat offenses, suspension or access revocation for serious "
        "violations, and termination for egregious or intentional breaches. Document each "
        "action in the employee's file.</p>"
        "<p><strong>Example 2:</strong> Work with HR and legal to ensure security sanctions are "
        "included in your employee handbook and communicated during onboarding. When a violation "
        "occurs, document the incident, the investigation findings, and the sanction applied. "
        "Report trends to leadership quarterly so patterns (e.g., repeated phishing failures "
        "by the same team) can be addressed with targeted training.</p>"
    ),

    "ps-9": (
        "<p>Job descriptions for positions with system access should include the security "
        "responsibilities of the role, the risk designation level, and any screening "
        "requirements. Security is part of the job, not separate from it.</p>"
        "<p><strong>Example 1:</strong> Update all position descriptions to include a section "
        "on security responsibilities. For example, a system administrator's job description "
        "should state they are responsible for patching, log review, account management, and "
        "compliance with the organization's security policies.</p>"
        "<p><strong>Example 2:</strong> In your HRIS, add custom fields to position descriptions "
        "for: risk designation level (low/moderate/high), required clearance level (if any), "
        "security certifications required, and security-specific duties. Use these fields to "
        "automate background check level selection and training assignment during onboarding.</p>"
    ),

    # ── PII Processing & Transparency (PT) ─────────────────────────────

    "pt-1": (
        "<p>You need documented policies and procedures for how your organization handles PII "
        "processing and transparency. These should explain your rules for collecting, using, "
        "storing, sharing, and disposing of personal information.</p>"
        "<p><strong>Example 1:</strong> Write a PII processing policy that covers: legal "
        "authorities for collecting PII, purpose limitations, data minimization requirements, "
        "retention schedules, individual rights (access, correction, deletion), and breach "
        "notification procedures. Review annually.</p>"
        "<p><strong>Example 2:</strong> Create step-by-step procedures for common PII scenarios: "
        "how to respond to a data subject access request, how to process a deletion request, "
        "how to conduct a privacy impact assessment for a new system, and how to report a "
        "potential privacy incident. Store these in your SharePoint governance library.</p>"
    ),

    "pt-2": (
        "<p>Before processing PII, you must have a legitimate legal authority or basis for "
        "doing so. You cannot just collect personal data because it might be useful — you "
        "need a documented reason backed by law, regulation, or consent.</p>"
        "<p><strong>Example 1:</strong> For each system that processes PII, document the legal "
        "authority that permits the collection — whether it is a statute, executive order, "
        "contractual requirement, or individual consent. Record this in your system's Privacy "
        "Impact Assessment (PIA) and reference the specific legal citation.</p>"
        "<p><strong>Example 2:</strong> Create a data processing register (similar to GDPR's "
        "Article 30 record of processing activities) that lists every PII processing activity, "
        "the legal basis for each, the categories of data involved, and the retention period. "
        "Your privacy officer should review and approve new entries before processing begins.</p>"
    ),

    "pt-2-1": (
        "<p>Data tagging means labeling PII with metadata that indicates the legal authority "
        "and purpose for which the data was collected. This makes it possible to automatically "
        "enforce processing rules based on those tags.</p>"
        "<p><strong>Example 1:</strong> In your database schema, add metadata fields that tag "
        "each PII record with its collection purpose (e.g., 'employment,' 'contract "
        "administration,' 'benefits') and legal authority. These tags help ensure the data is "
        "not repurposed beyond its original authorization.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Purview <em>Sensitivity Labels</em> to "
        "tag documents containing PII with their processing authority. Create labels like "
        "'PII - Consent Based' and 'PII - Legal Obligation' and apply them to documents "
        "and emails. Configure DLP policies to enforce different handling rules based on "
        "the label.</p>"
    ),

    "pt-2-2": (
        "<p>This enhancement automates the checking and enforcement of processing authorities, "
        "reducing reliance on people to remember and follow the rules manually.</p>"
        "<p><strong>Example 1:</strong> Configure your database or application to check a "
        "user's authorization against the data's purpose tag before allowing access. If a "
        "user does not have a role authorized for that data's stated purpose, the query is "
        "denied automatically.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Purview, use automated <em>DLP policies</em> "
        "that detect and block unauthorized processing of labeled PII. For instance, if a "
        "document labeled 'PII - HR Only' is attached to an email going outside the HR group, "
        "the DLP policy blocks the send and notifies the sender of the restriction.</p>"
    ),

    "pt-3": (
        "<p>You must clearly define and document the specific purposes for which you process "
        "PII. People should know why you have their data, and you should only use it for "
        "those stated purposes.</p>"
        "<p><strong>Example 1:</strong> In your privacy notices and system documentation, state "
        "each purpose plainly: 'We collect your name and email to fulfill your service request. "
        "We collect your mailing address to ship your order.' Avoid vague purposes like "
        "'business operations' or 'improving our services.'</p>"
        "<p><strong>Example 2:</strong> Build a purpose specification matrix in your data "
        "governance documentation. List each PII element (name, SSN, address, etc.), the "
        "systems that store it, and the specific purpose for each. Review annually with your "
        "privacy officer to ensure purposes are still valid and data is not being used for "
        "unauthorized purposes.</p>"
    ),

    "pt-3-1": (
        "<p>Tag PII with the specific processing purpose so that automated systems can enforce "
        "purpose limitations. This is the data tagging counterpart to documenting purposes in "
        "PT-3.</p>"
        "<p><strong>Example 1:</strong> In your CRM or customer database, add a 'purpose' "
        "field to PII records that records why each piece of data was collected. Use picklist "
        "values like 'contract fulfillment,' 'marketing with consent,' 'legal compliance' to "
        "keep tags consistent.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Purview's <em>Exact Data Match</em> "
        "classifiers to identify specific PII types in your environment and tag them with "
        "sensitivity labels that encode the processing purpose. This enables automated DLP "
        "enforcement based on why the data was collected.</p>"
    ),

    "pt-3-2": (
        "<p>Automate the enforcement of purpose limitations so that PII is not used for "
        "purposes beyond what was originally stated. This reduces the chance of accidental "
        "purpose creep.</p>"
        "<p><strong>Example 1:</strong> Build access control rules in your application that "
        "check the data's purpose tag against the user's authorized purposes before displaying "
        "PII. A marketing team member should not see data collected solely for contract "
        "administration, even if both datasets are in the same system.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Purview, set up <em>DLP policies</em> "
        "and <em>Information Barriers</em> that prevent PII collected for one purpose from "
        "being accessed by teams with a different purpose. For example, prevent the sales team "
        "from accessing HR-collected employee PII through Teams or SharePoint.</p>"
    ),

    "pt-4": (
        "<p>When consent is your legal basis for processing PII, you must obtain it properly — "
        "clearly, voluntarily, and before you start processing. People need to understand what "
        "they are consenting to.</p>"
        "<p><strong>Example 1:</strong> Design consent forms that use plain language and clearly "
        "state what data you are collecting, why, who will have access, how long you will keep "
        "it, and how to withdraw consent. Avoid pre-checked boxes or confusing double negatives. "
        "Store consent records with a timestamp.</p>"
        "<p><strong>Example 2:</strong> For web-based services, implement a consent management "
        "platform (like OneTrust or Cookiebot) that records each user's consent choices, "
        "allows them to update preferences at any time, and provides an audit trail showing "
        "exactly what each person consented to and when.</p>"
    ),

    "pt-4-1": (
        "<p>Tailored consent means adjusting the granularity and presentation of consent "
        "requests based on the sensitivity of the data and the specific processing activity. "
        "Not all consent requests should be the same.</p>"
        "<p><strong>Example 1:</strong> For less sensitive data (like a name for a newsletter "
        "signup), a simple checkbox consent may suffice. For more sensitive data (like health "
        "information or biometrics), present a more detailed consent form that explains the "
        "specific risks and protections in place.</p>"
        "<p><strong>Example 2:</strong> On your website, present layered consent — a brief "
        "summary with an 'I agree' button, plus an expandable section with full details for "
        "those who want them. This respects user time while still providing complete "
        "information for those who want it.</p>"
    ),

    "pt-4-2": (
        "<p>Just-in-time consent means asking for consent at the exact moment it is needed, "
        "rather than bundling all consent requests upfront. This gives people more control and "
        "better understanding of what they are agreeing to.</p>"
        "<p><strong>Example 1:</strong> Instead of asking for permission to access the camera, "
        "microphone, and location all at once during app signup, ask for camera access only "
        "when the user tries to take a photo, location access only when they search for nearby "
        "services, and so on.</p>"
        "<p><strong>Example 2:</strong> On a web application, the first time a user reaches a "
        "feature that requires additional data processing (like analytics on their usage "
        "patterns), present a contextual consent prompt explaining what data will be collected "
        "and why. Store the response and do not ask again unless the terms change.</p>"
    ),

    "pt-4-3": (
        "<p>People must be able to revoke their consent as easily as they gave it. When consent "
        "is revoked, you must stop the processing and, if appropriate, delete the data that "
        "was collected under that consent.</p>"
        "<p><strong>Example 1:</strong> Provide a clear 'Manage Privacy Preferences' page in "
        "your application or website where users can see what they consented to and revoke "
        "any consent with a single click. Process revocation requests within a defined "
        "timeframe (e.g., 72 hours).</p>"
        "<p><strong>Example 2:</strong> Build a workflow in Power Automate that triggers when "
        "a consent revocation is received: it updates the consent database, notifies the data "
        "processing team to stop the relevant processing, initiates data deletion if required, "
        "and sends a confirmation to the individual.</p>"
    ),

    "pt-5": (
        "<p>Before collecting PII, you must provide individuals with a clear notice explaining "
        "what data you collect, why, how it will be used, who it may be shared with, and their "
        "rights. No surprises.</p>"
        "<p><strong>Example 1:</strong> Post a comprehensive privacy notice on your website that "
        "covers: categories of PII collected, purposes of collection, legal authority, whether "
        "disclosure is voluntary or mandatory, third parties who may receive the data, retention "
        "periods, and how to contact your privacy officer.</p>"
        "<p><strong>Example 2:</strong> For federal systems, publish a Privacy Act System of "
        "Records Notice (SORN) in the Federal Register that describes the system, the records "
        "it maintains, and how individuals can request access or amendment. For commercial "
        "organizations, publish equivalent information in your privacy policy.</p>"
    ),

    "pt-5-1": (
        "<p>Just-in-time notices are brief privacy notifications presented at the exact point "
        "of data collection, giving people the information they need right when they need it.</p>"
        "<p><strong>Example 1:</strong> When a user reaches a contact form on your website, "
        "display a brief notice directly on the form: 'We will use your email to respond to "
        "your inquiry. See our Privacy Policy for details.' This is faster to read than "
        "referring them to a full privacy policy they will probably skip.</p>"
        "<p><strong>Example 2:</strong> In a mobile app, before the first feature that collects "
        "location data, show a brief modal: 'This feature uses your location to find nearby "
        "services. We do not sell or share your location data. Tap here for full privacy "
        "details.' The notice appears in context, when it is relevant.</p>"
    ),

    "pt-5-2": (
        "<p>Privacy Act Statements are required whenever a federal agency collects PII from "
        "individuals. The statement must appear on or accompany the form used to collect the "
        "information.</p>"
        "<p><strong>Example 1:</strong> On every form that collects PII from individuals, "
        "include a Privacy Act Statement block that states: the authority to collect (cite the "
        "statute), the purpose, the routine uses, and whether providing the information is "
        "mandatory or voluntary with consequences of not providing it.</p>"
        "<p><strong>Example 2:</strong> For electronic forms, display the Privacy Act Statement "
        "above the submit button where it cannot be missed. In Microsoft Forms or Power Apps, "
        "add a text block containing the complete Privacy Act Statement and a checkbox "
        "confirming the individual has read it. The form cannot be submitted without checking "
        "the box.</p>"
    ),

    "pt-6": (
        "<p>A System of Records Notice (SORN) is a formal notice published in the Federal "
        "Register describing a system that maintains records about individuals from which "
        "information is retrieved by personal identifier. This is a federal agency requirement.</p>"
        "<p><strong>Example 1:</strong> Before deploying a new system that stores PII retrievable "
        "by name or SSN, draft and publish a SORN that describes the system name, categories of "
        "individuals covered, types of records maintained, authority for maintenance, routine "
        "uses, and how individuals can access or contest their records.</p>"
        "<p><strong>Example 2:</strong> Maintain a SORN inventory that lists all published SORNs, "
        "their publication dates, the systems they cover, and the next scheduled review date. "
        "Review each SORN every two years or whenever the system undergoes a significant "
        "change to ensure the notice is still accurate.</p>"
    ),

    "pt-6-1": (
        "<p>Routine uses are the specific purposes, beyond the original purpose of collection, "
        "for which PII in a system of records may be disclosed without the individual's consent. "
        "Each routine use must be published in the SORN.</p>"
        "<p><strong>Example 1:</strong> When drafting a SORN, clearly list every routine use. "
        "For example: 'Records may be disclosed to the Department of Justice for litigation "
        "purposes' or 'Records may be shared with a contractor performing system maintenance "
        "under the terms of the contract.' Each use must be compatible with the original purpose.</p>"
        "<p><strong>Example 2:</strong> Review routine uses annually with your privacy officer "
        "and legal counsel. Remove routine uses that are no longer applicable and add new ones "
        "when legitimate needs arise. Publish amendments in the Federal Register 30 days before "
        "the new routine use takes effect.</p>"
    ),

    "pt-6-2": (
        "<p>Exemption rules allow agencies to exempt certain systems of records from specific "
        "provisions of the Privacy Act. These exemptions must be formally established through "
        "rulemaking and published in the Federal Register.</p>"
        "<p><strong>Example 1:</strong> If your system contains law enforcement investigative "
        "records, you may need to exempt it from the Privacy Act provision requiring disclosure "
        "to the individual (to avoid compromising an investigation). Draft the exemption rule, "
        "publish it for public comment, and finalize it in the Code of Federal Regulations.</p>"
        "<p><strong>Example 2:</strong> Maintain a record of all active exemptions, the systems "
        "they apply to, the legal basis for each exemption, and the date of the final rule. "
        "Review exemptions periodically to ensure they are still necessary and legally "
        "supportable. Document this review in your privacy program records.</p>"
    ),

    "pt-7": (
        "<p>Certain categories of PII — Social Security numbers, health records, financial "
        "data, biometrics — require additional safeguards due to their sensitivity. This "
        "control requires you to identify and apply extra protection to these data types.</p>"
        "<p><strong>Example 1:</strong> Classify PII by sensitivity tier. Tier 1 might be "
        "publicly available information (business email). Tier 2 might be internal PII (home "
        "address, phone number). Tier 3 would be highly sensitive PII (SSN, medical records, "
        "biometrics). Apply progressively stronger controls — encryption, access restrictions, "
        "audit logging — as the tier increases.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Purview, create <em>Sensitive Information "
        "Types</em> for each category and configure DLP policies that apply stricter rules to "
        "higher-sensitivity types. For example, SSNs trigger automatic encryption and block "
        "external sharing, while business email addresses only generate a policy tip.</p>"
    ),

    "pt-7-1": (
        "<p>Social Security numbers (SSNs) require special handling due to the severe "
        "consequences of unauthorized disclosure. Eliminate unnecessary SSN collection and "
        "protect SSNs wherever they must be used.</p>"
        "<p><strong>Example 1:</strong> Audit all forms, databases, and processes that collect "
        "or store SSNs. Eliminate SSN collection wherever an alternative identifier can be "
        "used (employee ID, account number). Where SSNs must be used, mask them so only the "
        "last four digits are displayed and the full number is encrypted at rest.</p>"
        "<p><strong>Example 2:</strong> In Microsoft 365, create a DLP policy using the built-in "
        "<em>U.S. Social Security Number (SSN)</em> sensitive information type. Configure the "
        "policy to block SSNs from being sent in email, uploaded to unapproved cloud storage, "
        "or shared in Teams chats. Alert the privacy officer when violations are detected.</p>"
    ),

    "pt-7-2": (
        "<p>First Amendment information relates to an individual's exercise of rights guaranteed "
        "by the First Amendment — religious beliefs, political activities, freedom of speech "
        "and association. Collecting or maintaining this information requires extreme care.</p>"
        "<p><strong>Example 1:</strong> Prohibit the collection of information about employees' "
        "or customers' religious beliefs, political affiliations, or protest activities unless "
        "there is a specific and documented legal requirement. If such information is "
        "inadvertently collected, establish procedures to delete it promptly.</p>"
        "<p><strong>Example 2:</strong> Train your HR and management staff that First Amendment "
        "activities — union membership, political donations, religious practices — are protected "
        "and must never be used as a factor in employment decisions or security determinations. "
        "Include this in your annual security and privacy awareness training.</p>"
    ),

    "pt-8": (
        "<p>Computer matching involves comparing records from two or more automated systems of "
        "records to find or verify information about individuals. Federal agencies conducting "
        "matching programs must follow specific procedural requirements.</p>"
        "<p><strong>Example 1:</strong> Before starting a computer matching program, execute a "
        "written matching agreement between the participating agencies that specifies the "
        "purpose, records to be matched, accuracy assurances, and protections for individual "
        "rights. Submit the agreement to the Data Integrity Board for approval.</p>"
        "<p><strong>Example 2:</strong> Notify affected individuals and provide due process "
        "before taking adverse action based on matching results. For example, if a match "
        "indicates someone is receiving benefits they should not, provide written notice and "
        "an opportunity to contest the finding before reducing or terminating benefits. Document "
        "the entire process.</p>"
    ),

    # ── Risk Assessment (RA) ───────────────────────────────────────────

    "ra-1": (
        "<p>You need documented risk assessment policies and procedures that describe how your "
        "organization identifies, evaluates, and responds to risks. These are the rules of the "
        "road for all your risk-related activities.</p>"
        "<p><strong>Example 1:</strong> Write a risk assessment policy that defines: when risk "
        "assessments are required (before deploying new systems, annually for existing systems, "
        "after major changes), who performs them, what methodology is used (NIST RMF, FAIR), "
        "and how results are reported to leadership.</p>"
        "<p><strong>Example 2:</strong> Create a risk assessment procedures document with "
        "step-by-step instructions: how to scope the assessment, identify threats and "
        "vulnerabilities, rate likelihood and impact, calculate risk levels, document findings, "
        "and present results. Include templates for risk registers and risk assessment reports.</p>"
    ),

    "ra-2": (
        "<p>Security categorization is the process of determining how much protection a system "
        "needs based on the types of information it processes and the potential impact of a "
        "security breach. This drives all subsequent security decisions.</p>"
        "<p><strong>Example 1:</strong> Use FIPS 199 to categorize each system by evaluating "
        "the potential impact (low, moderate, high) to confidentiality, integrity, and "
        "availability. A payroll system storing SSNs would be moderate or high for "
        "confidentiality. A public website would be low for confidentiality but potentially "
        "moderate for availability.</p>"
        "<p><strong>Example 2:</strong> Document the categorization in each system's security "
        "plan using NIST SP 800-60 as a guide for mapping information types to impact levels. "
        "Review the categorization whenever the system's function, data types, or user base "
        "changes significantly. The categorization determines the baseline set of controls "
        "you must implement.</p>"
    ),

    "ra-2-1": (
        "<p>Impact-level prioritization means that during contingency situations or when "
        "resources are limited, you focus recovery and protection efforts on the highest-"
        "impact systems first.</p>"
        "<p><strong>Example 1:</strong> Create a prioritized system recovery list ranked by "
        "security categorization and mission criticality. During an incident, your team knows "
        "to restore the 'High' impact systems before the 'Moderate' systems. Document this "
        "priority order in your contingency plan and incident response procedures.</p>"
        "<p><strong>Example 2:</strong> In your patch management process, use impact level to "
        "prioritize which systems get patched first. Critical vulnerabilities on high-impact "
        "systems are patched within 24-48 hours; the same vulnerability on a low-impact "
        "system might have a 7-day window. Document these timelines in your vulnerability "
        "management procedure.</p>"
    ),

    "ra-3": (
        "<p>A risk assessment systematically identifies threats and vulnerabilities to your "
        "systems, evaluates the likelihood and impact of exploitation, and determines the "
        "level of risk. This is the core analytical activity of risk management.</p>"
        "<p><strong>Example 1:</strong> Conduct an annual risk assessment for each system using "
        "a structured methodology: identify threats (malware, phishing, insider threat, natural "
        "disaster), identify vulnerabilities (unpatched systems, weak passwords), estimate "
        "likelihood and impact, and calculate a risk score. Document everything in a risk "
        "assessment report.</p>"
        "<p><strong>Example 2:</strong> Use a GRC tool or even a well-structured spreadsheet "
        "to maintain your risk register. For each risk, record the threat source, vulnerability, "
        "existing controls, residual risk level, and planned mitigations. Review the register "
        "with leadership quarterly and update it when vulnerability scans or threat intelligence "
        "reveal new risks.</p>"
    ),

    "ra-3-1": (
        "<p>A supply chain risk assessment evaluates the risks introduced by your vendors, "
        "suppliers, and service providers. Compromised supply chains are one of the most "
        "effective attack vectors adversaries use today.</p>"
        "<p><strong>Example 1:</strong> For each critical vendor, assess the risk they pose: "
        "what data do they access, what systems do they connect to, how strong is their "
        "security posture (request SOC 2 reports, penetration test results), and what would "
        "happen if they were breached? Document these assessments in your vendor risk register.</p>"
        "<p><strong>Example 2:</strong> Before selecting new software or hardware vendors, "
        "include a supply chain risk evaluation in the procurement process. Check CISA's Known "
        "Exploited Vulnerabilities catalog for the vendor's products, review their SBOM "
        "(Software Bill of Materials), and verify they are not on restricted entity lists.</p>"
    ),

    "ra-3-2": (
        "<p>This enhancement leverages all-source intelligence — open-source, commercial, and "
        "government intelligence feeds — to inform your risk assessments with real-world threat "
        "data rather than relying solely on theoretical risk scenarios.</p>"
        "<p><strong>Example 1:</strong> Subscribe to CISA advisories, sector-specific ISACs, "
        "and commercial threat intelligence feeds. Before conducting a risk assessment, review "
        "current threat reports relevant to your industry and technology stack to ensure your "
        "threat scenarios reflect actual adversary behavior.</p>"
        "<p><strong>Example 2:</strong> Integrate threat intelligence into your risk assessment "
        "methodology by mapping known threat actor TTPs (from MITRE ATT&CK) to your systems' "
        "vulnerabilities. This gives you a more realistic picture of which threats are most "
        "likely and helps prioritize your mitigations.</p>"
    ),

    "ra-3-3": (
        "<p>Dynamic threat awareness means continuously updating your understanding of threats "
        "rather than treating risk assessment as a one-time event. Your risk picture should "
        "change as the threat landscape changes.</p>"
        "<p><strong>Example 1:</strong> Configure your SIEM (Microsoft Sentinel, Splunk, etc.) "
        "to automatically ingest threat intelligence feeds and correlate indicators of compromise "
        "against your network data. When new threats emerge, your monitoring automatically "
        "adjusts to detect them without waiting for the next scheduled risk assessment.</p>"
        "<p><strong>Example 2:</strong> Establish a weekly threat briefing where your security "
        "team reviews the latest CISA alerts, vendor advisories, and dark web intelligence "
        "reports. Update your risk register and adjust your defensive priorities based on "
        "emerging threats that are relevant to your environment.</p>"
    ),

    "ra-3-4": (
        "<p>Predictive cyber analytics uses data analytics and modeling to anticipate future "
        "threats and vulnerabilities before they are exploited. This is a proactive approach "
        "to risk rather than a reactive one.</p>"
        "<p><strong>Example 1:</strong> Use your SIEM's machine learning capabilities to "
        "identify anomalous patterns that may indicate an emerging attack. Microsoft Sentinel "
        "and Splunk both offer User and Entity Behavior Analytics (UEBA) that baseline normal "
        "activity and flag deviations that could predict an attack in progress.</p>"
        "<p><strong>Example 2:</strong> Analyze your vulnerability scan trend data to predict "
        "which systems are most likely to have critical vulnerabilities in the future. Systems "
        "that consistently show late patching or recurring misconfigurations should receive "
        "extra monitoring and faster remediation timelines.</p>"
    ),

    "ra-4": (
        "<p>Risk assessments are not one-and-done. You must update them regularly and whenever "
        "significant changes occur — new systems, new threats, organizational changes, or "
        "after a security incident.</p>"
        "<p><strong>Example 1:</strong> Schedule risk assessment updates annually at minimum and "
        "trigger ad-hoc updates after: deployment of new systems, major infrastructure changes, "
        "significant security incidents, or when new threat intelligence reveals risks you "
        "had not previously considered. Document the trigger and the update in your risk "
        "register.</p>"
        "<p><strong>Example 2:</strong> After every vulnerability scan cycle (monthly or "
        "quarterly), review the findings against your current risk register. If new critical "
        "vulnerabilities appear, update the affected system's risk assessment and adjust the "
        "POA&M accordingly. Use Microsoft Defender Vulnerability Management to track these "
        "changes over time.</p>"
    ),

    "ra-5": (
        "<p>Vulnerability scanning is one of the most fundamental security activities. You must "
        "regularly scan your systems for known vulnerabilities, analyze the results, and fix "
        "what you find. This is not optional.</p>"
        "<p><strong>Example 1:</strong> Deploy a vulnerability scanner (Tenable Nessus, Qualys, "
        "Rapid7 InsightVM) and scan all systems at least monthly. Configure credentialed scans "
        "for deeper visibility. After each scan, triage the findings by severity: critical and "
        "high vulnerabilities get patched within 14 days, moderate within 30, and low within 90.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Defender for Endpoint, use the <em>Threat "
        "and Vulnerability Management</em> dashboard to see real-time vulnerability data across "
        "all enrolled endpoints. The dashboard prioritizes vulnerabilities based on actual "
        "exploit availability and your exposure. Export the recommendations and feed them into "
        "your POA&M and patch management process.</p>"
    ),

    "ra-5-1": (
        "<p>Your vulnerability scanning tools must be kept up to date with the latest "
        "vulnerability checks, plugins, and signatures. An outdated scanner misses new "
        "vulnerabilities.</p>"
        "<p><strong>Example 1:</strong> Configure your vulnerability scanner (Nessus, Qualys) "
        "to automatically update its plugin feed daily. Verify updates are applying by checking "
        "the plugin version date before each scan. If updates fail, investigate and resolve "
        "before scanning — a scan with outdated plugins gives false confidence.</p>"
        "<p><strong>Example 2:</strong> Microsoft Defender for Endpoint automatically updates "
        "its vulnerability database through cloud connectivity. Verify that your endpoints are "
        "checking in to the service regularly by reviewing the <em>Device Health</em> reports "
        "in the Defender portal. Devices that have not checked in for 7+ days need attention.</p>"
    ),

    "ra-5-2": (
        "<p>The list of vulnerabilities you scan for must be updated to include newly discovered "
        "vulnerabilities. This means subscribing to CVE feeds and updating your scan profiles "
        "accordingly.</p>"
        "<p><strong>Example 1:</strong> Monitor the NIST National Vulnerability Database (NVD) "
        "and CISA's Known Exploited Vulnerabilities (KEV) catalog. When new vulnerabilities are "
        "added to the KEV catalog, verify that your scanner includes checks for them and run "
        "a targeted scan within 48 hours.</p>"
        "<p><strong>Example 2:</strong> Subscribe to vendor security advisory mailing lists "
        "(Microsoft Security Response Center, Cisco PSIRT, etc.) for all software in your "
        "environment. When a new advisory drops, verify your scanner has the corresponding "
        "check and update your scan configuration if needed.</p>"
    ),

    "ra-5-3": (
        "<p>Your vulnerability scanning must cover the full breadth of your environment (all "
        "systems) and provide sufficient depth (credentialed, thorough scans, not just surface-"
        "level port scans).</p>"
        "<p><strong>Example 1:</strong> Maintain a scan coverage matrix that shows every IP "
        "range, VLAN, and cloud subscription in your environment mapped to the scanner that "
        "covers it. Identify any gaps — if you have a new cloud subscription or office network "
        "that is not being scanned, add it immediately.</p>"
        "<p><strong>Example 2:</strong> Run both unauthenticated and authenticated (credentialed) "
        "scans. Unauthenticated scans show what an attacker would see from the network. "
        "Authenticated scans log into systems and identify missing patches, misconfigurations, "
        "and software vulnerabilities that external scans cannot see. Compare the two to "
        "validate coverage.</p>"
    ),

    "ra-5-4": (
        "<p>Discoverable information refers to data about your organization that is publicly "
        "available and could help an attacker plan an attack — exposed services, leaked "
        "credentials, organizational details, and technical information.</p>"
        "<p><strong>Example 1:</strong> Conduct an Open Source Intelligence (OSINT) assessment "
        "of your organization. Search for employee email addresses on breach databases (Have I "
        "Been Pwned), look for exposed services on Shodan or Censys, and review your DNS "
        "records for information leakage. Feed the findings into your risk assessment.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Defender External Attack Surface "
        "Management (EASM) to continuously discover and monitor your internet-facing assets. "
        "The tool identifies exposed services, expired certificates, and vulnerable components "
        "that an attacker could find. Review the dashboard weekly and remediate findings.</p>"
    ),

    "ra-5-5": (
        "<p>Some vulnerability scans require privileged (administrator-level) access to "
        "properly assess the system. Running credentialed scans provides significantly more "
        "accurate and complete results.</p>"
        "<p><strong>Example 1:</strong> Create dedicated service accounts for vulnerability "
        "scanning with local administrator privileges on target systems. Use a unique account "
        "per scan zone, store credentials in a vault (CyberArk, Azure Key Vault), and rotate "
        "passwords after each scan cycle.</p>"
        "<p><strong>Example 2:</strong> In your Tenable or Qualys configuration, set up scan "
        "credentials using domain service accounts with appropriate privileges. Verify "
        "credentialed scan success by checking the authentication status in scan results — "
        "if a system shows 'authentication failure,' the scan results for that system are "
        "incomplete and should not be trusted.</p>"
    ),

    "ra-5-6": (
        "<p>Automated trend analysis tracks your vulnerability data over time to identify "
        "patterns — are things getting better or worse? Which systems are chronically "
        "vulnerable? Which vulnerabilities keep coming back after remediation?</p>"
        "<p><strong>Example 1:</strong> Configure your vulnerability scanner to generate trend "
        "reports showing: total vulnerabilities by severity over the last 12 months, average "
        "time to remediate by severity, and systems with the most recurring findings. Present "
        "these trends to leadership monthly to demonstrate improvement or highlight areas "
        "needing attention.</p>"
        "<p><strong>Example 2:</strong> Export your scan data into Power BI and build dashboards "
        "that show vulnerability trends by system, team, severity, and age. Use the data to "
        "identify systemic issues — if one department always has the most critical findings, "
        "investigate whether they need more resources, training, or better patching processes.</p>"
    ),

    "ra-5-7": (
        "<p>This enhancement uses automated tools to detect unauthorized hardware, software, "
        "or services on your network and alert you immediately. Rogue devices and unapproved "
        "software are common attack vectors.</p>"
        "<p><strong>Example 1:</strong> Deploy a Network Access Control (NAC) solution like "
        "Cisco ISE or Forescout that automatically detects devices connecting to your network "
        "and quarantines any device not in your approved inventory. Alert your security team "
        "when an unauthorized device is detected.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Defender for Endpoint, enable <em>Device "
        "Discovery</em> to find unmanaged devices on your network. Configure alerts for new "
        "devices that appear and are not enrolled in management. Use Intune's compliance "
        "policies to block non-compliant devices from accessing corporate resources.</p>"
    ),

    "ra-5-8": (
        "<p>Reviewing historical audit logs as part of your vulnerability assessment helps "
        "you understand whether a vulnerability was exploited before it was discovered. "
        "The vulnerability might be patched now, but the damage may already be done.</p>"
        "<p><strong>Example 1:</strong> When a critical vulnerability is discovered on a system, "
        "review audit logs from the period between when the vulnerability was introduced "
        "(e.g., when the vulnerable software was installed) and when it was patched. Look for "
        "indicators of exploitation — unusual access patterns, unexpected processes, data "
        "exfiltration signs.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Sentinel, use the <em>Hunting</em> feature "
        "to search historical logs for indicators associated with newly discovered CVEs. "
        "Microsoft often publishes hunting queries for major vulnerabilities that you can run "
        "against your retained log data to determine if you were affected.</p>"
    ),

    "ra-5-9": (
        "<p>Penetration testing goes beyond automated vulnerability scanning by having skilled "
        "testers actively attempt to exploit your systems, simulating real-world attack "
        "techniques to find weaknesses that scanners miss.</p>"
        "<p><strong>Example 1:</strong> Engage an independent penetration testing firm at "
        "least annually to test your external-facing systems and internal network. The scope "
        "should include network penetration testing, web application testing, and social "
        "engineering (phishing). Require a detailed report with findings, evidence, and "
        "remediation recommendations.</p>"
        "<p><strong>Example 2:</strong> For continuous validation, deploy a breach and attack "
        "simulation (BAS) tool like AttackIQ, SafeBreach, or Microsoft's built-in <em>Attack "
        "Simulation Training</em>. These tools automatically run simulated attack techniques "
        "against your defenses and report which attacks succeed, giving you ongoing insight "
        "into gaps between assessments.</p>"
    ),

    "ra-5-10": (
        "<p>Correlating scan results from different scanners and data sources gives you a more "
        "complete picture of your vulnerabilities. One scanner might find something another "
        "misses, and combining data helps prioritize remediation.</p>"
        "<p><strong>Example 1:</strong> Feed vulnerability scan results from multiple tools "
        "(Nessus, Qualys, Defender) into a single platform for correlation. Compare findings "
        "to eliminate duplicates, identify discrepancies between scanners, and build a unified "
        "view of your vulnerability posture.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Sentinel, create a workbook that ingests "
        "data from your vulnerability scanner, endpoint detection tool, and cloud security "
        "posture management. Correlate a system's vulnerability data with its exposure "
        "(internet-facing? high-privilege users?) and active threat detections to prioritize "
        "remediation on the systems with the highest combined risk.</p>"
    ),

    "ra-5-11": (
        "<p>A public disclosure program (like a bug bounty or vulnerability disclosure policy) "
        "gives outside security researchers a way to report vulnerabilities they find in your "
        "systems. This turns the wider security community into an extension of your team.</p>"
        "<p><strong>Example 1:</strong> Publish a Vulnerability Disclosure Policy (VDP) on "
        "your website at /.well-known/security.txt following the ISO 29147 standard. State "
        "what systems are in scope, how to report findings securely, and commit to no legal "
        "action against good-faith reporters.</p>"
        "<p><strong>Example 2:</strong> If your organization is mature enough, launch a bug "
        "bounty program through a platform like HackerOne or Bugcrowd. Define clear scope, "
        "severity-based payouts, and response SLAs. Even a modest program (starting at $100 "
        "per valid finding) can surface vulnerabilities your internal team missed.</p>"
    ),

    "ra-6": (
        "<p>Technical Surveillance Countermeasures (TSCM) surveys detect unauthorized "
        "electronic surveillance devices — bugs, hidden cameras, rogue wireless access "
        "points — in sensitive areas. This applies primarily to facilities handling "
        "classified information.</p>"
        "<p><strong>Example 1:</strong> For spaces where classified or sensitive discussions "
        "occur, schedule periodic TSCM sweeps using qualified personnel with spectrum "
        "analyzers, non-linear junction detectors, and physical inspection capabilities. "
        "Document each sweep with date, location, equipment used, and findings.</p>"
        "<p><strong>Example 2:</strong> Implement continuous RF monitoring in your most "
        "sensitive spaces using commercial TSCM monitoring systems that alert when unexpected "
        "radio frequency emissions are detected. Supplement electronic monitoring with "
        "physical security measures like access control and visual inspections of the space "
        "before sensitive meetings.</p>"
    ),

    "ra-7": (
        "<p>Risk response is what you actually do about the risks you identify. For each risk, "
        "you must choose a response: accept it, mitigate it, transfer it (insurance), share "
        "it, or avoid it — and document the decision.</p>"
        "<p><strong>Example 1:</strong> For each risk in your risk register, document the chosen "
        "response and the rationale. 'We will mitigate the risk of unpatched servers by "
        "implementing automated patch management within 30 days. We will accept the residual "
        "risk of the 48-hour patching window because the cost of zero-downtime patching "
        "exceeds the risk exposure.'</p>"
        "<p><strong>Example 2:</strong> For risks you transfer, document the mechanism. 'We "
        "transfer the financial risk of a data breach through our cyber insurance policy "
        "(Policy #12345, $2M coverage). We transfer the operational risk of 24/7 monitoring "
        "to our MSSP under contract C-2024-001 with defined SLAs.' Track these transfer "
        "mechanisms in your risk register alongside the risks they address.</p>"
    ),

    "ra-8": (
        "<p>A Privacy Impact Assessment (PIA) evaluates how a system or project collects, "
        "uses, stores, and shares PII, and whether those practices are compliant with privacy "
        "requirements. PIAs are required before deploying systems that handle PII.</p>"
        "<p><strong>Example 1:</strong> Before deploying a new HR system or customer database "
        "that will store PII, complete a PIA. Document what PII is collected, the legal "
        "authority, purpose, access controls, retention periods, and data sharing arrangements. "
        "Have your privacy officer review and approve the PIA before the system goes live.</p>"
        "<p><strong>Example 2:</strong> Create a PIA template in Word or SharePoint with "
        "standard sections: system description, data elements collected, legal authority, "
        "purpose specification, data sharing, security controls, individual access rights, "
        "and privacy risks with mitigations. Publish completed PIAs on your website or "
        "intranet as required by policy.</p>"
    ),

    "ra-9": (
        "<p>Criticality analysis identifies which systems and components are most critical to "
        "your mission. This determines where to focus your strongest protections and fastest "
        "recovery capabilities.</p>"
        "<p><strong>Example 1:</strong> Rank your systems by mission criticality: Tier 1 "
        "(mission-critical — failure stops operations), Tier 2 (mission-important — failure "
        "degrades operations), Tier 3 (business support — failure is inconvenient). Use this "
        "ranking to prioritize patching, monitoring, backup frequency, and incident response.</p>"
        "<p><strong>Example 2:</strong> Conduct a dependency analysis that maps which systems "
        "depend on which infrastructure components. If your Active Directory goes down, what "
        "else breaks? If your VPN concentrator fails, who cannot work? Document these "
        "dependencies so your contingency planning addresses the right priorities.</p>"
    ),

    "ra-10": (
        "<p>Threat hunting is the proactive search for adversaries already inside your network "
        "who have evaded your automated defenses. Instead of waiting for alerts, hunters "
        "actively look for signs of compromise.</p>"
        "<p><strong>Example 1:</strong> Schedule monthly threat hunting exercises where your "
        "security team develops hypotheses based on recent threat intelligence (e.g., 'APT "
        "group X uses PowerShell for lateral movement — let us look for unusual PowerShell "
        "activity on our servers') and searches your log data for evidence.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Sentinel, use the <em>Hunting</em> "
        "workspace and built-in hunting queries aligned to MITRE ATT&CK techniques. Run "
        "queries for living-off-the-land techniques, unusual authentication patterns, and "
        "data staging. Document each hunt with the hypothesis, data sources searched, "
        "findings, and recommended actions.</p>"
    ),

    # ── System and Services Acquisition (SA) ───────────────────────────

    "sa-1": (
        "<p>You need documented policies and procedures for how your organization acquires "
        "systems and services with security built into the process. Buying or building systems "
        "without security requirements leads to expensive retrofits later.</p>"
        "<p><strong>Example 1:</strong> Write an acquisition security policy that requires "
        "security requirements to be included in all RFPs, contracts, and service agreements. "
        "Define minimum security standards vendors must meet (encryption, access controls, "
        "audit logging) and include them as evaluation criteria in procurement decisions.</p>"
        "<p><strong>Example 2:</strong> Create procurement procedures that include a security "
        "review checkpoint. Before any IT purchase over a defined threshold, the CISO or "
        "security team must review the vendor's security posture, the product's security "
        "features, and the data it will handle. No purchase order without a signed security "
        "review form.</p>"
    ),

    "sa-2": (
        "<p>When planning new systems or services, you must allocate specific resources — "
        "budget, staff, time — for information security. Security cannot be unfunded and then "
        "expected to happen.</p>"
        "<p><strong>Example 1:</strong> In your project planning process, require a security "
        "budget line item for every IT project. This includes costs for security testing, "
        "secure configuration, monitoring tools, and ongoing maintenance. If the project plan "
        "has no security budget, it does not get approved.</p>"
        "<p><strong>Example 2:</strong> During capital planning, include security resource "
        "requirements for each system in your portfolio: FTE hours for security management, "
        "license costs for monitoring and scanning tools, and budget for annual assessments "
        "and penetration tests. Track these allocations in your investment portfolio alongside "
        "the system's operational costs.</p>"
    ),

    "sa-3": (
        "<p>Your System Development Life Cycle (SDLC) must include security at every phase — "
        "from requirements through design, development, testing, deployment, and retirement. "
        "Security bolted on at the end is always more expensive and less effective.</p>"
        "<p><strong>Example 1:</strong> Define security activities for each SDLC phase: "
        "requirements (identify security requirements and data sensitivity), design (threat "
        "modeling, security architecture review), development (secure coding standards), testing "
        "(security testing, code review), deployment (hardening, configuration verification), "
        "and retirement (data sanitization, decommissioning).</p>"
        "<p><strong>Example 2:</strong> If you use Azure DevOps or GitHub for development, "
        "integrate security into your CI/CD pipeline. Add SAST (static analysis) tools like "
        "SonarQube or GitHub Advanced Security to scan code on every pull request. Add DAST "
        "(dynamic analysis) scans before deployment to staging. Gate production deployments on "
        "zero critical security findings.</p>"
    ),

    "sa-3-1": (
        "<p>Manage your preproduction (development, test, staging) environments with appropriate "
        "security controls. These environments are often targets because they have weaker "
        "protections but may contain real data or provide a path to production.</p>"
        "<p><strong>Example 1:</strong> Apply security controls to development and test "
        "environments that are proportional to the data they contain. At minimum: access "
        "control, network segmentation from production, and regular patching. Never use "
        "production credentials in preproduction environments.</p>"
        "<p><strong>Example 2:</strong> In Azure, create separate subscriptions for dev, test, "
        "and production with Azure Policy enforcement on each. Use Azure Blueprints to ensure "
        "consistent security baselines across all environments. Lock production access so "
        "developers cannot directly access production systems from their development tools.</p>"
    ),

    "sa-3-2": (
        "<p>Using live or operational data in development and test environments creates risk. "
        "If test environments are breached, real customer or employee data is exposed. Use "
        "synthetic data whenever possible.</p>"
        "<p><strong>Example 1:</strong> Establish a policy that prohibits using production data "
        "in non-production environments without approval and data masking. When testing requires "
        "realistic data, use tools like Redgate Data Masker or Faker to generate synthetic "
        "data that matches production structure without containing real PII.</p>"
        "<p><strong>Example 2:</strong> In Azure SQL, use <em>Dynamic Data Masking</em> on "
        "any production data copied to test environments. Configure masking rules that replace "
        "names, SSNs, emails, and financial data with randomized equivalents. This lets "
        "developers test with realistic data structures without exposing real information.</p>"
    ),

    "sa-3-3": (
        "<p>Technology refresh means planning for and executing the replacement of aging "
        "systems and components before they become unsupported, insecure, or unable to meet "
        "mission requirements.</p>"
        "<p><strong>Example 1:</strong> Maintain a technology lifecycle inventory that tracks "
        "each major system and component, its vendor support end date, and your planned "
        "replacement date. For example, if Windows Server 2016 reaches end of support in "
        "January 2027, your refresh plan should have replacement underway by mid-2026.</p>"
        "<p><strong>Example 2:</strong> Tie technology refresh to your budget cycle. Each year, "
        "identify systems approaching end-of-life in the next 18 months and include replacement "
        "costs in the next budget request. Track refresh progress in your POA&M so aging "
        "technology does not become a recurring audit finding.</p>"
    ),

    "sa-4": (
        "<p>When acquiring systems or services, include specific security requirements in your "
        "contracts and procurement documents. Vendors should know exactly what security "
        "standards they need to meet before they bid on the work.</p>"
        "<p><strong>Example 1:</strong> Include security requirements in every RFP and contract "
        "for IT services: FIPS 140-2 validated encryption, NIST 800-53 control compliance, "
        "incident notification within 24 hours, annual third-party security assessments, and "
        "right-to-audit clauses. Evaluate vendor proposals against these requirements.</p>"
        "<p><strong>Example 2:</strong> For cloud services, require vendors to provide SOC 2 "
        "Type II reports, FedRAMP authorization status (if applicable), and documentation of "
        "their shared responsibility model. Include DFARS 252.204-7012 clause in contracts "
        "involving CUI to flow down cybersecurity requirements to your suppliers.</p>"
    ),

    "sa-4-1": (
        "<p>Require vendors to describe the functional properties of the security controls "
        "implemented in their products or services. You need to know what the controls do "
        "in plain terms, not just that they exist.</p>"
        "<p><strong>Example 1:</strong> In your procurement requirements, ask vendors to "
        "describe how their access controls work: 'The system supports role-based access "
        "control with configurable roles, requires MFA for privileged access, and logs all "
        "authentication events with timestamps and source IP.' This is more useful than "
        "'the system implements access control.'</p>"
        "<p><strong>Example 2:</strong> When evaluating a SaaS product, request the vendor's "
        "security whitepaper or architecture documentation that explains their encryption "
        "methods (AES-256 at rest, TLS 1.3 in transit), authentication options (SAML, OIDC, "
        "SCIM provisioning), and audit logging capabilities in functional terms.</p>"
    ),

    "sa-4-2": (
        "<p>Go beyond functional descriptions — require vendors to provide design and "
        "implementation details for their security controls. You need to know how controls "
        "are built, not just what they claim to do.</p>"
        "<p><strong>Example 1:</strong> Request vendors provide architecture diagrams showing "
        "how security controls are implemented: where encryption is applied in the data flow, "
        "how authentication tokens are managed, where audit logs are stored, and how network "
        "segmentation is achieved. Review these against your security requirements.</p>"
        "<p><strong>Example 2:</strong> For critical acquisitions, include contract language "
        "requiring the vendor to provide design documentation sufficient for independent "
        "security assessment. This might include API security specifications, key management "
        "procedures, and vulnerability management processes — enough detail to verify their "
        "claims are backed by solid engineering.</p>"
    ),

    "sa-4-3": (
        "<p>Require vendors to use recognized secure development methods, techniques, and "
        "practices when building the products and services you acquire. How they build is as "
        "important as what they build.</p>"
        "<p><strong>Example 1:</strong> In your RFPs, require vendors to describe their SDLC "
        "security practices: do they use secure coding standards (OWASP, CERT), perform code "
        "reviews, conduct static and dynamic analysis, and do penetration testing before "
        "releases? Vendors who cannot articulate their development security practices are a "
        "higher risk.</p>"
        "<p><strong>Example 2:</strong> Require vendors to attest to compliance with frameworks "
        "like NIST SSDF (Secure Software Development Framework) or demonstrate adherence to "
        "OWASP SAMM (Software Assurance Maturity Model). Ask for evidence: SAST/DAST scan "
        "reports, code review records, or third-party audit results.</p>"
    ),

    "sa-4-4": (
        "<p>When integrating components from different vendors into a single system, document "
        "which components belong to which systems and ensure that security boundaries are "
        "clear between them.</p>"
        "<p><strong>Example 1:</strong> Maintain a system component inventory that maps each "
        "hardware and software component to the system it belongs to. Document the security "
        "boundary — where one system's responsibility ends and another begins — especially "
        "at integration points where data flows between systems.</p>"
        "<p><strong>Example 2:</strong> In your network diagrams, clearly label which components "
        "are part of which system's authorization boundary. When a shared component (like a "
        "database server) serves multiple systems, document the shared responsibility and "
        "ensure both system owners agree on who is responsible for its security.</p>"
    ),

    "sa-4-5": (
        "<p>Require vendors to deliver systems and components in a secure configuration, not "
        "with default settings that need to be hardened after deployment. Secure by default "
        "saves time and reduces risk.</p>"
        "<p><strong>Example 1:</strong> Include language in contracts requiring vendors to "
        "deliver systems configured to DISA STIG, CIS Benchmark, or your organization's "
        "hardening standard. Systems should arrive with unnecessary services disabled, default "
        "passwords changed, and security features enabled — not in a factory-default state.</p>"
        "<p><strong>Example 2:</strong> When procuring cloud services, require the vendor to "
        "document their default security configuration and any tenant-configurable security "
        "settings. Compare their defaults against your security baseline and identify settings "
        "you need to change. In M365, use the <em>Secure Score</em> recommendations as a "
        "checklist for proper tenant configuration.</p>"
    ),

    "sa-4-6": (
        "<p>When acquiring information assurance products (encryption modules, firewalls, "
        "intrusion detection systems), use products that have been evaluated and validated "
        "by recognized testing programs.</p>"
        "<p><strong>Example 1:</strong> For encryption products, require FIPS 140-2 or FIPS "
        "140-3 validation. Check the NIST Cryptographic Module Validation Program (CMVP) list "
        "to verify the vendor's certification is current. Include the FIPS validation "
        "certificate number in your procurement documentation.</p>"
        "<p><strong>Example 2:</strong> For network security products (firewalls, IDS/IPS), "
        "check whether they appear on the DoDIN APL (Department of Defense Information Network "
        "Approved Products List). Products on the APL have been tested for interoperability "
        "and security. Include APL compliance as a procurement requirement for defense "
        "contracts.</p>"
    ),

    "sa-4-7": (
        "<p>NIAP (National Information Assurance Partnership) Protection Profiles define "
        "security requirements for specific product categories. Using NIAP-evaluated products "
        "ensures they meet a recognized security standard.</p>"
        "<p><strong>Example 1:</strong> When procuring security products for a DoD environment, "
        "check the NIAP Product Compliant List at niap-ccevs.org. Only products with current "
        "NIAP evaluations against the relevant Protection Profile should be considered. Include "
        "NIAP evaluation as a mandatory requirement in your procurement specifications.</p>"
        "<p><strong>Example 2:</strong> For mobile device management, require products evaluated "
        "against the NIAP MDM Protection Profile. For firewalls, require the Network Device "
        "or Stateful Traffic Filter Firewall Protection Profile. Document which Protection "
        "Profile applies to each product category in your acquisition procedures.</p>"
    ),

    "sa-4-8": (
        "<p>Require vendors to provide a continuous monitoring plan that describes how they "
        "will monitor the effectiveness of security controls in their products or services "
        "after deployment.</p>"
        "<p><strong>Example 1:</strong> In service contracts, require the vendor to define "
        "how they will continuously monitor their security controls: regular vulnerability "
        "scans, configuration audits, log analysis, and periodic security assessments. The "
        "plan should specify what is monitored, how frequently, and how findings are reported "
        "to you.</p>"
        "<p><strong>Example 2:</strong> For cloud service providers, require them to provide "
        "ongoing access to their compliance documentation (SOC 2 reports updated annually, "
        "FedRAMP continuous monitoring monthly reports) and a defined process for notifying "
        "you of security incidents, new vulnerabilities, or changes in their control "
        "environment.</p>"
    ),

    "sa-4-9": (
        "<p>Require vendors to document all functions, ports, protocols, and services that "
        "their products use. You cannot secure what you do not understand, and undocumented "
        "network behavior is a risk.</p>"
        "<p><strong>Example 1:</strong> Before deploying a new product, require the vendor to "
        "provide a complete list of network ports and protocols it requires (e.g., TCP 443 "
        "for HTTPS management, UDP 514 for syslog, TCP 8443 for API). Map these against your "
        "firewall rules and deny any traffic not explicitly documented and approved.</p>"
        "<p><strong>Example 2:</strong> In your procurement checklist, include a requirement "
        "for vendors to provide a 'ports and protocols' matrix. After deployment, validate "
        "using network monitoring tools (Wireshark, NetFlow analyzers) that the product is "
        "only communicating on the documented ports. Any undocumented communication should "
        "be investigated and reported to the vendor.</p>"
    ),

    "sa-4-10": (
        "<p>For systems requiring Personal Identity Verification (PIV), only use products "
        "that are on the GSA FIPS 201 Approved Products List. This ensures the products "
        "properly implement the PIV standard.</p>"
        "<p><strong>Example 1:</strong> When procuring smart card readers, card management "
        "systems, or physical access control systems for PIV use, verify the product is listed "
        "on the GSA FIPS 201 Approved Products List at idmanagement.gov before purchasing. "
        "Include APL listing as a mandatory procurement requirement.</p>"
        "<p><strong>Example 2:</strong> For logical access control, verify that your PKI "
        "certificates and authentication infrastructure support PIV credentials. In Windows "
        "environments, configure Group Policy for smart card authentication and test PIV "
        "card login against your Active Directory Certificate Services infrastructure.</p>"
    ),

    "sa-4-11": (
        "<p>When acquiring systems that will maintain records about individuals, require the "
        "vendor to support compliance with Privacy Act requirements, including the ability "
        "to produce records for individual access requests.</p>"
        "<p><strong>Example 1:</strong> In contracts for systems that store PII, include "
        "requirements for the vendor to support Privacy Act compliance: the ability to search "
        "records by personal identifier, export records in a readable format, and apply "
        "retention and disposition schedules. Verify these capabilities during acceptance "
        "testing.</p>"
        "<p><strong>Example 2:</strong> Require vendor systems to support data subject access "
        "requests — the ability to find, export, and delete an individual's records on demand. "
        "Test this capability during procurement evaluation by providing test scenarios: 'Show "
        "me all records for individual X' and 'Delete all records for individual Y.'</p>"
    ),

    "sa-4-12": (
        "<p>Your contracts must clearly establish that your organization retains ownership of "
        "its data, even when it is processed or stored by a vendor. Data ownership should "
        "never be ambiguous.</p>"
        "<p><strong>Example 1:</strong> Include explicit data ownership clauses in all vendor "
        "contracts: 'All data provided by the Customer, and all data generated from Customer "
        "data, remains the exclusive property of the Customer. The Vendor shall not use Customer "
        "data for any purpose other than providing the contracted services.'</p>"
        "<p><strong>Example 2:</strong> Require contracts to include data portability and "
        "return provisions: upon contract termination, the vendor must return all your data in "
        "a standard format within 30 days and certify deletion from their systems within 90 "
        "days. Test data export capabilities before signing the contract to ensure they work.</p>"
    ),

    "sa-5": (
        "<p>Require adequate documentation for all systems — administrator guides, user guides, "
        "and security configuration documentation. Without proper documentation, systems cannot "
        "be securely operated or maintained.</p>"
        "<p><strong>Example 1:</strong> In your procurement requirements, specify that vendors "
        "must deliver administrator documentation covering: installation procedures, security "
        "configuration settings, backup and recovery procedures, account management, log "
        "management, and patch/update procedures. The documentation must be current and "
        "versioned.</p>"
        "<p><strong>Example 2:</strong> Create a documentation requirements checklist for "
        "system acceptance: security architecture documentation, network diagrams, data flow "
        "diagrams, user guides, admin guides, and a security configuration guide based on "
        "DISA STIGs or CIS Benchmarks. The system is not accepted into operations until all "
        "documentation is delivered and reviewed.</p>"
    ),

    "sa-5-1": (
        "<p>System documentation must describe the functional properties of security controls — "
        "what each control does in terms the administrator can understand and verify.</p>"
        "<p><strong>Example 1:</strong> The system documentation should explain each security "
        "feature in functional terms: 'The system enforces password complexity by requiring a "
        "minimum of 14 characters, at least one uppercase, one lowercase, one number, and one "
        "special character. Failed login lockout occurs after 3 consecutive failures for 15 "
        "minutes.'</p>"
        "<p><strong>Example 2:</strong> For each security control documented, the administrator "
        "guide should include: what it does, how to configure it, how to verify it is working, "
        "and what happens when it fails. This enables your admins to properly operate and "
        "troubleshoot security features.</p>"
    ),

    "sa-5-2": (
        "<p>Documentation must describe how the system interfaces with external systems from "
        "a security perspective — what data flows across the boundary, what protocols are "
        "used, and what security measures protect those interfaces.</p>"
        "<p><strong>Example 1:</strong> Create interface documentation for each external system "
        "connection: the remote system name, data exchanged, protocol and port, authentication "
        "method, encryption used, and the security agreement (ISA/MOU) governing the "
        "connection. Include this in your system security plan.</p>"
        "<p><strong>Example 2:</strong> In your network diagrams, label every external interface "
        "with its security properties. A connection to a cloud API should show: HTTPS/TLS 1.3, "
        "OAuth 2.0 authentication, data classification of traffic, and bandwidth/rate "
        "limiting. This makes it easy to audit and assess interface security.</p>"
    ),

    "sa-5-3": (
        "<p>High-level design documentation describes the system's overall security architecture "
        "in terms of major components, their relationships, and how security is implemented "
        "across them.</p>"
        "<p><strong>Example 1:</strong> Require a high-level design document that shows the "
        "system's security architecture: where encryption is applied, where access control "
        "is enforced, where audit logging occurs, and how components are segmented. This "
        "document should be understandable by a security reviewer who is not a developer.</p>"
        "<p><strong>Example 2:</strong> Use architecture diagrams (draw.io, Visio, Lucidchart) "
        "to document the security boundary, trust zones, and data flows. Label each zone with "
        "its security level and the controls that protect the boundary between zones. Store "
        "these diagrams alongside the system security plan.</p>"
    ),

    "sa-5-4": (
        "<p>Low-level design documentation provides detailed technical descriptions of how "
        "individual security mechanisms are implemented — enough detail for a developer or "
        "security tester to understand exactly how they work.</p>"
        "<p><strong>Example 1:</strong> The low-level design document should describe how "
        "specific security functions are implemented: the exact encryption algorithm and key "
        "length, the password hashing function and salt handling, the session management "
        "approach (token format, expiration, revocation), and the audit log record format.</p>"
        "<p><strong>Example 2:</strong> For custom-developed applications, maintain design "
        "specifications for each security module: authentication service, authorization "
        "engine, encryption library, logging framework. These specifications should be "
        "detailed enough that a security auditor can verify the implementation matches the "
        "design.</p>"
    ),

    "sa-5-5": (
        "<p>In some cases, you may need access to the source code of security-relevant "
        "components to verify that security controls are properly implemented. This applies "
        "primarily to custom-developed or high-assurance systems.</p>"
        "<p><strong>Example 1:</strong> For custom-developed applications, maintain the source "
        "code in a version-controlled repository (Git) with access restricted to authorized "
        "developers and security reviewers. Conduct code reviews of security-relevant modules "
        "(authentication, authorization, cryptography, input validation) before each release.</p>"
        "<p><strong>Example 2:</strong> For vendor-provided software where source code access "
        "is needed, include escrow provisions in contracts so that source code is available "
        "for security review or if the vendor goes out of business. For open-source components, "
        "review the relevant source code and track the project's security posture.</p>"
    ),

    "sa-6": (
        "<p>This control (withdrawn and incorporated into CM-10 and SI-7) addresses software "
        "usage restrictions — ensuring your organization only uses properly licensed software "
        "and does not use software in ways that violate licensing agreements or create "
        "security risks.</p>"
        "<p><strong>Example 1:</strong> Maintain a software license inventory that tracks every "
        "software product, the number of licenses owned, the number deployed, and the license "
        "terms. Use a software asset management tool to automatically detect unlicensed "
        "installations and flag them for remediation.</p>"
        "<p><strong>Example 2:</strong> In Microsoft Intune, use the <em>Discovered Apps</em> "
        "feature to see all software installed across your managed endpoints. Compare this "
        "against your approved software list and license inventory. Block or remove any "
        "unapproved or unlicensed software through Intune compliance policies.</p>"
    ),

    "sa-7": (
        "<p>This control (withdrawn and incorporated into CM-11 and SI-7) addresses user-"
        "installed software — ensuring that users cannot install unauthorized software that "
        "might introduce vulnerabilities, malware, or licensing violations.</p>"
        "<p><strong>Example 1:</strong> Remove local administrator privileges from standard "
        "users so they cannot install software on their own. Use a software deployment tool "
        "(SCCM, Intune, PDQ Deploy) to manage all software installations centrally. Users "
        "request software through a ticketing system; IT approves and deploys it.</p>"
        "<p><strong>Example 2:</strong> Configure application control policies (AppLocker or "
        "Windows Defender Application Control) to allow only approved applications to run. "
        "Create allow-list rules based on publisher certificates or file paths. Blocked "
        "attempts are logged and reviewed by the security team weekly.</p>"
    ),

    "sa-8": (
        "<p>Build systems using recognized security and privacy engineering principles from "
        "the start. These principles — defense in depth, least privilege, fail-safe defaults, "
        "separation of duties — should guide every design decision.</p>"
        "<p><strong>Example 1:</strong> Publish a set of security engineering principles that "
        "all development teams must follow: secure defaults (deny by default), defense in "
        "depth (multiple layers of protection), least privilege (minimum access needed), fail "
        "secure (lock down on failure), and separation of duties. Review designs against these "
        "principles before development begins.</p>"
        "<p><strong>Example 2:</strong> In your Azure or AWS environment, apply these principles "
        "through architecture patterns: use Azure Policy to enforce secure defaults, deploy "
        "network security groups for defense in depth, implement Azure PIM for just-in-time "
        "privileged access (least privilege), and configure resource locks for fail-safe "
        "protection.</p>"
    ),

    "sa-8-1": (
        "<p>Clear abstractions means that security interfaces and mechanisms should be simple, "
        "well-defined, and easy to understand. Confusing interfaces lead to misconfigurations "
        "and security mistakes.</p>"
        "<p><strong>Example 1:</strong> Design access control systems with clear, easily "
        "understood abstractions. Instead of complex, granular permissions that nobody "
        "configures correctly, define role-based access with clearly named roles like 'Reader,' "
        "'Contributor,' and 'Administrator' that map to intuitive permission sets.</p>"
        "<p><strong>Example 2:</strong> When building APIs, present security functions through "
        "clean, well-documented interfaces. Authentication should use standard protocols "
        "(OAuth 2.0, SAML) with clear documentation, not custom token schemes that developers "
        "need to reverse-engineer. The simpler the interface, the less likely it is to be "
        "misused.</p>"
    ),

    "sa-8-2": (
        "<p>Least common mechanism means minimizing the number of shared components between "
        "users and systems. Shared mechanisms (shared databases, shared service accounts) "
        "create paths for one user to affect another.</p>"
        "<p><strong>Example 1:</strong> Avoid shared service accounts — give each service and "
        "application its own dedicated credential. If your web app and reporting tool share "
        "the same database account, a vulnerability in the reporting tool gives an attacker "
        "the same access as the web app. Separate accounts, separate permissions.</p>"
        "<p><strong>Example 2:</strong> In cloud environments, avoid shared tenants or shared "
        "compute resources for sensitive workloads when possible. Use dedicated Azure "
        "subscriptions for different security zones and isolate workloads using separate "
        "virtual networks rather than relying solely on security groups within a shared "
        "network.</p>"
    ),

    "sa-8-3": (
        "<p>Modularity and layering means designing systems as distinct, manageable components "
        "with clear interfaces between layers. This makes security easier to implement, test, "
        "and verify at each layer independently.</p>"
        "<p><strong>Example 1:</strong> Design applications with separate modules for "
        "authentication, authorization, data access, and business logic. Each module can be "
        "independently updated, tested, and secured. A vulnerability in the business logic "
        "layer should not directly compromise the authentication layer.</p>"
        "<p><strong>Example 2:</strong> Apply defense in depth through network layering: "
        "perimeter firewall, DMZ for public-facing services, internal firewall, segmented "
        "VLANs for different sensitivity levels, and host-based firewalls on individual "
        "systems. Each layer provides independent protection so that if one fails, the next "
        "one catches the threat.</p>"
    ),

    "sa-8-4": (
        "<p>Partially ordered dependencies means designing systems so that component "
        "dependencies flow in one direction and do not create circular relationships. This "
        "reduces complexity and makes security properties easier to reason about.</p>"
        "<p><strong>Example 1:</strong> In application architecture, structure dependencies so "
        "higher-level components depend on lower-level components, not the reverse. Your web "
        "front-end depends on the API layer, which depends on the database. The database "
        "should never call back into the web front-end — that creates a circular dependency "
        "that is hard to secure.</p>"
        "<p><strong>Example 2:</strong> In your infrastructure, avoid circular trust "
        "relationships between security domains. Your authentication service (Active Directory) "
        "should be a foundational dependency that other services rely on, not something that "
        "depends on the services it authenticates.</p>"
    ),

    "sa-8-5": (
        "<p>Efficiently mediated access means that every access attempt is checked by a "
        "reference monitor (access control mechanism) that cannot be bypassed, is tamper-"
        "proof, and is small enough to be verified.</p>"
        "<p><strong>Example 1:</strong> Ensure your access control enforcement points cannot "
        "be bypassed. If users must go through a VPN to access internal resources, make sure "
        "there are no alternative paths (open RDP ports, unprotected management interfaces) "
        "that skip the VPN. Regularly scan for unauthorized access paths.</p>"
        "<p><strong>Example 2:</strong> In web applications, enforce authorization checks at "
        "the API layer, not just in the UI. A user might bypass the UI by calling the API "
        "directly — every API endpoint must independently verify the caller's permissions "
        "before returning data. Never rely on the front-end to enforce security.</p>"
    ),

    "sa-8-6": (
        "<p>Minimized sharing means reducing the information and resources shared between "
        "components, users, and systems. The less sharing, the smaller the blast radius "
        "when something goes wrong.</p>"
        "<p><strong>Example 1:</strong> Apply the need-to-know principle to data sharing "
        "between systems. Your HR system does not need to share SSNs with the email system. "
        "Your CRM does not need access to the engineering design database. Connect systems "
        "only when there is a documented business need and share only the minimum data "
        "required.</p>"
        "<p><strong>Example 2:</strong> In M365, use <em>Information Barriers</em> to prevent "
        "inappropriate data sharing between departments. For example, prevent the trading desk "
        "from communicating with the compliance investigation team, or prevent the HR team's "
        "SharePoint sites from being shared with contractors.</p>"
    ),

    "sa-8-7": (
        "<p>Reduced complexity means keeping systems as simple as practical. Complex systems "
        "have more potential failure points, more attack surface, and are harder to secure "
        "and audit.</p>"
        "<p><strong>Example 1:</strong> During system design reviews, actively challenge "
        "complexity. If a system has 50 open ports but only needs 5, disable the other 45. "
        "If a server runs 10 services but only 3 are required, remove the other 7. Every "
        "unnecessary component is attack surface you have to defend.</p>"
        "<p><strong>Example 2:</strong> In your cloud environment, prefer managed services "
        "over self-managed infrastructure when security requirements allow it. Using Azure "
        "SQL Managed Instance instead of running SQL Server on a VM eliminates the complexity "
        "of managing the OS, patching, and host-level security — Microsoft handles those "
        "layers for you.</p>"
    ),

    "sa-8-8": (
        "<p>Secure evolvability means designing systems so they can be updated, patched, and "
        "upgraded without introducing security gaps. Systems that are hard to update tend to "
        "fall behind on security.</p>"
        "<p><strong>Example 1:</strong> Design systems with modularity that allows individual "
        "components to be updated without a full system rebuild. Use containerized deployments "
        "(Docker, Kubernetes) so that updating a single service does not require downtime or "
        "re-testing the entire application stack.</p>"
        "<p><strong>Example 2:</strong> Maintain CI/CD pipelines with automated security tests "
        "that run on every update. This lets you deploy patches and updates quickly and "
        "confidently, knowing that each change is automatically checked for security "
        "regressions before it reaches production.</p>"
    ),

    "sa-8-9": (
        "<p>Trusted components means using components (hardware, software, firmware) whose "
        "integrity and security properties can be verified. You need to trust but verify "
        "the building blocks of your systems.</p>"
        "<p><strong>Example 1:</strong> Maintain an approved components list that identifies "
        "trusted hardware and software sources. Verify software integrity using vendor-provided "
        "checksums or digital signatures before installation. For critical systems, use only "
        "components from verified supply chains.</p>"
        "<p><strong>Example 2:</strong> In your development environment, use signed packages "
        "from trusted registries (NuGet, npm, PyPI) and lock dependency versions. Implement "
        "tools like Dependabot or Snyk to alert you when a dependency has known "
        "vulnerabilities or has been tampered with.</p>"
    ),

    "sa-8-10": (
        "<p>Hierarchical trust means organizing trust relationships in a layered structure "
        "where higher layers depend on the trustworthiness of lower layers. Your most secure "
        "components form the foundation everything else relies on.</p>"
        "<p><strong>Example 1:</strong> Design your infrastructure so that the most critical "
        "security components (domain controllers, certificate authorities, key management "
        "systems) are the most protected and form the trust foundation. If Active Directory "
        "is compromised, everything that depends on it is compromised — so AD gets the "
        "strongest protection.</p>"
        "<p><strong>Example 2:</strong> Implement a PKI hierarchy with offline root CAs that "
        "sign intermediate CAs, which in turn issue certificates. The root CA sits at the "
        "top of the trust hierarchy and is stored offline. If an intermediate CA is "
        "compromised, it can be revoked without affecting the root.</p>"
    ),

    "sa-8-11": (
        "<p>Inverse modification threshold means that the more critical a component is, the "
        "harder it should be to modify. High-privilege changes should require more approvals, "
        "more oversight, and more verification than low-privilege changes.</p>"
        "<p><strong>Example 1:</strong> Implement tiered change control: changes to workstations "
        "require IT manager approval. Changes to servers require both IT manager and system "
        "owner approval. Changes to domain controllers or security infrastructure require "
        "CISO approval and a documented change advisory board review.</p>"
        "<p><strong>Example 2:</strong> In Azure, use Resource Locks on critical resources "
        "(domain controllers, key vaults, security appliances) to prevent accidental "
        "modification. Implement Azure PIM so that privileged changes require just-in-time "
        "approval with multi-person authorization for the most critical resources.</p>"
    ),

    "sa-8-12": (
        "<p>Hierarchical protection means applying stronger protection measures to more "
        "critical components and data. Not everything needs the same level of security — "
        "protect the crown jewels the most.</p>"
        "<p><strong>Example 1:</strong> Apply security controls proportional to data "
        "sensitivity. Public data gets basic access controls. Internal data gets encryption "
        "at rest and role-based access. CUI gets encryption in transit and at rest, DLP "
        "policies, and audit logging. Classified data gets all of the above plus physical "
        "controls and clearance requirements.</p>"
        "<p><strong>Example 2:</strong> In your network architecture, place the most sensitive "
        "systems behind multiple layers of protection: a DMZ for public-facing services, a "
        "general internal zone for standard workloads, and a restricted enclave with additional "
        "firewalls and monitoring for CUI and critical systems.</p>"
    ),

    "sa-8-13": (
        "<p>Minimized security elements means keeping the security mechanisms themselves as "
        "small and focused as possible. The less code in your security-critical components, "
        "the less there is to audit, test, and potentially fail.</p>"
        "<p><strong>Example 1:</strong> When developing custom security modules (authentication, "
        "encryption wrappers), keep them focused on a single responsibility. An authentication "
        "module should only handle authentication — do not bundle logging, reporting, and "
        "configuration management into the same module.</p>"
        "<p><strong>Example 2:</strong> Prefer well-established, focused security libraries "
        "over rolling your own. Use proven cryptography libraries (libsodium, BouncyCastle) "
        "instead of implementing custom encryption. Use established authentication frameworks "
        "(ASP.NET Identity, Spring Security) instead of building your own token system.</p>"
    ),

    "sa-8-14": (
        "<p>Least privilege in design means that every component, process, and user is given "
        "the minimum access necessary to perform its function — nothing more.</p>"
        "<p><strong>Example 1:</strong> Configure application service accounts with only the "
        "database permissions they need. If a web application only reads from and writes to "
        "two tables, its database account should have SELECT and INSERT permissions on those "
        "two tables — not dbo access to the entire database.</p>"
        "<p><strong>Example 2:</strong> In Azure, assign RBAC roles at the most specific scope "
        "possible. If a developer needs to manage a single App Service, assign them the "
        "Contributor role on that App Service resource — not at the resource group or "
        "subscription level. Use Azure PIM for any privileged roles that are only needed "
        "occasionally.</p>"
    ),

    "sa-8-15": (
        "<p>Predicate permission means that access decisions are based on verifiable conditions "
        "(predicates) that are evaluated at the time of access, not just at the time of initial "
        "authorization.</p>"
        "<p><strong>Example 1:</strong> Implement Conditional Access policies that evaluate "
        "conditions at every login: user role, device compliance, location, and risk level. "
        "A user who was authorized yesterday from a compliant device in the office might be "
        "denied today if they are logging in from an unknown device in a foreign country.</p>"
        "<p><strong>Example 2:</strong> In Azure AD Conditional Access, create policies that "
        "require device compliance and MFA for all access, block access from risky sign-in "
        "locations, and enforce app-level restrictions based on user risk score. The access "
        "decision is made in real-time based on current conditions, not a static permission "
        "grant.</p>"
    ),

    "sa-8-16": (
        "<p>Self-reliant trustworthiness means that a system should not depend on external "
        "entities for its fundamental security properties. If the network goes down, the "
        "system should still protect its data.</p>"
        "<p><strong>Example 1:</strong> Configure endpoints to enforce security policies locally, "
        "even when disconnected from the network. BitLocker should encrypt the disk whether or "
        "not the device can reach the domain controller. Windows Defender should continue "
        "scanning with cached definitions when offline.</p>"
        "<p><strong>Example 2:</strong> Design applications so that security checks run locally "
        "rather than requiring a round-trip to a central server for every decision. Cache "
        "authorization tokens with appropriate expiration times so the application can continue "
        "making access decisions during brief network outages.</p>"
    ),

    "sa-8-17": (
        "<p>Secure distributed composition means that when multiple components or services "
        "work together across a distributed system, the overall security is not weaker than "
        "any individual component.</p>"
        "<p><strong>Example 1:</strong> In a microservices architecture, enforce security at "
        "every service boundary, not just at the edge. Each microservice should authenticate "
        "and authorize requests from other services using mutual TLS or service-to-service "
        "tokens, not just trust any request that comes from within the private network.</p>"
        "<p><strong>Example 2:</strong> When integrating cloud services from multiple providers, "
        "ensure consistent security policies across all of them. If one provider encrypts data "
        "at rest but another does not, the overall system's security is limited by the weakest "
        "link. Document the security properties of each component and verify the composition "
        "maintains your required security level.</p>"
    ),

    "sa-8-18": (
        "<p>Trusted communications channels means that data moving between components must be "
        "protected against interception, modification, and replay. All network communication "
        "should use encrypted, authenticated channels.</p>"
        "<p><strong>Example 1:</strong> Enforce TLS 1.2 or higher for all network communications. "
        "Disable TLS 1.0 and 1.1, SSL v3, and weak cipher suites across all systems. Use Group "
        "Policy to set minimum TLS versions on Windows systems and configure web servers to "
        "present only strong cipher suites.</p>"
        "<p><strong>Example 2:</strong> For internal service-to-service communication, implement "
        "mutual TLS (mTLS) where both sides authenticate with certificates. In Kubernetes, "
        "use a service mesh like Istio to automatically enforce mTLS between all pods without "
        "requiring application-level changes.</p>"
    ),

    "sa-8-19": (
        "<p>Continuous protection means that security controls protect the system at all times, "
        "including during startup, shutdown, maintenance, and failure conditions. There should "
        "be no gaps in protection.</p>"
        "<p><strong>Example 1:</strong> Verify that your security controls operate during all "
        "system states. Encryption should protect data on disk whether the system is running "
        "or shut down (full disk encryption). Firewall rules should be the first thing applied "
        "during boot and the last thing removed during shutdown.</p>"
        "<p><strong>Example 2:</strong> Test your security controls during maintenance windows. "
        "When you take a system offline for patching, verify that data remains encrypted, "
        "access controls are still enforced, and audit logging resumes immediately after the "
        "system returns to service. Document any protection gaps during maintenance and "
        "mitigate them.</p>"
    ),

    "sa-8-20": (
        "<p>Secure metadata management means protecting the metadata (data about data) in "
        "your systems with the same rigor as the data itself. Metadata like access logs, "
        "classification labels, and timestamps can reveal sensitive information.</p>"
        "<p><strong>Example 1:</strong> Protect audit logs and access records with the same "
        "security controls as the data they describe. If your audit logs capture who accessed "
        "classified information and when, those logs are themselves sensitive. Store them in "
        "a protected, append-only log store with restricted access.</p>"
        "<p><strong>Example 2:</strong> When transmitting files with sensitivity labels or "
        "classification markings, ensure the metadata travels with the file and cannot be "
        "stripped in transit. In Microsoft Purview, sensitivity labels are embedded in the "
        "file and travel with it — verify that your DLP policies check the label metadata, "
        "not just the file contents.</p>"
    ),

    "sa-8-21": (
        "<p>Self-analysis means designing systems with built-in capabilities to monitor "
        "their own security state and report anomalies. Systems should be able to detect "
        "when their own security properties have been violated.</p>"
        "<p><strong>Example 1:</strong> Enable Windows Measured Boot and Secure Boot so the "
        "system checks its own boot integrity on every startup. If the boot process has been "
        "tampered with, the system detects and reports it through the TPM (Trusted Platform "
        "Module) attestation mechanism.</p>"
        "<p><strong>Example 2:</strong> Implement application-level health checks that verify "
        "security configuration on startup: are encryption keys loaded, are TLS certificates "
        "valid, are required security services running? If any check fails, the application "
        "should refuse to start and alert the operations team rather than running in a "
        "degraded security state.</p>"
    ),

    "sa-8-22": (
        "<p>Accountability and traceability means that every action in the system can be "
        "attributed to a specific individual and traced through the system's audit trail. "
        "No action should be anonymous.</p>"
        "<p><strong>Example 1:</strong> Eliminate shared accounts and require individual "
        "authentication for all system access. Even for emergency or break-glass accounts, "
        "log which individual used the shared credential by requiring a sign-out process "
        "that records the user's identity alongside the shared account usage.</p>"
        "<p><strong>Example 2:</strong> In Azure AD, enable <em>Sign-in Logs</em> and <em>Audit "
        "Logs</em> with retention in Microsoft Sentinel or Log Analytics. Every authentication "
        "event, role assignment, application access, and configuration change is attributed "
        "to a specific identity with timestamps and source metadata. Set retention to at "
        "least one year.</p>"
    ),

    "sa-8-23": (
        "<p>Secure defaults means that systems should be secure out of the box. The default "
        "configuration should be the most secure configuration, requiring administrators to "
        "explicitly open things up rather than lock things down.</p>"
        "<p><strong>Example 1:</strong> When deploying new systems, start from a hardened "
        "baseline (DISA STIG, CIS Benchmark) where everything is locked down by default. "
        "Then selectively enable only the features and services actually needed. This is "
        "more secure than starting with defaults and trying to harden after the fact.</p>"
        "<p><strong>Example 2:</strong> In M365, new tenants come with a set of default "
        "security settings (Security Defaults). Review Microsoft's <em>Secure Score</em> "
        "recommendations immediately and implement the top-priority items before users start "
        "using the environment. Block legacy authentication, enable MFA, and disable external "
        "sharing by default.</p>"
    ),

    "sa-8-24": (
        "<p>Secure failure and recovery means that when a system fails, it fails into a "
        "secure state rather than an insecure one, and recovery procedures do not introduce "
        "security gaps.</p>"
        "<p><strong>Example 1:</strong> Configure firewalls in fail-closed mode: if the "
        "firewall crashes or loses its configuration, it blocks all traffic rather than "
        "allowing everything through. Similarly, if your authentication service goes down, "
        "systems should deny access rather than allowing unauthenticated access.</p>"
        "<p><strong>Example 2:</strong> Test your disaster recovery procedures for security. "
        "When you restore a system from backup, verify that security configurations (firewall "
        "rules, access controls, encryption settings) are restored correctly. A recovered "
        "system that comes back with weaker security than before the failure creates a "
        "window of vulnerability.</p>"
    ),

    "sa-8-25": (
        "<p>Economic security means considering the costs and resource requirements of "
        "security mechanisms. Security controls that are too expensive to implement or "
        "maintain properly will eventually be disabled or neglected.</p>"
        "<p><strong>Example 1:</strong> When selecting security controls, evaluate the total "
        "cost of ownership — not just the license fee, but staffing to operate and monitor, "
        "training, maintenance, and the operational impact on users. A cheaper tool that your "
        "team can actually use and maintain is more secure than an expensive one that nobody "
        "understands.</p>"
        "<p><strong>Example 2:</strong> Leverage built-in security features before purchasing "
        "additional tools. Microsoft 365 E5 includes Defender for Endpoint, Sentinel-ready "
        "connectors, DLP, and Conditional Access. If you are already paying for E5, use these "
        "capabilities rather than buying separate products that add cost and complexity.</p>"
    ),

    "sa-8-26": (
        "<p>Performance security means that security controls should not degrade system "
        "performance to the point where users bypass them. Security that slows work to a "
        "crawl gets disabled in practice.</p>"
        "<p><strong>Example 1:</strong> Test the performance impact of security controls "
        "before deployment. If full-disk encryption slows laptop boot time from 30 seconds "
        "to 5 minutes, users will resist. Choose encryption solutions with hardware "
        "acceleration (most modern CPUs support AES-NI) that make the performance impact "
        "imperceptible.</p>"
        "<p><strong>Example 2:</strong> Configure endpoint protection (antivirus, EDR) with "
        "appropriate exclusions for performance-sensitive applications. If your scanner slows "
        "database operations by 40%, work with the vendor to configure scan exclusions for "
        "database data files while maintaining protection for executable files and scripts.</p>"
    ),

    "sa-8-27": (
        "<p>Human-factored security means designing security controls that work with human "
        "behavior rather than against it. If a security control requires perfect human "
        "behavior to be effective, it will fail.</p>"
        "<p><strong>Example 1:</strong> Replace complex password requirements with passphrase "
        "policies and MFA. 'FourRandomWordsAreEasy!' is both more secure and easier to "
        "remember than 'P@ssw0rd123!'. Combine with MFA so that even if the passphrase is "
        "compromised, the account is still protected.</p>"
        "<p><strong>Example 2:</strong> Use single sign-on (SSO) to reduce the number of "
        "credentials users must manage. Every separate login is a security failure point — "
        "users will reuse passwords, write them on sticky notes, or choose weak ones. "
        "Federate all applications through Azure AD SSO so users authenticate once with "
        "strong MFA and everything else follows automatically.</p>"
    ),

    "sa-8-28": (
        "<p>Acceptable security means that the level of security implemented is appropriate "
        "for the system's risk level and mission importance. Over-engineering security wastes "
        "resources; under-engineering creates unacceptable risk.</p>"
        "<p><strong>Example 1:</strong> Match your security investment to the system's "
        "categorization. A FIPS 199 Low system does not need the same depth of monitoring as "
        "a High system. Spend your limited resources where the risk is greatest — protect "
        "your CUI processing systems more heavily than your break room display TV.</p>"
        "<p><strong>Example 2:</strong> Use your risk assessment results to justify security "
        "spending. If the annual loss expectancy from a risk is $10,000, spending $100,000 "
        "to mitigate it does not make business sense. Document the cost-benefit analysis and "
        "present risk acceptance decisions to leadership for formal approval.</p>"
    ),

    "sa-8-29": (
        "<p>Repeatable and documented procedures ensure that security activities are performed "
        "consistently every time, regardless of who performs them. Undocumented procedures "
        "live only in people's heads and leave when they do.</p>"
        "<p><strong>Example 1:</strong> Write standard operating procedures (SOPs) for all "
        "recurring security tasks: vulnerability scanning, patch management, account "
        "provisioning and deprovisioning, incident response, and backup verification. "
        "Include step-by-step instructions with screenshots so anyone with basic technical "
        "skills can follow them.</p>"
        "<p><strong>Example 2:</strong> Store SOPs in a central location (SharePoint, "
        "Confluence) with version control. Require procedures to be reviewed and updated "
        "annually or whenever the process changes. When new staff perform a procedure for "
        "the first time, have them follow the SOP and note any steps that are unclear or "
        "outdated — then update the SOP.</p>"
    ),

    "sa-8-30": (
        "<p>Procedural rigor means that security procedures are followed precisely and "
        "completely, not approximated or shortcut. When you cut corners on security "
        "procedures, you introduce the very risks the procedures were designed to prevent.</p>"
        "<p><strong>Example 1:</strong> Implement checklists for critical security procedures "
        "and require them to be completed in full. For system hardening, use a STIG checklist "
        "where each item must be verified and signed off. For incident response, use a "
        "structured playbook where each step is documented as completed.</p>"
        "<p><strong>Example 2:</strong> Conduct periodic compliance audits where you verify "
        "that procedures are being followed as written. Spot-check a sample of account "
        "provisioning requests to verify all steps were completed. Review a sample of change "
        "management tickets to ensure security reviews were conducted before changes were "
        "implemented. Document and correct deviations.</p>"
    ),

    "sa-8-31": (
        "<p>Secure system modification means that any change to a system preserves or improves "
        "its security properties. Changes should not weaken security, and the modification "
        "process itself should be controlled.</p>"
        "<p><strong>Example 1:</strong> Require a security review for every system change "
        "through your change management process. Before implementing a change, evaluate its "
        "security impact: does it open new ports, add new users, change permissions, or "
        "introduce new software? If yes, the security team must approve the change.</p>"
        "<p><strong>Example 2:</strong> After implementing changes, verify that security "
        "controls still function correctly. Run a configuration compliance scan (SCAP, STIG "
        "Viewer) after major changes to confirm that the system still meets its security "
        "baseline. If the change caused a compliance deviation, remediate it before closing "
        "the change ticket.</p>"
    ),

    "sa-8-32": (
        "<p>Sufficient documentation means that security-relevant aspects of the system are "
        "documented well enough to be independently verified, operated, and maintained. "
        "Undocumented security is unverifiable security.</p>"
        "<p><strong>Example 1:</strong> For each system, maintain documentation that covers: "
        "security architecture, access control configuration, encryption implementation, "
        "audit logging setup, backup procedures, and incident response contacts. Store this "
        "documentation alongside the system security plan.</p>"
        "<p><strong>Example 2:</strong> Create runbooks for your security operations team "
        "that document common scenarios: how to investigate an alert, how to isolate a "
        "compromised system, how to restore from backup, and how to report an incident. "
        "Test the runbooks during tabletop exercises and update them with lessons learned.</p>"
    ),

    "sa-8-33": (
        "<p>Minimization as a design principle means collecting, processing, and retaining "
        "only the minimum information necessary for the system's purpose. Less data means "
        "less risk.</p>"
        "<p><strong>Example 1:</strong> Review your data collection forms and database schemas. "
        "For every field, ask: 'Do we actually need this to perform the function?' If you "
        "collect date of birth but never use it for anything, stop collecting it. Less data "
        "stored means less data to protect and less damage if breached.</p>"
        "<p><strong>Example 2:</strong> Implement data retention policies that automatically "
        "purge data past its useful life. In Microsoft Purview, use <em>Retention Labels</em> "
        "to mark data with retention periods and automatically delete it when the period "
        "expires. Configure Exchange Online to purge deleted items after 30 days and apply "
        "retention policies to SharePoint content.</p>"
    ),

    "sa-9": (
        "<p>When your organization uses external services — cloud providers, managed services, "
        "outsourced IT — you must ensure those services meet your security requirements. "
        "Outsourcing the work does not outsource the risk.</p>"
        "<p><strong>Example 1:</strong> Require all external service providers to meet defined "
        "security requirements documented in your contracts. Include clauses for incident "
        "notification (within 24 hours), data protection standards (encryption at rest and "
        "in transit), access controls, and the right to audit or request compliance evidence.</p>"
        "<p><strong>Example 2:</strong> For cloud services, review the provider's shared "
        "responsibility model to understand exactly what they secure and what you must secure. "
        "For Microsoft 365, Microsoft secures the infrastructure; you are responsible for "
        "identity management, data classification, DLP policies, and Conditional Access "
        "configuration. Document this division of responsibility.</p>"
    ),

    "sa-9-1": (
        "<p>Before using an external service, conduct a risk assessment and obtain "
        "organizational approval. Someone with authority must accept the risk of depending "
        "on an external provider.</p>"
        "<p><strong>Example 1:</strong> Before onboarding a new cloud service, complete a "
        "vendor risk assessment that evaluates their security certifications (SOC 2, ISO "
        "27001, FedRAMP), data handling practices, incident history, and financial stability. "
        "Present the assessment to your CISO or risk management board for formal approval.</p>"
        "<p><strong>Example 2:</strong> Create a vendor approval workflow in your procurement "
        "system. No purchase order for IT services can be issued without a completed security "
        "risk assessment form and sign-off from the security team. Track all approved vendors "
        "in a vendor register with their risk rating and next assessment date.</p>"
    ),

    "sa-9-2": (
        "<p>Document all functions, ports, protocols, and services used by your external "
        "service providers. You need to know exactly what traffic flows to and from external "
        "services to secure and monitor those connections.</p>"
        "<p><strong>Example 1:</strong> For each external service, document the network "
        "connections required: protocols (HTTPS, SFTP), destination URLs or IPs, ports, "
        "authentication methods, and the type of data transmitted. Configure your firewall "
        "to allow only these documented connections and deny everything else.</p>"
        "<p><strong>Example 2:</strong> Use network monitoring tools to validate that external "
        "services are communicating only on documented ports and protocols. In Microsoft "
        "Defender for Cloud Apps, use <em>Cloud Discovery</em> to detect all cloud service "
        "connections from your network and compare them against your approved service list.</p>"
    ),

    "sa-9-3": (
        "<p>Establish and maintain a trust relationship with your external service providers. "
        "Trust is not a one-time evaluation — it requires ongoing monitoring and verification "
        "that the provider continues to meet your security requirements.</p>"
        "<p><strong>Example 1:</strong> Request updated SOC 2 Type II reports from your "
        "critical vendors annually. Review the auditor's findings and management responses. "
        "If the report shows significant control failures, schedule a meeting with the vendor "
        "to understand their remediation plan and timeline.</p>"
        "<p><strong>Example 2:</strong> Include contractual provisions for regular security "
        "attestations, notification of material security changes, and the right to conduct or "
        "commission independent audits. Schedule annual vendor review meetings to discuss "
        "security posture, incident history, and upcoming changes that might affect your "
        "security.</p>"
    ),

    "sa-9-4": (
        "<p>Ensure that your service provider's interests align with yours when it comes to "
        "security. If the provider profits from collecting your data or benefits from lax "
        "security practices, there is a conflict of interest.</p>"
        "<p><strong>Example 1:</strong> Review your vendor contracts for conflicts of interest. "
        "Does the vendor have the right to use your data for their own purposes (analytics, "
        "marketing, AI training)? If so, negotiate those terms out or find a vendor whose "
        "business model does not depend on monetizing your data.</p>"
        "<p><strong>Example 2:</strong> Include performance-based security SLAs in contracts: "
        "uptime guarantees, patch deployment timelines, incident response SLAs, and financial "
        "penalties for security failures. When the vendor has financial skin in the game, their "
        "interests align more closely with yours.</p>"
    ),

    "sa-9-5": (
        "<p>Know where your data is being processed and stored by external service providers. "
        "Data location affects which laws apply, what risks exist, and whether your regulatory "
        "requirements are met.</p>"
        "<p><strong>Example 1:</strong> In your service agreements, specify that data must be "
        "processed and stored in the United States (or other approved jurisdictions). Require "
        "the provider to notify you before any data location changes and give you the right "
        "to terminate if data moves to an unapproved jurisdiction.</p>"
        "<p><strong>Example 2:</strong> In Azure, use <em>Azure Policy</em> to restrict "
        "resource deployment to specific regions (e.g., East US, West US). This ensures that "
        "your virtual machines, databases, and storage accounts are only created in approved "
        "data center locations. Audit compliance with these policies monthly.</p>"
    ),

    "sa-9-6": (
        "<p>When using external services that encrypt your data, you should control your own "
        "encryption keys rather than relying on the provider to manage them. This ensures you "
        "maintain control over your data even if the relationship with the provider ends.</p>"
        "<p><strong>Example 1:</strong> For cloud services that offer customer-managed keys, "
        "use your own keys stored in your Azure Key Vault or AWS KMS rather than relying on "
        "the provider's default encryption. This ensures the provider cannot access your "
        "encrypted data without your key.</p>"
        "<p><strong>Example 2:</strong> In Microsoft 365, configure <em>Customer Key</em> "
        "(available with E5) so that your data in Exchange Online, SharePoint, and Teams is "
        "encrypted with keys you control. If you ever need to leave the service, you can "
        "revoke the keys, rendering the data unreadable.</p>"
    ),

    "sa-9-7": (
        "<p>When external services process or store your data, you should have the ability "
        "to independently verify the integrity of that data — not just trust the provider's "
        "word that nothing has been modified.</p>"
        "<p><strong>Example 1:</strong> Implement cryptographic integrity verification for "
        "data stored with external providers. Before uploading critical data, compute and "
        "store hash values (SHA-256) locally. Periodically download samples and verify the "
        "hashes match to confirm data has not been altered.</p>"
        "<p><strong>Example 2:</strong> For database replication to external services, use "
        "transaction log verification to confirm that all transactions are applied correctly. "
        "Run periodic reconciliation checks comparing local and external data stores to "
        "detect any discrepancies that might indicate data corruption or tampering.</p>"
    ),

    "sa-9-8": (
        "<p>For certain sensitive data, processing and storage must be limited to locations "
        "within U.S. jurisdiction. This is particularly important for CUI, ITAR data, and "
        "other regulated information types.</p>"
        "<p><strong>Example 1:</strong> For systems processing CUI or ITAR-controlled data, "
        "verify that all processing and storage locations are within the United States. Review "
        "your cloud provider's data residency documentation and restrict deployments to U.S. "
        "regions only. Include U.S.-only data processing requirements in your contracts.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft 365 GCC or GCC High environments for "
        "government and defense contractor workloads that require U.S.-only data residency. "
        "These environments guarantee data processing within U.S. borders by Microsoft "
        "personnel who are U.S. persons with appropriate background checks.</p>"
    ),

    "sa-10": (
        "<p>Require developers (internal or vendor) to use configuration management for their "
        "code and systems. Every change should be tracked, authorized, and reversible.</p>"
        "<p><strong>Example 1:</strong> Require all development teams to use version control "
        "(Git) for source code, configuration files, and infrastructure-as-code templates. "
        "All changes must go through pull requests with at least one reviewer approval before "
        "merging. No direct commits to main branches.</p>"
        "<p><strong>Example 2:</strong> In Azure DevOps or GitHub, enforce branch protection "
        "policies that require code reviews, passing CI checks, and signed commits before "
        "merging to production branches. Use release pipelines with approval gates so that "
        "only authorized personnel can promote code to production.</p>"
    ),

    "sa-10-1": (
        "<p>Verify the integrity of software and firmware to ensure it has not been tampered "
        "with during development, distribution, or installation.</p>"
        "<p><strong>Example 1:</strong> Implement code signing for all internally developed "
        "software. Sign release builds with your organization's code signing certificate so "
        "that any tampering after signing is detectable. Configure your endpoints to only "
        "run signed code through Windows Defender Application Control or AppLocker.</p>"
        "<p><strong>Example 2:</strong> When downloading software from vendors, verify the "
        "file hash or digital signature against the vendor's published values before "
        "installing. Automate this in your deployment pipeline: the script downloads the "
        "software, verifies the hash, and only proceeds with installation if the hash "
        "matches.</p>"
    ),

    "sa-10-2": (
        "<p>When standard configuration management processes are not feasible (emergency "
        "patches, rapid prototyping), have an alternative process that still provides "
        "oversight and traceability.</p>"
        "<p><strong>Example 1:</strong> Define an emergency change process for situations "
        "where normal change management would take too long (e.g., deploying a critical "
        "security patch during an active attack). The process should include who can authorize "
        "emergency changes, what documentation is required after the fact, and a mandatory "
        "post-incident review.</p>"
        "<p><strong>Example 2:</strong> In Azure DevOps, create a separate 'hotfix' pipeline "
        "that allows expedited deployments with fewer approval gates but still requires at "
        "least one senior engineer approval and automated security scan. After the emergency, "
        "the change must be retroactively reviewed and merged into the standard release process.</p>"
    ),

    "sa-10-3": (
        "<p>Verify the integrity of hardware components to ensure they have not been tampered "
        "with during manufacturing, shipping, or installation.</p>"
        "<p><strong>Example 1:</strong> When receiving new hardware, inspect packaging for "
        "signs of tampering (broken seals, evidence of opening and resealing). Compare serial "
        "numbers and model numbers against the purchase order. For critical components, verify "
        "firmware versions against the manufacturer's published versions before deployment.</p>"
        "<p><strong>Example 2:</strong> Enable hardware integrity features like TPM (Trusted "
        "Platform Module) on all systems and configure them to verify boot integrity through "
        "Secure Boot and Measured Boot. If the firmware or boot loader has been tampered with, "
        "the system alerts the administrator before loading the operating system.</p>"
    ),

    "sa-10-4": (
        "<p>Trusted generation ensures that software builds are produced in a secure, "
        "controlled environment where the build process cannot be tampered with. The "
        "build system itself must be trusted.</p>"
        "<p><strong>Example 1:</strong> Use dedicated, hardened build servers that are not "
        "used for general development. Restrict access to the build environment to only the "
        "personnel who maintain it. Implement build reproducibility so that the same source "
        "code always produces the same binary output, making tampering detectable.</p>"
        "<p><strong>Example 2:</strong> In your CI/CD pipeline, implement supply chain "
        "integrity measures: lock dependency versions, verify dependency hashes, use signed "
        "container base images, and generate SBOMs (Software Bills of Materials) for every "
        "build. Tools like SLSA (Supply-chain Levels for Software Artifacts) provide a "
        "framework for securing your build pipeline.</p>"
    ),

    "sa-10-5": (
        "<p>Mapping integrity for version control ensures that the relationship between source "
        "code versions and deployed artifacts is maintained and verifiable. You need to know "
        "exactly what code is running in production.</p>"
        "<p><strong>Example 1:</strong> Tag every release in your version control system with "
        "a unique version number. Record the exact commit hash, build number, and deployment "
        "date for every production deployment. At any point, you should be able to trace a "
        "running binary back to the exact source code that produced it.</p>"
        "<p><strong>Example 2:</strong> In your CI/CD pipeline, embed version metadata (Git "
        "commit hash, build timestamp, pipeline run ID) in the built artifact. This makes "
        "it possible to verify that a deployed application matches a specific source code "
        "version without needing to rebuild.</p>"
    ),

    "sa-10-6": (
        "<p>Trusted distribution ensures that software reaches the end user or deployment "
        "target without being tampered with during transit. The delivery channel must be as "
        "secure as the build process.</p>"
        "<p><strong>Example 1:</strong> Distribute software through secure, authenticated "
        "channels only. Use HTTPS for all downloads, digitally sign packages, and publish "
        "checksums on a separate channel so recipients can verify integrity. Never distribute "
        "software via unencrypted email or open file shares.</p>"
        "<p><strong>Example 2:</strong> Use private package repositories (Azure Artifacts, "
        "JFrog Artifactory, GitHub Packages) for internal software distribution. Configure "
        "the repository to only accept signed packages and to serve packages over HTTPS. "
        "Your deployment pipelines should pull artifacts exclusively from these trusted "
        "repositories.</p>"
    ),

    "sa-10-7": (
        "<p>Include security and privacy representatives in the development team so that "
        "security considerations are part of the development process, not a last-minute "
        "review.</p>"
        "<p><strong>Example 1:</strong> Assign a security champion to every development team. "
        "This person participates in design reviews, user story grooming, and code reviews "
        "with a security lens. They do not replace the security team but ensure security "
        "is considered during daily development activities.</p>"
        "<p><strong>Example 2:</strong> Include a privacy engineer or privacy point of contact "
        "in projects that handle PII. This person reviews data collection plans, ensures "
        "privacy by design principles are followed, and validates that the implementation "
        "matches the approved Privacy Impact Assessment.</p>"
    ),

    "sa-11": (
        "<p>Developers must test and evaluate the security of their products as part of the "
        "development process. Security testing should not be an afterthought — it must be "
        "built into the development lifecycle.</p>"
        "<p><strong>Example 1:</strong> Require developers to submit a security test plan and "
        "test results as part of their delivery package. The plan should cover authentication "
        "testing, authorization testing, input validation, encryption verification, and "
        "error handling. Results should demonstrate that each security requirement was tested "
        "and met.</p>"
        "<p><strong>Example 2:</strong> Integrate security testing tools into your CI/CD "
        "pipeline: SAST tools (SonarQube, Semgrep) scan code on every commit, dependency "
        "checkers (Dependabot, Snyk) alert on vulnerable libraries, and DAST tools (OWASP "
        "ZAP, Burp Suite) test running applications before deployment. Gate production "
        "releases on passing security tests.</p>"
    ),

    "sa-11-1": (
        "<p>Static code analysis examines source code for security vulnerabilities without "
        "executing the program. It catches many common coding errors like SQL injection, "
        "cross-site scripting, and buffer overflows before the code ever runs.</p>"
        "<p><strong>Example 1:</strong> Configure a static analysis tool (SonarQube, Semgrep, "
        "Checkmarx) to scan code automatically on every pull request. Set quality gates that "
        "block merging if critical or high-severity findings are detected. Review and resolve "
        "findings before the code moves forward.</p>"
        "<p><strong>Example 2:</strong> In GitHub, enable <em>Advanced Security</em> with "
        "CodeQL analysis. CodeQL scans your codebase for vulnerability patterns and creates "
        "security alerts directly in the pull request. Configure it to scan on every push "
        "and pull request to the main branch.</p>"
    ),

    "sa-11-2": (
        "<p>Threat modeling identifies potential threats during the design phase, and "
        "vulnerability analysis examines the system for exploitable weaknesses. Together, "
        "they help you find and fix problems before attackers do.</p>"
        "<p><strong>Example 1:</strong> Conduct threat modeling for every new system or major "
        "feature using the STRIDE methodology: identify Spoofing, Tampering, Repudiation, "
        "Information Disclosure, Denial of Service, and Elevation of Privilege threats for "
        "each component. Document threats and mitigations in a threat model document.</p>"
        "<p><strong>Example 2:</strong> Use the Microsoft Threat Modeling Tool or OWASP Threat "
        "Dragon to create data flow diagrams and automatically identify threats at trust "
        "boundaries. For each identified threat, document whether it is mitigated by an "
        "existing control, needs a new control, or is accepted as a residual risk.</p>"
    ),

    "sa-11-3": (
        "<p>Have someone independent of the development team verify that the security test "
        "plans are adequate and that the test results are accurate. This prevents the 'grading "
        "your own homework' problem.</p>"
        "<p><strong>Example 1:</strong> Before accepting a vendor's claim that their product "
        "passed security testing, have your security team or an independent third party review "
        "the test plan and results. Verify that the tests covered the right attack scenarios "
        "and that the results demonstrate adequate security, not just that tests ran.</p>"
        "<p><strong>Example 2:</strong> For internal development, require the security team "
        "(separate from the development team) to review security test plans before testing "
        "begins and validate a sample of test results after testing completes. This independent "
        "verification ensures testing is thorough and results are trustworthy.</p>"
    ),

    "sa-11-4": (
        "<p>Manual code reviews have humans examine source code for security issues that "
        "automated tools may miss — logic errors, business logic flaws, race conditions, "
        "and design weaknesses.</p>"
        "<p><strong>Example 1:</strong> Require manual security-focused code reviews for "
        "all code that handles authentication, authorization, cryptography, user input "
        "processing, and sensitive data. Use an OWASP-based code review checklist to ensure "
        "reviewers check for common vulnerability patterns.</p>"
        "<p><strong>Example 2:</strong> In your Git workflow, require at least one security-"
        "trained reviewer to approve pull requests that touch security-sensitive code paths. "
        "Use CODEOWNERS files to automatically assign security reviewers when changes are "
        "made to authentication, encryption, or access control modules.</p>"
    ),

    "sa-11-5": (
        "<p>Penetration testing by the development team (or on behalf of the development team) "
        "tests the running application for vulnerabilities by simulating real attacks.</p>"
        "<p><strong>Example 1:</strong> Require the development team to conduct penetration "
        "testing before each major release. At minimum, test for the OWASP Top 10 "
        "vulnerabilities: injection, broken authentication, sensitive data exposure, XML "
        "external entities, broken access control, security misconfigurations, cross-site "
        "scripting, insecure deserialization, using components with known vulnerabilities, "
        "and insufficient logging.</p>"
        "<p><strong>Example 2:</strong> Use OWASP ZAP or Burp Suite in the CI/CD pipeline to "
        "run automated penetration tests against each staging deployment. Configure the tool "
        "to test for SQL injection, XSS, CSRF, and authentication bypass. Fail the deployment "
        "if critical findings are detected.</p>"
    ),

    "sa-11-6": (
        "<p>Attack surface reviews examine all the ways an attacker could potentially interact "
        "with your system — open ports, exposed APIs, user interfaces, file upload points — "
        "and work to reduce them.</p>"
        "<p><strong>Example 1:</strong> After each development sprint, review the application's "
        "attack surface: new endpoints, new input fields, new file handlers, new integrations. "
        "For each new surface area, verify that appropriate security controls (input validation, "
        "authentication, authorization) are in place.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Defender External Attack Surface "
        "Management to continuously discover and monitor your organization's internet-facing "
        "assets. The tool identifies exposed services, open ports, and vulnerable technologies "
        "from an attacker's perspective. Review findings weekly and eliminate unnecessary "
        "exposure.</p>"
    ),

    "sa-11-7": (
        "<p>Verify that the scope of security testing and evaluation actually covers the "
        "security requirements. Testing that misses critical areas provides false confidence.</p>"
        "<p><strong>Example 1:</strong> Create a traceability matrix that maps each security "
        "requirement to the test cases that validate it. Before accepting test results, verify "
        "that every requirement has at least one corresponding test case and that the test was "
        "actually executed with a pass result.</p>"
        "<p><strong>Example 2:</strong> In your CI/CD pipeline, implement code coverage "
        "metrics for security tests. Track what percentage of security-critical code paths "
        "are covered by automated tests. Set a minimum coverage threshold (e.g., 80% for "
        "security modules) and fail the build if coverage drops below it.</p>"
    ),

    "sa-11-8": (
        "<p>Dynamic code analysis (DAST) tests the running application by sending requests "
        "and examining responses. Unlike static analysis, it tests the application's actual "
        "behavior, including runtime configuration and environment-specific issues.</p>"
        "<p><strong>Example 1:</strong> Deploy a DAST tool (OWASP ZAP, Burp Suite Enterprise, "
        "Qualys WAS) to scan your web applications in a staging environment. Run authenticated "
        "scans that test behind the login page — most vulnerabilities are in authenticated "
        "functionality that surface-level scans never reach.</p>"
        "<p><strong>Example 2:</strong> Integrate DAST into your CI/CD pipeline. After deploying "
        "to a staging environment, automatically trigger an OWASP ZAP scan. Parse the results "
        "and fail the pipeline if critical or high findings are detected. This catches "
        "vulnerabilities in the running application before they reach production.</p>"
    ),

    "sa-11-9": (
        "<p>Interactive Application Security Testing (IAST) combines elements of SAST and DAST "
        "by instrumenting the running application to observe its behavior from the inside. "
        "This catches vulnerabilities that pure SAST or DAST might miss.</p>"
        "<p><strong>Example 1:</strong> Deploy an IAST agent (Contrast Security, HCL AppScan) "
        "in your test environment alongside your functional test suite. As functional tests "
        "exercise the application, the IAST agent monitors internal execution for security "
        "issues — data flows, tainted inputs, and unsafe function calls.</p>"
        "<p><strong>Example 2:</strong> Use IAST during your QA testing cycle so that security "
        "testing happens automatically as functional testers exercise the application. The IAST "
        "agent identifies vulnerabilities in real-time with precise code location and data flow "
        "information, making them faster and easier for developers to fix than traditional "
        "scan-based findings.</p>"
    ),

    "sa-12": (
        "<p>This control (moved to SR family in Rev 5) addresses supply chain protection — "
        "ensuring that the products and services you acquire are not compromised during "
        "development, manufacturing, or delivery.</p>"
        "<p><strong>Example 1:</strong> Implement a supply chain risk management program that "
        "evaluates vendors before purchase, monitors them during the relationship, and includes "
        "contractual provisions for security requirements, incident notification, and right to "
        "audit. Focus your efforts on vendors that provide critical or high-risk components.</p>"
        "<p><strong>Example 2:</strong> Require Software Bills of Materials (SBOMs) from "
        "software vendors and scan them for known vulnerabilities using tools like Dependabot "
        "or Snyk. Track vendor security advisories and apply patches within defined timelines. "
        "Verify the integrity of delivered products using digital signatures and checksums.</p>"
    ),

    "sa-12-1": (
        "<p>Use acquisition strategies, tools, and methods that reduce supply chain risk. "
        "Your purchasing process should include security as a selection criterion, not just "
        "price and features.</p>"
        "<p><strong>Example 1:</strong> Include security evaluation criteria in your RFP "
        "scoring rubric. Award points for vendors with SOC 2 Type II reports, ISO 27001 "
        "certification, FedRAMP authorization, or CMMC certification. Make security a "
        "weighted factor in vendor selection, not a pass/fail checkbox.</p>"
        "<p><strong>Example 2:</strong> Use GSA Schedule contracts or other vetted procurement "
        "vehicles when possible. Products available through these channels have already "
        "undergone some level of vendor vetting. For custom acquisitions, require vendors to "
        "complete a security questionnaire and provide evidence of secure development "
        "practices before being considered.</p>"
    ),

    "sa-12-2": (
        "<p>Conduct regular reviews of your suppliers to verify they continue to meet your "
        "security requirements throughout the relationship, not just at contract signing.</p>"
        "<p><strong>Example 1:</strong> Schedule annual security reviews for all critical "
        "vendors. Request updated SOC 2 reports, review their recent security incident "
        "history, and verify that contractual security requirements are still being met. "
        "Document findings and follow up on any concerns.</p>"
        "<p><strong>Example 2:</strong> Use a vendor risk management platform (BitSight, "
        "SecurityScorecard) that continuously monitors your suppliers' external security "
        "posture. These platforms track things like exposed services, SSL certificate status, "
        "and data breach history, giving you early warning of declining vendor security.</p>"
    ),

    "sa-12-3": (
        "<p>Protect the supply chain during shipping and warehousing to ensure products are "
        "not tampered with between the manufacturer and your facility.</p>"
        "<p><strong>Example 1:</strong> For critical hardware components, specify secure "
        "shipping requirements in your procurement contracts: tamper-evident packaging, "
        "tracked shipping, and direct shipment from the manufacturer (not through "
        "intermediaries). Inspect packaging on receipt for signs of tampering.</p>"
        "<p><strong>Example 2:</strong> When warehousing IT equipment before deployment, "
        "store it in a physically secured area with access controls and surveillance cameras. "
        "Maintain a chain of custody log that records who handled the equipment from receipt "
        "through deployment.</p>"
    ),

    "sa-12-4": (
        "<p>Using multiple suppliers for critical components reduces the risk of a single "
        "supplier compromise affecting your entire operation. Diversity in your supply chain "
        "builds resilience.</p>"
        "<p><strong>Example 1:</strong> Identify components and services where you depend on "
        "a single supplier. For each one, evaluate whether a viable alternative exists. "
        "Maintain a secondary vendor for your most critical components so that if your "
        "primary vendor is compromised or unavailable, you have a fallback option.</p>"
        "<p><strong>Example 2:</strong> For software components, avoid depending on a single "
        "open-source library or vendor SDK when alternatives exist. If a critical library is "
        "compromised (as in the SolarWinds or Log4j incidents), having familiarity with "
        "alternatives lets you switch more quickly.</p>"
    ),

    "sa-12-5": (
        "<p>Limit the potential harm from a supply chain compromise by reducing the access "
        "and privileges granted to vendor-supplied components and services.</p>"
        "<p><strong>Example 1:</strong> Run vendor-supplied software with minimum privileges. "
        "If a monitoring agent only needs read access to system metrics, do not give it "
        "administrator access. Apply the principle of least privilege to vendor service "
        "accounts, network access, and data permissions.</p>"
        "<p><strong>Example 2:</strong> Segment vendor-supplied systems on your network so "
        "that a compromise of one vendor's product does not give the attacker access to your "
        "entire environment. Place vendor management consoles and agent communication channels "
        "on a dedicated management VLAN with restricted access to production systems.</p>"
    ),

    "sa-12-6": (
        "<p>Minimize the time between ordering and deploying IT components to reduce the "
        "window during which products could be intercepted or tampered with in the supply "
        "chain.</p>"
        "<p><strong>Example 1:</strong> For critical security components (firewalls, HSMs, "
        "encryption appliances), order directly from the manufacturer with expedited shipping "
        "rather than using slow distribution channels. The less time a device spends in "
        "transit and warehousing, the less opportunity for tampering.</p>"
        "<p><strong>Example 2:</strong> Maintain a small inventory of critical spare parts "
        "on-site so that replacements can be deployed immediately rather than waiting for "
        "procurement and shipping cycles. Store spares in a secure, access-controlled "
        "location with inventory tracking.</p>"
    ),

    "sa-12-7": (
        "<p>Assess the security of components before selecting them, before accepting delivery, "
        "and before installing updates. Each stage is an opportunity for compromise.</p>"
        "<p><strong>Example 1:</strong> Before selecting a new software component, review "
        "its security track record: check CVE databases for past vulnerabilities, review "
        "the vendor's patching history, and evaluate their security certifications. A product "
        "with a history of critical vulnerabilities and slow patches is a higher risk.</p>"
        "<p><strong>Example 2:</strong> Before installing vendor updates, verify the update's "
        "digital signature and hash against the vendor's published values. Test updates in a "
        "non-production environment first to verify they do not introduce security regressions. "
        "Only deploy to production after successful testing.</p>"
    ),

    "sa-12-8": (
        "<p>Use all-source intelligence to inform supply chain risk decisions. Threat "
        "intelligence about vendor compromises, nation-state targeting of supply chains, and "
        "counterfeit component risks should factor into your procurement decisions.</p>"
        "<p><strong>Example 1:</strong> Before procuring critical components, check government "
        "advisories and sanctions lists to verify the manufacturer is not a known supply chain "
        "risk. CISA, NSA, and FBI regularly publish advisories about compromised supply chains "
        "and vendors with known security concerns.</p>"
        "<p><strong>Example 2:</strong> Subscribe to supply chain threat intelligence feeds "
        "specific to your industry. For defense contractors, the DIB ISAC and DCSA provide "
        "intelligence about supply chain threats targeting the defense industrial base. Use "
        "this intelligence to adjust your vendor risk assessments and procurement decisions.</p>"
    ),

    "sa-12-9": (
        "<p>Apply operations security (OPSEC) to your supply chain processes. Information "
        "about your security infrastructure, deployment schedules, and vendor relationships "
        "should not be publicly available.</p>"
        "<p><strong>Example 1:</strong> Do not publicly disclose specific security products "
        "and versions in use (e.g., on job postings, social media, or website metadata). "
        "Attackers use this information to tailor their attacks to your specific technology "
        "stack. Keep infrastructure details internal.</p>"
        "<p><strong>Example 2:</strong> When communicating with vendors about security "
        "requirements, use secure channels (encrypted email, secure portals) rather than "
        "standard email. Sensitive procurement details, security architecture information, "
        "and vulnerability data should never travel over unprotected channels.</p>"
    ),

    "sa-12-10": (
        "<p>Validate that components and products are genuine and have not been altered before "
        "deploying them. Counterfeit or tampered components are a serious supply chain risk.</p>"
        "<p><strong>Example 1:</strong> Verify hardware serial numbers and firmware versions "
        "against the manufacturer's records before deployment. For critical components, "
        "contact the manufacturer to confirm the serial number matches their production "
        "records and has not been reported as counterfeit or stolen.</p>"
        "<p><strong>Example 2:</strong> For software, verify digital signatures and file "
        "hashes before installation. Use the vendor's official download site or authenticated "
        "package repository, not third-party mirror sites. Configure your package managers "
        "(apt, yum, npm) to verify signatures automatically.</p>"
    ),

    "sa-12-11": (
        "<p>Conduct penetration testing not just of your own systems, but also analyze the "
        "supply chain elements, processes, and actors that deliver products and services to "
        "your organization.</p>"
        "<p><strong>Example 1:</strong> Include supply chain attack scenarios in your "
        "penetration test scope. Can a tester compromise a vendor portal and inject malicious "
        "code into an update? Can they intercept communications between you and a supplier? "
        "These tests reveal real-world supply chain attack paths.</p>"
        "<p><strong>Example 2:</strong> Evaluate the security of vendor portals and integration "
        "points as part of your regular security assessments. Test the authentication, "
        "encryption, and access controls on any system where you exchange data or software "
        "with vendors. Findings should be shared with the vendor for remediation.</p>"
    ),

    "sa-12-12": (
        "<p>Use inter-organizational agreements to establish supply chain security requirements "
        "with your partners and suppliers. Agreements formalize expectations and provide "
        "accountability.</p>"
        "<p><strong>Example 1:</strong> Execute Interconnection Security Agreements (ISAs) or "
        "Memoranda of Understanding (MOUs) with organizations that connect to your systems. "
        "These agreements should specify security requirements, incident notification "
        "procedures, and responsibilities for each party.</p>"
        "<p><strong>Example 2:</strong> Include supply chain security clauses in all vendor "
        "contracts: requirements for reporting security incidents, obligation to notify you "
        "of subcontractor changes, and the right to audit their security practices. Review "
        "and update these clauses annually as threats evolve.</p>"
    ),

    "sa-12-13": (
        "<p>Identify and apply enhanced protections to critical information system components — "
        "the parts of your infrastructure that, if compromised, would have the most severe "
        "impact on your mission.</p>"
        "<p><strong>Example 1:</strong> Identify your critical components (domain controllers, "
        "certificate authorities, key management servers, core network switches) and apply "
        "enhanced supply chain protections: buy only from authorized resellers, verify "
        "authenticity before deployment, and monitor them more closely during operation.</p>"
        "<p><strong>Example 2:</strong> Maintain a critical components registry that lists each "
        "critical component, its vendor, supply chain risk rating, and the enhanced protections "
        "applied. Review this registry semiannually and update it when your infrastructure "
        "changes or new threats emerge.</p>"
    ),

    "sa-12-14": (
        "<p>Establish identity and traceability for critical components throughout the supply "
        "chain. You need to know where a component came from, who handled it, and where it "
        "ended up in your environment.</p>"
        "<p><strong>Example 1:</strong> Maintain a chain of custody record for critical hardware "
        "from purchase through deployment. Track the component from the manufacturer through "
        "shipping, receiving, storage, and installation. Include serial numbers, dates, and "
        "the names of personnel who handled the component at each stage.</p>"
        "<p><strong>Example 2:</strong> For software components, maintain an SBOM that traces "
        "each component to its source. Track the provenance of open-source libraries (which "
        "repository, which version, which maintainer) so that if a supply chain compromise is "
        "discovered, you can quickly determine if your systems are affected.</p>"
    ),

    "sa-12-15": (
        "<p>Establish processes to address weaknesses and deficiencies found in supply chain "
        "components after they are deployed. This includes vulnerability management for "
        "vendor-supplied products and processes for handling recalls or advisories.</p>"
        "<p><strong>Example 1:</strong> Subscribe to security advisories from all your "
        "hardware and software vendors. When a vulnerability is disclosed in a vendor product, "
        "assess its applicability to your environment, determine the risk, and patch or "
        "mitigate within defined timelines based on severity.</p>"
        "<p><strong>Example 2:</strong> Maintain a process for handling vendor product recalls "
        "or emergency advisories. When CISA issues an Emergency Directive affecting a product "
        "in your environment, have a documented process for rapid assessment, mitigation, "
        "and reporting — including notifying leadership and updating your risk register.</p>"
    ),

    "sa-13": (
        "<p>This control (withdrawn and incorporated into SA-8) addresses the trustworthiness "
        "of information systems — the degree to which they can be trusted to operate correctly "
        "and protect information as intended.</p>"
        "<p><strong>Example 1:</strong> Evaluate the trustworthiness of your systems by "
        "considering the security engineering principles used in their design, the rigor of "
        "their development process, and the thoroughness of their testing. Systems built with "
        "more rigorous processes deserve higher trust.</p>"
        "<p><strong>Example 2:</strong> Document the assurance level required for each system "
        "based on its criticality and the sensitivity of data it processes. A high-assurance "
        "system might require formal verification of security properties, while a low-assurance "
        "system might only require standard development practices and testing.</p>"
    ),

    "sa-14": (
        "<p>Criticality analysis for acquired systems and services identifies which components "
        "are most critical to your mission and therefore require the most careful acquisition "
        "and supply chain protection.</p>"
        "<p><strong>Example 1:</strong> Before acquiring new systems, conduct a criticality "
        "analysis that evaluates how mission-critical each component is. A firewall protecting "
        "your CUI enclave is more critical than a printer in the break room — and the "
        "acquisition process for each should reflect that difference in criticality.</p>"
        "<p><strong>Example 2:</strong> Map acquired components to your mission functions "
        "and identify dependencies. If your email system goes down, which mission functions "
        "are affected and for how long? Use this analysis to prioritize which vendor "
        "relationships need the most oversight and which components need the fastest "
        "replacement options.</p>"
    ),

    "sa-14-1": (
        "<p>When critical components have no viable alternative source, you face a concentrated "
        "supply chain risk. If that sole-source vendor is compromised, you have no fallback.</p>"
        "<p><strong>Example 1:</strong> Identify all sole-source components in your environment "
        "and document the risk. If only one vendor makes the specialized software your mission "
        "depends on, develop a contingency plan: maintain stockpiles, negotiate source code "
        "escrow agreements, or invest in developing an internal alternative.</p>"
        "<p><strong>Example 2:</strong> For critical components with no alternative, negotiate "
        "enhanced contract terms: source code escrow, enhanced security requirements, priority "
        "support, and the right to independent security assessments. Monitor the vendor's "
        "financial and security health more closely than you would a vendor with alternatives.</p>"
    ),

    "sa-15": (
        "<p>Require developers (internal and vendor) to follow defined development processes, "
        "standards, and tools that include security. Ad-hoc development without standards "
        "produces inconsistent and insecure results.</p>"
        "<p><strong>Example 1:</strong> Establish a development standards document that "
        "specifies: approved programming languages, secure coding standards (OWASP, CERT), "
        "required development tools (IDE, version control, SAST/DAST tools), and mandatory "
        "security activities at each development phase. All development teams, internal and "
        "vendor, must follow these standards.</p>"
        "<p><strong>Example 2:</strong> In your CI/CD pipeline, enforce standards through "
        "automation: linters check coding standards, SAST tools check security, dependency "
        "scanners check for vulnerable libraries, and build pipelines enforce branch "
        "protection rules. Code that does not meet standards cannot be merged or deployed.</p>"
    ),

    "sa-15-1": (
        "<p>Define and track quality metrics for your development process, including metrics "
        "that indicate the security quality of the code being produced.</p>"
        "<p><strong>Example 1:</strong> Track security-relevant quality metrics: number of "
        "security findings per release, time to fix security findings, percentage of findings "
        "found by automated tools vs. manual review, and escaped defects (security issues "
        "found in production that should have been caught in development).</p>"
        "<p><strong>Example 2:</strong> Use your SAST tool's reporting features to trend "
        "security findings over time. If the number of critical findings per 1,000 lines of "
        "code is increasing, it indicates a quality problem in the development process. Set "
        "targets for improvement and track progress in your development metrics dashboard.</p>"
    ),

    "sa-15-2": (
        "<p>Use tracking tools to manage security and privacy requirements, findings, and "
        "remediation throughout the development process.</p>"
        "<p><strong>Example 1:</strong> Use Azure DevOps Work Items or Jira tickets to track "
        "security requirements alongside functional requirements. Tag security-related items "
        "so they can be filtered and reported on separately. Track each security requirement "
        "through design, implementation, testing, and verification.</p>"
        "<p><strong>Example 2:</strong> Configure your SAST/DAST tools to automatically create "
        "tickets in your issue tracker when new findings are detected. This ensures findings "
        "enter the development workflow automatically and are tracked through resolution, "
        "rather than sitting in a scanner report that nobody reads.</p>"
    ),

    "sa-15-3": (
        "<p>Apply criticality analysis to the development process — the most critical "
        "components should receive the most rigorous development practices, testing, and "
        "review.</p>"
        "<p><strong>Example 1:</strong> Classify software components by criticality: security-"
        "critical code (authentication, encryption, access control) gets the most rigorous "
        "review and testing. Standard business logic gets normal review. Non-critical utility "
        "code gets minimal review. This focuses your limited security review resources where "
        "they matter most.</p>"
        "<p><strong>Example 2:</strong> Document the required development rigor for each "
        "criticality level in your development standards: critical components require threat "
        "modeling, manual code review, and penetration testing; important components require "
        "SAST scanning and code review; standard components require SAST scanning only.</p>"
    ),

    "sa-15-4": (
        "<p>Apply threat modeling and vulnerability analysis during the development process "
        "to proactively identify and address security issues before they become deployed "
        "vulnerabilities.</p>"
        "<p><strong>Example 1:</strong> Require threat modeling during the design phase of "
        "every project. Use STRIDE or PASTA methodology to identify threats, and use the "
        "results to drive security requirements and test cases. A feature that is released "
        "without threat modeling is more likely to have unaddressed security risks.</p>"
        "<p><strong>Example 2:</strong> During development, run regular vulnerability analysis "
        "using SAST tools, dependency checks, and manual review. Compare findings against the "
        "threat model to verify that identified threats have been mitigated. If the threat "
        "model predicted an injection risk and the SAST tool finds an injection vulnerability, "
        "the threat model was right and the mitigation was incomplete.</p>"
    ),

    "sa-15-5": (
        "<p>Actively work to reduce the attack surface of systems during development. Every "
        "unnecessary feature, open port, and exposed interface is potential attack surface "
        "that must be defended.</p>"
        "<p><strong>Example 1:</strong> During design reviews, challenge every exposed "
        "interface: Does this API endpoint need to be public? Does this feature need to be "
        "enabled by default? Can we reduce the permissions this service needs? Remove every "
        "interface, feature, and privilege that is not explicitly required.</p>"
        "<p><strong>Example 2:</strong> Use container images with minimal base images (Alpine "
        "Linux, distroless) rather than full OS images. A minimal image has fewer installed "
        "packages, fewer potential vulnerabilities, and a smaller attack surface. Scan your "
        "container images with Trivy or Snyk to identify and remove unnecessary components.</p>"
    ),

    "sa-15-6": (
        "<p>Continuously improve your development process by learning from security findings, "
        "incidents, and industry best practices. The development process should get more "
        "secure over time, not stay static.</p>"
        "<p><strong>Example 1:</strong> After each release, conduct a security retrospective "
        "that reviews: what security findings were discovered during development, how long "
        "they took to fix, whether any escaped to production, and what process improvements "
        "would prevent similar issues in the future. Implement the improvements in the next "
        "sprint.</p>"
        "<p><strong>Example 2:</strong> Track your security metrics over time and set "
        "improvement targets. If you found 50 high-severity issues per release last year, "
        "target 30 this year through improved training, better tools, and earlier security "
        "reviews. Celebrate improvements and investigate regressions.</p>"
    ),

    "sa-15-7": (
        "<p>Use automated tools to continuously analyze code for vulnerabilities rather than "
        "relying solely on periodic manual reviews. Automation catches common issues "
        "consistently and at scale.</p>"
        "<p><strong>Example 1:</strong> Integrate automated vulnerability scanning into every "
        "stage of your pipeline: pre-commit hooks check for secrets, pull request checks run "
        "SAST analysis, build pipelines scan dependencies, and deployment pipelines run DAST. "
        "Each stage catches different types of issues automatically.</p>"
        "<p><strong>Example 2:</strong> Use GitHub Advanced Security or GitLab Ultimate with "
        "built-in SAST, secret detection, and dependency scanning. Configure these tools to "
        "run on every commit and create automatic security alerts. Review and triage findings "
        "daily rather than waiting for periodic scan reports.</p>"
    ),

    "sa-15-8": (
        "<p>Reuse threat and vulnerability information from previous projects, industry "
        "databases, and external sources to improve the security of new development. Do not "
        "start every project's threat analysis from scratch.</p>"
        "<p><strong>Example 1:</strong> Maintain a lessons-learned database that records "
        "vulnerability patterns found in previous projects. If SQL injection has been found "
        "in three past projects, new projects should specifically test for it and use "
        "parameterized queries from the start.</p>"
        "<p><strong>Example 2:</strong> Use MITRE CWE (Common Weakness Enumeration) and "
        "OWASP Top 10 as starting points for threat modeling and testing. These curated lists "
        "represent the most common vulnerability patterns and save you from rediscovering "
        "well-known risks. Map your coding standards and test cases directly to these "
        "references.</p>"
    ),

    "sa-15-9": (
        "<p>Limit the use of live (production) data in development and test environments. "
        "Real data in non-production environments exposes it to weaker controls and "
        "broader access.</p>"
        "<p><strong>Example 1:</strong> Establish a policy that requires approval and data "
        "masking before production data can be used in development or testing. If live data "
        "is absolutely necessary for a specific test scenario, create a time-limited exception "
        "with a specific purge date for when the data must be removed from the test "
        "environment.</p>"
        "<p><strong>Example 2:</strong> Invest in synthetic data generation tools that create "
        "realistic test data without using real information. For database testing, use tools "
        "that generate fake but realistic names, addresses, and other data elements that "
        "exercise the same code paths as real data without the privacy risk.</p>"
    ),

    "sa-15-10": (
        "<p>Developers should have an incident response plan specific to their development "
        "environment and products. If a development environment is compromised or a "
        "vulnerability is found in deployed code, the team needs a clear response plan.</p>"
        "<p><strong>Example 1:</strong> Create a development-specific incident response plan "
        "that addresses: compromised developer credentials, malicious code injected into the "
        "repository, compromised build pipeline, and zero-day vulnerabilities in deployed "
        "products. Define who responds, how code is rolled back, and how customers are "
        "notified.</p>"
        "<p><strong>Example 2:</strong> Conduct tabletop exercises with your development team "
        "simulating scenarios like a compromised npm package in your dependencies, a developer "
        "laptop infected with malware, or a critical vulnerability reported by a security "
        "researcher. Practice the response and refine the plan based on lessons learned.</p>"
    ),

    "sa-15-11": (
        "<p>Archive system configurations, code, and documentation when decommissioning "
        "systems so that historical information is available for future reference, legal "
        "proceedings, or forensic analysis.</p>"
        "<p><strong>Example 1:</strong> Before decommissioning a system, create a complete "
        "archive: final configuration backup, source code snapshot (tagged in version control), "
        "system security plan, all assessment reports, and incident records. Store the archive "
        "in a secure, accessible location with a defined retention period.</p>"
        "<p><strong>Example 2:</strong> In Azure DevOps, tag the final release of decommissioned "
        "projects and archive the repository. Retain build artifacts and deployment logs for "
        "the period required by your records retention policy. Document the archive location "
        "and contents in your system inventory so future staff can locate it if needed.</p>"
    ),

    "sa-15-12": (
        "<p>Minimize the collection and use of personally identifiable information in the "
        "development process. Developers should not need access to real PII to do their work.</p>"
        "<p><strong>Example 1:</strong> Prohibit developers from using real PII in test data, "
        "debug logs, or development documentation. Establish synthetic data standards and "
        "provide developers with tools and libraries for generating realistic test data "
        "without real personal information.</p>"
        "<p><strong>Example 2:</strong> Configure your logging framework to automatically "
        "redact PII from log output. Instead of logging 'User John Smith (SSN: 123-45-6789) "
        "logged in,' the log should show 'User [REDACTED] (SSN: ***-**-6789) logged in.' "
        "Implement this at the framework level so individual developers do not have to "
        "remember to redact.</p>"
    ),

    "sa-15-13": (
        "<p>Standardize your logging syntax across all systems and applications so that logs "
        "from different sources can be correlated and analyzed together. Inconsistent log "
        "formats make security analysis difficult.</p>"
        "<p><strong>Example 1:</strong> Define a standard log format for all applications: "
        "include timestamp (ISO 8601), severity level, source application, event type, user "
        "identity, source IP, and event description. Use structured logging (JSON format) "
        "so logs are machine-parseable.</p>"
        "<p><strong>Example 2:</strong> Use a centralized logging framework (Serilog, Log4j, "
        "Winston) with organization-defined templates that enforce your standard format. "
        "Configure your SIEM (Microsoft Sentinel) with parsers that understand your standard "
        "format and can automatically correlate events across different applications.</p>"
    ),

    "sa-16": (
        "<p>Require developers to provide training for administrators and users of the systems "
        "they build or sell. Without proper training, even secure systems will be operated "
        "insecurely.</p>"
        "<p><strong>Example 1:</strong> Include training requirements in contracts with system "
        "developers and vendors. The vendor should provide administrator training covering "
        "security configuration, account management, log review, patch management, and "
        "incident response specific to their product.</p>"
        "<p><strong>Example 2:</strong> For internally developed systems, have the development "
        "team create training materials and conduct knowledge transfer sessions with the "
        "operations team before handoff. Cover security architecture, common attack scenarios, "
        "hardening procedures, and how to recognize and respond to security events specific "
        "to the application.</p>"
    ),

    "sa-17": (
        "<p>Require developers to produce and maintain a security architecture and design "
        "document that describes how the system implements security requirements. The "
        "architecture should be designed before code is written.</p>"
        "<p><strong>Example 1:</strong> Require a security architecture document for every "
        "new system that covers: trust boundaries, authentication and authorization design, "
        "encryption strategy, audit logging approach, network segmentation, and data flow "
        "diagrams showing where sensitive data is processed, stored, and transmitted.</p>"
        "<p><strong>Example 2:</strong> Use architecture review boards that include security "
        "expertise to evaluate designs before development begins. Review proposed architectures "
        "against NIST, OWASP, and organization-specific security standards. Document review "
        "findings and require resolution before development proceeds.</p>"
    ),

    "sa-17-1": (
        "<p>For high-assurance systems, require a formal policy model that mathematically "
        "describes the security properties the system must enforce. This provides the "
        "strongest basis for verifying that the system behaves correctly.</p>"
        "<p><strong>Example 1:</strong> For systems requiring high assurance (e.g., those "
        "processing Top Secret information), require the developer to provide a formal "
        "security policy model (such as Bell-LaPadula for confidentiality or Biba for "
        "integrity) and demonstrate that the system's design enforces the model.</p>"
        "<p><strong>Example 2:</strong> Use formal methods tools (TLA+, Alloy, Z notation) "
        "to specify and verify critical security properties of the system. While formal "
        "methods are resource-intensive, they provide mathematical certainty that the "
        "system's security properties hold under all conditions.</p>"
    ),

    "sa-17-2": (
        "<p>Identify and isolate the security-relevant components of a system so they can "
        "be analyzed, tested, and protected more rigorously than the rest of the system.</p>"
        "<p><strong>Example 1:</strong> In your system architecture, clearly identify which "
        "components are security-relevant: authentication modules, access control engines, "
        "encryption services, audit logging, and key management. These components should be "
        "documented separately and receive more rigorous code review and testing.</p>"
        "<p><strong>Example 2:</strong> Isolate security-relevant code into separate modules "
        "or microservices so they can be independently updated, tested, and audited. A change "
        "to the authentication service should not require retesting the entire application, "
        "and a vulnerability in a business logic module should not directly compromise the "
        "authentication service.</p>"
    ),

    "sa-17-3": (
        "<p>Demonstrate formal correspondence between the security policy model, the "
        "high-level design, and the implementation. Each layer should provably implement the "
        "layer above it.</p>"
        "<p><strong>Example 1:</strong> For high-assurance systems, provide a mapping document "
        "that traces each element of the formal security policy to its implementation in the "
        "high-level design, and from the design to specific code modules. An evaluator should "
        "be able to verify that every security policy requirement is addressed at every level.</p>"
        "<p><strong>Example 2:</strong> Use automated verification tools to check that the "
        "implementation matches the design specification. Contract language should require "
        "the developer to demonstrate this correspondence as part of their security "
        "evaluation deliverables.</p>"
    ),

    "sa-17-4": (
        "<p>Even without formal mathematical proofs, provide clear informal arguments that "
        "demonstrate the design implements the security policy. This is appropriate for "
        "systems that do not require the highest assurance levels.</p>"
        "<p><strong>Example 1:</strong> Create a security design rationale document that "
        "explains, in plain technical language, how each security requirement is addressed "
        "by the design. 'To prevent unauthorized access, the system uses role-based access "
        "control implemented through Azure AD groups, with permissions checked at every API "
        "endpoint.'</p>"
        "<p><strong>Example 2:</strong> During design reviews, walk through each security "
        "requirement and demonstrate informally (with diagrams, data flow analysis, and code "
        "walkthrough) that the implementation addresses it. Document the review findings and "
        "any gaps identified for remediation.</p>"
    ),

    "sa-17-5": (
        "<p>Keep the security design as simple as possible. A simpler design is easier to "
        "analyze for correctness, easier to implement without errors, and easier to audit.</p>"
        "<p><strong>Example 1:</strong> During architecture reviews, push for the simplest "
        "security design that meets requirements. If the same security goal can be achieved "
        "with a single centralized access control layer or a complex distributed system, "
        "choose the centralized approach — it is easier to verify and harder to misconfigure.</p>"
        "<p><strong>Example 2:</strong> Limit the number of different authentication and "
        "authorization mechanisms in your environment. Rather than having each application "
        "implement its own authentication, centralize through Azure AD with SSO. One "
        "well-implemented mechanism is more secure than ten different implementations.</p>"
    ),

    "sa-17-6": (
        "<p>Design the system in a way that facilitates thorough security testing. If a "
        "system's architecture makes testing difficult, important security properties will "
        "go unverified.</p>"
        "<p><strong>Example 1:</strong> Design applications with testability in mind: separate "
        "security logic from business logic so security functions can be unit-tested "
        "independently, expose health check and diagnostic endpoints (protected by "
        "authentication), and support running in a test mode that allows security testing "
        "without affecting production data.</p>"
        "<p><strong>Example 2:</strong> Provide test harnesses and mock services that allow "
        "security testers to exercise security functions in isolation. For example, provide "
        "a test authentication service that returns configurable responses so testers can "
        "verify how the application handles various authentication failures.</p>"
    ),

    "sa-17-7": (
        "<p>Structure the system's architecture to facilitate implementing least privilege. "
        "The architecture should make it easy to grant minimum necessary access and hard to "
        "accidentally grant excessive access.</p>"
        "<p><strong>Example 1:</strong> Design your application with granular permission models "
        "from the start. Each API endpoint should have a well-defined permission requirement, "
        "and roles should be composed of specific, minimal permission sets. Avoid broad "
        "permissions like 'admin' that grant access to everything.</p>"
        "<p><strong>Example 2:</strong> In your infrastructure, use network microsegmentation "
        "to enforce least privilege at the network level. Each service should only be able to "
        "communicate with the specific services it depends on. Use Kubernetes NetworkPolicies "
        "or Azure NSGs to enforce this at the network layer.</p>"
    ),

    "sa-17-8": (
        "<p>Design for orchestration — the ability to coordinate security controls across "
        "multiple systems and components to provide a unified security posture.</p>"
        "<p><strong>Example 1:</strong> Design your security architecture with central "
        "orchestration in mind. Use a SIEM (Microsoft Sentinel) as the central hub that "
        "receives data from all security controls (endpoint protection, firewalls, identity "
        "systems) and orchestrates responses through SOAR playbooks.</p>"
        "<p><strong>Example 2:</strong> Implement security orchestration through Azure Logic "
        "Apps or Microsoft Sentinel playbooks. When an identity risk is detected (impossible "
        "travel, credential leak), the orchestration automatically disables the account, "
        "revokes active sessions, notifies the security team, and creates an incident ticket "
        "— all without manual intervention.</p>"
    ),

    "sa-17-9": (
        "<p>Design diversity means using different technologies and approaches for redundant "
        "security controls, so that a single vulnerability does not compromise all layers "
        "of defense.</p>"
        "<p><strong>Example 1:</strong> Use different vendors or technologies for different "
        "layers of network defense. If your perimeter firewall is from Vendor A, use Vendor "
        "B for your internal IDS/IPS. A zero-day vulnerability affecting Vendor A's product "
        "will not simultaneously compromise your internal monitoring.</p>"
        "<p><strong>Example 2:</strong> Use different antivirus/EDR engines for different "
        "parts of your environment. Email scanning might use one engine, endpoint protection "
        "another, and your network sandbox a third. Malware designed to evade one engine is "
        "more likely to be caught by a different one.</p>"
    ),

    "sa-18": (
        "<p>For systems that require high assurance, implement tamper resistance (making "
        "tampering difficult) and tamper detection (detecting when tampering has occurred). "
        "This applies to both hardware and software.</p>"
        "<p><strong>Example 1:</strong> Deploy hardware security modules (HSMs) for "
        "cryptographic key storage. HSMs are designed with tamper-resistant enclosures that "
        "destroy the keys if physical tampering is detected. This protects your most "
        "sensitive cryptographic material even if an attacker gains physical access.</p>"
        "<p><strong>Example 2:</strong> Implement file integrity monitoring (FIM) using tools "
        "like OSSEC, Tripwire, or Microsoft Defender for Endpoint to detect unauthorized "
        "changes to critical system files, configuration files, and application binaries. "
        "When a change is detected outside of an approved change window, generate an "
        "immediate alert.</p>"
    ),

    "sa-18-1": (
        "<p>Apply tamper resistance and detection measures at multiple phases of the system "
        "development lifecycle, not just at deployment. This protects the system during "
        "development, testing, shipping, and operation.</p>"
        "<p><strong>Example 1:</strong> Protect your development environment with the same "
        "rigor as production. Implement code signing so that code cannot be modified between "
        "development and deployment without detection. Use secure build pipelines that log "
        "every build step and verify build artifact integrity.</p>"
        "<p><strong>Example 2:</strong> Implement integrity verification at each handoff "
        "point: from development to testing (signed builds), from testing to staging "
        "(verified artifacts), from staging to production (hash verification). Any integrity "
        "failure at any stage stops the deployment and triggers an investigation.</p>"
    ),

    "sa-18-2": (
        "<p>Physically or logically inspect systems and components for evidence of tampering. "
        "Periodic inspection catches issues that automated monitoring might miss.</p>"
        "<p><strong>Example 1:</strong> Conduct periodic physical inspections of critical "
        "hardware: check for unauthorized modifications, additional devices (keyloggers, "
        "rogue network taps), and broken tamper-evident seals. Document each inspection "
        "with the date, inspector name, and findings.</p>"
        "<p><strong>Example 2:</strong> For software, periodically compare deployed binaries "
        "against known-good versions from your build pipeline. Use file hash comparison to "
        "verify that what is running in production exactly matches what was approved through "
        "your change management process.</p>"
    ),

    "sa-19": (
        "<p>Verify that system components are authentic and not counterfeit. Counterfeit "
        "components may contain backdoors, malware, or simply fail when you need them most.</p>"
        "<p><strong>Example 1:</strong> Purchase IT equipment only from authorized resellers "
        "or directly from manufacturers. Verify component authenticity by checking serial "
        "numbers against manufacturer databases before deployment. Report any suspected "
        "counterfeits to the manufacturer and appropriate authorities.</p>"
        "<p><strong>Example 2:</strong> Implement anti-counterfeit procedures in your "
        "procurement process: require certificates of authenticity from vendors, verify "
        "firmware versions against manufacturer specifications, and use hardware "
        "authentication features (like TPM attestation) to verify component integrity "
        "during system boot.</p>"
    ),

    "sa-19-1": (
        "<p>Train personnel responsible for acquisition and deployment to recognize counterfeit "
        "components. Awareness is the first line of defense against counterfeits.</p>"
        "<p><strong>Example 1:</strong> Provide anti-counterfeit awareness training to your "
        "procurement, receiving, and IT staff. Cover how to identify common indicators of "
        "counterfeit products: misspelled labels, inconsistent serial numbers, different "
        "packaging than expected, and suspiciously low prices from unauthorized sellers.</p>"
        "<p><strong>Example 2:</strong> Share industry resources on counterfeit IT components, "
        "such as reports from GIDEP (Government-Industry Data Exchange Program) and SAE "
        "International counterfeit avoidance standards. Require receiving staff to follow a "
        "verification checklist for every hardware delivery.</p>"
    ),

    "sa-19-2": (
        "<p>Maintain configuration control over components when they are sent out for service "
        "or repair. A component that leaves your facility for repair could be tampered with "
        "or swapped during the repair process.</p>"
        "<p><strong>Example 1:</strong> Before sending equipment for service, record the "
        "component's serial number, firmware version, and configuration. When it returns, "
        "verify these match. If the firmware version has changed, investigate before "
        "redeploying. Maintain a chain of custody log for all equipment sent for external "
        "repair.</p>"
        "<p><strong>Example 2:</strong> For critical components, prefer on-site repair by "
        "cleared or vetted technicians over sending equipment off-site. If off-site repair "
        "is necessary, use only manufacturer-authorized service centers and require the "
        "service center to document all changes made during repair.</p>"
    ),

    "sa-19-3": (
        "<p>Dispose of system components securely to prevent data leakage and ensure that "
        "decommissioned equipment cannot be repurposed to attack your organization.</p>"
        "<p><strong>Example 1:</strong> Sanitize storage media before disposal using NIST "
        "SP 800-88 guidelines: clear for low-sensitivity media, purge for moderate, and "
        "destroy for high-sensitivity. Document the sanitization method, date, and personnel "
        "who performed it. Keep sanitization certificates for your records.</p>"
        "<p><strong>Example 2:</strong> For equipment that cannot be adequately sanitized "
        "(like SSDs with wear leveling that prevents complete data erasure), physically "
        "destroy the component using an approved method: shredding, degaussing (for magnetic "
        "media), or incineration. Use a certified destruction vendor and obtain a certificate "
        "of destruction for each batch.</p>"
    ),

    "sa-19-4": (
        "<p>Use automated scanning tools to detect counterfeit components during receiving "
        "inspection. Automated scanning is more consistent and thorough than visual "
        "inspection alone.</p>"
        "<p><strong>Example 1:</strong> For critical hardware components, use electronic "
        "testing equipment to verify component authenticity: X-ray inspection for circuit "
        "boards, firmware extraction and comparison for embedded systems, and automated "
        "serial number verification against manufacturer databases.</p>"
        "<p><strong>Example 2:</strong> For software components, automate authenticity "
        "verification: validate digital signatures against the publisher's known signing "
        "certificate, verify file hashes against the vendor's published checksums, and scan "
        "binaries for known malware signatures before deployment. Integrate these checks into "
        "your automated deployment pipeline.</p>"
    ),

    "sa-20": (
        "<p>When standard commercial products cannot meet your security requirements for "
        "critical functions, consider custom development. Customized components can be "
        "tailored to your exact security needs.</p>"
        "<p><strong>Example 1:</strong> Identify functions where commercial off-the-shelf "
        "(COTS) products do not meet your security requirements — perhaps due to unique "
        "encryption needs, specialized access control requirements, or the need to avoid "
        "widely-known products that are common attack targets. In these cases, custom "
        "development may reduce risk.</p>"
        "<p><strong>Example 2:</strong> If you develop custom critical components, apply the "
        "most rigorous development practices: formal code review, extensive testing, "
        "independent security assessment, and ongoing vulnerability management. Custom code "
        "does not have the broad user base that helps find bugs in popular products, so you "
        "need to invest more in your own testing.</p>"
    ),

    "sa-21": (
        "<p>Screen developers who will have access to your systems, source code, or development "
        "environments. Developers with malicious intent can introduce backdoors, weaken "
        "security controls, or exfiltrate sensitive code.</p>"
        "<p><strong>Example 1:</strong> Require background screening for all developers — "
        "internal and contractor — based on the sensitivity of the systems they will develop "
        "or access. Developers working on classified systems need security clearances. "
        "Developers working on CUI-related systems need, at minimum, standard background "
        "checks.</p>"
        "<p><strong>Example 2:</strong> For vendor development teams, require the vendor to "
        "certify that all developers assigned to your project have been screened to the "
        "appropriate level. Include screening requirements in the contract and the right to "
        "verify compliance. For offshore development, understand and document the screening "
        "limitations in different jurisdictions.</p>"
    ),

    "sa-21-1": (
        "<p>Validate that the screening claimed by vendors for their developers actually meets "
        "your requirements. Trust but verify — do not just take the vendor's word for it.</p>"
        "<p><strong>Example 1:</strong> In your vendor contracts, include the right to request "
        "documentation verifying that developer screening was performed to your standards. "
        "This might include redacted screening reports, certification letters, or attestations "
        "from the vendor's HR department.</p>"
        "<p><strong>Example 2:</strong> For high-security development work, require vendor "
        "developers to undergo your own screening process or provide screening results from "
        "a provider you trust. Include this as a contract deliverable with defined timelines: "
        "no developer writes code for your project until screening verification is on file.</p>"
    ),

    "sa-22": (
        "<p>Identify and manage system components that are no longer supported by their "
        "vendor. Unsupported software and hardware no longer receive security patches, making "
        "them increasingly vulnerable over time.</p>"
        "<p><strong>Example 1:</strong> Maintain a technology lifecycle inventory that flags "
        "components approaching or past end-of-life. Windows Server 2012 R2, Oracle Database "
        "12c, and similar products past their support dates should be highlighted with a "
        "planned migration timeline. Include unsupported components as POA&M items.</p>"
        "<p><strong>Example 2:</strong> If unsupported components cannot be immediately "
        "replaced, implement compensating controls: isolate them on a separate network "
        "segment, apply application whitelisting, increase monitoring, disable unnecessary "
        "services, and restrict user access. Document the risk acceptance with a specific "
        "migration plan and deadline approved by leadership.</p>"
    ),

    "sa-22-1": (
        "<p>When a vendor discontinues support for a product you depend on, seek alternative "
        "sources for continued support — extended support contracts, third-party maintenance "
        "providers, or community-maintained patches.</p>"
        "<p><strong>Example 1:</strong> Before a product reaches end-of-life, research "
        "alternative support options: Microsoft Extended Security Updates (ESU) for Windows "
        "Server, Oracle Lifetime Support, or third-party providers like Rimini Street that "
        "offer extended support for products the original vendor no longer patches.</p>"
        "<p><strong>Example 2:</strong> For open-source components that are no longer actively "
        "maintained, evaluate community forks that have taken over development. If no "
        "alternative support exists, prioritize migration to a supported product and treat "
        "the unsupported component as a high-risk item in your risk register.</p>"
    ),

    "sa-23": (
        "<p>Specialization means using dedicated, purpose-built components for security "
        "functions rather than general-purpose components with security features added on. "
        "Specialized tools are typically more effective at their specific function.</p>"
        "<p><strong>Example 1:</strong> Use a dedicated Web Application Firewall (WAF) for "
        "protecting web applications rather than relying solely on a general-purpose network "
        "firewall. A WAF is specifically designed to detect and block web attacks like SQL "
        "injection and XSS that a network firewall cannot see.</p>"
        "<p><strong>Example 2:</strong> Use a dedicated secrets management service (Azure Key "
        "Vault, HashiCorp Vault) for storing API keys, certificates, and passwords rather "
        "than general-purpose storage. Specialized secrets managers provide access controls, "
        "audit logging, rotation capabilities, and hardware-backed encryption that general "
        "storage cannot match.</p>"
    ),

    "sa-24": (
        "<p>Design systems with cyber resiliency in mind — the ability to anticipate, "
        "withstand, recover from, and adapt to attacks. Resiliency assumes that some attacks "
        "will succeed and focuses on continuing operations despite compromise.</p>"
        "<p><strong>Example 1:</strong> Design your architecture with redundancy and "
        "graceful degradation. If your primary authentication server is compromised, can "
        "users still authenticate through a backup? If your database is encrypted by "
        "ransomware, how quickly can you restore from backups? Design for these failure "
        "scenarios, not just for normal operations.</p>"
        "<p><strong>Example 2:</strong> Implement MITRE's Cyber Resiliency Engineering "
        "Framework: apply techniques like diversity (use different products for redundant "
        "functions), segmentation (limit blast radius of a compromise), and dynamic "
        "positioning (move critical assets to avoid persistent targeting). Test resiliency "
        "through regular tabletop exercises and red team engagements.</p>"
    ),
}
