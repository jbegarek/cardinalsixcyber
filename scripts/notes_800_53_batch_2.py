NOTES = {
    # =========================================================================
    # CA — Security Assessment and Authorization (32 controls)
    # =========================================================================

    "ca-1": (
        "<p>This control asks you to write down your rules for how your organization handles security assessments, "
        "authorizations, and ongoing monitoring — and share those rules with everyone who needs them.</p>"
        "<p><strong>Example 1:</strong> Create a <em>Security Assessment Policy</em> document in SharePoint that "
        "defines who is responsible for conducting annual security reviews and how results are reported to leadership.</p>"
        "<p><strong>Example 2:</strong> In your Microsoft 365 Compliance Center, set up a recurring calendar reminder "
        "to review and update your assessment procedures at least once per year or after any major security incident.</p>"
    ),

    "ca-2": (
        "<p>This control requires you to formally assess whether your security controls are working as intended. "
        "Think of it as a health check for your cybersecurity program — you need a plan, qualified people, and documented results.</p>"
        "<p><strong>Example 1:</strong> Hire a qualified assessor to run a NIST-based assessment using tools like "
        "<em>Nessus</em> or <em>Tenable.sc</em> to scan your systems and verify that controls like patching and access "
        "restrictions are actually in place.</p>"
        "<p><strong>Example 2:</strong> Use <em>eMASS</em> (Enterprise Mission Assurance Support Service) to document "
        "your assessment plan, track findings, and record assessment results for your authorizing official to review.</p>"
    ),

    "ca-2-1": (
        "<p>This enhancement requires that your security assessors be independent — meaning they should not be the same "
        "people who built or manage the system being assessed. Independence reduces bias.</p>"
        "<p><strong>Example 1:</strong> Contract with a third-party assessment organization (3PAO) to conduct your "
        "annual security control assessment rather than relying on your own IT staff.</p>"
        "<p><strong>Example 2:</strong> If using internal staff, ensure the assessor reports to a different chain of "
        "command than the system owner — for instance, your compliance team assesses systems managed by IT operations.</p>"
    ),

    "ca-2-2": (
        "<p>This enhancement calls for specialized types of assessments beyond standard control reviews — such as "
        "vulnerability scanning, penetration testing, or insider threat analysis.</p>"
        "<p><strong>Example 1:</strong> Schedule quarterly <em>Nessus</em> vulnerability scans of your network and "
        "include the scan results as part of your overall control assessment package.</p>"
        "<p><strong>Example 2:</strong> Commission an annual <em>red team exercise</em> where ethical hackers attempt "
        "to breach your defenses, and incorporate findings into your assessment report.</p>"
    ),

    "ca-2-3": (
        "<p>This enhancement allows your organization to reuse assessment results from external organizations, such as "
        "cloud service providers or partner agencies, rather than re-testing everything yourself.</p>"
        "<p><strong>Example 1:</strong> If you use <em>Microsoft Azure Government</em>, leverage Microsoft's FedRAMP "
        "authorization package instead of independently assessing Azure's physical security controls.</p>"
        "<p><strong>Example 2:</strong> When a subcontractor already has a valid CMMC Level 2 certification, accept "
        "their assessment results for overlapping controls rather than duplicating the assessment effort.</p>"
    ),

    "ca-3": (
        "<p>This control requires you to formally approve and document every connection between your system and other "
        "systems. You need written agreements that spell out what data is shared, how it is protected, and who is responsible.</p>"
        "<p><strong>Example 1:</strong> Create an <em>Interconnection Security Agreement (ISA)</em> for every connection "
        "between your network and a partner organization's network, specifying firewall rules, encryption requirements, "
        "and data types exchanged.</p>"
        "<p><strong>Example 2:</strong> Document all API connections between your on-premises systems and cloud services "
        "like <em>Salesforce</em> or <em>ServiceNow</em>, including authentication methods (OAuth, API keys) and "
        "data flow diagrams.</p>"
    ),

    "ca-3-1": (
        "<p>This enhancement was incorporated into the base CA-3 control. It previously addressed connections involving "
        "unclassified national security systems specifically.</p>"
        "<p><strong>Example 1:</strong> If your unclassified system connects to a DoD network like <em>NIPRNet</em>, "
        "ensure you have a signed connection approval from the authorizing official on both sides.</p>"
        "<p><strong>Example 2:</strong> Use a <em>cross-domain solution</em> or approved boundary protection device "
        "when connecting unclassified national security systems to other networks, and document the configuration.</p>"
    ),

    "ca-3-2": (
        "<p>This enhancement was incorporated into the base CA-3 control. It previously addressed connections involving "
        "classified national security systems.</p>"
        "<p><strong>Example 1:</strong> Connections to <em>SIPRNet</em> or other classified networks require formal "
        "approval through your agency's classified connection approval process with full documentation.</p>"
        "<p><strong>Example 2:</strong> Ensure any cross-domain solution between classified and unclassified networks "
        "is on the <em>Unified Cross Domain Services Management Office (UCDSMO)</em> approved products list.</p>"
    ),

    "ca-3-3": (
        "<p>This enhancement was incorporated into the base CA-3 control. It previously addressed connections between "
        "unclassified systems that are not national security systems.</p>"
        "<p><strong>Example 1:</strong> Document connections between your corporate IT network and a vendor's system "
        "using a standard <em>Memorandum of Understanding (MOU)</em> that defines security responsibilities.</p>"
        "<p><strong>Example 2:</strong> Maintain a network diagram showing all external connections from your business "
        "systems, reviewed quarterly by your IT security team.</p>"
    ),

    "ca-3-4": (
        "<p>This enhancement was incorporated into the base CA-3 control. It previously addressed connections to public "
        "networks like the internet.</p>"
        "<p><strong>Example 1:</strong> Configure your <em>Palo Alto</em> or <em>Fortinet</em> firewall with explicit "
        "rules governing what traffic is allowed between your internal network and the public internet.</p>"
        "<p><strong>Example 2:</strong> Deploy a <em>web application firewall (WAF)</em> like AWS WAF or Cloudflare "
        "in front of any public-facing web servers to filter malicious traffic.</p>"
    ),

    "ca-3-5": (
        "<p>This enhancement requires you to restrict connections to external systems by using an allow-list or "
        "deny-list approach — only approved connections are permitted.</p>"
        "<p><strong>Example 1:</strong> Configure your perimeter firewall to use a <em>deny-by-default</em> policy "
        "where only explicitly approved external IP addresses and ports are allowed through.</p>"
        "<p><strong>Example 2:</strong> Maintain an approved vendor connections list in a spreadsheet or GRC tool like "
        "<em>Archer</em>, and require formal approval before any new external connection is established.</p>"
    ),

    "ca-3-6": (
        "<p>This enhancement requires formal authorization before any data can be transferred between connected systems. "
        "It is not enough to just approve the connection — you also need to approve what flows through it.</p>"
        "<p><strong>Example 1:</strong> Implement <em>data loss prevention (DLP)</em> policies in Microsoft 365 that "
        "block sensitive data types (like CUI or PII) from being transferred to unapproved external systems.</p>"
        "<p><strong>Example 2:</strong> Require a signed data transfer agreement before allowing automated file "
        "transfers via SFTP between your system and a subcontractor's system.</p>"
    ),

    "ca-3-7": (
        "<p>This enhancement addresses transitive information exchanges — when System A connects to System B, which "
        "connects to System C, your data may end up on System C without your direct approval.</p>"
        "<p><strong>Example 1:</strong> Include clauses in your <em>Interconnection Security Agreements</em> that "
        "prohibit the receiving system from forwarding your data to third-party systems without written consent.</p>"
        "<p><strong>Example 2:</strong> In your cloud environment, review service provider subprocessor lists "
        "(e.g., <em>Microsoft's subprocessor page</em>) to understand where your data might transit beyond your "
        "primary provider.</p>"
    ),

    "ca-4": (
        "<p>This control has been withdrawn and incorporated into CA-2 (Control Assessments). Security certification "
        "activities are now handled as part of the broader assessment process.</p>"
        "<p><strong>Example 1:</strong> Instead of a separate certification step, include certification-level rigor "
        "in your CA-2 assessment plan by using NIST SP 800-53A assessment procedures.</p>"
        "<p><strong>Example 2:</strong> Use your organization's <em>eMASS</em> or GRC platform to track the assessment "
        "and authorization workflow in one unified process rather than treating certification separately.</p>"
    ),

    "ca-5": (
        "<p>A Plan of Action and Milestones (POA&M) is your organization's to-do list for fixing security weaknesses. "
        "Every finding from assessments, audits, or scans that is not immediately fixed must be tracked here with "
        "deadlines and responsible parties.</p>"
        "<p><strong>Example 1:</strong> After a <em>Nessus</em> scan reveals 15 critical vulnerabilities, create a "
        "POA&M entry for each one in your GRC tool (like <em>eMASS</em> or <em>Xacta</em>) with a remediation "
        "deadline of 30 days and an assigned owner.</p>"
        "<p><strong>Example 2:</strong> Track all audit findings from your annual CMMC assessment in a POA&M "
        "spreadsheet that includes columns for weakness description, severity, milestone dates, and status updates "
        "reviewed monthly by leadership.</p>"
    ),

    "ca-5-1": (
        "<p>This enhancement requires automated tools to keep your POA&M accurate and current rather than relying on "
        "manual spreadsheet updates that quickly go stale.</p>"
        "<p><strong>Example 1:</strong> Integrate your <em>Tenable.io</em> vulnerability scanner with your GRC "
        "platform so that when a vulnerability is remediated, the corresponding POA&M entry automatically updates.</p>"
        "<p><strong>Example 2:</strong> Use <em>Jira</em> or <em>ServiceNow</em> to track POA&M items with automated "
        "notifications that alert owners when milestones are approaching or overdue.</p>"
    ),

    "ca-6": (
        "<p>Authorization is the formal decision by a senior official (the Authorizing Official, or AO) to allow a "
        "system to operate. The AO accepts the residual risk based on the assessment results and POA&M.</p>"
        "<p><strong>Example 1:</strong> Your company's CISO or designated Authorizing Official signs an <em>Authorization "
        "to Operate (ATO)</em> letter after reviewing the security assessment report and POA&M in <em>eMASS</em>.</p>"
        "<p><strong>Example 2:</strong> For a new cloud system, the AO reviews the FedRAMP package, your agency-specific "
        "controls, and any residual risks before granting a three-year ATO with conditions.</p>"
    ),

    "ca-6-1": (
        "<p>This enhancement enables joint authorization within the same organization — multiple officials can share "
        "the authorization responsibility for a single system.</p>"
        "<p><strong>Example 1:</strong> A shared IT system used by both your HR and Finance departments gets a joint "
        "ATO signed by both department heads, each accepting the risk for their portion of the data.</p>"
        "<p><strong>Example 2:</strong> Document the joint authorization arrangement in your system security plan, "
        "clearly defining which authorizing official is responsible for which aspects of the system's risk.</p>"
    ),

    "ca-6-2": (
        "<p>This enhancement extends joint authorization across different organizations — useful when multiple agencies "
        "or companies share a common system or platform.</p>"
        "<p><strong>Example 1:</strong> When your company and a partner company share a <em>Microsoft GCC High</em> "
        "tenant, both organizations' authorizing officials jointly approve the shared environment's authorization.</p>"
        "<p><strong>Example 2:</strong> Use the FedRAMP Joint Authorization Board (JAB) process as a model where "
        "multiple agencies accept a single cloud provider's authorization rather than each conducting separate reviews.</p>"
    ),

    "ca-7": (
        "<p>Continuous monitoring means you do not just check security once a year and forget about it. You need an "
        "ongoing program that regularly watches your security posture and catches problems early.</p>"
        "<p><strong>Example 1:</strong> Deploy a <em>SIEM</em> like <em>Splunk</em> or <em>Microsoft Sentinel</em> "
        "to continuously collect and analyze security logs from firewalls, servers, and endpoints, alerting on anomalies.</p>"
        "<p><strong>Example 2:</strong> Schedule monthly automated <em>Nessus</em> vulnerability scans and quarterly "
        "manual control reviews, feeding results into your POA&M and reporting dashboard for leadership review.</p>"
    ),

    "ca-7-1": (
        "<p>This enhancement requires that independent assessors participate in your continuous monitoring program — "
        "not just your internal IT team doing self-assessments.</p>"
        "<p><strong>Example 1:</strong> Contract with an independent assessor to review a sample of your security "
        "controls each quarter, rotating through the full control set over the year.</p>"
        "<p><strong>Example 2:</strong> Have your internal audit team (separate from IT) independently validate the "
        "accuracy of your continuous monitoring reports before they go to the authorizing official.</p>"
    ),

    "ca-7-2": (
        "<p>This enhancement was incorporated into CA-2. It previously specified different types of assessments "
        "(testing, examining, interviewing) that should be used during continuous monitoring.</p>"
        "<p><strong>Example 1:</strong> Include a mix of automated scanning (testing), document review (examining), "
        "and staff interviews in your continuous monitoring plan to get a complete picture.</p>"
        "<p><strong>Example 2:</strong> Use <em>SCAP-compliant tools</em> for automated testing of technical controls "
        "and supplement with manual interviews of system administrators for operational controls.</p>"
    ),

    "ca-7-3": (
        "<p>This enhancement requires you to analyze security trends over time — not just look at individual findings "
        "in isolation. Are things getting better or worse?</p>"
        "<p><strong>Example 1:</strong> Create a monthly <em>Power BI</em> or <em>Splunk</em> dashboard showing "
        "vulnerability count trends, mean time to remediate, and open POA&M items over the past 12 months.</p>"
        "<p><strong>Example 2:</strong> Track your <em>Nessus</em> scan results month-over-month to identify whether "
        "critical vulnerability counts are trending down, and brief leadership on the trend quarterly.</p>"
    ),

    "ca-7-4": (
        "<p>This enhancement integrates risk monitoring into your continuous monitoring program — you are not just "
        "tracking vulnerabilities but actively monitoring changes in risk to the organization.</p>"
        "<p><strong>Example 1:</strong> Subscribe to <em>CISA alerts</em> and threat intelligence feeds and correlate "
        "them with your asset inventory to identify when new threats elevate risk to your specific systems.</p>"
        "<p><strong>Example 2:</strong> Use your GRC tool to flag when POA&M items exceed their remediation deadline, "
        "automatically escalating the associated risk rating and notifying the authorizing official.</p>"
    ),

    "ca-7-5": (
        "<p>This enhancement requires you to check whether the security information you are collecting from various "
        "sources is consistent and reliable.</p>"
        "<p><strong>Example 1:</strong> Compare the asset counts in your <em>SCCM/Intune</em> inventory against "
        "your network scan results to ensure you are monitoring all devices and not missing rogue assets.</p>"
        "<p><strong>Example 2:</strong> Cross-reference <em>Active Directory</em> user counts with your HR system "
        "to verify that your identity data is consistent and no orphaned accounts exist.</p>"
    ),

    "ca-7-6": (
        "<p>This enhancement requires automated tools to support your continuous monitoring activities, reducing "
        "manual effort and improving consistency.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>Tenable.sc</em> with scheduled automated scans and dashboards "
        "that automatically generate continuous monitoring reports for leadership review.</p>"
        "<p><strong>Example 2:</strong> Use <em>Microsoft Defender for Cloud</em> Secure Score to continuously "
        "and automatically assess your cloud security posture and flag configuration drift.</p>"
    ),

    "ca-8": (
        "<p>Penetration testing means hiring skilled testers to actually try to break into your systems the way a "
        "real attacker would. This goes beyond automated scanning to find weaknesses scanners might miss.</p>"
        "<p><strong>Example 1:</strong> Hire a penetration testing firm to conduct an annual test of your external-facing "
        "web applications and network perimeter, delivering a report with findings and recommended fixes.</p>"
        "<p><strong>Example 2:</strong> Use a tool like <em>Cobalt Strike</em> or <em>Metasploit</em> (with proper "
        "authorization) to simulate real-world attacks against your internal network and validate your defenses.</p>"
    ),

    "ca-8-1": (
        "<p>This enhancement requires that penetration testers be independent — they should not be the same people "
        "who built, operate, or defend the system being tested.</p>"
        "<p><strong>Example 1:</strong> Contract with an external penetration testing firm that has no other business "
        "relationship with your organization to ensure truly unbiased results.</p>"
        "<p><strong>Example 2:</strong> If using internal testers, ensure they are from a separate red team that does "
        "not report to the same management chain as the network defenders or system administrators.</p>"
    ),

    "ca-8-2": (
        "<p>Red team exercises go beyond standard penetration testing — red teams simulate a full adversary campaign, "
        "including social engineering, physical access attempts, and multi-stage attacks.</p>"
        "<p><strong>Example 1:</strong> Conduct an annual red team exercise that includes phishing campaigns against "
        "employees, physical security tests of office entry points, and technical exploitation attempts.</p>"
        "<p><strong>Example 2:</strong> Use a red team framework aligned with <em>MITRE ATT&CK</em> to test your "
        "organization's detection and response capabilities across the full attack lifecycle.</p>"
    ),

    "ca-8-3": (
        "<p>This enhancement extends penetration testing to your physical facilities — testing whether someone could "
        "gain unauthorized physical access to your servers, network equipment, or data center.</p>"
        "<p><strong>Example 1:</strong> Hire a physical penetration testing team to attempt to bypass your badge "
        "readers, tailgate through secure doors, and access your server room without authorization.</p>"
        "<p><strong>Example 2:</strong> Test whether your security guards and reception staff follow proper visitor "
        "verification procedures by sending testers posing as delivery personnel or maintenance workers.</p>"
    ),

    "ca-9": (
        "<p>Internal system connections are links between components within your authorization boundary — such as "
        "connecting a new server to your internal network. These still need to be authorized and documented.</p>"
        "<p><strong>Example 1:</strong> Maintain a list of all internal connections in your system security plan, "
        "including connections between your <em>Active Directory</em> domain controllers and member servers.</p>"
        "<p><strong>Example 2:</strong> Before connecting a new <em>IoT device</em> or printer to your internal "
        "network, require IT security approval and document the device, its purpose, and its network segment.</p>"
    ),

    "ca-9-1": (
        "<p>This enhancement requires compliance checks before allowing internal system connections — verifying that "
        "devices meet security requirements before they join the network.</p>"
        "<p><strong>Example 1:</strong> Use <em>Microsoft Intune</em> compliance policies to verify that devices meet "
        "security baselines (encryption enabled, antivirus current, OS patched) before granting network access.</p>"
        "<p><strong>Example 2:</strong> Deploy <em>802.1X network access control</em> on your switches so that "
        "devices must authenticate and pass a health check before being allowed onto the production network.</p>"
    ),

    # =========================================================================
    # CM — Configuration Management (66 controls)
    # =========================================================================

    "cm-1": (
        "<p>This control asks you to create and share written rules for how your organization manages the configuration "
        "of its IT systems — who can make changes, how changes are approved, and how configurations are documented.</p>"
        "<p><strong>Example 1:</strong> Write a <em>Configuration Management Policy</em> that defines roles (such as "
        "a Configuration Control Board), change approval processes, and documentation requirements, stored in SharePoint.</p>"
        "<p><strong>Example 2:</strong> Create step-by-step <em>configuration management procedures</em> in your IT "
        "wiki that explain how technicians request, test, approve, and implement configuration changes.</p>"
    ),

    "cm-2": (
        "<p>A baseline configuration is a documented, approved snapshot of how your system is supposed to be set up. "
        "It covers hardware, software, firmware, and settings. If something changes unexpectedly, you can compare "
        "against the baseline to spot problems.</p>"
        "<p><strong>Example 1:</strong> Use <em>DISA STIGs</em> as your baseline configuration for Windows servers "
        "and apply them via Group Policy Objects (GPOs) to enforce consistent settings across all servers.</p>"
        "<p><strong>Example 2:</strong> Maintain a documented baseline in a <em>SCCM</em> or <em>Intune</em> "
        "configuration profile that defines the approved software, services, and security settings for standard "
        "workstations.</p>"
    ),

    "cm-2-1": (
        "<p>This enhancement requires you to regularly review and update your baseline configuration — not just set "
        "it once and forget it. Baselines must evolve as your environment changes.</p>"
        "<p><strong>Example 1:</strong> Schedule quarterly reviews of your <em>GPO baselines</em> to incorporate "
        "new DISA STIG releases and verify settings still align with current security requirements.</p>"
        "<p><strong>Example 2:</strong> After every major system change (like a Windows version upgrade), update your "
        "baseline documentation in <em>Confluence</em> or your GRC tool and get approval from the CCB.</p>"
    ),

    "cm-2-2": (
        "<p>This enhancement requires automated tools to keep your baseline documentation accurate and current — "
        "manual tracking is too slow and error-prone for complex environments.</p>"
        "<p><strong>Example 1:</strong> Use <em>Microsoft Defender for Endpoint</em> to automatically inventory "
        "installed software and settings across all endpoints and flag deviations from the approved baseline.</p>"
        "<p><strong>Example 2:</strong> Deploy <em>Ansible</em> or <em>Puppet</em> to define your baseline as "
        "code and automatically detect and report configuration drift across your server fleet.</p>"
    ),

    "cm-2-3": (
        "<p>This enhancement requires you to keep previous versions of your baseline configurations so you can roll "
        "back if a change causes problems.</p>"
        "<p><strong>Example 1:</strong> Store all versions of your <em>GPO configurations</em> in a version-controlled "
        "repository like <em>Git</em> so you can compare changes and revert to previous settings if needed.</p>"
        "<p><strong>Example 2:</strong> Before applying STIG updates, export and archive the current <em>Intune</em> "
        "configuration profiles so you have a restore point if the new settings cause issues.</p>"
    ),

    "cm-2-4": (
        "<p>This enhancement was incorporated into CM-7. It previously focused on identifying and preventing "
        "unauthorized software on your systems.</p>"
        "<p><strong>Example 1:</strong> Use <em>Microsoft Defender Application Control</em> (WDAC) to block "
        "execution of any software not on your approved list.</p>"
        "<p><strong>Example 2:</strong> Run regular <em>SCCM</em> software inventory reports and compare them "
        "against your approved software list, flagging unauthorized installations for removal.</p>"
    ),

    "cm-2-5": (
        "<p>This enhancement was incorporated into CM-7. It previously focused on maintaining a list of authorized "
        "software and allowing only that software to run.</p>"
        "<p><strong>Example 1:</strong> Implement <em>AppLocker</em> policies via Group Policy to create an allowlist "
        "of approved applications that can execute on user workstations.</p>"
        "<p><strong>Example 2:</strong> Maintain an approved software catalog in <em>Intune</em> or <em>SCCM</em> "
        "and use application deployment policies to ensure only listed software is available to users.</p>"
    ),

    "cm-2-6": (
        "<p>This enhancement requires separate development and test environments from your production environment, "
        "each with its own documented baseline configuration.</p>"
        "<p><strong>Example 1:</strong> Maintain separate <em>Azure subscriptions</em> or <em>AWS accounts</em> for "
        "development, testing, and production, each with documented baseline configurations and no direct connections "
        "between dev/test and production.</p>"
        "<p><strong>Example 2:</strong> Use <em>VMware</em> or <em>Hyper-V</em> to create isolated virtual networks "
        "for testing configuration changes before deploying them to production servers.</p>"
    ),

    "cm-2-7": (
        "<p>This enhancement requires you to issue specially configured systems for personnel traveling to or working "
        "in high-risk areas, then wipe or inspect those systems when they return.</p>"
        "<p><strong>Example 1:</strong> Issue <em>loaner laptops</em> with minimal data and hardened configurations "
        "for employees traveling to countries with elevated cyber espionage risk, and wipe the devices upon return.</p>"
        "<p><strong>Example 2:</strong> Configure travel devices with <em>full-disk encryption</em>, disabled USB "
        "ports, and VPN-only internet access, and re-image them from a clean baseline after each trip.</p>"
    ),

    "cm-3": (
        "<p>Configuration change control means you have a formal process for requesting, reviewing, approving, and "
        "documenting any changes to your system. No one should make changes without going through the process.</p>"
        "<p><strong>Example 1:</strong> Establish a <em>Configuration Control Board (CCB)</em> that meets weekly to "
        "review change requests submitted through <em>ServiceNow</em> or <em>Jira</em> before any changes are made.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure DevOps</em> or <em>GitHub</em> pull request workflows to "
        "enforce peer review and approval before any infrastructure-as-code changes are deployed to production.</p>"
    ),

    "cm-3-1": (
        "<p>This enhancement requires automated tools to document changes, notify stakeholders, and prevent "
        "unauthorized changes — taking the human error out of change management.</p>"
        "<p><strong>Example 1:</strong> Configure <em>ServiceNow</em> to automatically send email notifications to "
        "the security team and CCB members when change requests are submitted, approved, or implemented.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure Policy</em> or <em>AWS Config Rules</em> to automatically "
        "block changes that violate your security baseline and log all attempted modifications.</p>"
    ),

    "cm-3-2": (
        "<p>This enhancement requires you to test changes in a non-production environment, validate they work "
        "correctly, and document the results before deploying to production.</p>"
        "<p><strong>Example 1:</strong> Before applying a Windows update to production servers, deploy it first to "
        "your <em>test environment</em> in <em>WSUS</em> or <em>SCCM</em> and verify no application compatibility "
        "issues arise during a 48-hour observation period.</p>"
        "<p><strong>Example 2:</strong> Require all firewall rule changes to be tested in a <em>lab firewall</em> "
        "and documented with before/after screenshots before being applied to production <em>Palo Alto</em> devices.</p>"
    ),

    "cm-3-3": (
        "<p>This enhancement requires automated implementation of approved changes — reducing the risk of human error "
        "during deployment.</p>"
        "<p><strong>Example 1:</strong> Use <em>Ansible playbooks</em> or <em>Terraform</em> to automatically deploy "
        "approved configuration changes to servers, ensuring consistency and eliminating manual mistakes.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Intune</em> to automatically push approved configuration "
        "profiles and security baselines to enrolled devices without requiring manual action by technicians.</p>"
    ),

    "cm-3-4": (
        "<p>This enhancement requires that security and privacy representatives be involved in the change control "
        "process — not just IT operations.</p>"
        "<p><strong>Example 1:</strong> Include your <em>ISSO</em> (Information System Security Officer) as a required "
        "approver on all change requests in <em>ServiceNow</em> before changes can proceed to implementation.</p>"
        "<p><strong>Example 2:</strong> Add a security impact assessment checklist to your change request template "
        "that must be completed by the security team before the CCB votes on approval.</p>"
    ),

    "cm-3-5": (
        "<p>This enhancement requires the system to automatically respond to unauthorized configuration changes — "
        "such as reverting changes or alerting administrators.</p>"
        "<p><strong>Example 1:</strong> Use <em>Desired State Configuration (DSC)</em> in PowerShell to automatically "
        "revert server settings back to the approved baseline if someone makes unauthorized changes.</p>"
        "<p><strong>Example 2:</strong> Configure <em>AWS Config</em> auto-remediation rules to automatically revert "
        "security group changes that violate your approved firewall rules.</p>"
    ),

    "cm-3-6": (
        "<p>This enhancement requires formal management of cryptographic mechanisms used in the system, including "
        "tracking certificates, keys, and cryptographic algorithms as configuration items.</p>"
        "<p><strong>Example 1:</strong> Maintain an inventory of all <em>SSL/TLS certificates</em> in a tool like "
        "<em>Venafi</em> or a spreadsheet, tracking expiration dates, key lengths, and issuing certificate authorities.</p>"
        "<p><strong>Example 2:</strong> Document all cryptographic algorithms and key management procedures used "
        "in your system, and include cryptographic changes in your CCB review process.</p>"
    ),

    "cm-3-7": (
        "<p>This enhancement was incorporated into SI-7. It previously required reviewing system changes after "
        "implementation to verify they were applied correctly.</p>"
        "<p><strong>Example 1:</strong> After deploying a change, run a <em>SCAP compliance scan</em> to verify the "
        "system still meets its security baseline and no unintended changes occurred.</p>"
        "<p><strong>Example 2:</strong> Conduct post-implementation reviews at your CCB meeting to confirm changes "
        "were deployed as approved and no unexpected issues were introduced.</p>"
    ),

    "cm-3-8": (
        "<p>This enhancement requires preventing or restricting certain configuration changes entirely — some settings "
        "should be locked down so no one can change them without extraordinary approval.</p>"
        "<p><strong>Example 1:</strong> Use <em>Group Policy</em> to lock critical security settings (like audit "
        "logging and password policies) so that local administrators cannot override them.</p>"
        "<p><strong>Example 2:</strong> In <em>Azure</em>, use resource locks (CanNotDelete, ReadOnly) to prevent "
        "accidental or unauthorized changes to critical infrastructure resources like network security groups.</p>"
    ),

    "cm-4": (
        "<p>Before you make a change to your system, you need to analyze the potential security impact. Will this "
        "change break an existing security control? Could it introduce a new vulnerability?</p>"
        "<p><strong>Example 1:</strong> Before upgrading your <em>firewall firmware</em>, review the vendor release "
        "notes for known security issues and test the upgrade in a lab to verify existing rules still function.</p>"
        "<p><strong>Example 2:</strong> Include a <em>security impact analysis</em> section in every change request "
        "in <em>ServiceNow</em> that requires the submitter to identify which security controls might be affected.</p>"
    ),

    "cm-4-1": (
        "<p>This enhancement requires a separate test environment where you can evaluate the security impact of "
        "changes without risking your production systems.</p>"
        "<p><strong>Example 1:</strong> Maintain a <em>VMware lab environment</em> that mirrors your production "
        "setup where you can test patches, updates, and configuration changes before deploying them live.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure DevTest Labs</em> or <em>AWS sandbox accounts</em> to spin "
        "up temporary environments that replicate production for security impact testing.</p>"
    ),

    "cm-4-2": (
        "<p>This enhancement requires you to verify that security controls still work after making changes — not "
        "just assume they do.</p>"
        "<p><strong>Example 1:</strong> After applying a Windows patch, run a <em>STIG compliance scan</em> to verify "
        "that security controls like audit logging, account lockout, and encryption are still properly configured.</p>"
        "<p><strong>Example 2:</strong> After firewall rule changes, run an <em>Nmap</em> scan to confirm that only "
        "the intended ports are open and previously blocked ports remain closed.</p>"
    ),

    "cm-5": (
        "<p>This control restricts who can make changes to your system. Only authorized personnel should be able to "
        "modify configurations, install software, or change system settings.</p>"
        "<p><strong>Example 1:</strong> Use <em>Active Directory</em> security groups to restrict who has "
        "administrative access to servers, and require <em>privileged access management (PAM)</em> tools like "
        "<em>CyberArk</em> for elevated access.</p>"
        "<p><strong>Example 2:</strong> In <em>Azure</em>, use Role-Based Access Control (RBAC) to limit who can "
        "modify infrastructure settings, granting only the minimum permissions needed for each role.</p>"
    ),

    "cm-5-1": (
        "<p>This enhancement requires automated tools to enforce access restrictions for changes and to create audit "
        "trails of who changed what and when.</p>"
        "<p><strong>Example 1:</strong> Enable <em>Azure Activity Log</em> or <em>AWS CloudTrail</em> to automatically "
        "record every configuration change, including who made it and when.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Windows Event Forwarding</em> to collect audit logs from all "
        "servers showing administrative actions, and send them to your SIEM for monitoring.</p>"
    ),

    "cm-5-2": (
        "<p>This enhancement was incorporated into SI-7. It previously required reviewing system changes to detect "
        "unauthorized modifications.</p>"
        "<p><strong>Example 1:</strong> Use <em>Tripwire</em> or <em>OSSEC</em> file integrity monitoring to detect "
        "unauthorized changes to critical system files and configuration files.</p>"
        "<p><strong>Example 2:</strong> Run weekly comparison reports between your <em>documented baseline</em> and "
        "actual system configurations using SCAP tools to identify unauthorized modifications.</p>"
    ),

    "cm-5-3": (
        "<p>This enhancement requires that software and firmware components be digitally signed to prevent tampering. "
        "Only signed, verified code should be allowed to run or be installed.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Windows Defender Application Control (WDAC)</em> to require "
        "valid digital signatures on all executables before they are allowed to run.</p>"
        "<p><strong>Example 2:</strong> Verify <em>GPG signatures</em> on Linux packages before installation and "
        "configure your package manager (apt/yum) to reject unsigned packages.</p>"
    ),

    "cm-5-4": (
        "<p>This enhancement requires two authorized individuals to approve changes to critical system components — "
        "no single person can make high-impact changes alone.</p>"
        "<p><strong>Example 1:</strong> Configure your <em>GitHub</em> repository to require at least two approving "
        "reviewers on pull requests before code can be merged into the production branch.</p>"
        "<p><strong>Example 2:</strong> Require two authorized administrators to independently approve and execute "
        "firewall rule changes on your <em>Palo Alto</em> or <em>Cisco ASA</em> firewalls for critical rules.</p>"
    ),

    "cm-5-5": (
        "<p>This enhancement limits the privileges of personnel who work on production and operational systems — "
        "developers should not have unrestricted access to production.</p>"
        "<p><strong>Example 1:</strong> Implement separate <em>Active Directory</em> accounts for system "
        "administrators — a standard user account for daily work and a separate admin account used only for "
        "production changes, managed through <em>CyberArk</em> or <em>Azure PIM</em>.</p>"
        "<p><strong>Example 2:</strong> In your CI/CD pipeline, ensure developers can deploy to test environments "
        "but only designated operations staff can deploy to production using <em>Azure DevOps</em> environment gates.</p>"
    ),

    "cm-5-6": (
        "<p>This enhancement restricts the ability to modify shared software libraries — unauthorized changes to "
        "libraries could affect many systems at once.</p>"
        "<p><strong>Example 1:</strong> Restrict write access to your shared <em>NuGet</em>, <em>npm</em>, or "
        "<em>PyPI</em> package repositories to only designated library maintainers using repository access controls.</p>"
        "<p><strong>Example 2:</strong> Use read-only file permissions on shared DLL directories on application "
        "servers, requiring change requests and elevated access to modify any shared library files.</p>"
    ),

    "cm-5-7": (
        "<p>This enhancement was incorporated into SI-7. It previously required automatic implementation of security "
        "safeguards when unauthorized changes were detected.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Desired State Configuration (DSC)</em> to automatically revert "
        "critical settings to their approved state when drift is detected.</p>"
        "<p><strong>Example 2:</strong> Use <em>AWS Config</em> auto-remediation to automatically restore S3 bucket "
        "policies if they are changed to allow public access.</p>"
    ),

    "cm-6": (
        "<p>This control requires you to establish, document, and enforce specific security settings for all IT "
        "products in your environment. Think of it as the specific knobs and dials you set on each system.</p>"
        "<p><strong>Example 1:</strong> Apply <em>DISA STIGs</em> to your Windows servers and workstations using "
        "Group Policy, enforcing settings like password complexity, screen lock timeout, and audit logging.</p>"
        "<p><strong>Example 2:</strong> Configure your <em>Cisco</em> or <em>Palo Alto</em> network devices according "
        "to the vendor's security hardening guide and DISA Network STIG, documenting all settings applied.</p>"
    ),

    "cm-6-1": (
        "<p>This enhancement requires automated tools to manage, apply, and verify your configuration settings — "
        "manual spot-checking is not sufficient.</p>"
        "<p><strong>Example 1:</strong> Use <em>SCAP Compliance Checker (SCC)</em> to automatically scan systems "
        "against STIG benchmarks and generate compliance reports showing which settings pass or fail.</p>"
        "<p><strong>Example 2:</strong> Deploy <em>Intune</em> configuration profiles to automatically apply and "
        "enforce security settings on all enrolled Windows devices, with compliance reporting in the admin center.</p>"
    ),

    "cm-6-2": (
        "<p>This enhancement requires your system to automatically respond to unauthorized configuration changes — "
        "not just detect them, but take action.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Microsoft Defender for Endpoint</em> to automatically quarantine "
        "a device that falls out of compliance with your security baseline until it is remediated.</p>"
        "<p><strong>Example 2:</strong> Set up <em>Azure Policy</em> with DeployIfNotExists effects to automatically "
        "remediate non-compliant resource configurations in your cloud environment.</p>"
    ),

    "cm-6-3": (
        "<p>This enhancement was incorporated into SI-7. It previously focused on detecting unauthorized changes to "
        "configuration settings.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>Tripwire</em> or <em>AIDE</em> to monitor critical configuration "
        "files (like /etc/passwd, registry hives, or firewall rules) and alert on any unauthorized changes.</p>"
        "<p><strong>Example 2:</strong> Use <em>AWS Config</em> or <em>Azure Policy</em> compliance dashboards to "
        "continuously monitor for configuration drift from your approved settings.</p>"
    ),

    "cm-6-4": (
        "<p>This enhancement requires you to be able to demonstrate that your systems are configured as intended — "
        "you need evidence, not just assertions.</p>"
        "<p><strong>Example 1:</strong> Generate weekly <em>SCAP scan reports</em> that show compliance percentages "
        "for each STIG benchmark, providing auditors with concrete evidence of configuration conformance.</p>"
        "<p><strong>Example 2:</strong> Maintain a <em>configuration compliance dashboard</em> in <em>Splunk</em> or "
        "<em>Power BI</em> that shows real-time conformance status across all systems for auditor review.</p>"
    ),

    "cm-7": (
        "<p>Least functionality means your systems should only have the services, ports, protocols, and software that "
        "are absolutely necessary for their mission. Everything else gets turned off or removed.</p>"
        "<p><strong>Example 1:</strong> Disable unnecessary Windows services (like Print Spooler on servers that do "
        "not print) and close unused ports via <em>Windows Firewall</em> GPO settings.</p>"
        "<p><strong>Example 2:</strong> On your <em>Linux</em> servers, uninstall packages that are not required for "
        "the server's function (like GUI components on a headless server) and disable unused network services.</p>"
    ),

    "cm-7-1": (
        "<p>This enhancement requires periodic review of your system functions, ports, protocols, and services to "
        "ensure nothing unnecessary has crept in over time.</p>"
        "<p><strong>Example 1:</strong> Conduct quarterly <em>Nmap</em> scans of your network to identify any new "
        "open ports or services that were not in the approved baseline, and disable any unauthorized ones.</p>"
        "<p><strong>Example 2:</strong> Review <em>Windows Firewall</em> rules and running services on all servers "
        "every 90 days, removing any that are no longer needed for business operations.</p>"
    ),

    "cm-7-2": (
        "<p>This enhancement requires automated mechanisms to prevent unauthorized software from running — not just "
        "policies, but technical enforcement.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>AppLocker</em> or <em>WDAC</em> policies via Group Policy to "
        "technically prevent users from running executables that are not on the approved allowlist.</p>"
        "<p><strong>Example 2:</strong> Use <em>SELinux</em> or <em>AppArmor</em> on Linux systems to confine "
        "applications to only the resources and actions they need, blocking unauthorized program execution.</p>"
    ),

    "cm-7-3": (
        "<p>This enhancement requires that software components be registered and tracked in a central system — you "
        "need to know what software is running and ensure it complies with licensing and security requirements.</p>"
        "<p><strong>Example 1:</strong> Maintain a <em>software register</em> in your asset management tool that "
        "lists all approved software with version numbers, license counts, and security approval status.</p>"
        "<p><strong>Example 2:</strong> Use <em>SCCM Software Metering</em> or <em>Intune</em> discovered apps to "
        "track what software is actually installed and running, comparing against your approved list.</p>"
    ),

    "cm-7-4": (
        "<p>This enhancement implements a deny-by-exception approach to software — everything is blocked unless "
        "explicitly authorized. This is a strong security posture.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Windows Defender Application Control (WDAC)</em> in enforce "
        "mode to block all unsigned or unapproved applications, with a formal exception process for business needs.</p>"
        "<p><strong>Example 2:</strong> Deploy <em>Carbon Black App Control</em> to block unapproved software "
        "from executing on endpoints, requiring IT security approval to add new applications to the allowlist.</p>"
    ),

    "cm-7-5": (
        "<p>This enhancement implements an allow-by-exception approach — you maintain a list of approved software, "
        "and only software on that list is permitted to run.</p>"
        "<p><strong>Example 1:</strong> Create <em>AppLocker</em> allowlist policies that permit only signed "
        "Microsoft applications and your organization's approved business applications to execute.</p>"
        "<p><strong>Example 2:</strong> Use your <em>Intune</em> managed apps feature to deploy only approved "
        "applications to devices and block installation of applications from outside the managed catalog.</p>"
    ),

    "cm-7-6": (
        "<p>This enhancement requires running software in confined environments with limited privileges — "
        "sandboxing or containerization to limit the damage if software is compromised.</p>"
        "<p><strong>Example 1:</strong> Run web-facing applications in <em>Docker containers</em> with minimal "
        "privileges and no access to the host filesystem beyond their designated volumes.</p>"
        "<p><strong>Example 2:</strong> Use <em>Windows Sandbox</em> or <em>Microsoft Application Guard</em> to "
        "open untrusted files and browse untrusted websites in an isolated environment.</p>"
    ),

    "cm-7-7": (
        "<p>This enhancement requires code to execute in protected environments with integrity verification — "
        "ensuring code has not been tampered with before execution.</p>"
        "<p><strong>Example 1:</strong> Enable <em>Secure Boot</em> and <em>Measured Boot</em> on all systems to "
        "verify the integrity of boot code and operating system components before they execute.</p>"
        "<p><strong>Example 2:</strong> Use <em>code signing certificates</em> for all internally developed "
        "applications and configure systems to only execute code with valid signatures.</p>"
    ),

    "cm-7-8": (
        "<p>This enhancement prohibits using binary or machine-executable code from unknown or untrusted sources — "
        "if you cannot verify where the code came from, do not run it.</p>"
        "<p><strong>Example 1:</strong> Block execution of downloaded executables that lack valid digital signatures "
        "using <em>Windows SmartScreen</em> and <em>WDAC</em> policies.</p>"
        "<p><strong>Example 2:</strong> Prohibit developers from using pre-compiled binary dependencies without "
        "verifying their source and integrity through <em>hash verification</em> or trusted package registries.</p>"
    ),

    "cm-7-9": (
        "<p>This enhancement extends least functionality to hardware — prohibiting unauthorized hardware components "
        "like USB devices, unauthorized network adapters, or rogue wireless access points.</p>"
        "<p><strong>Example 1:</strong> Use <em>Group Policy</em> to disable USB mass storage devices on all "
        "workstations, allowing only approved peripherals like keyboards and mice.</p>"
        "<p><strong>Example 2:</strong> Deploy <em>wireless intrusion detection</em> to identify unauthorized "
        "wireless access points connected to your network and physically locate them for removal.</p>"
    ),

    "cm-8": (
        "<p>You must maintain a complete, accurate inventory of all system components — every server, workstation, "
        "network device, and software application. You cannot protect what you do not know about.</p>"
        "<p><strong>Example 1:</strong> Use <em>Microsoft Intune</em> and <em>SCCM</em> to automatically inventory "
        "all enrolled devices including hardware specifications, installed software, and patch levels.</p>"
        "<p><strong>Example 2:</strong> Maintain a centralized asset inventory in a tool like <em>ServiceNow CMDB</em> "
        "that includes servers, network devices, applications, and their owners, updated whenever assets are "
        "added or removed.</p>"
    ),

    "cm-8-1": (
        "<p>This enhancement requires you to update your inventory whenever new components are installed or existing "
        "ones are removed — not just during periodic reviews.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Intune</em> auto-enrollment so that when a new device joins "
        "your network, it automatically appears in your asset inventory with its hardware and software details.</p>"
        "<p><strong>Example 2:</strong> Include inventory update steps in your <em>ServiceNow change management</em> "
        "workflow so that installing or removing hardware automatically triggers a CMDB update.</p>"
    ),

    "cm-8-2": (
        "<p>This enhancement requires automated tools to maintain your inventory — manual spreadsheets are not "
        "sufficient for keeping an accurate, real-time picture of your environment.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>Qualys Asset Inventory</em> or <em>Tenable.io</em> to continuously "
        "discover and catalog all devices on your network, including shadow IT devices.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure Resource Graph</em> or <em>AWS Config</em> to automatically "
        "maintain an inventory of all cloud resources across all subscriptions and accounts.</p>"
    ),

    "cm-8-3": (
        "<p>This enhancement requires automated detection of unauthorized components on your network — finding "
        "rogue devices that should not be there.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>802.1X port-based network access control</em> to detect and "
        "block unauthorized devices that attempt to connect to your network switches.</p>"
        "<p><strong>Example 2:</strong> Use <em>Nmap</em> or <em>Rumble</em> network discovery scans weekly to "
        "identify unknown devices on your network and compare results against your approved asset inventory.</p>"
    ),

    "cm-8-4": (
        "<p>This enhancement requires your inventory to include accountability information — who owns each component, "
        "who is responsible for it, and how to contact them.</p>"
        "<p><strong>Example 1:</strong> In your <em>ServiceNow CMDB</em>, every asset record should include an "
        "assigned owner, department, location, and the name of the system it belongs to.</p>"
        "<p><strong>Example 2:</strong> Tag all <em>Azure</em> or <em>AWS</em> cloud resources with owner, cost "
        "center, environment, and system-of-record tags so every resource is traceable to a responsible person.</p>"
    ),

    "cm-8-5": (
        "<p>This enhancement prevents the same component from being counted in multiple systems' inventories — "
        "each component should belong to exactly one system boundary.</p>"
        "<p><strong>Example 1:</strong> In <em>eMASS</em> or your GRC tool, validate that each asset is assigned "
        "to only one authorization boundary and not listed as part of multiple systems.</p>"
        "<p><strong>Example 2:</strong> Run quarterly reports from your <em>CMDB</em> to identify any assets "
        "assigned to multiple system records and resolve the ownership conflicts.</p>"
    ),

    "cm-8-6": (
        "<p>This enhancement requires your inventory to include the assessed security configuration status and any "
        "approved deviations from the baseline for each component.</p>"
        "<p><strong>Example 1:</strong> Link each asset in your <em>CMDB</em> to its most recent <em>STIG scan</em> "
        "results, showing which settings are compliant and which have approved exceptions documented in the POA&M.</p>"
        "<p><strong>Example 2:</strong> Maintain a deviation register that documents any approved departures from "
        "your standard security baseline, cross-referenced to the specific assets and the business justification.</p>"
    ),

    "cm-8-7": (
        "<p>This enhancement requires a centralized repository for your component inventory — one authoritative source "
        "of truth rather than scattered spreadsheets.</p>"
        "<p><strong>Example 1:</strong> Use <em>ServiceNow CMDB</em> as your single authoritative inventory, "
        "integrating data feeds from <em>Intune</em>, <em>Qualys</em>, and <em>Active Directory</em> into one view.</p>"
        "<p><strong>Example 2:</strong> Centralize your cloud resource inventory using <em>Azure Resource Graph</em> "
        "or <em>AWS Organizations</em> to provide a single pane of glass across all accounts and subscriptions.</p>"
    ),

    "cm-8-8": (
        "<p>This enhancement requires automated tracking of component locations — knowing not just what you have, "
        "but where it is physically or logically located.</p>"
        "<p><strong>Example 1:</strong> Use <em>Intune</em> device compliance policies to track the last check-in "
        "location and network of managed devices, flagging devices that appear in unexpected locations.</p>"
        "<p><strong>Example 2:</strong> For data center equipment, maintain rack location data in your <em>CMDB</em> "
        "with barcode or RFID tracking to verify physical location during audits.</p>"
    ),

    "cm-8-9": (
        "<p>This enhancement requires that every component be assigned to a specific system — no orphaned assets "
        "floating around without a designated system owner.</p>"
        "<p><strong>Example 1:</strong> During your quarterly inventory review, run a report from your <em>CMDB</em> "
        "to identify any assets not assigned to a system boundary and work with asset owners to resolve them.</p>"
        "<p><strong>Example 2:</strong> In your <em>Azure</em> environment, use resource groups and management groups "
        "to ensure every resource is organized under a system and tagged with the system name.</p>"
    ),

    "cm-9": (
        "<p>A configuration management plan describes your overall strategy for managing configurations — who is "
        "responsible, what tools you use, how changes are controlled, and how you maintain baselines.</p>"
        "<p><strong>Example 1:</strong> Write a <em>Configuration Management Plan</em> document that identifies your "
        "CCB members, the tools you use (like <em>SCCM</em>, <em>Ansible</em>, <em>Git</em>), and your change "
        "management workflow from request through implementation.</p>"
        "<p><strong>Example 2:</strong> Include a section in your CM plan that defines which configuration items are "
        "under formal change control (operating systems, firewalls, databases) versus items managed informally.</p>"
    ),

    "cm-9-1": (
        "<p>This enhancement requires you to assign specific responsibility for configuration management to "
        "designated individuals or roles — someone must own this process.</p>"
        "<p><strong>Example 1:</strong> Designate a <em>Configuration Manager</em> role in your IT organization "
        "who is responsible for maintaining baselines, running the CCB, and tracking configuration changes.</p>"
        "<p><strong>Example 2:</strong> In your system security plan, name the specific individuals responsible "
        "for configuration management of each major system component (servers, network, applications).</p>"
    ),

    "cm-10": (
        "<p>This control requires you to use software in accordance with license agreements and copyright law. "
        "Pirated or unlicensed software is both a legal risk and a security risk.</p>"
        "<p><strong>Example 1:</strong> Use <em>Microsoft 365 Admin Center</em> license management to track how "
        "many licenses you own versus how many are assigned, ensuring you do not exceed your entitlements.</p>"
        "<p><strong>Example 2:</strong> Deploy a software asset management tool like <em>Snow License Manager</em> "
        "or <em>Flexera</em> to automatically track software installations against purchased license counts.</p>"
    ),

    "cm-10-1": (
        "<p>This enhancement addresses the use of open-source software — you need policies governing when and how "
        "open-source components can be used, including license compliance and security vetting.</p>"
        "<p><strong>Example 1:</strong> Require all developers to run open-source dependencies through <em>Snyk</em> "
        "or <em>Black Duck</em> to check for known vulnerabilities and license conflicts before use.</p>"
        "<p><strong>Example 2:</strong> Maintain an approved list of open-source libraries with accepted license "
        "types (MIT, Apache 2.0) and require review for any library with a restrictive license like GPL.</p>"
    ),

    "cm-11": (
        "<p>This control restricts users from installing software on their own — only approved software should be "
        "installed, and only through approved methods.</p>"
        "<p><strong>Example 1:</strong> Remove local administrator rights from standard users via <em>Group Policy</em> "
        "so they cannot install software on their workstations without IT involvement.</p>"
        "<p><strong>Example 2:</strong> Provide a self-service <em>Intune Company Portal</em> or <em>SCCM Software "
        "Center</em> where users can install only pre-approved applications without needing admin rights.</p>"
    ),

    "cm-11-1": (
        "<p>This enhancement was incorporated into CM-8(3). It previously required alerts when users attempted to "
        "install unauthorized software.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Microsoft Defender for Endpoint</em> to generate alerts when "
        "blocked applications attempt to install or execute on managed devices.</p>"
        "<p><strong>Example 2:</strong> Set up <em>SIEM alerts</em> in <em>Splunk</em> or <em>Sentinel</em> to "
        "notify the security team when software installation events are detected outside approved workflows.</p>"
    ),

    "cm-11-2": (
        "<p>This enhancement requires that software installation only be performed by users with appropriate "
        "privileged access — standard users should not have installation capabilities.</p>"
        "<p><strong>Example 1:</strong> Enforce <em>UAC (User Account Control)</em> settings via Group Policy to "
        "require administrator credentials for any software installation, even if the user has some admin rights.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure PIM</em> (Privileged Identity Management) to grant "
        "just-in-time admin access for software installation tasks, automatically revoking access after a set period.</p>"
    ),

    "cm-11-3": (
        "<p>This enhancement requires automated enforcement and monitoring of software installation restrictions — "
        "technical controls, not just policies.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>AppLocker</em> policies that technically block installation of "
        "any software not signed by your organization or trusted publishers.</p>"
        "<p><strong>Example 2:</strong> Use <em>Intune compliance policies</em> to continuously monitor devices "
        "for unauthorized software and automatically mark non-compliant devices for remediation.</p>"
    ),

    "cm-12": (
        "<p>This control requires you to know where your important information lives — which systems, databases, and "
        "storage locations contain sensitive data like CUI, PII, or financial records.</p>"
        "<p><strong>Example 1:</strong> Use <em>Microsoft Purview Data Map</em> to scan your file shares, SharePoint "
        "sites, and databases to discover and classify where sensitive data resides across your organization.</p>"
        "<p><strong>Example 2:</strong> Create a <em>data flow diagram</em> that shows where CUI enters your "
        "environment, where it is stored, where it is processed, and where it exits, and review it annually.</p>"
    ),

    "cm-12-1": (
        "<p>This enhancement requires automated tools to help you discover and track where information is stored — "
        "manual data hunts miss too much.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>Microsoft Purview DLP</em> with content inspection policies to "
        "automatically discover files containing sensitive data patterns (SSNs, credit card numbers, CUI markings).</p>"
        "<p><strong>Example 2:</strong> Use <em>Varonis</em> or <em>Netwrix</em> to automatically scan file servers "
        "and SharePoint for sensitive data, generating reports on where it resides and who has access.</p>"
    ),

    "cm-13": (
        "<p>Data action mapping requires you to document how personal information moves through your system — what "
        "data actions are performed (collection, storage, sharing, deletion) and by which components.</p>"
        "<p><strong>Example 1:</strong> Create a <em>data flow diagram</em> in Visio or Lucidchart showing how "
        "customer PII flows from your web form to your database to your CRM to your email system.</p>"
        "<p><strong>Example 2:</strong> Use <em>Microsoft Purview Compliance Manager</em> to map data processing "
        "activities against privacy requirements and identify gaps in your data handling procedures.</p>"
    ),

    "cm-14": (
        "<p>This control requires that system components use digitally signed code to verify integrity and "
        "authenticity — ensuring software has not been tampered with since it was produced.</p>"
        "<p><strong>Example 1:</strong> Require all vendor software to include valid <em>code signing certificates</em> "
        "and verify signatures before deploying updates to production systems.</p>"
        "<p><strong>Example 2:</strong> Sign all internally developed PowerShell scripts and configure your "
        "<em>execution policy</em> to AllSigned, preventing execution of unsigned or tampered scripts.</p>"
    ),

    # =========================================================================
    # CP — Contingency Planning (56 controls)
    # =========================================================================

    "cp-1": (
        "<p>This control asks you to create and share written rules for how your organization plans for and responds "
        "to disruptions — natural disasters, cyberattacks, system failures, or any event that could take your "
        "systems offline.</p>"
        "<p><strong>Example 1:</strong> Write a <em>Contingency Planning Policy</em> that defines leadership roles "
        "during a disaster, maximum acceptable downtime for each system, and when to activate the contingency plan.</p>"
        "<p><strong>Example 2:</strong> Create step-by-step <em>contingency procedures</em> stored in both SharePoint "
        "and printed binders so staff can follow them even if the network is down.</p>"
    ),

    "cp-2": (
        "<p>A contingency plan is your written playbook for keeping your business running when something goes wrong. "
        "It identifies your most important systems, defines recovery priorities, and assigns responsibilities.</p>"
        "<p><strong>Example 1:</strong> Create a contingency plan document that lists your critical systems (email, "
        "ERP, file shares), their Recovery Time Objectives (e.g., email restored within 4 hours), and the specific "
        "steps to restore each one from backups.</p>"
        "<p><strong>Example 2:</strong> Include contact lists for key personnel, vendor support numbers, and "
        "<em>Azure</em> or <em>AWS</em> support escalation procedures in your contingency plan, with copies stored "
        "offsite and in print.</p>"
    ),

    "cp-2-1": (
        "<p>This enhancement requires your contingency plan to coordinate with related plans — like your incident "
        "response plan, business continuity plan, and disaster recovery plan.</p>"
        "<p><strong>Example 1:</strong> Cross-reference your contingency plan with your <em>incident response plan</em> "
        "so that when a major security incident triggers a system outage, both plans activate in coordination.</p>"
        "<p><strong>Example 2:</strong> Coordinate with your building's <em>physical emergency plan</em> (fire, "
        "evacuation) so that IT contingency procedures account for scenarios where the building is inaccessible.</p>"
    ),

    "cp-2-2": (
        "<p>This enhancement requires capacity planning as part of contingency planning — your backup systems and "
        "alternate sites need enough capacity to handle the workload during a disaster.</p>"
        "<p><strong>Example 1:</strong> Ensure your <em>Azure Site Recovery</em> or <em>AWS Disaster Recovery</em> "
        "environment has enough compute and storage capacity to run your critical workloads at acceptable performance.</p>"
        "<p><strong>Example 2:</strong> Document the minimum bandwidth, storage, and processing requirements for "
        "each critical system so your alternate site can be properly provisioned before a disaster strikes.</p>"
    ),

    "cp-2-3": (
        "<p>This enhancement requires your contingency plan to address resuming essential mission and business "
        "functions within a defined time period after a disruption.</p>"
        "<p><strong>Example 1:</strong> Define specific Recovery Time Objectives (RTOs) for each critical function — "
        "for example, email within 4 hours, ERP within 8 hours, file shares within 24 hours.</p>"
        "<p><strong>Example 2:</strong> Document the sequence of system restoration in your plan: restore "
        "<em>Active Directory</em> first, then DNS, then email, then business applications, ensuring dependencies "
        "are addressed in order.</p>"
    ),

    "cp-2-4": (
        "<p>This enhancement requires your contingency plan to address resuming <em>all</em> mission and business "
        "functions — not just the critical ones — within a defined time period.</p>"
        "<p><strong>Example 1:</strong> Beyond your critical systems, define recovery timelines for secondary systems "
        "like training platforms, development environments, and reporting tools within 72 hours.</p>"
        "<p><strong>Example 2:</strong> Include a phased recovery schedule in your plan that shows when each system "
        "tier (critical, important, nice-to-have) will be restored after a full disaster scenario.</p>"
    ),

    "cp-2-5": (
        "<p>This enhancement requires the ability to continue essential functions with minimal or no interruption — "
        "true high availability rather than just recovery after a disruption.</p>"
        "<p><strong>Example 1:</strong> Deploy critical applications across multiple <em>Azure Availability Zones</em> "
        "or <em>AWS Regions</em> so that if one zone fails, the application automatically fails over to another.</p>"
        "<p><strong>Example 2:</strong> Implement <em>Always On Availability Groups</em> for your SQL Server databases "
        "with automatic failover to a secondary replica in a different data center.</p>"
    ),

    "cp-2-6": (
        "<p>This enhancement requires your contingency plan to address alternate processing and storage sites "
        "specifically — where will you operate if your primary location is unavailable?</p>"
        "<p><strong>Example 1:</strong> Document your <em>Azure paired region</em> or secondary data center as your "
        "alternate processing site, including the procedures to activate it and redirect users.</p>"
        "<p><strong>Example 2:</strong> Establish an agreement with a colocation provider for emergency rack space "
        "and document the procedures for shipping and installing backup equipment at the alternate site.</p>"
    ),

    "cp-2-7": (
        "<p>This enhancement requires coordination with external service providers as part of your contingency "
        "planning — your plan must account for their capabilities and limitations.</p>"
        "<p><strong>Example 1:</strong> Review your <em>Microsoft 365</em> and <em>Azure</em> SLAs to understand "
        "what Microsoft guarantees during an outage and build your contingency plan around those commitments.</p>"
        "<p><strong>Example 2:</strong> Include your ISP's emergency contact information and SLA terms in your "
        "contingency plan, along with procedures for activating backup internet connections.</p>"
    ),

    "cp-2-8": (
        "<p>This enhancement requires you to identify your most critical assets as part of contingency planning — "
        "what systems and data absolutely must be protected and recovered first?</p>"
        "<p><strong>Example 1:</strong> Conduct a <em>Business Impact Analysis (BIA)</em> to rank your systems by "
        "criticality and identify which ones would cause the most damage if unavailable for extended periods.</p>"
        "<p><strong>Example 2:</strong> Create a <em>critical asset list</em> that includes your domain controllers, "
        "financial databases, CUI repositories, and customer-facing systems, with each asset's RTO and RPO defined.</p>"
    ),

    "cp-3": (
        "<p>Your staff need to be trained on the contingency plan so they know what to do when disaster strikes. "
        "Training should happen when people join and be refreshed regularly.</p>"
        "<p><strong>Example 1:</strong> Include contingency plan orientation in your <em>new employee onboarding</em> "
        "process, covering their role during a disaster, communication procedures, and where to find the plan.</p>"
        "<p><strong>Example 2:</strong> Conduct annual <em>tabletop exercises</em> where IT staff walk through a "
        "disaster scenario (like a ransomware attack) and practice their response procedures step by step.</p>"
    ),

    "cp-3-1": (
        "<p>This enhancement requires training to include simulated events — not just reading the plan, but "
        "practicing the response in realistic scenarios.</p>"
        "<p><strong>Example 1:</strong> Run a <em>simulated ransomware scenario</em> where IT staff practice "
        "isolating infected systems, restoring from backups, and communicating with leadership under time pressure.</p>"
        "<p><strong>Example 2:</strong> Conduct a simulated <em>data center failure</em> exercise where staff "
        "practice failing over to the backup site using your documented contingency procedures.</p>"
    ),

    "cp-3-2": (
        "<p>This enhancement requires training environments to use the same mechanisms (tools, systems, procedures) "
        "that would be used during an actual contingency event.</p>"
        "<p><strong>Example 1:</strong> Practice your <em>Azure Site Recovery</em> failover procedures in a training "
        "environment that uses the same recovery tools and dashboards as production.</p>"
        "<p><strong>Example 2:</strong> Train your backup operators on the actual <em>Veeam</em> or <em>Commvault</em> "
        "restore interface using a test restore environment, so they are familiar with the tools when it matters.</p>"
    ),

    "cp-4": (
        "<p>You must regularly test your contingency plan to make sure it actually works. A plan that has never been "
        "tested is just a hope, not a plan.</p>"
        "<p><strong>Example 1:</strong> Conduct an annual <em>full backup restoration test</em> where you restore "
        "critical systems from backup media to verify the backups are complete and the procedures are accurate.</p>"
        "<p><strong>Example 2:</strong> Run a semi-annual <em>tabletop exercise</em> with IT leadership and key "
        "staff to walk through a disaster scenario, identify gaps in the plan, and update procedures accordingly.</p>"
    ),

    "cp-4-1": (
        "<p>This enhancement requires your contingency plan tests to be coordinated with tests of related plans — "
        "incident response, business continuity, and others.</p>"
        "<p><strong>Example 1:</strong> Schedule your contingency plan test on the same day as your <em>incident "
        "response exercise</em> to practice how both teams coordinate when a security incident causes a system outage.</p>"
        "<p><strong>Example 2:</strong> Coordinate your IT disaster recovery test with your facilities team's "
        "<em>building evacuation drill</em> to simulate a scenario where physical access is lost simultaneously.</p>"
    ),

    "cp-4-2": (
        "<p>This enhancement requires testing your contingency plan at the alternate processing site — not just "
        "in theory, but by actually failing over to the backup location.</p>"
        "<p><strong>Example 1:</strong> Conduct an annual <em>Azure Site Recovery</em> test failover to your "
        "secondary region and verify that critical applications are accessible and functional at the backup site.</p>"
        "<p><strong>Example 2:</strong> Perform a live test where your team sets up operations at your designated "
        "<em>alternate office location</em> and verifies VPN connectivity, phone systems, and application access.</p>"
    ),

    "cp-4-3": (
        "<p>This enhancement requires automated testing of your contingency plan — using tools to regularly validate "
        "that recovery mechanisms work without waiting for annual manual tests.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Azure Site Recovery</em> to run automated test failovers monthly, "
        "generating reports that confirm virtual machines can be successfully recovered at the secondary site.</p>"
        "<p><strong>Example 2:</strong> Use <em>Veeam SureBackup</em> to automatically verify backup integrity by "
        "booting backed-up VMs in an isolated environment and running health checks nightly.</p>"
    ),

    "cp-4-4": (
        "<p>This enhancement requires full recovery and reconstitution testing — restoring the system completely from "
        "scratch to verify you can rebuild from bare metal if necessary.</p>"
        "<p><strong>Example 1:</strong> Annually perform a <em>bare-metal restore</em> of a critical server from "
        "backup to verify that your backup includes everything needed to fully rebuild the system.</p>"
        "<p><strong>Example 2:</strong> Test your <em>infrastructure-as-code</em> scripts (Terraform, ARM templates) "
        "by deploying a complete copy of your production environment from scratch in an isolated subscription.</p>"
    ),

    "cp-4-5": (
        "<p>This enhancement requires your organization to challenge itself by simulating disruptions to test "
        "resilience — proactively breaking things to find weaknesses before real disasters do.</p>"
        "<p><strong>Example 1:</strong> Implement a <em>chaos engineering</em> practice using tools like "
        "<em>Azure Chaos Studio</em> to randomly disrupt services in a controlled way and validate your recovery.</p>"
        "<p><strong>Example 2:</strong> Conduct unannounced contingency tests where IT leadership simulates a "
        "system failure without advance warning to staff, testing their ability to respond under realistic conditions.</p>"
    ),

    "cp-5": (
        "<p>This control was incorporated into CP-2. It required that your contingency plan be reviewed and updated "
        "regularly to reflect changes in your environment, lessons learned, and new threats.</p>"
        "<p><strong>Example 1:</strong> After every contingency plan test or real incident, conduct a <em>lessons "
        "learned</em> session and update the plan to address any gaps or procedural issues discovered.</p>"
        "<p><strong>Example 2:</strong> Review your contingency plan whenever significant system changes occur — like "
        "migrating to a new <em>cloud platform</em> or adding a new critical business application.</p>"
    ),

    "cp-6": (
        "<p>An alternate storage site is a separate location where you keep copies of your backups and critical data. "
        "If your primary location is destroyed, you can recover from the alternate site.</p>"
        "<p><strong>Example 1:</strong> Replicate your backups to an <em>Azure Blob Storage</em> account in a "
        "different geographic region using geo-redundant storage (GRS) or to an offsite <em>Veeam Cloud Connect</em> "
        "repository.</p>"
        "<p><strong>Example 2:</strong> Store encrypted backup tapes at a secure offsite facility like <em>Iron "
        "Mountain</em>, with documented procedures for retrieving them in an emergency.</p>"
    ),

    "cp-6-1": (
        "<p>This enhancement requires your alternate storage site to be geographically separated from the primary "
        "site — far enough that a single disaster (flood, hurricane) cannot affect both.</p>"
        "<p><strong>Example 1:</strong> Store backup replicas in an <em>Azure region</em> at least 300 miles from "
        "your primary region (e.g., East US primary, West US secondary) to protect against regional disasters.</p>"
        "<p><strong>Example 2:</strong> Choose an offsite tape storage facility in a different <em>FEMA flood zone</em> "
        "and different utility grid than your primary data center.</p>"
    ),

    "cp-6-2": (
        "<p>This enhancement requires your alternate storage site to support your Recovery Time Objectives (RTO) and "
        "Recovery Point Objectives (RPO) — your backups need to be recent enough and accessible fast enough.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Azure Site Recovery</em> with a replication frequency of 15 "
        "minutes to meet a 15-minute RPO, and verify that your secondary region can spin up VMs within your 4-hour RTO.</p>"
        "<p><strong>Example 2:</strong> Use <em>Veeam</em> backup copy jobs to replicate backups to your offsite "
        "location every hour, ensuring data loss is limited to no more than one hour of work (1-hour RPO).</p>"
    ),

    "cp-6-3": (
        "<p>This enhancement requires your alternate storage site to be accessible during a disruption — there is "
        "no point in having backups you cannot reach when you need them.</p>"
        "<p><strong>Example 1:</strong> Ensure your offsite <em>Azure</em> or <em>AWS</em> backup storage is "
        "accessible via an independent internet connection that does not depend on your primary site's network.</p>"
        "<p><strong>Example 2:</strong> Verify that key personnel have VPN credentials and procedures to access the "
        "alternate storage site from home or a mobile location during a facility-level disaster.</p>"
    ),

    "cp-7": (
        "<p>An alternate processing site is a separate location where you can run your systems if your primary site "
        "goes down. This could be a second data center, a cloud region, or a hot standby facility.</p>"
        "<p><strong>Example 1:</strong> Maintain a secondary <em>Azure region</em> with pre-configured infrastructure "
        "using <em>Azure Site Recovery</em> that can be activated within hours of a primary site failure.</p>"
        "<p><strong>Example 2:</strong> Contract with a <em>disaster recovery service provider</em> for dedicated "
        "rack space and pre-staged equipment that can be activated within your defined recovery time.</p>"
    ),

    "cp-7-1": (
        "<p>This enhancement requires your alternate processing site to be geographically separated from the primary "
        "site to protect against regional disasters.</p>"
        "<p><strong>Example 1:</strong> Select an alternate <em>Azure region</em> in a different geographic area "
        "(e.g., East US and West US) to ensure a regional disaster cannot affect both sites simultaneously.</p>"
        "<p><strong>Example 2:</strong> If using physical sites, choose a backup facility at least 100 miles from "
        "your primary data center, in a different utility service area and flood zone.</p>"
    ),

    "cp-7-2": (
        "<p>This enhancement requires your alternate processing site to be accessible and ready for use during a "
        "disruption — staff need to be able to get there and operate.</p>"
        "<p><strong>Example 1:</strong> Pre-stage <em>VPN concentrators</em> and remote access infrastructure at "
        "your alternate site so that staff can connect and work remotely even if the primary office is inaccessible.</p>"
        "<p><strong>Example 2:</strong> Document driving directions, building access procedures, and equipment "
        "locations for your alternate site, and ensure all key personnel have building access credentials.</p>"
    ),

    "cp-7-3": (
        "<p>This enhancement addresses priority of service agreements with your alternate processing site provider — "
        "ensuring you get priority access when multiple customers need the facility simultaneously.</p>"
        "<p><strong>Example 1:</strong> Include <em>priority of service</em> clauses in your contract with your "
        "disaster recovery provider, guaranteeing that your organization gets first access during a regional event.</p>"
        "<p><strong>Example 2:</strong> For cloud services, choose a <em>Reserved Instance</em> or <em>Dedicated Host</em> "
        "model for your disaster recovery environment to ensure capacity is available when you need it.</p>"
    ),

    "cp-7-4": (
        "<p>This enhancement requires your alternate processing site to be ready to use immediately — not requiring "
        "hours or days of setup before operations can begin.</p>"
        "<p><strong>Example 1:</strong> Maintain a <em>hot standby</em> environment in your secondary Azure region "
        "with VMs pre-deployed (but deallocated) and data replicated, allowing activation within minutes.</p>"
        "<p><strong>Example 2:</strong> Pre-install and configure networking equipment, servers, and workstations at "
        "your physical alternate site so staff can walk in and begin working immediately.</p>"
    ),

    "cp-7-5": (
        "<p>This enhancement was incorporated into CP-7. It required your alternate processing site to have equivalent "
        "security controls as your primary site.</p>"
        "<p><strong>Example 1:</strong> Apply the same <em>STIG baselines</em> and security group policies to systems "
        "at your alternate site as you do at your primary site, and include them in your regular SCAP scans.</p>"
        "<p><strong>Example 2:</strong> Ensure your backup <em>Azure subscription</em> has the same security "
        "configurations — network security groups, Defender for Cloud settings, and access controls — as production.</p>"
    ),

    "cp-7-6": (
        "<p>This enhancement requires planning for the possibility that you cannot return to your primary site — "
        "your alternate site may need to become your permanent home.</p>"
        "<p><strong>Example 1:</strong> Include procedures in your contingency plan for transitioning your alternate "
        "site to become the new primary site, including updating DNS records, VPN configurations, and vendor contacts.</p>"
        "<p><strong>Example 2:</strong> Ensure your <em>disaster recovery contract</em> allows for extended-term use "
        "and can be converted to a permanent hosting arrangement if your primary facility is permanently lost.</p>"
    ),

    "cp-8": (
        "<p>This control requires you to have backup telecommunications services — internet, phone, and data "
        "connections — so you can keep communicating if your primary connections fail.</p>"
        "<p><strong>Example 1:</strong> Contract with a second <em>ISP</em> using a different last-mile technology "
        "(e.g., fiber primary, LTE/5G backup) to ensure internet connectivity if your primary connection goes down.</p>"
        "<p><strong>Example 2:</strong> Set up <em>Microsoft Teams Phone</em> or another cloud-based phone system "
        "as a backup to your on-premises PBX so employees can make and receive calls from any internet connection.</p>"
    ),

    "cp-8-1": (
        "<p>This enhancement requires priority of service provisions in your telecommunications contracts — during "
        "a widespread outage, your organization should get prioritized restoration.</p>"
        "<p><strong>Example 1:</strong> Enroll in the <em>Telecommunications Service Priority (TSP)</em> program to "
        "get priority restoration of your critical telecommunications circuits during a national emergency.</p>"
        "<p><strong>Example 2:</strong> Negotiate <em>SLA terms</em> with your ISP that include priority restoration "
        "and dedicated support contacts during outages affecting multiple customers.</p>"
    ),

    "cp-8-2": (
        "<p>This enhancement requires you to eliminate single points of failure in your telecommunications — one "
        "cut cable should not take down all your communications.</p>"
        "<p><strong>Example 1:</strong> Ensure your primary and backup internet connections enter your building "
        "through <em>different physical paths</em> (e.g., different conduits, different street sides) to avoid "
        "a single cable cut affecting both.</p>"
        "<p><strong>Example 2:</strong> Use <em>SD-WAN</em> technology to automatically fail over between multiple "
        "internet connections (fiber, cable, LTE) without manual intervention or service interruption.</p>"
    ),

    "cp-8-3": (
        "<p>This enhancement requires your primary and alternate telecommunications providers to be different "
        "companies — or at least use different infrastructure — to avoid a single provider failure taking down both.</p>"
        "<p><strong>Example 1:</strong> Use two different ISPs (e.g., <em>AT&T</em> fiber and <em>Comcast</em> cable) "
        "rather than two circuits from the same provider, which might share the same backbone infrastructure.</p>"
        "<p><strong>Example 2:</strong> For your alternate site, contract with a local ISP that uses completely "
        "different backbone infrastructure than your primary site's provider.</p>"
    ),

    "cp-8-4": (
        "<p>This enhancement requires your telecommunications provider to have their own contingency plan — "
        "their ability to recover affects your ability to recover.</p>"
        "<p><strong>Example 1:</strong> Request your ISP's <em>business continuity plan</em> and review it to "
        "understand their recovery capabilities, redundancy, and expected restoration times during a major outage.</p>"
        "<p><strong>Example 2:</strong> Include provider contingency plan review as a criterion in your "
        "<em>vendor risk assessment</em> process, and re-evaluate annually during contract renewals.</p>"
    ),

    "cp-8-5": (
        "<p>This enhancement requires you to periodically test your alternate telecommunications services to "
        "ensure they work when needed.</p>"
        "<p><strong>Example 1:</strong> Quarterly, failover your internet traffic to your <em>backup ISP</em> for "
        "a few hours during a maintenance window and verify all critical applications remain accessible.</p>"
        "<p><strong>Example 2:</strong> Test your <em>LTE/5G backup</em> connection monthly by disabling the primary "
        "link and verifying that VPN, email, and critical web applications function over the backup connection.</p>"
    ),

    "cp-9": (
        "<p>System backup means regularly copying your data, configurations, and system images so you can restore "
        "them after a failure. Without good backups, a ransomware attack or hardware failure could be fatal to your "
        "business.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Veeam Backup & Replication</em> to perform daily incremental "
        "backups and weekly full backups of all critical servers, storing copies both locally and in offsite cloud "
        "storage.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure Backup</em> to protect your cloud VMs, SQL databases, and file "
        "shares with automated backup schedules and retention policies that keep daily backups for 30 days and "
        "monthly backups for one year.</p>"
    ),

    "cp-9-1": (
        "<p>This enhancement requires you to test your backups to verify they can be successfully restored — "
        "a backup you have never tested is a backup you cannot trust.</p>"
        "<p><strong>Example 1:</strong> Use <em>Veeam SureBackup</em> to automatically boot backed-up VMs in an "
        "isolated environment nightly and run application health checks to verify backup integrity.</p>"
        "<p><strong>Example 2:</strong> Conduct quarterly <em>test restores</em> where you pick a random server "
        "backup and restore it to a test environment, verifying the data is complete and applications function.</p>"
    ),

    "cp-9-2": (
        "<p>This enhancement requires you to test restoration using a sample of your backups — verifying that a "
        "representative set of your backup data can be successfully recovered.</p>"
        "<p><strong>Example 1:</strong> Each quarter, select three random backup sets from different systems and "
        "perform a <em>test restoration</em> to a lab environment, documenting the results and any issues found.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure Backup</em> restore verification to periodically restore "
        "random files and database tables from different backup dates and verify data integrity.</p>"
    ),

    "cp-9-3": (
        "<p>This enhancement requires you to store backups of critical information at a separate location from the "
        "primary system — so a single event cannot destroy both your live data and your backups.</p>"
        "<p><strong>Example 1:</strong> Replicate your most critical backups to a <em>different Azure region</em> "
        "or <em>AWS region</em> using backup copy jobs that run automatically after each primary backup completes.</p>"
        "<p><strong>Example 2:</strong> Store encrypted backup copies of your most critical databases at a secure "
        "offsite facility, physically separated from your primary data center by at least 100 miles.</p>"
    ),

    "cp-9-4": (
        "<p>This enhancement requires you to protect backups from unauthorized modification — attackers increasingly "
        "target backups (especially during ransomware attacks) to prevent recovery.</p>"
        "<p><strong>Example 1:</strong> Enable <em>immutable storage</em> on your Azure Blob backup containers or "
        "use <em>Veeam Hardened Repository</em> on Linux to prevent anyone from modifying or deleting backups.</p>"
        "<p><strong>Example 2:</strong> Store backup copies on <em>write-once media</em> or use S3 Object Lock with "
        "compliance mode to ensure backups cannot be altered even by administrators.</p>"
    ),

    "cp-9-5": (
        "<p>This enhancement requires automated transfer of backups to an alternate storage site — not relying on "
        "someone to manually copy or transport backup media.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Veeam Backup Copy</em> jobs to automatically replicate completed "
        "backups to your secondary data center or cloud storage repository over an encrypted WAN link.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure Backup</em> geo-redundant storage (GRS) which automatically "
        "replicates backup data to a paired Azure region without any manual intervention.</p>"
    ),

    "cp-9-6": (
        "<p>This enhancement provides redundancy through a secondary system that can take over if the primary fails — "
        "going beyond traditional backup and restore to real-time redundancy.</p>"
        "<p><strong>Example 1:</strong> Deploy a <em>SQL Server Always On Availability Group</em> with a synchronous "
        "secondary replica that can take over the database workload within seconds of a primary failure.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure Traffic Manager</em> or <em>AWS Route 53</em> health checks "
        "to automatically redirect traffic to a secondary application instance if the primary becomes unavailable.</p>"
    ),

    "cp-9-7": (
        "<p>This enhancement requires dual authorization before backups can be deleted or destroyed — preventing a "
        "single rogue or compromised administrator from wiping out your recovery capability.</p>"
        "<p><strong>Example 1:</strong> Configure your <em>Veeam</em> backup repository so that deleting backup files "
        "requires approval from both the backup administrator and the security officer.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure resource locks</em> on your backup storage accounts that "
        "require two administrators to approve removal, preventing accidental or malicious deletion.</p>"
    ),

    "cp-9-8": (
        "<p>This enhancement requires backups to be cryptographically protected — encrypted both at rest and in "
        "transit to prevent unauthorized access to backup data.</p>"
        "<p><strong>Example 1:</strong> Enable <em>AES-256 encryption</em> on all <em>Veeam</em> backup jobs so that "
        "backup files are encrypted at rest and cannot be read without the encryption key.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Azure Backup</em> to use customer-managed keys in <em>Azure Key "
        "Vault</em> for encrypting backup data, giving you full control over the encryption keys.</p>"
    ),

    "cp-10": (
        "<p>System recovery and reconstitution means getting your system back to a fully operational, secure state "
        "after a disruption. This goes beyond just restoring data — you need to verify the system is clean and "
        "properly configured.</p>"
        "<p><strong>Example 1:</strong> Document a step-by-step <em>system recovery runbook</em> that covers restoring "
        "from backup, applying current patches, verifying security configurations, and running a STIG compliance scan "
        "before returning the system to production.</p>"
        "<p><strong>Example 2:</strong> After recovering from a ransomware incident, rebuild affected systems from "
        "clean images rather than just restoring files, and run <em>Microsoft Defender</em> full scans before "
        "reconnecting to the network.</p>"
    ),

    "cp-10-1": (
        "<p>This enhancement was incorporated into CP-4. It previously required contingency plan testing as part "
        "of system recovery and reconstitution.</p>"
        "<p><strong>Example 1:</strong> Include system recovery verification steps in your annual <em>contingency "
        "plan test</em> — actually restore a server and validate it works, not just review procedures on paper.</p>"
        "<p><strong>Example 2:</strong> After each contingency plan test, document recovery times achieved and compare "
        "them against your <em>RTOs</em> to identify areas where recovery procedures need improvement.</p>"
    ),

    "cp-10-2": (
        "<p>This enhancement requires the ability to recover individual transactions — not just full system restores — "
        "for systems that process ongoing transactions.</p>"
        "<p><strong>Example 1:</strong> Enable <em>SQL Server transaction log backups</em> every 15 minutes so you "
        "can perform point-in-time recovery of your database to any moment, not just the last full backup.</p>"
        "<p><strong>Example 2:</strong> Configure your <em>Azure SQL Database</em> with automated point-in-time "
        "restore capability, allowing recovery to any point within the retention period (up to 35 days).</p>"
    ),

    "cp-10-3": (
        "<p>This enhancement was incorporated into SI-13. It previously addressed implementing compensating security "
        "controls when primary controls are unavailable during recovery.</p>"
        "<p><strong>Example 1:</strong> Document alternative security measures to use during recovery — for example, "
        "if your SIEM is down, have staff manually review firewall logs until monitoring is restored.</p>"
        "<p><strong>Example 2:</strong> If your primary MFA system is unavailable during recovery, define approved "
        "compensating controls like temporary IP restrictions and enhanced password requirements.</p>"
    ),

    "cp-10-4": (
        "<p>This enhancement requires you to restore system functionality within a defined time period — your "
        "recovery must meet your documented Recovery Time Objectives.</p>"
        "<p><strong>Example 1:</strong> Define and document RTOs in your contingency plan — for example, <em>Active "
        "Directory</em> within 2 hours, email within 4 hours, ERP within 8 hours — and test to verify you can "
        "meet them.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Azure Site Recovery</em> with recovery plans that automate "
        "the startup sequence and have been tested to complete within your defined RTO targets.</p>"
    ),

    "cp-10-5": (
        "<p>This enhancement requires automated failover capability — the system should automatically switch to "
        "a backup without manual intervention when a failure is detected.</p>"
        "<p><strong>Example 1:</strong> Deploy applications behind <em>Azure Front Door</em> or <em>AWS Global "
        "Accelerator</em> with health probes that automatically route traffic away from failed endpoints.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Windows Failover Clustering</em> for critical services so "
        "that if one node fails, the service automatically restarts on a healthy cluster node.</p>"
    ),

    "cp-10-6": (
        "<p>This enhancement requires protection of system components that are essential for recovery — if your "
        "recovery tools themselves are compromised or destroyed, you cannot recover.</p>"
        "<p><strong>Example 1:</strong> Store your <em>recovery tools</em> (restore software, OS installation media, "
        "configuration scripts) in a secure, offline location separate from production systems.</p>"
        "<p><strong>Example 2:</strong> Maintain offline copies of your <em>Ansible playbooks</em> or <em>Terraform "
        "scripts</em> in a secure vault so you can rebuild infrastructure even if your Git repository is compromised.</p>"
    ),

    "cp-11": (
        "<p>This control requires the ability to use alternative communications protocols when primary methods "
        "are unavailable or compromised — having a backup way to communicate.</p>"
        "<p><strong>Example 1:</strong> Establish <em>Signal</em> or <em>satellite phone</em> as a backup "
        "communication channel for key personnel if your primary email and Teams systems are unavailable.</p>"
        "<p><strong>Example 2:</strong> Pre-configure <em>out-of-band management</em> interfaces (like iDRAC or "
        "iLO) on critical servers so you can manage them over a separate network if the primary network is down.</p>"
    ),

    "cp-12": (
        "<p>Safe mode means your system can continue operating in a degraded but secure state when full functionality "
        "is not available — maintaining security even when not everything is working.</p>"
        "<p><strong>Example 1:</strong> Configure your <em>firewall</em> to fail closed (block all traffic) rather "
        "than fail open if it experiences a critical error, preventing unsecured traffic during the outage.</p>"
        "<p><strong>Example 2:</strong> Design your web application to display a <em>maintenance page</em> and "
        "reject all user sessions gracefully if the authentication backend becomes unavailable, rather than "
        "bypassing authentication.</p>"
    ),

    "cp-13": (
        "<p>This control requires alternative security mechanisms that can be activated when primary security controls "
        "fail or are unavailable — backup plans for your security tools.</p>"
        "<p><strong>Example 1:</strong> If your primary <em>SIEM</em> goes down, have a documented procedure to "
        "enable local logging on all devices and manually review logs until the SIEM is restored.</p>"
        "<p><strong>Example 2:</strong> Maintain a <em>backup VPN solution</em> (such as WireGuard alongside your "
        "primary Cisco AnyConnect) that can be activated if your primary VPN infrastructure fails.</p>"
    ),

    # =========================================================================
    # IA — Identification and Authentication (74 controls)
    # =========================================================================

    "ia-1": (
        "<p>This control asks you to create and share written rules for how your organization identifies and "
        "authenticates users — how people prove who they are before accessing your systems.</p>"
        "<p><strong>Example 1:</strong> Write an <em>Identification and Authentication Policy</em> that specifies "
        "password requirements, MFA mandates, account naming conventions, and how new accounts are provisioned.</p>"
        "<p><strong>Example 2:</strong> Document <em>authentication procedures</em> in your IT wiki that explain "
        "how users enroll in MFA, reset passwords, and request access to new systems.</p>"
    ),

    "ia-2": (
        "<p>Every person who uses your systems must have a unique account that identifies them, and they must prove "
        "their identity before being granted access. No shared accounts for individual work.</p>"
        "<p><strong>Example 1:</strong> Assign every employee a unique <em>Active Directory</em> account with the "
        "naming convention first.last@company.com, and disable shared or generic accounts like \"admin\" or "
        "\"helpdesk.\"</p>"
        "<p><strong>Example 2:</strong> Require all users to authenticate with their unique credentials through "
        "<em>Azure AD (Entra ID)</em> before accessing any company application, cloud service, or VPN connection.</p>"
    ),

    "ia-2-1": (
        "<p>This enhancement requires multi-factor authentication (MFA) for privileged accounts — admin accounts "
        "must use more than just a password to log in.</p>"
        "<p><strong>Example 1:</strong> Enable <em>Azure AD Conditional Access</em> policies that require MFA "
        "(Microsoft Authenticator app) for all Global Admin, Security Admin, and other privileged roles.</p>"
        "<p><strong>Example 2:</strong> Configure your <em>CyberArk</em> or <em>Azure PIM</em> to require MFA "
        "every time an administrator activates a privileged role, even from trusted network locations.</p>"
    ),

    "ia-2-2": (
        "<p>This enhancement requires multi-factor authentication for non-privileged accounts too — regular users "
        "also need MFA, not just administrators.</p>"
        "<p><strong>Example 1:</strong> Enable <em>Azure AD Security Defaults</em> or Conditional Access to require "
        "MFA for all users when accessing email, SharePoint, Teams, and other Microsoft 365 applications.</p>"
        "<p><strong>Example 2:</strong> Require all VPN users to authenticate with their password plus a "
        "<em>hardware token</em> (YubiKey) or authenticator app before establishing a remote connection.</p>"
    ),

    "ia-2-3": (
        "<p>This enhancement requires MFA for local (console) access to privileged accounts — not just remote access "
        "but physically sitting at the machine.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Windows Hello for Business</em> with PIN plus biometric to "
        "require multi-factor authentication even for local administrator logins at the console.</p>"
        "<p><strong>Example 2:</strong> For Linux servers, configure <em>PAM (Pluggable Authentication Modules)</em> "
        "to require a TOTP code from Google Authenticator in addition to the password for local root access.</p>"
    ),

    "ia-2-4": (
        "<p>This enhancement requires MFA for local access to non-privileged accounts — standard users logging in "
        "locally also need multi-factor authentication.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>Windows Hello for Business</em> across all workstations so that "
        "even standard users must authenticate with PIN plus facial recognition or fingerprint at the keyboard.</p>"
        "<p><strong>Example 2:</strong> Require <em>smart card</em> (CAC/PIV) authentication for all users logging "
        "in to workstations connected to your organization's domain.</p>"
    ),

    "ia-2-5": (
        "<p>This enhancement requires individual authentication when using a shared or group account — even if an "
        "account is shared, each user must first prove their individual identity.</p>"
        "<p><strong>Example 1:</strong> Require administrators to log in with their personal <em>Active Directory</em> "
        "account before accessing a shared administrative account through <em>CyberArk</em> session manager.</p>"
        "<p><strong>Example 2:</strong> For shared service accounts used in applications, implement <em>just-in-time "
        "access</em> through Azure PIM where each person requesting access is individually authenticated and logged.</p>"
    ),

    "ia-2-6": (
        "<p>This enhancement requires MFA using a separate physical device — the authentication factor must come from "
        "a device that is different from the system being accessed.</p>"
        "<p><strong>Example 1:</strong> Require users accessing their laptop to authenticate with a <em>YubiKey</em> "
        "hardware token or a code from their <em>mobile phone authenticator app</em> — a separate device.</p>"
        "<p><strong>Example 2:</strong> For VPN access from a laptop, require an approval push notification on the "
        "user's enrolled <em>Microsoft Authenticator</em> smartphone — ensuring a second device is involved.</p>"
    ),

    "ia-2-7": (
        "<p>This enhancement was incorporated into IA-2(6). It previously specifically addressed MFA via separate "
        "device for non-privileged network access.</p>"
        "<p><strong>Example 1:</strong> Apply the same <em>separate device MFA requirement</em> to non-privileged "
        "accounts — standard users must also use a phone or hardware token, not just software on the same computer.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Conditional Access</em> to require phishing-resistant MFA "
        "(FIDO2 key or Windows Hello) for all users, regardless of privilege level.</p>"
    ),

    "ia-2-8": (
        "<p>This enhancement requires replay-resistant authentication mechanisms — an attacker who captures your "
        "authentication traffic should not be able to replay it to gain access.</p>"
        "<p><strong>Example 1:</strong> Use <em>FIDO2 security keys</em> (like YubiKeys) which provide "
        "cryptographic challenge-response authentication that is inherently replay-resistant.</p>"
        "<p><strong>Example 2:</strong> Implement <em>Kerberos</em> authentication (used by Active Directory) which "
        "includes timestamps in tickets, making captured authentication data useless after a short time window.</p>"
    ),

    "ia-2-9": (
        "<p>This enhancement was incorporated into IA-2(8). It previously addressed replay-resistant authentication "
        "specifically for non-privileged network access.</p>"
        "<p><strong>Example 1:</strong> Ensure all network authentication — privileged and non-privileged — uses "
        "<em>Kerberos</em> or <em>certificate-based authentication</em> rather than NTLM, which is more vulnerable "
        "to replay attacks.</p>"
        "<p><strong>Example 2:</strong> Disable <em>NTLM authentication</em> via Group Policy where possible and "
        "force all clients to use Kerberos for domain authentication.</p>"
    ),

    "ia-2-10": (
        "<p>Single sign-on (SSO) allows users to authenticate once and access multiple systems without re-entering "
        "credentials — improving both security and user experience.</p>"
        "<p><strong>Example 1:</strong> Implement <em>Azure AD SSO</em> so employees log in once to their computer "
        "and get seamless access to Microsoft 365, Salesforce, ServiceNow, and other SAML/OIDC-integrated apps.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Okta</em> or <em>Ping Identity</em> as your SSO provider, "
        "connecting all your web applications through federated authentication to reduce password fatigue.</p>"
    ),

    "ia-2-11": (
        "<p>This enhancement was incorporated into IA-2(6). It previously addressed MFA via separate device "
        "specifically for remote access scenarios.</p>"
        "<p><strong>Example 1:</strong> Require all <em>VPN users</em> to authenticate with a hardware token or "
        "phone-based authenticator in addition to their password before establishing remote connections.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Conditional Access</em> policies to always require MFA for "
        "any sign-in from outside your trusted network locations, regardless of the device used.</p>"
    ),

    "ia-2-12": (
        "<p>This enhancement requires your systems to accept Personal Identity Verification (PIV) credentials — "
        "the smart card standard used by federal agencies (CAC for DoD).</p>"
        "<p><strong>Example 1:</strong> Configure <em>Active Directory</em> and your PKI infrastructure to accept "
        "<em>CAC/PIV smart card</em> authentication for all Windows logons and application access.</p>"
        "<p><strong>Example 2:</strong> Enable <em>PIV certificate-based authentication</em> in Azure AD (Entra ID) "
        "so users can authenticate to cloud applications using their government-issued smart card.</p>"
    ),

    "ia-2-13": (
        "<p>Out-of-band authentication uses a separate, independent communication channel to verify identity — "
        "like receiving a verification code via phone call or SMS on a different network than the one you are logging into.</p>"
        "<p><strong>Example 1:</strong> For high-risk transactions (like password resets for admin accounts), require "
        "a verification phone call to the user's registered <em>mobile number</em> before processing the request.</p>"
        "<p><strong>Example 2:</strong> Implement <em>Azure AD phone call verification</em> as an additional "
        "authentication factor for sensitive operations like adding new MFA methods or changing security settings.</p>"
    ),

    "ia-3": (
        "<p>This control requires your systems to identify and authenticate devices — not just people — before "
        "allowing them on the network. Your network should know and trust devices, not just users.</p>"
        "<p><strong>Example 1:</strong> Deploy <em>802.1X certificate-based authentication</em> on your network "
        "switches and wireless access points so that only devices with valid machine certificates can connect.</p>"
        "<p><strong>Example 2:</strong> Use <em>Intune device compliance</em> and <em>Conditional Access</em> to "
        "ensure only enrolled, managed devices can access company resources like email and SharePoint.</p>"
    ),

    "ia-3-1": (
        "<p>This enhancement requires cryptographic bidirectional authentication between devices — both the device "
        "and the network must prove their identity to each other.</p>"
        "<p><strong>Example 1:</strong> Use <em>mutual TLS (mTLS)</em> for server-to-server communication where "
        "both sides present certificates and verify each other's identity before exchanging data.</p>"
        "<p><strong>Example 2:</strong> Configure <em>802.1X with EAP-TLS</em> where both the client device and "
        "the RADIUS server authenticate each other using digital certificates.</p>"
    ),

    "ia-3-2": (
        "<p>This enhancement was incorporated into IA-3(1). It previously addressed cryptographic bidirectional "
        "authentication specifically for network communications.</p>"
        "<p><strong>Example 1:</strong> Implement <em>IPsec</em> with mutual certificate authentication between "
        "site-to-site VPN endpoints so both sides cryptographically verify each other before establishing the tunnel.</p>"
        "<p><strong>Example 2:</strong> Configure <em>TLS mutual authentication</em> on your API gateways so that "
        "client services must present valid certificates to access backend APIs.</p>"
    ),

    "ia-3-3": (
        "<p>This enhancement requires dynamic allocation of network addresses to be tied to device identity — "
        "tracking which device got which IP address from DHCP.</p>"
        "<p><strong>Example 1:</strong> Configure your <em>DHCP server</em> to log MAC address-to-IP address "
        "assignments and integrate with your <em>NAC solution</em> so allocated addresses are traceable to "
        "authenticated devices.</p>"
        "<p><strong>Example 2:</strong> Use <em>DHCP reservations</em> for critical servers and network devices so "
        "their IP addresses are always mapped to their known MAC addresses in your asset inventory.</p>"
    ),

    "ia-3-4": (
        "<p>This enhancement requires device attestation — the ability for a device to cryptographically prove it is "
        "in a known-good state, not just that it has valid credentials.</p>"
        "<p><strong>Example 1:</strong> Use <em>Windows Attestation</em> with a Trusted Platform Module (TPM) to "
        "verify that a device's boot process has not been tampered with before granting network access.</p>"
        "<p><strong>Example 2:</strong> Implement <em>Intune device compliance</em> policies that check TPM "
        "attestation, Secure Boot status, and BitLocker encryption before allowing access to sensitive resources.</p>"
    ),

    "ia-4": (
        "<p>Identifier management means having a formal process for assigning, managing, and retiring user IDs, "
        "device IDs, and other identifiers. Every identifier should be unique and traceable to a real person or device.</p>"
        "<p><strong>Example 1:</strong> Establish naming conventions in <em>Active Directory</em> (e.g., "
        "first.last for users, SVC-appname for service accounts) and prohibit reuse of identifiers for at least "
        "two years after deactivation.</p>"
        "<p><strong>Example 2:</strong> Integrate your <em>HR system</em> with Azure AD using automated provisioning "
        "(SCIM) so that user identifiers are created when employees are hired and disabled when they depart.</p>"
    ),

    "ia-4-1": (
        "<p>This enhancement prohibits using system account identifiers as public identifiers — your usernames should "
        "not be easily guessable or publicly discoverable.</p>"
        "<p><strong>Example 1:</strong> Do not use employee email addresses as their primary <em>Active Directory</em> "
        "login username if those emails are publicly listed on your company website.</p>"
        "<p><strong>Example 2:</strong> Use <em>employee ID numbers</em> or non-obvious identifiers for system "
        "accounts rather than names or email addresses that could be harvested from LinkedIn or your website.</p>"
    ),

    "ia-4-2": (
        "<p>This enhancement requires supervisor authorization before new identifiers are issued — someone in "
        "authority must approve new account creation.</p>"
        "<p><strong>Example 1:</strong> Configure your <em>ServiceNow</em> new account request workflow to require "
        "the employee's direct supervisor to approve the request before the IT help desk creates the account.</p>"
        "<p><strong>Example 2:</strong> In your <em>Active Directory</em> account creation procedure, require a "
        "signed supervisor approval form that specifies the access level needed before an account is provisioned.</p>"
    ),

    "ia-4-3": (
        "<p>This enhancement requires multiple forms of certification to verify a person's identity before issuing "
        "them system credentials — more rigorous identity proofing.</p>"
        "<p><strong>Example 1:</strong> Require new employees to present <em>two forms of government-issued ID</em> "
        "(e.g., passport and driver's license) during in-person onboarding before issuing network credentials.</p>"
        "<p><strong>Example 2:</strong> For remote onboarding, use a <em>video identity verification</em> service "
        "that compares the person to their government ID photo and validates the ID document's authenticity.</p>"
    ),

    "ia-4-4": (
        "<p>This enhancement requires user identifiers to include status information — such as whether the user is "
        "a contractor, temporary employee, or has other relevant attributes.</p>"
        "<p><strong>Example 1:</strong> Include employment type in <em>Active Directory</em> attributes (e.g., "
        "employeeType = \"Contractor\" or \"FTE\") and use these attributes in Conditional Access policies.</p>"
        "<p><strong>Example 2:</strong> Use a naming convention that includes status indicators — for example, "
        "prefix contractor accounts with \"CTR-\" in your <em>Azure AD</em> to make their status immediately visible.</p>"
    ),

    "ia-4-5": (
        "<p>This enhancement requires dynamic management of identifiers — automatically adjusting or revoking "
        "identifiers based on changing conditions like role changes or security events.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Azure AD Identity Governance</em> with access reviews that "
        "automatically remove access when users change roles and their old access is no longer appropriate.</p>"
        "<p><strong>Example 2:</strong> Implement automated <em>SCIM provisioning</em> between your HR system and "
        "identity provider so that job role changes automatically trigger access adjustments within 24 hours.</p>"
    ),

    "ia-4-6": (
        "<p>This enhancement requires coordination of identifier management across organizations — when you work "
        "with partners or agencies, identifiers need to be managed consistently.</p>"
        "<p><strong>Example 1:</strong> Use <em>Azure AD B2B collaboration</em> to manage external partner "
        "identities in your directory, maintaining a clear record of which external organization each user belongs to.</p>"
        "<p><strong>Example 2:</strong> Establish a <em>federation trust</em> with partner organizations using SAML "
        "so their users can authenticate with their home organization's credentials while you maintain control "
        "over authorization.</p>"
    ),

    "ia-4-7": (
        "<p>This enhancement requires in-person registration when issuing identifiers — the person must physically "
        "appear before a registration authority to receive their credentials.</p>"
        "<p><strong>Example 1:</strong> Require all new employees to pick up their <em>CAC/smart card</em> and "
        "initial network credentials in person at the security office after presenting government-issued photo ID.</p>"
        "<p><strong>Example 2:</strong> For high-security systems, require users to visit the <em>IT help desk</em> "
        "in person with photo ID to receive their initial password and MFA enrollment token.</p>"
    ),

    "ia-4-8": (
        "<p>This enhancement requires the use of pairwise pseudonymous identifiers — unique identifiers that are "
        "different for each relationship, preventing tracking across services.</p>"
        "<p><strong>Example 1:</strong> When integrating with external services, use <em>OIDC pairwise subject "
        "identifiers</em> so that each service receives a different identifier for the same user, preventing "
        "cross-service tracking.</p>"
        "<p><strong>Example 2:</strong> Configure your <em>identity provider</em> to issue pairwise pseudonymous IDs "
        "for privacy-sensitive applications, ensuring user identifiers cannot be correlated between applications.</p>"
    ),

    "ia-4-9": (
        "<p>This enhancement requires maintaining and protecting the attributes associated with identifiers — "
        "keeping identity information accurate, current, and secure.</p>"
        "<p><strong>Example 1:</strong> Restrict who can modify <em>Active Directory</em> user attributes (like "
        "department, title, and manager) to HR administrators and designated identity management staff.</p>"
        "<p><strong>Example 2:</strong> Enable <em>audit logging</em> on all identity attribute changes in Azure AD "
        "so you can track who modified user profile information and when.</p>"
    ),

    "ia-5": (
        "<p>Authenticator management covers how you handle passwords, tokens, certificates, and other secrets used "
        "to prove identity. You need processes for issuing, protecting, revoking, and changing authenticators.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Azure AD password policies</em> to require 14+ character "
        "passwords, prohibit common passwords (using the banned password list), and enforce MFA registration "
        "for all users within their first day.</p>"
        "<p><strong>Example 2:</strong> Establish procedures for <em>revoking certificates</em> and resetting "
        "passwords within 24 hours when an employee is terminated, using your HR-triggered offboarding workflow.</p>"
    ),

    "ia-5-1": (
        "<p>This enhancement specifies requirements for password-based authentication — minimum length, complexity, "
        "and management requirements for passwords.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Active Directory</em> password policy via GPO to require "
        "minimum 14 characters, check against the <em>Azure AD banned password list</em>, and enforce password "
        "history of 24 previous passwords.</p>"
        "<p><strong>Example 2:</strong> Deploy <em>Azure AD Password Protection</em> which blocks users from setting "
        "passwords containing common words, company names, or patterns found in known breach databases.</p>"
    ),

    "ia-5-2": (
        "<p>This enhancement addresses public key-based authentication — using certificates and PKI rather than "
        "passwords for stronger authentication.</p>"
        "<p><strong>Example 1:</strong> Deploy an internal <em>Active Directory Certificate Services (AD CS)</em> "
        "PKI and issue user certificates for smart card (CAC/PIV) authentication to workstations and VPN.</p>"
        "<p><strong>Example 2:</strong> Configure <em>Azure AD certificate-based authentication</em> (CBA) so users "
        "can authenticate to cloud applications using their X.509 certificates stored on smart cards or devices.</p>"
    ),

    "ia-5-3": (
        "<p>This enhancement requires in-person or trusted third-party registration when issuing authenticators — "
        "verifying identity before handing out credentials.</p>"
        "<p><strong>Example 1:</strong> Require new employees to register their <em>MFA device</em> (phone or "
        "hardware token) in person at the IT service desk after showing their employee badge and photo ID.</p>"
        "<p><strong>Example 2:</strong> For remote employees, use a <em>trusted HR representative</em> at the "
        "employee's location to verify identity via video call before the IT team activates their credentials.</p>"
    ),

    "ia-5-4": (
        "<p>This enhancement requires automated tools to check password strength — the system should reject weak "
        "passwords automatically, not rely on users to choose strong ones.</p>"
        "<p><strong>Example 1:</strong> Enable <em>Azure AD Password Protection</em> to automatically block passwords "
        "that contain dictionary words, repeated characters, or patterns found in breach databases.</p>"
        "<p><strong>Example 2:</strong> Configure your <em>Linux PAM</em> password quality module (pam_pwquality) "
        "to enforce minimum length, character diversity, and dictionary word checks at password change time.</p>"
    ),

    "ia-5-5": (
        "<p>This enhancement requires changing default authenticators before or during system installation — default "
        "passwords on devices and software must be changed immediately.</p>"
        "<p><strong>Example 1:</strong> Before deploying any new <em>network device</em> (router, switch, firewall), "
        "change all default passwords and community strings as part of your standard build checklist.</p>"
        "<p><strong>Example 2:</strong> Include a step in your <em>server deployment runbook</em> to change default "
        "administrator passwords and disable default accounts before connecting the system to the network.</p>"
    ),

    "ia-5-6": (
        "<p>This enhancement requires protecting authenticators commensurate with the sensitivity of the information "
        "they protect — high-value secrets need high-value protection.</p>"
        "<p><strong>Example 1:</strong> Store service account passwords and API keys in a <em>secrets vault</em> like "
        "<em>Azure Key Vault</em>, <em>HashiCorp Vault</em>, or <em>CyberArk</em> rather than in scripts or "
        "config files.</p>"
        "<p><strong>Example 2:</strong> Require <em>hardware security modules (HSMs)</em> or hardware tokens for "
        "authenticators protecting your most sensitive systems (domain admin accounts, PKI root keys).</p>"
    ),

    "ia-5-7": (
        "<p>This enhancement prohibits embedding unencrypted static passwords or credentials in applications, "
        "scripts, or configuration files — a common and dangerous practice.</p>"
        "<p><strong>Example 1:</strong> Scan your code repositories with <em>GitLeaks</em> or <em>TruffleHog</em> "
        "to detect hardcoded passwords, API keys, or connection strings, and move them to <em>Azure Key Vault</em>.</p>"
        "<p><strong>Example 2:</strong> Replace hardcoded database passwords in application config files with "
        "<em>managed identity</em> authentication (Azure) or <em>IAM role-based</em> authentication (AWS) that "
        "requires no static credentials.</p>"
    ),

    "ia-5-8": (
        "<p>This enhancement addresses users who have accounts on multiple systems — ensuring they use different "
        "authenticators for different systems to limit the blast radius of a compromised credential.</p>"
        "<p><strong>Example 1:</strong> Require administrators to use <em>different passwords</em> for their "
        "standard user account, their admin account, and any cloud admin accounts — enforced through separate "
        "password policies.</p>"
        "<p><strong>Example 2:</strong> Use <em>CyberArk</em> or <em>Azure PIM</em> to manage privileged "
        "credentials separately from standard credentials, with automatic password rotation for admin accounts.</p>"
    ),

    "ia-5-9": (
        "<p>This enhancement addresses federated credential management — using identity federation to manage "
        "credentials across organizational boundaries.</p>"
        "<p><strong>Example 1:</strong> Implement <em>SAML federation</em> with partner organizations so their users "
        "authenticate with their home organization's credentials rather than you issuing and managing separate accounts.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure AD B2B</em> guest access to allow external collaborators to "
        "use their own organization's credentials, avoiding the need to manage external user passwords.</p>"
    ),

    "ia-5-10": (
        "<p>This enhancement requires dynamic credential binding — associating credentials with identity in real "
        "time rather than through static, pre-configured mappings.</p>"
        "<p><strong>Example 1:</strong> Use <em>FIDO2 security keys</em> with Azure AD that dynamically bind "
        "the cryptographic credential to the user's identity during registration, with no shared secrets.</p>"
        "<p><strong>Example 2:</strong> Implement <em>just-in-time certificate issuance</em> through your PKI "
        "where short-lived certificates are issued dynamically for each session rather than long-lived static certs.</p>"
    ),

    "ia-5-11": (
        "<p>This enhancement addresses hardware token-based authentication — using physical tokens like smart cards "
        "or USB security keys for authentication.</p>"
        "<p><strong>Example 1:</strong> Issue <em>YubiKey 5</em> hardware tokens to all employees and require them "
        "for MFA, supporting FIDO2, PIV smart card, and TOTP authentication methods.</p>"
        "<p><strong>Example 2:</strong> Deploy <em>CAC/PIV smart card readers</em> on all workstations and require "
        "certificate-based authentication via the physical card for Windows logon.</p>"
    ),

    "ia-5-12": (
        "<p>This enhancement specifies requirements for biometric authentication performance — biometrics must meet "
        "defined accuracy thresholds to be acceptable.</p>"
        "<p><strong>Example 1:</strong> If using <em>Windows Hello</em> facial recognition, verify that the cameras "
        "meet Microsoft's anti-spoofing requirements and the system achieves the false acceptance rates specified "
        "by your organization.</p>"
        "<p><strong>Example 2:</strong> For fingerprint readers, select devices that meet <em>FBI PIV standards</em> "
        "for false acceptance rate (FAR) and false rejection rate (FRR) to ensure reliable authentication.</p>"
    ),

    "ia-5-13": (
        "<p>This enhancement requires that cached authenticators expire after a defined period — you should not be "
        "able to log in with cached credentials indefinitely.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Group Policy</em> to limit the number of cached logons on "
        "Windows laptops to no more than 2 (or as your policy dictates) and require network re-authentication "
        "within 24 hours.</p>"
        "<p><strong>Example 2:</strong> Set <em>Azure AD token lifetime</em> policies to limit refresh token "
        "lifetimes so users must re-authenticate with MFA at least every 24 hours, even on trusted devices.</p>"
    ),

    "ia-5-14": (
        "<p>This enhancement requires managing the content of PKI trust stores — controlling which certificate "
        "authorities your systems trust.</p>"
        "<p><strong>Example 1:</strong> Use <em>Group Policy</em> to manage the Trusted Root Certificate Authorities "
        "store on all domain-joined machines, removing untrusted CAs and adding only your organization's approved CAs.</p>"
        "<p><strong>Example 2:</strong> Regularly audit the <em>certificate trust list</em> on your servers and "
        "devices, removing any root CAs that are not needed for your business operations to reduce attack surface.</p>"
    ),

    "ia-5-15": (
        "<p>This enhancement requires using GSA-approved products and services for identity verification — "
        "leveraging government-vetted solutions.</p>"
        "<p><strong>Example 1:</strong> Use a <em>GSA-approved identity proofing service</em> from the "
        "Trust Services List for verifying the identity of remote users before issuing credentials.</p>"
        "<p><strong>Example 2:</strong> Select identity and credentialing services from the <em>GSA Approved Products "
        "List (APL)</em> for PIV/CAC card issuance and management.</p>"
    ),

    "ia-5-16": (
        "<p>This enhancement requires in-person or trusted external party involvement when issuing authenticators — "
        "someone trusted must physically verify the recipient's identity.</p>"
        "<p><strong>Example 1:</strong> Require new employees to receive their <em>initial password and MFA token</em> "
        "in person from the IT help desk after the HR department confirms their identity.</p>"
        "<p><strong>Example 2:</strong> For remote employees, use a <em>bonded courier service</em> to deliver "
        "hardware tokens and initial credentials, with signature verification upon delivery.</p>"
    ),

    "ia-5-17": (
        "<p>This enhancement requires presentation attack detection for biometric authenticators — the system must "
        "be able to detect spoofing attempts like using a photo or fake fingerprint.</p>"
        "<p><strong>Example 1:</strong> Use <em>Windows Hello Enhanced Sign-in Security</em> cameras with IR "
        "sensors that detect whether a live face is present rather than a photograph or mask.</p>"
        "<p><strong>Example 2:</strong> Select fingerprint readers with <em>liveness detection</em> that can "
        "distinguish between a real finger and a silicone replica or printed fingerprint.</p>"
    ),

    "ia-5-18": (
        "<p>This enhancement addresses the use of password managers — approved tools that help users create and "
        "store strong, unique passwords for each system.</p>"
        "<p><strong>Example 1:</strong> Deploy an enterprise <em>password manager</em> like <em>1Password Business</em> "
        "or <em>Keeper Enterprise</em> to all employees so they can generate and store unique, complex passwords "
        "for each application.</p>"
        "<p><strong>Example 2:</strong> Configure your approved password manager to enforce <em>master password "
        "requirements</em> (minimum 16 characters, MFA enabled) and prohibit users from using unapproved password "
        "storage methods like browser auto-save or sticky notes.</p>"
    ),

    "ia-6": (
        "<p>Authentication feedback means that when users enter their password, the system should not reveal the "
        "password on screen. This prevents shoulder surfing and screen capture attacks.</p>"
        "<p><strong>Example 1:</strong> Ensure all login screens display <em>dots or asterisks</em> instead of "
        "the actual password characters as users type, including custom web applications and admin portals.</p>"
        "<p><strong>Example 2:</strong> Configure your <em>Linux SSH</em> login and <em>sudo</em> prompts to not "
        "echo any characters (not even asterisks) when passwords are entered at the command line.</p>"
    ),

    "ia-7": (
        "<p>This control requires that cryptographic modules used for authentication meet FIPS 140 requirements — "
        "the encryption protecting your login process must meet federal standards.</p>"
        "<p><strong>Example 1:</strong> Ensure your <em>VPN concentrators</em> (Cisco, Palo Alto) use FIPS 140-2 "
        "or 140-3 validated cryptographic modules for authenticating VPN connections.</p>"
        "<p><strong>Example 2:</strong> Verify that <em>Windows</em> is configured to use FIPS-compliant algorithms "
        "for authentication by enabling the \"System cryptography: Use FIPS compliant algorithms\" Group Policy setting.</p>"
    ),

    "ia-8": (
        "<p>This control addresses identifying and authenticating non-organizational users — people who are not your "
        "employees but need access to your systems, like contractors, partners, or the public.</p>"
        "<p><strong>Example 1:</strong> Use <em>Azure AD B2B</em> guest accounts to provide external partners "
        "with authenticated access to specific SharePoint sites and Teams channels without giving them full "
        "employee accounts.</p>"
        "<p><strong>Example 2:</strong> For public-facing applications, implement <em>Login.gov</em> or a "
        "commercial identity provider for customer authentication rather than building your own login system.</p>"
    ),

    "ia-8-1": (
        "<p>This enhancement requires your systems to accept PIV credentials from other federal agencies — enabling "
        "cross-agency authentication with government smart cards.</p>"
        "<p><strong>Example 1:</strong> Configure your <em>Active Directory</em> to trust the Federal PKI "
        "certificate chain so that employees from other agencies can log in with their PIV/CAC cards.</p>"
        "<p><strong>Example 2:</strong> Enable <em>cross-certificate trust</em> in your PKI infrastructure "
        "to accept certificates issued by other federal agencies' certificate authorities.</p>"
    ),

    "ia-8-2": (
        "<p>This enhancement requires accepting external authenticators that meet defined assurance levels — "
        "trusting credentials from vetted external identity providers.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Azure AD External Identities</em> to accept authentication "
        "from partner organizations' identity providers that meet NIST SP 800-63B AAL2 or higher.</p>"
        "<p><strong>Example 2:</strong> Accept <em>Login.gov</em> credentials from external users at the IAL2/AAL2 "
        "assurance level for accessing your citizen-facing applications.</p>"
    ),

    "ia-8-3": (
        "<p>This enhancement was incorporated into IA-8(2). It previously required using FICAM-approved products for "
        "identity and access management of non-organizational users.</p>"
        "<p><strong>Example 1:</strong> Select your <em>identity provider</em> and MFA solutions from the "
        "FICAM-approved products list to ensure they meet federal interoperability requirements.</p>"
        "<p><strong>Example 2:</strong> Use <em>Login.gov</em> — a FICAM-approved service — as the authentication "
        "front end for public-facing federal applications.</p>"
    ),

    "ia-8-4": (
        "<p>This enhancement requires using defined identity assurance profiles for authenticating non-organizational "
        "users — aligning with NIST SP 800-63 assurance levels.</p>"
        "<p><strong>Example 1:</strong> Define in your system security plan that external users must authenticate "
        "at <em>NIST SP 800-63B AAL2</em> (MFA required) for access to sensitive but unclassified data.</p>"
        "<p><strong>Example 2:</strong> Configure your <em>identity provider</em> to enforce different authentication "
        "requirements based on risk: AAL1 for public information, AAL2 for CUI, AAL3 for high-value assets.</p>"
    ),

    "ia-8-5": (
        "<p>This enhancement addresses acceptance of PIV-I (PIV-Interoperable) credentials — non-federal smart cards "
        "that meet PIV technical specifications.</p>"
        "<p><strong>Example 1:</strong> Configure your <em>Active Directory</em> to accept PIV-I credentials from "
        "defense contractors who have been issued PIV-I cards by their organizations.</p>"
        "<p><strong>Example 2:</strong> Add the <em>PIV-I issuing CAs</em> to your trust store so that contractor "
        "smart cards can be used for authentication alongside government-issued PIV/CAC cards.</p>"
    ),

    "ia-8-6": (
        "<p>This enhancement requires disassociability — the ability to authenticate external users without "
        "unnecessarily linking their activities across different interactions or systems.</p>"
        "<p><strong>Example 1:</strong> Use <em>pairwise pseudonymous identifiers</em> for external users so that "
        "their activity on one application cannot be correlated with their activity on another.</p>"
        "<p><strong>Example 2:</strong> Configure your <em>OIDC identity provider</em> to issue different subject "
        "identifiers to different relying parties for the same external user, preserving privacy.</p>"
    ),

    "ia-9": (
        "<p>This control requires services (not just people and devices) to identify and authenticate themselves — "
        "when one system talks to another, they must verify each other's identity.</p>"
        "<p><strong>Example 1:</strong> Use <em>mutual TLS (mTLS)</em> between microservices so that each service "
        "presents a certificate and verifies the other service's identity before exchanging data.</p>"
        "<p><strong>Example 2:</strong> Implement <em>OAuth 2.0 client credentials flow</em> for service-to-service "
        "authentication, where each service has unique client ID and secret stored in Azure Key Vault.</p>"
    ),

    "ia-9-1": (
        "<p>This enhancement was incorporated into IA-9. It previously addressed ensuring that service identity "
        "information is exchanged between services.</p>"
        "<p><strong>Example 1:</strong> Include service identity claims in <em>JWT tokens</em> exchanged between "
        "your API services so each service can verify the calling service's identity and permissions.</p>"
        "<p><strong>Example 2:</strong> Use a <em>service mesh</em> like Istio that automatically handles service "
        "identity and mutual TLS between all microservices in your environment.</p>"
    ),

    "ia-9-2": (
        "<p>This enhancement was incorporated into IA-9. It previously addressed transmission of service "
        "authentication decisions to downstream services.</p>"
        "<p><strong>Example 1:</strong> Use <em>token propagation</em> in your API gateway so that authentication "
        "decisions made at the gateway are passed downstream to backend services via signed tokens.</p>"
        "<p><strong>Example 2:</strong> Implement an <em>API gateway</em> (like Azure API Management) that "
        "authenticates the calling service and includes verified identity claims in headers forwarded to backend APIs.</p>"
    ),

    "ia-10": (
        "<p>Adaptive authentication means your system adjusts its authentication requirements based on risk — "
        "requiring stronger proof of identity in riskier situations.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Azure AD Conditional Access</em> with risk-based policies: "
        "low-risk sign-ins require MFA, medium-risk sign-ins require password change plus MFA, and high-risk "
        "sign-ins are blocked until an admin reviews.</p>"
        "<p><strong>Example 2:</strong> Use <em>Azure AD Identity Protection</em> to automatically detect risky "
        "sign-ins (impossible travel, anonymous IP, leaked credentials) and step up authentication requirements.</p>"
    ),

    "ia-11": (
        "<p>Re-authentication means requiring users to prove their identity again during a session — not just at "
        "initial login but periodically or before sensitive actions.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Azure AD Conditional Access</em> to require re-authentication "
        "with MFA every 4 hours for access to sensitive applications like financial systems or admin portals.</p>"
        "<p><strong>Example 2:</strong> Implement <em>step-up authentication</em> in your web application that "
        "requires users to re-enter their password or MFA code before performing high-risk actions like "
        "changing account settings or downloading bulk data.</p>"
    ),

    "ia-12": (
        "<p>Identity proofing is the process of verifying that a person is who they claim to be before issuing "
        "them an account. This happens before authentication — you need to confirm their real-world identity first.</p>"
        "<p><strong>Example 1:</strong> During onboarding, require new employees to present <em>government-issued "
        "photo ID</em> and complete an I-9 verification before HR authorizes IT to create their account.</p>"
        "<p><strong>Example 2:</strong> For remote identity proofing, use a <em>NIST SP 800-63A compliant service</em> "
        "that performs document verification, photo matching, and knowledge-based verification.</p>"
    ),

    "ia-12-1": (
        "<p>This enhancement requires supervisor authorization as part of the identity proofing process — a "
        "supervisor must confirm the person's identity and authorize their access.</p>"
        "<p><strong>Example 1:</strong> Include a supervisor signature line on your <em>System Access Request Form</em> "
        "confirming they have verified the individual's identity and authorize account creation.</p>"
        "<p><strong>Example 2:</strong> In your <em>ServiceNow</em> onboarding workflow, require the hiring "
        "manager to approve the identity proofing results before the account provisioning step can proceed.</p>"
    ),

    "ia-12-2": (
        "<p>This enhancement specifies requirements for the identity evidence used during proofing — what documents "
        "or credentials are acceptable for proving someone's identity.</p>"
        "<p><strong>Example 1:</strong> Define in your identity proofing policy that acceptable evidence includes "
        "a <em>valid U.S. passport</em>, <em>state driver's license</em>, or <em>military ID (CAC)</em> — "
        "following NIST SP 800-63A evidence strength guidelines.</p>"
        "<p><strong>Example 2:</strong> For remote proofing, require applicants to submit <em>high-resolution photos</em> "
        "of two forms of ID and a live selfie for automated comparison by an identity verification service.</p>"
    ),

    "ia-12-3": (
        "<p>This enhancement requires validation and verification of identity evidence — not just collecting "
        "documents but confirming they are genuine and belong to the person presenting them.</p>"
        "<p><strong>Example 1:</strong> Use an automated <em>identity verification service</em> (like ID.me or "
        "Jumio) that checks government ID documents for tampering and matches the photo against a live selfie.</p>"
        "<p><strong>Example 2:</strong> Train your HR staff to check government IDs for <em>security features</em> "
        "(holograms, watermarks, UV features) and verify the photo matches the person during in-person onboarding.</p>"
    ),

    "ia-12-4": (
        "<p>This enhancement requires in-person validation and verification of identity evidence — the person "
        "must physically appear before a trusted agent.</p>"
        "<p><strong>Example 1:</strong> Require all employees to complete <em>in-person identity verification</em> "
        "at your HR office during their first day, presenting original (not photocopied) government-issued IDs.</p>"
        "<p><strong>Example 2:</strong> For high-security positions, require the identity proofing to occur at a "
        "<em>HSPD-12 enrollment center</em> or authorized PIV card issuance facility.</p>"
    ),

    "ia-12-5": (
        "<p>This enhancement requires address confirmation as part of identity proofing — verifying that the person "
        "actually resides at the address they claim.</p>"
        "<p><strong>Example 1:</strong> Send an <em>enrollment confirmation code</em> via physical mail to the "
        "applicant's claimed address, requiring them to enter the code online to complete registration.</p>"
        "<p><strong>Example 2:</strong> Verify the applicant's address against <em>USPS address validation</em> "
        "databases and cross-reference with their submitted utility bills or bank statements.</p>"
    ),

    "ia-12-6": (
        "<p>This enhancement allows your organization to accept identity proofing performed by trusted external "
        "organizations — avoiding redundant proofing when someone has already been vetted.</p>"
        "<p><strong>Example 1:</strong> Accept <em>Login.gov IAL2</em> identity proofing for external users "
        "rather than conducting your own identity proofing process from scratch.</p>"
        "<p><strong>Example 2:</strong> Accept identity proofing results from a <em>partner agency</em> that uses "
        "NIST SP 800-63A compliant processes, documented in an inter-agency agreement.</p>"
    ),

    "ia-13": (
        "<p>This control addresses the management and security of identity providers and authorization servers — "
        "the systems that issue and validate identity assertions and access tokens.</p>"
        "<p><strong>Example 1:</strong> Harden your <em>Azure AD (Entra ID)</em> tenant by enabling security "
        "defaults, requiring MFA for all admins, and regularly reviewing app registrations and service principals.</p>"
        "<p><strong>Example 2:</strong> If running an on-premises <em>ADFS</em> or <em>Keycloak</em> identity "
        "provider, apply all security patches promptly, restrict admin access, and monitor for suspicious "
        "authentication patterns.</p>"
    ),

    "ia-13-1": (
        "<p>This enhancement requires protection of cryptographic keys used by identity providers and authorization "
        "servers — these keys are the crown jewels of your authentication infrastructure.</p>"
        "<p><strong>Example 1:</strong> Store your <em>SAML signing certificates</em> and <em>OAuth signing keys</em> "
        "in a <em>Hardware Security Module (HSM)</em> or Azure Key Vault with HSM backing to prevent extraction.</p>"
        "<p><strong>Example 2:</strong> Implement automatic key rotation for your <em>identity provider's token "
        "signing keys</em> and publish updated public keys to relying parties through standard metadata endpoints.</p>"
    ),

    "ia-13-2": (
        "<p>This enhancement requires verifying the authenticity and integrity of identity assertions and access "
        "tokens — ensuring they have not been forged or tampered with.</p>"
        "<p><strong>Example 1:</strong> Configure all your applications to <em>validate JWT signatures</em> against "
        "the identity provider's published signing keys before accepting access tokens or ID tokens.</p>"
        "<p><strong>Example 2:</strong> Implement <em>token audience validation</em> in your APIs to ensure that "
        "access tokens were issued specifically for your application and not replayed from another service.</p>"
    ),

    "ia-13-3": (
        "<p>This enhancement addresses token management — controlling the lifecycle of access tokens, refresh tokens, "
        "and other security tokens issued by your identity infrastructure.</p>"
        "<p><strong>Example 1:</strong> Configure <em>Azure AD token lifetime policies</em> to limit access tokens "
        "to 1 hour and refresh tokens to 24 hours, forcing periodic re-authentication.</p>"
        "<p><strong>Example 2:</strong> Implement <em>token revocation</em> capabilities in your identity provider "
        "so that when a user's access is terminated, their outstanding tokens can be immediately invalidated "
        "rather than waiting for natural expiration.</p>"
    ),
}
