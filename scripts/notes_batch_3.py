NOTES = {
    # =========================================================================
    # MAINTENANCE (MA) — 6 practices
    # =========================================================================

    "ma-l2-3-7-1": (
        "<p>This one sounds simple, but it trips people up because it is really about <em>documenting</em> "
        "your maintenance, not just doing it. An assessor wants to see that you have a schedule, you follow it, "
        "and you keep records of what was done, when, and by whom.</p>"
        "<p><strong>Example 1:</strong> Use a ticketing system like Jira, ConnectWise, or even a shared "
        "spreadsheet to log every maintenance action \u2014 Windows updates applied via WSUS or Intune, "
        "firmware updates on firewalls, drive replacements, etc. Each entry should capture the date, the "
        "technician, and what was done.</p>"
        "<p><strong>Example 2:</strong> Set up a recurring maintenance calendar in your IT department. "
        "For example, configure Microsoft Endpoint Configuration Manager (MECM/SCCM) to deploy patches "
        "on a defined monthly cycle, and retain the deployment reports as your maintenance records.</p>"
    ),

    "ma-l2-3-7-2": (
        "<p>This practice asks you to keep a handle on <em>who</em> does maintenance and <em>what tools</em> "
        "they use. You cannot just let a vendor walk in with their own laptop and plug into your network "
        "without any oversight.</p>"
        "<p><strong>Example 1:</strong> Maintain an approved tools list \u2014 document that your team uses "
        "specific versions of tools like PuTTY, WinSCP, or manufacturer diagnostic software. Store "
        "approved copies on a controlled network share and prohibit technicians from using personal "
        "thumb drives or unapproved utilities.</p>"
        "<p><strong>Example 2:</strong> Require vendor technicians to use a company-provided jump box or "
        "a supervised remote session (e.g., BeyondTrust Privileged Remote Access) rather than their own "
        "equipment. Log every session and review the recordings periodically.</p>"
    ),

    "ma-l2-3-7-3": (
        "<p>Before any piece of equipment leaves your building for repair \u2014 a laptop sent to the "
        "manufacturer, a hard drive going to a disposal service \u2014 you need to make sure there is no "
        "CUI left on it. If you cannot sanitize it, the equipment should not leave.</p>"
        "<p><strong>Example 1:</strong> Before shipping a laptop for warranty repair, use a NIST 800-88 "
        "compliant tool like DBAN (Darik's Boot and Nuke) or Blancco Drive Eraser to wipe the drive. "
        "Document the sanitization with a certificate or log entry that includes the serial number and "
        "date wiped.</p>"
        "<p><strong>Example 2:</strong> For equipment with drives that cannot be removed or wiped "
        "(like a multifunction printer with an internal drive), enable the built-in disk encryption "
        "or secure erase feature in the device\u2019s admin console before sending it out. Many enterprise "
        "printers from HP and Xerox have a \"Secure Storage Erase\" option in their management interface.</p>"
    ),

    "ma-l2-3-7-4": (
        "<p>This practice goes a step further than 3.7.2 \u2014 you need to actively approve, control, and "
        "monitor maintenance tools, and scan any media used for diagnostics before plugging it in.</p>"
        "<p><strong>Example 1:</strong> Before using a vendor-supplied diagnostic USB drive, scan it with "
        "your endpoint protection tool (e.g., Microsoft Defender for Endpoint, CrowdStrike Falcon, or "
        "Trellix ENS) on a standalone, non-production workstation. Document the scan results before "
        "allowing the media onto any production system.</p>"
        "<p><strong>Example 2:</strong> Create a Group Policy Object (GPO) under <em>Computer Configuration "
        "> Administrative Templates > System > Removable Storage Access</em> to deny all removable "
        "storage by default. Only grant exceptions to specific maintenance workstations where approved "
        "diagnostic tools are used under supervision.</p>"
    ),

    "ma-l2-3-7-5": (
        "<p>Nonlocal maintenance means remote maintenance \u2014 someone fixing your systems from outside "
        "your facility over a network connection. This is common with managed service providers and "
        "vendor support, and it needs strong controls.</p>"
        "<p><strong>Example 1:</strong> Require all remote maintenance sessions to authenticate through "
        "your VPN with MFA enabled (e.g., Cisco AnyConnect or Palo Alto GlobalProtect with Duo or "
        "Microsoft Authenticator as the second factor). When the maintenance session is over, terminate "
        "the VPN connection and verify the session ended in your VPN logs.</p>"
        "<p><strong>Example 2:</strong> Use a Privileged Access Management (PAM) tool like CyberArk or "
        "BeyondTrust that provides session recording, just-in-time access, and automatic credential "
        "rotation after each remote maintenance session. The session recording gives you an audit trail "
        "and the credential rotation prevents reuse.</p>"
    ),

    "ma-l2-3-7-6": (
        "<p>You need to know exactly who is authorized to perform maintenance on your systems, and anyone "
        "who is not on that list needs to be escorted and supervised by someone who is.</p>"
        "<p><strong>Example 1:</strong> Maintain an authorized maintenance personnel list in your "
        "security documentation \u2014 this can be a simple roster with names, organizations, clearance "
        "levels (if applicable), and the specific systems they are authorized to maintain. Review and "
        "update it quarterly or whenever personnel change.</p>"
        "<p><strong>Example 2:</strong> For third-party maintenance technicians who do not have the "
        "required access authorization, assign a cleared and technically competent employee to escort "
        "them at all times. Log the escort activity in your visitor/maintenance log, including arrival "
        "time, departure time, escort name, and a summary of work performed.</p>"
    ),

    # =========================================================================
    # MEDIA PROTECTION (MP) — 9 practices
    # =========================================================================

    "mp-l2-3-8-1": (
        "<p>This is about where you keep media that contains CUI \u2014 USB drives, backup tapes, external "
        "hard drives, printed documents. If it has CUI on it, it needs to be stored securely with "
        "controlled access.</p>"
        "<p><strong>Example 1:</strong> Store removable media containing CUI (USB drives, external SSDs, "
        "backup tapes) in a locked safe or locking cabinet within a controlled-access room. Maintain a "
        "check-out/check-in log so you know who has what media at all times \u2014 a simple sign-out sheet "
        "next to the cabinet works.</p>"
        "<p><strong>Example 2:</strong> For digital media stored on network shares, restrict access using "
        "NTFS permissions and Active Directory security groups. Only members of a specific \"CUI Media "
        "Handlers\" group should have read/write access to the share where CUI backups or archives are "
        "stored.</p>"
    ),

    "mp-l2-3-8-2": (
        "<p>This practice focuses on limiting <em>who</em> can access media containing CUI. Think of it as "
        "the access control layer on top of the secure storage from 3.8.1.</p>"
        "<p><strong>Example 1:</strong> Use a Group Policy Object to restrict removable storage device "
        "access. Under <em>Computer Configuration > Administrative Templates > System > Removable "
        "Storage Access</em>, set \"All Removable Storage classes: Deny all access\" for standard users, "
        "and only allow access for accounts in a specific security group that handle CUI media.</p>"
        "<p><strong>Example 2:</strong> For physical (non-digital) media like printed CUI documents, "
        "keep them in a locked file cabinet inside a room with badge-reader access control. Limit "
        "badge access to personnel whose roles require handling CUI documents, and review the access "
        "list at least quarterly.</p>"
    ),

    "mp-l1-3-8-3": (
        "<p>When you are done with media \u2014 or reusing it for a different purpose \u2014 you need to sanitize "
        "it so the CUI cannot be recovered. This applies to everything from hard drives to printed paper "
        "to the internal drives in your copiers.</p>"
        "<p><strong>Example 1:</strong> For hard drives and SSDs being decommissioned, use a NIST 800-88 "
        "compliant method. For magnetic drives, use a tool like Blancco or DBAN to perform a full "
        "overwrite. For SSDs, use the manufacturer\u2019s secure erase command (e.g., Samsung Magician\u2019s "
        "\"Secure Erase\" or Intel SSD Toolbox). Document each sanitization with the media serial number, "
        "method used, date, and technician name.</p>"
        "<p><strong>Example 2:</strong> For paper documents containing CUI, use a cross-cut shredder "
        "that meets DIN 66399 Level P-4 or higher. If you use a shredding service, get a Certificate "
        "of Destruction for each pickup and keep it on file. Do not just toss CUI paper into a standard "
        "recycling bin.</p>"
    ),

    "mp-l2-3-8-4": (
        "<p>CUI media needs to be clearly marked so anyone handling it knows what they are dealing with. "
        "This applies to both digital media (labels on USB drives, backup tapes) and non-digital media "
        "(cover sheets, headers and footers on printed documents).</p>"
        "<p><strong>Example 1:</strong> Apply physical labels to all removable media containing CUI. "
        "Use pre-printed labels or a label maker to print \"CUI\" along with the CUI category and any "
        "dissemination markings (e.g., \"CUI//SP-CTI\" for Controlled Technical Information). Stick the "
        "label directly on the USB drive, tape cartridge, or external drive.</p>"
        "<p><strong>Example 2:</strong> For printed CUI documents, include CUI markings in the header "
        "and footer of every page using your document template. In Microsoft Word, go to <em>Insert > "
        "Header & Footer</em> and add \"CUI\" or the appropriate category marking. You can also create a "
        "company Word template (.dotx) with CUI markings pre-configured so employees do not forget.</p>"
    ),

    "mp-l2-3-8-5": (
        "<p>When CUI media leaves your controlled area \u2014 whether you are mailing a backup drive or "
        "carrying a laptop to a client site \u2014 you need to protect it, track it, and document the "
        "transport.</p>"
        "<p><strong>Example 1:</strong> Ship removable media containing CUI via a trackable service "
        "like FedEx or UPS with signature-required delivery. Use tamper-evident bags or containers, "
        "and log the shipment details (tracking number, sender, recipient, date, contents) in a media "
        "transport log.</p>"
        "<p><strong>Example 2:</strong> When employees travel with laptops containing CUI, require "
        "BitLocker full-disk encryption (verify via <em>Control Panel > BitLocker Drive Encryption</em> "
        "or <code>manage-bde -status</code> in an admin command prompt). Also require employees to "
        "keep the laptop in their physical possession at all times \u2014 no leaving it in a car trunk "
        "or hotel room unattended.</p>"
    ),

    "mp-l2-3-8-6": (
        "<p>This is the encryption-specific requirement for CUI on digital media during transport. If you "
        "are moving a USB drive, external hard drive, or laptop with CUI outside your controlled area, "
        "the data needs to be encrypted.</p>"
        "<p><strong>Example 1:</strong> Enable BitLocker To Go on all USB drives used to transport CUI. "
        "You can enforce this via Group Policy at <em>Computer Configuration > Administrative Templates "
        "> Windows Components > BitLocker Drive Encryption > Removable Data Drives</em> \u2014 set \"Deny "
        "write access to removable drives not protected by BitLocker.\" This forces encryption before "
        "any data can be written to the drive.</p>"
        "<p><strong>Example 2:</strong> For file-level encryption during transport, use 7-Zip with "
        "AES-256 encryption to create encrypted archives of CUI files before copying them to removable "
        "media. Transmit the decryption password through a separate channel (e.g., phone call or "
        "separate email). This provides a FIPS-validated encryption layer on top of the transport.</p>"
    ),

    "mp-l2-3-8-7": (
        "<p>This practice is about restricting or outright prohibiting certain types of media on your "
        "systems. You get to decide what is allowed and what is not, but you need to document and "
        "enforce it.</p>"
        "<p><strong>Example 1:</strong> Use a GPO to block all removable media by default across your "
        "domain. Under <em>Computer Configuration > Administrative Templates > System > Removable "
        "Storage Access</em>, enable \"All Removable Storage classes: Deny all access.\" Then create "
        "exception GPOs linked to specific OUs for workstations that have a legitimate business need "
        "for removable media.</p>"
        "<p><strong>Example 2:</strong> Deploy an endpoint management tool like Microsoft Intune and "
        "create a device control policy that blocks unauthorized USB devices by hardware ID. You can "
        "whitelist specific approved USB drives (by vendor ID and product ID) and block everything "
        "else. This lets you allow company-issued encrypted drives while blocking personal thumb drives.</p>"
    ),

    "mp-l2-3-8-8": (
        "<p>If someone finds a random USB drive in the parking lot or a conference room, it should never "
        "end up plugged into one of your systems. This practice says that any portable storage device "
        "without a known, identifiable owner is prohibited from use.</p>"
        "<p><strong>Example 1:</strong> Establish a company policy that all USB drives must be issued "
        "and tracked by IT. Maintain an asset inventory of approved USB drives with serial numbers "
        "linked to specific employees. Any USB drive not in the inventory is confiscated and turned "
        "over to IT for analysis \u2014 never plugged into a production system.</p>"
        "<p><strong>Example 2:</strong> Include this requirement in your annual security awareness "
        "training. Use a real-world example like the 2008 Agent.btz attack (a USB-based worm that "
        "compromised DoD networks) to drive home why unknown USB devices are a serious threat. Track "
        "training completion in your LMS as evidence of policy communication.</p>"
    ),

    "mp-l2-3-8-9": (
        "<p>Your backups contain CUI, which means they need the same confidentiality protection as the "
        "original data. This practice requires encryption of backup data at the storage location.</p>"
        "<p><strong>Example 1:</strong> If you use Windows Server Backup or Veeam, enable encryption "
        "on backup jobs. In Veeam, go to <em>Backup Job Settings > Storage > Advanced > Enable backup "
        "file encryption</em> and select AES-256. Store the encryption password in a secure password "
        "manager like KeePass or your PAM tool \u2014 not in a sticky note on the server.</p>"
        "<p><strong>Example 2:</strong> For cloud backups (e.g., Azure Backup or AWS Backup), ensure "
        "encryption at rest is enabled. In Azure, backups are encrypted at rest with Microsoft-managed "
        "keys by default, but for CUI you should use customer-managed keys stored in Azure Key Vault. "
        "This gives you full control over the encryption keys and meets the FIPS 140 validation "
        "requirements.</p>"
    ),

    # =========================================================================
    # PERSONNEL SECURITY (PS) — 2 practices
    # =========================================================================

    "ps-l2-3-9-1": (
        "<p>Before anyone gets access to systems that handle CUI, you need to screen them. This is not "
        "just about government clearances \u2014 it applies to any personnel, including contractors and "
        "employees at a small business.</p>"
        "<p><strong>Example 1:</strong> Require a background check through a third-party service like "
        "Sterling, GoodHire, or HireRight before granting system access to new employees or contractors. "
        "At minimum, run a criminal history check and verify employment history. Document the screening "
        "results in the employee\u2019s HR file and do not provision their account until the check clears.</p>"
        "<p><strong>Example 2:</strong> Define a rescreening schedule in your personnel security policy "
        "\u2014 for example, rescreen all employees with CUI access every five years, or trigger a "
        "rescreening when someone transfers to a more sensitive role. Use your HRIS system (e.g., "
        "BambooHR, ADP, or Workday) to set reminder notifications when rescreening is due.</p>"
    ),

    "ps-l2-3-9-2": (
        "<p>When someone leaves the company or moves to a different role, you need to cut or adjust their "
        "access quickly. A former employee with active credentials is one of the most common and dangerous "
        "security gaps.</p>"
        "<p><strong>Example 1:</strong> Create a termination checklist that IT and HR execute together. "
        "Within the defined timeframe (e.g., same business day), disable the Active Directory account, "
        "revoke MFA tokens in Azure AD / Entra ID, remove the user from VPN access groups, and disable "
        "their email. In the Microsoft 365 Admin Center, go to <em>Users > Active Users</em>, select "
        "the departed employee, and click \"Block sign-in\" followed by revoking all sessions.</p>"
        "<p><strong>Example 2:</strong> For transfers within the company, review and adjust access "
        "rights using the principle of least privilege. In Active Directory, remove the user from "
        "security groups associated with their old role and add them to groups for their new role. "
        "Do not just add new permissions on top of old ones \u2014 that leads to privilege creep. "
        "Document the access review in a ticket and have the new supervisor approve the updated "
        "access rights.</p>"
        "<p>Also, collect all physical items: badges, keys, laptops, mobile devices, and any removable "
        "media. Log the return of each item in your asset management system.</p>"
    ),

    # =========================================================================
    # PHYSICAL PROTECTION (PE) — 6 practices
    # =========================================================================

    "pe-l1-3-10-1": (
        "<p>You need to know who is allowed into the spaces where your systems live, and you need to keep "
        "that list current. This is not just about server rooms \u2014 it includes any area where CUI is "
        "processed or stored.</p>"
        "<p><strong>Example 1:</strong> Maintain a facility access list \u2014 a document or spreadsheet "
        "listing every person authorized to enter your server room, data center, or CUI processing "
        "areas. Include their name, role, and date authorized. Review and update this list at least "
        "quarterly. When someone leaves the company or changes roles, remove them immediately.</p>"
        "<p><strong>Example 2:</strong> Use a badge access control system (e.g., Honeywell Pro-Watch, "
        "LenelS2, or Verkada Access Control) to issue credentials tied to individual employees. "
        "Program the system so that only people on the authorized access list can badge into sensitive "
        "areas. When you revoke authorization, deactivate their badge in the system the same day.</p>"
    ),

    "pe-l2-3-10-2": (
        "<p>It is not enough to control who can enter \u2014 you also need to watch what is happening. "
        "This means monitoring entry points and reviewing the logs for anything unusual.</p>"
        "<p><strong>Example 1:</strong> Install security cameras at all entry and exit points to your "
        "server room and CUI processing areas. Use a system like Verkada, Axis, or Milestone XProtect "
        "that provides motion-triggered recording and at least 30 days of retention. Position cameras "
        "so they capture faces at door-height, not just the tops of heads.</p>"
        "<p><strong>Example 2:</strong> Configure your badge access system to generate alerts for "
        "anomalous events \u2014 such as access attempts outside business hours, repeated failed badge "
        "reads, or tailgating detection (door held open too long). Review physical access logs weekly "
        "or after any security incident. Most access control platforms (LenelS2, Genetec, etc.) can "
        "email alerts automatically to your security team.</p>"
    ),

    "pe-l1-3-10-3": (
        "<p>Every visitor who enters an area where CUI is present must be escorted by an authorized "
        "employee and monitored during their entire visit. No exceptions \u2014 this includes vendor "
        "technicians, delivery personnel, and auditors.</p>"
        "<p><strong>Example 1:</strong> Implement a visitor sign-in process at your front desk or "
        "building entry. Use a visitor management system like Envoy, SwipedOn, or even a simple "
        "paper log. Record the visitor\u2019s name, company, purpose of visit, escort name, and "
        "time in/time out. Issue a temporary visitor badge that is visually distinct from employee "
        "badges (e.g., a bright red \"VISITOR\" lanyard).</p>"
        "<p><strong>Example 2:</strong> Ensure your escort policy is included in employee training. "
        "Employees should know that visitors are never to be left unattended in areas where CUI is "
        "accessible. This includes not propping open secure doors for a vendor \"just for a minute.\" "
        "Post signage near secure areas reminding staff of the escort requirement.</p>"
    ),

    "pe-l1-3-10-4": (
        "<p>You need a record of who entered and exited your facility and when. This audit log is "
        "critical for investigating incidents and proving compliance to an assessor.</p>"
        "<p><strong>Example 1:</strong> Configure your badge access system to retain access logs for "
        "at least one year. Most systems (Honeywell, LenelS2, Genetec) store logs in a database that "
        "you can export to CSV or PDF for assessor review. Make sure the logs capture the badge holder\u2019s "
        "name, the door accessed, the date and time, and whether access was granted or denied.</p>"
        "<p><strong>Example 2:</strong> If you do not have an electronic badge system, maintain a "
        "paper sign-in/sign-out log at each controlled entry point. Each entry should include the "
        "person\u2019s name, date, time in, time out, and purpose. Store completed log sheets in a secure "
        "location (locked file cabinet) and retain them for your defined retention period. Scan and "
        "back up the logs digitally as well.</p>"
    ),

    "pe-l1-3-10-5": (
        "<p>Physical access devices \u2014 keys, badges, key cards, PINs, combination codes \u2014 need to be "
        "controlled and managed. If you do not know where your keys are, you do not really have "
        "physical security.</p>"
        "<p><strong>Example 1:</strong> Maintain a key and badge inventory. Track every physical key "
        "and badge issued: who has it, when it was issued, and what areas it grants access to. Use "
        "a spreadsheet or your access control system\u2019s built-in asset tracking. When a key or badge "
        "is lost, rekey the lock or deactivate the badge immediately and issue a replacement.</p>"
        "<p><strong>Example 2:</strong> Change default access codes and combinations on cipher locks "
        "and keypad entries on a regular schedule (e.g., every 90 days) and whenever someone with "
        "knowledge of the code leaves the organization. Document each code change with the date, "
        "the lock location, and the person who made the change. Avoid obvious codes like 1234 or "
        "the company\u2019s street address.</p>"
    ),

    "pe-l2-3-10-6": (
        "<p>If your employees work from home or other locations outside your main office, those alternate "
        "work sites need security controls too. CUI does not stop being sensitive just because someone "
        "is working from their kitchen table.</p>"
        "<p><strong>Example 1:</strong> Create a telework or remote work policy that defines minimum "
        "security requirements for home offices: the work area must be in a private space (not a "
        "coffee shop), the laptop must have BitLocker enabled, the home Wi-Fi must use WPA3 or WPA2 "
        "with a strong passphrase, and the employee must connect to company resources only through the "
        "VPN. Have employees sign an acknowledgment form agreeing to these requirements.</p>"
        "<p><strong>Example 2:</strong> Use Microsoft Intune compliance policies to enforce security "
        "requirements on devices used at alternate work sites. Create a compliance policy that checks "
        "for BitLocker encryption, up-to-date antivirus definitions, OS patch level, and active "
        "firewall. Mark non-compliant devices as \"not compliant\" in Conditional Access so they cannot "
        "access CUI in SharePoint, Teams, or other M365 services until they meet the baseline.</p>"
    ),
}
