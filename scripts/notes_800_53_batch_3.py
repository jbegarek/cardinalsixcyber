"""
Practitioner notes for NIST 800-53 Rev 5 controls — Batch 3:
Incident Response (IR), Maintenance (MA), Media Protection (MP),
Physical & Environmental Protection (PE), and Planning (PL).

Keys match the control `id` field from nist-800-53.json.
Values are HTML strings rendered on the control detail pages.
"""

NOTES = {
    # ── Incident Response (IR) ─────────────────────────────────────────

    "ir-1": (
        "<p>This control requires you to write down your incident response policy and make sure "
        "everyone who needs it can find it. Think of it as your company's official playbook for "
        "what happens when something goes wrong with your systems or data.</p>"
        "<p><strong>Example 1:</strong> Create an Incident Response Policy document in SharePoint "
        "under a dedicated <em>Security Policies</em> library. Include sections on scope, roles, "
        "reporting timelines, and escalation paths. Set a calendar reminder to review it annually "
        "and after any major incident.</p>"
        "<p><strong>Example 2:</strong> Use a policy management tool like PowerDMS or even a "
        "simple Word template with version control. Distribute the policy via email to all staff "
        "and require acknowledgment signatures. Store signed acknowledgments in your compliance "
        "folder for auditor review.</p>"
    ),

    "ir-2": (
        "<p>Your people need to know what to do when an incident happens — before it happens. "
        "This means formal training for anyone with a role in your incident response process, "
        "not just IT staff but also managers and communications personnel.</p>"
        "<p><strong>Example 1:</strong> Enroll your IR team in SANS SEC504 (Hacker Tools, "
        "Techniques, and Incident Handling) or equivalent training. For general staff, assign "
        "a yearly security awareness module through KnowBe4 or Proofpoint that covers how to "
        "report suspicious activity.</p>"
        "<p><strong>Example 2:</strong> Conduct a lunch-and-learn session quarterly where your "
        "IT security lead walks through a real-world breach case study. Document attendance "
        "in a training log spreadsheet that tracks who attended, the date, and topics covered. "
        "This log becomes your evidence for auditors.</p>"
    ),

    "ir-2-1": (
        "<p>Training works best when people practice under pressure. This enhancement requires "
        "you to include realistic simulated events — like a fake phishing attack or a mock "
        "ransomware scenario — in your incident response training.</p>"
        "<p><strong>Example 1:</strong> Use KnowBe4 or Proofpoint to send simulated phishing "
        "emails to all employees quarterly. Track who clicks, who reports, and use the results "
        "to tailor follow-up training for repeat offenders.</p>"
        "<p><strong>Example 2:</strong> Run a tabletop exercise where you present a scenario — "
        "such as an employee laptop stolen from a car — and walk your IR team through each "
        "step of the response. Document decisions made and gaps identified. Tools like Immersive "
        "Labs or AttackIQ can automate parts of this.</p>"
    ),

    "ir-2-2": (
        "<p>This enhancement calls for automated training environments — essentially cyber "
        "ranges or simulation platforms where your team can practice incident response in "
        "a safe, realistic setting without risking production systems.</p>"
        "<p><strong>Example 1:</strong> Subscribe to a cyber range platform like Immersive Labs, "
        "RangeForce, or SANS Cyber Ranges. Assign IR team members monthly labs that simulate "
        "malware analysis, log investigation, and containment procedures.</p>"
        "<p><strong>Example 2:</strong> Stand up an isolated virtual lab using VirtualBox or "
        "Hyper-V with intentionally vulnerable VMs (like Metasploitable or DVWA). Have your "
        "team practice detecting and responding to attacks in this sandboxed environment, "
        "then debrief findings together.</p>"
    ),

    "ir-2-3": (
        "<p>If your organization handles personal data, your IR team needs specific training "
        "on breach notification requirements — who to notify, how fast, and what to include. "
        "This is not just a technical issue; it is a legal and regulatory one.</p>"
        "<p><strong>Example 1:</strong> Train your IR team on your state's breach notification "
        "laws and any federal requirements (HIPAA, DFARS 7012). Create a quick-reference card "
        "listing notification timelines: 72 hours for GDPR, 60 days for HIPAA, 72 hours for "
        "DFARS cyber incidents to DIBCNET.</p>"
        "<p><strong>Example 2:</strong> Conduct an annual tabletop exercise specifically focused "
        "on a data breach scenario involving PII. Walk through the entire notification process: "
        "determining scope, contacting legal counsel, drafting notification letters, and "
        "reporting to regulators. Document the exercise and lessons learned.</p>"
    ),

    "ir-3": (
        "<p>You cannot just write an incident response plan and shelve it. You need to test it "
        "regularly to make sure it actually works. Testing can range from simple tabletop "
        "exercises to full-blown simulations.</p>"
        "<p><strong>Example 1:</strong> Conduct an annual tabletop exercise with your IR team, "
        "management, and legal. Use a realistic scenario like a ransomware attack that encrypts "
        "a file server. Walk through detection, containment, eradication, recovery, and "
        "communication steps. Document gaps and update the plan.</p>"
        "<p><strong>Example 2:</strong> Hire a penetration testing firm to conduct a red team "
        "engagement and measure how quickly your team detects and responds. Compare response "
        "times against your plan's targets. Alternatively, use tools like AttackIQ or SafeBreach "
        "to simulate attack scenarios and test detection capabilities.</p>"
    ),

    "ir-3-1": (
        "<p>This enhancement requires automated mechanisms to support your incident response "
        "testing. Instead of purely manual tabletop exercises, you use tools that automatically "
        "generate test scenarios or simulate attacks.</p>"
        "<p><strong>Example 1:</strong> Deploy a breach and attack simulation (BAS) tool like "
        "AttackIQ, SafeBreach, or Picus Security. Schedule automated attack simulations monthly "
        "that test your SIEM detection rules and endpoint response capabilities.</p>"
        "<p><strong>Example 2:</strong> Use Atomic Red Team scripts to automatically execute "
        "MITRE ATT&CK techniques on test systems. Compare the alerts generated in your SIEM "
        "(Splunk, Sentinel, or Elastic) against what should have been detected. Track detection "
        "coverage percentage over time.</p>"
    ),

    "ir-3-2": (
        "<p>Your incident response plan does not exist in a vacuum. It needs to work together "
        "with your business continuity plan, disaster recovery plan, and any other contingency "
        "plans your organization maintains.</p>"
        "<p><strong>Example 1:</strong> When you test your IR plan, invite the business continuity "
        "team to participate. Run a combined scenario where a cyber incident triggers a business "
        "disruption — for example, ransomware takes down your ERP system during quarter-end close.</p>"
        "<p><strong>Example 2:</strong> Create a cross-reference matrix in Excel or SharePoint that "
        "maps your IR plan sections to your disaster recovery and continuity plans. When you update "
        "or test one plan, check the matrix to ensure related plans are also reviewed and aligned.</p>"
    ),

    "ir-3-3": (
        "<p>Every time you test your incident response capability, you should be measuring results "
        "and using that data to get better. This enhancement formalizes the continuous improvement "
        "loop — test, measure, fix, repeat.</p>"
        "<p><strong>Example 1:</strong> After each IR exercise or real incident, conduct a formal "
        "after-action review. Track metrics like mean time to detect (MTTD), mean time to respond "
        "(MTTR), and communication delays. Log these in a spreadsheet and trend them over time.</p>"
        "<p><strong>Example 2:</strong> Use your SIEM's built-in reporting (Splunk dashboards, "
        "Microsoft Sentinel workbooks) to measure detection accuracy during simulated attacks. "
        "Compare quarter-over-quarter and set improvement targets — for example, reducing MTTD "
        "from 4 hours to 2 hours within six months.</p>"
    ),

    "ir-4": (
        "<p>This is the core of incident response — your organization must have an actual, "
        "working capability to handle security incidents through the full lifecycle: preparation, "
        "detection, analysis, containment, eradication, and recovery.</p>"
        "<p><strong>Example 1:</strong> Build your incident handling workflow in a ticketing system "
        "like Jira, ServiceNow, or even a shared SharePoint list. Create ticket templates for "
        "common incident types (phishing, malware, unauthorized access) with pre-populated "
        "checklists for each phase of the response lifecycle.</p>"
        "<p><strong>Example 2:</strong> Configure Microsoft Sentinel or Splunk SOAR to automate "
        "initial triage steps — for example, when a high-severity alert fires, automatically "
        "create an incident ticket, notify the on-call analyst via PagerDuty or Teams, and "
        "gather initial context like the affected user and device.</p>"
    ),

    "ir-4-1": (
        "<p>This enhancement requires automated tools to support your incident handling process. "
        "Manual-only processes are too slow for modern threats, so you need automation to help "
        "with triage, correlation, and initial response actions.</p>"
        "<p><strong>Example 1:</strong> Deploy a SOAR (Security Orchestration, Automation, and "
        "Response) platform like Microsoft Sentinel with automated playbooks, Splunk SOAR, or "
        "Palo Alto XSOAR. Create playbooks that automatically enrich alerts with threat intelligence, "
        "check IOCs against VirusTotal, and assign severity levels.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Defender for Endpoint's automated investigation "
        "and remediation (AIR) capabilities. When Defender detects malware, it can automatically "
        "isolate the device, collect forensic artifacts, and remediate the threat — all without "
        "analyst intervention for known threat types.</p>"
    ),

    "ir-4-2": (
        "<p>When an incident is detected, your systems should be able to reconfigure themselves "
        "dynamically — blocking an IP, isolating a network segment, or disabling a compromised "
        "account — as part of the response, not after a manual review.</p>"
        "<p><strong>Example 1:</strong> Configure your firewall (Palo Alto, Fortinet, or pfSense) "
        "to accept automated block rules from your SIEM or SOAR. When a confirmed malicious IP "
        "is identified, the SOAR playbook pushes a block rule to the firewall in real time.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Defender for Endpoint to automatically isolate "
        "a compromised machine from the network while keeping its connection to the Defender cloud "
        "for continued investigation. Set up Conditional Access policies in Azure AD that can "
        "dynamically block a user's access when their risk level changes to High.</p>"
    ),

    "ir-4-3": (
        "<p>Some incidents could shut down critical business operations. This enhancement requires "
        "you to identify which incidents could threaten mission continuity and have specific "
        "response actions ready to keep operations running.</p>"
        "<p><strong>Example 1:</strong> Identify your top five business-critical systems (email, "
        "ERP, file shares, customer portal, etc.) and create specific IR playbooks for each. "
        "Include failover procedures — for example, if your primary email server goes down due "
        "to an incident, document how to switch to a backup Exchange Online instance.</p>"
        "<p><strong>Example 2:</strong> Maintain a business impact analysis (BIA) document that "
        "maps each system to its recovery time objective (RTO). When an incident affects a critical "
        "system, your IR team uses the BIA to prioritize recovery. Store this document alongside "
        "your IR plan in SharePoint for quick access.</p>"
    ),

    "ir-4-4": (
        "<p>Individual incidents often look minor in isolation but form a pattern when correlated "
        "together. This enhancement requires you to connect the dots across incidents to get a "
        "big-picture view of what is happening.</p>"
        "<p><strong>Example 1:</strong> Use your SIEM (Splunk, Microsoft Sentinel, Elastic) to "
        "create correlation rules. For example, correlate multiple failed login attempts from "
        "different accounts with the same source IP to identify credential-stuffing attacks "
        "that individual alerts would miss.</p>"
        "<p><strong>Example 2:</strong> Maintain an incident tracking spreadsheet or database "
        "that logs every incident with common fields: date, type, affected systems, source IP, "
        "affected users. Review this quarterly to identify trends — are phishing attempts "
        "increasing? Is one department targeted more often than others?</p>"
    ),

    "ir-4-5": (
        "<p>In extreme cases, a system may need to shut itself down automatically to prevent "
        "further damage. This enhancement calls for configurable triggers that can disable a "
        "system when certain security violations are detected.</p>"
        "<p><strong>Example 1:</strong> Configure your endpoint detection tool (CrowdStrike, "
        "Microsoft Defender for Endpoint, or SentinelOne) to automatically isolate a machine "
        "from the network when it detects ransomware encryption behavior or a known exploit chain.</p>"
        "<p><strong>Example 2:</strong> Set up a GPO or Intune compliance policy that marks a "
        "device as non-compliant when critical security settings are tampered with. Pair this "
        "with a Conditional Access policy in Azure AD that blocks non-compliant devices from "
        "accessing corporate resources until the issue is resolved.</p>"
    ),

    "ir-4-6": (
        "<p>Insider threats — whether malicious employees or compromised accounts — require "
        "different handling than external attacks. You need specialized procedures because "
        "the threat actor already has legitimate access.</p>"
        "<p><strong>Example 1:</strong> Enable Microsoft Purview Insider Risk Management in "
        "M365 to detect risky user behaviors like mass file downloads, unusual email forwarding "
        "patterns, or data exfiltration to personal cloud storage. Configure alerts to go to "
        "HR and legal in addition to your security team.</p>"
        "<p><strong>Example 2:</strong> Create a specific insider threat section in your IR plan "
        "that includes coordination with HR and legal counsel before taking action. Document "
        "when to involve law enforcement. Keep insider threat investigations in a restricted "
        "access ticket queue separate from normal IT incidents.</p>"
    ),

    "ir-4-7": (
        "<p>Insider threat incidents cross organizational boundaries — security, HR, legal, "
        "management, and sometimes law enforcement all need to coordinate. This enhancement "
        "formalizes that coordination.</p>"
        "<p><strong>Example 1:</strong> Establish an Insider Threat Working Group that includes "
        "representatives from IT security, HR, legal, and department management. Meet quarterly "
        "to review indicators and monthly during active investigations. Document the group's "
        "charter and communication protocols.</p>"
        "<p><strong>Example 2:</strong> Create a secure Teams channel or encrypted email "
        "distribution list for insider threat communications. Use this channel to share "
        "sensitive investigation updates. Ensure all participants have signed NDAs and "
        "understand need-to-know restrictions for investigation details.</p>"
    ),

    "ir-4-8": (
        "<p>Some incidents affect more than just your organization — they may involve shared "
        "infrastructure, supply chain partners, or industry-wide attacks. This enhancement "
        "requires coordination with external organizations to share incident information.</p>"
        "<p><strong>Example 1:</strong> Join an Information Sharing and Analysis Center (ISAC) "
        "relevant to your industry — the Defense Industrial Base ISAC (DIB-ISAC) for defense "
        "contractors or Health-ISAC for healthcare. Share and receive threat indicators through "
        "their platforms.</p>"
        "<p><strong>Example 2:</strong> Establish a memorandum of understanding (MOU) with key "
        "partners and vendors for incident information sharing. When an incident involves a "
        "shared service or vendor, use the MOU framework to coordinate response and share "
        "IOCs, timelines, and remediation steps.</p>"
    ),

    "ir-4-9": (
        "<p>This enhancement requires your organization to have the ability to change its "
        "defensive posture dynamically in response to incidents — deploying new tools, changing "
        "configurations, or activating additional capabilities on demand.</p>"
        "<p><strong>Example 1:</strong> Maintain a library of pre-tested firewall rule sets and "
        "GPO configurations that can be rapidly deployed during an active incident. For example, "
        "have a ready-to-deploy GPO that disables USB storage across the domain, which you can "
        "link during a data exfiltration incident.</p>"
        "<p><strong>Example 2:</strong> Use cloud-based security tools like Microsoft Defender for "
        "Endpoint or CrowdStrike that allow you to push new detection rules, increase logging "
        "levels, or enable enhanced monitoring across all endpoints within minutes through their "
        "cloud console during an active threat.</p>"
    ),

    "ir-4-10": (
        "<p>When an incident involves your supply chain — a compromised vendor, a tainted software "
        "update, or a hardware tampering issue — you need to coordinate your response with every "
        "organization in that supply chain.</p>"
        "<p><strong>Example 1:</strong> Maintain a vendor contact list in your IR plan that includes "
        "security points of contact for all critical suppliers. When a supply chain incident occurs "
        "(like SolarWinds or MOVEit), you can quickly notify and coordinate with affected vendors.</p>"
        "<p><strong>Example 2:</strong> Include supply chain incident scenarios in your annual "
        "tabletop exercises. Walk through a scenario where a key software vendor is compromised "
        "and you need to determine exposure, isolate affected systems, and communicate with "
        "the vendor and your customers simultaneously.</p>"
    ),

    "ir-4-11": (
        "<p>This enhancement calls for an integrated IR team that can be deployed anywhere your "
        "organization operates. This is common in larger organizations with multiple locations "
        "or in organizations supporting geographically dispersed missions.</p>"
        "<p><strong>Example 1:</strong> Build a go-team kit with pre-configured laptops loaded "
        "with forensic tools (FTK, Autopsy, Wireshark), portable hard drives for evidence "
        "collection, and documented procedures. Ensure the team can deploy within 24 hours "
        "to any company facility.</p>"
        "<p><strong>Example 2:</strong> Contract with a managed detection and response (MDR) "
        "provider like CrowdStrike, Arctic Wolf, or Secureworks that offers on-site incident "
        "response services with guaranteed response times. Include deployment SLAs in the "
        "contract and test the engagement process annually.</p>"
    ),

    "ir-4-12": (
        "<p>After an incident is contained, you need to analyze any malicious code or artifacts "
        "left behind. This helps you understand what happened, confirm eradication is complete, "
        "and improve your defenses.</p>"
        "<p><strong>Example 1:</strong> Submit suspicious files to a malware sandbox like "
        "Any.Run, Joe Sandbox, or VirusTotal for automated analysis. Review the behavioral "
        "report to understand what the malware does — does it establish persistence, phone home "
        "to a C2 server, or exfiltrate data?</p>"
        "<p><strong>Example 2:</strong> Use tools like Volatility for memory forensics or "
        "Autopsy/FTK for disk forensics to examine compromised systems. Look for indicators "
        "of compromise (IOCs) like registry modifications, scheduled tasks, or rogue services. "
        "Feed discovered IOCs back into your SIEM detection rules.</p>"
    ),

    "ir-4-13": (
        "<p>Sometimes you detect suspicious behavior before a clear incident occurs — unusual "
        "network traffic, abnormal login patterns, or unexpected system changes. This enhancement "
        "requires you to analyze that anomalous behavior proactively.</p>"
        "<p><strong>Example 1:</strong> Enable User and Entity Behavior Analytics (UEBA) in "
        "Microsoft Sentinel or Splunk UBA. These tools baseline normal behavior for users and "
        "devices, then flag anomalies like a user suddenly downloading gigabytes of data or "
        "logging in from an unusual location.</p>"
        "<p><strong>Example 2:</strong> Use network detection tools like Darktrace or Zeek to "
        "monitor for unusual network patterns — unexpected outbound connections, lateral movement "
        "between servers, or DNS queries to newly registered domains. Have your analysts "
        "investigate flagged behaviors daily.</p>"
    ),

    "ir-4-14": (
        "<p>A Security Operations Center (SOC) provides dedicated, continuous monitoring and "
        "incident response capabilities. This can be an in-house team or an outsourced managed "
        "SOC service.</p>"
        "<p><strong>Example 1:</strong> Contract with a managed SOC provider like Arctic Wolf, "
        "Secureworks, or Binary Defense. They provide 24/7 monitoring of your SIEM and endpoint "
        "tools, triage alerts, and escalate confirmed incidents to your internal team with "
        "context and recommended response actions.</p>"
        "<p><strong>Example 2:</strong> If building an in-house SOC, start with a dedicated "
        "analyst during business hours using Microsoft Sentinel as your SIEM. Set up automated "
        "alerting for after-hours via PagerDuty or Opsgenie. Define clear escalation tiers and "
        "runbooks for common alert types.</p>"
    ),

    "ir-4-15": (
        "<p>Major incidents can damage your organization's reputation. This enhancement requires "
        "you to have a plan for public communications and reputation management following a "
        "significant security incident.</p>"
        "<p><strong>Example 1:</strong> Pre-draft incident communication templates for different "
        "audiences: customers, media, regulators, and employees. Store these in your IR plan. "
        "Include holding statements, FAQs, and escalation criteria for when to activate your "
        "communications plan.</p>"
        "<p><strong>Example 2:</strong> Identify a spokesperson and a backup who are trained in "
        "crisis communications. Ensure legal reviews all external communications before release. "
        "Monitor social media and news coverage during an incident using Google Alerts or a "
        "media monitoring service to manage the narrative proactively.</p>"
    ),

    "ir-5": (
        "<p>You need to track and document every security incident — when it happened, what was "
        "affected, who responded, and what the outcome was. This creates an organizational memory "
        "that helps you improve over time and prove due diligence to auditors.</p>"
        "<p><strong>Example 1:</strong> Use a ticketing system like Jira Service Management, "
        "ServiceNow, or even a dedicated SharePoint list to log all incidents. Require fields "
        "for date/time, type, severity, affected systems, responder, actions taken, and "
        "resolution. Run monthly reports to track trends.</p>"
        "<p><strong>Example 2:</strong> Configure your SIEM (Splunk, Microsoft Sentinel) to "
        "automatically create incident records when alerts exceed a severity threshold. Build "
        "a dashboard that shows open incidents, average resolution time, and incident volume "
        "by category over the past 12 months.</p>"
    ),

    "ir-5-1": (
        "<p>This enhancement requires automated tools to track incidents and collect and analyze "
        "incident data. Manual spreadsheets and email chains are not sufficient — you need "
        "systems that capture data consistently and support analysis.</p>"
        "<p><strong>Example 1:</strong> Deploy Microsoft Sentinel with automated incident "
        "creation from analytics rules. Use Sentinel's built-in investigation graph to "
        "automatically correlate alerts, entities, and timelines. Export incident data to "
        "Power BI for trend analysis and executive reporting.</p>"
        "<p><strong>Example 2:</strong> Use a SOAR platform (Splunk SOAR, Palo Alto XSOAR) that "
        "automatically enriches incident tickets with threat intelligence, tracks analyst "
        "actions, and generates metrics like MTTD and MTTR. Set up automated weekly summary "
        "reports to management.</p>"
    ),

    "ir-6": (
        "<p>Everyone in your organization needs to know how and where to report a suspected "
        "security incident. Reporting must happen quickly — delays give attackers more time "
        "to cause damage.</p>"
        "<p><strong>Example 1:</strong> Create a clearly visible 'Report a Security Incident' "
        "button on your company intranet that opens a simple form or sends an email to your "
        "security team distribution list. Train all employees during onboarding on how to use "
        "it. Set a policy requiring reports within one hour of discovery.</p>"
        "<p><strong>Example 2:</strong> If you are a defense contractor, configure your incident "
        "reporting process to meet DFARS 252.204-7012 requirements — report cyber incidents to "
        "DIBCNET within 72 hours. Create a checklist of required information for the report and "
        "keep it in your IR plan for quick reference during an active incident.</p>"
    ),

    "ir-6-1": (
        "<p>This enhancement requires automated mechanisms for reporting incidents. Instead of "
        "relying on manual emails or phone calls, your systems should automatically generate "
        "and route incident reports.</p>"
        "<p><strong>Example 1:</strong> Configure your SIEM to automatically generate incident "
        "reports when certain alert thresholds are met and email them to designated recipients. "
        "Use Microsoft Sentinel's automated notification rules to alert leadership via Teams or "
        "email when a Severity 1 incident is created.</p>"
        "<p><strong>Example 2:</strong> Set up a Power Automate flow or similar automation that "
        "generates a formatted incident report from your ticketing system and distributes it to "
        "required stakeholders (CISO, legal, management). Include relevant details like timeline, "
        "scope, and current status automatically pulled from the ticket.</p>"
    ),

    "ir-6-2": (
        "<p>When an incident reveals a vulnerability — whether in your software, configuration, "
        "or processes — that vulnerability needs to be reported to the right people so it can be "
        "fixed and not exploited again.</p>"
        "<p><strong>Example 1:</strong> After every incident, conduct a root cause analysis that "
        "identifies any underlying vulnerabilities. Log these in your vulnerability management "
        "tool (Tenable, Qualys, or Rapid7) and assign them for remediation with priority based "
        "on the incident severity.</p>"
        "<p><strong>Example 2:</strong> Create a post-incident vulnerability report template "
        "that captures the CVE (if applicable), affected systems, how it was exploited, and "
        "recommended fixes. Submit this to your patch management team and track remediation "
        "through your change management process.</p>"
    ),

    "ir-6-3": (
        "<p>When an incident involves a product or service from a vendor, you need to report "
        "the relevant details back to that vendor and coordinate across the supply chain so "
        "everyone can protect themselves.</p>"
        "<p><strong>Example 1:</strong> If you discover a zero-day vulnerability in a vendor's "
        "product during incident response, report it to the vendor through their security "
        "disclosure process (usually found on their website). Also report to CISA if the "
        "product is widely used in critical infrastructure.</p>"
        "<p><strong>Example 2:</strong> Include vendor notification procedures in your IR plan. "
        "Maintain a list of security contacts for your critical vendors. When an incident "
        "involves a vendor product, notify them within 24 hours and share relevant IOCs and "
        "log data to help them investigate on their end.</p>"
    ),

    "ir-7": (
        "<p>Your employees need somewhere to turn for help when they encounter a security "
        "incident. This control requires an incident response support resource — like a help "
        "desk, security team, or managed service — that can assist users.</p>"
        "<p><strong>Example 1:</strong> Add incident response support to your IT help desk "
        "procedures. Train help desk staff to recognize security incidents, capture key details, "
        "and escalate to your security team. Create a dedicated queue or ticket category for "
        "security incidents so they are prioritized appropriately.</p>"
        "<p><strong>Example 2:</strong> If you use a managed security service provider (MSSP), "
        "ensure their contact information is posted in common areas and on the intranet. Provide "
        "a 24/7 phone number or chat option for after-hours security emergencies. Test the "
        "response process quarterly by calling in a simulated report.</p>"
    ),

    "ir-7-1": (
        "<p>This enhancement calls for automation to make incident response information and "
        "support more readily available to users. People should be able to find what they need "
        "quickly without hunting for it.</p>"
        "<p><strong>Example 1:</strong> Create a dedicated incident response page on your "
        "company intranet with quick links to the IR plan, reporting forms, contact information, "
        "and common incident runbooks. Use a chatbot (like a Teams bot built with Power Virtual "
        "Agents) that can answer basic incident questions and route reports.</p>"
        "<p><strong>Example 2:</strong> Set up automated email responses that acknowledge "
        "incident reports and provide immediate guidance. When someone reports a phishing email, "
        "the auto-response could include steps to take immediately (disconnect from VPN, do not "
        "click further links, preserve the email as evidence).</p>"
    ),

    "ir-7-2": (
        "<p>Your incident response capability should have a working relationship with external "
        "security service providers — like your ISP, MSSP, antivirus vendor, or law enforcement — "
        "so you can get help quickly when needed.</p>"
        "<p><strong>Example 1:</strong> Maintain a contact directory of external IR resources: "
        "your MSSP, FBI Cyber Division field office, CISA regional office, and your cyber "
        "insurance provider's breach response hotline. Include account numbers and contract "
        "references so you can activate support quickly.</p>"
        "<p><strong>Example 2:</strong> Pre-negotiate an incident response retainer with a "
        "digital forensics firm (like CrowdStrike Services, Mandiant, or Kroll). Having a "
        "retainer means you do not have to negotiate contracts during a crisis — you just "
        "make a phone call and they start working.</p>"
    ),

    "ir-8": (
        "<p>The incident response plan is the master document that ties everything together. "
        "It defines roles, responsibilities, communication procedures, and the step-by-step "
        "process for handling incidents from detection through recovery.</p>"
        "<p><strong>Example 1:</strong> Write your IR plan using NIST SP 800-61 Rev 2 as a "
        "template. Include sections for: purpose and scope, roles and responsibilities (name "
        "specific people), communication procedures (internal and external), incident categories "
        "and severity levels, and step-by-step procedures for each phase.</p>"
        "<p><strong>Example 2:</strong> Store the IR plan in a location accessible even if your "
        "primary systems are down — a printed copy in a fire safe, a copy on a secured USB drive, "
        "or in a cloud-based document store separate from your main infrastructure. Review and "
        "update it at least annually and after every significant incident.</p>"
    ),

    "ir-8-1": (
        "<p>If your organization handles personally identifiable information, your IR plan needs "
        "a specific section on data breaches — including how you determine whether notification "
        "is required and how you carry it out.</p>"
        "<p><strong>Example 1:</strong> Add a breach notification annex to your IR plan that "
        "includes decision trees for determining notification requirements under applicable "
        "laws (state breach notification, HIPAA, GDPR). Include template notification letters "
        "for individuals and regulators.</p>"
        "<p><strong>Example 2:</strong> Document your breach assessment process: who determines "
        "scope, how you identify affected individuals, what your notification timeline is, and "
        "who approves external communications. Include contact information for your state "
        "attorney general's office, HHS (if HIPAA applies), and your cyber insurance carrier's "
        "breach coach.</p>"
    ),

    "ir-9": (
        "<p>Information spillage — when classified or controlled data ends up on a system not "
        "authorized to handle it — requires a specific response process. This is especially "
        "critical for defense contractors handling CUI or classified information.</p>"
        "<p><strong>Example 1:</strong> Create a spillage response procedure that covers: "
        "identifying the data involved, isolating affected systems, determining the scope of "
        "exposure, sanitizing or destroying affected media, and notifying the data owner. For "
        "CUI spills, follow your organization's CUI marking and handling guide.</p>"
        "<p><strong>Example 2:</strong> If someone emails a document containing CUI to a personal "
        "email account, your procedure should include: immediately recalling the email (if "
        "possible via Exchange admin center), confirming deletion from the recipient's mailbox, "
        "documenting the incident, and reporting it to your security officer. Use Microsoft "
        "Purview DLP policies to prevent future occurrences.</p>"
    ),

    "ir-9-1": (
        "<p>This enhancement requires you to identify specific personnel responsible for "
        "responding to information spillage incidents. These individuals should have the "
        "authority and training to manage spillage cleanup.</p>"
        "<p><strong>Example 1:</strong> Designate your Information System Security Officer "
        "(ISSO) or Facility Security Officer (FSO) as the primary spillage response lead. "
        "Document this assignment in your IR plan and ensure they have completed spillage "
        "response training.</p>"
        "<p><strong>Example 2:</strong> Create a spillage response team roster that includes "
        "your security officer, system administrator, and a representative from the program "
        "office that owns the spilled data. Post this roster alongside your IR plan and ensure "
        "all listed personnel understand their roles.</p>"
    ),

    "ir-9-2": (
        "<p>People involved in handling information spillage need specific training on how to "
        "contain and clean up spills without making them worse. Training should cover both "
        "technical steps and reporting requirements.</p>"
        "<p><strong>Example 1:</strong> Include spillage response procedures in your annual "
        "security awareness training. Cover scenarios like accidentally copying classified "
        "files to an unclassified USB drive or emailing CUI to an unauthorized recipient. "
        "Walk through the correct response step by step.</p>"
        "<p><strong>Example 2:</strong> Conduct a focused tabletop exercise on information "
        "spillage for your IT and security staff. Use a scenario like finding CUI data on a "
        "shared drive accessible to unauthorized users. Practice the containment, sanitization, "
        "and reporting steps, then document lessons learned.</p>"
    ),

    "ir-9-3": (
        "<p>After an information spillage, your team needs to keep working while contaminated "
        "systems are being cleaned. This enhancement requires documented procedures for "
        "continuing operations during spillage remediation.</p>"
        "<p><strong>Example 1:</strong> Maintain a list of backup systems or workarounds for "
        "each critical business function. If a workstation is taken offline for spillage "
        "cleanup, the affected employee should know which backup machine to use or how to "
        "access systems remotely through an alternate path.</p>"
        "<p><strong>Example 2:</strong> Document standard operating procedures for reassigning "
        "work during spillage incidents. For example, if a shared file server is quarantined, "
        "have a procedure to grant temporary access to an alternate server with clean copies "
        "of non-contaminated working files.</p>"
    ),

    "ir-9-4": (
        "<p>When someone without proper authorization is exposed to spilled information, you "
        "need specific procedures to handle that exposure — this might include briefing them "
        "on handling requirements or getting them to sign non-disclosure agreements.</p>"
        "<p><strong>Example 1:</strong> If an employee without CUI authorization accidentally "
        "views a CUI document, have them sign a non-disclosure acknowledgment form. Brief them "
        "on what they saw and their obligation not to discuss or distribute it. Document this "
        "interaction in the incident record.</p>"
        "<p><strong>Example 2:</strong> For classified spillage involving unauthorized viewers, "
        "follow your facility's security procedures: notify your FSO, contact the cognizant "
        "security agency, and arrange for a security briefing/debriefing of the exposed "
        "personnel. Document everything on the appropriate incident report forms.</p>"
    ),

    "ir-10": (
        "<p>This control calls for an integrated team that brings together security analysts, "
        "forensic specialists, threat intelligence analysts, and other experts into a cohesive "
        "unit that can analyze incidents holistically.</p>"
        "<p><strong>Example 1:</strong> Form a cross-functional security analysis team that "
        "includes network analysts, endpoint specialists, and threat intelligence staff. "
        "Hold weekly threat review meetings to discuss active threats, recent incidents, and "
        "new intelligence. Use a shared platform like Microsoft Sentinel or Splunk for "
        "collaborative analysis.</p>"
        "<p><strong>Example 2:</strong> If your organization is too small for a dedicated team, "
        "contract with an MDR provider that offers integrated analysis capabilities. Ensure "
        "their service includes threat hunting, forensic analysis, and intelligence sharing. "
        "Schedule monthly review calls to discuss their findings and your organization's risk "
        "posture.</p>"
    ),

    # ── Maintenance (MA) ───────────────────────────────────────────────

    "ma-1": (
        "<p>This control requires a documented maintenance policy and procedures. Your policy "
        "should describe how system maintenance is authorized, performed, and tracked — covering "
        "both routine upkeep and emergency repairs.</p>"
        "<p><strong>Example 1:</strong> Create a System Maintenance Policy document in SharePoint "
        "that defines who can perform maintenance, what approvals are needed, how maintenance "
        "windows are scheduled, and what records must be kept. Include both on-site and remote "
        "maintenance procedures. Review it annually.</p>"
        "<p><strong>Example 2:</strong> Use a change management system like ServiceNow or Jira "
        "Service Management to enforce maintenance procedures. Require a change request ticket "
        "for all planned maintenance with approval workflows. Store your policy and procedures "
        "in a compliance library that all IT staff can access.</p>"
    ),

    "ma-2": (
        "<p>Maintenance on your systems — patching, hardware replacement, repairs — needs to be "
        "scheduled, approved, documented, and reviewed. You cannot just let anyone make changes "
        "whenever they want.</p>"
        "<p><strong>Example 1:</strong> Use Windows Server Update Services (WSUS) or Microsoft "
        "Endpoint Configuration Manager (MECM/SCCM) to schedule and deploy patches during "
        "defined maintenance windows. Document each patch cycle in a maintenance log that "
        "records what was installed, when, and on which systems.</p>"
        "<p><strong>Example 2:</strong> For hardware maintenance, create a maintenance log "
        "spreadsheet or use a CMDB tool (ServiceNow, Snipe-IT) to track all repairs and "
        "replacements. Record the technician name, date, work performed, parts replaced, and "
        "supervisor approval. Review these records quarterly to identify recurring issues.</p>"
    ),

    "ma-2-1": (
        "<p>This enhancement specifies what information your maintenance records should contain. "
        "Good records protect you during audits and help you track the health of your systems "
        "over time.</p>"
        "<p><strong>Example 1:</strong> In your CMDB or maintenance tracking system, require "
        "the following fields for every maintenance record: date and time, system or component "
        "name, type of maintenance (preventive, corrective, emergency), technician name, "
        "description of work, parts used, and supervisor approval.</p>"
        "<p><strong>Example 2:</strong> Create a standardized maintenance record template in "
        "Word or SharePoint that technicians fill out for every maintenance action. Include "
        "checkboxes for common activities (firmware update, hardware replacement, configuration "
        "change) and a free-text field for details. Archive completed forms in a compliance "
        "folder organized by date.</p>"
    ),

    "ma-2-2": (
        "<p>This enhancement calls for automated tools to schedule, perform, and document "
        "maintenance activities. Automation reduces human error and ensures nothing falls "
        "through the cracks.</p>"
        "<p><strong>Example 1:</strong> Use Microsoft Endpoint Configuration Manager (MECM) "
        "to automate patch deployment on a schedule: test patches in a pilot group first, then "
        "deploy to production after a defined soak period. MECM automatically logs what was "
        "deployed, to which machines, and whether it succeeded or failed.</p>"
        "<p><strong>Example 2:</strong> Use Ansible, Puppet, or Chef to automate system "
        "configuration maintenance. Write playbooks that check for and apply required "
        "configurations (NTP settings, security baselines, log rotation). Schedule these "
        "to run weekly and output reports to a central log for review.</p>"
    ),

    "ma-3": (
        "<p>Any tools used for system maintenance — diagnostic software, USB drives, external "
        "hard drives, boot media — need to be approved, controlled, and monitored. You do not "
        "want unauthorized tools introducing malware or creating vulnerabilities.</p>"
        "<p><strong>Example 1:</strong> Maintain an approved tools list that documents every "
        "diagnostic and maintenance tool authorized for use on your systems. Include the tool "
        "name, version, purpose, and the person responsible for keeping it current. Review "
        "and update this list at least annually.</p>"
        "<p><strong>Example 2:</strong> Use application whitelisting through AppLocker (GPO path: "
        "<em>Computer Configuration → Policies → Windows Settings → Security Settings → "
        "Application Control Policies → AppLocker</em>) to restrict which executables can run "
        "on systems. Only approved maintenance tools should be whitelisted on server systems.</p>"
    ),

    "ma-3-1": (
        "<p>Before maintenance personnel use their tools on your systems, those tools need to "
        "be inspected for unauthorized modifications. A tampered maintenance tool could be used "
        "to install backdoors or steal data.</p>"
        "<p><strong>Example 1:</strong> Before allowing a vendor technician to connect their "
        "laptop or diagnostic tool to your network, have your security team verify the tool "
        "against your approved list. Check software versions and look for unauthorized software. "
        "Document the inspection in the maintenance record.</p>"
        "<p><strong>Example 2:</strong> For internally maintained tools, compute and store "
        "cryptographic hashes (SHA-256) of all approved maintenance software. Before each use, "
        "verify the hash matches the known-good value using PowerShell: "
        "<em>Get-FileHash -Algorithm SHA256 tool.exe</em>. Any mismatch triggers an investigation.</p>"
    ),

    "ma-3-2": (
        "<p>Diagnostic or test media — like bootable USB drives or CDs used for troubleshooting — "
        "need to be scanned for malicious code before you plug them into any system.</p>"
        "<p><strong>Example 1:</strong> Before using any external media for maintenance, scan it "
        "with your endpoint protection tool (Microsoft Defender, CrowdStrike, SentinelOne). "
        "Create a dedicated scanning workstation that is isolated from your production network "
        "specifically for inspecting incoming media.</p>"
        "<p><strong>Example 2:</strong> Establish a policy that all maintenance media must be "
        "scanned at a quarantine workstation before use. Log each scan in a media inspection "
        "register (date, media description, scan tool used, results, inspector name). Reject "
        "any media that fails the scan.</p>"
    ),

    "ma-3-3": (
        "<p>Maintenance equipment that has been connected to your systems may contain "
        "organizational data. You need to prevent that equipment from leaving with your data "
        "still on it.</p>"
        "<p><strong>Example 1:</strong> Before a vendor technician leaves your facility, have "
        "your security team verify that no organizational data remains on their tools or "
        "laptops. Check any files created during the session, clear temp files, and document "
        "the verification in the maintenance record.</p>"
        "<p><strong>Example 2:</strong> Implement a sign-in/sign-out process for maintenance "
        "equipment at your facility entrance. When equipment leaves, a supervisor verifies "
        "that storage media has been sanitized. Use a checklist: was equipment connected to "
        "the network? Did it access any data stores? Were temp files cleared?</p>"
    ),

    "ma-3-4": (
        "<p>Only authorized personnel should be using maintenance tools on your systems. This "
        "prevents unauthorized individuals from using diagnostic tools that could access "
        "sensitive data or modify system configurations.</p>"
        "<p><strong>Example 1:</strong> Lock maintenance tools in a secure cabinet or equipment "
        "room. Require sign-out with supervisor approval before tools can be used. Maintain "
        "a log of who checked out each tool, when, and for what purpose.</p>"
        "<p><strong>Example 2:</strong> For software-based maintenance tools, restrict access "
        "using Active Directory security groups. Only members of a 'Maintenance Tools' group "
        "can launch diagnostic applications. Configure AppLocker rules to enforce this "
        "restriction at the OS level.</p>"
    ),

    "ma-3-5": (
        "<p>Some maintenance tools run with elevated privileges — administrative rights, kernel "
        "access, or root-level permissions. These tools need extra monitoring because misuse "
        "could compromise the entire system.</p>"
        "<p><strong>Example 1:</strong> Enable command-line auditing and PowerShell script block "
        "logging on all systems where maintenance tools with elevated privileges are used. "
        "Configure the GPO at <em>Computer Configuration → Administrative Templates → Windows "
        "Components → Windows PowerShell → Turn on Script Block Logging</em>.</p>"
        "<p><strong>Example 2:</strong> Use a privileged access management (PAM) tool like "
        "CyberArk, BeyondTrust, or Azure AD Privileged Identity Management (PIM) to control "
        "access to maintenance tools that require admin rights. Require just-in-time activation "
        "and record all sessions for review.</p>"
    ),

    "ma-3-6": (
        "<p>Maintenance tools themselves need to be kept current with the latest software updates "
        "and patches. An outdated diagnostic tool could have vulnerabilities that compromise "
        "the systems you are trying to maintain.</p>"
        "<p><strong>Example 1:</strong> Include maintenance tools in your regular patch management "
        "cycle. When you update your approved tools list, verify that each tool is running the "
        "latest version. Use a software inventory tool like PDQ Inventory or MECM to track "
        "versions across all maintenance workstations.</p>"
        "<p><strong>Example 2:</strong> Set calendar reminders to check for updates to your "
        "maintenance software monthly. Subscribe to vendor security advisories for your "
        "diagnostic tools. Document the current version of each tool in your approved tools "
        "list and update it whenever a new version is deployed.</p>"
    ),

    "ma-4": (
        "<p>Nonlocal maintenance — maintenance performed over the network rather than in person — "
        "needs to be explicitly approved and monitored. Remote access for maintenance is a "
        "common attack vector, so treat it with extra caution.</p>"
        "<p><strong>Example 1:</strong> Require all remote maintenance sessions to go through "
        "your VPN and be authenticated with multi-factor authentication. Use a remote access "
        "tool like a jump server or privileged access workstation (PAW) that logs all sessions. "
        "Document each session in your maintenance log.</p>"
        "<p><strong>Example 2:</strong> If vendors need remote access for maintenance, use a "
        "vendor access management solution like BeyondTrust or CyberArk Vendor PAM. Grant "
        "time-limited access only during approved maintenance windows. Record the session and "
        "review the recording if any anomalies are detected.</p>"
    ),

    "ma-4-1": (
        "<p>All nonlocal (remote) maintenance sessions need to be logged, and those logs need "
        "to be reviewed for anything unusual. This gives you an audit trail and helps detect "
        "unauthorized activity during maintenance windows.</p>"
        "<p><strong>Example 1:</strong> Configure your VPN and remote access tools to log all "
        "session details: who connected, when, from where, what systems they accessed, and "
        "session duration. Forward these logs to your SIEM (Splunk, Sentinel) and create "
        "an alert for sessions outside approved maintenance windows.</p>"
        "<p><strong>Example 2:</strong> Use Windows Event Forwarding to collect Remote Desktop "
        "session logs (Event IDs 4624, 4634 for logon/logoff, and 21/22/25 from the "
        "TerminalServices-LocalSessionManager). Review these weekly for unexpected remote "
        "maintenance connections.</p>"
    ),

    "ma-4-2": (
        "<p>This enhancement requires you to document all nonlocal maintenance activities — "
        "who performed what, when, from where, and what was the outcome. Documentation is "
        "your evidence that remote maintenance was authorized and properly conducted.</p>"
        "<p><strong>Example 1:</strong> Create a Nonlocal Maintenance Log template in SharePoint "
        "with fields for: date, start/end time, technician name, remote IP address, systems "
        "accessed, work description, and supervisor approval. Require completion for every "
        "remote session.</p>"
        "<p><strong>Example 2:</strong> Use your change management system (ServiceNow, Jira) to "
        "create a specific ticket type for remote maintenance. The ticket must be approved "
        "before work begins and closed out with a summary of actions taken. Link the ticket "
        "to session recordings if available.</p>"
    ),

    "ma-4-3": (
        "<p>If remote maintenance is performed from an external system, that system needs to "
        "have security controls comparable to what you would require internally. Alternatively, "
        "you sanitize the affected component before reconnecting it to your network.</p>"
        "<p><strong>Example 1:</strong> Require vendors performing remote maintenance to "
        "complete a security questionnaire confirming their maintenance systems meet your "
        "standards: current patches, endpoint protection, encrypted connections, MFA. Include "
        "this requirement in your vendor contracts.</p>"
        "<p><strong>Example 2:</strong> After a vendor completes remote maintenance on a "
        "system, run a STIG compliance scan (using SCAP tools or STIG Viewer) to verify "
        "the system still meets your security baseline. Address any new findings before "
        "returning the system to production.</p>"
    ),

    "ma-4-4": (
        "<p>Remote maintenance sessions need strong authentication and network separation. "
        "You do not want maintenance traffic mixed in with regular user traffic where it "
        "could be intercepted or misrouted.</p>"
        "<p><strong>Example 1:</strong> Set up a dedicated management VLAN for remote "
        "maintenance connections. Configure your firewall to only allow maintenance traffic "
        "from authorized IPs into this VLAN. Require multi-factor authentication (smart card "
        "or MFA app) for all maintenance sessions.</p>"
        "<p><strong>Example 2:</strong> Use Azure AD Conditional Access to require MFA and "
        "a compliant device for any remote session that accesses management interfaces. "
        "Separate maintenance sessions by using a dedicated jump server or Azure Bastion "
        "host that provides session isolation from the production network.</p>"
    ),

    "ma-4-5": (
        "<p>Each remote maintenance session should be individually approved before it begins, "
        "and designated personnel should be notified of planned maintenance. This prevents "
        "surprise access and ensures oversight.</p>"
        "<p><strong>Example 1:</strong> Require a change request ticket approved by the system "
        "owner before any remote maintenance session. Configure ServiceNow or Jira to send "
        "automated notifications to the security team, system owner, and IT manager when "
        "remote maintenance is scheduled.</p>"
        "<p><strong>Example 2:</strong> Implement a maintenance scheduling calendar in Teams "
        "or SharePoint that all remote sessions are posted to at least 24 hours in advance. "
        "The ISSO or system administrator must acknowledge the scheduled session before access "
        "credentials are provided to the technician.</p>"
    ),

    "ma-4-6": (
        "<p>All remote maintenance communications must be encrypted to prevent eavesdropping "
        "and tampering. Plaintext remote access tools are not acceptable for system maintenance.</p>"
        "<p><strong>Example 1:</strong> Require all remote maintenance connections to use "
        "encrypted protocols: SSH instead of Telnet, HTTPS instead of HTTP, RDP with Network "
        "Level Authentication over a VPN. Block unencrypted management protocols at the "
        "firewall level.</p>"
        "<p><strong>Example 2:</strong> Configure your VPN concentrator to use TLS 1.2 or higher "
        "with FIPS-validated cryptographic modules. If using Azure, enable Azure Bastion "
        "which provides encrypted RDP and SSH sessions through the Azure portal without "
        "exposing management ports to the internet.</p>"
    ),

    "ma-4-7": (
        "<p>After remote maintenance is complete, you need to verify that the session has "
        "actually been disconnected and that no persistent connections remain. Lingering "
        "sessions are a security risk.</p>"
        "<p><strong>Example 1:</strong> After each remote maintenance session, verify "
        "disconnection by checking active sessions on the target system: use <em>quser</em> "
        "or <em>query session</em> on Windows servers to confirm no orphaned RDP sessions "
        "remain. Log the verification in the maintenance record.</p>"
        "<p><strong>Example 2:</strong> Configure your VPN concentrator and remote access "
        "tools to automatically terminate sessions after a defined idle timeout (e.g., 15 "
        "minutes). Set up session limits so technicians cannot leave connections open "
        "indefinitely. Review VPN session logs daily for sessions exceeding expected durations.</p>"
    ),

    "ma-5": (
        "<p>Anyone performing maintenance on your systems needs to be authorized and vetted. "
        "You need a process for approving maintenance personnel and a list of who is approved, "
        "whether they are employees or contractors.</p>"
        "<p><strong>Example 1:</strong> Maintain an authorized maintenance personnel list in "
        "SharePoint or your CMDB. For each person, record their name, organization, clearance "
        "level (if applicable), what systems they are authorized to work on, and the date "
        "their authorization was last reviewed. Review the list quarterly.</p>"
        "<p><strong>Example 2:</strong> For vendor technicians, require a completed background "
        "check verification and a signed rules of behavior agreement before granting maintenance "
        "access. Escort uncleared vendor personnel at all times and log their visit in your "
        "visitor log. Have a supervisor verify their work before they leave.</p>"
    ),

    "ma-5-1": (
        "<p>When maintenance must be performed by someone who does not have the appropriate "
        "security clearance or access authorization, you need extra safeguards — escorting, "
        "supervision, and sanitization of classified information before they can access the system.</p>"
        "<p><strong>Example 1:</strong> Before an uncleared technician works on a system, "
        "remove or power off any storage media containing sensitive data. Have a cleared "
        "employee escort and directly supervise the technician throughout the entire "
        "maintenance session. Document the escort and supervision in the maintenance record.</p>"
        "<p><strong>Example 2:</strong> Create a pre-maintenance checklist for uncleared "
        "personnel visits: sanitize or disconnect sensitive storage, assign an escort, brief "
        "the escort on supervision requirements, log the technician's entry and exit times, "
        "and perform a post-maintenance security check on the system before returning it to "
        "service.</p>"
    ),

    "ma-5-2": (
        "<p>Personnel performing maintenance on classified systems must possess the appropriate "
        "security clearances and formal access approvals for the classification level of the "
        "information being processed.</p>"
        "<p><strong>Example 1:</strong> Before granting a technician access to a classified "
        "system, verify their clearance level through DISS (Defense Information System for "
        "Security) or your FSO. Confirm they have been formally read into the relevant "
        "program. Document the verification in the maintenance record.</p>"
        "<p><strong>Example 2:</strong> Maintain a matrix that maps each classified system to "
        "its required clearance level and approved maintenance personnel. When a maintenance "
        "request comes in, check the technician against this matrix before granting access. "
        "Your FSO should sign off on every maintenance event involving classified systems.</p>"
    ),

    "ma-5-3": (
        "<p>For classified systems, maintenance personnel must be U.S. citizens. This is a "
        "non-negotiable requirement for systems processing national security information.</p>"
        "<p><strong>Example 1:</strong> Include citizenship verification as part of your "
        "maintenance personnel authorization process. Verify U.S. citizenship through your "
        "HR records or the technician's employer. Document the verification in their "
        "authorization file.</p>"
        "<p><strong>Example 2:</strong> Add citizenship verification to your vendor contract "
        "requirements for any work involving classified systems. Include a contract clause "
        "requiring the vendor to certify that all maintenance personnel assigned to your "
        "classified systems are U.S. citizens.</p>"
    ),

    "ma-5-4": (
        "<p>Foreign nationals may only perform maintenance on classified systems under specific "
        "conditions — generally only on jointly owned and operated systems, and only with "
        "appropriate clearances from their government.</p>"
        "<p><strong>Example 1:</strong> If your organization operates a coalition or partner "
        "system, document which systems foreign nationals may access and the specific agreements "
        "(such as a CJCS or bilateral security agreement) that authorize their access. Maintain "
        "this documentation with your FSO.</p>"
        "<p><strong>Example 2:</strong> For any foreign national performing maintenance, obtain "
        "approval from your cognizant security agency. Document the foreign national's "
        "clearance, citizenship, the authorizing agreement, and supervisory arrangements. "
        "Assign a U.S. citizen escort for the duration of the maintenance.</p>"
    ),

    "ma-5-5": (
        "<p>Non-system maintenance — like building maintenance, HVAC, or electrical work — "
        "performed near your systems still requires access authorization. A plumber in your "
        "server room can be a security risk even if they never touch a keyboard.</p>"
        "<p><strong>Example 1:</strong> Require escort for any non-IT maintenance personnel "
        "(electricians, HVAC technicians, janitorial staff) when they work in or near server "
        "rooms or network closets. The escort must be a cleared employee who can observe "
        "their activities at all times.</p>"
        "<p><strong>Example 2:</strong> Install access controls on server room and network "
        "closet doors that restrict entry to authorized personnel only. When building "
        "maintenance staff need access, issue a temporary badge, assign an escort, and "
        "log the visit. Review the visitor log monthly.</p>"
    ),

    "ma-6": (
        "<p>When critical systems fail, you need to get them fixed fast. This control requires "
        "you to have maintenance support and spare parts available within defined timeframes "
        "based on how critical each system is.</p>"
        "<p><strong>Example 1:</strong> Purchase hardware support contracts (Dell ProSupport, "
        "HPE Pointnext, or Lenovo Premier Support) with next-business-day or 4-hour response "
        "SLAs for your critical servers and network equipment. Keep the contract details and "
        "support contact numbers readily accessible.</p>"
        "<p><strong>Example 2:</strong> Stock critical spare parts on-site — extra hard drives, "
        "power supplies, network switches, and memory modules for your most important systems. "
        "Maintain a spare parts inventory list and reorder when stock drops below your "
        "minimum threshold.</p>"
    ),

    "ma-6-1": (
        "<p>Preventive maintenance means performing regular, scheduled upkeep to prevent "
        "failures before they happen — like changing oil in a car. This applies to both "
        "hardware and software systems.</p>"
        "<p><strong>Example 1:</strong> Schedule quarterly server maintenance windows for "
        "firmware updates, disk health checks (S.M.A.R.T. monitoring), fan cleaning, and "
        "UPS battery testing. Create recurring tasks in your ticketing system to ensure "
        "these are not forgotten.</p>"
        "<p><strong>Example 2:</strong> Set up automated health checks using PowerShell scripts "
        "or monitoring tools (Nagios, PRTG, Zabbix) that run daily and check disk space, "
        "event logs for hardware errors, certificate expiration dates, and backup success "
        "status. Address warnings before they become failures.</p>"
    ),

    "ma-6-2": (
        "<p>Predictive maintenance goes beyond preventive — it uses data and analytics to "
        "predict when a component is likely to fail so you can replace it proactively. "
        "Think of it as using trends and telemetry to forecast problems.</p>"
        "<p><strong>Example 1:</strong> Use S.M.A.R.T. monitoring tools (CrystalDiskInfo or "
        "your server management interface like Dell iDRAC or HP iLO) to track hard drive "
        "health metrics over time. Replace drives showing degrading metrics before they fail "
        "and cause downtime.</p>"
        "<p><strong>Example 2:</strong> Deploy a monitoring solution like Datadog, SolarWinds, "
        "or Azure Monitor that tracks hardware telemetry trends — CPU temperatures, memory "
        "errors, fan speeds. Set alerts for metrics trending toward failure thresholds so you "
        "can schedule replacement during planned maintenance windows.</p>"
    ),

    "ma-6-3": (
        "<p>This enhancement requires automated tools to collect and transfer predictive "
        "maintenance data to a maintenance management system. This removes the manual step "
        "of checking health metrics and automates the workflow.</p>"
        "<p><strong>Example 1:</strong> Configure your server management tools (Dell OpenManage, "
        "HP OneView, or Lenovo XClarity) to automatically feed hardware health data into "
        "your IT service management platform (ServiceNow, Jira). When a component health "
        "alert triggers, a maintenance ticket is automatically created.</p>"
        "<p><strong>Example 2:</strong> Use Azure Monitor or AWS CloudWatch to collect "
        "infrastructure health metrics and set up automated alerts that create maintenance "
        "requests in your ticketing system when predictive thresholds are crossed — for "
        "example, when a disk's remaining useful life drops below 20 percent.</p>"
    ),

    "ma-7": (
        "<p>Field maintenance — repairing or servicing equipment at the location where it is "
        "deployed rather than in a controlled repair facility — may need to be restricted or "
        "prohibited for certain systems due to security risks.</p>"
        "<p><strong>Example 1:</strong> For systems processing CUI or classified data, require "
        "that all hardware repairs be performed in your secured facility, not at a vendor's "
        "workshop. If a drive fails, replace it on-site and destroy the failed drive according "
        "to your media sanitization policy rather than sending it out for warranty replacement.</p>"
        "<p><strong>Example 2:</strong> Document in your maintenance policy which systems require "
        "in-house-only maintenance and which can be serviced in the field. For field-serviceable "
        "equipment, ensure all storage media is removed and secured before the equipment leaves "
        "your facility. Track the chain of custody in your maintenance log.</p>"
    ),

    # ── Media Protection (MP) ──────────────────────────────────────────

    "mp-1": (
        "<p>Your media protection policy defines how your organization handles, stores, "
        "transports, and destroys media that contains data — hard drives, USB drives, backup "
        "tapes, printed documents, and anything else that holds information.</p>"
        "<p><strong>Example 1:</strong> Write a Media Protection Policy that covers all media "
        "types used in your organization. Include sections on labeling requirements, storage "
        "locations, transport procedures, and destruction methods. Store it in your SharePoint "
        "policy library and review it annually.</p>"
        "<p><strong>Example 2:</strong> Use a policy management platform or a simple Word "
        "document with version tracking. Distribute the policy to all employees and require "
        "signed acknowledgments. Include media handling in your annual security awareness "
        "training to reinforce the requirements.</p>"
    ),

    "mp-2": (
        "<p>Access to media containing organizational data — both digital and physical — must "
        "be restricted to authorized individuals only. Not everyone in your office needs access "
        "to backup tapes, external drives, or printed reports.</p>"
        "<p><strong>Example 1:</strong> Store backup tapes, external hard drives, and removable "
        "media in a locked cabinet or safe in your server room. Limit key or combination access "
        "to your system administrator and backup operator. Maintain a sign-out log for any "
        "media removed from storage.</p>"
        "<p><strong>Example 2:</strong> Use a GPO to control USB storage device access on "
        "workstations. Configure the policy at <em>Computer Configuration → Administrative "
        "Templates → System → Removable Storage Access</em> to deny read/write access to "
        "removable storage devices for all users except those in an approved security group.</p>"
    ),

    "mp-2-1": (
        "<p>This enhancement requires automated mechanisms to restrict access to media storage "
        "areas. Instead of relying solely on physical locks and manual sign-out logs, you use "
        "electronic controls.</p>"
        "<p><strong>Example 1:</strong> Install electronic access control (badge reader or "
        "keypad) on the door to your media storage room or cabinet. Log all access attempts "
        "and review them monthly. Configure alerts for access attempts outside business hours.</p>"
        "<p><strong>Example 2:</strong> For digital media access, configure Microsoft Purview "
        "Information Protection or a DLP solution to automatically restrict access to "
        "sensitive files based on classification labels. Only users with the appropriate "
        "permissions can access or copy media containing labeled content.</p>"
    ),

    "mp-2-2": (
        "<p>This enhancement requires cryptographic protection for media. Encryption ensures "
        "that even if someone gains physical access to the media, they cannot read the data "
        "without the decryption key.</p>"
        "<p><strong>Example 1:</strong> Enable BitLocker on all laptop drives and removable "
        "media through GPO at <em>Computer Configuration → Administrative Templates → Windows "
        "Components → BitLocker Drive Encryption</em>. Require BitLocker To Go for any USB "
        "storage device used with company systems. Store recovery keys in Active Directory.</p>"
        "<p><strong>Example 2:</strong> Use hardware-encrypted USB drives (such as Kingston "
        "IronKey or Apricorn Aegis) for any removable media that stores organizational data. "
        "Purchase only FIPS 140-2 validated encrypted drives and document approved models in "
        "your media protection policy.</p>"
    ),

    "mp-3": (
        "<p>Media containing organizational data needs to be clearly marked with distribution "
        "limitations and handling instructions. If someone picks up a drive or document, they "
        "should immediately know how sensitive it is and how to handle it.</p>"
        "<p><strong>Example 1:</strong> Create a media labeling standard: apply CUI marking "
        "labels to USB drives, backup tapes, and external hard drives that contain controlled "
        "information. Use pre-printed labels or a label maker with your organization's CUI "
        "banner marking (e.g., 'CUI//SP-CTI').</p>"
        "<p><strong>Example 2:</strong> For printed documents, configure your printers to "
        "automatically add header and footer banners showing the sensitivity level. In "
        "Microsoft 365, use sensitivity labels in Microsoft Purview to automatically apply "
        "headers, footers, and watermarks to documents based on their classification.</p>"
    ),

    "mp-4": (
        "<p>Media containing organizational data must be physically controlled and securely "
        "stored. This means locked storage in a protected area — not sitting loose on desks "
        "or in unlocked drawers.</p>"
        "<p><strong>Example 1:</strong> Store all removable media (USB drives, backup tapes, "
        "external drives) in a GSA-approved security container or a locked media safe when "
        "not in active use. Keep the safe in a room with access controls. Maintain an "
        "inventory of all stored media and verify it quarterly.</p>"
        "<p><strong>Example 2:</strong> For server hard drives, ensure they are stored in "
        "locked server racks within a secured server room with badge access. When drives are "
        "decommissioned, remove them from the server and transfer them immediately to secure "
        "storage pending sanitization or destruction.</p>"
    ),

    "mp-4-1": (
        "<p>This enhancement requires cryptographic protection for media in storage. Even in "
        "a locked cabinet, encrypted media provides an additional layer of defense against "
        "theft or unauthorized access.</p>"
        "<p><strong>Example 1:</strong> Enable BitLocker full-disk encryption on all systems "
        "and removable media. For servers, use BitLocker with TPM and a startup PIN. Store "
        "recovery keys in Active Directory and back them up to a separate secured location.</p>"
        "<p><strong>Example 2:</strong> For backup media, use your backup software's encryption "
        "feature (Veeam, Commvault, or Veritas all support AES-256 encryption for backup jobs). "
        "Enable encryption for all backup jobs and manage encryption keys separately from the "
        "backup media themselves.</p>"
    ),

    "mp-4-2": (
        "<p>This enhancement requires automated access controls for media storage areas, "
        "combined with access logging. You need to know who accessed the media storage and "
        "when, automatically.</p>"
        "<p><strong>Example 1:</strong> Install a badge reader with audit logging on your media "
        "storage room door. Configure the system to log every access attempt (successful and "
        "failed) and forward those logs to your SIEM. Review access logs weekly and investigate "
        "any unauthorized access attempts.</p>"
        "<p><strong>Example 2:</strong> For digital media, configure file share auditing in "
        "Windows. Enable the <em>Audit Object Access</em> policy through GPO and set SACLs "
        "on folders containing sensitive media. Forward audit events (Event IDs 4663, 4656) "
        "to your SIEM for monitoring and alerting.</p>"
    ),

    "mp-5": (
        "<p>When media is transported outside your facility — whether it is a laptop, backup "
        "tape, or USB drive — it needs protection and accountability. You should know where "
        "the media is at all times during transport.</p>"
        "<p><strong>Example 1:</strong> Require all media leaving the facility to be encrypted "
        "(BitLocker, hardware-encrypted drives) and transported in a locked bag or container. "
        "Maintain a media transport log that records what left, when, who carried it, and the "
        "destination. Verify receipt at the destination.</p>"
        "<p><strong>Example 2:</strong> For backup tape offsite rotation, use a bonded courier "
        "service (Iron Mountain, Recall) that provides chain-of-custody documentation. Track "
        "each tape with a barcode or serial number. Reconcile your tape inventory monthly "
        "against the courier's records.</p>"
    ),

    "mp-5-1": (
        "<p>This enhancement is incorporated into the base MP-5 control. Media transported "
        "outside controlled areas needs specific protections — encryption, physical safeguards, "
        "and custody controls.</p>"
        "<p><strong>Example 1:</strong> Issue tamper-evident bags for transporting media outside "
        "your facility. When the recipient opens the bag, any tampering is visible. Log the "
        "bag's serial number in your transport record and have the recipient confirm the seal "
        "was intact upon delivery.</p>"
        "<p><strong>Example 2:</strong> For electronic transport, ensure all files are encrypted "
        "before transfer. Use Microsoft 365 sensitivity labels with encryption, or encrypt "
        "files using 7-Zip with AES-256 before attaching to email or uploading to a file "
        "sharing service.</p>"
    ),

    "mp-5-2": (
        "<p>This enhancement requires you to document all media transport activities. "
        "Good documentation creates an audit trail that proves your media was handled "
        "properly throughout its journey.</p>"
        "<p><strong>Example 1:</strong> Create a Media Transport Form that records: date, "
        "media description and serial number, classification/sensitivity level, sender name, "
        "recipient name, transport method, expected delivery date, and receipt confirmation. "
        "File completed forms in your compliance records.</p>"
        "<p><strong>Example 2:</strong> Use a shared spreadsheet or database to track all media "
        "in transit. Include columns for shipment date, tracking number, contents description, "
        "sender, recipient, and delivery confirmation date. Review for overdue shipments "
        "weekly and investigate any missing media immediately.</p>"
    ),

    "mp-5-3": (
        "<p>An identified custodian — a named, accountable person — must accompany media during "
        "transport outside controlled areas. The media should never be left unattended.</p>"
        "<p><strong>Example 1:</strong> Assign a specific employee as the custodian for each "
        "media shipment. The custodian is responsible for the media from the moment it leaves "
        "storage until it is delivered and receipt is confirmed. Document the custodian's name "
        "on the transport form.</p>"
        "<p><strong>Example 2:</strong> For courier-transported media, the courier company "
        "serves as custodian. Ensure your contract specifies chain-of-custody requirements "
        "and that the courier provides signed delivery receipts. Retain these receipts in "
        "your compliance files for at least the retention period specified in your policy.</p>"
    ),

    "mp-5-4": (
        "<p>This enhancement requires cryptographic protection for media during transport. "
        "Encryption ensures that even if media is lost or stolen in transit, the data remains "
        "protected.</p>"
        "<p><strong>Example 1:</strong> Use BitLocker To Go to encrypt all USB drives before "
        "they leave your facility. For backup tapes, enable encryption at the backup software "
        "level (Veeam AES-256, Commvault encryption). Never transport unencrypted media "
        "containing sensitive data.</p>"
        "<p><strong>Example 2:</strong> For laptop transport, ensure BitLocker is enabled with "
        "pre-boot authentication. Use hardware-encrypted portable drives (FIPS 140-2 validated) "
        "for any data that needs to travel. Document the encryption method used on the media "
        "transport form.</p>"
    ),

    "mp-6": (
        "<p>Before you dispose of media, release it outside your organization, or reuse it for "
        "a different purpose, you must sanitize it — remove all data in a way that prevents "
        "recovery. Simple file deletion is not sanitization.</p>"
        "<p><strong>Example 1:</strong> For hard drives being reused internally, use NIST "
        "800-88 Clear methods — a full disk overwrite using a tool like DBAN (Darik's Boot "
        "and Nuke) or the built-in <em>cipher /w:C:\\</em> command on Windows. For drives "
        "being disposed of, use Purge or Destroy methods.</p>"
        "<p><strong>Example 2:</strong> For SSDs, use the manufacturer's secure erase utility "
        "(Samsung Magician, Intel SSD Toolbox) or physically destroy them with a drive shredder. "
        "Standard overwrite tools do not reliably sanitize SSDs due to wear leveling. Document "
        "every sanitization action in a media disposition log with date, method, and witness.</p>"
    ),

    "mp-6-1": (
        "<p>This enhancement adds formal review, approval, tracking, documentation, and "
        "verification steps to your media sanitization process. Every sanitization action "
        "needs oversight and a paper trail.</p>"
        "<p><strong>Example 1:</strong> Create a Media Sanitization Record form that requires: "
        "media description and serial number, sanitization method, date, technician name, "
        "witness name, verification method (e.g., attempted data recovery), and supervisor "
        "approval. File these records for your retention period.</p>"
        "<p><strong>Example 2:</strong> Use an asset management tool (Snipe-IT, ServiceNow "
        "Asset Management) to track media through its lifecycle from deployment to sanitization "
        "to destruction. Require sign-off at each stage. Run a quarterly reconciliation to "
        "ensure every decommissioned asset has a corresponding sanitization record.</p>"
    ),

    "mp-6-2": (
        "<p>Your sanitization equipment and procedures need to be tested regularly to confirm "
        "they actually work. A degausser that has lost strength or a wipe tool with a bug "
        "could leave your data exposed.</p>"
        "<p><strong>Example 1:</strong> Test your degausser annually by degaussing a test "
        "tape or disk and then attempting data recovery using forensic tools. If data is "
        "recoverable, the degausser needs service or replacement. Document the test results.</p>"
        "<p><strong>Example 2:</strong> After running your disk sanitization tool (DBAN, "
        "Blancco, or similar), spot-check a percentage of sanitized drives by connecting "
        "them to a forensic workstation and scanning for residual data. Keep a log of "
        "verification tests with pass/fail results for each batch.</p>"
    ),

    "mp-6-3": (
        "<p>Before plugging a portable storage device into your system, sanitize it using "
        "nondestructive methods (like a full format or overwrite) to remove any potential "
        "threats. This prevents malware from jumping onto your network via removable media.</p>"
        "<p><strong>Example 1:</strong> Set up a standalone, air-gapped sanitization workstation "
        "where all incoming USB devices are scanned and wiped before use. Run a full antivirus "
        "scan followed by a secure format. Only after clearance can the device be used on "
        "production systems.</p>"
        "<p><strong>Example 2:</strong> Use an automated media sanitization kiosk (like OPSWAT "
        "MetaDefender Kiosk) that scans removable media with multiple antivirus engines and "
        "can perform data sanitization. Place the kiosk at your facility entrance so all "
        "incoming media goes through it before entering the network.</p>"
    ),

    "mp-6-4": (
        "<p>Media containing Controlled Unclassified Information (CUI) must be sanitized "
        "according to NIST SP 800-88 guidelines before disposal or reuse. CUI requires "
        "at least the Clear sanitization level for reuse and Purge or Destroy for disposal.</p>"
        "<p><strong>Example 1:</strong> Follow NIST SP 800-88 Rev 1 guidelines: for magnetic "
        "media containing CUI, perform a Clear (overwrite) for internal reuse or a Purge "
        "(degauss) for release outside the organization. For disposal, physically destroy "
        "the media using a shredder or disintegrator.</p>"
        "<p><strong>Example 2:</strong> Create a CUI Media Disposition checklist specific to "
        "your organization. Map each media type (HDD, SSD, USB, paper) to the required "
        "sanitization method. Include this checklist in your media protection procedures and "
        "train all IT staff on its use.</p>"
    ),

    "mp-6-5": (
        "<p>Classified media requires sanitization and destruction procedures approved by the "
        "cognizant security agency. These requirements are more stringent than CUI handling "
        "and are defined by NSA and the classification guide.</p>"
        "<p><strong>Example 1:</strong> For classified media, follow NSA/CSS EPL (Evaluated "
        "Products List) approved methods for sanitization and destruction. Use NSA-approved "
        "degaussers for magnetic media and NSA-listed disintegrators or shredders for physical "
        "destruction. Document every action on the appropriate security forms.</p>"
        "<p><strong>Example 2:</strong> Maintain a classified media destruction log that your "
        "FSO reviews monthly. Include media type, serial number, classification level, "
        "destruction method, date, and two witness signatures. Follow your classification "
        "management plan for retention of destruction records.</p>"
    ),

    "mp-6-6": (
        "<p>This enhancement specifically addresses physical destruction of media — shredding, "
        "disintegrating, pulverizing, or incinerating media to make data recovery physically "
        "impossible.</p>"
        "<p><strong>Example 1:</strong> Purchase a hard drive shredder or contract with a "
        "certified destruction vendor (Iron Mountain, Shred-it) that provides on-site "
        "destruction services with certificates of destruction. Require the vendor to "
        "destroy drives at your location while your staff witnesses the process.</p>"
        "<p><strong>Example 2:</strong> For paper documents and optical media, use a "
        "cross-cut shredder rated to P-4 or higher (DIN 66399 standard). For drives, "
        "if a shredder is not available, use a drill press to put multiple holes through "
        "the platters. Document every destruction event with serial numbers, date, method, "
        "and witness.</p>"
    ),

    "mp-6-7": (
        "<p>Dual authorization means two people must be involved in the sanitization process — "
        "one to perform the sanitization and another to verify and authorize it. This prevents "
        "a single person from improperly handling sensitive media.</p>"
        "<p><strong>Example 1:</strong> Require two authorized employees to be present for all "
        "media sanitization of CUI or higher. One person performs the sanitization while the "
        "other observes and signs as witness on the sanitization record. Neither person can "
        "complete the process alone.</p>"
        "<p><strong>Example 2:</strong> In your ticketing system, create a media sanitization "
        "workflow that requires two separate approvals — the technician performing the work "
        "and a supervisor or security officer verifying completion. The ticket cannot be closed "
        "without both approvals recorded.</p>"
    ),

    "mp-6-8": (
        "<p>This enhancement provides the ability to remotely wipe or purge data from devices — "
        "critical for lost or stolen laptops, phones, and tablets. If a device goes missing, "
        "you need to erase it before the data is compromised.</p>"
        "<p><strong>Example 1:</strong> Enroll all company mobile devices and laptops in "
        "Microsoft Intune or another MDM solution. Enable remote wipe capability so you can "
        "erase a device's data immediately when it is reported lost or stolen. Test the "
        "remote wipe function on a test device quarterly.</p>"
        "<p><strong>Example 2:</strong> Configure Microsoft 365 Exchange Online with remote "
        "wipe policies for mobile devices accessing corporate email. In the Exchange admin "
        "center, under <em>Mobile → Mobile Device Access</em>, enable remote wipe capability. "
        "Document the procedure for initiating a remote wipe in your IR plan.</p>"
    ),

    "mp-7": (
        "<p>This control governs how and where different types of media can be used within your "
        "organization. You might allow certain media types, restrict others, and prohibit some "
        "entirely — particularly portable storage devices without an identifiable owner.</p>"
        "<p><strong>Example 1:</strong> Create a GPO to restrict or prohibit the use of removable "
        "storage devices. Configure it at <em>Computer Configuration → Administrative Templates "
        "→ System → Removable Storage Access</em>. Block all removable storage by default and "
        "create exceptions only for approved, encrypted devices assigned to specific users.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Defender for Endpoint's Device Control "
        "feature to allow only specific approved USB devices (by vendor ID or serial number). "
        "Block all other removable media automatically and generate an alert when someone "
        "tries to use an unauthorized device.</p>"
    ),

    "mp-7-1": (
        "<p>Portable storage devices without an identifiable owner should not be used on your "
        "systems. If you find a random USB drive in the parking lot, plugging it in could "
        "introduce malware or be an intentional social engineering attack.</p>"
        "<p><strong>Example 1:</strong> Include a section in your security awareness training "
        "about the danger of unknown USB devices. Train employees to never plug in found or "
        "unidentified media. Instead, they should turn it in to IT security for safe inspection "
        "on an isolated workstation.</p>"
        "<p><strong>Example 2:</strong> Label all company-owned USB devices with asset tags "
        "or engravings that include the organization name and an asset number. Configure your "
        "endpoint protection to block USB devices that do not match your approved device list. "
        "Any unlabeled device is treated as unauthorized.</p>"
    ),

    "mp-7-2": (
        "<p>Some media types cannot be effectively sanitized due to their physical design — "
        "for example, certain types of flash memory, optical media, or devices with embedded "
        "storage. These should not be used on systems handling sensitive data.</p>"
        "<p><strong>Example 1:</strong> Maintain a list of prohibited media types in your media "
        "protection policy. Include CD-Rs (cannot be erased), certain IoT devices with embedded "
        "non-removable storage, and any storage device that does not support verified "
        "sanitization. Train staff on these restrictions.</p>"
        "<p><strong>Example 2:</strong> Configure your device control policies (via Intune, "
        "GPO, or endpoint protection tools) to block device classes that cannot be sanitized. "
        "Block generic mass storage devices and only allow specific hardware-encrypted, "
        "remotely wipeable devices that support verified sanitization.</p>"
    ),

    "mp-8": (
        "<p>Media downgrading is the process of reducing the classification or sensitivity level "
        "of media so it can be used in a lower-security environment. This requires approved "
        "procedures and verification that the downgrading was successful.</p>"
        "<p><strong>Example 1:</strong> Establish a media downgrading process document that "
        "defines which media types can be downgraded, the approved sanitization methods for "
        "each type, verification procedures, and who has authority to approve downgrades. "
        "Get this approved by your security officer or ISSM.</p>"
        "<p><strong>Example 2:</strong> For hard drives being downgraded from classified to "
        "unclassified use, use an NSA-approved sanitization method, verify with a forensic "
        "scan, and have the downgrade authorized in writing by the appropriate official. "
        "Re-mark the media with its new classification level after downgrading.</p>"
    ),

    "mp-8-1": (
        "<p>Every media downgrading action needs to be documented — what was downgraded, "
        "from what level to what level, the method used, and who authorized it.</p>"
        "<p><strong>Example 1:</strong> Create a Media Downgrading Record form with fields for: "
        "original classification, target classification, media type and serial number, "
        "sanitization method, technician name, verifier name, authorizing official, and date. "
        "File completed records with your security documentation.</p>"
        "<p><strong>Example 2:</strong> Log all downgrading actions in your asset management "
        "system. Update the media record to reflect the new classification level, the date "
        "of downgrade, and who authorized it. This creates an audit trail that can be reviewed "
        "during security inspections.</p>"
    ),

    "mp-8-2": (
        "<p>Just like sanitization equipment, your media downgrading equipment and procedures "
        "need to be tested to confirm they work correctly. A flawed downgrade could release "
        "sensitive data into an unprotected environment.</p>"
        "<p><strong>Example 1:</strong> Test your downgrading procedures annually by performing "
        "a downgrade on test media and then attempting data recovery using forensic tools. "
        "If any data is recoverable, revise your procedures or replace your equipment.</p>"
        "<p><strong>Example 2:</strong> If you use a degausser for downgrading magnetic media, "
        "have it calibrated and tested according to the manufacturer's specifications. Document "
        "each calibration test with the date, results, and the name of the person who performed "
        "the test.</p>"
    ),

    "mp-8-3": (
        "<p>CUI media must be properly sanitized before it can be released to the public or "
        "downgraded for use in environments that do not protect CUI. Follow NIST SP 800-88 "
        "guidance for the appropriate sanitization level.</p>"
        "<p><strong>Example 1:</strong> Before releasing any media that previously contained "
        "CUI for public use, perform a Purge-level sanitization per NIST SP 800-88. Verify "
        "the sanitization was successful by attempting data recovery. Document the sanitization "
        "and verification on your media disposition form.</p>"
        "<p><strong>Example 2:</strong> Create a CUI downgrading checklist: identify the CUI "
        "categories on the media, select the appropriate sanitization method from NIST 800-88, "
        "perform the sanitization, verify, get supervisor approval, re-label the media, and "
        "file the record. Include this checklist in your CUI handling procedures.</p>"
    ),

    "mp-8-4": (
        "<p>Classified media requires approved downgrading procedures before it can be released "
        "to individuals without the required clearances. This is governed by classification "
        "guides and cognizant security agency requirements.</p>"
        "<p><strong>Example 1:</strong> Follow your cognizant security agency's approved "
        "procedures for downgrading classified media. This typically involves NSA-approved "
        "sanitization methods, verification by a trained professional, and written authorization "
        "from your security officer or classification authority.</p>"
        "<p><strong>Example 2:</strong> Maintain a classified media downgrading log reviewed "
        "by your FSO. Each entry must include: the original classification, downgrade "
        "authorization reference, sanitization method used, verification results, the "
        "authorizing official's signature, and the new classification marking applied "
        "to the media.</p>"
    ),

    # ── Physical & Environmental Protection (PE) ───────────────────────

    "pe-1": (
        "<p>This control requires a documented physical and environmental protection policy. "
        "It covers who can access your facilities, how they gain access, and how you protect "
        "your physical environment — power, fire, water, temperature — from threats.</p>"
        "<p><strong>Example 1:</strong> Write a Physical Security Policy that covers facility "
        "access controls, visitor management, security monitoring, environmental protections, "
        "and emergency procedures. Store it in your policy library on SharePoint and review "
        "it annually or after any physical security incident.</p>"
        "<p><strong>Example 2:</strong> Pair your policy with documented procedures — step-by-step "
        "instructions for issuing access badges, escorting visitors, responding to fire alarms, "
        "and handling after-hours access requests. Train all employees on these procedures "
        "during onboarding and refresh the training annually.</p>"
    ),

    "pe-2": (
        "<p>You need a formal list of who is allowed physical access to the facility where your "
        "systems are located. This list must be reviewed regularly and credentials must be "
        "issued, updated, and revoked as people come and go.</p>"
        "<p><strong>Example 1:</strong> Maintain a physical access authorization list in a "
        "spreadsheet or access control system database. For each authorized person, record "
        "their name, role, access level (full facility vs. specific areas), badge number, "
        "and authorization date. Review the list quarterly and remove anyone who no longer "
        "needs access.</p>"
        "<p><strong>Example 2:</strong> Use a physical access control system (PACS) like "
        "Lenel, AMAG, or Honeywell to manage badge access. Integrate it with your HR system "
        "so when an employee is terminated, their badge is automatically deactivated. Run a "
        "monthly report of active badges and cross-reference against current employees.</p>"
    ),

    "pe-2-1": (
        "<p>Instead of (or in addition to) authorizing access for specific individuals, you "
        "can authorize access based on position or role. For example, all IT administrators "
        "get server room access, all executives get executive suite access.</p>"
        "<p><strong>Example 1:</strong> Define access levels tied to job roles in your access "
        "control system: 'IT Staff' gets server room access, 'All Employees' get general "
        "office access, 'Executives' get the executive floor. When someone changes roles, "
        "update their access profile to match their new position.</p>"
        "<p><strong>Example 2:</strong> Document role-based physical access in a matrix "
        "showing which roles can access which areas. Include this matrix in your physical "
        "security procedures. When a new employee is onboarded, HR provides their role and "
        "your badge administrator grants the corresponding access profile.</p>"
    ),

    "pe-2-2": (
        "<p>Visitors to your facility must present two forms of identification before being "
        "granted access. This adds confidence that the person is who they claim to be.</p>"
        "<p><strong>Example 1:</strong> Require visitors to present a government-issued photo "
        "ID (driver's license or passport) plus a second form such as a company badge from "
        "their employer, a meeting confirmation email, or a business card. Record both forms "
        "of ID in the visitor log.</p>"
        "<p><strong>Example 2:</strong> Train your front desk or security staff on acceptable "
        "forms of identification and how to verify them. Create a quick-reference guide that "
        "lists approved primary IDs (government photo ID) and approved secondary IDs (CAC, "
        "company badge, verified appointment). Post this guide at the reception desk.</p>"
    ),

    "pe-2-3": (
        "<p>Unescorted access to your facility — the ability to move around without someone "
        "watching you — should be restricted to personnel who meet specific criteria like "
        "security clearance, background checks, or employment status.</p>"
        "<p><strong>Example 1:</strong> Configure your badge access system so that only employees "
        "with completed background investigations can access the facility unescorted. Visitors "
        "and new employees pending background check completion receive a visitor badge that "
        "requires escort.</p>"
        "<p><strong>Example 2:</strong> Post signage at facility entrances reminding staff that "
        "all visitors and uncleared personnel must be escorted at all times. Include escort "
        "responsibilities in your security awareness training — the escort must remain in "
        "visual contact with the visitor at all times.</p>"
    ),

    "pe-3": (
        "<p>Physical access controls enforce your access authorization decisions at the door. "
        "This means locks, badge readers, guards, or other mechanisms that verify someone is "
        "authorized before letting them in.</p>"
        "<p><strong>Example 1:</strong> Install electronic badge readers at all entry points to "
        "your facility and server room. Configure the system to log every access (granted and "
        "denied). Require badge + PIN for high-security areas like the server room. Test all "
        "door hardware quarterly to ensure locks and readers function properly.</p>"
        "<p><strong>Example 2:</strong> For a smaller office, use commercial-grade electronic "
        "locks (like Kaba, Schlage, or HID) with access logging. Change access codes regularly "
        "and immediately when an employee departs. Install a deadbolt backup in case the "
        "electronic system fails. Maintain a physical key log for any keyed entry points.</p>"
    ),

    "pe-3-1": (
        "<p>Beyond controlling access to the building, you need to control access to the "
        "systems themselves — the server room, network closets, and any area where IT "
        "equipment is installed.</p>"
        "<p><strong>Example 1:</strong> Install a separate badge reader on your server room "
        "door with a more restricted access list than the general facility. Only IT staff "
        "and authorized maintenance personnel should have server room badges. Log all "
        "entries and review logs weekly.</p>"
        "<p><strong>Example 2:</strong> For network closets (IDF/MDF rooms), install key locks "
        "at a minimum, or electronic locks with logging for higher-security environments. "
        "Ensure these rooms are not left propped open. Include network closet checks in your "
        "building security rounds.</p>"
    ),

    "pe-3-2": (
        "<p>This enhancement requires periodic security checks at the physical perimeter — "
        "looking for signs of tampering, unauthorized equipment, or exfiltration of data "
        "or equipment.</p>"
        "<p><strong>Example 1:</strong> Conduct daily walkthroughs of your facility perimeter "
        "and server rooms. Check that doors and windows are secure, no unauthorized equipment "
        "has been installed, and no company equipment is staged for unauthorized removal. "
        "Use a checklist and log each walkthrough.</p>"
        "<p><strong>Example 2:</strong> Perform random bag/equipment checks at exits during "
        "high-risk periods or as part of your ongoing security program. Post signage informing "
        "employees and visitors that equipment inspections may occur. Document any findings "
        "and report anomalies to your security officer.</p>"
    ),

    "pe-3-3": (
        "<p>This enhancement requires 24/7 security guard presence at your facility. This is "
        "typically reserved for high-security environments processing classified information "
        "or critical infrastructure.</p>"
        "<p><strong>Example 1:</strong> Contract with a licensed security guard service to "
        "provide 24/7 coverage at your facility. Define guard duties in the contract: access "
        "control, patrol routes, incident response, visitor processing, and alarm monitoring. "
        "Review guard logs daily.</p>"
        "<p><strong>Example 2:</strong> If in-house guards are used, establish written post "
        "orders that detail responsibilities, patrol schedules, and emergency procedures. "
        "Equip guards with communication devices and ensure they can reach your security "
        "manager and local law enforcement. Conduct random quality checks on guard performance.</p>"
    ),

    "pe-3-4": (
        "<p>System components should be housed in lockable casings to prevent unauthorized "
        "physical access. This stops someone from walking up to a server and pulling a drive "
        "or plugging in a rogue device.</p>"
        "<p><strong>Example 1:</strong> Use locking server rack cabinets with keyed or "
        "combination locks. Restrict keys to authorized IT staff only and maintain a key "
        "control log. When installing equipment in shared spaces, use locking network "
        "enclosures for switches and patch panels.</p>"
        "<p><strong>Example 2:</strong> For workstations in public or shared areas (like "
        "reception or manufacturing floor), use locking computer cases and cable locks to "
        "secure laptops to desks. Install port blockers on unused USB ports to prevent "
        "unauthorized device connections.</p>"
    ),

    "pe-3-5": (
        "<p>Tamper protection detects or prevents physical tampering with your hardware. This "
        "could mean tamper-evident seals, intrusion detection switches on server cases, or "
        "other mechanisms that alert you when someone opens or modifies equipment.</p>"
        "<p><strong>Example 1:</strong> Apply tamper-evident seals (serialized security tape "
        "or holographic stickers) to server cases, network equipment, and cable connections. "
        "During regular inspections, check that seals are intact and serial numbers match. "
        "Investigate and document any broken seals immediately.</p>"
        "<p><strong>Example 2:</strong> Enable chassis intrusion detection in server BIOS/UEFI "
        "settings (available on most Dell, HP, and Lenovo servers). Configure the server to "
        "log or alert when the chassis is opened. Forward these alerts to your monitoring "
        "system for investigation.</p>"
    ),

    "pe-3-6": (
        "<p>This enhancement calls for physical penetration testing of your facility — hiring "
        "professionals to attempt to bypass your physical security controls, just like you "
        "would test your network with a penetration test.</p>"
        "<p><strong>Example 1:</strong> Hire a physical security assessment firm to test your "
        "facility annually. They will attempt to tailgate through doors, bypass badge readers, "
        "pick locks, and access restricted areas using social engineering. Use their findings "
        "to improve your physical security posture.</p>"
        "<p><strong>Example 2:</strong> Conduct internal physical security tests where a trusted "
        "employee (unknown to most staff) attempts to access restricted areas or remove "
        "equipment without authorization. Track how far they get before being challenged. "
        "Use results to reinforce security awareness training and tighten procedures.</p>"
    ),

    "pe-3-7": (
        "<p>Physical barriers — fences, walls, bollards, planters — limit access to your "
        "facility by creating physical obstacles that direct people to controlled entry points.</p>"
        "<p><strong>Example 1:</strong> Install perimeter fencing around your facility with "
        "controlled entry gates. Use anti-climb fencing (topped with barbed wire or similar) "
        "for high-security areas. Ensure all perimeter barriers funnel foot and vehicle "
        "traffic to monitored access points.</p>"
        "<p><strong>Example 2:</strong> For office buildings, use lobby turnstiles or access "
        "gates that require badge authentication. Install reinforced doors with anti-tailgating "
        "features on critical areas. Use bollards or planters to prevent vehicle approach to "
        "building entrances where systems are located.</p>"
    ),

    "pe-3-8": (
        "<p>Access control vestibules — also called mantraps or airlocks — are small rooms "
        "between two interlocking doors where only one door can be open at a time. They prevent "
        "tailgating and piggybacking into secured areas.</p>"
        "<p><strong>Example 1:</strong> Install an access control vestibule at the entrance to "
        "your server room or data center. Configure it so the outer door must close and lock "
        "before the inner door will open. Require badge authentication at both doors to prevent "
        "unauthorized entry.</p>"
        "<p><strong>Example 2:</strong> For existing facilities where a physical vestibule is "
        "not practical, implement an anti-tailgating system using optical turnstiles with "
        "sensors that detect when more than one person passes per badge swipe. Alert security "
        "when tailgating is detected.</p>"
    ),

    "pe-4": (
        "<p>Transmission media — network cabling, fiber optic lines, and wireless access points — "
        "need physical protection to prevent wiretapping, signal interception, or physical "
        "damage that could disrupt communications.</p>"
        "<p><strong>Example 1:</strong> Run network cabling through conduit or cable trays in "
        "secure areas. Avoid running cables through public spaces or areas accessible to "
        "visitors. Use locked network closets for patch panels and switches. Install physical "
        "port security (port blockers) on unused switch ports.</p>"
        "<p><strong>Example 2:</strong> For wireless networks, position access points to minimize "
        "signal leakage outside your facility. Use directional antennas where possible and "
        "reduce transmit power to cover only required areas. Conduct periodic wireless surveys "
        "to detect rogue access points using tools like NetStumbler or Ekahau.</p>"
    ),

    "pe-5": (
        "<p>Output devices — printers, monitors, fax machines, audio devices — produce data "
        "that anyone nearby can see or hear. You need to control physical access to prevent "
        "unauthorized people from viewing or taking printed output.</p>"
        "<p><strong>Example 1:</strong> Place printers in areas accessible only to authorized "
        "personnel — not in public hallways or reception areas. Enable pull printing (also "
        "called follow-me printing) using a solution like PaperCut, Pharos, or the printer's "
        "built-in feature, so documents only print when the user authenticates at the printer.</p>"
        "<p><strong>Example 2:</strong> Position monitors so they face away from windows and "
        "walkways. Install privacy screens on monitors in shared workspaces. For fax machines "
        "receiving sensitive documents, place them in a locked room and assign someone to "
        "retrieve and distribute incoming faxes promptly.</p>"
    ),

    "pe-5-1": (
        "<p>This enhancement ensures that only authorized individuals can access output from "
        "devices — for example, requiring authentication before a document prints.</p>"
        "<p><strong>Example 1:</strong> Implement badge-release printing where users must "
        "tap their access badge at the printer to release their print jobs. This prevents "
        "documents from sitting uncollected in the printer tray. Solutions like PaperCut "
        "or Ricoh SmartDeviceMonitor support this.</p>"
        "<p><strong>Example 2:</strong> For network-connected multifunction printers, configure "
        "access controls so that only authorized users can access scan-to-email, fax, and "
        "copy functions. Require PIN or badge authentication for all printer functions, not "
        "just printing.</p>"
    ),

    "pe-5-2": (
        "<p>This enhancement links each piece of output to the individual who produced it, "
        "creating accountability. If a sensitive document is found in the wrong place, you "
        "can trace it back to who printed it.</p>"
        "<p><strong>Example 1:</strong> Enable print logging on your print server that records "
        "the username, document name, printer used, and timestamp for every print job. In "
        "Windows, enable <em>Audit Object Access</em> on the print server or use a print "
        "management tool like PaperCut to maintain detailed logs.</p>"
        "<p><strong>Example 2:</strong> Configure printers to stamp a user ID or watermark on "
        "printed output. Some enterprise printers support automatic header/footer insertion "
        "with the username and date. This makes every printed page traceable to the individual "
        "who printed it.</p>"
    ),

    "pe-5-3": (
        "<p>Output devices need to be labeled to indicate the sensitivity level of information "
        "they are approved to handle. A printer in the classified area should be clearly "
        "marked differently from one in the unclassified area.</p>"
        "<p><strong>Example 1:</strong> Label all printers, fax machines, and multifunction "
        "devices with the highest classification level of data they are authorized to process. "
        "Use color-coded labels — for example, green for unclassified, yellow for CUI, red "
        "for classified — placed prominently on the device.</p>"
        "<p><strong>Example 2:</strong> Include output device markings in your facility security "
        "documentation and diagrams. When new devices are installed, the security team must "
        "approve the marking and location before the device goes into service. Include device "
        "marking checks in your regular security walkthroughs.</p>"
    ),

    "pe-6": (
        "<p>You need to monitor who is physically entering and leaving your facility and the "
        "areas where your systems are located. This means access logs, cameras, guards, or a "
        "combination — and someone needs to actually review the records.</p>"
        "<p><strong>Example 1:</strong> Configure your badge access system to log all entry "
        "and exit events. Review access logs weekly for anomalies — access during unusual hours, "
        "repeated denied access attempts, or access by individuals no longer authorized. "
        "Investigate and document any anomalies found.</p>"
        "<p><strong>Example 2:</strong> Install security cameras at all facility entry points, "
        "server room doors, and loading docks. Store recordings for at least 90 days. When "
        "an access anomaly is detected in badge logs, cross-reference with camera footage "
        "to identify the individual and their activities.</p>"
    ),

    "pe-6-1": (
        "<p>This enhancement requires intrusion alarms and surveillance equipment to monitor "
        "physical access. You need systems that can detect unauthorized entry attempts and "
        "record who enters and when.</p>"
        "<p><strong>Example 1:</strong> Install intrusion detection sensors (door contacts, "
        "motion detectors, glass break sensors) on all entry points and sensitive areas. "
        "Connect them to a monitored alarm system that alerts your security company and "
        "local law enforcement when triggered after hours.</p>"
        "<p><strong>Example 2:</strong> Deploy IP-based surveillance cameras with motion-triggered "
        "recording and alerts. Use a video management system (VMS) like Milestone, Genetec, "
        "or even a NVR appliance to manage cameras. Configure alerts for motion in restricted "
        "areas after business hours and send notifications to security staff.</p>"
    ),

    "pe-6-2": (
        "<p>This enhancement calls for automated systems that can recognize intrusion attempts "
        "and initiate responses automatically — like locking doors, activating alarms, or "
        "notifying security when specific events are detected.</p>"
        "<p><strong>Example 1:</strong> Configure your intrusion detection system to automatically "
        "lock down areas when a forced entry is detected. For example, if a door contact "
        "sensor registers an unauthorized opening, automatically lock adjacent doors, activate "
        "audible alarms, and notify security via text message.</p>"
        "<p><strong>Example 2:</strong> Use a video analytics platform that can detect "
        "tailgating, loitering, or unauthorized access patterns on camera feeds. When the "
        "system detects suspicious behavior, it triggers a real-time alert to security "
        "personnel with a video clip of the event for immediate assessment.</p>"
    ),

    "pe-6-3": (
        "<p>This enhancement specifically requires video surveillance of designated areas, "
        "with regular review of recordings and retention for a defined period. Cameras "
        "are your eyes when security personnel are not physically present.</p>"
        "<p><strong>Example 1:</strong> Install video surveillance cameras at all building "
        "entrances, server room doors, loading docks, and parking areas. Use cameras with "
        "night vision capability and sufficient resolution to identify individuals. Store "
        "recordings for at least 90 days on a secured NVR or cloud-based storage.</p>"
        "<p><strong>Example 2:</strong> Schedule weekly reviews of video footage from "
        "high-security areas (server room, executive offices). Use a review checklist "
        "to document what was reviewed, the time period covered, and any anomalies found. "
        "Retain review logs as evidence for compliance audits.</p>"
    ),

    "pe-6-4": (
        "<p>Beyond monitoring the facility itself, this enhancement requires monitoring "
        "physical access specifically to your information systems — individual server racks, "
        "network closets, or equipment cabinets within the facility.</p>"
        "<p><strong>Example 1:</strong> Install individual rack-level access controls "
        "(electronic locks with logging) on server cabinets. Use solutions like Chatsworth "
        "Products or Rittal intelligent rack locks that log who opened which cabinet and "
        "when. Forward access logs to your monitoring system.</p>"
        "<p><strong>Example 2:</strong> Place a camera directly covering your server rack "
        "area. When combined with badge reader logs on the server room door, you can "
        "correlate who entered the room with what activity occurred at the racks. Review "
        "recordings whenever unexpected access is logged.</p>"
    ),

    "pe-7": (
        "<p>Visitors to your facility must be controlled — identified, authorized, escorted, "
        "and monitored. No one should wander freely through areas where your systems are "
        "located without proper oversight.</p>"
        "<p><strong>Example 1:</strong> Establish a visitor management process: all visitors "
        "must sign in at reception, present government-issued ID, receive a visitor badge, "
        "and be escorted by an employee at all times. Visitor badges should be visually "
        "distinct from employee badges (different color or marked 'VISITOR').</p>"
        "<p><strong>Example 2:</strong> Use a digital visitor management system like Envoy, "
        "iLobby, or SwipedOn that captures visitor information, takes photos, prints badges, "
        "and notifies the host employee when their visitor arrives. At departure, visitors "
        "must check out and return their badge. Run reports on visitor activity monthly.</p>"
    ),

    "pe-8": (
        "<p>You must maintain a log of all visitors to your facility, including who they visited, "
        "when they arrived and left, and their purpose. These records must be reviewed regularly "
        "and retained for a defined period.</p>"
        "<p><strong>Example 1:</strong> Maintain a visitor log — either a physical sign-in book "
        "or a digital visitor management system — that captures: visitor name, organization, "
        "person being visited, date, arrival time, departure time, badge number issued, and "
        "areas accessed. Review the log weekly for anomalies.</p>"
        "<p><strong>Example 2:</strong> Use a digital visitor management system that automatically "
        "timestamps entries and exits, stores records electronically, and generates reports. "
        "Retain records for at least one year (or longer if required by your contracts or "
        "regulations). Flag any visitor who did not properly check out for investigation.</p>"
    ),

    "pe-8-1": (
        "<p>This enhancement requires automated systems to maintain and review visitor access "
        "records, replacing or augmenting manual sign-in books with electronic systems.</p>"
        "<p><strong>Example 1:</strong> Deploy a digital visitor management system (Envoy, "
        "Traction Guest, or HID Visitor Manager) that integrates with your badge system. "
        "The system automatically logs entry and exit times, generates daily visitor reports, "
        "and alerts security to visitors who overstay their appointment.</p>"
        "<p><strong>Example 2:</strong> Configure automated weekly reports from your visitor "
        "management system that summarize total visitors, repeat visitors, areas accessed, "
        "and any anomalies (unsigned checkouts, off-hours visits). Send these reports to "
        "your security manager for review and file them in your compliance records.</p>"
    ),

    "pe-8-2": (
        "<p>In addition to visitor records, this enhancement requires you to maintain records "
        "of physical access by your own personnel — who badged in where and when.</p>"
        "<p><strong>Example 1:</strong> Your badge access system already generates these records "
        "— make sure they are retained for at least one year, backed up regularly, and reviewed "
        "monthly for anomalies. Look for patterns like after-hours access, access to unusual "
        "areas, and access by recently terminated employees.</p>"
        "<p><strong>Example 2:</strong> Forward badge access logs to your SIEM for correlation "
        "with logical access events. For example, if someone badges into the server room and "
        "an admin logon occurs on a server at the same time, that is a correlated event. If "
        "no badge-in is recorded but a local login occurs, that is a red flag.</p>"
    ),

    "pe-8-3": (
        "<p>Visitor access records often contain personal information (names, ID numbers, "
        "photos). This enhancement requires you to limit the PII collected to only what is "
        "necessary, based on a privacy risk assessment.</p>"
        "<p><strong>Example 1:</strong> Review your visitor sign-in form and remove any fields "
        "that are not necessary for security purposes. You likely need name, organization, "
        "host employee, and entry/exit times — but you may not need full address, phone number, "
        "or Social Security number.</p>"
        "<p><strong>Example 2:</strong> Configure your digital visitor management system to "
        "automatically purge visitor records after your required retention period. Set "
        "appropriate access controls so only security and compliance staff can view visitor "
        "PII. Include visitor data handling in your privacy documentation.</p>"
    ),

    "pe-9": (
        "<p>Your power equipment and cabling need protection from damage and destruction — "
        "whether from accidents, weather, or intentional tampering. Losing power to your "
        "systems means losing availability.</p>"
        "<p><strong>Example 1:</strong> Route power cabling through conduit or cable trays "
        "that protect against physical damage. Place power distribution units (PDUs) and UPS "
        "systems in locked areas accessible only to authorized facilities and IT staff. "
        "Label all circuits clearly so you know what each one powers.</p>"
        "<p><strong>Example 2:</strong> Protect your electrical panel and generator with "
        "locked enclosures or rooms. Restrict access to facilities and IT personnel. "
        "Include power equipment in your regular maintenance inspections — check for frayed "
        "cables, overloaded circuits, and proper grounding quarterly.</p>"
    ),

    "pe-9-1": (
        "<p>This enhancement requires redundant power cabling paths that are physically "
        "separated so that a single event — fire, water damage, construction accident — "
        "cannot take out all your power at once.</p>"
        "<p><strong>Example 1:</strong> Run two independent power feeds to your server room "
        "from different electrical panels or different utility feeds. Route them through "
        "different physical pathways (different walls, floors, or conduit runs) so a fire "
        "or flood in one area does not affect both feeds.</p>"
        "<p><strong>Example 2:</strong> For server racks, use dual-corded servers with each "
        "power supply connected to a different PDU fed from a different circuit. This way, "
        "if one PDU or circuit fails, the server stays running on the other. Document your "
        "power redundancy design in your facility plans.</p>"
    ),

    "pe-9-2": (
        "<p>Automatic voltage controls protect your equipment from power surges, sags, and "
        "fluctuations that can damage sensitive electronics or cause unexpected shutdowns.</p>"
        "<p><strong>Example 1:</strong> Install UPS (uninterruptible power supply) units with "
        "automatic voltage regulation (AVR) for all critical IT equipment. Size UPS units "
        "to provide at least 15 minutes of runtime for graceful shutdown. Use enterprise "
        "UPS brands like APC, Eaton, or Vertiv.</p>"
        "<p><strong>Example 2:</strong> Install surge protectors on all power circuits feeding "
        "IT equipment. For large installations, use a power distribution unit (PDU) with "
        "built-in voltage regulation and surge protection. Monitor power quality using the "
        "UPS management software and set alerts for voltage events.</p>"
    ),

    "pe-10": (
        "<p>In an emergency — fire, flood, electrical hazard — you need the ability to shut "
        "off power to your systems quickly and safely. Emergency shutoff switches must be "
        "accessible and clearly marked.</p>"
        "<p><strong>Example 1:</strong> Install clearly labeled Emergency Power Off (EPO) "
        "buttons at server room exits and near the main electrical panel. Cover them with "
        "protective guards to prevent accidental activation. Ensure all IT staff know where "
        "they are located and when to use them.</p>"
        "<p><strong>Example 2:</strong> Document the location of all emergency shutoff switches "
        "in your emergency procedures guide. Include them on your facility floor plans. Test "
        "EPO functionality annually during planned maintenance windows to confirm they actually "
        "work. Train new IT staff on EPO locations during their first week.</p>"
    ),

    "pe-10-1": (
        "<p>Emergency shutoff controls need protection against accidental or unauthorized "
        "activation. An accidental EPO press can cause more damage than the emergency it "
        "was designed to prevent.</p>"
        "<p><strong>Example 1:</strong> Install protective covers (flip covers or recessed "
        "mounting) on all EPO buttons. Require a deliberate two-step action to activate — "
        "lift cover, then press button. This prevents accidental activation from someone "
        "brushing against or leaning on the switch.</p>"
        "<p><strong>Example 2:</strong> Position EPO buttons away from high-traffic walkways "
        "and door frames where they might be accidentally hit. Clearly label them with 'EMERGENCY "
        "POWER OFF — DO NOT ACTIVATE UNLESS EMERGENCY' signage. Include accidental EPO "
        "prevention in your facility orientation for new employees and visitors.</p>"
    ),

    "pe-11": (
        "<p>An uninterruptible power supply (UPS) provides temporary power during outages, "
        "giving your systems time to shut down gracefully or switch to a backup generator. "
        "Without a UPS, a power flicker can corrupt data and crash systems.</p>"
        "<p><strong>Example 1:</strong> Install rack-mounted UPS units (APC Smart-UPS, Eaton "
        "5PX, or CyberPower) for all server racks and network equipment. Size each UPS to "
        "provide at least 15-30 minutes of runtime at current load. Configure UPS management "
        "software to trigger graceful OS shutdown if power is not restored within 10 minutes.</p>"
        "<p><strong>Example 2:</strong> For critical workstations (security consoles, "
        "reception systems), provide desktop UPS units. Set up automated email or Teams "
        "notifications when the UPS switches to battery power so IT staff are alerted "
        "immediately. Test UPS batteries annually and replace them on the manufacturer's "
        "recommended schedule.</p>"
    ),

    "pe-11-1": (
        "<p>This enhancement requires an alternate power supply (like a generator) that can "
        "maintain at least minimal operational capability during an extended power outage — "
        "longer than what your UPS batteries can cover.</p>"
        "<p><strong>Example 1:</strong> Install a diesel or natural gas generator sized to "
        "power your critical IT infrastructure (servers, network equipment, cooling) for at "
        "least 24-72 hours. Configure an automatic transfer switch (ATS) so the generator "
        "starts and takes over within seconds of a utility power failure.</p>"
        "<p><strong>Example 2:</strong> If a permanent generator is not feasible, contract "
        "with a generator rental company for emergency power. Have a pre-negotiated agreement "
        "so you can get a portable generator delivered within hours. Ensure your electrical "
        "panel has a manual transfer switch connector ready for a portable generator hookup.</p>"
    ),

    "pe-11-2": (
        "<p>This enhancement calls for a self-contained alternate power supply that does not "
        "rely on external power generation or fuel delivery. This is for environments that "
        "must remain operational regardless of external infrastructure availability.</p>"
        "<p><strong>Example 1:</strong> Install a combined solar panel and battery storage "
        "system sized to power critical systems independently. This removes dependence on "
        "fuel deliveries during extended outages. Design the system to power essential IT "
        "equipment for at least 48 hours of autonomy.</p>"
        "<p><strong>Example 2:</strong> For high-security installations, consider a natural "
        "gas generator with a direct pipeline connection (no fuel storage or delivery needed) "
        "combined with a large battery bank for instant switchover. Document the capacity "
        "and autonomy time in your continuity of operations plan.</p>"
    ),

    "pe-12": (
        "<p>Emergency lighting must activate automatically when power fails, illuminating "
        "emergency exits and evacuation routes so people can safely leave the facility.</p>"
        "<p><strong>Example 1:</strong> Install battery-backed emergency lighting fixtures "
        "above all exit doors and along evacuation routes. Test them monthly by pressing the "
        "test button on each fixture to verify the battery works. Replace batteries on the "
        "manufacturer's recommended schedule (typically every 3-5 years).</p>"
        "<p><strong>Example 2:</strong> Install illuminated EXIT signs at all exits, required "
        "by fire code. Maintain a testing log that records monthly push-to-test results and "
        "annual 90-minute duration tests for all emergency lighting. Fix any failures within "
        "48 hours. Keep the testing log in your compliance files.</p>"
    ),

    "pe-12-1": (
        "<p>This enhancement extends emergency lighting to all areas that support essential "
        "mission and business functions — not just exit routes. If your server room loses "
        "power, staff need to see what they are doing during emergency response.</p>"
        "<p><strong>Example 1:</strong> Install battery-backed emergency lighting in your "
        "server room, network closets, and security operations areas. These lights should "
        "activate automatically and provide enough illumination to read labels, identify "
        "equipment, and safely work during a power outage.</p>"
        "<p><strong>Example 2:</strong> Provide flashlights or headlamps in emergency kits "
        "located in the server room and key operations areas. Include these items in your "
        "emergency equipment inventory and test batteries quarterly. This supplements fixed "
        "emergency lighting and helps during extended outages.</p>"
    ),

    "pe-13": (
        "<p>Your facility needs fire detection and suppression systems that work even when "
        "the main power is out. An independent energy source (battery backup or generator) "
        "ensures your fire protection systems keep running during a power failure.</p>"
        "<p><strong>Example 1:</strong> Install a fire alarm system with battery backup that "
        "meets NFPA 72 standards. Include smoke detectors, heat detectors, and manual pull "
        "stations throughout the facility. Test the system semi-annually and have it "
        "professionally inspected annually.</p>"
        "<p><strong>Example 2:</strong> In the server room, install a clean-agent fire "
        "suppression system (FM-200, Novec 1230, or Inergen) that extinguishes fires without "
        "damaging electronics. Water sprinklers can destroy your IT equipment, so clean-agent "
        "systems are strongly preferred for server rooms and data closets.</p>"
    ),

    "pe-13-1": (
        "<p>Fire detection systems must activate automatically and notify both internal "
        "personnel and emergency services. You cannot rely on someone happening to notice "
        "smoke.</p>"
        "<p><strong>Example 1:</strong> Configure your fire alarm system to automatically "
        "notify the local fire department through a monitored alarm service (like ADT, "
        "SimpliSafe commercial, or a local alarm company). Also configure it to send "
        "alerts to your facilities team and security staff via text or email.</p>"
        "<p><strong>Example 2:</strong> Install networked smoke detectors that integrate with "
        "your building management system (BMS). When smoke is detected in the server room, "
        "the BMS can automatically shut down HVAC to prevent smoke spread, alert the building "
        "manager, and activate pre-action fire suppression if confirmed.</p>"
    ),

    "pe-13-2": (
        "<p>Fire suppression systems must activate automatically when fire is detected and "
        "notify the right people. This includes sprinklers for general areas and clean-agent "
        "systems for IT equipment areas.</p>"
        "<p><strong>Example 1:</strong> Install a pre-action sprinkler system in the server "
        "room (requires both smoke detection and sprinkler head activation to release water, "
        "reducing accidental discharge risk). For the rest of the facility, wet-pipe sprinklers "
        "per NFPA 13 standards are standard.</p>"
        "<p><strong>Example 2:</strong> Configure your clean-agent suppression system to send "
        "automated alerts to your fire alarm monitoring service and your IT team when it "
        "activates. Include a pre-discharge alarm (audible and visual) that gives personnel "
        "time to evacuate before agent release. Test annually per NFPA 2001.</p>"
    ),

    "pe-13-3": (
        "<p>This enhancement requires automatic fire suppression capability — the system "
        "activates without human intervention when fire conditions are detected.</p>"
        "<p><strong>Example 1:</strong> Ensure your server room fire suppression system "
        "(clean agent like FM-200 or Novec 1230) is configured for automatic discharge "
        "upon confirmed fire detection (typically cross-zone smoke detection). Do not "
        "set it to manual-only mode, as delays during an actual fire can be catastrophic.</p>"
        "<p><strong>Example 2:</strong> For general office areas, verify that your sprinkler "
        "system is fully operational and not impaired by closed valves or maintenance "
        "activities. Test the tamper switches on all sprinkler control valves — these should "
        "alert your alarm monitoring service if a valve is closed. Inspect quarterly per "
        "NFPA 25.</p>"
    ),

    "pe-13-4": (
        "<p>Your facility must undergo regular fire protection inspections by qualified "
        "inspectors, and any deficiencies they find must be fixed within a defined timeframe.</p>"
        "<p><strong>Example 1:</strong> Schedule annual fire protection inspections by your "
        "local fire marshal or a certified fire protection inspector. Address any deficiencies "
        "they identify within 30 days. Keep inspection reports and remediation records in "
        "your compliance files.</p>"
        "<p><strong>Example 2:</strong> In addition to official inspections, conduct monthly "
        "internal fire safety walkthroughs. Check that fire extinguishers are accessible and "
        "current (check the inspection tag), exit routes are clear, fire doors are not propped "
        "open, and sprinkler heads are not obstructed. Log findings on a checklist.</p>"
    ),

    "pe-14": (
        "<p>Environmental controls — temperature, humidity, and airflow — must be maintained "
        "within acceptable ranges for your equipment. Servers that overheat fail, and "
        "excessive humidity causes corrosion and short circuits.</p>"
        "<p><strong>Example 1:</strong> Install a dedicated HVAC system or precision cooling "
        "unit for your server room. Maintain temperature between 64-80°F (18-27°C) and "
        "relative humidity between 40-60% per ASHRAE recommendations. Install temperature "
        "and humidity sensors that display current readings and log historical data.</p>"
        "<p><strong>Example 2:</strong> Use environmental monitoring tools (APC NetBotz, "
        "Vertiv Liebert, or Paessler PRTG with environmental sensors) to continuously "
        "monitor temperature and humidity. Set alert thresholds at 5 degrees below the "
        "critical limit so you have time to respond. Send alerts via email, text, or Teams "
        "to IT and facilities staff.</p>"
    ),

    "pe-14-1": (
        "<p>This enhancement requires automatic environmental controls — your HVAC and cooling "
        "systems should adjust automatically to maintain proper conditions without requiring "
        "manual intervention.</p>"
        "<p><strong>Example 1:</strong> Configure your precision cooling unit to automatically "
        "adjust cooling output based on real-time temperature readings. Set it to increase "
        "cooling when the temperature rises above 72°F and alert facilities staff if it "
        "cannot maintain the setpoint.</p>"
        "<p><strong>Example 2:</strong> Use a building management system (BMS) to automatically "
        "control HVAC for your server room. Configure the BMS to switch to backup cooling "
        "units if the primary unit fails, send alerts for any environmental exceedances, "
        "and log all temperature and humidity data for trending and compliance reporting.</p>"
    ),

    "pe-14-2": (
        "<p>Environmental monitoring equipment should generate alarms or notifications when "
        "conditions drift outside acceptable ranges. Someone needs to know immediately when "
        "the server room is getting too hot.</p>"
        "<p><strong>Example 1:</strong> Set up temperature and humidity alerts in your "
        "environmental monitoring system. Configure two tiers: a warning alert (e.g., temp "
        "above 78°F) that goes to IT staff and a critical alert (e.g., temp above 85°F) "
        "that goes to IT management and facilities. Include instructions for response in "
        "each alert.</p>"
        "<p><strong>Example 2:</strong> Use standalone environmental sensors (like Sensaphone "
        "or AKCP) that can send alerts via phone call, text, and email independently of your "
        "network. This way, even if your network goes down (which might happen during a "
        "cooling failure), you still get notified of dangerous environmental conditions.</p>"
    ),

    "pe-15": (
        "<p>Water damage is a real threat to IT equipment — from burst pipes, roof leaks, or "
        "flooding. You need master shutoff valves that key personnel know about and can "
        "access quickly to stop water flow in an emergency.</p>"
        "<p><strong>Example 1:</strong> Identify and label all water shutoff valves in or "
        "near your server room and IT equipment areas. Ensure they are accessible (not "
        "blocked by equipment or debris) and functioning properly. Test them annually. "
        "Train IT and facilities staff on their locations.</p>"
        "<p><strong>Example 2:</strong> Document shutoff valve locations on your facility "
        "floor plans and include them in your emergency procedures. Avoid locating IT "
        "equipment below water pipes when possible. If water pipes must run above or near "
        "your server room, install drip pans and water sensors beneath them.</p>"
    ),

    "pe-15-1": (
        "<p>This enhancement requires automated water detection near your systems — sensors "
        "that detect water and alert the right people before equipment is damaged.</p>"
        "<p><strong>Example 1:</strong> Install water leak detection sensors (rope-style or "
        "spot sensors) under raised flooring in the server room, below HVAC units, and "
        "near any water pipes. Connect them to your environmental monitoring system (APC "
        "NetBotz, AKCP) for immediate alerting via email and text.</p>"
        "<p><strong>Example 2:</strong> Use standalone water detection alarms (like the "
        "Honeywell Lyric water sensor or Phyn smart water monitor) as a low-cost option "
        "for smaller installations. Place them under server racks, near CRAC units, and "
        "at any low point in the server room where water would accumulate first.</p>"
    ),

    "pe-16": (
        "<p>When IT equipment enters or leaves your facility, it must be authorized, "
        "controlled, and recorded. You need to know what hardware came in, what went out, "
        "and who authorized the movement.</p>"
        "<p><strong>Example 1:</strong> Create an equipment delivery and removal form that "
        "records the item description, serial number, sender/recipient, purpose, authorizing "
        "manager, and date. Require this form to be completed and approved before any equipment "
        "passes through your doors. Maintain these records in your asset management system.</p>"
        "<p><strong>Example 2:</strong> Use an asset management tool (Snipe-IT, ServiceNow, "
        "or even a spreadsheet) to track all hardware assets. When equipment arrives, receive "
        "it into inventory with a photo and serial number. When equipment leaves, record the "
        "authorization, destination, and reason. Reconcile your physical inventory against "
        "your records quarterly.</p>"
    ),

    "pe-17": (
        "<p>If employees work from alternate locations — home offices, satellite offices, or "
        "temporary work sites — those locations need appropriate security controls too. Your "
        "data does not stop being sensitive just because it left your building.</p>"
        "<p><strong>Example 1:</strong> Create a telework security agreement that employees "
        "sign before working remotely. Include requirements for: locking the workstation "
        "when unattended, using VPN for all connections, encrypting the hard drive (BitLocker), "
        "securing printed documents, and reporting any security incidents immediately.</p>"
        "<p><strong>Example 2:</strong> Provide remote workers with company-managed equipment "
        "(laptops, monitors) pre-configured with security controls. Require home office setups "
        "in a private space where screens are not visible to others. Use Microsoft Intune "
        "or similar MDM to ensure remote devices remain compliant with security policies.</p>"
    ),

    "pe-18": (
        "<p>Where you place your systems within a facility matters. Position equipment to "
        "minimize exposure to physical threats (water, fire, windows, high-traffic areas) "
        "and unauthorized access.</p>"
        "<p><strong>Example 1:</strong> Do not put servers in the basement (flood risk) or top "
        "floor (roof leak risk) if you can avoid it. Place server rooms in interior spaces "
        "away from exterior walls and windows. Position network equipment away from loading "
        "docks, kitchens, and restrooms where water and foot traffic are high.</p>"
        "<p><strong>Example 2:</strong> When designing or renovating your IT spaces, work with "
        "facilities to ensure server rooms are not adjacent to wet areas (restrooms, kitchens, "
        "mechanical rooms with chillers). Position monitors to prevent shoulder surfing from "
        "windows or public areas. Document location decisions in your facility security plan.</p>"
    ),

    "pe-18-1": (
        "<p>This enhancement considers the security of the facility site itself — its "
        "geographic location and surrounding environment — when planning where to locate "
        "system components.</p>"
        "<p><strong>Example 1:</strong> When selecting a new facility or data center location, "
        "evaluate the risk from natural hazards (flood zone, earthquake zone, tornado alley), "
        "proximity to high-risk targets (military bases, chemical plants), and crime rates "
        "in the area. Document this risk assessment.</p>"
        "<p><strong>Example 2:</strong> Review FEMA flood maps and local hazard assessments "
        "before leasing or purchasing a facility. Avoid locations in 100-year flood plains. "
        "Consider proximity to emergency services (fire station, hospital). Include site "
        "risk factors in your risk management documentation.</p>"
    ),

    "pe-19": (
        "<p>Systems can leak information through electromagnetic signals — screen emissions, "
        "cable radiation, and other electronic emanations that can be intercepted from a "
        "distance. This control requires protection against such leakage.</p>"
        "<p><strong>Example 1:</strong> For systems processing sensitive information, use "
        "shielded cables (STP for network, shielded HDMI/DisplayPort) to reduce electromagnetic "
        "emissions. Position monitors away from windows where emissions could be captured "
        "from outside. Consider TEMPEST-rated equipment for classified environments.</p>"
        "<p><strong>Example 2:</strong> For most commercial environments, basic practices "
        "provide adequate protection: keep servers in interior rooms away from exterior walls, "
        "use fiber optic cabling (which does not emit electromagnetic signals) for connections "
        "that cross public spaces, and maintain physical distance between sensitive systems "
        "and areas accessible to the public.</p>"
    ),

    "pe-19-1": (
        "<p>For systems processing classified information, this enhancement requires compliance "
        "with national Emissions Security (EMSEC/TEMPEST) policies and procedures based on "
        "the classification level of the information.</p>"
        "<p><strong>Example 1:</strong> If your facility processes classified information, "
        "work with your cognizant security agency to determine TEMPEST countermeasure "
        "requirements. This may include purchasing TEMPEST-certified equipment from the "
        "NSA EPL, implementing zone-of-control measures, or conducting TEMPEST assessments.</p>"
        "<p><strong>Example 2:</strong> Maintain your TEMPEST countermeasures documentation "
        "as required by your security plan. This includes equipment certifications, zone "
        "measurements, and any waivers or risk acceptances. Have your TEMPEST program "
        "reviewed during your facility security inspections.</p>"
    ),

    "pe-20": (
        "<p>Asset monitoring and tracking ensures you know where your hardware is at all times — "
        "servers, laptops, mobile devices, and other equipment. If something goes missing, "
        "you need to know quickly.</p>"
        "<p><strong>Example 1:</strong> Implement an asset management system (Snipe-IT, "
        "ServiceNow, or a spreadsheet for smaller organizations) that tracks every piece of "
        "IT equipment: serial number, location, assigned user, and status. Conduct physical "
        "inventory checks quarterly and reconcile against your records.</p>"
        "<p><strong>Example 2:</strong> For mobile assets (laptops, tablets), use Microsoft "
        "Intune or another MDM solution that reports device location and last check-in time. "
        "For high-value physical assets, consider RFID tags or GPS trackers. Flag any device "
        "that has not checked in for 30+ days for investigation.</p>"
    ),

    "pe-21": (
        "<p>Electromagnetic pulse (EMP) events — from nuclear detonations, solar storms, or "
        "intentional EMP weapons — can destroy electronic equipment. This control requires "
        "protective measures for systems that must survive such events.</p>"
        "<p><strong>Example 1:</strong> For critical infrastructure or continuity-of-government "
        "systems, install EMP-hardened enclosures (Faraday cages) around essential equipment. "
        "Use EMP-rated surge protectors on all power and data lines entering the protected "
        "space. Consult MIL-STD-188-125 for DoD requirements.</p>"
        "<p><strong>Example 2:</strong> For most commercial organizations, basic EMP protection "
        "includes quality surge protectors on all power circuits, fiber optic cabling for "
        "external data connections (fiber is inherently EMP-resistant), and maintaining offline "
        "backup copies of critical data that would survive an EMP event.</p>"
    ),

    "pe-22": (
        "<p>Hardware components should be visually marked to indicate the sensitivity level "
        "of information they are authorized to process. This prevents someone from accidentally "
        "connecting a classified drive to an unclassified system.</p>"
        "<p><strong>Example 1:</strong> Apply color-coded labels to all hardware: green stickers "
        "for unclassified systems, yellow for CUI, red for classified. Apply labels to "
        "monitors, keyboards, system units, cables, and peripherals. Make the markings "
        "large enough to be easily visible from a normal working distance.</p>"
        "<p><strong>Example 2:</strong> Use engraved asset tags or tamper-evident labels that "
        "include the system name, classification level, and asset number. For cables, use "
        "color-coded cable ties or labels at both ends. Include marking requirements in your "
        "configuration management procedures so new equipment is marked before deployment.</p>"
    ),

    "pe-23": (
        "<p>When selecting a location for your facility, consider physical and environmental "
        "hazards — floods, earthquakes, tornadoes, industrial accidents, and other threats — "
        "that could disrupt operations or damage your systems.</p>"
        "<p><strong>Example 1:</strong> Before establishing a new facility, conduct a site "
        "risk assessment that evaluates: FEMA flood zone designation, seismic activity, "
        "proximity to chemical or industrial facilities, crime rates, proximity to airports "
        "or rail lines, and historical weather patterns. Document findings and mitigation "
        "measures.</p>"
        "<p><strong>Example 2:</strong> For existing facilities, review your location risk "
        "periodically — new construction, zoning changes, or climate pattern shifts can "
        "change your risk profile. Work with your insurance provider to identify site-specific "
        "risks and ensure your business continuity plan accounts for location-based threats. "
        "Update your risk assessment at least every three years.</p>"
    ),

    # ── Planning (PL) ──────────────────────────────────────────────────

    "pl-1": (
        "<p>This control requires a documented planning policy and procedures. Your planning "
        "policy governs how you develop, maintain, and update security and privacy plans for "
        "your systems — it is the plan for making plans.</p>"
        "<p><strong>Example 1:</strong> Write a Security Planning Policy that defines how your "
        "organization creates and maintains system security plans (SSPs), who is responsible "
        "for each plan, how often plans are reviewed, and what triggers an update. Store it "
        "in your policy library and review it annually.</p>"
        "<p><strong>Example 2:</strong> Include planning procedures in your security program "
        "documentation. Define a template for SSPs that all system owners must use, a review "
        "cycle (at least annually), and an approval workflow (system owner writes, ISSO reviews, "
        "AO approves). Track plan status in a spreadsheet or GRC tool.</p>"
    ),

    "pl-2": (
        "<p>Every system needs a security plan (SSP) and, if applicable, a privacy plan. The "
        "SSP is your master document that describes how you protect the system — what controls "
        "are in place, how they are implemented, and who is responsible for them.</p>"
        "<p><strong>Example 1:</strong> Develop your SSP using the NIST SP 800-18 template or "
        "your organization's standard format. Include: system description, system boundary, "
        "data types processed, user roles, implemented security controls with implementation "
        "details, and a diagram showing how the system connects to your network.</p>"
        "<p><strong>Example 2:</strong> Use a GRC tool like eMASS, CSAM, or Archer to manage "
        "your SSP. These tools provide structured templates that map controls to your system "
        "and track implementation status. If a GRC tool is not available, a well-organized "
        "Word document with a control-by-control implementation description works fine. "
        "Update the SSP whenever there is a significant change to the system.</p>"
    ),

    "pl-2-1": (
        "<p>A Concept of Operations (CONOPS) describes how your system is intended to be "
        "operated from a security perspective. It bridges the gap between technical "
        "implementation and operational use.</p>"
        "<p><strong>Example 1:</strong> Write a CONOPS section in your SSP that describes "
        "how users interact with the system, what security roles are defined (admin, user, "
        "auditor), how data flows through the system, and what the expected operating "
        "environment looks like (on-premise, cloud, hybrid).</p>"
        "<p><strong>Example 2:</strong> Include operational scenarios in your CONOPS: normal "
        "operations (day-to-day use), degraded mode (key components unavailable), maintenance "
        "mode (system updates being applied), and emergency mode (active incident response). "
        "Describe the security posture for each scenario and who has what authorities.</p>"
    ),

    "pl-2-2": (
        "<p>A functional architecture describes how the security and privacy functions are "
        "distributed across your system's components. It shows how different parts of the "
        "system work together to provide security.</p>"
        "<p><strong>Example 1:</strong> Create a functional architecture diagram that shows "
        "where key security controls are implemented: firewall at the perimeter, IDS on the "
        "internal network, MFA at the authentication layer, encryption at the storage layer. "
        "Include this diagram in your SSP.</p>"
        "<p><strong>Example 2:</strong> Map your security functions to specific technologies "
        "and products: authentication (Azure AD with MFA), access control (NTFS permissions "
        "+ Conditional Access), auditing (Microsoft Sentinel), endpoint protection (Defender "
        "for Endpoint). Present this as a table or layered diagram in your security "
        "architecture documentation.</p>"
    ),

    "pl-2-3": (
        "<p>Your security planning should be coordinated with other groups in your organization "
        "that have related responsibilities — IT operations, privacy, legal, HR, and physical "
        "security teams all need to be aligned.</p>"
        "<p><strong>Example 1:</strong> When developing or updating your SSP, circulate drafts "
        "to stakeholders: the privacy officer (for PII handling), HR (for personnel security), "
        "facilities (for physical security), and legal (for compliance requirements). Document "
        "their feedback and how it was incorporated.</p>"
        "<p><strong>Example 2:</strong> Establish a security planning review board that meets "
        "quarterly and includes representatives from IT, security, privacy, legal, and "
        "business operations. Use this forum to coordinate security plan updates, discuss "
        "new requirements, and resolve conflicts between operational needs and security "
        "controls.</p>"
    ),

    "pl-3": (
        "<p>Your system security plan is a living document — it needs to be updated whenever "
        "there are significant changes to the system, its environment, or the threats it faces. "
        "An outdated SSP is almost as bad as no SSP.</p>"
        "<p><strong>Example 1:</strong> Set a calendar reminder to review your SSP at least "
        "annually. Also update it whenever you make significant changes: adding new servers, "
        "migrating to cloud, changing network architecture, or deploying new security tools. "
        "Track versions with a revision history table at the front of the document.</p>"
        "<p><strong>Example 2:</strong> Tie SSP updates to your change management process. "
        "When a significant change is approved, include 'Update SSP' as a required step in "
        "the change ticket. This ensures the SSP stays current without relying solely on "
        "periodic reviews. Use your GRC tool or a simple tracker to log every SSP update.</p>"
    ),

    "pl-4": (
        "<p>Rules of behavior define what users can and cannot do on your systems — acceptable "
        "use, security responsibilities, and consequences for violations. Every user must "
        "read and acknowledge these rules before getting access.</p>"
        "<p><strong>Example 1:</strong> Write an Acceptable Use Policy (AUP) that covers: "
        "authorized use of company systems, personal use limits, social media restrictions, "
        "data handling requirements, password responsibilities, and consequences for "
        "violations. Have all employees sign it during onboarding and re-sign annually.</p>"
        "<p><strong>Example 2:</strong> Implement a logon banner using GPO (<em>Computer "
        "Configuration → Policies → Windows Settings → Security Settings → Local Policies → "
        "Security Options → Interactive logon: Message text/title for users attempting to "
        "log on</em>) that displays a summary of rules of behavior and requires "
        "acknowledgment before access is granted.</p>"
    ),

    "pl-4-1": (
        "<p>Your rules of behavior should specifically address social media use and external "
        "websites/applications — what employees can share publicly, how they represent the "
        "organization online, and what information they must not post.</p>"
        "<p><strong>Example 1:</strong> Add a social media section to your AUP that prohibits: "
        "sharing proprietary or sensitive information on social media, posting photos of "
        "work areas showing screens or documents, discussing specific client projects without "
        "approval, and using personal social media accounts for company business.</p>"
        "<p><strong>Example 2:</strong> Configure Microsoft Defender for Cloud Apps or a web "
        "filtering solution to monitor and control access to social media and personal cloud "
        "storage from company devices. Block uploads to personal cloud storage (Google Drive, "
        "Dropbox) and log social media access for review if needed.</p>"
    ),

    "pl-5": (
        "<p>A Privacy Impact Assessment (PIA) evaluates how your system collects, stores, "
        "uses, and shares personally identifiable information (PII). It identifies privacy "
        "risks and documents how you mitigate them.</p>"
        "<p><strong>Example 1:</strong> Conduct a PIA for each system that processes PII. "
        "Document: what PII is collected, why it is needed, how it is stored and protected, "
        "who has access, how long it is retained, and how it is disposed of. Use your "
        "agency's PIA template if one exists, or create one based on OMB guidance.</p>"
        "<p><strong>Example 2:</strong> Publish completed PIAs on your organization's website "
        "or make them available upon request, as required by policy. Review PIAs when system "
        "changes affect PII processing — new data fields, new sharing agreements, or changes "
        "in retention periods should trigger a PIA update.</p>"
    ),

    "pl-6": (
        "<p>Security-related activities — like penetration testing, vulnerability scanning, "
        "or security assessments — need to be planned and coordinated to avoid disrupting "
        "operations or triggering false alarms.</p>"
        "<p><strong>Example 1:</strong> Create a security activity calendar that schedules all "
        "planned security activities: annual penetration tests, quarterly vulnerability scans, "
        "monthly phishing simulations, and weekly log reviews. Share this calendar with IT "
        "operations so they know what to expect and when.</p>"
        "<p><strong>Example 2:</strong> Before conducting any security testing, submit a "
        "notification to IT operations, help desk, and management. Include the scope, timing, "
        "and expected impact. This prevents unnecessary incident responses when your vulnerability "
        "scanner triggers IDS alerts or your phishing test generates a flood of reports.</p>"
    ),

    "pl-7": (
        "<p>A Concept of Operations (CONOPS) document describes how you intend to operate the "
        "system from a security perspective. It tells the story of how security works in "
        "practice, not just on paper.</p>"
        "<p><strong>Example 1:</strong> Write a CONOPS that describes your operating environment, "
        "user communities, data flows, interconnections with other systems, security roles and "
        "responsibilities, and how you operate the system day-to-day from a security standpoint. "
        "Review and update it when operational changes occur.</p>"
        "<p><strong>Example 2:</strong> Include scenarios in your CONOPS: how the system operates "
        "normally, how it handles peak load, what happens during maintenance windows, and how "
        "it operates during degraded mode or emergency. For each scenario, describe which "
        "security controls remain active and which may be temporarily modified.</p>"
    ),

    "pl-8": (
        "<p>Your security architecture describes the overall design approach for protecting "
        "your systems and information. It should align with your enterprise architecture and "
        "guide security decisions across the organization.</p>"
        "<p><strong>Example 1:</strong> Develop a security architecture document that covers: "
        "network segmentation strategy, authentication and access control approach, data "
        "protection methods (encryption at rest and in transit), monitoring and logging "
        "strategy, and incident response capabilities. Map these to specific technologies "
        "and products in use.</p>"
        "<p><strong>Example 2:</strong> Create a security architecture diagram showing your "
        "defense-in-depth layers: perimeter (firewall, WAF), network (IDS/IPS, segmentation), "
        "endpoint (EDR, AV), application (input validation, WAF rules), data (encryption, "
        "DLP), and identity (MFA, PAM). Update this diagram when you add or change security "
        "technologies.</p>"
    ),

    "pl-8-1": (
        "<p>Defense in depth means layering multiple security controls so that if one fails, "
        "others still protect your systems. Your security architecture should be deliberately "
        "designed with overlapping protections.</p>"
        "<p><strong>Example 1:</strong> Map your controls to defense layers: perimeter firewall "
        "blocks known bad traffic, IDS monitors for suspicious patterns that get through, "
        "endpoint protection catches malware on the host, application controls limit what "
        "programs can run, and data encryption protects information even if all other layers "
        "fail. Document this layered approach in your security architecture.</p>"
        "<p><strong>Example 2:</strong> Ensure no single point of failure exists in your "
        "security architecture. For example, do not rely solely on your firewall for access "
        "control — also implement network segmentation, host-based firewalls (Windows "
        "Firewall configured via GPO), and Conditional Access policies. If the firewall is "
        "bypassed, these layers still provide protection.</p>"
    ),

    "pl-8-2": (
        "<p>This enhancement requires that security controls are obtained from different "
        "suppliers (vendor diversity) so that a vulnerability in one vendor's product does not "
        "compromise all your defenses simultaneously.</p>"
        "<p><strong>Example 1:</strong> Use different vendors for different security layers: "
        "one vendor for your perimeter firewall (e.g., Palo Alto), a different vendor for "
        "endpoint protection (e.g., CrowdStrike), and another for your SIEM (e.g., Splunk). "
        "This way, a zero-day in one vendor's product does not leave all layers exposed.</p>"
        "<p><strong>Example 2:</strong> Document your vendor diversity strategy in your "
        "security architecture. Include a matrix that maps each security function to its "
        "vendor and product. Review this matrix when renewing contracts or evaluating new "
        "products to ensure you are not consolidating too many critical functions with a "
        "single vendor.</p>"
    ),

    "pl-9": (
        "<p>Central management means managing selected security controls from a single point "
        "rather than configuring each system individually. This ensures consistency and "
        "reduces the chance of misconfiguration.</p>"
        "<p><strong>Example 1:</strong> Use Group Policy (Active Directory GPOs) to centrally "
        "manage security settings across all domain-joined machines: password policies, audit "
        "policies, firewall rules, and software restrictions. Changes are made once in the "
        "GPO and pushed to all affected systems automatically.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Intune or MECM to centrally manage "
        "endpoint security configurations, patch deployment, and compliance policies across "
        "all managed devices. Use Azure AD Conditional Access to centrally enforce access "
        "policies. Central management ensures every system is configured the same way and "
        "makes compliance auditing much easier.</p>"
    ),

    "pl-10": (
        "<p>Baseline selection means choosing the appropriate set of security controls for "
        "your system based on its impact level (Low, Moderate, or High). NIST SP 800-53B "
        "defines the control baselines.</p>"
        "<p><strong>Example 1:</strong> Categorize your system using FIPS 199 criteria "
        "(confidentiality, integrity, and availability impact levels). Then select the "
        "corresponding control baseline from NIST SP 800-53B. For example, a Moderate-impact "
        "system uses the Moderate baseline. Document your categorization and baseline "
        "selection in your SSP.</p>"
        "<p><strong>Example 2:</strong> Use CNSSI 1253 for national security systems or "
        "reference CMMC level requirements if you are a defense contractor. Map the selected "
        "baseline controls to your SSP and begin documenting how each control is implemented "
        "in your environment. Use a GRC tool or a spreadsheet to track implementation status "
        "across all baseline controls.</p>"
    ),

    "pl-11": (
        "<p>After selecting a control baseline, you tailor it — adjusting controls to fit your "
        "specific system and operational environment. Not every control applies equally to "
        "every system, and tailoring lets you add, remove, or modify controls appropriately.</p>"
        "<p><strong>Example 1:</strong> Review each control in your selected baseline and "
        "determine if it applies to your system as-is, needs modification, or does not apply "
        "(with justification). For example, if your system has no wireless capability, you "
        "can mark wireless-related controls as not applicable with documented rationale.</p>"
        "<p><strong>Example 2:</strong> Document your tailoring decisions in your SSP. For "
        "each tailored control, explain what was changed and why. Common tailoring actions "
        "include applying scoping guidance (not applicable), compensating controls (using "
        "an alternative control to achieve the same objective), and organization-defined "
        "parameters (setting specific values like password length or audit retention period).</p>"
    ),
}
