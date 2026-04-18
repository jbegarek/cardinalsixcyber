NOTES = {
    # =========================================================================
    # RISK ASSESSMENT (RA) -- 3 practices
    # =========================================================================

    "ra-l2-3-11-1": (
        '<p>A risk assessment is really just a structured way of asking: &quot;What could go wrong '
        'with how we handle CUI, and how bad would it be?&quot; You are looking at your systems, '
        'your processes, and even your vendors to figure out where the weak spots are.</p>'
        '<p><strong>Example 1:</strong> Use NIST\'s CSET (Cyber Security Evaluation Tool) to walk '
        'through a guided assessment of your network. CSET asks plain-English questions about your '
        'environment and generates a risk report with prioritized findings you can hand to leadership.</p>'
        '<p><strong>Example 2:</strong> In Microsoft 365, go to the <em>Compliance Center &gt; '
        'Compliance Manager</em>. It automatically scores your tenant against NIST 800-171 controls '
        'and shows you exactly which settings are increasing your risk -- like whether MFA is enforced '
        'or if DLP policies are missing.</p>'
        '<p>Update this assessment at least annually, or any time you make a major change to your '
        'environment -- new systems, new vendors, new data flows.</p>'
    ),

    "ra-l2-3-11-2": (
        '<p>Vulnerability scanning means regularly checking your systems for known weaknesses -- '
        'missing patches, misconfigurations, outdated software -- before an attacker finds them first.</p>'
        '<p><strong>Example 1:</strong> Run authenticated Nessus (or ACAS if you are in a DoD environment) '
        'scans against all your endpoints and servers at least monthly. Use credentialed scans so the '
        'scanner can log into each machine and check installed software versions, not just probe from '
        'the outside. Review the results filtered by CVSS score 7.0 and above for priority remediation.</p>'
        '<p><strong>Example 2:</strong> Enable <em>Microsoft Defender Vulnerability Management</em> in '
        'the Microsoft 365 Defender portal. It continuously monitors your enrolled devices for '
        'vulnerabilities and misconfigurations, assigns severity scores, and even recommends specific '
        'remediation steps -- all without running a separate scan tool.</p>'
        '<p>The key here is consistency. Scanning once a year will not cut it. Set up recurring scans and '
        'make sure someone is actually reviewing the results and tracking remediation.</p>'
    ),

    "ra-l2-3-11-3": (
        '<p>Finding vulnerabilities is only half the job -- you have to actually fix them, and you '
        'should fix the most dangerous ones first. This practice says your remediation priority should '
        'be driven by your risk assessment, not just by whatever showed up most recently.</p>'
        '<p><strong>Example 1:</strong> After a Nessus scan, sort findings by CVSS score and cross-reference '
        'them with your risk assessment. A critical vulnerability on a system that processes CUI gets '
        'patched immediately. The same vulnerability on an isolated test machine with no CUI access '
        'can wait for the next maintenance window. Use your WSUS or SCCM console to push the patches '
        'and verify installation.</p>'
        '<p><strong>Example 2:</strong> In <em>Microsoft Defender for Endpoint &gt; Threat &amp; Vulnerability '
        'Management &gt; Remediation</em>, create remediation requests tied to specific CVEs. Assign them '
        'to your IT team with deadlines based on severity -- 72 hours for critical, 30 days for medium. '
        'The portal tracks completion so you have evidence for your assessor.</p>'
        '<p>Document your remediation decisions. If you accept a risk instead of fixing it, write down why '
        'and get leadership to sign off.</p>'
    ),

    # =========================================================================
    # SECURITY ASSESSMENT (CA) -- 4 practices
    # =========================================================================

    "ca-l2-3-12-1": (
        '<p>A security assessment is a formal check to see if your security controls are actually working '
        'the way they are supposed to. Think of it as a health checkup for your cybersecurity program -- '
        'you are testing whether the protections you put in place are doing their job.</p>'
        '<p><strong>Example 1:</strong> Hire a C3PAO or an independent assessor to run a NIST 800-171 '
        'assessment against your environment. They will interview staff, review documentation, and test '
        'controls -- for instance, verifying that your GPO for password complexity (minimum 14 characters, '
        'complexity enabled) is actually applied to all workstations by running <code>gpresult /r</code> '
        'on a sample of machines.</p>'
        '<p><strong>Example 2:</strong> Use <em>Microsoft Secure Score</em> in the M365 admin center as '
        'a self-assessment tool. It evaluates your tenant configuration against security best practices '
        'and gives you a numerical score with specific recommendations -- like enabling Safe Attachments '
        'in Exchange Online or blocking legacy authentication protocols.</p>'
        '<p>The assessment should result in a written report documenting what was tested, what passed, '
        'and what needs attention.</p>'
    ),

    "ca-l2-3-12-2": (
        '<p>A Plan of Action and Milestones (POA&amp;M) is your to-do list for security gaps. When an '
        'assessment finds something that is not right, you document it here along with what you are going '
        'to do about it and when you will have it done.</p>'
        '<p><strong>Example 1:</strong> Your Nessus scan found that SMBv1 is still enabled on three file '
        'servers. Your POA&amp;M entry would say: &quot;Disable SMBv1 on SRV-FILE01, SRV-FILE02, SRV-FILE03 via '
        'GPO (<code>Computer Configuration &gt; Administrative Templates &gt; Network &gt; Lanman Server '
        '&gt; SMB Minimum version</code>). Responsible: IT Admin. Due: 30 days. Milestone: GPO tested in '
        'dev by day 14.&quot;</p>'
        '<p><strong>Example 2:</strong> Your assessment found that endpoint detection logs are not being '
        'forwarded to a central location. The POA&amp;M entry: &quot;Configure Microsoft Defender for Endpoint to '
        'stream alerts to the SIEM via the <em>Settings &gt; APIs &gt; SIEM</em> connector in the M365 '
        'Defender portal. Responsible: Security team. Due: 45 days.&quot;</p>'
        '<p>Keep this document alive. Review it monthly, update completion percentages, and close items '
        'as they are resolved. Your assessor will want to see this.</p>'
    ),

    "ca-l2-3-12-3": (
        '<p>Continuous monitoring means you do not just check your security posture once a year and forget '
        'about it. You have tools and processes running all the time to watch for changes that could '
        'introduce risk.</p>'
        '<p><strong>Example 1:</strong> Deploy a SIEM solution (like Microsoft Sentinel or Splunk) that '
        'ingests logs from your firewall, Active Directory, endpoints, and cloud services. Set up '
        'detection rules for high-risk events -- failed login brute-force attempts, new admin accounts '
        'created, or firewall rules changed. Review alerts daily.</p>'
        '<p><strong>Example 2:</strong> Enable <em>Microsoft Defender for Cloud Apps</em> to continuously '
        'monitor your cloud environment. It flags risky behaviors like mass file downloads, sign-ins from '
        'impossible travel locations, or OAuth app consent grants. Alerts are generated automatically '
        'and assigned to your security team for triage.</p>'
        '<p>The point is not to drown in dashboards -- it is to make sure someone is watching for meaningful '
        'changes to your security posture between formal assessments.</p>'
    ),

    "ca-l2-3-12-4": (
        '<p>A System Security Plan (SSP) is the single document that describes your entire security '
        'program for a given system. It explains what the system does, where CUI lives, how you protect '
        'it, and how your controls map to NIST 800-171 requirements.</p>'
        '<p><strong>Example 1:</strong> Document your network boundary by including a current network '
        'diagram (from a tool like Visio or draw.io) that shows your firewall, VLANs, DMZ, VPN '
        'concentrator, and where CUI is stored. For each boundary device, note the specific rules -- '
        'for instance, your SonicWall firewall\'s default deny rule on the WAN interface with explicit '
        'allow rules only for HTTPS (443) and IPSec VPN (UDP 500/4500).</p>'
        '<p><strong>Example 2:</strong> In the SSP, describe how each NIST 800-171 control is implemented. '
        'For example, under Access Control, document that you enforce account lockout via GPO: '
        '<code>Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; Account Lockout '
        'Policy</code> -- threshold set to 3 invalid attempts, lockout duration 15 minutes, reset counter '
        'after 15 minutes.</p>'
        '<p>Update the SSP whenever your environment changes -- new systems, new connections, new security '
        'tools. Treat it as a living document, not a one-time deliverable.</p>'
    ),

    # =========================================================================
    # SYSTEM & COMMUNICATIONS PROTECTION (SC) -- 16 practices
    # =========================================================================

    "sc-l1-3-13-1": (
        '<p>Boundary protection is about controlling what traffic flows in and out of your network -- and '
        'monitoring the key choke points inside it. Your firewall is the most obvious example, but it '
        'also includes internal segmentation between sensitive and non-sensitive zones.</p>'
        '<p><strong>Example 1:</strong> Configure your perimeter firewall (Palo Alto, SonicWall, pfSense, '
        'etc.) with a default-deny outbound rule, then add explicit allow rules only for required traffic: '
        'HTTPS (443), DNS (53 to your approved DNS servers only), and your VPN ports. Log all denied '
        'traffic and review weekly.</p>'
        '<p><strong>Example 2:</strong> Enable <em>Windows Defender Firewall with Advanced Security</em> '
        'via GPO (<code>Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; '
        'Windows Defender Firewall</code>) on all endpoints. Set the domain, private, and public profiles '
        'to block inbound connections by default. Create inbound rules only for approved management '
        'traffic like RDP from your admin VLAN.</p>'
        '<p>Think of boundary protection as layers -- your perimeter firewall is the outer wall, host-based '
        'firewalls are the inner doors, and network segmentation creates separate rooms.</p>'
    ),

    "sc-l2-3-13-2": (
        '<p>This practice is about building security into your systems from the ground up, not bolting '
        'it on after the fact. Your network architecture, your applications, and your infrastructure '
        'should all be designed with security as a core principle.</p>'
        '<p><strong>Example 1:</strong> Implement a zero-trust network architecture by segmenting your '
        'network into VLANs with inter-VLAN routing controlled by ACLs on your managed switch or '
        'firewall. For example, put CUI systems on VLAN 10, general workstations on VLAN 20, and '
        'printers/IoT on VLAN 30 -- with firewall rules that prevent VLAN 20 and 30 from reaching '
        'VLAN 10 directly.</p>'
        '<p><strong>Example 2:</strong> In Azure or M365, use <em>Conditional Access Policies</em> in '
        'Entra ID to enforce security at the identity layer. Create a policy that requires MFA and a '
        'compliant device for any access to SharePoint sites containing CUI. This is security baked into '
        'the architecture, not an afterthought.</p>'
        '<p>The assessor wants to see that security decisions were intentional and documented, not '
        'accidental.</p>'
    ),

    "sc-l2-3-13-3": (
        '<p>Regular users should not be using the same accounts or interfaces they use for day-to-day '
        'work to manage servers, domain controllers, or security tools. Keeping these separate reduces '
        'the blast radius if a user account gets compromised.</p>'
        '<p><strong>Example 1:</strong> Create separate admin accounts in Active Directory (e.g., '
        '<code>j.smith-admin</code>) for IT staff and place them in a dedicated Admin OU with a stricter '
        'GPO. Use the <em>Deny log on locally</em> setting for these admin accounts on regular '
        'workstations, and use <em>Deny log on through Remote Desktop Services</em> for regular user '
        'accounts on servers.</p>'
        '<p><strong>Example 2:</strong> In M365, assign the Global Administrator role only to dedicated '
        'admin accounts in the <em>Microsoft Entra admin center &gt; Roles and administrators</em>. '
        'These accounts should not have mailboxes or be used for daily email. Enable Privileged Identity '
        'Management (PIM) so admin roles are activated just-in-time rather than permanently assigned.</p>'
    ),

    "sc-l2-3-13-4": (
        '<p>When users or processes share system resources -- like memory, disk space, or temp directories -- '
        'there is a risk that leftover data from one user could be accessible to the next. This practice '
        'says you need to prevent that kind of data leakage.</p>'
        '<p><strong>Example 1:</strong> Enable the GPO setting <code>Computer Configuration &gt; Windows '
        'Settings &gt; Security Settings &gt; Local Policies &gt; Security Options &gt; Shutdown: Clear '
        'virtual memory pagefile</code> to ensure the pagefile is wiped at shutdown. This prevents '
        'sensitive data fragments from persisting in virtual memory between sessions.</p>'
        '<p><strong>Example 2:</strong> On shared workstations or terminal servers, configure '
        '<em>Disk Cleanup</em> policies or use the GPO <code>Delete user profiles older than a specified '
        'number of days on system restart</code> (under Computer Configuration &gt; Administrative '
        'Templates &gt; System &gt; User Profiles). This ensures temp files and cached data from previous '
        'user sessions are removed.</p>'
    ),

    "sc-l2-3-13-5": (
        '<p>If you have anything publicly accessible -- a web server, a customer portal, an email gateway -- '
        'it needs to live in a separate network segment (a DMZ) so that if it gets compromised, the '
        'attacker cannot walk straight into your internal network where CUI lives.</p>'
        '<p><strong>Example 1:</strong> Configure a DMZ on your firewall with three zones: WAN (untrusted), '
        'DMZ (semi-trusted), and LAN (trusted). Place your public-facing web server in the DMZ. Create '
        'firewall rules that allow inbound HTTPS from WAN to DMZ, but block all direct traffic from '
        'DMZ to LAN. If the web server needs to query an internal database, allow only that specific '
        'port from the DMZ server\'s IP to the database server\'s IP.</p>'
        '<p><strong>Example 2:</strong> If you are using cloud services, leverage <em>Azure Network Security '
        'Groups (NSGs)</em> to isolate public-facing resources. Place your web app in a public subnet '
        'with an NSG that allows only port 443 inbound, and your backend services in a private subnet '
        'with an NSG that allows traffic only from the web app\'s subnet.</p>'
    ),

    "sc-l2-3-13-6": (
        '<p>Your network should block everything by default and only allow the traffic you have explicitly '
        'approved. This is the opposite of the common (and dangerous) approach where everything is open '
        'and you try to block known-bad traffic.</p>'
        '<p><strong>Example 1:</strong> On your perimeter firewall, set the default rule for both inbound '
        'and outbound traffic to <strong>Deny All</strong>. Then add specific allow rules above it: '
        'allow outbound HTTPS (443), allow outbound DNS (53) only to your designated DNS servers, allow '
        'inbound VPN (UDP 500/4500 or WireGuard port) to your VPN concentrator. Every rule should have '
        'a documented business justification.</p>'
        '<p><strong>Example 2:</strong> On Windows endpoints via GPO, configure <em>Windows Defender '
        'Firewall</em> to block all inbound connections by default for all profiles. Under '
        '<code>Inbound Rules</code>, create exceptions only for approved services. Log blocked '
        'connections by enabling <code>Logging &gt; Log dropped packets: Yes</code> in the firewall '
        'profile properties.</p>'
    ),

    "sc-l2-3-13-7": (
        '<p>Split tunneling means a VPN user can access your corporate network and the open internet '
        'at the same time through different network paths. That is a problem because malware or an '
        'attacker on the internet side could potentially pivot into your corporate network through '
        'that user\'s machine.</p>'
        '<p><strong>Example 1:</strong> In your VPN solution (Cisco AnyConnect, GlobalProtect, Windows '
        'Always On VPN), configure <em>full tunnel</em> mode so that all traffic -- including internet '
        'traffic -- routes through the corporate VPN gateway. In Cisco AnyConnect, this is set in the '
        'AnyConnect profile XML: <code>&lt;SplitTunneling&gt;Disabled&lt;/SplitTunneling&gt;</code>.</p>'
        '<p><strong>Example 2:</strong> If using Windows Always On VPN with a GPO or Intune profile, '
        'set the VPN connection to <em>Force Tunnel</em> in the VPN profile configuration. In Intune, '
        'go to <em>Devices &gt; Configuration profiles &gt; VPN</em> and set the split tunneling option '
        'to <strong>Disabled</strong>. This forces all traffic through the VPN tunnel when connected.</p>'
    ),

    "sc-l2-3-13-8": (
        '<p>CUI needs to be encrypted whenever it is moving across a network and whenever it is sitting '
        'on a disk. If someone intercepts the traffic or steals the drive, they should not be able to '
        'read the data.</p>'
        '<p><strong>Example 1:</strong> For data in transit, enforce TLS 1.2 or higher on all web '
        'services and email. In the M365 admin center, go to <em>Exchange admin center &gt; Mail flow '
        '&gt; Connectors</em> and configure your mail flow connectors to require TLS. On IIS or your '
        'web server, disable TLS 1.0 and 1.1 via registry settings or the IIS Crypto tool.</p>'
        '<p><strong>Example 2:</strong> For data at rest, enable <em>BitLocker Drive Encryption</em> on '
        'all endpoints via GPO: <code>Computer Configuration &gt; Administrative Templates &gt; Windows '
        'Components &gt; BitLocker Drive Encryption</code>. Require TPM + PIN for OS drives. Store '
        'recovery keys in Active Directory. Verify encryption status across your fleet using '
        '<code>manage-bde -status</code> or the BitLocker Recovery report in MBAM/Intune.</p>'
    ),

    "sc-l2-3-13-9": (
        '<p>Network sessions should not stay open forever. If a user walks away from their desk or a '
        'connection sits idle, it should be terminated after a defined period to prevent unauthorized '
        'access on an unattended session.</p>'
        '<p><strong>Example 1:</strong> Configure session timeouts for Remote Desktop connections via '
        'GPO: <code>Computer Configuration &gt; Administrative Templates &gt; Windows Components &gt; '
        'Remote Desktop Services &gt; Session Time Limits</code>. Set '
        '<em>Set time limit for disconnected sessions</em> to 15 minutes and '
        '<em>Set time limit for active but idle sessions</em> to 30 minutes.</p>'
        '<p><strong>Example 2:</strong> On your firewall or VPN concentrator, configure idle session '
        'timeouts. For example, on a Palo Alto firewall, set the TCP session timeout under '
        '<em>Device &gt; Setup &gt; Session &gt; Session Timeouts</em> to 30 minutes for general traffic. '
        'For VPN sessions, configure the idle timeout in the GlobalProtect gateway settings to '
        'disconnect users after 30 minutes of inactivity.</p>'
    ),

    "sc-l2-3-13-10": (
        '<p>If you are using encryption (and you should be), you need a solid process for creating, '
        'distributing, storing, rotating, and destroying the cryptographic keys. The encryption is '
        'only as strong as how you manage the keys.</p>'
        '<p><strong>Example 1:</strong> For BitLocker, store recovery keys in Active Directory Domain '
        'Services (AD DS). Configure this via GPO: <code>Computer Configuration &gt; Administrative '
        'Templates &gt; Windows Components &gt; BitLocker &gt; Store BitLocker recovery information in '
        'AD DS</code>. This ensures keys are centrally managed and recoverable, not written on sticky '
        'notes.</p>'
        '<p><strong>Example 2:</strong> For TLS certificates on your web servers, use a certificate '
        'management tool or process. Track certificate expiration dates in a spreadsheet or tool like '
        'Venafi or Let\'s Encrypt with auto-renewal. Ensure you are using keys of at least 2048-bit RSA '
        'or 256-bit ECC, and rotate certificates annually. If using Azure, leverage <em>Azure Key Vault</em> '
        'to store and manage certificates and secrets with access policies and audit logging.</p>'
    ),

    "sc-l2-3-13-11": (
        '<p>This practice requires that when you use cryptography to protect CUI, you use FIPS-validated '
        'cryptographic modules. In practical terms, this means making sure your encryption tools and '
        'algorithms meet federal standards -- not rolling your own crypto.</p>'
        '<p><strong>Example 1:</strong> Enable FIPS-compliant mode on Windows endpoints via GPO: '
        '<code>Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; Local Policies '
        '&gt; Security Options &gt; System cryptography: Use FIPS compliant algorithms for encryption, '
        'hashing, and signing</code> -- set to <strong>Enabled</strong>. This forces Windows to use only '
        'FIPS 140-validated cryptographic modules.</p>'
        '<p><strong>Example 2:</strong> Verify that your VPN solution uses FIPS-validated encryption. '
        'For example, Cisco AnyConnect supports FIPS mode -- enable it in the AnyConnect Local Policy '
        'profile by setting <code>&lt;FIPSMode&gt;true&lt;/FIPSMode&gt;</code>. This ensures the VPN '
        'tunnel uses only approved algorithms (AES-256, SHA-256, etc.).</p>'
        '<p>Check NIST\'s Cryptographic Module Validation Program (CMVP) list at csrc.nist.gov to confirm '
        'your products have valid FIPS 140 certificates.</p>'
    ),

    "sc-l2-3-13-12": (
        '<p>Collaborative computing devices include things like webcams, microphones, and smart displays '
        'in conference rooms. The concern is that these could be remotely activated to eavesdrop. You '
        'need to prevent remote activation and make it obvious to people in the room when these '
        'devices are active.</p>'
        '<p><strong>Example 1:</strong> Use a GPO to disable the camera and microphone on workstations '
        'by default. Under <code>Computer Configuration &gt; Administrative Templates &gt; Windows '
        'Components &gt; Camera</code>, set <em>Allow Use of Camera</em> to <strong>Disabled</strong>. '
        'For microphone access, manage it through <em>Settings &gt; Privacy &gt; Microphone</em> '
        'or deploy an Intune device restriction profile that blocks microphone access for all apps '
        'except approved conferencing tools like Teams.</p>'
        '<p><strong>Example 2:</strong> For conference room systems (like Microsoft Teams Rooms devices '
        'or Zoom Rooms), ensure the device has a physical indicator light that activates when the camera '
        'or microphone is in use. Configure the device to require a physical button press to start '
        'a meeting -- do not allow remote meeting joins to automatically activate A/V hardware. Disable '
        'remote management features that could allow external activation.</p>'
    ),

    "sc-l2-3-13-13": (
        '<p>Mobile code refers to software that is downloaded and executed automatically -- things like '
        'JavaScript, Java applets, ActiveX controls, PowerShell scripts, or macros. You need to control '
        'what types of mobile code can run in your environment.</p>'
        '<p><strong>Example 1:</strong> Restrict Office macro execution via GPO: <code>User Configuration '
        '&gt; Administrative Templates &gt; Microsoft Office &gt; Security Settings &gt; VBA Macro '
        'Notification Settings</code> -- set to <em>Disable all except digitally signed macros</em>. '
        'This prevents untrusted macros (a common malware delivery method) from running while still '
        'allowing business-critical signed macros.</p>'
        '<p><strong>Example 2:</strong> Configure Windows Defender Application Control (WDAC) or '
        'AppLocker to restrict which scripts and executables can run. Create an AppLocker policy via '
        'GPO (<code>Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; '
        'Application Control Policies &gt; AppLocker</code>) that allows only scripts signed by '
        'your organization or from trusted paths (e.g., <code>C:\\Program Files\\*</code>) and blocks '
        'everything else.</p>'
    ),

    "sc-l2-3-13-14": (
        '<p>VoIP systems -- like Microsoft Teams calling, Cisco phone systems, or SIP-based solutions -- '
        'carry voice traffic over your data network. That means they are subject to the same threats as '
        'any other network service: eavesdropping, denial of service, and unauthorized access.</p>'
        '<p><strong>Example 1:</strong> Segment your VoIP traffic onto a dedicated VLAN (e.g., VLAN 50) '
        'with QoS policies that prioritize voice traffic. On your managed switch, configure the voice '
        'VLAN and apply ACLs that prevent data VLAN devices from accessing the voice VLAN directly. '
        'This limits the attack surface and prevents casual network sniffing of voice traffic.</p>'
        '<p><strong>Example 2:</strong> If using Microsoft Teams for voice, enable end-to-end encryption '
        'for 1:1 Teams calls in the <em>Teams admin center &gt; Enhanced encryption policies</em>. '
        'Also review and restrict who can make PSTN calls by configuring calling policies under '
        '<em>Voice &gt; Calling policies</em> -- assign policies that limit external dialing to only '
        'the users who need it.</p>'
    ),

    "sc-l2-3-13-15": (
        '<p>Session authenticity means both sides of a network conversation can trust that they are '
        'talking to who they think they are talking to, and that the data has not been tampered with '
        'in transit. This protects against man-in-the-middle attacks and session hijacking.</p>'
        '<p><strong>Example 1:</strong> Enforce TLS 1.2+ on all internal web applications and services. '
        'On IIS, disable older protocols using the IIS Crypto tool or by editing the registry under '
        '<code>HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols</code>. '
        'Disable TLS 1.0, TLS 1.1, SSL 2.0, and SSL 3.0 by setting their <code>Enabled</code> DWORD '
        'to <code>0</code>.</p>'
        '<p><strong>Example 2:</strong> Enable SMB signing on all domain-joined systems via GPO: '
        '<code>Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; Local Policies '
        '&gt; Security Options</code> -- set <em>Microsoft network client: Digitally sign communications '
        '(always)</em> and <em>Microsoft network server: Digitally sign communications (always)</em> to '
        '<strong>Enabled</strong>. This prevents SMB relay and man-in-the-middle attacks on file shares.</p>'
    ),

    "sc-l2-3-13-16": (
        '<p>CUI sitting on a hard drive, USB drive, or in a database needs to be encrypted so that '
        'if someone physically steals the device or gains unauthorized access to storage, they cannot '
        'read the data.</p>'
        '<p><strong>Example 1:</strong> Enable <em>BitLocker</em> on all laptops and workstations that '
        'process or store CUI. Deploy via GPO: <code>Computer Configuration &gt; Administrative Templates '
        '&gt; Windows Components &gt; BitLocker Drive Encryption &gt; Operating System Drives</code> -- '
        'require TPM + startup PIN. For removable drives, enable BitLocker To Go under the Removable '
        'Data Drives section and set it to deny write access to drives that are not BitLocker-encrypted.</p>'
        '<p><strong>Example 2:</strong> For CUI stored in SharePoint Online or OneDrive, Microsoft '
        'applies encryption at rest by default using service-level encryption with AES-256. Go further '
        'by applying <em>Microsoft Purview sensitivity labels</em> to CUI files -- these labels apply '
        'persistent encryption and access controls that travel with the file, even if it is downloaded '
        'or forwarded. Configure labels in the <em>Microsoft Purview compliance portal &gt; Information '
        'protection &gt; Labels</em>.</p>'
    ),

    # =========================================================================
    # SYSTEM & INFORMATION INTEGRITY (SI) -- 7 practices
    # =========================================================================

    "si-l1-3-14-1": (
        '<p>Flaw remediation is a fancy way of saying &quot;patch your systems.&quot; When vendors release security '
        'updates, you need to install them promptly. The longer you wait, the more time attackers have '
        'to exploit known vulnerabilities.</p>'
        '<p><strong>Example 1:</strong> Use <em>Windows Server Update Services (WSUS)</em> or '
        '<em>Microsoft Endpoint Configuration Manager (MECM/SCCM)</em> to centrally manage and deploy '
        'patches. Configure automatic approval rules for critical and security updates, and set a '
        'deployment deadline of 14 days after release. Run the WSUS console report monthly to verify '
        'compliance across your fleet.</p>'
        '<p><strong>Example 2:</strong> For cloud-managed endpoints, use <em>Microsoft Intune &gt; '
        'Devices &gt; Windows updates &gt; Update rings</em> to define patching policies. Create an '
        'update ring that defers feature updates by 30 days but installs quality (security) updates '
        'within 7 days. Set the compliance deadline so devices that miss the window are automatically '
        'forced to restart and apply updates.</p>'
        '<p>Do not forget non-Windows systems. Firmware updates for firewalls, switches, and printers '
        'count too -- track these in your asset inventory.</p>'
    ),

    "si-l2-3-14-2": (
        '<p>You need antivirus/anti-malware protection on every system that can host malicious code, '
        'and it needs to be active at the points where data enters and leaves your network -- email '
        'gateways, web proxies, and endpoints.</p>'
        '<p><strong>Example 1:</strong> Deploy <em>Microsoft Defender for Endpoint</em> across all '
        'workstations and servers. In the <em>Microsoft 365 Defender portal &gt; Settings &gt; Endpoints '
        '&gt; Advanced features</em>, enable real-time protection, cloud-delivered protection, and '
        'automatic sample submission. Configure the scan schedule under <em>Endpoint security &gt; '
        'Antivirus &gt; Microsoft Defender Antivirus policy</em> to run a weekly full scan and '
        'continuous real-time monitoring.</p>'
        '<p><strong>Example 2:</strong> For email-based threats, enable <em>Microsoft Defender for '
        'Office 365</em> in the M365 security center. Configure <em>Safe Attachments</em> policies '
        'to detonate attachments in a sandbox before delivery, and <em>Safe Links</em> policies to '
        'rewrite and check URLs at time of click. These catch malware at the email gateway before '
        'it reaches user endpoints.</p>'
    ),

    "si-l2-3-14-3": (
        '<p>You need a way to stay informed about new vulnerabilities and threats that could affect '
        'your systems. This means subscribing to official sources and having a process to review '
        'and act on what you learn.</p>'
        '<p><strong>Example 1:</strong> Subscribe to CISA\'s Known Exploited Vulnerabilities (KEV) '
        'catalog alerts at cisa.gov and US-CERT\'s National Cyber Awareness System mailing list. When '
        'a new advisory drops that affects software in your environment -- say, a critical Exchange '
        'Server vulnerability -- triage it within 48 hours and initiate patching per your POA&amp;M process.</p>'
        '<p><strong>Example 2:</strong> Enable <em>Microsoft 365 Message Center</em> notifications in '
        'the M365 admin center (<em>Health &gt; Message center</em>) and set up email notifications '
        'for security-related posts. Also subscribe to vendor-specific security bulletins -- for example, '
        'Cisco\'s Security Advisories or Palo Alto\'s Security Advisory page -- for any network hardware '
        'in your environment.</p>'
        '<p>The key is having a named person or team responsible for reviewing these alerts weekly and '
        'deciding what action to take.</p>'
    ),

    "si-l2-3-14-4": (
        '<p>Your antivirus and anti-malware tools are only as good as their latest definitions. If '
        'your signature files are weeks old, you are essentially blind to new threats. Keep protection '
        'mechanisms current.</p>'
        '<p><strong>Example 1:</strong> In <em>Microsoft Defender Antivirus</em>, verify that automatic '
        'definition updates are enabled. Check via GPO: <code>Computer Configuration &gt; Administrative '
        'Templates &gt; Windows Components &gt; Microsoft Defender Antivirus &gt; Security Intelligence '
        'Updates</code> -- ensure <em>Define the number of days before security intelligence is considered '
        'out of date</em> is set to 1 day. You can verify definitions are current on any machine by '
        'running <code>Get-MpComputerStatus | Select AntivirusSignatureLastUpdated</code> in '
        'PowerShell.</p>'
        '<p><strong>Example 2:</strong> For environments using a third-party AV like CrowdStrike Falcon '
        'or Trellix (formerly McAfee), check the management console to confirm sensor/agent versions are '
        'current across all endpoints. In CrowdStrike, go to <em>Host Management &gt; Sensor Update '
        'Policy</em> and ensure auto-update is set to the N-1 or Latest channel. Set alerts for any '
        'endpoints that have not checked in within 48 hours.</p>'
    ),

    "si-l2-3-14-5": (
        '<p>This is the companion to malicious code protection -- you need to be scanning your systems '
        'on a regular schedule and also scanning files in real time as they arrive from external '
        'sources (email attachments, downloads, USB drives).</p>'
        '<p><strong>Example 1:</strong> Configure <em>Microsoft Defender Antivirus</em> scheduled scans '
        'via GPO or Intune. Set a weekly full scan (all files and running programs) for off-hours -- say, '
        'Saturday at 2 AM -- and ensure real-time protection is always on. In Intune, this is under '
        '<em>Endpoint security &gt; Antivirus &gt; Microsoft Defender Antivirus &gt; Scan schedule</em>.</p>'
        '<p><strong>Example 2:</strong> Run authenticated ACAS/Nessus vulnerability scans against your '
        'entire CUI enclave at least monthly. Schedule recurring scans in the Nessus console using a '
        'credentialed scan policy that checks for missing patches, misconfigurations, and malware '
        'indicators. Review the results within 5 business days and feed critical findings into your '
        'POA&amp;M.</p>'
    ),

    "si-l2-3-14-6": (
        '<p>System monitoring means actively watching your systems for signs of attacks, unauthorized '
        'access, and suspicious behavior. You need tools collecting logs, generating alerts, and '
        'someone reviewing them regularly.</p>'
        '<p><strong>Example 1:</strong> Deploy <em>Microsoft Sentinel</em> (cloud SIEM) or a similar '
        'SIEM solution. Connect it to your Active Directory, M365 audit logs, firewall logs, and '
        'endpoint telemetry from Defender for Endpoint. Create analytics rules for high-priority events: '
        'multiple failed logins followed by a success (credential stuffing), new service installations, '
        'or PowerShell execution with encoded commands. Assign these alerts to a security analyst '
        'for daily review.</p>'
        '<p><strong>Example 2:</strong> Enable Windows Security Event logging via GPO: '
        '<code>Computer Configuration &gt; Windows Settings &gt; Security Settings &gt; Advanced Audit '
        'Policy Configuration</code>. At minimum, enable auditing for Logon/Logoff (success and failure), '
        'Account Management (success and failure), Object Access (failure), and Policy Change (success). '
        'Forward these events to a central log collector using Windows Event Forwarding (WEF) or a '
        'log shipping agent.</p>'
        '<p>Monitoring without review is just storage. Make sure someone is looking at alerts daily.</p>'
    ),

    "si-l2-3-14-7": (
        '<p>This practice is about detecting when someone or something is using your systems in a way '
        'that was not authorized -- whether that is an employee accessing data they should not, a '
        'compromised account, or shadow IT popping up on your network.</p>'
        '<p><strong>Example 1:</strong> Use <em>Microsoft Defender for Identity</em> (formerly Azure ATP) '
        'to monitor Active Directory for suspicious behaviors: pass-the-hash attacks, lateral movement, '
        'privilege escalation, or reconnaissance activity. It installs sensors on your domain controllers '
        'and flags anomalies like a user account suddenly querying all AD objects or authenticating from '
        'an unusual location.</p>'
        '<p><strong>Example 2:</strong> Implement network access control (NAC) using 802.1X authentication '
        'on your switches. Configure a RADIUS server (like Windows NPS) so that only domain-joined, '
        'authorized devices can connect to your network. Unrecognized devices get placed in a quarantine '
        'VLAN with no access to CUI systems. Review NAC logs weekly for unauthorized connection '
        'attempts.</p>'
        '<p>Combine these with the audit logs from SI.L2-3.14.6 to build a complete picture of who is '
        'doing what on your network.</p>'
    ),
}
