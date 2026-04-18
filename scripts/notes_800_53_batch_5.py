NOTES = {
    # =========================================================================
    # SYSTEM AND COMMUNICATIONS PROTECTION (SC) — 162 controls
    # =========================================================================

    "sc-1": (
        '<p>This control requires you to create and maintain a written policy for how your '
        'organization protects its systems and communications. Think of it as the rulebook '
        'that tells everyone how data should be secured when it moves between systems or '
        'sits on your network.</p>'
        '<p><strong>Example 1:</strong> Draft a System and Communications Protection policy '
        'document that covers topics like encryption requirements, firewall rules, and network '
        'segmentation. Store it in SharePoint with version control and assign your IT manager '
        'as the owner who reviews it annually.</p>'
        '<p><strong>Example 2:</strong> In M365 Compliance Center, use the Compliance Manager '
        'to track your SC family controls. Upload your policy document as evidence and set a '
        'recurring calendar reminder for annual review and update.</p>'
    ),

    "sc-2": (
        '<p>This control means keeping the tools and interfaces that regular users see '
        'completely separate from the tools administrators use to manage systems. A normal '
        'employee should never stumble into a server management console.</p>'
        '<p><strong>Example 1:</strong> Configure your Windows servers so that administrative '
        'tools like Server Manager, PowerShell ISE, and MMC snap-ins are only available on '
        'dedicated admin workstations — not on standard employee desktops. Use a GPO to '
        'remove administrative tools from non-admin machines.</p>'
        '<p><strong>Example 2:</strong> In Microsoft 365, use Privileged Access Workstations '
        '(PAWs) for Exchange and Azure AD administration. Regular users access Outlook and '
        'Teams from standard machines, while admins manage tenant settings only from hardened, '
        'dedicated devices on a separate network segment.</p>'
    ),

    "sc-2-1": (
        '<p>Non-privileged users should never see system management options on their screens. '
        'If a regular employee opens a web portal or application, admin functions should be '
        'completely hidden — not just grayed out.</p>'
        '<p><strong>Example 1:</strong> Configure your web applications so admin panels and '
        'management consoles are served on a completely different URL or port that is only '
        'accessible from the admin VLAN. Regular users never even see a login page for '
        'admin functions.</p>'
        '<p><strong>Example 2:</strong> In Azure AD, use Conditional Access policies to block '
        'access to admin portals (portal.azure.com, admin.microsoft.com) from non-admin '
        'accounts. Only accounts with admin roles assigned can reach those interfaces.</p>'
    ),

    "sc-2-2": (
        '<p>This enhancement focuses on privacy — storing user interaction data (session state, '
        'preferences, activity history) separately from the application itself. If the app is '
        'compromised, attackers should not automatically get access to user behavior data.</p>'
        '<p><strong>Example 1:</strong> Configure your web applications to store session data '
        'in a separate database or Redis cache that is on a different server segment from the '
        'application code. Apply different access controls to the session store.</p>'
        '<p><strong>Example 2:</strong> In M365, use Information Barriers and Data Loss '
        'Prevention policies to ensure user activity logs and interaction data are stored in '
        'separate compliance boundaries from the application data itself.</p>'
    ),

    "sc-3": (
        '<p>Security functions — things like access control checks, encryption, and audit '
        'logging — need to run in their own protected space, isolated from regular application '
        'code. If an attacker compromises a normal application, they should not be able to '
        'tamper with your security mechanisms.</p>'
        '<p><strong>Example 1:</strong> Use Windows Credential Guard, which runs the LSASS '
        'process in a virtualization-based security container. Even if malware compromises '
        'the OS kernel, it cannot steal cached credentials because they are isolated in a '
        'separate security domain.</p>'
        '<p><strong>Example 2:</strong> Deploy a dedicated SIEM server (like Splunk or the '
        'Elastic Stack) on a hardened, isolated network segment. Audit logs flow one-way into '
        'the SIEM, and even if an attacker compromises production servers, they cannot reach '
        'or tamper with the security monitoring infrastructure.</p>'
    ),

    "sc-3-1": (
        '<p>This enhancement requires using physical hardware separation to isolate security '
        'functions, not just software-based isolation. The idea is that hardware boundaries '
        'are much harder to bypass than software boundaries.</p>'
        '<p><strong>Example 1:</strong> Use a Hardware Security Module (HSM) to handle all '
        'cryptographic key operations. The HSM is a physically separate device that processes '
        'encryption and signing operations in tamper-resistant hardware — keys never leave '
        'the device.</p>'
        '<p><strong>Example 2:</strong> Enable Intel TXT (Trusted Execution Technology) or '
        'AMD SEV on your servers to create hardware-enforced memory regions where security '
        'functions execute. The CPU hardware itself prevents other processes from reading '
        'or modifying that protected memory.</p>'
    ),

    "sc-3-2": (
        '<p>Access control and information flow control functions need extra isolation — they '
        'must be separated not just from regular applications but from other security functions '
        'like auditing or malware scanning.</p>'
        '<p><strong>Example 1:</strong> Deploy your firewall (access/flow control) on dedicated '
        'appliances separate from your IDS/IPS sensors and your SIEM. Each security function '
        'runs on its own hardware or VM with its own management interface and credentials.</p>'
        '<p><strong>Example 2:</strong> In a virtualized environment, run your access control '
        'services (Active Directory domain controllers) on dedicated Hyper-V hosts that do not '
        'share physical hardware with application VMs or monitoring VMs.</p>'
    ),

    "sc-3-3": (
        '<p>Keep the security boundary as lean as possible. The less non-security code running '
        'inside the trusted security perimeter, the smaller the attack surface.</p>'
        '<p><strong>Example 1:</strong> On your domain controllers, remove all unnecessary '
        'roles and features — no web servers, no file shares, no print services. The only '
        'software running should be Active Directory, DNS for AD, and the security agent. '
        'Use Server Core installations to minimize the OS footprint.</p>'
        '<p><strong>Example 2:</strong> On your firewall appliances, disable any optional '
        'modules you do not use — VPN concentrator features, web filtering, application '
        'proxying — if they are not required. Each extra feature is extra code inside your '
        'security boundary that could be exploited.</p>'
    ),

    "sc-3-4": (
        '<p>Security functions should be built as independent modules that do not depend heavily '
        'on each other. If one module has a bug, it should not cascade into other security '
        'functions.</p>'
        '<p><strong>Example 1:</strong> Design your security architecture so that your '
        'authentication system (Active Directory), your encryption service (certificate '
        'authority), and your logging system (SIEM) each operate independently. A failure '
        'in your SIEM should not prevent users from authenticating.</p>'
        '<p><strong>Example 2:</strong> When developing custom security applications, follow '
        'modular design principles — separate input validation, authentication, authorization, '
        'and audit logging into distinct code modules with clean interfaces between them.</p>'
    ),

    "sc-3-5": (
        '<p>Security functions should be organized in layers where lower layers never depend '
        'on higher layers. This prevents circular dependencies that could be exploited to '
        'bypass security.</p>'
        '<p><strong>Example 1:</strong> Structure your network security in layers: the hardware '
        'firewall at the perimeter (lowest layer) does not depend on the host-based firewall '
        '(higher layer). If the host firewall fails, the perimeter firewall still blocks '
        'unauthorized traffic independently.</p>'
        '<p><strong>Example 2:</strong> In your server builds, the boot integrity check (UEFI '
        'Secure Boot at the lowest layer) does not depend on the OS-level antivirus (higher '
        'layer). Each layer validates independently, and lower layers are never affected by '
        'failures in the layers above them.</p>'
    ),

    "sc-4": (
        '<p>When one user or process finishes using shared system resources — memory, disk '
        'space, CPU registers — the system must clean up so the next user cannot read '
        'leftover data. This prevents information leakage between users.</p>'
        '<p><strong>Example 1:</strong> Enable the "Clear virtual memory pagefile" GPO setting '
        'under Computer Configuration > Windows Settings > Security Settings > Local Policies '
        '> Security Options. This ensures the Windows pagefile is wiped at shutdown so '
        'sensitive data from RAM is not left on disk.</p>'
        '<p><strong>Example 2:</strong> On database servers, configure your SQL instance to '
        'overwrite deleted data blocks rather than simply marking them as available. In SQL '
        'Server, enable Transparent Data Encryption (TDE) so even if old data blocks are '
        'recovered, they are encrypted and unreadable.</p>'
    ),

    "sc-4-1": (
        '<p>This enhancement applies to systems that process data at different security '
        'classification levels. Shared resources must prevent data at one security level '
        'from leaking to users at a different level.</p>'
        '<p><strong>Example 1:</strong> On cross-domain systems, use certified cross-domain '
        'solutions (CDS) that sanitize shared memory and disk buffers between sessions '
        'operating at different classification levels.</p>'
        '<p><strong>Example 2:</strong> Configure your virtualization platform to use '
        'memory scrubbing between VM allocations so that a VM operating at one security '
        'level cannot recover memory contents from a VM that operated at a higher level.</p>'
    ),

    "sc-4-2": (
        '<p>During multilevel or periods processing — where a system switches between handling '
        'data at different classification levels — shared resources must be sanitized according '
        'to approved procedures before the switch.</p>'
        '<p><strong>Example 1:</strong> Before switching a workstation from processing '
        'SECRET data to UNCLASSIFIED data, follow your approved sanitization procedure: '
        'clear memory, flush caches, and verify no residual classified data remains using '
        'approved tools.</p>'
        '<p><strong>Example 2:</strong> On shared printers that handle documents at multiple '
        'classification levels, configure the device to purge its internal memory and print '
        'queue completely between classification level changes, and display the current '
        'operating level on the printer console.</p>'
    ),

    "sc-5": (
        '<p>Denial-of-service (DoS) protection means making sure your systems stay available '
        'even when someone tries to overwhelm them with traffic or requests. You need to '
        'both detect and limit the effects of these attacks.</p>'
        '<p><strong>Example 1:</strong> Place a web application firewall (WAF) like AWS WAF '
        'or Cloudflare in front of your public-facing websites. Configure rate limiting to '
        'cap requests per IP address and enable DDoS protection rules that automatically '
        'block traffic patterns that match known attack signatures.</p>'
        '<p><strong>Example 2:</strong> On your perimeter firewall (Palo Alto, Fortinet), '
        'enable flood protection settings — SYN flood thresholds, ICMP rate limiting, and '
        'UDP flood detection. Set alerts in your SIEM to notify your team when traffic '
        'volumes exceed normal baselines by more than 200 percent.</p>'
    ),

    "sc-5-1": (
        '<p>This enhancement prevents your own systems from being used as launch platforms '
        'for denial-of-service attacks against other organizations. If an attacker compromises '
        'your network, they should not be able to use your bandwidth to attack others.</p>'
        '<p><strong>Example 1:</strong> Configure egress filtering on your firewall to block '
        'outbound traffic with spoofed source IP addresses (BCP38/BCP84). This prevents your '
        'network from being used in amplification attacks.</p>'
        '<p><strong>Example 2:</strong> Use your endpoint protection platform (like Microsoft '
        'Defender for Endpoint) to detect and block botnet command-and-control communications. '
        'If a compromised workstation tries to participate in a DDoS botnet, the agent '
        'blocks the outbound traffic and alerts your SOC.</p>'
    ),

    "sc-5-2": (
        '<p>This enhancement focuses on having enough capacity, bandwidth, and redundancy to '
        'survive a denial-of-service attack. The goal is to absorb the attack rather than '
        'go offline.</p>'
        '<p><strong>Example 1:</strong> Deploy your critical web applications behind a CDN '
        'like Cloudflare or Akamai that can absorb massive traffic spikes. The CDN has far '
        'more bandwidth than any single attacker, so your origin servers stay available.</p>'
        '<p><strong>Example 2:</strong> Set up redundant DNS servers with different providers '
        '(for example, Route 53 and Cloudflare DNS). If one DNS provider is attacked, the '
        'other continues resolving your domain names so customers can still reach you.</p>'
    ),

    "sc-5-3": (
        '<p>You need to actively monitor for denial-of-service attacks and detect them early '
        'so you can respond before services go down completely.</p>'
        '<p><strong>Example 1:</strong> Configure your SIEM (Splunk, Sentinel) to alert on '
        'sudden traffic spikes — for example, if inbound connections per second exceed three '
        'times your normal baseline. Create a dashboard showing real-time traffic volume by '
        'source country and protocol.</p>'
        '<p><strong>Example 2:</strong> Enable NetFlow or sFlow on your core switches and '
        'send the data to a flow analyzer. Tools like SolarWinds NTA or ntopng can detect '
        'volumetric attacks in real time and automatically trigger mitigation rules on your '
        'upstream router.</p>'
    ),

    "sc-6": (
        '<p>Resource availability means making sure critical system resources — CPU, memory, '
        'bandwidth, storage — are allocated so that one runaway process or user cannot '
        'starve others.</p>'
        '<p><strong>Example 1:</strong> Use Windows Resource Manager or Linux cgroups to set '
        'CPU and memory limits per application. Your critical database server gets a guaranteed '
        'minimum allocation so a misbehaving batch job cannot consume all available resources.</p>'
        '<p><strong>Example 2:</strong> On your virtualization platform (VMware, Hyper-V), '
        'configure resource reservations and limits for each VM. Give your domain controllers '
        'and security tools guaranteed CPU and memory reservations so they keep running even '
        'when application VMs spike to 100 percent utilization.</p>'
    ),

    "sc-7": (
        '<p>Boundary protection is about controlling what traffic flows in and out of your '
        'network and between internal network segments. Every connection point is a potential '
        'entry for attackers, so each one needs monitoring and filtering.</p>'
        '<p><strong>Example 1:</strong> Deploy a next-generation firewall (Palo Alto, Fortinet) '
        'at your network perimeter with rules that deny all traffic by default and only allow '
        'specific, documented flows. Enable logging for all allowed and denied connections '
        'and forward those logs to your SIEM.</p>'
        '<p><strong>Example 2:</strong> Segment your internal network into VLANs — one for '
        'workstations, one for servers, one for management, one for guests. Use access control '
        'lists on your layer-3 switches to restrict which VLANs can talk to each other. Your '
        'guest WiFi should never be able to reach your server VLAN.</p>'
    ),

    "sc-7-1": (
        '<p>Publicly accessible systems (web servers, email gateways) must sit on a physically '
        'separate network subnetwork from your internal systems. This is the classic DMZ '
        'architecture.</p>'
        '<p><strong>Example 1:</strong> Place your public web server on a DMZ segment with its '
        'own firewall interface. The firewall allows inbound HTTP/HTTPS from the internet to '
        'the DMZ but blocks all direct traffic from the internet to the internal network. The '
        'web server can make limited, specific connections to internal databases.</p>'
        '<p><strong>Example 2:</strong> Put your email gateway (Exchange Edge Transport or '
        'a Barracuda appliance) in the DMZ. Internet email flows into the DMZ, the gateway '
        'scans for malware and spam, then forwards clean mail to the internal Exchange server. '
        'No external mail server ever touches your internal network directly.</p>'
    ),

    "sc-7-2": (
        '<p>Systems that the public can access must not sit on the same network segment as '
        'your internal systems. Public-facing services get their own isolated zone.</p>'
        '<p><strong>Example 1:</strong> Host your company website on a cloud platform (Azure '
        'App Service, AWS) or in a DMZ completely separated from your corporate LAN. If the '
        'website is compromised, the attacker has no direct path to your internal file servers '
        'or Active Directory.</p>'
        '<p><strong>Example 2:</strong> If you must host a customer portal on-premises, place '
        'it on a dedicated VLAN with strict firewall rules. The portal server cannot initiate '
        'connections to any internal system — it can only respond to specific API calls from '
        'an internal application server through a tightly controlled firewall rule.</p>'
    ),

    "sc-7-3": (
        '<p>Limit the number of network access points — every connection into your network '
        'is a door that needs to be guarded. Fewer doors mean fewer opportunities for '
        'attackers and easier monitoring.</p>'
        '<p><strong>Example 1:</strong> Consolidate your internet connections to a single, '
        'well-monitored point with a next-gen firewall, IDS/IPS, and full packet logging. '
        'Eliminate any rogue internet connections that departments may have set up on their '
        'own, such as personal hotspots or unauthorized cable modems.</p>'
        '<p><strong>Example 2:</strong> For remote access, funnel all VPN connections through '
        'a single VPN gateway (like Cisco AnyConnect or GlobalProtect) rather than having '
        'multiple VPN entry points. This gives you one place to enforce MFA, monitor sessions, '
        'and apply security policies.</p>'
    ),

    "sc-7-4": (
        '<p>When you use external telecom services (internet, leased lines, MPLS), you need '
        'a documented plan for how those connections are protected and what happens if the '
        'provider is compromised.</p>'
        '<p><strong>Example 1:</strong> Document all your ISP and telecom provider connections '
        'in a network diagram. For each connection, specify the encryption used (IPsec VPN, '
        'TLS), the firewall rules applied, and the provider&apos;s SLA for uptime and security '
        'incident notification.</p>'
        '<p><strong>Example 2:</strong> If you use an MPLS circuit from a telecom provider, '
        'layer your own encryption (IPsec tunnel) on top of it rather than trusting the '
        'provider&apos;s network security. This way, even if the provider&apos;s infrastructure '
        'is compromised, your data remains encrypted.</p>'
    ),

    "sc-7-5": (
        '<p>Your firewall rules should start with "deny all" and only add specific "allow" '
        'rules for traffic you have explicitly approved. This is the principle of least '
        'privilege applied to network traffic.</p>'
        '<p><strong>Example 1:</strong> On your perimeter firewall, set the default rule to '
        'deny all inbound and outbound traffic. Then add specific allow rules for each '
        'business need — HTTPS outbound for web browsing, SMTP to your email provider, VPN '
        'for remote workers. Each rule should reference a change request with business '
        'justification.</p>'
        '<p><strong>Example 2:</strong> On Windows endpoints, configure the Windows Firewall '
        'via GPO to block all inbound connections by default. Only allow specific exceptions '
        'like your management tools (SCCM, remote desktop from admin VLAN) and security '
        'agents. Log all blocked connections for review.</p>'
    ),

    "sc-7-6": (
        '<p>When a firewall or boundary protection device fails, it must fail in a secure '
        'state — either blocking all traffic (fail-closed) or alerting immediately so '
        'administrators can respond.</p>'
        '<p><strong>Example 1:</strong> Configure your perimeter firewall for fail-closed '
        'operation. If the firewall software crashes or the device loses power, no traffic '
        'passes through. Deploy a high-availability pair so the standby unit takes over '
        'within seconds.</p>'
        '<p><strong>Example 2:</strong> Set up SNMP traps and syslog alerts from your '
        'firewall to your SIEM so that any device failure — hardware fault, process crash, '
        'HA failover — triggers an immediate notification to your security team with a '
        'documented response procedure.</p>'
    ),

    "sc-7-7": (
        '<p>Split tunneling on VPN allows remote workers to access the internet directly '
        'while also connected to your corporate network. This creates a bypass around your '
        'perimeter security. This control says to prevent or restrict it.</p>'
        '<p><strong>Example 1:</strong> Configure your VPN (Cisco AnyConnect, GlobalProtect) '
        'to force full-tunnel mode. All traffic from the remote device routes through your '
        'corporate firewall and web proxy — no direct internet access. This ensures the '
        'same security filtering applies whether the user is in the office or remote.</p>'
        '<p><strong>Example 2:</strong> If full-tunnel creates performance problems, use '
        'Microsoft 365 split-tunnel exceptions only for trusted M365 endpoints (as Microsoft '
        'recommends) while routing all other traffic through the corporate tunnel. Document '
        'this decision and ensure your endpoint protection still monitors direct connections.</p>'
    ),

    "sc-7-8": (
        '<p>Outbound web traffic from your users should route through an authenticated proxy '
        'server that can inspect, filter, and log the traffic before it reaches the internet.</p>'
        '<p><strong>Example 1:</strong> Deploy a web proxy (Zscaler, Squid, or Blue Coat) that '
        'requires user authentication before allowing internet access. The proxy logs every '
        'URL visited, blocks known malicious sites, and prevents access to unauthorized '
        'categories like file sharing or anonymizers.</p>'
        '<p><strong>Example 2:</strong> Configure a GPO to set the proxy server address on all '
        'domain-joined workstations and prevent users from changing proxy settings. Use WPAD '
        'or PAC files to route traffic through the proxy automatically. The proxy authenticates '
        'users via Kerberos against Active Directory.</p>'
    ),

    "sc-7-9": (
        '<p>Your network boundary devices should detect and block outgoing traffic that looks '
        'threatening — like connections to known command-and-control servers, data exfiltration '
        'attempts, or outbound scanning.</p>'
        '<p><strong>Example 1:</strong> Enable threat intelligence feeds on your firewall '
        '(Palo Alto WildFire, Fortinet FortiGuard) that automatically block outbound '
        'connections to known malicious IP addresses and domains. Update these feeds '
        'automatically at least daily.</p>'
        '<p><strong>Example 2:</strong> Configure your IDS/IPS (Snort, Suricata) to monitor '
        'outbound traffic for indicators of compromise — DNS queries to dynamic DNS providers, '
        'large outbound data transfers to foreign IP addresses, or encoded data in HTTP '
        'headers that suggest command-and-control traffic.</p>'
    ),

    "sc-7-10": (
        '<p>Data exfiltration prevention means stopping sensitive data from leaving your '
        'network through unauthorized channels — encrypted tunnels, steganography, covert '
        'channels, or simple file uploads to cloud storage.</p>'
        '<p><strong>Example 1:</strong> Deploy a Data Loss Prevention (DLP) solution at your '
        'network boundary that inspects outbound traffic for patterns matching CUI, PII, or '
        'other sensitive data. Microsoft Purview DLP can scan outbound email and file uploads '
        'and block transfers that violate your policies.</p>'
        '<p><strong>Example 2:</strong> On your firewall, block outbound DNS over HTTPS (DoH) '
        'and DNS over TLS (DoT) to prevent DNS tunneling as an exfiltration channel. Force '
        'all DNS through your internal DNS servers where you can monitor queries for '
        'suspicious patterns like unusually long subdomain names.</p>'
    ),

    "sc-7-11": (
        '<p>Inbound traffic restrictions go beyond basic firewall rules — you only allow '
        'incoming communications from authorized sources and for authorized purposes.</p>'
        '<p><strong>Example 1:</strong> On your perimeter firewall, create explicit allow '
        'rules for each inbound service. Your web server only accepts HTTPS from the CDN. '
        'Your VPN gateway only accepts connections from specific IP ranges or with valid '
        'certificates. Everything else is denied and logged.</p>'
        '<p><strong>Example 2:</strong> Use Azure Network Security Groups or AWS Security '
        'Groups to restrict inbound traffic to your cloud workloads. Only allow SSH/RDP '
        'from your corporate IP range, HTTPS from your load balancer, and nothing else. '
        'Review these rules quarterly.</p>'
    ),

    "sc-7-12": (
        '<p>Host-based boundary protection means running firewall and filtering software on '
        'individual servers and workstations, not just relying on network firewalls. This '
        'provides defense-in-depth.</p>'
        '<p><strong>Example 1:</strong> Use GPO to enable and configure Windows Defender '
        'Firewall on every domain-joined machine. Define inbound and outbound rules that '
        'match your network security policy. Block all inbound connections by default and '
        'only allow specific management ports from your admin subnet.</p>'
        '<p><strong>Example 2:</strong> Deploy Microsoft Defender for Endpoint or CrowdStrike '
        'on every server and workstation. These agents enforce host-level network protection, '
        'detect lateral movement attempts, and can isolate compromised machines from the '
        'network in seconds.</p>'
    ),

    "sc-7-13": (
        '<p>Security tools — SIEM, vulnerability scanners, forensic workstations — should be '
        'on their own isolated network segment. If an attacker compromises your production '
        'environment, they should not be able to reach and disable your security monitoring.</p>'
        '<p><strong>Example 1:</strong> Place your SIEM (Splunk, Sentinel), vulnerability '
        'scanner (Nessus/ACAS), and network monitoring tools on a dedicated management VLAN. '
        'Only security team workstations can access this VLAN, and firewall rules prevent '
        'any production system from initiating connections to the security tools.</p>'
        '<p><strong>Example 2:</strong> Store security tool backups and configuration files '
        'on a separate storage system that is not accessible from the production network. '
        'If an attacker wipes production servers, your SIEM data and security baselines '
        'remain intact for forensic investigation.</p>'
    ),

    "sc-7-14": (
        '<p>This control protects against someone physically plugging an unauthorized device '
        'into your network — a rogue switch, a wireless access point, or a network tap.</p>'
        '<p><strong>Example 1:</strong> Enable 802.1X port-based network access control on '
        'your switches. Only devices with valid machine certificates or credentials can '
        'connect to the network. Unknown devices are placed on a quarantine VLAN or '
        'blocked entirely.</p>'
        '<p><strong>Example 2:</strong> Disable unused switch ports and lock server room '
        'patch panels. Conduct periodic physical inspections to look for unauthorized '
        'devices connected to your network. Use your switch management console to alert '
        'on new MAC addresses appearing on ports that should have known devices.</p>'
    ),

    "sc-7-15": (
        '<p>Privileged network access — administrator remote sessions, management plane '
        'connections — should go through dedicated, secured network paths that are separate '
        'from regular user traffic.</p>'
        '<p><strong>Example 1:</strong> Set up a dedicated management VLAN for all admin '
        'access to servers, network devices, and security tools. RDP, SSH, and HTTPS '
        'management connections are only allowed from this management VLAN. Admin workstations '
        'have two network connections — one for regular work, one for management.</p>'
        '<p><strong>Example 2:</strong> Deploy a Privileged Access Management (PAM) solution '
        'like CyberArk or Azure AD PIM. All privileged sessions are brokered through the PAM '
        'gateway, which records the session, enforces MFA, and limits the duration of '
        'elevated access.</p>'
    ),

    "sc-7-16": (
        '<p>This control prevents external parties from discovering what systems, services, '
        'and network components you have. The less attackers know about your infrastructure, '
        'the harder it is to target you.</p>'
        '<p><strong>Example 1:</strong> Configure your external DNS to only expose records '
        'that are absolutely necessary — your mail server MX record, your website A record. '
        'Remove any internal hostnames, HINFO records, or TXT records that reveal software '
        'versions or internal naming conventions.</p>'
        '<p><strong>Example 2:</strong> On your web servers, suppress version banners. '
        'Configure Apache to set ServerTokens to "Prod" and ServerSignature to "Off." '
        'On IIS, remove the X-Powered-By header. On your firewall, disable ICMP responses '
        'to external probes so port scans reveal as little as possible.</p>'
    ),

    "sc-7-17": (
        '<p>Your boundary devices should automatically enforce protocol compliance — rejecting '
        'malformed packets, invalid protocol sequences, or unexpected data formats before '
        'they reach internal systems.</p>'
        '<p><strong>Example 1:</strong> Enable protocol validation on your next-gen firewall. '
        'Palo Alto&apos;s App-ID, for example, decodes application protocols and blocks traffic '
        'that claims to be HTTP but contains non-HTTP data (like tunneled traffic or '
        'command-and-control communications).</p>'
        '<p><strong>Example 2:</strong> Deploy a WAF (ModSecurity, AWS WAF) in front of your '
        'web applications that validates HTTP requests against RFC standards. Malformed '
        'requests, oversized headers, or unusual encoding are automatically blocked before '
        'reaching the application server.</p>'
    ),

    "sc-7-18": (
        '<p>When a boundary protection device fails, it must default to a secure state — '
        'blocking all traffic rather than allowing everything through. This is "fail secure" '
        'or "fail closed."</p>'
        '<p><strong>Example 1:</strong> Configure your firewall in fail-closed mode so that '
        'if the inspection engine crashes, all traffic is blocked rather than passed through '
        'uninspected. Pair this with a high-availability setup so the standby firewall takes '
        'over within seconds.</p>'
        '<p><strong>Example 2:</strong> Test your fail-secure configuration regularly. During '
        'a maintenance window, simulate a firewall process crash and verify that traffic '
        'stops flowing (fail-closed) rather than being passed through (fail-open). Document '
        'the test results.</p>'
    ),

    "sc-7-19": (
        '<p>Block network traffic from internal hosts that have not been configured according '
        'to your organization&apos;s standards. If a device is not properly managed, it should '
        'not be allowed to communicate.</p>'
        '<p><strong>Example 1:</strong> Use 802.1X with Microsoft NPS (Network Policy Server) '
        'to check device health before granting network access. Machines that lack current '
        'antivirus definitions, are missing patches, or are not domain-joined get placed on '
        'a remediation VLAN with limited access.</p>'
        '<p><strong>Example 2:</strong> Deploy Microsoft Intune compliance policies for all '
        'endpoints. Devices that do not meet compliance requirements (encryption enabled, '
        'firewall on, up-to-date OS) are automatically blocked from accessing corporate '
        'resources through Conditional Access policies.</p>'
    ),

    "sc-7-20": (
        '<p>Dynamic isolation means the system can automatically quarantine compromised or '
        'suspicious network segments in real time without waiting for an administrator to '
        'manually reconfigure the network.</p>'
        '<p><strong>Example 1:</strong> Configure Microsoft Defender for Endpoint to '
        'automatically isolate compromised machines from the network. When a high-severity '
        'threat is detected, the agent blocks all network connections except communication '
        'with the Defender cloud service, cutting the attacker off instantly.</p>'
        '<p><strong>Example 2:</strong> Use Cisco ISE or Aruba ClearPass to dynamically '
        'move compromised devices to a quarantine VLAN based on alerts from your IDS/IPS. '
        'When Suricata detects command-and-control traffic from a host, ISE automatically '
        'changes that port&apos;s VLAN assignment.</p>'
    ),

    "sc-7-21": (
        '<p>Critical system components should be physically or logically isolated from each '
        'other so that a compromise of one component does not give an attacker access to '
        'everything.</p>'
        '<p><strong>Example 1:</strong> Put your database servers on a dedicated VLAN that '
        'only your application servers can reach. Web servers sit on another VLAN. Management '
        'interfaces sit on a third. Firewall rules between VLANs enforce strict, documented '
        'access paths.</p>'
        '<p><strong>Example 2:</strong> In Azure or AWS, deploy different application tiers '
        'in separate subnets with Network Security Groups/Security Groups between them. '
        'Your web tier can talk to the app tier on port 443, the app tier can talk to the '
        'database tier on port 1433, but no other paths are allowed.</p>'
    ),

    "sc-7-22": (
        '<p>When connecting to different security domains (classified vs. unclassified, '
        'production vs. development), each domain gets its own separate subnet with '
        'controlled interconnections.</p>'
        '<p><strong>Example 1:</strong> If your organization processes both CUI and public '
        'data, place CUI systems on a dedicated subnet with stricter firewall rules, stronger '
        'encryption requirements, and separate logging. Public-facing systems sit on a '
        'completely different subnet with their own security controls.</p>'
        '<p><strong>Example 2:</strong> For development and production environments, use '
        'separate VLANs with no direct routing between them. Developers cannot access '
        'production databases from their development subnet. Code moves between environments '
        'only through an approved CI/CD pipeline.</p>'
    ),

    "sc-7-23": (
        '<p>When your boundary devices detect malformed or invalid protocol data, they '
        'should not send detailed error messages back to the sender. Detailed errors help '
        'attackers refine their techniques.</p>'
        '<p><strong>Example 1:</strong> Configure your WAF to return generic "403 Forbidden" '
        'or "400 Bad Request" responses when it blocks malicious input. Never include details '
        'about which specific rule triggered the block or what the WAF expected to see.</p>'
        '<p><strong>Example 2:</strong> On your mail gateway, configure it to silently drop '
        'or quarantine emails that fail protocol validation rather than sending bounce '
        'messages that reveal your mail server software, version, or internal hostnames.</p>'
    ),

    "sc-7-24": (
        '<p>When personally identifiable information (PII) crosses network boundaries, extra '
        'protections must be in place — encryption, access controls, and monitoring — to '
        'prevent unauthorized disclosure.</p>'
        '<p><strong>Example 1:</strong> Configure Microsoft Purview DLP policies to detect '
        'and block outbound email or file transfers containing PII (Social Security numbers, '
        'dates of birth, financial data). Set policies to encrypt PII automatically if it '
        'must be transmitted externally.</p>'
        '<p><strong>Example 2:</strong> On your firewall, create specific logging rules for '
        'traffic to and from systems that store PII (HR databases, patient records). Forward '
        'these logs to your SIEM with alerts for unusual data transfer volumes that could '
        'indicate a breach.</p>'
    ),

    "sc-7-25": (
        '<p>Connections between unclassified national security systems require special '
        'approval and protection measures beyond standard network connections.</p>'
        '<p><strong>Example 1:</strong> Document all connections between your unclassified '
        'NSS and other networks in an Interconnection Security Agreement (ISA). Specify the '
        'encryption, firewall rules, and monitoring required for each connection. Get the '
        'authorizing official to approve each ISA.</p>'
        '<p><strong>Example 2:</strong> Deploy dedicated firewall rules and IDS monitoring '
        'for NSS interconnections. Log all traffic crossing these boundaries and review '
        'logs monthly for unauthorized access patterns or policy violations.</p>'
    ),

    "sc-7-26": (
        '<p>Connections involving classified national security systems have the strictest '
        'requirements — typically requiring NSA-approved encryption and cross-domain solutions.</p>'
        '<p><strong>Example 1:</strong> Use an NSA-approved cross-domain solution (CDS) for '
        'any data exchange between classified and unclassified networks. The CDS inspects '
        'and sanitizes all data transfers according to content filtering rules approved by '
        'the designated approving authority.</p>'
        '<p><strong>Example 2:</strong> Classified network connections must use NSA Type 1 '
        'encryption devices. Document these connections in your System Security Plan and '
        'get explicit authorization from the appropriate government authority before '
        'establishing any new connection.</p>'
    ),

    "sc-7-27": (
        '<p>Connections between your systems and other unclassified non-national-security '
        'networks must be documented, approved, and monitored — even though the data is '
        'not classified.</p>'
        '<p><strong>Example 1:</strong> Maintain a list of all external network connections '
        '— partner VPNs, vendor remote access, cloud service connections. Each one should '
        'have an ISA or MOU that documents what data flows across the connection and what '
        'security controls protect it.</p>'
        '<p><strong>Example 2:</strong> Review your external connections quarterly. Verify '
        'that each connection is still needed, that the security controls described in the '
        'ISA are still in place, and that the other party is still meeting their security '
        'obligations. Remove connections that are no longer needed.</p>'
    ),

    "sc-7-28": (
        '<p>Any connection to a public network (the internet) needs extra protection because '
        'public networks are inherently untrusted.</p>'
        '<p><strong>Example 1:</strong> Route all internet traffic through a secure web '
        'gateway that performs TLS inspection, malware scanning, and URL filtering. No '
        'system should connect directly to the internet without passing through your '
        'security stack.</p>'
        '<p><strong>Example 2:</strong> For systems that must be internet-accessible, use '
        'a reverse proxy or load balancer as the public-facing endpoint. The actual '
        'application servers sit behind the proxy on a private network segment and are '
        'never directly exposed to the internet.</p>'
    ),

    "sc-7-29": (
        '<p>Use separate subnets to isolate different system functions — a web tier, an '
        'application tier, a database tier, a management tier — so a compromise in one '
        'area does not spread to others.</p>'
        '<p><strong>Example 1:</strong> In your data center, create separate VLANs for '
        'each functional tier. Use ACLs on your core switch to control traffic between '
        'tiers. The web tier can only reach the application tier on specific ports, and '
        'the application tier can only reach the database tier on the database port.</p>'
        '<p><strong>Example 2:</strong> In AWS, deploy a three-tier architecture with '
        'public subnets for load balancers, private subnets for application servers, and '
        'isolated subnets for databases with no internet gateway. Use Security Groups to '
        'enforce least-privilege network access between tiers.</p>'
    ),

    "sc-8": (
        '<p>Data in transit — emails, file transfers, web traffic, database queries — must '
        'be protected from eavesdropping and tampering. If someone intercepts your network '
        'traffic, they should not be able to read or modify it.</p>'
        '<p><strong>Example 1:</strong> Require TLS 1.2 or higher for all web traffic by '
        'configuring your web servers and load balancers to reject connections using older '
        'protocols. Use a GPO to configure Windows systems to disable TLS 1.0 and 1.1 in '
        'the registry.</p>'
        '<p><strong>Example 2:</strong> In Microsoft 365, enable encryption for all email '
        'in transit by verifying that your Exchange Online connectors enforce TLS. Go to '
        'Exchange Admin Center > Mail Flow > Connectors and confirm that "Reject if TLS '
        'is not available" is enabled for partner organizations handling sensitive data.</p>'
    ),

    "sc-8-1": (
        '<p>This enhancement specifically requires using cryptographic mechanisms — not just '
        'any protection — to secure data in transit. Encryption is mandatory, not optional.</p>'
        '<p><strong>Example 1:</strong> Configure IPsec VPN tunnels between your office '
        'locations using AES-256 encryption. All site-to-site traffic is encrypted at the '
        'network layer, protecting everything from file shares to database replication '
        'without requiring application-level changes.</p>'
        '<p><strong>Example 2:</strong> Enable BitLocker and require encrypted connections '
        'for all Remote Desktop sessions. Configure a GPO under Computer Configuration > '
        'Administrative Templates > Windows Components > Remote Desktop Services to set '
        '"Require use of specific security layer for remote (RDP) connections" to SSL.</p>'
    ),

    "sc-8-2": (
        '<p>Protect data not just while it is moving across the network, but also at the '
        'sending and receiving endpoints before and after transmission. Data should be '
        'encrypted before it hits the wire and remain protected after it arrives.</p>'
        '<p><strong>Example 1:</strong> Use Microsoft Purview Message Encryption (formerly '
        'OME) so emails are encrypted before they leave the sender&apos;s mailbox and remain '
        'encrypted until the recipient decrypts them. The data is protected at both ends, '
        'not just in transit.</p>'
        '<p><strong>Example 2:</strong> For file transfers, encrypt files with 7-Zip AES-256 '
        'before uploading them to a file sharing service. The file is protected at the source '
        'before transmission, during transit, and at rest on the destination server until '
        'the recipient decrypts it.</p>'
    ),

    "sc-8-3": (
        '<p>Protect the external metadata of messages — headers, routing information, '
        'addresses — not just the message content. Metadata can reveal sensitive information '
        'about who is communicating with whom.</p>'
        '<p><strong>Example 1:</strong> Use a VPN for all communications so that network '
        'observers cannot see the source and destination of individual connections. All '
        'traffic appears as encrypted VPN traffic to a single endpoint, hiding the actual '
        'communication patterns inside.</p>'
        '<p><strong>Example 2:</strong> Configure your email system to use TLS for server-to-'
        'server connections and strip internal routing headers from outbound email. Your '
        'Exchange transport rules can remove X-headers that reveal internal server names '
        'and IP addresses before messages leave your organization.</p>'
    ),

    "sc-8-4": (
        '<p>Conceal or randomize communication patterns to make it harder for an adversary '
        'to perform traffic analysis — figuring out what you are doing based on when and '
        'how much you communicate.</p>'
        '<p><strong>Example 1:</strong> Use traffic padding on your VPN tunnels to maintain '
        'a constant traffic volume. Whether your users are busy or idle, the tunnel sends '
        'the same amount of encrypted data, making it impossible for observers to infer '
        'activity levels from traffic volume.</p>'
        '<p><strong>Example 2:</strong> Randomize the timing of automated processes like '
        'backup transfers, patch downloads, and SIEM log forwarding. Instead of running '
        'backups at exactly 2:00 AM every night (a predictable pattern), add a random '
        'delay of 0-60 minutes.</p>'
    ),

    "sc-8-5": (
        '<p>A protected distribution system (PDS) is a physically secured cable run — '
        'conduit, locked trays, or alarmed pathways — used to carry classified or sensitive '
        'data without encryption, because the physical path itself is protected.</p>'
        '<p><strong>Example 1:</strong> Install network cables carrying sensitive data in '
        'locked, alarmed conduit that is inspected regularly. The conduit runs from your '
        'secure server room to your secure operations center with no accessible junction '
        'points in between.</p>'
        '<p><strong>Example 2:</strong> For classified environments, follow the CNSSI 7003 '
        'standard for PDS installation. Maintain a PDS log documenting installation, '
        'inspections, and any maintenance. Conduct visual inspections of the conduit '
        'at defined intervals to check for tampering.</p>'
    ),

    "sc-9": (
        '<p>This control (withdrawn in Rev 5) has been incorporated into SC-8. See SC-8 '
        'for transmission confidentiality requirements.</p>'
        '<p><strong>Example 1:</strong> Refer to SC-8 — require TLS 1.2 or higher for all '
        'web-based communications to protect data confidentiality in transit.</p>'
        '<p><strong>Example 2:</strong> Refer to SC-8 — use IPsec VPN tunnels for '
        'site-to-site connections to ensure all inter-office traffic is encrypted and '
        'confidential.</p>'
    ),

    "sc-10": (
        '<p>Network sessions should automatically disconnect after a period of inactivity '
        'or at the end of a session. Idle connections are an invitation for session hijacking.</p>'
        '<p><strong>Example 1:</strong> Configure your VPN gateway to disconnect idle '
        'sessions after 30 minutes of inactivity. In Cisco AnyConnect, set the "idle '
        'timeout" to 1800 seconds. Users must re-authenticate to reconnect.</p>'
        '<p><strong>Example 2:</strong> Use a GPO to set RDP session timeouts. Under '
        'Computer Configuration > Administrative Templates > Windows Components > Remote '
        'Desktop Services > Session Time Limits, set idle session limits to 15-30 minutes '
        'and disconnected session limits to end the session after 1 hour.</p>'
    ),

    "sc-11": (
        '<p>A trusted path provides a secure, verifiable communication channel between '
        'the user and the system for security-critical operations like login. The user '
        'must be confident they are talking to the real system, not a spoof.</p>'
        '<p><strong>Example 1:</strong> Windows Secure Attention Sequence (Ctrl+Alt+Delete) '
        'is a trusted path — it guarantees the login screen is the real Windows login and '
        'not a fake login screen planted by malware. Require Ctrl+Alt+Delete for login '
        'via GPO under Interactive Logon settings.</p>'
        '<p><strong>Example 2:</strong> For web applications, use HTTPS with extended '
        'validation (EV) certificates or certificate pinning so users can verify they are '
        'communicating with the genuine application and not a phishing site performing a '
        'man-in-the-middle attack.</p>'
    ),

    "sc-11-1": (
        '<p>The trusted path must provide irrefutable proof that both parties in a '
        'communication are who they claim to be — neither side can deny the exchange.</p>'
        '<p><strong>Example 1:</strong> Use mutual TLS (mTLS) for critical system-to-system '
        'communications. Both the client and server present certificates, so neither side '
        'can deny the connection. Log the certificate details in your SIEM for audit '
        'purposes.</p>'
        '<p><strong>Example 2:</strong> Implement digital signatures on all administrative '
        'commands sent to critical infrastructure. The signature proves the command came from '
        'an authorized administrator and was not altered in transit. Store signed command '
        'logs for non-repudiation.</p>'
    ),

    "sc-12": (
        '<p>Cryptographic keys are the foundation of all your encryption — if keys are '
        'poorly managed, your encryption is worthless. This control requires a formal '
        'process for creating, distributing, storing, rotating, and destroying keys.</p>'
        '<p><strong>Example 1:</strong> Use Active Directory Certificate Services (AD CS) '
        'as your internal PKI to issue, renew, and revoke certificates for servers and users. '
        'Configure auto-enrollment via GPO so certificates are automatically issued and '
        'renewed. Store the CA root key on an offline, air-gapped system.</p>'
        '<p><strong>Example 2:</strong> For cloud environments, use Azure Key Vault or AWS '
        'KMS to manage encryption keys. These services handle key generation, rotation, '
        'and access control. Configure automatic key rotation every 90 days and audit all '
        'key access through the service&apos;s built-in logging.</p>'
    ),

    "sc-12-1": (
        '<p>Maintain the availability of your cryptographic keys — if you lose your keys, '
        'you lose access to all your encrypted data. Key backup and recovery are essential.</p>'
        '<p><strong>Example 1:</strong> Back up your BitLocker recovery keys to Active '
        'Directory. If a user forgets their PIN or a TPM fails, the recovery key stored '
        'in AD lets you unlock the drive. Verify backups are working by spot-checking '
        'that recovery keys are present for all encrypted machines.</p>'
        '<p><strong>Example 2:</strong> For your certificate authority, create an encrypted '
        'backup of the CA private key and store it in a physical safe at a secure offsite '
        'location. Document the recovery procedure and test it annually — you need to know '
        'you can restore the CA if your primary server is destroyed.</p>'
    ),

    "sc-12-2": (
        '<p>Symmetric encryption keys (the same key encrypts and decrypts) require special '
        'handling because anyone with the key can both read and create encrypted data.</p>'
        '<p><strong>Example 1:</strong> Use FIPS 140-2 validated modules to generate symmetric '
        'keys (like AES-256 keys for BitLocker or database TDE). Never generate keys with '
        'custom or homegrown random number generators — use the OS cryptographic provider.</p>'
        '<p><strong>Example 2:</strong> For symmetric keys shared between systems (like a '
        'shared encryption key for a partner data exchange), distribute the key through an '
        'out-of-band channel — for example, a phone call to verify the key after sending '
        'it via encrypted email. Never send the key and the encrypted data through the '
        'same channel.</p>'
    ),

    "sc-12-3": (
        '<p>Asymmetric keys (public/private key pairs) are used for digital signatures, key '
        'exchange, and certificate-based authentication. They require their own management '
        'procedures.</p>'
        '<p><strong>Example 1:</strong> Generate RSA key pairs of at least 2048 bits (4096 '
        'preferred) using your PKI. Issue certificates that bind the public key to a verified '
        'identity. Configure certificate lifetimes — typically one to two years for user '
        'certificates and three to five years for CA certificates.</p>'
        '<p><strong>Example 2:</strong> Use your ADCS certificate authority to manage the '
        'full lifecycle of asymmetric keys — generation, issuance, renewal, revocation. '
        'Publish your certificate revocation list (CRL) and configure OCSP responders so '
        'systems can verify certificates in real time.</p>'
    ),

    "sc-12-4": (
        '<p>PKI certificates must be issued by a trusted certificate authority and managed '
        'throughout their lifecycle — from issuance to revocation.</p>'
        '<p><strong>Example 1:</strong> Deploy an internal PKI using Active Directory '
        'Certificate Services. Create certificate templates for different use cases — user '
        'authentication, server TLS, code signing. Use GPO to auto-enroll domain computers '
        'and users for their appropriate certificates.</p>'
        '<p><strong>Example 2:</strong> For public-facing TLS certificates, use a trusted '
        'commercial CA (DigiCert, Let&apos;s Encrypt) and automate renewal with ACME protocol. '
        'Monitor certificate expiration dates with a tool like Keyfactor or a simple script '
        'that alerts 30 days before any certificate expires.</p>'
    ),

    "sc-12-5": (
        '<p>For high-security environments, PKI certificates and private keys should be '
        'stored on hardware tokens (smart cards, HSMs) rather than in software keystores.</p>'
        '<p><strong>Example 1:</strong> Issue CAC/PIV smart cards to users for authentication. '
        'The private key is generated on the card and never leaves the hardware. Users must '
        'insert the card and enter a PIN to authenticate — two factors in one device.</p>'
        '<p><strong>Example 2:</strong> Store your certificate authority&apos;s signing key in '
        'a FIPS 140-2 Level 3 Hardware Security Module (HSM). The HSM performs all signing '
        'operations internally — the private key cannot be exported, copied, or extracted '
        'from the hardware.</p>'
    ),

    "sc-12-6": (
        '<p>Maintain physical control of cryptographic keys — know where they are, who has '
        'access, and ensure they cannot be copied or stolen.</p>'
        '<p><strong>Example 1:</strong> Store backup copies of critical encryption keys on '
        'encrypted USB drives locked in a fireproof safe with dual-person access control. '
        'Maintain a key custodian log showing who accessed the safe, when, and why.</p>'
        '<p><strong>Example 2:</strong> For HSM-based key storage, keep the HSM in a locked '
        'server rack inside a controlled-access server room. Require two authorized personnel '
        'to access the HSM for any key ceremony (key generation, backup, or destruction). '
        'Log all physical access with video recording.</p>'
    ),

    "sc-13": (
        '<p>Use encryption wherever your organization requires confidentiality or integrity '
        'protection — at rest, in transit, for authentication. Do not roll your own '
        'cryptography; use established, validated algorithms.</p>'
        '<p><strong>Example 1:</strong> Use FIPS 140-2 validated cryptographic modules for '
        'all encryption. On Windows, enable FIPS mode via GPO (Computer Configuration > '
        'Windows Settings > Security Settings > Local Policies > Security Options > "System '
        'cryptography: Use FIPS compliant algorithms"). This ensures Windows uses validated '
        'implementations of AES, SHA-256, and RSA.</p>'
        '<p><strong>Example 2:</strong> Configure your VPN, TLS, and disk encryption to use '
        'only approved algorithms — AES-256 for encryption, SHA-256 or SHA-384 for hashing, '
        'RSA-2048+ or ECDSA P-256+ for key exchange. Document these choices in your System '
        'Security Plan.</p>'
    ),

    "sc-13-1": (
        '<p>All cryptography used in the system must be FIPS-validated — meaning the specific '
        'software or hardware module has been tested and certified by an accredited lab.</p>'
        '<p><strong>Example 1:</strong> Verify that your Windows Cryptographic Providers '
        'appear on the NIST Cryptographic Module Validation Program (CMVP) list. Check '
        'the certificate number and ensure it covers the algorithms you are using.</p>'
        '<p><strong>Example 2:</strong> For third-party encryption products (VPN appliances, '
        'database encryption), request the vendor&apos;s FIPS 140-2 or 140-3 validation '
        'certificate before purchasing. Confirm the certificate is current, not expired '
        'or historical.</p>'
    ),

    "sc-13-2": (
        '<p>For national security systems, use NSA-approved (Suite B or CNSA) cryptographic '
        'algorithms and implementations.</p>'
        '<p><strong>Example 1:</strong> Configure classified network VPN concentrators to use '
        'CNSA Suite algorithms — AES-256 for encryption, SHA-384 for hashing, ECDH P-384 '
        'for key exchange. Only use NSA-certified encryption devices (Type 1) for classified '
        'data protection.</p>'
        '<p><strong>Example 2:</strong> For Secret-level communications, deploy NSA-approved '
        'encryptors like the KG-175D (TACLANE) for network encryption. These devices are '
        'certified by NSA and provide government-approved protection for classified data '
        'in transit.</p>'
    ),

    "sc-13-3": (
        '<p>When individuals without formal access approvals need to handle encrypted data '
        '(like IT support staff), ensure the encryption prevents them from accessing the '
        'data content while still allowing them to perform their support tasks.</p>'
        '<p><strong>Example 1:</strong> Use BitLocker with TPM+PIN so IT support staff can '
        'troubleshoot hardware issues and reimage machines without ever seeing the encrypted '
        'data on the drive. The encryption key is bound to the TPM and the authorized '
        'user&apos;s PIN — IT staff do not have the PIN.</p>'
        '<p><strong>Example 2:</strong> For database support, use column-level encryption '
        'with Always Encrypted in SQL Server. Database administrators can manage the '
        'database schema, perform backups, and tune performance without ever seeing the '
        'plaintext values in encrypted columns.</p>'
    ),

    "sc-13-4": (
        '<p>Use digital signatures to verify the authenticity and integrity of critical data, '
        'software, and communications. A valid signature proves the data came from a known '
        'source and has not been tampered with.</p>'
        '<p><strong>Example 1:</strong> Require code signing for all internally developed '
        'scripts and executables. Use a code signing certificate from your internal CA to '
        'sign PowerShell scripts, and configure a GPO to only allow signed scripts to '
        'run (Set-ExecutionPolicy AllSigned).</p>'
        '<p><strong>Example 2:</strong> Enable S/MIME digital signatures in Outlook for '
        'emails containing sensitive directives or approvals. The recipient can verify the '
        'signature to confirm the email actually came from the stated sender and was not '
        'altered in transit.</p>'
    ),

    "sc-14": (
        '<p>This control (withdrawn in Rev 5) has been incorporated into other controls. '
        'The protections for publicly accessible systems are now addressed by AC-2, AC-3, '
        'AC-5, AC-6, SI-3, SI-4, SI-5, SI-7, and SI-10.</p>'
        '<p><strong>Example 1:</strong> For public-facing web servers, implement input '
        'validation (SI-10) and malware protection (SI-3) as described in those respective '
        'controls.</p>'
        '<p><strong>Example 2:</strong> Apply access control (AC-3) and least privilege '
        '(AC-6) to all public-facing systems, ensuring they run with minimal permissions '
        'and only serve their intended function.</p>'
    ),

    "sc-15": (
        '<p>Collaborative computing devices — webcams, microphones, smart displays, '
        'conference room systems — can be used for eavesdropping if not properly controlled. '
        'You need the ability to disable them when not in use.</p>'
        '<p><strong>Example 1:</strong> Use a GPO to disable built-in microphones and cameras '
        'on workstations by default. Users must explicitly enable them through a controlled '
        'process (like requesting temporary access through a self-service portal) before '
        'joining a video call.</p>'
        '<p><strong>Example 2:</strong> In conference rooms with Zoom or Teams Rooms devices, '
        'install physical camera covers and use systems with hardware mute buttons that '
        'physically disconnect the microphone circuit. Train staff to engage the mute/cover '
        'when meetings are not in progress.</p>'
    ),

    "sc-15-1": (
        '<p>Collaborative computing devices must have the ability to be physically or '
        'logically disconnected — not just muted or paused, but truly cut off from '
        'capturing audio or video.</p>'
        '<p><strong>Example 1:</strong> Choose conference room systems that have a hardware '
        'disconnect switch for cameras and microphones. The switch physically breaks the '
        'circuit — software cannot override it. Verify this during procurement.</p>'
        '<p><strong>Example 2:</strong> For laptops, use device manager policies via GPO '
        'to disable webcam and microphone device drivers when not needed. The devices '
        'show as disabled in Device Manager and cannot capture data until an admin '
        're-enables them.</p>'
    ),

    "sc-15-2": (
        '<p>Block collaborative computing devices from sending or receiving unauthorized '
        'traffic — preventing them from being used as covert communication channels.</p>'
        '<p><strong>Example 1:</strong> Place conference room video systems on a dedicated '
        'VLAN with strict firewall rules. They can only communicate with your approved video '
        'conferencing service (Teams, Zoom) and cannot reach the internet or internal '
        'servers for any other purpose.</p>'
        '<p><strong>Example 2:</strong> On endpoint workstations, use application control '
        'policies (AppLocker, WDAC) to restrict which applications can access the camera '
        'and microphone. Only approved conferencing apps (Teams, Zoom) are allowed — '
        'unknown applications cannot access these devices.</p>'
    ),

    "sc-15-3": (
        '<p>In areas where classified or highly sensitive work is performed, collaborative '
        'computing devices with cameras and microphones must be physically removed or '
        'disabled.</p>'
        '<p><strong>Example 1:</strong> In SCIFs or secure work areas, remove all devices '
        'with cameras and microphones — no webcams, no smart speakers, no personal phones. '
        'Use desktop computers without built-in cameras and with microphone jacks physically '
        'disabled or removed.</p>'
        '<p><strong>Example 2:</strong> For classified conference rooms, use hardened '
        'communication equipment that has been inspected and approved by your security '
        'office. Regular commercial video conferencing equipment is prohibited. Post '
        'signs reminding personnel to leave personal electronic devices outside.</p>'
    ),

    "sc-15-4": (
        '<p>When using collaborative computing, every participant in the session must be '
        'clearly visible to all other participants. No hidden observers or undisclosed '
        'listeners.</p>'
        '<p><strong>Example 1:</strong> Configure your Teams or Zoom rooms to display a '
        'participant list that all attendees can see. Disable the ability for participants '
        'to join anonymously — require named accounts for all meeting attendees.</p>'
        '<p><strong>Example 2:</strong> Enable meeting join/leave notifications (audio '
        'chimes and visual alerts) in your conferencing platform so everyone is aware '
        'when someone enters or exits. Disable the option for attendees to lurk without '
        'appearing in the participant list.</p>'
    ),

    "sc-16": (
        '<p>When data moves between systems, its security labels and privacy attributes '
        '(classification level, handling caveats, access restrictions) must travel with it '
        'and be interpreted correctly by the receiving system.</p>'
        '<p><strong>Example 1:</strong> Use Microsoft Purview Information Protection '
        'sensitivity labels. When a document labeled "Confidential" is emailed or shared, '
        'the label travels with the file. The receiving system (Exchange, SharePoint, Teams) '
        'reads the label and enforces the associated protections automatically.</p>'
        '<p><strong>Example 2:</strong> In DoD environments, use data tags in email headers '
        '(X-headers) that indicate the classification level and handling caveats. Your email '
        'gateway reads these tags and applies appropriate routing and encryption rules based '
        'on the data&apos;s sensitivity.</p>'
    ),

    "sc-16-1": (
        '<p>Verify the integrity of security and privacy attributes during transmission — '
        'make sure labels have not been tampered with in transit.</p>'
        '<p><strong>Example 1:</strong> Use digital signatures on sensitivity labels so '
        'receiving systems can verify the label was applied by an authorized source and '
        'has not been modified. Microsoft Purview labels support this natively.</p>'
        '<p><strong>Example 2:</strong> Configure your email gateway to check classification '
        'markings in message headers against a cryptographic hash. If the header has been '
        'altered in transit, the gateway quarantines the message and alerts security.</p>'
    ),

    "sc-16-2": (
        '<p>Implement anti-spoofing mechanisms for security attributes to prevent an attacker '
        'from downgrading or removing classification labels to bypass access controls.</p>'
        '<p><strong>Example 1:</strong> Configure your data classification tool to prevent '
        'users from removing or downgrading sensitivity labels without justification and '
        'approval. In Microsoft Purview, enable "require justification for label downgrade" '
        'so users must explain why they are reducing a document&apos;s sensitivity.</p>'
        '<p><strong>Example 2:</strong> On your mail gateway, reject inbound emails that '
        'claim a lower classification than the content warrants. Use content inspection rules '
        'that flag messages containing classified keywords but carrying unclassified labels.</p>'
    ),

    "sc-16-3": (
        '<p>Bind security attributes to data using cryptographic mechanisms so the attributes '
        'cannot be separated from the data or independently modified.</p>'
        '<p><strong>Example 1:</strong> Use Azure Information Protection (AIP) to apply '
        'encrypted labels that are cryptographically bound to the document content. The '
        'label and its protections cannot be removed without the appropriate decryption '
        'key, even if the file is copied to another system.</p>'
        '<p><strong>Example 2:</strong> Implement HMAC-based integrity checks on data export '
        'files that include both the data and its classification metadata. The receiving '
        'system verifies the HMAC before processing, ensuring the classification has not '
        'been altered.</p>'
    ),

    "sc-17": (
        '<p>If your organization uses PKI certificates (and most do), you need to issue '
        'them from a trusted certificate authority following established policies.</p>'
        '<p><strong>Example 1:</strong> Deploy Active Directory Certificate Services as your '
        'internal PKI. Publish your CA certificate to all domain machines via GPO so they '
        'automatically trust certificates issued by your CA. Create a Certificate Practice '
        'Statement (CPS) that documents how certificates are issued, managed, and revoked.</p>'
        '<p><strong>Example 2:</strong> For external-facing services, use certificates from '
        'a publicly trusted CA. Implement Certificate Transparency (CT) log monitoring so '
        'you are alerted if someone fraudulently obtains a certificate for your domain from '
        'any CA in the world.</p>'
    ),

    "sc-18": (
        '<p>Mobile code — JavaScript, Java applets, ActiveX controls, macros — runs on your '
        'users&apos; machines after being downloaded from somewhere else. You need to control '
        'what mobile code can run and what it can do.</p>'
        '<p><strong>Example 1:</strong> Use a GPO to configure Microsoft Office macro settings: '
        'block macros from the internet, disable macros without notification for standard '
        'users, and only allow macros signed by trusted publishers. This prevents macro-based '
        'malware while still allowing approved business macros.</p>'
        '<p><strong>Example 2:</strong> Configure your web proxy to block downloads of '
        'executable content (Java applets, ActiveX, Flash) from untrusted websites. Use your '
        'browser&apos;s enterprise policies (Edge/Chrome ADMX templates) to disable Java and '
        'ActiveX plugins entirely on standard workstations.</p>'
    ),

    "sc-18-1": (
        '<p>Your systems should be able to identify unacceptable mobile code and take '
        'corrective action automatically — block it, quarantine it, or alert on it.</p>'
        '<p><strong>Example 1:</strong> Configure Windows Defender Application Control (WDAC) '
        'to block unsigned or untrusted executables, scripts, and DLLs. When a user downloads '
        'a suspicious script, WDAC prevents it from running and logs the attempt.</p>'
        '<p><strong>Example 2:</strong> Deploy a cloud-based email security gateway (like '
        'Proofpoint or Microsoft Defender for Office 365) that detonates email attachments '
        'in a sandbox. Macros and scripts that exhibit malicious behavior are stripped from '
        'the attachment before delivery to the user.</p>'
    ),

    "sc-18-2": (
        '<p>Control mobile code during its acquisition, development, and use — ensuring only '
        'approved mobile code from trusted sources is used in your environment.</p>'
        '<p><strong>Example 1:</strong> Maintain an approved list of browser extensions and '
        'Office add-ins. Use Chrome Enterprise or Edge management to push only approved '
        'extensions and block all others. Review and update the approved list quarterly.</p>'
        '<p><strong>Example 2:</strong> For internally developed macros and scripts, require '
        'code review and signing before deployment. Store approved scripts in a controlled '
        'repository (like an internal Git server) and use code signing certificates to '
        'verify authenticity before execution.</p>'
    ),

    "sc-18-3": (
        '<p>Prevent the download and execution of prohibited mobile code entirely — do not '
        'rely on users to make safe decisions.</p>'
        '<p><strong>Example 1:</strong> Configure your web proxy to block downloads of file '
        'types commonly used for mobile code attacks — .hta, .js, .vbs, .wsf, .jar. Block '
        'these at the network level so users never have the opportunity to run them.</p>'
        '<p><strong>Example 2:</strong> Use AppLocker via GPO to prevent execution of scripts '
        'and executables from user-writable locations (Downloads, Temp, AppData). Even if a '
        'user downloads a malicious script, it cannot execute because AppLocker blocks '
        'execution from that directory.</p>'
    ),

    "sc-18-4": (
        '<p>Prevent mobile code from executing automatically — users should have to '
        'deliberately choose to run it.</p>'
        '<p><strong>Example 1:</strong> Configure Office via GPO to "Disable all macros '
        'with notification." Users see a warning bar and must actively click "Enable Content" '
        'to run macros. Macros never execute automatically when a document is opened.</p>'
        '<p><strong>Example 2:</strong> In your browser policy, set JavaScript to prompt '
        'or block for downloaded HTML files opened locally. Configure file associations so '
        'that .js, .vbs, and .wsf files open in Notepad rather than executing in the '
        'Windows Script Host.</p>'
    ),

    "sc-18-5": (
        '<p>If mobile code must run, confine it to a sandbox or restricted environment where '
        'it cannot access the rest of the system.</p>'
        '<p><strong>Example 1:</strong> Enable Windows Sandbox or Application Guard for '
        'Edge. When users download and open untrusted files or visit untrusted websites, '
        'they run in an isolated container that is destroyed when closed — any malware is '
        'contained and discarded.</p>'
        '<p><strong>Example 2:</strong> Use browser isolation technology (like Menlo Security '
        'or Zscaler Browser Isolation) that executes web content in a remote container. '
        'Only a safe visual stream reaches the user&apos;s browser — malicious scripts run in '
        'the cloud container where they cannot touch the endpoint.</p>'
    ),

    "sc-19": (
        '<p>This control (withdrawn in Rev 5) addressed VoIP security and has been '
        'incorporated into other SC family controls. VoIP systems should follow the same '
        'boundary protection (SC-7) and transmission security (SC-8) requirements as any '
        'other networked system.</p>'
        '<p><strong>Example 1:</strong> Place your VoIP phones on a dedicated voice VLAN '
        'separated from your data network. Apply QoS policies and firewall rules specific '
        'to voice traffic (SC-7).</p>'
        '<p><strong>Example 2:</strong> Enable SRTP (Secure Real-time Transport Protocol) '
        'for voice call encryption so conversations cannot be intercepted by someone '
        'sniffing network traffic (SC-8).</p>'
    ),

    "sc-20": (
        '<p>Your authoritative DNS servers must provide data origin authentication and '
        'integrity verification — proving that DNS responses actually came from your '
        'server and were not tampered with in transit.</p>'
        '<p><strong>Example 1:</strong> Implement DNSSEC on your authoritative DNS zones. '
        'Sign your DNS zone files so resolvers can verify the authenticity of your DNS '
        'records. This prevents attackers from injecting fake DNS responses (DNS poisoning).</p>'
        '<p><strong>Example 2:</strong> On your internal Active Directory DNS, configure '
        'secure dynamic updates. Only authenticated, domain-joined machines can update DNS '
        'records, preventing unauthorized devices from registering rogue DNS entries that '
        'redirect traffic to malicious servers.</p>'
    ),

    "sc-20-1": (
        '<p>Provide DNS integrity services for child subspaces (subdomains) to maintain '
        'the chain of trust from the parent domain.</p>'
        '<p><strong>Example 1:</strong> If you delegate subdomains (like dev.company.com), '
        'sign the DS (Delegation Signer) records in the parent zone so the entire chain '
        'from root to subdomain is DNSSEC-protected.</p>'
        '<p><strong>Example 2:</strong> For Active Directory child domains, ensure DNS '
        'zone delegation includes proper NS records and that secure dynamic updates are '
        'enabled on the child domain&apos;s DNS zone, maintaining the same security posture '
        'as the parent domain.</p>'
    ),

    "sc-20-2": (
        '<p>Provide data origin and integrity protection for DNS data specifically — '
        'ensuring responses are authentic and complete.</p>'
        '<p><strong>Example 1:</strong> Enable DNSSEC validation on your recursive resolvers '
        'so they verify the cryptographic signatures on DNS responses before passing them '
        'to clients. Invalid signatures cause the query to fail rather than return '
        'potentially poisoned data.</p>'
        '<p><strong>Example 2:</strong> Monitor DNSSEC validation failures in your DNS '
        'server logs and forward them to your SIEM. A spike in validation failures could '
        'indicate a DNS poisoning attack or a misconfigured upstream zone.</p>'
    ),

    "sc-21": (
        '<p>Your recursive or caching DNS resolvers — the servers your users actually query '
        '— must validate DNS responses before caching them to prevent DNS poisoning attacks.</p>'
        '<p><strong>Example 1:</strong> Configure your internal DNS resolvers (Windows DNS, '
        'BIND) to validate DNSSEC signatures on responses from authoritative servers. Enable '
        'DNSSEC validation in Windows DNS via PowerShell: Set-DnsServerDsSetting '
        '-EnableDnsSec $true.</p>'
        '<p><strong>Example 2:</strong> Use Cloudflare (1.1.1.1) or Google (8.8.8.8) as '
        'forwarders for external DNS resolution — both perform DNSSEC validation. Configure '
        'your internal DNS to forward external queries to these resolvers over DNS-over-HTTPS '
        'for additional transport security.</p>'
    ),

    "sc-21-1": (
        '<p>Perform data origin authentication and integrity verification on all DNS data '
        'at the recursive resolver level.</p>'
        '<p><strong>Example 1:</strong> Configure BIND to set "dnssec-validation auto;" in '
        'named.conf. This enables automatic DNSSEC validation using the built-in root trust '
        'anchors, verifying every signed DNS response.</p>'
        '<p><strong>Example 2:</strong> On Windows DNS servers acting as recursive resolvers, '
        'import trust anchors for zones you want to validate. Use the DNS Manager console to '
        'add trust points and verify that validation is working by querying a known '
        'DNSSEC-signed domain.</p>'
    ),

    "sc-22": (
        '<p>Design your DNS architecture for fault tolerance and security — redundant servers, '
        'separation of authoritative and recursive functions, and proper capacity planning.</p>'
        '<p><strong>Example 1:</strong> Deploy at least two DNS servers in different physical '
        'locations (or availability zones in the cloud). If one server goes down, the other '
        'continues resolving queries. Use Active Directory-integrated DNS for automatic '
        'replication between domain controllers.</p>'
        '<p><strong>Example 2:</strong> Separate your authoritative DNS (what the internet '
        'sees) from your recursive DNS (what your internal users query). Run authoritative '
        'DNS on dedicated servers in the DMZ and recursive DNS on internal servers. This '
        'prevents external queries from poisoning your internal DNS cache.</p>'
    ),

    "sc-23": (
        '<p>Protect the authenticity of communication sessions — make sure the session '
        'between a user and a system is genuine and has not been hijacked.</p>'
        '<p><strong>Example 1:</strong> Configure your web applications to use secure session '
        'cookies: set the Secure flag (HTTPS only), HttpOnly flag (no JavaScript access), '
        'SameSite attribute (prevent cross-site request forgery), and a reasonable expiration '
        'time.</p>'
        '<p><strong>Example 2:</strong> Enable Kerberos authentication for internal '
        'applications rather than NTLM. Kerberos provides mutual authentication (both client '
        'and server verify each other) and protects against session replay attacks with '
        'time-stamped tickets.</p>'
    ),

    "sc-23-1": (
        '<p>Session identifiers (tokens, cookies) must be invalidated when a user logs out, '
        'so they cannot be reused by an attacker.</p>'
        '<p><strong>Example 1:</strong> Configure your web application to destroy the session '
        'on the server side when a user clicks "Log Out." Do not just delete the cookie on '
        'the client — the server must also invalidate the session ID so it cannot be replayed.</p>'
        '<p><strong>Example 2:</strong> In Azure AD, configure token lifetime policies to '
        'limit how long access tokens remain valid. Use "Continuous Access Evaluation" so '
        'tokens are revoked almost immediately when a user&apos;s session is terminated or '
        'their risk level changes.</p>'
    ),

    "sc-23-2": (
        '<p>Users should be able to initiate a logout at any time, and the system should '
        'clearly display when they are logged out.</p>'
        '<p><strong>Example 1:</strong> Ensure every web application displays a visible '
        '"Log Out" button on every page. When clicked, it terminates the session and '
        'redirects the user to a clear "You have been logged out" confirmation page.</p>'
        '<p><strong>Example 2:</strong> For terminal/RDP sessions, ensure the Windows logoff '
        'option is available and not hidden. Train users to log off rather than just close '
        'the RDP window, which may leave their session running on the server.</p>'
    ),

    "sc-23-3": (
        '<p>Session identifiers must be system-generated, not predictable or user-chosen. '
        'Predictable session IDs let attackers guess valid sessions.</p>'
        '<p><strong>Example 1:</strong> Configure your web framework to use its built-in '
        'cryptographically random session ID generator. In ASP.NET, the framework generates '
        '120-bit random session IDs by default. Never create custom session ID schemes.</p>'
        '<p><strong>Example 2:</strong> In IIS, configure the session state to use cookie-'
        'based session tracking with the default random ID generator. Set the cookieless '
        'attribute to "UseCookies" to prevent session IDs from appearing in URLs where '
        'they could be logged or shared.</p>'
    ),

    "sc-23-4": (
        '<p>Session identifiers should be unique and generated with sufficient randomness '
        'to prevent guessing or brute-force attacks.</p>'
        '<p><strong>Example 1:</strong> Use session IDs of at least 128 bits generated from '
        'a cryptographically secure random number generator (CSPRNG). In Python Flask, use '
        'the default session implementation which uses os.urandom() for session tokens.</p>'
        '<p><strong>Example 2:</strong> Configure your load balancer or reverse proxy to '
        'regenerate session IDs after authentication (not just at session start). This '
        'prevents session fixation attacks where an attacker pre-sets a known session ID '
        'before the victim logs in.</p>'
    ),

    "sc-23-5": (
        '<p>Only accept TLS certificates from certificate authorities your organization '
        'has explicitly approved. This prevents attackers from using certificates from '
        'rogue or compromised CAs.</p>'
        '<p><strong>Example 1:</strong> Use GPO to manage the Trusted Root Certification '
        'Authorities store on domain-joined machines. Remove CAs you do not trust and only '
        'keep the CAs your organization uses. Audit the trusted root store quarterly.</p>'
        '<p><strong>Example 2:</strong> Configure certificate pinning for your critical '
        'internal web applications. The application only accepts connections presenting '
        'certificates from your specific CA, rejecting all others — even if the certificate '
        'is technically valid and from a public CA.</p>'
    ),

    "sc-24": (
        '<p>When a system fails (crash, hardware fault, attack), it must fail into a known, '
        'secure state rather than an unpredictable state that might expose data or disable '
        'security controls.</p>'
        '<p><strong>Example 1:</strong> Configure your web servers to display a generic error '
        'page on failure rather than detailed stack traces or debug information. The custom '
        'error page gives users a support contact without revealing system internals to '
        'an attacker.</p>'
        '<p><strong>Example 2:</strong> Set your firewall to fail-closed mode. If the '
        'inspection engine crashes, the firewall blocks all traffic rather than passing '
        'it through uninspected. This ensures a failure does not create a window where '
        'traffic flows unmonitored.</p>'
    ),

    "sc-25": (
        '<p>Thin nodes (thin clients, zero clients) minimize the processing and storage '
        'on the endpoint itself. All the real work happens on a server — the endpoint is '
        'just a window into the server session.</p>'
        '<p><strong>Example 1:</strong> Deploy thin client terminals (Dell Wyse, HP t-series) '
        'for users who primarily work in virtual desktops (VDI). The thin client has no local '
        'storage for data and boots from a read-only image. If the device is stolen, there '
        'is nothing on it to compromise.</p>'
        '<p><strong>Example 2:</strong> Use Azure Virtual Desktop or Citrix to deliver '
        'applications to users on thin clients. All data processing and storage happens '
        'in the data center or cloud. The thin client only sends keyboard/mouse input and '
        'receives screen updates.</p>'
    ),

    "sc-26": (
        '<p>Decoys (honeypots, honeynets, honey tokens) are fake systems or data designed '
        'to attract attackers and detect unauthorized activity. They look real to an attacker '
        'but serve no legitimate business purpose.</p>'
        '<p><strong>Example 1:</strong> Deploy a honeypot server on your network that looks '
        'like a vulnerable file server. It has fake "sensitive" files and open shares. Any '
        'access to this server is immediately suspicious because no legitimate user has a '
        'reason to touch it. Alert your SIEM on any connection to the honeypot.</p>'
        '<p><strong>Example 2:</strong> Create honey tokens — fake credentials stored in '
        'a document on a file share, or fake API keys in a configuration file. If these '
        'credentials are ever used to authenticate, you know an attacker has accessed your '
        'internal systems and is trying to move laterally.</p>'
    ),

    "sc-26-1": (
        '<p>Use decoy components specifically designed to detect malicious code — malware '
        'that interacts with the decoy reveals itself.</p>'
        '<p><strong>Example 1:</strong> Deploy canary files in directories commonly targeted '
        'by ransomware. Create hidden files named with patterns ransomware typically targets '
        '(like budget.xlsx). Monitor these files — if they are encrypted or modified, you '
        'have an immediate ransomware indicator.</p>'
        '<p><strong>Example 2:</strong> Set up a deception platform (like Attivo or Illusive '
        'Networks) that deploys fake credentials, fake network shares, and fake services '
        'throughout your environment. Malware that harvests credentials or scans for open '
        'shares interacts with the decoys and triggers an alert.</p>'
    ),

    "sc-27": (
        '<p>Applications should be platform-independent when feasible — able to run on '
        'multiple operating systems and hardware platforms. This provides flexibility '
        'and reduces vendor lock-in.</p>'
        '<p><strong>Example 1:</strong> Develop internal web applications using standard '
        'HTML5, CSS, and JavaScript that runs in any modern browser, rather than using '
        'browser-specific features or plugins that lock you into one platform.</p>'
        '<p><strong>Example 2:</strong> When selecting commercial software, prefer products '
        'that run on multiple operating systems (Windows, Linux, macOS) or are delivered '
        'as SaaS. This gives you the flexibility to switch platforms if a security '
        'vulnerability is discovered in one OS.</p>'
    ),

    "sc-28": (
        '<p>Data at rest — on hard drives, in databases, on backup tapes — must be protected '
        'from unauthorized access. If someone steals a drive or gains unauthorized access '
        'to storage, they should not be able to read the data.</p>'
        '<p><strong>Example 1:</strong> Enable BitLocker on all Windows laptops and desktops '
        'via GPO. Use TPM + PIN for pre-boot authentication. Back up recovery keys to Active '
        'Directory. If a laptop is lost or stolen, the data on the drive is encrypted and '
        'unreadable without the correct credentials.</p>'
        '<p><strong>Example 2:</strong> Enable Transparent Data Encryption (TDE) on your SQL '
        'Server databases. TDE encrypts the database files at rest so even if someone copies '
        'the .mdf file, they cannot read the data without the encryption key managed by the '
        'SQL Server instance.</p>'
    ),

    "sc-28-1": (
        '<p>Use cryptographic mechanisms specifically to protect the confidentiality and '
        'integrity of data at rest — encryption is mandatory, not optional.</p>'
        '<p><strong>Example 1:</strong> Use AES-256 encryption for all data at rest. For '
        'file servers, use BitLocker. For databases, use TDE or Always Encrypted. For cloud '
        'storage, enable server-side encryption with customer-managed keys in Azure Key '
        'Vault or AWS KMS.</p>'
        '<p><strong>Example 2:</strong> Encrypt backup data before it leaves your server. '
        'Configure your backup solution (Veeam, Commvault) to use AES-256 encryption with '
        'a key stored separately from the backup media. A stolen backup tape is useless '
        'without the decryption key.</p>'
    ),

    "sc-28-2": (
        '<p>Data stored offline (tapes, removable drives, cold storage) needs protection '
        'too — physical security and encryption for media that is not actively connected '
        'to your systems.</p>'
        '<p><strong>Example 1:</strong> Encrypt backup tapes before sending them to offsite '
        'storage with Iron Mountain or a similar service. Use hardware encryption on the '
        'tape drive (LTO encryption) with keys managed in your key management system. '
        'Track every tape with a barcode inventory system.</p>'
        '<p><strong>Example 2:</strong> For archived data on removable drives, use BitLocker '
        'To Go or VeraCrypt to encrypt the entire drive. Store the encrypted drives in a '
        'locked, access-controlled safe. Maintain a log of who accesses the safe and when, '
        'and verify the drives&apos; integrity when they are accessed.</p>'
    ),

    "sc-28-3": (
        '<p>Protect cryptographic keys used for data-at-rest encryption with the same rigor '
        'as the data itself. If an attacker gets your keys, encryption is meaningless.</p>'
        '<p><strong>Example 1:</strong> Store database encryption keys in Azure Key Vault '
        'or AWS KMS, not in the database configuration files. The key management service '
        'has its own access controls, audit logging, and hardware-backed key storage.</p>'
        '<p><strong>Example 2:</strong> For BitLocker, store recovery keys in Active '
        'Directory (not on sticky notes or in shared spreadsheets). Restrict who can view '
        'recovery keys in AD to your security team and IT managers. Audit all access to '
        'recovery key objects.</p>'
    ),

    "sc-29": (
        '<p>Use diverse components — different hardware vendors, operating systems, and '
        'software — to reduce the risk that a single vulnerability takes down everything. '
        'If all your systems run the same software, one exploit compromises them all.</p>'
        '<p><strong>Example 1:</strong> Run your web servers on Linux (Apache/Nginx) and '
        'your application servers on Windows (IIS). An exploit targeting one OS does not '
        'automatically compromise the other tier. The attacker needs separate exploits for '
        'each layer.</p>'
        '<p><strong>Example 2:</strong> Use firewalls from different vendors at different '
        'points in your architecture — for example, Palo Alto at the perimeter and a '
        'different vendor for internal segmentation. A zero-day vulnerability in one vendor&apos;s '
        'product does not open your entire network.</p>'
    ),

    "sc-29-1": (
        '<p>Use virtualization to create diverse processing environments. Virtual machines '
        'can run different operating systems and configurations, providing heterogeneity '
        'within a single physical infrastructure.</p>'
        '<p><strong>Example 1:</strong> Run critical applications on VMs with different OS '
        'versions or distributions. Your primary database on Ubuntu, your backup on CentOS. '
        'A kernel exploit targeting one distribution does not affect the other.</p>'
        '<p><strong>Example 2:</strong> Use containerization (Docker, Kubernetes) to isolate '
        'applications in different runtime environments. Each container has its own OS '
        'libraries and dependencies, so a vulnerability in one container&apos;s stack does not '
        'affect others.</p>'
    ),

    "sc-30": (
        '<p>Use concealment and misdirection techniques to make it harder for attackers to '
        'target your systems. If they cannot find or understand your infrastructure, they '
        'cannot attack it effectively.</p>'
        '<p><strong>Example 1:</strong> Randomize your server naming conventions so hostnames '
        'do not reveal function (do not name servers "DC01" or "SQL-PROD"). Use opaque names '
        'that give attackers no clues about what each system does.</p>'
        '<p><strong>Example 2:</strong> Change the default ports for management services. '
        'Move SSH from port 22 to a non-standard port. Move RDP from 3389. This does not '
        'stop a determined attacker but it defeats automated scanning tools and reduces '
        'noise in your logs.</p>'
    ),

    "sc-30-1": (
        '<p>Use virtualization to support concealment — move virtual machines between physical '
        'hosts, change IP addresses, and reconfigure the virtual environment to present a '
        'moving target.</p>'
        '<p><strong>Example 1:</strong> Use VMware vMotion or Hyper-V Live Migration to '
        'periodically move critical VMs to different physical hosts. An attacker who has '
        'fingerprinted the hardware characteristics of a specific host finds their '
        'reconnaissance is outdated.</p>'
        '<p><strong>Example 2:</strong> Use DHCP with short lease times for server VMs in '
        'development environments so IP addresses change regularly. Combine this with DNS '
        'service discovery so legitimate clients always find the right server regardless '
        'of IP changes.</p>'
    ),

    "sc-30-2": (
        '<p>Introduce randomness into your system configurations and operations to defeat '
        'attackers who rely on predictable patterns.</p>'
        '<p><strong>Example 1:</strong> Enable Address Space Layout Randomization (ASLR) on '
        'all systems. ASLR randomizes memory addresses so buffer overflow exploits cannot '
        'reliably predict where code and data are located. On Windows, ASLR is enabled by '
        'default — verify it has not been disabled.</p>'
        '<p><strong>Example 2:</strong> Randomize scheduled task timing. Instead of running '
        'security scans at exactly midnight, add a random 0-60 minute jitter. This makes '
        'it harder for an attacker to predict when your defenses are performing scans '
        'and time their activities to avoid detection.</p>'
    ),

    "sc-30-3": (
        '<p>Periodically change where data is processed and stored so attackers cannot rely '
        'on static locations to find their targets.</p>'
        '<p><strong>Example 1:</strong> In a cloud environment, periodically migrate workloads '
        'between regions or availability zones. An attacker who has identified the specific '
        'physical infrastructure hosting your data finds it has moved.</p>'
        '<p><strong>Example 2:</strong> Rotate which servers handle specific functions. '
        'Instead of always processing CUI on Server-A, cycle the function between multiple '
        'prepared servers. Use load balancers and automation to make this transparent to '
        'users while confusing attackers.</p>'
    ),

    "sc-30-4": (
        '<p>Plant misleading information that leads attackers down wrong paths or reveals '
        'their presence when they act on the false intelligence.</p>'
        '<p><strong>Example 1:</strong> Create fake administrator accounts in Active Directory '
        'with enticing names like "backup_admin" or "svc_sql_prod." These accounts are never '
        'used legitimately. Any authentication attempt triggers an immediate high-priority '
        'alert in your SIEM.</p>'
        '<p><strong>Example 2:</strong> Place fake network diagrams and password files in '
        'decoy file shares. If an attacker finds and uses this information, they waste time '
        'on non-existent systems while your monitoring detects their activity through the '
        'honey tokens embedded in the fake documents.</p>'
    ),

    "sc-30-5": (
        '<p>Hide the existence or characteristics of specific system components so attackers '
        'do not know what to target.</p>'
        '<p><strong>Example 1:</strong> Configure your network to block ICMP echo requests '
        'to internal hosts and suppress TCP RST packets for closed ports. Attackers scanning '
        'your network receive no response, making it difficult to map your infrastructure.</p>'
        '<p><strong>Example 2:</strong> Use a reverse proxy that terminates all connections '
        'and presents a uniform front to external users. The proxy hides the number, type, '
        'and configuration of backend servers. To an attacker, everything looks like a '
        'single web server.</p>'
    ),

    "sc-31": (
        '<p>Covert channels are hidden methods attackers use to extract data or communicate '
        'with malware — like encoding data in packet timing, unused protocol fields, or '
        'DNS queries. This control requires analyzing your systems for these hidden channels.</p>'
        '<p><strong>Example 1:</strong> Conduct a covert channel analysis during system '
        'development or major upgrades. Identify shared resources (memory, storage, network '
        'buffers) where information could leak between processes at different security levels. '
        'Document findings in your System Security Plan.</p>'
        '<p><strong>Example 2:</strong> Use network monitoring tools to look for data in '
        'unusual protocol fields — excessively long DNS queries (DNS tunneling), data '
        'encoded in ICMP payloads, or HTTP headers containing encoded information. Configure '
        'your IDS rules to alert on these patterns.</p>'
    ),

    "sc-31-1": (
        '<p>After identifying covert channels, test whether they can actually be exploited '
        'to transfer meaningful amounts of data.</p>'
        '<p><strong>Example 1:</strong> Use a DNS tunneling tool (like dnscat2 or iodine) '
        'in a controlled test to measure the bandwidth achievable through DNS covert '
        'channels on your network. If the bandwidth is high enough to be useful to an '
        'attacker, implement countermeasures.</p>'
        '<p><strong>Example 2:</strong> Test timing covert channels by measuring whether '
        'one process can reliably communicate information to another by modulating its '
        'use of shared resources (CPU, memory). Document the maximum achievable bandwidth '
        'and determine if it poses an acceptable risk.</p>'
    ),

    "sc-31-2": (
        '<p>Set maximum allowable bandwidth for identified covert channels to limit the '
        'amount of data that could be exfiltrated through them.</p>'
        '<p><strong>Example 1:</strong> After identifying DNS as a potential covert channel, '
        'configure your DNS server to limit the rate and size of DNS queries from any single '
        'host. Cap queries to 100 per minute and limit TXT record responses to standard '
        'sizes.</p>'
        '<p><strong>Example 2:</strong> Implement network traffic rate limiting on protocols '
        'commonly used for covert channels. Cap ICMP traffic to minimal levels needed for '
        'network diagnostics. Limit outbound DNS query rates. These limits reduce the '
        'bandwidth available for covert data exfiltration.</p>'
    ),

    "sc-31-3": (
        '<p>Measure covert channel bandwidth in your actual operational environment, not '
        'just in a lab. Real-world conditions affect how much data can leak through '
        'covert channels.</p>'
        '<p><strong>Example 1:</strong> During operational testing, run covert channel '
        'bandwidth measurement tools while the system is under normal load. The results '
        'may differ significantly from lab measurements because shared resource contention '
        'affects covert channel throughput.</p>'
        '<p><strong>Example 2:</strong> Monitor network traffic patterns over time using '
        'your SIEM to establish baselines for protocol volumes. Significant deviations '
        'in DNS query volume, ICMP traffic, or unusual protocol field sizes may indicate '
        'active covert channel exploitation.</p>'
    ),

    "sc-32": (
        '<p>Partition your system into distinct components so that a failure or compromise '
        'in one partition does not affect others. Each partition has its own security '
        'boundary.</p>'
        '<p><strong>Example 1:</strong> Separate your CUI-processing environment from your '
        'general office network. CUI systems sit on their own VLAN with dedicated servers, '
        'separate Active Directory OU policies, and independent backup systems. A compromise '
        'of the general network does not give access to CUI systems.</p>'
        '<p><strong>Example 2:</strong> In cloud deployments, use separate Azure subscriptions '
        'or AWS accounts for production, development, and security operations. Each '
        'subscription has its own identity boundary, network, and access controls. A '
        'compromised development account cannot reach production resources.</p>'
    ),

    "sc-32-1": (
        '<p>Use physically separate hardware for privileged functions so that administrative '
        'capabilities are completely isolated from regular user environments.</p>'
        '<p><strong>Example 1:</strong> Deploy dedicated Privileged Access Workstations (PAWs) '
        'on physically separate hardware for domain administration. These machines are not '
        'used for email, web browsing, or any non-administrative task. They sit on a '
        'separate management network.</p>'
        '<p><strong>Example 2:</strong> Run your domain controllers on dedicated physical '
        'servers (not shared virtualization hosts with regular VMs). If an attacker '
        'compromises a regular VM host, they cannot access the hypervisor running your '
        'domain controllers.</p>'
    ),

    "sc-33": (
        '<p>Verify the integrity of data before it is transmitted — ensure nothing has been '
        'tampered with between the time it was prepared and the time it is sent.</p>'
        '<p><strong>Example 1:</strong> Calculate and verify checksums or hash values for '
        'data files before transmitting them. The sender generates an SHA-256 hash, sends '
        'the file and hash separately, and the receiver verifies the hash to confirm the '
        'file was not altered.</p>'
        '<p><strong>Example 2:</strong> Use digital signatures on critical data exports. '
        'Before transmitting financial reports or compliance data, sign the file with your '
        'organization&apos;s code signing certificate. The recipient verifies the signature to '
        'confirm both authenticity and integrity.</p>'
    ),

    "sc-34": (
        '<p>Use non-modifiable executable programs — boot from read-only media or write-'
        'protected storage so attackers cannot permanently alter your system software.</p>'
        '<p><strong>Example 1:</strong> Boot thin clients from a read-only image stored on '
        'the network or in firmware. Even if malware executes during a session, a reboot '
        'restores the clean, unmodified image. The malware cannot persist.</p>'
        '<p><strong>Example 2:</strong> Use UEFI Secure Boot to verify the integrity of '
        'boot components before execution. The firmware checks digital signatures on the '
        'bootloader and kernel — unsigned or modified code is rejected before it can run.</p>'
    ),

    "sc-34-1": (
        '<p>Configure systems with no writable storage for the operating system and '
        'applications — all executable code comes from read-only sources.</p>'
        '<p><strong>Example 1:</strong> Deploy diskless workstations that PXE boot from a '
        'network server. The OS image is read-only on the server. Users save data to '
        'network shares, but the operating system itself cannot be permanently modified.</p>'
        '<p><strong>Example 2:</strong> Use immutable container images in Docker/Kubernetes. '
        'The container image is read-only at runtime. If an attacker modifies files inside '
        'the container, restarting it restores the original image. Persistent data is stored '
        'only in explicitly mounted volumes.</p>'
    ),

    "sc-34-2": (
        '<p>Protect the integrity of software on read-only media — verify that the media '
        'has not been tampered with before booting from it.</p>'
        '<p><strong>Example 1:</strong> Store boot images on USB drives with hardware '
        'write-protection switches. Before deploying, verify the image&apos;s SHA-256 hash '
        'against the known-good value. Any mismatch means the media has been tampered with.</p>'
        '<p><strong>Example 2:</strong> Use digitally signed firmware images. Before flashing '
        'firmware updates, the device verifies the manufacturer&apos;s digital signature. '
        'Modified or counterfeit firmware is rejected and the update fails safely.</p>'
    ),

    "sc-34-3": (
        '<p>Use hardware-based mechanisms to enforce protection of non-modifiable executables — '
        'not just software policies that could be bypassed.</p>'
        '<p><strong>Example 1:</strong> Use TPM-based measured boot to create a hardware-'
        'anchored chain of trust. Each boot component is measured into the TPM before '
        'execution. If any component has been modified, the TPM measurements change and '
        'the system can refuse to boot or alert the administrator.</p>'
        '<p><strong>Example 2:</strong> Deploy systems with hardware write-protect jumpers '
        'on BIOS/UEFI flash chips. The firmware cannot be modified by software (even by '
        'malware with root access) unless someone physically changes the jumper — requiring '
        'physical access to the machine.</p>'
    ),

    "sc-35": (
        '<p>Use external services and threat intelligence to identify malicious code before '
        'it reaches your systems — catching threats at the boundary rather than on the '
        'endpoint.</p>'
        '<p><strong>Example 1:</strong> Subscribe to threat intelligence feeds (CISA AIS, '
        'commercial feeds) and integrate them with your email gateway and firewall. Known '
        'malicious file hashes, URLs, and IP addresses are automatically blocked before '
        'they reach your users.</p>'
        '<p><strong>Example 2:</strong> Use a cloud-based sandbox service (like Microsoft '
        'Defender for Office 365 Safe Attachments or Palo Alto WildFire) that detonates '
        'suspicious files in an isolated environment. If the file exhibits malicious '
        'behavior, it is blocked from reaching the user.</p>'
    ),

    "sc-36": (
        '<p>Distribute processing and storage across multiple locations so that a single '
        'physical attack, disaster, or compromise cannot take out your entire operation.</p>'
        '<p><strong>Example 1:</strong> Replicate critical databases between two data centers '
        'in different geographic regions. If one site is destroyed by a natural disaster or '
        'compromised by an attacker, the other site has a current copy of the data and can '
        'take over operations.</p>'
        '<p><strong>Example 2:</strong> Use cloud-based storage with cross-region replication '
        '(like Azure GRS or AWS S3 Cross-Region Replication) for critical business data. '
        'Your data is automatically copied to a geographically separate location, providing '
        'resilience against regional outages and targeted attacks.</p>'
    ),

    "sc-36-1": (
        '<p>Use polling techniques to verify the integrity and consistency of distributed '
        'data — periodically checking that copies at different locations match.</p>'
        '<p><strong>Example 1:</strong> Configure your database replication monitoring to '
        'run periodic consistency checks between primary and replica databases. SQL Server '
        'DBCC CHECKDB can verify data integrity, and replication latency monitors ensure '
        'replicas stay in sync.</p>'
        '<p><strong>Example 2:</strong> Use file integrity monitoring (like Tripwire or '
        'OSSEC) across distributed file stores. Periodically compare checksums of critical '
        'files between locations. Discrepancies trigger alerts that could indicate tampering '
        'or replication failures.</p>'
    ),

    "sc-36-2": (
        '<p>Ensure distributed processing components stay synchronized — data and '
        'configurations must be consistent across all locations.</p>'
        '<p><strong>Example 1:</strong> Configure Active Directory replication monitoring '
        'to alert on replication failures between domain controllers. Use "repadmin '
        '/replsummary" regularly and forward results to your SIEM. Replication failures '
        'could indicate network issues or an attack on AD.</p>'
        '<p><strong>Example 2:</strong> For distributed databases, use synchronous '
        'replication for critical transaction data and configure alerts for replication lag. '
        'If the replica falls more than a few seconds behind, investigate immediately — '
        'it could indicate a network attack or infrastructure failure.</p>'
    ),

    "sc-37": (
        '<p>Use out-of-band channels — communication paths separate from your primary '
        'network — for delivering critical security information like keys, passwords, '
        'or emergency alerts.</p>'
        '<p><strong>Example 1:</strong> When resetting an administrator password, send the '
        'temporary password via encrypted SMS or a phone call — not through the same email '
        'system the password protects. The out-of-band channel prevents an attacker who has '
        'compromised email from intercepting the new password.</p>'
        '<p><strong>Example 2:</strong> Maintain a phone tree or out-of-band messaging '
        'system (like Signal) for incident response communications. If your corporate '
        'email and chat are compromised, you need an alternative way to coordinate your '
        'response team without the attacker listening in.</p>'
    ),

    "sc-37-1": (
        '<p>Verify delivery and transmission through out-of-band channels to ensure the '
        'information actually reached the intended recipient.</p>'
        '<p><strong>Example 1:</strong> When delivering a new encryption key via courier, '
        'require a signed receipt from the recipient. Follow up with a phone call to '
        'confirm the key was received and verify the key fingerprint over the phone.</p>'
        '<p><strong>Example 2:</strong> When sending critical security patches via removable '
        'media to an air-gapped system, verify the SHA-256 hash of the files with the '
        'recipient over a separate phone call to confirm the media was not tampered with '
        'during transit.</p>'
    ),

    "sc-38": (
        '<p>Operations security (OPSEC) means protecting information about your security '
        'posture, capabilities, and operations from adversaries. Do not reveal what '
        'defenses you have or how they work.</p>'
        '<p><strong>Example 1:</strong> Do not discuss specific security tools, versions, '
        'or configurations on public channels, social media, or in job postings. A job '
        'posting for a "Splunk administrator with CrowdStrike experience" tells attackers '
        'exactly what SIEM and EDR you use.</p>'
        '<p><strong>Example 2:</strong> Redact internal hostnames, IP addresses, and '
        'security tool names from any documents shared externally — incident reports, '
        'compliance submissions, vendor communications. Use generic terms like "our SIEM" '
        'or "our endpoint protection" instead of product names.</p>'
    ),

    "sc-39": (
        '<p>Each process running on your system should be isolated from other processes so '
        'that one compromised process cannot read or modify another process&apos;s memory '
        'and data.</p>'
        '<p><strong>Example 1:</strong> Ensure all systems have modern process isolation '
        'enabled — ASLR, DEP (Data Execution Prevention), and CFG (Control Flow Guard) '
        'on Windows. These are enabled by default on current Windows versions. Verify via '
        'GPO that they have not been disabled.</p>'
        '<p><strong>Example 2:</strong> In containerized environments, run each application '
        'in its own container with minimal privileges. Use seccomp profiles and AppArmor '
        'policies to restrict what system calls each container can make. One compromised '
        'container cannot access another container&apos;s memory or files.</p>'
    ),

    "sc-39-1": (
        '<p>Use hardware-enforced separation between processes — CPU rings, memory protection '
        'units, or virtualization extensions that the operating system cannot bypass.</p>'
        '<p><strong>Example 1:</strong> Enable Virtualization-Based Security (VBS) on Windows '
        '10/11 and Server 2019+. VBS uses the hypervisor to create isolated memory regions '
        'that even the OS kernel cannot access, protecting credentials and code integrity.</p>'
        '<p><strong>Example 2:</strong> Use Intel SGX enclaves for applications that process '
        'highly sensitive data. The CPU hardware creates encrypted memory regions that no '
        'other process — including the OS and hypervisor — can read or tamper with.</p>'
    ),

    "sc-39-2": (
        '<p>Give each execution thread its own separate domain to prevent thread-level '
        'attacks where one thread accesses another thread&apos;s data.</p>'
        '<p><strong>Example 1:</strong> Ensure your systems have Spectre and Meltdown '
        'mitigations enabled (microcode updates and OS patches). These attacks exploit '
        'shared CPU resources between threads. Verify mitigations are active using '
        'tools like SpecuCheck or InSpectre.</p>'
        '<p><strong>Example 2:</strong> For highly sensitive workloads, disable '
        'Hyper-Threading (SMT) on the physical CPU. This ensures each thread gets its '
        'own dedicated CPU core and cannot share execution resources with another thread '
        'that might be running malicious code.</p>'
    ),

    "sc-40": (
        '<p>Wireless communications — WiFi, Bluetooth, cellular — need protection from '
        'eavesdropping, jamming, and unauthorized access because radio signals can be '
        'intercepted from a distance.</p>'
        '<p><strong>Example 1:</strong> Configure all corporate WiFi access points to use '
        'WPA3-Enterprise with 802.1X certificate-based authentication. Disable legacy '
        'protocols (WEP, WPA, WPA2-Personal) that are vulnerable to known attacks.</p>'
        '<p><strong>Example 2:</strong> Use a wireless intrusion detection system (WIDS) '
        'like Cisco Aironet or Aruba to detect rogue access points, evil twin attacks, '
        'and deauthentication attacks. Alert your security team when unauthorized wireless '
        'devices are detected near your facilities.</p>'
    ),

    "sc-40-1": (
        '<p>Protect wireless communications from electromagnetic interference — both '
        'accidental (from nearby equipment) and intentional (jamming attacks).</p>'
        '<p><strong>Example 1:</strong> Conduct a wireless site survey to identify sources '
        'of electromagnetic interference — microwave ovens, industrial equipment, competing '
        'WiFi networks. Position your access points and choose channels to minimize '
        'interference.</p>'
        '<p><strong>Example 2:</strong> Deploy your wireless network with redundant access '
        'points and automatic channel switching so that if one AP or channel is jammed, '
        'clients automatically roam to an unaffected AP on a different channel.</p>'
    ),

    "sc-40-2": (
        '<p>Reduce the detection potential of your wireless communications — make it harder '
        'for adversaries to detect and locate your wireless infrastructure.</p>'
        '<p><strong>Example 1:</strong> Reduce WiFi transmit power to the minimum level '
        'needed for coverage within your facility. Excess power bleeds outside your '
        'building, making your network detectable and attackable from the parking lot '
        'or adjacent buildings.</p>'
        '<p><strong>Example 2:</strong> Disable SSID broadcast on sensitive wireless '
        'networks and use directional antennas that focus the signal inside your facility '
        'rather than radiating in all directions. This reduces the network&apos;s visibility '
        'to external observers.</p>'
    ),

    "sc-40-3": (
        '<p>Protect against imitative or manipulative communications deception — attacks '
        'where an adversary mimics your wireless communications to inject false data or '
        'steal credentials.</p>'
        '<p><strong>Example 1:</strong> Use 802.1X with certificate-based authentication '
        'for WiFi. Clients verify the authentication server&apos;s certificate before sending '
        'credentials, preventing evil twin access points from harvesting user passwords.</p>'
        '<p><strong>Example 2:</strong> Configure your wireless IDS to detect MAC address '
        'spoofing. Alert when a new access point appears with the same SSID as your '
        'corporate network but with a different MAC address or on a different channel — '
        'this is a classic evil twin indicator.</p>'
    ),

    "sc-40-4": (
        '<p>Identify and authenticate wireless signal parameters to verify that '
        'communications are coming from legitimate devices, not adversary equipment.</p>'
        '<p><strong>Example 1:</strong> Deploy wireless monitoring that fingerprints the '
        'unique radio characteristics (RF signatures) of your authorized access points. '
        'If a device transmits on your frequency with different RF characteristics, it is '
        'flagged as potentially rogue.</p>'
        '<p><strong>Example 2:</strong> Use your wireless controller&apos;s built-in rogue AP '
        'detection. Cisco WLC or Aruba controllers continuously scan for unauthorized '
        'access points by comparing detected BSSIDs against the authorized list. Unknown '
        'BSSIDs trigger automatic alerts and optional containment.</p>'
    ),

    "sc-41": (
        '<p>Control access to physical I/O ports — USB, Thunderbolt, serial, HDMI — on '
        'your systems to prevent unauthorized data transfer or device connections.</p>'
        '<p><strong>Example 1:</strong> Use a GPO to disable USB storage devices on '
        'workstations. Under Computer Configuration > Administrative Templates > System > '
        'Removable Storage Access, enable "All Removable Storage classes: Deny all access." '
        'This prevents data exfiltration via USB drives.</p>'
        '<p><strong>Example 2:</strong> Deploy endpoint protection with device control '
        '(CrowdStrike, Microsoft Defender for Endpoint) that allows you to whitelist '
        'specific authorized USB devices (like encrypted corporate drives) while blocking '
        'all other removable media. Log all USB device connections for audit.</p>'
    ),

    "sc-42": (
        '<p>Control sensors (cameras, microphones, GPS, accelerometers) on organizational '
        'devices to prevent unauthorized collection of sensitive information.</p>'
        '<p><strong>Example 1:</strong> Use mobile device management (Intune, JAMF) to '
        'control which applications can access the camera, microphone, and location '
        'services on corporate phones and tablets. Only approved apps get sensor access.</p>'
        '<p><strong>Example 2:</strong> In sensitive work areas, require that laptop webcams '
        'have physical covers and that phones be placed in signal-blocking pouches. Use '
        'GPO to disable microphone access for all applications except approved '
        'conferencing software.</p>'
    ),

    "sc-42-1": (
        '<p>Ensure sensor data is only reported to authorized individuals or roles — not '
        'to unauthorized parties or systems that have no need for it.</p>'
        '<p><strong>Example 1:</strong> Configure security cameras to stream only to the '
        'security operations center and authorized security personnel. Lock down the DVR/NVR '
        'interface with strong authentication and restrict network access to the camera '
        'VLAN from management stations only.</p>'
        '<p><strong>Example 2:</strong> For GPS tracking on company vehicles, ensure the '
        'location data is only accessible to fleet management and the employee&apos;s direct '
        'supervisor. Implement role-based access in the fleet management application and '
        'audit all access to location data.</p>'
    ),

    "sc-42-2": (
        '<p>Only use sensor capabilities for authorized purposes — define and document what '
        'sensor data is collected, why, and who can access it.</p>'
        '<p><strong>Example 1:</strong> Publish a clear policy stating that security cameras '
        'are used only for physical security and not for monitoring employee performance. '
        'Define retention periods (30 days) and who can request footage review.</p>'
        '<p><strong>Example 2:</strong> If your mobile app collects location data, document '
        'the specific business purpose (like field service dispatching) and ensure the app '
        'only collects location data when actively in use — not continuously in the '
        'background.</p>'
    ),

    "sc-42-3": (
        '<p>Prohibit the use of certain sensor-equipped devices in sensitive areas where '
        'unauthorized data collection poses a significant risk.</p>'
        '<p><strong>Example 1:</strong> Ban personal cell phones and smart watches from '
        'SCIFs, server rooms, and classified work areas. Post signs at entry points and '
        'provide secure storage lockers outside the controlled area.</p>'
        '<p><strong>Example 2:</strong> Prohibit the use of IoT devices (smart speakers, '
        'smart displays, connected thermostats) in areas where sensitive conversations '
        'occur. These devices may transmit audio or environmental data to cloud services '
        'outside your control.</p>'
    ),

    "sc-42-4": (
        '<p>When sensors collect data about individuals, provide notice to those individuals '
        'that collection is occurring.</p>'
        '<p><strong>Example 1:</strong> Post visible signs in areas monitored by security '
        'cameras: "This area is under video surveillance for security purposes." Include '
        'contact information for questions about the surveillance program.</p>'
        '<p><strong>Example 2:</strong> When deploying employee monitoring software that '
        'captures screenshots or tracks application usage, notify employees through your '
        'acceptable use policy and have them acknowledge the monitoring in writing before '
        'enrolling their devices.</p>'
    ),

    "sc-42-5": (
        '<p>Minimize the amount of sensor data collected to only what is necessary for the '
        'stated purpose — do not collect more than you need.</p>'
        '<p><strong>Example 1:</strong> Configure security cameras to record only during '
        'non-business hours or in high-security areas, rather than recording everything '
        'everywhere 24/7. Reduce retention periods to the minimum needed for your security '
        'program.</p>'
        '<p><strong>Example 2:</strong> For mobile apps that need location data, use '
        '"approximate location" instead of "precise location" when exact coordinates are '
        'not needed. Collect location only when the app is in the foreground, not '
        'continuously in the background.</p>'
    ),

    "sc-43": (
        '<p>Define and enforce usage restrictions for system components that pose elevated '
        'risk — things like collaboration tools, removable media, or externally accessible '
        'services.</p>'
        '<p><strong>Example 1:</strong> Create an acceptable use policy for Microsoft Teams '
        'that restricts guest access, prohibits sharing CUI in general channels, and '
        'requires sensitivity labels on files shared through Teams. Enforce these '
        'restrictions with DLP policies in Microsoft Purview.</p>'
        '<p><strong>Example 2:</strong> Restrict the use of personal cloud storage (Dropbox, '
        'Google Drive) on corporate devices. Use your web proxy to block access to '
        'unauthorized cloud storage services and provide an approved, managed alternative '
        'like SharePoint Online or OneDrive for Business.</p>'
    ),

    "sc-44": (
        '<p>Detonation chambers are isolated sandbox environments where suspicious files '
        'and code can be executed safely to observe their behavior before allowing them '
        'into your production environment.</p>'
        '<p><strong>Example 1:</strong> Deploy Microsoft Defender for Office 365 Safe '
        'Attachments, which opens email attachments in a cloud-based sandbox (detonation '
        'chamber) to detect malicious behavior. Attachments that trigger malware indicators '
        'are blocked from delivery to the user&apos;s mailbox.</p>'
        '<p><strong>Example 2:</strong> Set up a malware analysis sandbox (like Cuckoo '
        'Sandbox or Joe Sandbox) on an isolated network segment. Security analysts can '
        'submit suspicious files for automated behavioral analysis — the sandbox reports '
        'file system changes, network connections, and registry modifications without '
        'risking your production environment.</p>'
    ),

    "sc-45": (
        '<p>System clocks must be synchronized across all your devices so that log entries '
        'from different systems can be correlated during incident investigation. If clocks '
        'are off, piecing together an attack timeline becomes impossible.</p>'
        '<p><strong>Example 1:</strong> Configure all domain-joined machines to sync their '
        'clocks with the PDC Emulator domain controller via the Windows Time service. The '
        'PDC Emulator syncs to a reliable NTP source like time.nist.gov. Use a GPO to '
        'enforce NTP settings.</p>'
        '<p><strong>Example 2:</strong> For network devices (firewalls, switches, routers), '
        'configure NTP to point to your internal time server. On a Palo Alto firewall, '
        'set the NTP server under Device > Setup > Services. Verify synchronization is '
        'working and alert if a device drifts more than 1 second.</p>'
    ),

    "sc-45-1": (
        '<p>Synchronize with an authoritative time source — a recognized, reliable time '
        'server — not just any random NTP server on the internet.</p>'
        '<p><strong>Example 1:</strong> Configure your primary time server to sync with '
        'NIST time servers (time.nist.gov) or the US Naval Observatory (tick.usno.navy.mil). '
        'These are authoritative time sources maintained by the federal government.</p>'
        '<p><strong>Example 2:</strong> For environments requiring high accuracy, deploy '
        'a GPS-based NTP server (like a Meinberg appliance) that receives time directly '
        'from GPS satellites. This provides microsecond accuracy and does not depend on '
        'internet connectivity to an external NTP server.</p>'
    ),

    "sc-45-2": (
        '<p>Maintain a secondary authoritative time source as a backup in case your '
        'primary time source becomes unavailable.</p>'
        '<p><strong>Example 1:</strong> Configure your NTP clients with at least two NTP '
        'servers — your primary internal time server and a secondary. If the primary fails, '
        'clients automatically fall back to the secondary without losing synchronization.</p>'
        '<p><strong>Example 2:</strong> Use multiple upstream NTP sources for your internal '
        'time servers. Configure them with both time.nist.gov and time.windows.com as '
        'upstream sources. The NTP algorithm selects the most accurate source and fails '
        'over automatically if one becomes unreachable.</p>'
    ),

    "sc-46": (
        '<p>Cross-domain policy enforcement applies when systems need to exchange data '
        'between different security domains — like between classified and unclassified '
        'networks.</p>'
        '<p><strong>Example 1:</strong> Deploy an NSA-approved cross-domain solution (CDS) '
        'that enforces content inspection policies on all data crossing between security '
        'domains. The CDS checks file types, scans for embedded objects, and verifies '
        'classification markings before allowing transfer.</p>'
        '<p><strong>Example 2:</strong> For unclassified cross-domain needs (like between '
        'CUI and public networks), use an application-layer gateway that inspects content '
        'type, strips metadata, and enforces data format restrictions. Only approved file '
        'types in approved formats can cross the boundary.</p>'
    ),

    "sc-47": (
        '<p>Maintain alternate communication paths so you can still communicate during an '
        'incident even if your primary network is compromised or unavailable.</p>'
        '<p><strong>Example 1:</strong> Establish an out-of-band communication plan using '
        'cell phones with an encrypted messaging app (Signal) for your incident response '
        'team. If your corporate email and chat are compromised, the team can still '
        'coordinate response actions securely.</p>'
        '<p><strong>Example 2:</strong> Maintain a cellular hotspot and a backup ISP '
        'connection that are independent of your primary internet connection. If a DDoS '
        'attack takes down your primary connection, you can still access critical cloud '
        'services and communicate with stakeholders through the alternate path.</p>'
    ),

    "sc-48": (
        '<p>Relocate sensors and monitoring capabilities to different points in the network '
        'to improve detection coverage and adapt to evolving threats.</p>'
        '<p><strong>Example 1:</strong> If your IDS sensors are all at the perimeter and '
        'you discover lateral movement inside your network, deploy additional sensors on '
        'internal segments between VLANs. Move monitoring from a perimeter-only model to '
        'a distributed model with visibility inside the network.</p>'
        '<p><strong>Example 2:</strong> Periodically reposition network taps and SPAN port '
        'mirrors to monitor different segments. This quarter, focus monitoring on the '
        'database segment. Next quarter, shift focus to the development environment. '
        'Rotate coverage to detect threats across all areas over time.</p>'
    ),

    "sc-48-1": (
        '<p>Dynamically relocate sensors based on real-time threat intelligence — moving '
        'monitoring to where it is needed most as the threat landscape changes.</p>'
        '<p><strong>Example 1:</strong> Configure your SIEM to automatically increase log '
        'collection and enable additional detection rules on network segments that show '
        'indicators of compromise. If the SIEM detects anomalous traffic on the finance '
        'VLAN, automatically enable deep packet inspection on that segment.</p>'
        '<p><strong>Example 2:</strong> Use SDN (Software-Defined Networking) to dynamically '
        'route traffic through IDS sensors based on threat level. During normal operations, '
        'sample 10 percent of traffic. When a threat is detected, route 100 percent of '
        'traffic on the affected segment through the IDS for full inspection.</p>'
    ),

    "sc-49": (
        '<p>Use hardware-enforced separation and policy enforcement — where the CPU or '
        'dedicated hardware enforces security boundaries that software alone cannot bypass.</p>'
        '<p><strong>Example 1:</strong> Deploy systems with AMD SEV (Secure Encrypted '
        'Virtualization) or Intel TDX (Trust Domain Extensions) that use the CPU to encrypt '
        'each VM&apos;s memory with a unique key. Even the hypervisor cannot read a VM&apos;s memory, '
        'providing hardware-enforced isolation between tenants.</p>'
        '<p><strong>Example 2:</strong> Use ARM TrustZone on mobile and IoT devices to '
        'create a hardware-isolated "secure world" for processing sensitive data. The secure '
        'world runs a separate OS that handles cryptographic operations, while the normal '
        'world runs the user-facing applications.</p>'
    ),

    "sc-50": (
        '<p>Use software-enforced separation and policy enforcement as a complement to (or '
        'substitute for) hardware enforcement when hardware solutions are not available.</p>'
        '<p><strong>Example 1:</strong> Use SELinux or AppArmor on Linux servers to enforce '
        'mandatory access control policies. These kernel security modules restrict what '
        'files, network ports, and system calls each process can access, regardless of '
        'the process&apos;s user permissions.</p>'
        '<p><strong>Example 2:</strong> Deploy Windows Defender Application Control (WDAC) '
        'to enforce code integrity policies. Only signed, approved executables can run. '
        'Even if an attacker gains administrative access, they cannot run unsigned '
        'malicious binaries because the kernel-enforced policy blocks them.</p>'
    ),

    "sc-51": (
        '<p>Hardware-based protection provides the strongest security guarantees because '
        'hardware mechanisms cannot be bypassed by software exploits alone.</p>'
        '<p><strong>Example 1:</strong> Use a Trusted Platform Module (TPM) 2.0 chip to '
        'anchor all platform integrity measurements. The TPM stores boot measurements in '
        'hardware registers (PCRs) that cannot be reset by software. BitLocker uses TPM '
        'measurements to prevent booting a tampered operating system.</p>'
        '<p><strong>Example 2:</strong> Deploy systems with Intel Boot Guard that verifies '
        'the firmware&apos;s digital signature in hardware before any code executes. Even if '
        'an attacker reflashes the BIOS with a malicious firmware, the hardware verification '
        'detects the change and prevents the system from booting.</p>'
    ),

    # =========================================================================
    # SYSTEM AND INFORMATION INTEGRITY (SI) — 119 controls
    # =========================================================================

    "si-1": (
        '<p>Create and maintain a policy that tells your organization how to keep systems '
        'and data accurate, complete, and trustworthy. This covers patching, malware '
        'protection, monitoring, and ensuring data is not tampered with.</p>'
        '<p><strong>Example 1:</strong> Write a System and Information Integrity policy that '
        'covers patch management timelines, antivirus requirements, system monitoring, and '
        'error handling. Store it in SharePoint with version history and assign an owner '
        'who reviews it annually.</p>'
        '<p><strong>Example 2:</strong> Use the M365 Compliance Manager to track your SI '
        'family controls. Upload your policy document as evidence, assign action items to '
        'responsible teams, and set up review reminders to keep the policy current.</p>'
    ),

    "si-2": (
        '<p>Flaw remediation means finding and fixing software bugs and vulnerabilities '
        'before attackers exploit them. This is mostly about patching, but it also covers '
        'configuration errors and design flaws.</p>'
        '<p><strong>Example 1:</strong> Use WSUS or Microsoft Endpoint Configuration Manager '
        '(MECM/SCCM) to deploy security patches within 30 days of release. Test patches '
        'on a small pilot group first, then deploy broadly. Track compliance rates and '
        'follow up on machines that miss patches.</p>'
        '<p><strong>Example 2:</strong> Subscribe to CISA&apos;s Known Exploited Vulnerabilities '
        '(KEV) catalog. When a vulnerability appears on the KEV list, prioritize patching '
        'it within the remediation timeline specified by CISA — these are vulnerabilities '
        'actively being exploited in the wild.</p>'
    ),

    "si-2-1": (
        '<p>Manage flaw remediation centrally — use a single system to track, deploy, and '
        'verify patches across your entire organization rather than letting each team handle '
        'patching independently.</p>'
        '<p><strong>Example 1:</strong> Use Microsoft Endpoint Configuration Manager as your '
        'central patch management platform. All Windows patches are approved, deployed, and '
        'tracked from a single console. Compliance reports show which machines are patched '
        'and which are not.</p>'
        '<p><strong>Example 2:</strong> Centralize third-party application patching with a '
        'tool like Patch My PC or Ivanti that integrates with your existing SCCM/Intune '
        'infrastructure. Java, Chrome, Adobe, and other non-Microsoft applications are '
        'patched through the same central process as Windows updates.</p>'
    ),

    "si-2-2": (
        '<p>Automate the process of checking whether patches have been successfully applied '
        'so you do not rely on manual verification.</p>'
        '<p><strong>Example 1:</strong> Configure your vulnerability scanner (Nessus, ACAS, '
        'Qualys) to run automated scans after each patch cycle. The scanner compares '
        'installed patch levels against the expected baseline and flags any systems that '
        'are still missing required patches.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft Defender for Endpoint&apos;s Threat and '
        'Vulnerability Management dashboard to continuously monitor patch status. The '
        'dashboard automatically identifies missing patches and scores your exposure, '
        'without waiting for a manual scan cycle.</p>'
    ),

    "si-2-3": (
        '<p>Set specific remediation timelines and benchmarks — how quickly must different '
        'severity levels of vulnerabilities be fixed?</p>'
        '<p><strong>Example 1:</strong> Define a patch SLA in your security policy: critical '
        'vulnerabilities within 72 hours, high within 14 days, medium within 30 days, low '
        'within 90 days. Track these timelines in your vulnerability management tool and '
        'report compliance to leadership monthly.</p>'
        '<p><strong>Example 2:</strong> Use your SIEM or vulnerability management platform '
        'to create dashboards showing time-to-remediation metrics. Track the average number '
        'of days to patch by severity level. If you are consistently missing your benchmarks, '
        'investigate whether you need more patching resources or better processes.</p>'
    ),

    "si-2-4": (
        '<p>Use automated patch management tools that can detect, download, test, and deploy '
        'patches with minimal manual intervention.</p>'
        '<p><strong>Example 1:</strong> Configure WSUS with automatic approval rules for '
        'critical and security updates. Patches are downloaded from Microsoft, approved '
        'based on classification, and deployed to production machines on a defined schedule '
        '— all without manual approval for routine updates.</p>'
        '<p><strong>Example 2:</strong> Use Azure Update Management or Intune to automate '
        'patching for cloud and remote machines. Define maintenance windows, set up '
        'pre-deployment testing groups, and let the tool handle deployment and reporting. '
        'Focus your team&apos;s time on exceptions rather than routine patching.</p>'
    ),

    "si-2-5": (
        '<p>Enable automatic software and firmware updates where feasible, so systems '
        'receive critical security fixes without waiting for manual deployment.</p>'
        '<p><strong>Example 1:</strong> Configure Windows Update for Business policies via '
        'Intune to automatically install security updates with a short deferral period '
        '(e.g., 3 days for quality updates). This ensures machines get patches quickly '
        'while allowing a brief window to catch bad updates.</p>'
        '<p><strong>Example 2:</strong> Enable automatic firmware updates on your firewall '
        'appliances for critical security patches. Palo Alto, Fortinet, and other vendors '
        'offer automatic threat content updates (signatures, definitions) that should be '
        'applied as soon as they are available.</p>'
    ),

    "si-2-6": (
        '<p>Remove previous versions of software and firmware after updates are installed '
        'to eliminate the risk of reverting to a vulnerable version.</p>'
        '<p><strong>Example 1:</strong> After applying Windows updates, run Disk Cleanup '
        'to remove old update files and previous Windows installation files. Use DISM '
        'commands to clean the component store and prevent rollback to vulnerable versions.</p>'
        '<p><strong>Example 2:</strong> For firmware updates on network devices, after '
        'confirming the new firmware is working correctly, delete the old firmware image '
        'from the device&apos;s storage. This prevents an attacker from rolling back to a '
        'known-vulnerable firmware version.</p>'
    ),

    "si-2-7": (
        '<p>Perform root cause analysis on security flaws — do not just fix the symptom, '
        'understand why it happened so you can prevent similar issues in the future.</p>'
        '<p><strong>Example 1:</strong> When a critical vulnerability is discovered in your '
        'custom application, do not just patch it. Investigate how the flawed code was '
        'introduced — was it a training gap, a code review failure, or a missing security '
        'test? Address the process failure to prevent recurrence.</p>'
        '<p><strong>Example 2:</strong> After a patch fails to deploy to multiple machines, '
        'investigate the root cause. Is it a network issue, a disk space problem, or a '
        'conflicting application? Document findings and update your patch process to check '
        'for these conditions before deployment.</p>'
    ),

    "si-3": (
        '<p>Malicious code protection means running antivirus and anti-malware software '
        'that can detect, block, and remove viruses, ransomware, spyware, and other '
        'threats from your systems.</p>'
        '<p><strong>Example 1:</strong> Deploy Microsoft Defender Antivirus on all Windows '
        'endpoints via GPO. Enable real-time protection, cloud-delivered protection, and '
        'automatic sample submission. Verify it is running on all machines through the '
        'Defender for Endpoint portal.</p>'
        '<p><strong>Example 2:</strong> Deploy ESS/Trellix (formerly McAfee) endpoint '
        'protection managed through ePO (ePolicy Orchestrator). Configure policies for '
        'real-time scanning, on-access scanning, and scheduled full system scans. Set ePO '
        'to alert on detection events and quarantine actions.</p>'
    ),

    "si-3-1": (
        '<p>Manage malicious code protection centrally — deploy, configure, monitor, and '
        'update antimalware from a single management console.</p>'
        '<p><strong>Example 1:</strong> Use the Microsoft 365 Defender portal as your '
        'central management point for Defender Antivirus across all endpoints. View '
        'detection alerts, quarantined files, and protection status from a single dashboard. '
        'Push policy changes to all machines simultaneously.</p>'
        '<p><strong>Example 2:</strong> In an ESS/Trellix environment, use ePO to centrally '
        'manage all endpoint protection agents. Create policies, push signature updates, '
        'generate compliance reports, and investigate detections from one console.</p>'
    ),

    "si-3-2": (
        '<p>Ensure antimalware definitions and signatures update automatically — your '
        'protection is only as good as your latest definitions.</p>'
        '<p><strong>Example 1:</strong> Configure Microsoft Defender to receive definition '
        'updates from Microsoft Update, WSUS, or a file share. Set the update frequency '
        'to at least every 4 hours via GPO. Monitor update status in the Defender portal '
        'and alert on machines with definitions older than 48 hours.</p>'
        '<p><strong>Example 2:</strong> Configure ESS/Trellix ePO to push DAT file '
        'updates automatically as soon as they are available. Set the update check interval '
        'to 1 hour. Machines that miss updates are flagged in the ePO compliance dashboard '
        'for follow-up.</p>'
    ),

    "si-3-3": (
        '<p>Non-privileged users should not be able to disable or modify malicious code '
        'protection on their machines.</p>'
        '<p><strong>Example 1:</strong> Use GPO to lock down Microsoft Defender settings. '
        'Set "Turn off Microsoft Defender Antivirus" to "Not Configured" (meaning it stays '
        'on) and enable tamper protection so even local administrators cannot disable '
        'real-time protection.</p>'
        '<p><strong>Example 2:</strong> In your ESS/Trellix ePO policies, enable the '
        'self-protection feature and set a password for uninstalling or modifying the agent. '
        'Regular users cannot disable, uninstall, or change the antivirus configuration.</p>'
    ),

    "si-3-4": (
        '<p>Only privileged users (administrators) should be able to update malicious code '
        'protection software and definitions.</p>'
        '<p><strong>Example 1:</strong> Configure antimalware updates to come only from your '
        'central management server (WSUS, SCCM, ePO). Disable the ability for end users to '
        'manually trigger or control definition updates. Updates happen silently in the '
        'background via enterprise management.</p>'
        '<p><strong>Example 2:</strong> Use role-based access in your antimalware management '
        'console to restrict who can approve and push definition updates. Only your security '
        'team and IT administrators have the permissions to modify update policies.</p>'
    ),

    "si-3-5": (
        '<p>Scan removable media (USB drives, external hard drives) for malicious code '
        'before allowing access to the files on them.</p>'
        '<p><strong>Example 1:</strong> Configure Microsoft Defender via GPO to automatically '
        'scan removable drives when they are connected. Enable "Scan removable drives during '
        'full scan" and consider enabling the on-access scan for removable media.</p>'
        '<p><strong>Example 2:</strong> Deploy a dedicated malware scanning kiosk where '
        'all removable media must be scanned before being connected to any production '
        'system. The kiosk runs multiple antivirus engines for comprehensive scanning.</p>'
    ),

    "si-3-6": (
        '<p>Periodically test your malicious code protection to verify it actually detects '
        'threats — do not just assume it works because it is installed.</p>'
        '<p><strong>Example 1:</strong> Use the EICAR test file to verify your antivirus is '
        'working. Download the EICAR test string from eicar.org — it is a harmless file '
        'that every legitimate antivirus product detects as "malware." If your AV does not '
        'alert, you have a problem.</p>'
        '<p><strong>Example 2:</strong> Conduct periodic red team exercises or phishing '
        'simulations that include benign payload delivery. Track whether your endpoint '
        'protection detects and blocks the simulated attacks. Use the results to tune '
        'your detection policies.</p>'
    ),

    "si-3-7": (
        '<p>Use behavior-based detection (not just signature-based) to catch new, unknown '
        'malware that does not match existing signatures.</p>'
        '<p><strong>Example 1:</strong> Enable Microsoft Defender&apos;s cloud-delivered '
        'protection and "Block at First Sight" feature. These use machine learning and '
        'behavioral analysis in the Microsoft cloud to detect new threats that do not have '
        'signatures yet. Suspicious files are analyzed in real time.</p>'
        '<p><strong>Example 2:</strong> Deploy an EDR solution (CrowdStrike Falcon, Microsoft '
        'Defender for Endpoint) that monitors process behavior — unusual parent-child '
        'process relationships, suspicious file modifications, and anomalous network '
        'connections — rather than just matching file signatures.</p>'
    ),

    "si-3-8": (
        '<p>Detect unauthorized operating system commands issued to your systems, which '
        'could indicate an attacker has gained command-line access.</p>'
        '<p><strong>Example 1:</strong> Enable PowerShell Script Block Logging and Module '
        'Logging via GPO. Forward these logs to your SIEM and create detection rules for '
        'suspicious commands — encoded PowerShell, credential harvesting tools (Mimikatz), '
        'or unusual use of certutil, bitsadmin, or net commands.</p>'
        '<p><strong>Example 2:</strong> Deploy a host-based IDS (like OSSEC or Wazuh) that '
        'monitors command execution on servers. Configure rules to alert on commands commonly '
        'used by attackers — whoami, net user, net group, nltest, dsquery — especially when '
        'run by non-admin accounts.</p>'
    ),

    "si-3-9": (
        '<p>Authenticate remote commands before executing them to prevent attackers from '
        'sending unauthorized instructions to your systems.</p>'
        '<p><strong>Example 1:</strong> Configure Windows Remote Management (WinRM) to '
        'require Kerberos authentication. Remote PowerShell sessions must authenticate '
        'with valid domain credentials before any commands are accepted. Do not allow '
        'basic authentication or unencrypted connections.</p>'
        '<p><strong>Example 2:</strong> For SSH access to Linux servers, disable password '
        'authentication and require SSH key-based authentication with a passphrase. This '
        'ensures only users with the correct private key can issue remote commands.</p>'
    ),

    "si-3-10": (
        '<p>Analyze malicious code in detail to understand what it does, how it works, and '
        'what indicators of compromise it leaves behind.</p>'
        '<p><strong>Example 1:</strong> When your antivirus quarantines a suspicious file, '
        'submit it to VirusTotal for multi-engine analysis and behavioral analysis. Review '
        'the report for network indicators (C2 domains, IP addresses) and file indicators '
        '(hashes, mutexes) that you can add to your SIEM detection rules.</p>'
        '<p><strong>Example 2:</strong> Set up a malware analysis sandbox (Cuckoo Sandbox, '
        'ANY.RUN) on an isolated network. Detonate suspicious files in the sandbox and '
        'analyze their behavior — what files they create, what registry keys they modify, '
        'what network connections they make. Use findings to improve your defenses.</p>'
    ),

    "si-4": (
        '<p>System monitoring means watching your systems and network for signs of attack, '
        'misuse, or malfunction. Think of it as having security cameras for your IT '
        'environment — you need to watch what is happening.</p>'
        '<p><strong>Example 1:</strong> Deploy a SIEM (Microsoft Sentinel, Splunk) that '
        'collects logs from your firewalls, servers, endpoints, and cloud services. Create '
        'detection rules for common attack patterns — brute force login attempts, privilege '
        'escalation, lateral movement, data exfiltration.</p>'
        '<p><strong>Example 2:</strong> Enable Windows Security Auditing via GPO to log '
        'account logons, process creation, privilege use, and policy changes. Forward these '
        'logs to your SIEM. Without these audit logs enabled, you are blind to what is '
        'happening on your endpoints.</p>'
    ),

    "si-4-1": (
        '<p>Deploy intrusion detection across your entire system, not just at the perimeter. '
        'Attackers who bypass perimeter defenses must still be detected inside.</p>'
        '<p><strong>Example 1:</strong> Deploy network IDS sensors (Suricata, Snort) at your '
        'perimeter, between major network segments, and in front of critical servers. Each '
        'sensor feeds alerts to your central SIEM for correlation. Do not just watch the '
        'front door — watch the hallways too.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft Defender for Endpoint as a host-based '
        'IDS on every workstation and server. It detects threats on the endpoint itself, '
        'regardless of how the attacker got in — phishing, USB drive, compromised website, '
        'or insider threat.</p>'
    ),

    "si-4-2": (
        '<p>Use automated tools that can analyze events in real time and alert you '
        'immediately when they detect suspicious activity.</p>'
        '<p><strong>Example 1:</strong> Configure your SIEM (Sentinel, Splunk) with '
        'real-time correlation rules. When the SIEM sees a failed login followed by a '
        'successful login from a different country within 5 minutes (impossible travel), '
        'it generates an alert immediately — not during the next morning&apos;s log review.</p>'
        '<p><strong>Example 2:</strong> Enable automated investigation and response in '
        'Microsoft Defender for Endpoint. When a high-confidence threat is detected, the '
        'system automatically isolates the machine, collects forensic data, and creates '
        'an incident — all within seconds of detection.</p>'
    ),

    "si-4-3": (
        '<p>Integrate your monitoring tools so they share data and provide a unified view '
        'of your security posture rather than operating as isolated silos.</p>'
        '<p><strong>Example 1:</strong> Configure your firewall, IDS, endpoint protection, '
        'and cloud services to all feed logs into your SIEM. Create correlation rules that '
        'connect events across sources — a firewall alert plus an endpoint detection plus '
        'an authentication anomaly together may indicate a coordinated attack.</p>'
        '<p><strong>Example 2:</strong> Integrate Microsoft Defender for Endpoint with '
        'Microsoft Sentinel. Endpoint detections automatically appear in Sentinel, where '
        'they can be correlated with Azure AD sign-in logs, email security events, and '
        'cloud app activity for a complete picture of an incident.</p>'
    ),

    "si-4-4": (
        '<p>Monitor both inbound and outbound network traffic for threats. Many organizations '
        'only watch incoming traffic, but outbound monitoring is critical for detecting '
        'data exfiltration and command-and-control communications.</p>'
        '<p><strong>Example 1:</strong> Configure your firewall to log all outbound traffic '
        'and send those logs to your SIEM. Create alerts for unusual outbound patterns — '
        'large data transfers to external IPs, connections to known C2 servers, or traffic '
        'to countries you do not do business with.</p>'
        '<p><strong>Example 2:</strong> Enable DNS logging and monitor DNS queries for '
        'indicators of compromise — queries to dynamic DNS providers, domains registered '
        'in the last 30 days (newly registered domains), or unusually long domain names '
        'that may indicate DNS tunneling.</p>'
    ),

    "si-4-5": (
        '<p>Configure your monitoring systems to generate alerts when specific indicators '
        'of compromise or suspicious events occur — do not rely on humans scanning through '
        'logs manually.</p>'
        '<p><strong>Example 1:</strong> In your SIEM, create alert rules for high-priority '
        'events: account lockouts, privileged account usage outside business hours, '
        'new administrative accounts created, security software disabled, and connections '
        'to threat intelligence indicators. Route alerts to your security team&apos;s phone.</p>'
        '<p><strong>Example 2:</strong> Configure Microsoft Defender for Endpoint to send '
        'email and SMS alerts for high and critical severity detections. Integrate with '
        'your ticketing system (ServiceNow, Jira) so every alert automatically creates '
        'a tracking ticket that must be investigated and resolved.</p>'
    ),

    "si-4-6": (
        '<p>Restrict who can access monitoring tools and data — non-privileged users should '
        'not be able to see security alerts or tamper with monitoring configurations.</p>'
        '<p><strong>Example 1:</strong> Use role-based access control in your SIEM to limit '
        'who can view security events, create/modify detection rules, and access incident '
        'data. Regular IT staff get read-only access to their systems&apos; logs. Only your '
        'security team gets full access to all events and configuration.</p>'
        '<p><strong>Example 2:</strong> In Microsoft Sentinel, use Azure RBAC to control '
        'access. Assign the "Microsoft Sentinel Reader" role to operations staff and '
        '"Microsoft Sentinel Contributor" only to your security analysts. Audit who has '
        'access to the SIEM workspace quarterly.</p>'
    ),

    "si-4-7": (
        '<p>Configure automated responses to certain types of suspicious events — the system '
        'should react faster than a human can for high-confidence threats.</p>'
        '<p><strong>Example 1:</strong> Set up automated playbooks in Microsoft Sentinel '
        '(Logic Apps) that automatically disable a user account when impossible travel is '
        'detected, or automatically block an IP address in the firewall when a brute force '
        'attack is confirmed.</p>'
        '<p><strong>Example 2:</strong> Configure Microsoft Defender for Endpoint to '
        'automatically isolate a machine from the network when a high-confidence ransomware '
        'detection occurs. The machine stays online for investigation but cannot communicate '
        'with other machines on your network.</p>'
    ),

    "si-4-8": (
        '<p>Protect the integrity and availability of your monitoring information — if an '
        'attacker can delete or alter your logs, they can cover their tracks.</p>'
        '<p><strong>Example 1:</strong> Send logs to a write-once storage location (WORM '
        'storage or immutable blob storage in Azure) where they cannot be modified or '
        'deleted, even by administrators. This ensures forensic evidence is preserved.</p>'
        '<p><strong>Example 2:</strong> Configure your SIEM to alert if log collection '
        'stops from any source. If a server suddenly stops sending logs, it could mean '
        'the server is down — or it could mean an attacker disabled logging. Either way, '
        'you need to investigate immediately.</p>'
    ),

    "si-4-9": (
        '<p>Periodically test your monitoring tools to verify they are actually detecting '
        'threats — run test scenarios and confirm alerts are generated.</p>'
        '<p><strong>Example 1:</strong> Run regular purple team exercises where your red '
        'team performs known attack techniques (from the MITRE ATT&CK framework) and your '
        'blue team verifies that each technique triggers the expected detection in the SIEM.</p>'
        '<p><strong>Example 2:</strong> Use automated testing tools like Atomic Red Team '
        'to execute individual ATT&CK techniques on test systems and verify your endpoint '
        'detection and SIEM rules catch them. Run these tests monthly and document any '
        'detection gaps you discover.</p>'
    ),

    "si-4-10": (
        '<p>Maintain visibility into encrypted communications to the extent necessary for '
        'monitoring. Encryption can hide malicious activity if you cannot inspect the '
        'decrypted traffic.</p>'
        '<p><strong>Example 1:</strong> Deploy TLS inspection (SSL decryption) on your '
        'web proxy or next-gen firewall. The proxy decrypts HTTPS traffic, inspects it '
        'for threats, and re-encrypts it. This lets you see inside encrypted web traffic '
        'without users noticing any difference.</p>'
        '<p><strong>Example 2:</strong> For internal traffic, use endpoint-based monitoring '
        '(EDR) that can see data before encryption and after decryption. The EDR agent on '
        'the endpoint sees the plaintext data even when the network traffic is encrypted, '
        'providing visibility without breaking encryption in transit.</p>'
    ),

    "si-4-11": (
        '<p>Analyze communications traffic patterns — not just content — for anomalies that '
        'could indicate an attack. Even encrypted traffic has patterns (volume, timing, '
        'destinations) that can reveal threats.</p>'
        '<p><strong>Example 1:</strong> Use NetFlow analysis (SolarWinds NTA, Cisco '
        'Stealthwatch) to baseline normal traffic patterns and alert on anomalies. A '
        'workstation that suddenly starts communicating with hundreds of internal hosts '
        'might be performing reconnaissance or spreading malware.</p>'
        '<p><strong>Example 2:</strong> Monitor for beaconing patterns in your firewall '
        'logs. Command-and-control malware often "phones home" at regular intervals. '
        'Look for connections to the same external IP at suspiciously consistent time '
        'intervals — this is a strong indicator of compromise.</p>'
    ),

    "si-4-12": (
        '<p>Generate automated alerts when organizational security policies are violated — '
        'not just when external attacks occur.</p>'
        '<p><strong>Example 1:</strong> Configure your SIEM to alert when security policies '
        'are violated: software installed without approval, firewall rules changed outside '
        'maintenance windows, user accounts created by non-authorized personnel, or '
        'sensitive data shared to external recipients.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft Purview Insider Risk Management to '
        'automatically flag policy violations like bulk file downloads, printing of '
        'sensitive documents before a resignation, or emailing CUI to personal email '
        'accounts. Alerts are routed to your security team for investigation.</p>'
    ),

    "si-4-13": (
        '<p>Look for patterns in traffic and events over time — single events may look '
        'normal, but patterns can reveal sophisticated attacks that operate slowly.</p>'
        '<p><strong>Example 1:</strong> Configure your SIEM to correlate events over time '
        'windows. A single failed login is normal. But 50 failed logins across 20 different '
        'accounts over 3 hours from the same source IP is a password spray attack. Set '
        'correlation rules to catch these patterns.</p>'
        '<p><strong>Example 2:</strong> Use UEBA (User and Entity Behavior Analytics) in '
        'your SIEM to build baselines for each user and detect deviations. If a user who '
        'normally accesses 5 files per day suddenly downloads 500 files, that anomaly '
        'triggers an investigation even though each individual access was authorized.</p>'
    ),

    "si-4-14": (
        '<p>Deploy wireless intrusion detection to identify rogue access points, '
        'unauthorized wireless connections, and wireless-based attacks.</p>'
        '<p><strong>Example 1:</strong> Configure your enterprise wireless controller '
        '(Cisco, Aruba) to continuously scan for rogue access points. When an unknown '
        'SSID is detected on your premises, the system alerts security and can optionally '
        'send deauthentication frames to contain the rogue AP.</p>'
        '<p><strong>Example 2:</strong> Use a dedicated wireless IDS sensor (or your '
        'existing APs in monitor mode) to detect wireless attacks — deauthentication '
        'floods, evil twin attacks, WPA key cracking attempts. Forward wireless security '
        'events to your SIEM for correlation with wired network events.</p>'
    ),

    "si-4-15": (
        '<p>Monitor the connection between your wireless and wired networks to detect '
        'threats that use wireless access as an entry point into your wired infrastructure.</p>'
        '<p><strong>Example 1:</strong> Monitor all traffic crossing from your wireless VLAN '
        'to your wired network through a firewall or IDS sensor at the junction point. '
        'Apply the same inspection policies to wireless-to-wired traffic that you apply '
        'to internet-to-internal traffic.</p>'
        '<p><strong>Example 2:</strong> Require 802.1X authentication for wireless clients '
        'and monitor authentication events. A device that authenticates on the wireless '
        'network and immediately starts scanning wired subnets should trigger an alert '
        'in your SIEM.</p>'
    ),

    "si-4-16": (
        '<p>Correlate monitoring information from multiple sources to build a comprehensive '
        'picture of security events. No single source tells the whole story.</p>'
        '<p><strong>Example 1:</strong> In your SIEM, create multi-source correlation rules. '
        'Combine Azure AD sign-in logs + endpoint detections + firewall logs + email security '
        'events. A phishing email (email log) followed by a credential login from a new '
        'location (Azure AD) followed by data download (endpoint) tells a story that no '
        'single source reveals.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft 365 Defender&apos;s unified incident view '
        'that automatically correlates email, endpoint, identity, and cloud app alerts '
        'into a single incident. This cross-product correlation reveals multi-stage attacks '
        'that would be invisible if you looked at each product independently.</p>'
    ),

    "si-4-17": (
        '<p>Integrate your monitoring data with broader situational awareness — connecting '
        'cyber events with physical security events, threat intelligence, and operational '
        'context.</p>'
        '<p><strong>Example 1:</strong> Feed physical access control logs (badge swipes) '
        'into your SIEM alongside cyber events. If someone authenticates to the network '
        'from the office but their badge shows they never entered the building, that is '
        'a strong indicator their credentials are compromised.</p>'
        '<p><strong>Example 2:</strong> Subscribe to CISA alerts and sector-specific threat '
        'intelligence feeds. When a threat advisory targets your industry, increase your '
        'monitoring sensitivity for the specific indicators of compromise mentioned in '
        'the advisory.</p>'
    ),

    "si-4-18": (
        '<p>Monitor for covert exfiltration — attackers using hidden channels like DNS '
        'tunneling, steganography, or encrypted tunnels to sneak data out of your network.</p>'
        '<p><strong>Example 1:</strong> Monitor DNS query logs for signs of DNS tunneling: '
        'unusually long domain names, high volume of TXT record queries to a single domain, '
        'or domains with high entropy in their subdomains. Configure your SIEM to alert on '
        'these patterns.</p>'
        '<p><strong>Example 2:</strong> Use a network DLP solution that inspects outbound '
        'traffic for sensitive data patterns, even in unusual protocols. Look for CUI data '
        'patterns in HTTP headers, ICMP payloads, or DNS queries that should not normally '
        'contain sensitive data.</p>'
    ),

    "si-4-19": (
        '<p>When monitoring systems, consider the risk to individuals whose data may be '
        'collected — ensure monitoring does not disproportionately invade privacy.</p>'
        '<p><strong>Example 1:</strong> Define clear boundaries for employee monitoring in '
        'your acceptable use policy. Specify what is monitored (network traffic, email '
        'headers) and what is not (personal device content off the corporate network). '
        'Get legal review and employee acknowledgment.</p>'
        '<p><strong>Example 2:</strong> Anonymize or pseudonymize monitoring data where '
        'possible until an investigation is warranted. Your SIEM can track user IDs '
        'internally but only reveal the actual identity when a security analyst opens '
        'a formal investigation with manager approval.</p>'
    ),

    "si-4-20": (
        '<p>Apply heightened monitoring to privileged users (administrators, security '
        'staff) because their elevated access makes them higher-risk targets and potential '
        'insider threats.</p>'
        '<p><strong>Example 1:</strong> Enable enhanced auditing for all administrative '
        'accounts. Log every action they take — every command, every file accessed, every '
        'configuration change. Forward these logs to a SIEM instance that the admins being '
        'monitored cannot access or modify.</p>'
        '<p><strong>Example 2:</strong> Use Azure AD Privileged Identity Management (PIM) '
        'with session recording. When an admin activates a privileged role, their entire '
        'session is recorded. Require justification for each privilege activation and '
        'send notifications to security leadership.</p>'
    ),

    "si-4-21": (
        '<p>Apply enhanced monitoring during probationary periods for new employees, '
        'contractors, or users who have been flagged for security concerns.</p>'
        '<p><strong>Example 1:</strong> Configure your SIEM to apply a "heightened '
        'monitoring" tag to user accounts during the first 90 days of employment. Additional '
        'alert rules trigger for these accounts — large file downloads, access outside '
        'business hours, or attempts to access restricted systems.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft Purview Insider Risk Management to '
        'create a policy that applies increased scrutiny to users flagged by HR — those '
        'on performance improvement plans or who have given notice of resignation. Monitor '
        'for bulk data downloads and unusual sharing patterns.</p>'
    ),

    "si-4-22": (
        '<p>Detect unauthorized network services — software that is listening on network '
        'ports without approval, which could be backdoors or unauthorized applications.</p>'
        '<p><strong>Example 1:</strong> Run regular port scans of your internal network '
        'using Nmap or your vulnerability scanner. Compare results against your approved '
        'services baseline. Any new, unauthorized listening port triggers an investigation.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft Defender for Endpoint to monitor '
        'listening services on all enrolled machines. The "Device discovery" feature '
        'identifies all network services, and you can alert on any service that is not '
        'in your approved software inventory.</p>'
    ),

    "si-4-23": (
        '<p>Deploy host-based monitoring on individual devices — not just network-level '
        'monitoring — to detect threats that do not generate network traffic.</p>'
        '<p><strong>Example 1:</strong> Deploy Sysmon on all Windows machines to capture '
        'detailed process creation, file creation, registry modification, and network '
        'connection events. Forward Sysmon logs to your SIEM for analysis. Sysmon captures '
        'activity that standard Windows event logs miss.</p>'
        '<p><strong>Example 2:</strong> Use an EDR solution (CrowdStrike, Defender for '
        'Endpoint) on every server and workstation. The EDR agent monitors file system '
        'changes, process behavior, registry modifications, and memory activity directly '
        'on the host — catching threats that network monitoring cannot see.</p>'
    ),

    "si-4-24": (
        '<p>Monitor for indicators of compromise (IOCs) — specific technical artifacts '
        '(file hashes, IP addresses, domain names) that indicate a known threat is present.</p>'
        '<p><strong>Example 1:</strong> Subscribe to threat intelligence feeds (CISA AIS, '
        'Anomali, Recorded Future) and integrate them with your SIEM. When a known '
        'malicious IP or domain appears in your logs, the SIEM automatically flags it '
        'as a potential compromise.</p>'
        '<p><strong>Example 2:</strong> Configure Microsoft Defender for Endpoint to '
        'use custom IOC lists. Upload file hashes, URLs, and IP addresses from threat '
        'intelligence reports. The agent checks all endpoint activity against these '
        'indicators and alerts or blocks as configured.</p>'
    ),

    "si-4-25": (
        '<p>Optimize your network traffic analysis to focus monitoring resources on the '
        'most important traffic and reduce alert fatigue from false positives.</p>'
        '<p><strong>Example 1:</strong> Tune your IDS rules to your specific environment. '
        'Disable rules that do not apply (like Linux-specific rules on a Windows-only '
        'network) and adjust thresholds on remaining rules to reduce false positives while '
        'maintaining detection of real threats.</p>'
        '<p><strong>Example 2:</strong> Use machine learning-based network detection (like '
        'Darktrace or Vectra) that builds a model of your normal traffic patterns and '
        'alerts on true deviations rather than matching static signatures. This reduces '
        'alert fatigue while improving detection of novel threats.</p>'
    ),

    "si-5": (
        '<p>Stay informed about security alerts, advisories, and directives from authoritative '
        'sources like CISA, vendor security bulletins, and US-CERT. Then act on them.</p>'
        '<p><strong>Example 1:</strong> Subscribe to CISA alerts (us-cert.cisa.gov), '
        'Microsoft Security Response Center bulletins, and vendor-specific security '
        'advisories for all products in your environment. Assign someone to review these '
        'daily and assess applicability to your systems.</p>'
        '<p><strong>Example 2:</strong> When a CISA directive is issued (like a Binding '
        'Operational Directive for federal agencies), review it for applicability even if '
        'you are not a federal agency. These directives often highlight critical '
        'vulnerabilities that affect everyone, not just the government.</p>'
    ),

    "si-5-1": (
        '<p>Automate the receipt and distribution of security alerts so your team does not '
        'miss critical advisories because someone was on vacation.</p>'
        '<p><strong>Example 1:</strong> Set up automated feeds from CISA, Microsoft MSRC, '
        'and NVD into your ticketing system. When a critical advisory is published, a ticket '
        'is automatically created and assigned to the appropriate team for assessment '
        'and response.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft Defender Vulnerability Management&apos;s '
        'security recommendations feature, which automatically identifies applicable '
        'advisories for your enrolled devices and prioritizes them based on your specific '
        'exposure. No manual advisory review needed.</p>'
    ),

    "si-6": (
        '<p>Periodically verify that your security and privacy functions are working '
        'correctly — do not just deploy them and forget about them.</p>'
        '<p><strong>Example 1:</strong> Test your access control mechanisms quarterly. Try '
        'to access resources you should not have access to, verify that disabled accounts '
        'are actually disabled, and confirm that MFA is required where it should be. '
        'Document the test results.</p>'
        '<p><strong>Example 2:</strong> Verify your encryption is working by checking TLS '
        'configurations (use tools like SSL Labs Server Test), confirming BitLocker is '
        'active on all laptops (Get-BitLockerVolume in PowerShell), and testing that '
        'email encryption policies are enforcing as expected.</p>'
    ),

    "si-6-1": (
        '<p>When security function verification fails — when you discover a security '
        'mechanism is not working — notify the appropriate personnel immediately.</p>'
        '<p><strong>Example 1:</strong> Configure automated monitoring for your security '
        'tools. If antivirus stops reporting to the management console, if the SIEM stops '
        'receiving logs, or if the firewall enters a degraded state, an alert goes '
        'immediately to the security team and IT management.</p>'
        '<p><strong>Example 2:</strong> Create a runbook that defines who gets notified '
        'for different types of security function failures — CISO for critical failures '
        'like total SIEM outage, security lead for component failures like one server '
        'missing AV, and IT ops for infrastructure issues like NTP sync failures.</p>'
    ),

    "si-6-2": (
        '<p>Use automation to support distributed security testing across your environment '
        'rather than relying on manual checks of each system.</p>'
        '<p><strong>Example 1:</strong> Use automated configuration scanning (like SCAP '
        'scanners or Azure Policy) to verify security settings across all systems '
        'simultaneously. The scan checks that every machine meets your security baseline '
        'and reports non-compliant systems.</p>'
        '<p><strong>Example 2:</strong> Deploy automated compliance checking through '
        'Microsoft Intune or SCCM compliance baselines. Devices are continuously evaluated '
        'against required configurations (BitLocker, firewall, AV status), and non-compliant '
        'devices are automatically flagged and optionally restricted.</p>'
    ),

    "si-6-3": (
        '<p>Report the results of security function verification to appropriate personnel '
        'so leadership knows whether controls are working.</p>'
        '<p><strong>Example 1:</strong> Generate monthly security control health reports '
        'from your SIEM and vulnerability scanner showing: patch compliance rates, antivirus '
        'coverage, firewall rule review status, and access control audit results. Present '
        'these to your CISO and system owner.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft Secure Score as a continuously updated '
        'report card for your M365 security controls. Share the score and improvement '
        'recommendations with leadership monthly. Track the score trend over time to show '
        'whether your security posture is improving.</p>'
    ),

    "si-7": (
        '<p>Detect unauthorized changes to software, firmware, and data. If an attacker '
        'modifies a system file, replaces firmware, or alters database records, you need '
        'to know about it.</p>'
        '<p><strong>Example 1:</strong> Deploy a file integrity monitoring (FIM) tool like '
        'Tripwire, OSSEC, or the FIM capability built into Microsoft Defender for Endpoint. '
        'Monitor critical system files, configuration files, and executables. Any '
        'unauthorized change triggers an alert.</p>'
        '<p><strong>Example 2:</strong> Enable Windows Resource Protection and System File '
        'Checker (sfc /scannow) as part of your baseline security checks. These Windows '
        'built-in features detect when protected system files have been modified or replaced '
        'and can automatically restore the original versions.</p>'
    ),

    "si-7-1": (
        '<p>Perform integrity checks at specific points — startup, defined intervals, or '
        'when specific events occur — to detect unauthorized changes promptly.</p>'
        '<p><strong>Example 1:</strong> Configure your FIM tool to check critical file '
        'integrity every hour. Critical files include: boot files, OS kernel, security '
        'tool executables, and configuration files (web.config, httpd.conf, registry hives). '
        'Changes outside maintenance windows trigger immediate alerts.</p>'
        '<p><strong>Example 2:</strong> Use UEFI Secure Boot to verify firmware and '
        'bootloader integrity at every system startup. If the boot chain has been modified '
        '(by a bootkit or rootkit), the system refuses to boot and alerts the administrator.</p>'
    ),

    "si-7-2": (
        '<p>Automate notifications when integrity violations are detected so the security '
        'team is alerted immediately.</p>'
        '<p><strong>Example 1:</strong> Configure your FIM solution to send immediate email '
        'and SMS alerts to the security team when critical files are modified. Include the '
        'file path, what changed, the user/process that made the change, and a timestamp.</p>'
        '<p><strong>Example 2:</strong> Forward FIM alerts to your SIEM and create an '
        'automated response playbook. When a critical system binary is modified, the SIEM '
        'automatically opens an incident ticket, increases monitoring on the affected '
        'system, and notifies the incident response team.</p>'
    ),

    "si-7-3": (
        '<p>Manage integrity monitoring tools from a central console to ensure consistent '
        'coverage and configuration across all systems.</p>'
        '<p><strong>Example 1:</strong> Use Tripwire Enterprise or OSSEC Manager to centrally '
        'configure, deploy, and manage file integrity monitoring policies across all servers '
        'and workstations. One console shows compliance status for every monitored system.</p>'
        '<p><strong>Example 2:</strong> In Microsoft Defender for Endpoint, use the FIM '
        'feature that centrally reports file changes across all enrolled devices through '
        'the Defender portal. You get a single view of all integrity changes across your '
        'fleet without managing individual agent configurations.</p>'
    ),

    "si-7-4": (
        '<p>Use tamper-evident packaging for software and hardware shipments so you can '
        'detect if something was altered during transit.</p>'
        '<p><strong>Example 1:</strong> When receiving new hardware (servers, networking '
        'equipment), verify that tamper-evident seals on the packaging are intact before '
        'accepting delivery. Photograph the seals and packaging as part of your receiving '
        'process. Report any broken seals to the vendor and your security team.</p>'
        '<p><strong>Example 2:</strong> For software delivered on physical media (like '
        'firmware update USBs from vendors), verify the hash of the files against the '
        'vendor&apos;s published hash values before installing. If the hashes do not match, '
        'the media may have been tampered with during shipping.</p>'
    ),

    "si-7-5": (
        '<p>When an integrity violation is detected, the system should automatically take '
        'corrective action — not just alert and wait for someone to respond manually.</p>'
        '<p><strong>Example 1:</strong> Configure Windows File Protection to automatically '
        'restore system files that have been modified. If malware replaces a system DLL, '
        'Windows automatically restores the original from its cache.</p>'
        '<p><strong>Example 2:</strong> In a containerized environment (Docker/Kubernetes), '
        'configure the orchestrator to automatically restart containers with modified '
        'file systems. Since container images are immutable, restarting restores the known-'
        'good state automatically and alerts your monitoring team.</p>'
    ),

    "si-7-6": (
        '<p>Use cryptographic mechanisms — digital signatures, cryptographic hashes — to '
        'verify software and firmware integrity rather than relying on simple checksums.</p>'
        '<p><strong>Example 1:</strong> Verify GPG or Authenticode digital signatures on '
        'all software before installation. On Windows, check that executables are signed '
        'by the expected publisher. Use "Get-AuthenticodeSignature" in PowerShell to verify '
        'signatures programmatically.</p>'
        '<p><strong>Example 2:</strong> Before applying firmware updates to network devices, '
        'verify the firmware image&apos;s SHA-256 hash against the hash published on the '
        'vendor&apos;s secure download site. Never install firmware without hash verification.</p>'
    ),

    "si-7-7": (
        '<p>Integrate integrity detection with your incident response process so that '
        'integrity violations automatically trigger investigation and containment.</p>'
        '<p><strong>Example 1:</strong> Configure your SIEM so that file integrity alerts '
        'automatically create high-priority incident tickets in your ITSM tool (ServiceNow, '
        'Jira). The incident workflow includes steps for investigation, containment, '
        'remediation, and root cause analysis.</p>'
        '<p><strong>Example 2:</strong> In Microsoft Defender for Endpoint, integrity '
        'violations trigger automated investigation. The system collects forensic evidence, '
        'identifies the attack chain, and recommends or automatically takes remediation '
        'actions like quarantining the file or isolating the machine.</p>'
    ),

    "si-7-8": (
        '<p>When significant integrity events occur, generate audit records with enough '
        'detail for forensic investigation.</p>'
        '<p><strong>Example 1:</strong> Configure your FIM to log: what file changed, the '
        'previous and new hash values, what user or process made the change, the timestamp, '
        'and the machine name. Forward these audit records to your SIEM and retain them for '
        'your required audit period (typically one year or more).</p>'
        '<p><strong>Example 2:</strong> Enable Windows security auditing for file system '
        'changes to critical directories. Configure SACLs (System Access Control Lists) on '
        'directories containing executables and configuration files to log all modification '
        'attempts, successful or failed.</p>'
    ),

    "si-7-9": (
        '<p>Verify the integrity of the boot process — from firmware through bootloader '
        'to operating system kernel — to detect rootkits and bootkits that hide below the '
        'OS level.</p>'
        '<p><strong>Example 1:</strong> Enable UEFI Secure Boot on all systems and verify '
        'it is active via GPO reporting or your asset management tool. Secure Boot checks '
        'digital signatures on every component in the boot chain, preventing unsigned '
        'or modified code from loading during startup.</p>'
        '<p><strong>Example 2:</strong> Use Windows Defender System Guard with hardware-'
        'based attestation. The TPM measures each boot component and reports the '
        'measurements to a cloud attestation service. If the boot chain has been tampered '
        'with, the attestation fails and the machine is flagged as potentially compromised.</p>'
    ),

    "si-7-10": (
        '<p>Protect boot firmware from unauthorized modification — firmware-level malware '
        'persists across OS reinstallations and is extremely difficult to detect.</p>'
        '<p><strong>Example 1:</strong> Enable the BIOS/UEFI write-protection feature on '
        'your systems. Most enterprise systems have a BIOS setting that prevents firmware '
        'updates without physical presence or an administrator password.</p>'
        '<p><strong>Example 2:</strong> Deploy systems with Intel Boot Guard enabled in the '
        'firmware. Boot Guard creates a hardware root of trust that verifies firmware '
        'integrity before any code executes. Even with physical access, an attacker cannot '
        'install a malicious firmware without the manufacturer&apos;s signing key.</p>'
    ),

    "si-7-11": (
        '<p>Run untrusted software in confined environments with limited privileges to '
        'contain any damage if the software turns out to be malicious.</p>'
        '<p><strong>Example 1:</strong> Use Windows Sandbox or Application Guard to open '
        'untrusted files and browse untrusted websites in an isolated, disposable container. '
        'When the sandbox is closed, any malware inside is destroyed.</p>'
        '<p><strong>Example 2:</strong> Run third-party applications in Docker containers '
        'with minimal privileges — no root access, read-only file systems, limited network '
        'access. If the application is compromised, the container limits what the attacker '
        'can do and prevents lateral movement.</p>'
    ),

    "si-7-12": (
        '<p>Verify the integrity of specific data elements — not just software files — to '
        'detect unauthorized modification of critical information.</p>'
        '<p><strong>Example 1:</strong> Implement database audit logging that tracks changes '
        'to critical data tables (user accounts, financial records, configuration data). '
        'Any modification is logged with the user, timestamp, old value, and new value. '
        'Alert on bulk modifications or changes from unexpected sources.</p>'
        '<p><strong>Example 2:</strong> Use blockchain or cryptographic hash chains to '
        'protect the integrity of audit logs and compliance records. Each entry is '
        'cryptographically linked to the previous entry, making it impossible to alter '
        'or delete records without detection.</p>'
    ),

    "si-7-13": (
        '<p>Execute critical code in protected environments where it cannot be tampered '
        'with by other processes or users.</p>'
        '<p><strong>Example 1:</strong> Use Windows Virtualization-Based Security (VBS) '
        'to run code integrity enforcement in a protected environment. Even if an attacker '
        'gains kernel-level access, they cannot disable code integrity protection because '
        'it runs in a separate VBS enclave.</p>'
        '<p><strong>Example 2:</strong> Use Intel SGX or AMD SEV to execute sensitive '
        'algorithms (encryption, authentication) in hardware-protected enclaves. The '
        'enclave&apos;s code and data are encrypted in memory and inaccessible to all other '
        'software, including the operating system.</p>'
    ),

    "si-7-14": (
        '<p>Restrict or prohibit the use of binary or machine-executable code from '
        'unverified sources — do not run random executables on your systems.</p>'
        '<p><strong>Example 1:</strong> Use Windows Defender Application Control (WDAC) to '
        'allow only signed, approved executables to run. Create a policy that allows '
        'Microsoft-signed binaries, your organization&apos;s signed software, and specifically '
        'approved third-party applications. Block everything else.</p>'
        '<p><strong>Example 2:</strong> Implement AppLocker via GPO to restrict executable '
        'files, scripts, and DLLs to approved locations and publishers. Users cannot run '
        'executables downloaded from the internet or saved to their desktop — only approved '
        'software from approved installation paths can execute.</p>'
    ),

    "si-7-15": (
        '<p>Verify the authenticity of code through digital signatures or other '
        'authentication mechanisms before allowing it to execute.</p>'
        '<p><strong>Example 1:</strong> Require Authenticode signatures on all executables '
        'in your environment. Configure GPO to only allow signed scripts (PowerShell '
        'execution policy set to AllSigned). Unsigned code is blocked from running.</p>'
        '<p><strong>Example 2:</strong> Verify GPG signatures on Linux packages before '
        'installation. Configure yum or apt to require signed packages and reject '
        'unsigned ones. Import only trusted GPG keys from verified sources.</p>'
    ),

    "si-7-16": (
        '<p>Set time limits on processes that execute without human supervision — long-'
        'running unsupervised processes may be hijacked or behave unexpectedly.</p>'
        '<p><strong>Example 1:</strong> Configure timeout limits on batch jobs and scheduled '
        'tasks. If a backup job normally takes 2 hours but has been running for 8 hours, '
        'terminate it and alert the operations team. The unusual runtime could indicate '
        'a problem or compromise.</p>'
        '<p><strong>Example 2:</strong> Set session timeout policies for automated service '
        'accounts. If a service account&apos;s session has been active for longer than the '
        'expected maximum (like a 24-hour limit for a daily processing account), force '
        'reauthentication or terminate the session.</p>'
    ),

    "si-7-17": (
        '<p>Runtime Application Self-Protection (RASP) embeds security checks directly '
        'inside the application so it can detect and block attacks from within, in '
        'real time.</p>'
        '<p><strong>Example 1:</strong> Deploy a RASP solution (like Contrast Security or '
        'Imperva RASP) inside your web applications. The RASP agent detects SQL injection, '
        'XSS, and other attacks from within the application context, blocking them even '
        'if they bypass your WAF.</p>'
        '<p><strong>Example 2:</strong> For .NET applications, enable the built-in request '
        'validation feature and configure custom input validation rules. The application '
        'itself rejects malicious input patterns rather than relying solely on external '
        'security devices to filter attacks.</p>'
    ),

    "si-8": (
        '<p>Protect your email system from spam, which is not just an annoyance but a '
        'primary delivery mechanism for phishing and malware.</p>'
        '<p><strong>Example 1:</strong> Configure Exchange Online Protection (EOP) in M365 '
        'with anti-spam policies. Set the spam confidence level (SCL) thresholds, enable '
        'bulk email filtering, and configure quarantine policies. Review quarantined '
        'messages regularly for false positives.</p>'
        '<p><strong>Example 2:</strong> Deploy a third-party email security gateway '
        '(Proofpoint, Mimecast, Barracuda) in front of your email system. Configure '
        'it to check sender reputation, validate SPF/DKIM/DMARC records, and scan '
        'attachments before delivery. Block emails from known spam sources.</p>'
    ),

    "si-8-1": (
        '<p>Manage spam protection centrally so all email flows through the same '
        'filtering with consistent policies.</p>'
        '<p><strong>Example 1:</strong> Use the Microsoft 365 Defender portal as your '
        'central management point for all email security — anti-spam, anti-phishing, safe '
        'links, and safe attachments. Manage all policies from one console rather than '
        'configuring filtering on individual mail servers.</p>'
        '<p><strong>Example 2:</strong> If using a third-party email gateway, route all '
        'inbound and outbound email through it. Update your MX records to point to the '
        'gateway, and block direct SMTP connections to your mail server from the internet. '
        'All email must pass through central filtering.</p>'
    ),

    "si-8-2": (
        '<p>Spam filters must update their detection databases automatically to catch '
        'new spam campaigns as they emerge.</p>'
        '<p><strong>Example 1:</strong> Verify that Exchange Online Protection updates '
        'its spam filtering intelligence automatically (it does by default as a cloud '
        'service). For on-premises solutions, configure automatic signature and rule '
        'updates at least every hour.</p>'
        '<p><strong>Example 2:</strong> If using a dedicated spam appliance, configure '
        'it to pull updated spam signatures, IP reputation lists, and URL databases '
        'automatically. Set the update check interval to 15 minutes for real-time '
        'protection against emerging campaigns.</p>'
    ),

    "si-8-3": (
        '<p>Your spam filter should continuously learn from new spam patterns and user '
        'feedback to improve detection accuracy over time.</p>'
        '<p><strong>Example 1:</strong> Enable the "Report Message" add-in in Outlook so '
        'users can report missed spam and false positives directly to Microsoft. Their '
        'reports feed into the machine learning models that improve Exchange Online '
        'Protection&apos;s detection accuracy.</p>'
        '<p><strong>Example 2:</strong> Configure your spam gateway to use a feedback loop '
        'where messages released from quarantine (false positives) and user-reported spam '
        '(false negatives) automatically adjust the filtering algorithms. Over time, the '
        'filter learns what your organization considers spam.</p>'
    ),

    "si-9": (
        '<p>Restrict who can input information into systems based on their authorization '
        'and the sensitivity of the data. Not everyone should be able to enter data into '
        'every system.</p>'
        '<p><strong>Example 1:</strong> Configure your financial system so only authorized '
        'accounts payable staff can enter payment transactions. Use role-based access '
        'control to restrict data entry forms to specific user groups. Separate data entry '
        'from data approval (segregation of duties).</p>'
        '<p><strong>Example 2:</strong> In your HR system, restrict who can create new '
        'employee records or modify salary information. Only HR administrators should have '
        'write access to personnel data. Other staff can view their own records but cannot '
        'modify them.</p>'
    ),

    "si-10": (
        '<p>Validate all input before your system processes it. Never trust data coming '
        'from users, external systems, or APIs — always check that it meets expected '
        'format, length, type, and range.</p>'
        '<p><strong>Example 1:</strong> Configure your web applications to validate all '
        'form inputs: check field lengths, data types (numbers are actually numbers), '
        'date formats, email address patterns, and reject any input containing SQL special '
        'characters or script tags. Use server-side validation, not just client-side.</p>'
        '<p><strong>Example 2:</strong> On your firewall and WAF, enable input validation '
        'rules that reject oversized HTTP headers, excessively long URLs, malformed Unicode, '
        'and requests with suspicious encoding. ModSecurity&apos;s Core Rule Set provides a '
        'solid baseline for HTTP input validation.</p>'
    ),

    "si-10-1": (
        '<p>Provide a manual override capability for input validation — sometimes '
        'legitimate but unusual data needs to be entered, and there should be an '
        'authorized override process.</p>'
        '<p><strong>Example 1:</strong> Build a supervisor override function in your data '
        'entry applications. If a value fails validation (like an unusually large purchase '
        'order amount), a supervisor can review the entry, provide justification, and '
        'approve the override. Log all overrides for audit.</p>'
        '<p><strong>Example 2:</strong> In your web application, allow administrators to '
        'temporarily whitelist specific input patterns that are being falsely rejected. '
        'Provide an admin interface that logs the override, the justification, and who '
        'approved it.</p>'
    ),

    "si-10-2": (
        '<p>Review and resolve input validation errors promptly — do not just reject bad '
        'input and ignore it. Understand why errors are occurring.</p>'
        '<p><strong>Example 1:</strong> Monitor input validation error logs in your SIEM. '
        'A sudden spike in validation errors from a single source could indicate an attack '
        '(SQL injection probing). A gradual increase might indicate a legitimate data '
        'format change that needs accommodation.</p>'
        '<p><strong>Example 2:</strong> Create a process for reviewing rejected inputs '
        'weekly. If legitimate users are consistently triggering validation errors, adjust '
        'your validation rules to accommodate valid data while still blocking malicious '
        'input. Document rule changes and the rationale.</p>'
    ),

    "si-10-3": (
        '<p>Your system should behave predictably when it receives invalid input — always '
        'producing the same response to the same invalid input, not crashing or behaving '
        'erratically.</p>'
        '<p><strong>Example 1:</strong> Test your applications with fuzzing tools (like '
        'OWASP ZAP&apos;s fuzzer) that send random and malformed input. The application should '
        'consistently return appropriate error messages without crashing, hanging, or '
        'exposing stack traces.</p>'
        '<p><strong>Example 2:</strong> Implement consistent error handling in your code '
        'that catches all exceptions from input processing and returns a standardized error '
        'response. Never let unhandled exceptions reach the user — they should see a '
        'generic error page, not a debug dump.</p>'
    ),

    "si-10-4": (
        '<p>Account for timing interactions in input validation — ensure that the order and '
        'timing of inputs cannot be manipulated to bypass validation checks.</p>'
        '<p><strong>Example 1:</strong> Implement CSRF (Cross-Site Request Forgery) tokens '
        'in your web applications. Each form submission includes a unique, time-limited '
        'token that prevents attackers from replaying or timing-manipulating form '
        'submissions.</p>'
        '<p><strong>Example 2:</strong> Use sequence validation in multi-step forms. The '
        'system verifies that Step 2 data only arrives after Step 1 is completed, preventing '
        'attackers from skipping validation steps by submitting directly to later stages.</p>'
    ),

    "si-10-5": (
        '<p>Restrict inputs to trusted sources and approved formats — know where your data '
        'is coming from and accept only data that matches expected patterns.</p>'
        '<p><strong>Example 1:</strong> Configure your API endpoints to accept input only '
        'from authenticated, authorized clients. Use API keys, OAuth tokens, and IP '
        'whitelisting to verify that requests come from known, trusted sources.</p>'
        '<p><strong>Example 2:</strong> Define strict JSON or XML schemas for your APIs '
        'and validate all incoming requests against the schema. Reject requests with '
        'unexpected fields, wrong data types, or values outside defined ranges. Document '
        'the accepted format in your API specification.</p>'
    ),

    "si-10-6": (
        '<p>Specifically prevent injection attacks — SQL injection, command injection, '
        'LDAP injection, XSS — through rigorous input sanitization.</p>'
        '<p><strong>Example 1:</strong> Use parameterized queries (prepared statements) '
        'for all database operations. Never concatenate user input into SQL strings. In '
        'C# use SqlParameter, in Java use PreparedStatement, in Python use parameterized '
        'queries with your database library.</p>'
        '<p><strong>Example 2:</strong> Deploy a WAF with injection prevention rules '
        '(OWASP ModSecurity Core Rule Set) in front of your web applications. The WAF '
        'inspects input for SQL injection, XSS, and command injection patterns and blocks '
        'them before they reach your application code.</p>'
    ),

    "si-11": (
        '<p>Handle errors in a way that reveals useful information to legitimate users '
        'but not to attackers. Error messages should help users fix problems without '
        'exposing system internals.</p>'
        '<p><strong>Example 1:</strong> Configure your web applications to display user-'
        'friendly error pages ("Something went wrong. Please contact support.") rather '
        'than stack traces, database connection strings, or file paths. Log the detailed '
        'error information server-side for your developers.</p>'
        '<p><strong>Example 2:</strong> In IIS, configure custom error pages and disable '
        'detailed error messages for remote clients. Set the customErrors mode to "On" or '
        '"RemoteOnly" in web.config. Remote users see a generic error page; only requests '
        'from localhost see detailed debugging information.</p>'
    ),

    "si-12": (
        '<p>Manage information throughout its lifecycle — from creation through use, '
        'storage, and eventual disposal — in accordance with legal requirements and '
        'organizational policies.</p>'
        '<p><strong>Example 1:</strong> Define retention policies in Microsoft 365 using '
        'Retention Labels and Retention Policies in Purview. Set emails to be retained '
        'for 7 years (legal requirement), project documents for 5 years after project '
        'closure, and temporary files for 30 days.</p>'
        '<p><strong>Example 2:</strong> Create a data disposal procedure that specifies '
        'how different types of data and media are destroyed. Hard drives containing CUI '
        'are degaussed or shredded. Paper documents with sensitive data go through a '
        'cross-cut shredder. Document the disposal with a certificate of destruction.</p>'
    ),

    "si-12-1": (
        '<p>Limit the personally identifiable information (PII) elements your systems '
        'collect and maintain to only what is actually needed for your mission.</p>'
        '<p><strong>Example 1:</strong> Audit the PII your applications collect. Do you '
        'really need a Social Security number for every form, or would a less sensitive '
        'identifier work? Remove PII fields that are not essential for the business '
        'process.</p>'
        '<p><strong>Example 2:</strong> In your databases, identify all columns containing '
        'PII. For columns that are not necessary for daily operations, consider removing '
        'them or replacing them with de-identified alternatives. For example, replace full '
        'dates of birth with just the year if the exact date is not needed.</p>'
    ),

    "si-12-2": (
        '<p>Use anonymized or synthetic data in testing, training, and research environments '
        'rather than real PII. Developers and testers do not need real customer data.</p>'
        '<p><strong>Example 1:</strong> Create a data masking pipeline that generates '
        'realistic but fake data for your test environments. Tools like Redgate Data Masker '
        'or custom scripts can replace real names, SSNs, and addresses with plausible '
        'fakes while preserving data relationships.</p>'
        '<p><strong>Example 2:</strong> In SQL Server, use Dynamic Data Masking or the '
        'data masking features in Azure SQL to automatically mask PII when test teams '
        'query the database. They see realistic data patterns but not actual PII values.</p>'
    ),

    "si-12-3": (
        '<p>Dispose of information properly when it is no longer needed — do not just '
        'delete files or throw away equipment. Sensitive data must be destroyed beyond '
        'recovery.</p>'
        '<p><strong>Example 1:</strong> Use NIST SP 800-88 guidelines for media '
        'sanitization. For hard drives: use the "Purge" method (cryptographic erase for '
        'SSDs, overwrite patterns for HDDs) or physically destroy them. Maintain a log '
        'with serial numbers, destruction dates, and witness signatures.</p>'
        '<p><strong>Example 2:</strong> Configure M365 retention policies to automatically '
        'delete emails and documents after the retention period expires. For SharePoint, '
        'set site-level retention policies that automatically purge content from the '
        'recycle bin after the defined period.</p>'
    ),

    "si-13": (
        '<p>Predictable failure prevention means planning for component failures before '
        'they happen — using redundancy, monitoring, and replacement schedules to prevent '
        'outages.</p>'
        '<p><strong>Example 1:</strong> Monitor hard drive health using S.M.A.R.T. data '
        'and proactively replace drives that show signs of impending failure (increasing '
        'bad sectors, rising temperature). Use your monitoring tool to alert when any '
        'drive health metric crosses a warning threshold.</p>'
        '<p><strong>Example 2:</strong> Maintain a replacement schedule for critical '
        'infrastructure components. UPS batteries have a 3-5 year lifespan — replace '
        'them before they fail. Server hardware should be refreshed every 5-7 years. '
        'Document these schedules and budget for replacements.</p>'
    ),

    "si-13-1": (
        '<p>When a component starts to fail, automatically transfer its responsibilities '
        'to a backup component before complete failure occurs.</p>'
        '<p><strong>Example 1:</strong> Configure high availability for your database '
        'servers (SQL Server Always On, PostgreSQL streaming replication). If the primary '
        'server shows signs of failure (missed heartbeats, high error rates), the cluster '
        'automatically promotes the secondary server.</p>'
        '<p><strong>Example 2:</strong> Set up load balancer health checks that '
        'automatically remove servers from the pool when they stop responding correctly. '
        'The remaining healthy servers absorb the traffic while the failed server is '
        'repaired or replaced.</p>'
    ),

    "si-13-2": (
        '<p>Set time limits on processes running without supervision and transfer '
        'processing to fresh components before the time limit expires.</p>'
        '<p><strong>Example 1:</strong> Configure IIS application pools to recycle every '
        '29 hours (default) to prevent memory leaks and resource exhaustion. The application '
        'pool refreshes automatically, and users experience no downtime during recycling.</p>'
        '<p><strong>Example 2:</strong> Schedule automatic restarts of long-running services '
        'during maintenance windows. A web service that has been running for 30 days may '
        'have accumulated memory leaks — a planned restart restores clean operation before '
        'performance degradation becomes visible to users.</p>'
    ),

    "si-13-3": (
        '<p>Provide the ability to manually transfer processing from one component to '
        'another when administrators need to perform maintenance or respond to issues.</p>'
        '<p><strong>Example 1:</strong> Configure your load balancer to support manual '
        'drain mode. When you need to patch a server, enable drain mode — the load '
        'balancer stops sending new connections to that server and waits for existing '
        'connections to finish before taking it offline.</p>'
        '<p><strong>Example 2:</strong> Use VMware vMotion or Hyper-V Live Migration to '
        'manually move virtual machines from one host to another before performing host '
        'maintenance. Users experience no downtime during the migration.</p>'
    ),

    "si-13-4": (
        '<p>Install standby components that can take over automatically when primary '
        'components fail, and notify administrators when a failover occurs.</p>'
        '<p><strong>Example 1:</strong> Deploy Windows Server Failover Clustering for '
        'critical services like SQL Server, file shares, and domain controllers. The '
        'standby node takes over within seconds of a primary failure, and the cluster '
        'sends email alerts to your operations team about the failover.</p>'
        '<p><strong>Example 2:</strong> Configure your firewall in an active/passive HA '
        'pair. The standby firewall continuously mirrors the primary&apos;s state table. If '
        'the primary fails, the standby takes over with no dropped connections. SNMP traps '
        'alert your team about the failover event.</p>'
    ),

    "si-13-5": (
        '<p>Ensure your failover capability actually works by testing it regularly. An '
        'untested failover is just a hope, not a plan.</p>'
        '<p><strong>Example 1:</strong> Schedule quarterly failover tests for your critical '
        'systems. Deliberately fail the primary database server and verify the secondary '
        'takes over cleanly. Measure the failover time and document any issues for '
        'improvement.</p>'
        '<p><strong>Example 2:</strong> Test your backup power (UPS, generators) under load. '
        'Simulate a power failure and verify that the UPS sustains operations long enough '
        'for the generator to start and stabilize. Test annually and document results.</p>'
    ),

    "si-14": (
        '<p>Non-persistence means systems regularly refresh to a known-good state. Instead '
        'of letting a system accumulate changes (and potentially compromises) over time, '
        'you periodically wipe it and rebuild from a trusted image.</p>'
        '<p><strong>Example 1:</strong> Use VDI (Virtual Desktop Infrastructure) with '
        'non-persistent desktops. Each time a user logs in, they get a fresh virtual desktop '
        'built from a golden image. When they log out, the desktop is destroyed. Any '
        'malware from the session is wiped automatically.</p>'
        '<p><strong>Example 2:</strong> In cloud environments, use immutable infrastructure '
        'patterns. Instead of patching servers in place, deploy new servers from an updated '
        'image and destroy the old ones. Tools like Terraform and Packer automate this '
        'process so servers are always built from a known-good template.</p>'
    ),

    "si-14-1": (
        '<p>When refreshing components, only use trusted sources — known-good images, '
        'verified software repositories, or authenticated baselines.</p>'
        '<p><strong>Example 1:</strong> Store your golden images in a hardened, access-'
        'controlled repository. Before refreshing a system, verify the image&apos;s hash '
        'against the stored known-good value to ensure it has not been tampered with.</p>'
        '<p><strong>Example 2:</strong> For container-based deployments, only pull images '
        'from your private, trusted container registry. Configure Kubernetes admission '
        'controllers to reject images from public registries. Sign all images and verify '
        'signatures before deployment.</p>'
    ),

    "si-14-2": (
        '<p>Ensure that non-persistent systems do not retain sensitive information after '
        'sessions end — no residual data left behind.</p>'
        '<p><strong>Example 1:</strong> Configure non-persistent VDI desktops to redirect '
        'all user data to network storage. When the desktop is destroyed, no user data '
        'remains on the VDI infrastructure. Verify this by checking for residual data '
        'after session termination.</p>'
        '<p><strong>Example 2:</strong> For web applications using session storage, '
        'configure sessions to be completely purged from the server when they expire or '
        'when the user logs out. Use in-memory session storage rather than persistent '
        'disk-based storage for sensitive session data.</p>'
    ),

    "si-14-3": (
        '<p>Establish non-persistent network connections — connections are temporary and '
        'terminated after use rather than maintained indefinitely.</p>'
        '<p><strong>Example 1:</strong> Configure VPN connections to automatically '
        'disconnect after a set idle timeout (30 minutes) or maximum session duration '
        '(8 hours). Users must re-authenticate to reconnect, ensuring stale sessions '
        'are not exploited.</p>'
        '<p><strong>Example 2:</strong> For cloud-based management sessions, use just-in-'
        'time access (Azure AD PIM). Admin access is granted for a specific time window '
        '(1-4 hours), after which the elevated permissions are automatically revoked. '
        'Sessions are non-persistent by design.</p>'
    ),

    "si-15": (
        '<p>Filter the output of your systems to prevent sensitive information from being '
        'inadvertently disclosed in system outputs — reports, screens, error messages, '
        'and data exports.</p>'
        '<p><strong>Example 1:</strong> Configure your applications to mask sensitive data '
        'in output displays. Show only the last four digits of SSNs, mask credit card '
        'numbers except the last four digits, and redact passwords in log files. Never '
        'display full sensitive data unless the user specifically requests it.</p>'
        '<p><strong>Example 2:</strong> Use Microsoft Purview DLP policies to scan outbound '
        'emails and file shares for sensitive data patterns. If a report containing '
        'unmasked SSNs is attached to an email, the DLP policy blocks the send and '
        'notifies the user to redact the data first.</p>'
    ),

    "si-16": (
        '<p>Memory protection prevents attackers from executing code in memory regions '
        'that should only contain data — blocking common exploit techniques like buffer '
        'overflows.</p>'
        '<p><strong>Example 1:</strong> Ensure Data Execution Prevention (DEP) is enabled '
        'on all Windows systems. DEP marks memory pages as non-executable so malicious '
        'code injected into data memory regions cannot run. Verify via GPO or SCCM '
        'compliance baselines.</p>'
        '<p><strong>Example 2:</strong> Enable Address Space Layout Randomization (ASLR) '
        'to randomize where programs load in memory. This makes it extremely difficult '
        'for attackers to predict memory addresses for exploit code. On Windows, ASLR is '
        'on by default — verify it is active using Windows Security Center or the '
        'Exploit Protection settings.</p>'
    ),

    "si-17": (
        '<p>Define fail-safe procedures — specific steps your team follows when a system '
        'fails or a security control stops working — to ensure security is maintained '
        'during and after the failure.</p>'
        '<p><strong>Example 1:</strong> Document fail-safe procedures for your firewall. '
        'If the firewall fails, the procedure includes: activate the standby firewall, '
        'verify rules are consistent, notify the security team, block direct internet '
        'access until the primary is restored, and log the entire incident.</p>'
        '<p><strong>Example 2:</strong> Create runbooks for common failure scenarios — '
        'SIEM down, AV console unreachable, domain controller failure. Each runbook '
        'specifies what compensating controls to activate, who to notify, and what '
        'monitoring to increase until the primary system is restored.</p>'
    ),

    "si-18": (
        '<p>Maintain the quality and accuracy of personally identifiable information '
        'throughout its lifecycle. Inaccurate PII can lead to wrong decisions and harm '
        'to individuals.</p>'
        '<p><strong>Example 1:</strong> Implement data quality checks in your HR and '
        'customer databases. Run periodic reports to identify duplicate records, '
        'inconsistent addresses, invalid phone numbers, and outdated email addresses. '
        'Assign data stewards to review and correct discrepancies.</p>'
        '<p><strong>Example 2:</strong> Provide a self-service portal where employees '
        'and customers can review and update their own PII (address, phone, email). '
        'Changes go through a verification process before being applied to ensure '
        'accuracy.</p>'
    ),

    "si-18-1": (
        '<p>Use automated tools to support PII quality operations — finding and fixing '
        'data quality issues at scale.</p>'
        '<p><strong>Example 1:</strong> Deploy data quality software (like Informatica '
        'Data Quality or Microsoft Data Quality Services) that automatically identifies '
        'duplicate records, standardizes address formats, and flags inconsistencies in '
        'PII fields across your databases.</p>'
        '<p><strong>Example 2:</strong> Use email verification services to automatically '
        'validate email addresses in your customer database. Invalid addresses are flagged '
        'for removal or update, reducing bounce rates and ensuring communications reach '
        'the right people.</p>'
    ),

    "si-18-2": (
        '<p>Use data tags to identify the quality, source, and timeliness of PII so users '
        'know how much to trust the data.</p>'
        '<p><strong>Example 1:</strong> Add metadata tags to PII records indicating when '
        'the data was last verified, what source it came from, and a confidence level. '
        'An address verified by the postal service last month has higher confidence than '
        'one self-reported three years ago.</p>'
        '<p><strong>Example 2:</strong> In your CRM, tag records with their data source '
        '(customer-provided, third-party enrichment, manually entered) and last-verified '
        'date. Reports and decision-making processes can then filter by data quality '
        'to ensure they use only reliable information.</p>'
    ),

    "si-18-3": (
        '<p>Implement quality controls at the point of PII collection to ensure data is '
        'accurate from the start.</p>'
        '<p><strong>Example 1:</strong> On data entry forms, validate PII in real time — '
        'check email format, validate phone number patterns, use address autocomplete '
        'with postal service verification. Catch errors at entry rather than cleaning '
        'them up later.</p>'
        '<p><strong>Example 2:</strong> For PII collected from external systems via API, '
        'implement schema validation that checks required fields, data types, and format '
        'constraints before accepting the data. Reject submissions that fail quality '
        'checks and return clear error messages.</p>'
    ),

    "si-18-4": (
        '<p>Allow individuals to request corrections to their PII and process those '
        'requests in a timely manner.</p>'
        '<p><strong>Example 1:</strong> Provide a clear process (web form, email address, '
        'phone number) for individuals to request corrections to their PII. Set a maximum '
        'response time (e.g., 30 days) and track requests through your ticketing system.</p>'
        '<p><strong>Example 2:</strong> In your customer portal, allow users to submit '
        'change requests for their personal data. Route requests through a verification '
        'and approval workflow to prevent unauthorized changes. Notify the individual '
        'when their correction has been processed.</p>'
    ),

    "si-18-5": (
        '<p>When PII is corrected or deleted, notify other organizations or systems that '
        'received the original data so they can update their records too.</p>'
        '<p><strong>Example 1:</strong> Maintain a log of all organizations you have shared '
        'PII with. When a correction is made, send update notifications to all recipients. '
        'For deletions, send deletion requests and track confirmations.</p>'
        '<p><strong>Example 2:</strong> For systems integrated via APIs, implement webhooks '
        'or event-driven updates that automatically push PII corrections to downstream '
        'systems. When the master record is corrected in your HR system, the change '
        'automatically propagates to payroll, benefits, and access control systems.</p>'
    ),

    "si-19": (
        '<p>De-identification removes or obscures personally identifiable information '
        'from data sets so individuals cannot be identified from the data.</p>'
        '<p><strong>Example 1:</strong> Before sharing datasets for analysis, remove '
        'direct identifiers (names, SSNs, email addresses) and generalize quasi-identifiers '
        '(replace exact ages with age ranges, replace zip codes with the first three digits). '
        'Test the de-identified data with re-identification risk tools.</p>'
        '<p><strong>Example 2:</strong> Use SQL Server Dynamic Data Masking or Azure '
        'Purview data masking to automatically de-identify PII in query results for '
        'non-privileged users. Analysts see masked data (e.g., "XXXX-XX-1234") while '
        'authorized users see the full values.</p>'
    ),

    "si-19-1": (
        '<p>De-identify information at the point of collection when full PII is not needed '
        'for the stated purpose.</p>'
        '<p><strong>Example 1:</strong> If collecting survey responses, do not collect names '
        'or other identifiers unless they are essential to the survey purpose. Assign random '
        'identifiers at collection and store any linking table (if needed for follow-up) '
        'separately with restricted access.</p>'
        '<p><strong>Example 2:</strong> For website analytics, configure your tools to '
        'anonymize IP addresses at collection time. Google Analytics offers an IP '
        'anonymization feature that truncates visitor IP addresses before storage.</p>'
    ),

    "si-19-2": (
        '<p>De-identify PII before archiving data for long-term storage. Archived data '
        'often has weaker access controls, so removing PII reduces risk.</p>'
        '<p><strong>Example 1:</strong> Before moving old project data to archive storage, '
        'run a de-identification script that replaces employee names with generic identifiers, '
        'removes email addresses, and generalizes dates. Archive the de-identified version.</p>'
        '<p><strong>Example 2:</strong> Configure your database archival process to '
        'automatically apply data masking rules when moving records to archive tables. '
        'Direct identifiers are stripped and quasi-identifiers are generalized before '
        'the records are written to the archive.</p>'
    ),

    "si-19-3": (
        '<p>De-identify data before releasing it to third parties or making it publicly '
        'available.</p>'
        '<p><strong>Example 1:</strong> Before sharing incident response data with an ISAC '
        '(Information Sharing and Analysis Center), remove all internal hostnames, IP '
        'addresses, employee names, and customer information. Share only the threat '
        'indicators and attack patterns.</p>'
        '<p><strong>Example 2:</strong> If publishing research data, use k-anonymity or '
        'l-diversity techniques to ensure no individual can be identified from the released '
        'dataset. Test with re-identification tools before publication to verify the '
        'de-identification is effective.</p>'
    ),

    "si-19-4": (
        '<p>Remove, mask, encrypt, hash, or replace direct identifiers (names, SSNs, '
        'account numbers) to prevent identification of individuals.</p>'
        '<p><strong>Example 1:</strong> Use one-way hashing (SHA-256) to replace direct '
        'identifiers with hash values. The hash allows you to link records belonging to '
        'the same individual without knowing who they are. Use a salt to prevent rainbow '
        'table attacks on the hashes.</p>'
        '<p><strong>Example 2:</strong> Use format-preserving encryption (FPE) to encrypt '
        'SSNs and account numbers while maintaining their format. The encrypted value looks '
        'like a real SSN (9 digits, proper format) but is meaningless without the '
        'decryption key. Authorized users can decrypt; others see only the encrypted value.</p>'
    ),

    "si-19-5": (
        '<p>Apply statistical disclosure control techniques to prevent identification of '
        'individuals from aggregate or statistical data.</p>'
        '<p><strong>Example 1:</strong> When publishing statistics, suppress cells with '
        'small counts (fewer than 5 individuals) to prevent identification. If only 2 '
        'people in your organization match a specific demographic combination, reporting '
        'their average salary effectively reveals individual data.</p>'
        '<p><strong>Example 2:</strong> Add random noise to published statistics so exact '
        'values cannot be used for re-identification. Instead of reporting that exactly '
        '47 employees completed a training, report "approximately 45-50" or add Laplacian '
        'noise to the exact count.</p>'
    ),

    "si-19-6": (
        '<p>Use differential privacy techniques to provide mathematical guarantees that '
        'individual records cannot be identified from published data analysis results.</p>'
        '<p><strong>Example 1:</strong> When running analytics on employee data, use a '
        'differential privacy library (like Google&apos;s DP library or OpenDP) that adds '
        'calibrated noise to query results. Analysts get useful aggregate statistics while '
        'individual privacy is mathematically guaranteed.</p>'
        '<p><strong>Example 2:</strong> Configure data sharing platforms to enforce a '
        'privacy budget — a limit on how many queries can be run against a dataset. Each '
        'query consumes some of the budget, and once exhausted, no more queries are '
        'allowed. This prevents attackers from combining many queries to isolate '
        'individuals.</p>'
    ),

    "si-19-7": (
        '<p>Use validated, peer-reviewed algorithms and software for de-identification — '
        'do not invent your own de-identification methods.</p>'
        '<p><strong>Example 1:</strong> Use established de-identification tools like ARX '
        '(open-source data anonymization tool) that implement well-tested algorithms for '
        'k-anonymity, l-diversity, and t-closeness. These tools have been peer-reviewed '
        'and validated for correctness.</p>'
        '<p><strong>Example 2:</strong> When using commercial de-identification products, '
        'verify that the vendor documents their algorithms and has had them independently '
        'validated. Request documentation of the specific de-identification techniques used '
        'and their known limitations.</p>'
    ),

    "si-19-8": (
        '<p>Test your de-identification by simulating a "motivated intruder" — someone '
        'with publicly available information who actively tries to re-identify individuals '
        'in your de-identified dataset.</p>'
        '<p><strong>Example 1:</strong> Hire a privacy consultant or internal red team to '
        'attempt re-identification using publicly available data (LinkedIn profiles, voter '
        'registration records, social media). If they can identify individuals, your '
        'de-identification is insufficient.</p>'
        '<p><strong>Example 2:</strong> Use automated re-identification risk assessment '
        'tools that compare your de-identified dataset against external data sources to '
        'estimate the probability of re-identification. If the risk exceeds your threshold '
        '(typically 5-10%), apply additional de-identification techniques.</p>'
    ),

    "si-20": (
        '<p>Tainting is a technique where data from untrusted sources is "marked" so the '
        'system tracks it and applies extra validation before using it in sensitive '
        'operations.</p>'
        '<p><strong>Example 1:</strong> In your web application framework, enable taint '
        'tracking (available in Ruby, Perl, and some Java frameworks) that automatically '
        'marks all user input as "tainted." Tainted data cannot be used in database '
        'queries or system commands without first being validated and sanitized.</p>'
        '<p><strong>Example 2:</strong> Tag data received from external APIs as untrusted '
        'in your data processing pipeline. Untrusted data passes through a validation '
        'and sanitization layer before it can be written to production databases or '
        'used in business logic.</p>'
    ),

    "si-21": (
        '<p>Periodically refresh information from authoritative sources to ensure your '
        'systems are working with current, accurate data rather than stale copies.</p>'
        '<p><strong>Example 1:</strong> Configure your Active Directory to refresh group '
        'memberships and access rights from your HR system daily. When HR records show an '
        'employee has transferred departments, the access changes propagate to AD '
        'automatically, ensuring access rights stay current.</p>'
        '<p><strong>Example 2:</strong> Refresh your threat intelligence feeds at least '
        'every 24 hours. Stale IOCs (indicators of compromise) can lead to missed '
        'detections or false positives. Configure your SIEM and firewall to automatically '
        'pull updated threat feeds on a regular schedule.</p>'
    ),

    "si-22": (
        '<p>Use diverse information sources to reduce the risk of relying on a single '
        'source that could be compromised, inaccurate, or manipulated.</p>'
        '<p><strong>Example 1:</strong> Subscribe to multiple threat intelligence feeds '
        'from different providers (CISA, commercial feeds, industry ISACs). Cross-reference '
        'indicators across sources — an IOC confirmed by multiple independent sources is '
        'much more reliable than one seen in only a single feed.</p>'
        '<p><strong>Example 2:</strong> For critical business decisions based on data, '
        'verify the data from at least two independent sources before acting. If a '
        'vulnerability scan shows a critical finding, confirm it with a manual check or '
        'a second scanning tool before declaring an emergency.</p>'
    ),

    "si-23": (
        '<p>Information fragmentation splits sensitive data across multiple systems or '
        'locations so that compromising any single system does not give the attacker the '
        'complete dataset.</p>'
        '<p><strong>Example 1:</strong> Store different elements of sensitive records in '
        'different databases. Customer names in one database, account numbers in another, '
        'and transaction details in a third. An attacker who compromises one database gets '
        'only a fragment of the complete record.</p>'
        '<p><strong>Example 2:</strong> Use Shamir&apos;s Secret Sharing to split encryption '
        'master keys across multiple key custodians. No single person has the complete key. '
        'Reconstruction requires a minimum number of custodians (e.g., 3 of 5) to '
        'contribute their key fragments simultaneously.</p>'
    ),

    # =========================================================================
    # SUPPLY CHAIN RISK MANAGEMENT (SR) — 27 controls
    # =========================================================================

    "sr-1": (
        '<p>Create and maintain a policy for managing supply chain risks — the risks that '
        'come from the vendors, products, and services your organization relies on. Your '
        'supply chain is only as strong as its weakest link.</p>'
        '<p><strong>Example 1:</strong> Write a Supply Chain Risk Management policy that '
        'covers vendor assessment requirements, approved supplier lists, software integrity '
        'verification, and incident notification requirements from suppliers. Store it with '
        'version control and review annually.</p>'
        '<p><strong>Example 2:</strong> Use the M365 Compliance Manager to track your SR '
        'family controls. Upload your policy, vendor assessment records, and procurement '
        'procedures as evidence. Set up review reminders for annual policy updates.</p>'
    ),

    "sr-2": (
        '<p>Develop a supply chain risk management (SCRM) plan that covers how you assess, '
        'monitor, and mitigate risks from your suppliers, vendors, and service providers.</p>'
        '<p><strong>Example 1:</strong> Create an SCRM plan that lists all critical vendors '
        '(cloud providers, software vendors, hardware suppliers), assesses the risk each '
        'poses to your operations, and defines mitigation strategies — like requiring SOC 2 '
        'reports, conducting vendor security assessments, and maintaining backup suppliers.</p>'
        '<p><strong>Example 2:</strong> Include your software supply chain in the plan. '
        'Document all third-party libraries and open-source components used in your '
        'applications. Use a Software Composition Analysis (SCA) tool like Snyk or Black '
        'Duck to continuously monitor for vulnerabilities in your software dependencies.</p>'
    ),

    "sr-2-1": (
        '<p>Establish a dedicated supply chain risk management team with members from '
        'across your organization — IT, security, procurement, legal, and operations.</p>'
        '<p><strong>Example 1:</strong> Form an SCRM team that includes your CISO or security '
        'lead, a procurement representative, a legal advisor, and a representative from '
        'each major business unit. Meet quarterly to review vendor risks, discuss emerging '
        'threats, and update the SCRM plan.</p>'
        '<p><strong>Example 2:</strong> Assign the SCRM team specific responsibilities: '
        'procurement evaluates vendor financial stability, IT security reviews vendor '
        'security practices, legal reviews contract terms for security and liability '
        'provisions, and operations assesses vendor service delivery reliability.</p>'
    ),

    "sr-3": (
        '<p>Implement controls and processes to manage supply chain risks — from selecting '
        'vendors to verifying the integrity of delivered products and services.</p>'
        '<p><strong>Example 1:</strong> Before purchasing software or hardware, require '
        'vendors to complete a security questionnaire covering their security practices, '
        'incident response capabilities, data handling procedures, and compliance '
        'certifications. Score the responses and only approve vendors that meet your '
        'minimum threshold.</p>'
        '<p><strong>Example 2:</strong> Verify the integrity of all software before '
        'deploying it. Download software only from official vendor sites, check SHA-256 '
        'hashes against published values, and verify digital signatures. Never install '
        'software downloaded from third-party sites or torrents.</p>'
    ),

    "sr-3-1": (
        '<p>Maintain a diverse supply base so you are not dependent on a single supplier '
        'for critical products or services. If one supplier is compromised, you need '
        'alternatives.</p>'
        '<p><strong>Example 1:</strong> Identify your single-source dependencies — products '
        'or services where only one vendor can supply them. For each, identify at least one '
        'alternative supplier that has been vetted and can be activated if the primary '
        'supplier fails or is compromised.</p>'
        '<p><strong>Example 2:</strong> For cloud services, architect your applications to '
        'be portable between providers. Avoid deep lock-in to a single cloud vendor&apos;s '
        'proprietary services. Use containers and infrastructure-as-code so you can '
        'redeploy to a different provider if needed.</p>'
    ),

    "sr-3-2": (
        '<p>Limit the potential harm from a supply chain compromise by reducing your '
        'exposure to any single supplier or component.</p>'
        '<p><strong>Example 1:</strong> Segment your network so that vendor-supplied '
        'systems and services run in isolated zones. If a vendor&apos;s software is '
        'compromised (like the SolarWinds incident), the blast radius is limited to '
        'the segment where the vendor&apos;s tools operate.</p>'
        '<p><strong>Example 2:</strong> Limit the permissions granted to vendor software '
        'and service accounts to the minimum needed. A vendor&apos;s monitoring tool does not '
        'need domain admin access. Apply least privilege to reduce the impact if the '
        'vendor&apos;s product is compromised.</p>'
    ),

    "sr-3-3": (
        '<p>Ensure your supply chain security requirements flow down to sub-tier suppliers '
        '— your vendor&apos;s vendors need to meet security standards too.</p>'
        '<p><strong>Example 1:</strong> Include clauses in your vendor contracts that require '
        'them to impose equivalent security requirements on their own subcontractors. If '
        'your cloud provider uses a third-party data center, that data center must meet '
        'the same security standards you require of the cloud provider.</p>'
        '<p><strong>Example 2:</strong> Request your vendors&apos; subcontractor lists and '
        'verify that critical sub-tier suppliers have adequate security certifications '
        '(SOC 2, ISO 27001, FedRAMP). A weak link in the sub-tier supply chain can '
        'compromise your security regardless of how secure your direct vendor is.</p>'
    ),

    "sr-4": (
        '<p>Track the provenance (origin, history, and chain of custody) of system '
        'components — know where your hardware and software came from and who handled '
        'it along the way.</p>'
        '<p><strong>Example 1:</strong> Maintain a detailed inventory of all hardware '
        'components including manufacturer, model, serial number, date of purchase, '
        'reseller, and shipping carrier. If a hardware tampering concern arises, you '
        'can trace the complete chain of custody.</p>'
        '<p><strong>Example 2:</strong> For software, maintain a Software Bill of Materials '
        '(SBOM) for all applications. The SBOM lists every component, library, and module '
        'in the software, its version, and its source. Use tools like OWASP Dependency-'
        'Check or Syft to generate SBOMs automatically.</p>'
    ),

    "sr-4-1": (
        '<p>Verify the identity of suppliers and their authorized representatives to '
        'prevent impersonation or fraud in your supply chain.</p>'
        '<p><strong>Example 1:</strong> Before placing orders with new suppliers, verify '
        'their business registration, DUNS number, and physical address independently — '
        'not just from information they provide. Check the SAM.gov registration for '
        'government suppliers.</p>'
        '<p><strong>Example 2:</strong> For software suppliers, verify their domain '
        'ownership and code signing certificates. When a vendor representative contacts '
        'you about a software update or license change, verify their identity through '
        'a known, previously established communication channel — not the one they used '
        'to contact you.</p>'
    ),

    "sr-4-2": (
        '<p>Track and trace system components throughout the supply chain — from '
        'manufacture to delivery to deployment — to detect tampering or diversion.</p>'
        '<p><strong>Example 1:</strong> Use serialized tracking for critical hardware '
        'components. Record serial numbers at procurement, verify them at receiving, and '
        'check them again during deployment. Any serial number mismatch between records '
        'indicates potential component swapping.</p>'
        '<p><strong>Example 2:</strong> For software, use verified download channels with '
        'integrity verification. Record the hash of every software package at download '
        'time, store it in your configuration management database, and verify it again '
        'before installation. Any change in the hash means the software was modified.</p>'
    ),

    "sr-4-3": (
        '<p>Validate that system components are genuine (not counterfeit) and have not '
        'been altered from their original state.</p>'
        '<p><strong>Example 1:</strong> Purchase hardware only from authorized resellers '
        'or directly from manufacturers. For critical components like servers and network '
        'equipment, use vendor registration and authentication programs (like Cisco&apos;s '
        'Brand Protection) to verify authenticity.</p>'
        '<p><strong>Example 2:</strong> For software, verify digital signatures and compare '
        'hashes against the vendor&apos;s published values before installation. Use code signing '
        'verification tools to confirm the software was signed by the legitimate vendor '
        'and has not been modified since signing.</p>'
    ),

    "sr-4-4": (
        '<p>Maintain a complete pedigree — the documented history of a component from its '
        'origin through all handling, modification, and testing — for critical supply '
        'chain elements.</p>'
        '<p><strong>Example 1:</strong> For hardware used in classified or high-security '
        'environments, require vendors to provide a complete chain-of-custody document '
        'covering manufacture, assembly, testing, packaging, and shipping. Any gaps in '
        'the pedigree documentation should be investigated.</p>'
        '<p><strong>Example 2:</strong> For custom-developed software, maintain a complete '
        'development history in your version control system (Git). Every code change, code '
        'review, test result, and build artifact is traceable from requirements through '
        'deployment, creating a verifiable software pedigree.</p>'
    ),

    "sr-5": (
        '<p>Use acquisition strategies, tools, and methods that reduce supply chain risk '
        '— build security into your procurement process from the beginning.</p>'
        '<p><strong>Example 1:</strong> Include security requirements in all RFPs and '
        'procurement documents. Require vendors to demonstrate FIPS 140-2 validated '
        'encryption, SOC 2 Type II reports, and vulnerability management programs. Make '
        'these requirements mandatory, not optional.</p>'
        '<p><strong>Example 2:</strong> Use the GSA IT Schedule or other vetted procurement '
        'vehicles for IT purchases. These channels provide some assurance that vendors '
        'have been reviewed. For software, prefer products on the DoD&apos;s approved products '
        'list or FedRAMP-authorized cloud services.</p>'
    ),

    "sr-5-1": (
        '<p>Ensure adequate supply of critical components — maintain buffer stock or '
        'identify alternative sources for components essential to your operations.</p>'
        '<p><strong>Example 1:</strong> Maintain a small inventory of spare critical '
        'components — hard drives, network switches, power supplies — so a supply chain '
        'disruption does not halt your operations. Define minimum stock levels for each '
        'critical component.</p>'
        '<p><strong>Example 2:</strong> Establish contracts with multiple suppliers for '
        'critical components. If your primary supplier cannot deliver (due to shortage, '
        'trade restrictions, or compromise), you can activate the secondary supplier '
        'without a lengthy procurement process.</p>'
    ),

    "sr-5-2": (
        '<p>Conduct security assessments of supply chain elements before selecting, '
        'accepting, modifying, or updating them.</p>'
        '<p><strong>Example 1:</strong> Before deploying a new software application, '
        'conduct a security review. Run a vulnerability scan, check the SBOM for known '
        'vulnerable components, review the vendor&apos;s security practices, and perform a '
        'risk assessment. Only deploy after the assessment passes your criteria.</p>'
        '<p><strong>Example 2:</strong> Before applying major software updates, review '
        'the release notes for security-relevant changes. Check if any new components or '
        'dependencies have been added. Run the update through your test environment and '
        'verify it does not introduce new vulnerabilities or weaken existing controls.</p>'
    ),

    "sr-6": (
        '<p>Regularly assess and review your suppliers&apos; security posture — a vendor that '
        'was secure last year may not be secure today.</p>'
        '<p><strong>Example 1:</strong> Require critical vendors to provide annual SOC 2 '
        'Type II audit reports. Review the reports for any deficiencies, especially in '
        'areas relevant to your data (access control, encryption, incident response). '
        'Follow up on any noted exceptions or qualifications.</p>'
        '<p><strong>Example 2:</strong> Conduct annual security questionnaire reviews '
        'for all vendors handling your sensitive data. Ask about their security practices, '
        'recent incidents, insurance coverage, and business continuity plans. Track their '
        'responses year over year to identify trends or deterioration.</p>'
    ),

    "sr-6-1": (
        '<p>Test and analyze supplier-provided components to verify they function as '
        'expected and do not contain hidden functionality.</p>'
        '<p><strong>Example 1:</strong> Before deploying new hardware (especially from '
        'overseas manufacturers), conduct functional testing to verify the equipment '
        'operates according to specifications. Check firmware versions against known-good '
        'baselines and scan for unauthorized network communications.</p>'
        '<p><strong>Example 2:</strong> For software, run static and dynamic analysis tools '
        '(SonarQube, Checkmarx) on vendor-provided code or components before integrating '
        'them into your applications. Check for backdoors, hardcoded credentials, and '
        'suspicious network connections.</p>'
    ),

    "sr-7": (
        '<p>Apply operations security (OPSEC) to your supply chain activities — protect '
        'information about your procurement, security tools, and technology choices from '
        'adversaries.</p>'
        '<p><strong>Example 1:</strong> Do not publicly disclose which specific security '
        'products you use, who your vendors are, or your procurement timeline in job '
        'postings, social media, or conference presentations. An adversary who knows your '
        'exact security stack can target its weaknesses.</p>'
        '<p><strong>Example 2:</strong> Use non-disclosure agreements (NDAs) with all '
        'vendors and require them to protect information about your security architecture '
        'and procurement. A vendor who publicly lists you as a customer reveals information '
        'about your technology stack to potential attackers.</p>'
    ),

    "sr-8": (
        '<p>Establish notification agreements with your suppliers that require them to '
        'alert you promptly about security incidents, vulnerabilities, or supply chain '
        'disruptions that could affect your organization.</p>'
        '<p><strong>Example 1:</strong> Include a clause in all vendor contracts requiring '
        'notification within 24-72 hours of any security incident that could affect your '
        'data or services. Define what constitutes a reportable incident and specify the '
        'notification method (email, phone, both).</p>'
        '<p><strong>Example 2:</strong> Require software vendors to notify you of '
        'vulnerabilities in their products before or simultaneously with public disclosure. '
        'This gives you time to prepare patches and mitigations before attackers start '
        'exploiting the vulnerability.</p>'
    ),

    "sr-9": (
        '<p>Use tamper resistance and tamper detection mechanisms for critical system '
        'components to prevent and detect unauthorized physical modification.</p>'
        '<p><strong>Example 1:</strong> Purchase servers and network equipment with tamper-'
        'evident chassis intrusion detection. When the server case is opened, a sensor '
        'records the event in the firmware log. Review these logs during receiving and '
        'during periodic physical security inspections.</p>'
        '<p><strong>Example 2:</strong> Use tamper-evident seals on critical equipment '
        'during shipping and storage. Photograph the seals at departure and verify them '
        'at arrival. Broken or replaced seals indicate potential tampering and require '
        'investigation before the equipment is deployed.</p>'
    ),

    "sr-9-1": (
        '<p>Apply tamper protection at multiple stages of the system development lifecycle '
        '— not just at delivery, but during development, testing, and deployment.</p>'
        '<p><strong>Example 1:</strong> Use code signing throughout your development '
        'pipeline. Sign code at build time, verify signatures at testing, and re-verify '
        'at deployment. If signatures do not match at any stage, the code may have been '
        'tampered with between stages.</p>'
        '<p><strong>Example 2:</strong> For hardware development, apply tamper-evident '
        'controls during manufacturing, shipping, receiving, and installation. At each '
        'handoff point, verify the integrity of previous tamper controls and apply new '
        'ones. Document each verification in the component&apos;s pedigree record.</p>'
    ),

    "sr-10": (
        '<p>Inspect systems or components — physically or logically — to detect tampering, '
        'counterfeit components, or unauthorized modifications.</p>'
        '<p><strong>Example 1:</strong> When receiving new IT equipment, perform receiving '
        'inspections. Verify serial numbers match purchase orders, check for tamper-evident '
        'seal integrity, compare the firmware version against the vendor&apos;s published '
        'current version, and look for physical signs of modification.</p>'
        '<p><strong>Example 2:</strong> For software, conduct integrity verification before '
        'deployment. Compare file hashes against vendor-published values, verify code '
        'signatures, and scan for known malware. Do not deploy any software that fails '
        'integrity verification.</p>'
    ),

    "sr-11": (
        '<p>Implement anti-counterfeit measures to detect and prevent the use of fake or '
        'unauthorized components in your systems. Counterfeit components may fail '
        'unexpectedly or contain hidden backdoors.</p>'
        '<p><strong>Example 1:</strong> Purchase IT equipment only from authorized '
        'distributors and resellers. Verify the authenticity of components using '
        'manufacturer verification tools (like Cisco&apos;s hardware serial number checker '
        'or HPE Part Surfer). Flag components with unverifiable serial numbers.</p>'
        '<p><strong>Example 2:</strong> For critical electronic components, use X-ray '
        'inspection or other physical testing to verify component markings match actual '
        'capabilities. Report suspected counterfeits to GIDEP (Government-Industry Data '
        'Exchange Program) or the manufacturer.</p>'
    ),

    "sr-11-1": (
        '<p>Train your staff to recognize counterfeit components — procurement, receiving, '
        'and IT personnel should know what to look for.</p>'
        '<p><strong>Example 1:</strong> Provide annual training to procurement and receiving '
        'staff on counterfeit detection. Cover topics like checking packaging quality, '
        'verifying serial number formats, identifying suspiciously low prices, and using '
        'vendor authenticity verification tools.</p>'
        '<p><strong>Example 2:</strong> Include counterfeit awareness in your IT security '
        'awareness training. Teach IT staff to verify firmware versions, check digital '
        'signatures, and report any equipment that behaves unexpectedly or does not match '
        'specifications — these could be signs of counterfeit components.</p>'
    ),

    "sr-11-2": (
        '<p>Maintain configuration control when components are sent for service or repair '
        'to prevent unauthorized modifications or component substitution.</p>'
        '<p><strong>Example 1:</strong> Before sending equipment for repair, record the '
        'serial numbers, firmware versions, and component configuration. When the equipment '
        'returns, verify all serial numbers match and the firmware version has not changed '
        'unexpectedly. Any discrepancy requires investigation.</p>'
        '<p><strong>Example 2:</strong> Use only authorized service providers for critical '
        'equipment repairs. Include clauses in service contracts that prohibit component '
        'substitution without written approval. Require service reports documenting any '
        'parts replaced, with old part serial numbers and new part serial numbers.</p>'
    ),

    "sr-11-3": (
        '<p>Use automated scanning to detect counterfeit components based on component '
        'identifiers, firmware fingerprints, or known counterfeit databases.</p>'
        '<p><strong>Example 1:</strong> Use network device management tools to automatically '
        'inventory hardware serial numbers and firmware versions across your fleet. Compare '
        'against the manufacturer&apos;s database to verify authenticity. Flag any devices with '
        'serial numbers that do not match manufacturer records.</p>'
        '<p><strong>Example 2:</strong> For electronic components, use automated testing '
        'equipment that verifies component characteristics (timing, voltage, temperature '
        'response) against manufacturer specifications. Components that deviate from specs '
        'may be counterfeits that will fail prematurely or perform unexpectedly.</p>'
    ),

    "sr-12": (
        '<p>Dispose of system components properly to prevent sensitive data from leaving '
        'your control and to prevent counterfeit components from being re-introduced '
        'into the supply chain.</p>'
        '<p><strong>Example 1:</strong> Follow NIST SP 800-88 media sanitization guidelines '
        'before disposing of any equipment. For hard drives, use cryptographic erase (for '
        'SSDs) or degaussing (for HDDs). For equipment that cannot be sanitized, physically '
        'destroy it. Document all disposal with a certificate of destruction.</p>'
        '<p><strong>Example 2:</strong> Use a certified electronics recycler (e-Stewards or '
        'R2 certified) for equipment disposal. Require the recycler to provide a certificate '
        'of destruction with serial numbers of all destroyed items. Do not donate or sell '
        'equipment that contained sensitive data without proper sanitization — and never '
        'sell equipment that has been marked for destruction.</p>'
    ),
}
