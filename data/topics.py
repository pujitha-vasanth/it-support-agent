"""The fact base behind the generated corpus.

Everything in the corpus, the golden question set and the ticket set is
derived from this one structure. That matters for the evaluation: the correct
answer to a golden question is guaranteed to actually appear in the corpus, so
a wrong answer is a real retrieval or generation failure rather than a data bug.

The company is fictional. The .example top level domain is reserved by the
IETF and can never resolve to a real site.

Each topic yields one document in data/corpus. To swap in your own content,
replace TOPICS and re-run `python -m data.generate`. No application code reads
this file.
"""

from __future__ import annotations

COMPANY = "Meridian Group"
DOMAIN = "meridiangroup.example"
SERVICE_DESK = "servicedesk@meridiangroup.example"
PORTAL = "https://help.meridiangroup.example"

TOPICS: list[dict] = [{'slug': 'vpn-remote-access',
  'title': 'VPN and Remote Access Policy',
  'category': 'network',
  'doc_type': 'policy',
  'owner': 'Network Operations',
  'system': 'Ivanti Secure Access',
  'facts': [('maximum VPN session duration',
             '12 hours, after which re-authentication is required'),
            ('idle disconnect threshold', '30 minutes of inactivity'),
            ('concurrent device limit per user', '3 enrolled devices'),
            ('split tunnelling status',
             'disabled for all users except the Network Operations break-glass group'),
            ('VPN client version floor',
             'Ivanti Secure Access 22.6R2 or later; older clients are blocked at the gateway'),
            ('approval route for contractor VPN access',
             'line manager approval plus Information Security sign-off, valid for 90 days')],
  'definitions': [('Split tunnelling',
                   'a configuration where only corporate-bound traffic crosses the VPN and '
                   'everything else goes direct to the internet'),
                  ('Break-glass access',
                   'a pre-approved emergency account used only during a declared major '
                   'incident, with all sessions recorded'),
                  ('Posture check',
                   "an automated inspection of a device's patch level, disk encryption and "
                   'antivirus state before the tunnel is allowed to establish')],
  'policy_statements': ['Remote access to internal systems is permitted only through the '
                        'approved VPN client on a managed device.',
                        'Personal devices may not establish a VPN tunnel unless enrolled in '
                        'the mobile device management programme.',
                        'All VPN sessions are logged, and connection metadata is retained for '
                        '180 days.',
                        'Users must not share VPN credentials or certificates under any '
                        'circumstances.',
                        'Any device failing a posture check is placed in a remediation network '
                        'with access only to the patching service.'],
  'procedures': [{'name': 'Requesting VPN access for a new employee',
                  'steps': ['Confirm the employee record exists in the HR system and has an '
                            'active start date.',
                            'Raise a request in the service portal under Network Access, '
                            'choosing Standard VPN Profile.',
                            'The line manager approves the request; approval expires if not '
                            'actioned within 5 business days.',
                            'Network Operations assigns the user to the VPN-Standard-Users '
                            'group in the directory.',
                            'The user signs in to the client once on the corporate network so '
                            'the device certificate is issued.',
                            'Confirm the tunnel establishes and the posture check returns a '
                            'compliant result.']},
                 {'name': 'Revoking VPN access',
                  'steps': ['Remove the user from the VPN-Standard-Users group in the '
                            'directory.',
                            'Revoke the device certificate in the certificate authority '
                            'console.',
                            'Terminate any active sessions from the gateway administration '
                            'page.',
                            'Record the revocation against the original access request for '
                            'audit.']},
                 {'name': 'Raising the concurrent device limit',
                  'steps': ['The user submits a justification through the service portal.',
                            'Information Security reviews the justification against the device '
                            'inventory.',
                            'If approved, Network Operations raises the limit to a maximum of '
                            '5 devices.',
                            'The raised limit is reviewed at the next quarterly access '
                            'recertification.']}],
  'troubleshooting': [{'symptom': 'The VPN client reports error IVE-3105 and refuses to '
                                  'connect',
                       'cause': 'The device failed the posture check, almost always because '
                                'disk encryption is off or the antivirus definitions are more '
                                'than 14 days old',
                       'resolution': 'Open the endpoint protection console on the device, run '
                                     'a definition update, confirm disk encryption is enabled, '
                                     'then retry the connection. If it still fails, collect '
                                     'the client log bundle and raise a ticket to Network '
                                     'Operations.',
                       'error_code': 'IVE-3105'},
                      {'symptom': 'The tunnel drops roughly every half hour',
                       'cause': 'The idle disconnect threshold of 30 minutes is being reached '
                                "because the user's work is entirely local",
                       'resolution': 'This is expected behaviour, not a fault. Advise the user '
                                     'to reconnect, or if their role genuinely requires a '
                                     'persistent tunnel, raise a request for the Extended '
                                     'Session profile.',
                       'error_code': ''},
                      {'symptom': 'The user can connect but cannot reach any internal web '
                                  'applications',
                       'cause': 'Internal DNS is not being used because a third-party DNS '
                                'setting on the device is overriding the tunnel configuration',
                       'resolution': 'Reset the network adapter DNS to automatic, reconnect '
                                     'the tunnel, and confirm name resolution against an '
                                     'internal host. Permanent overrides should be removed by '
                                     'Desktop Support.',
                       'error_code': ''},
                      {'symptom': 'A fourth device cannot be enrolled',
                       'cause': 'The concurrent device limit of 3 enrolled devices has been '
                                'reached',
                       'resolution': 'Ask the user to retire an unused device through the '
                                     'self-service page, or submit a justification to raise '
                                     'the limit to a maximum of 5.',
                       'error_code': 'IVE-2240'}],
  'faqs': [('Can I use the VPN from a personal laptop?',
            'Only if that laptop is enrolled in the mobile device management programme. An '
            'unmanaged personal device will fail the posture check.'),
           ('Why do I have to sign in again every morning?',
            'Sessions are capped at 12 hours, so a session started during the working day will '
            'always expire overnight.'),
           ('Does my home internet traffic go through the company network?',
            'Yes. Split tunnelling is disabled, so all traffic crosses the VPN while '
            'connected.'),
           ('How long does contractor VPN access last?',
            '90 days, after which it must be renewed with fresh manager and Information '
            'Security approval.')]},
 {'slug': 'password-and-mfa',
  'title': 'Password and Multi-Factor Authentication Policy',
  'category': 'access',
  'doc_type': 'policy',
  'owner': 'Identity and Access Management',
  'system': 'Entra ID',
  'facts': [('minimum password length',
             '14 characters for standard accounts and 20 characters for privileged accounts'),
            ('password expiry rule',
             'standard passwords do not expire on a schedule; they are changed only on '
             'suspicion of compromise'),
            ('account lockout threshold',
             '10 failed attempts within 15 minutes, with a 30 minute automatic unlock'),
            ('approved MFA methods',
             'the authenticator app with number matching, and FIDO2 security keys; SMS codes '
             'are not accepted'),
            ('MFA re-registration requirement',
             'identity verification with a line manager on a video call before a reset is '
             'issued'),
            ('password manager standard',
             'the corporate vault; storing credentials in browsers or spreadsheets is '
             'prohibited')],
  'definitions': [('Number matching',
                   'an authenticator prompt that shows a two digit number on the sign-in '
                   'screen which the user must type into the app, defeating simple prompt '
                   'bombing'),
                  ('Prompt bombing',
                   'an attack where repeated MFA prompts are sent until a user approves one by '
                   'accident'),
                  ('Privileged account',
                   'any account with administrative rights over a production system, a '
                   "directory, or another user's data")],
  'policy_statements': ['Every account that can reach corporate data must be protected by '
                        'multi-factor authentication.',
                        'Passwords are never to be communicated over email, chat, or a phone '
                        'call.',
                        'Reused passwords from personal services are prohibited and are '
                        'checked against known breach corpora at the point of change.',
                        'Service accounts must use certificate or managed identity '
                        'authentication rather than a password wherever the platform supports '
                        'it.',
                        'Any suspected credential compromise must be reported to the service '
                        'desk within one hour of discovery.'],
  'procedures': [{'name': 'Resetting a forgotten password',
                  'steps': ['The user attempts self-service reset from the sign-in page using '
                            'their registered authenticator.',
                            'If the authenticator is unavailable, the user calls the service '
                            'desk.',
                            'The service desk agent verifies identity on a video call with the '
                            'line manager present.',
                            'A one-time temporary password is issued and must be changed at '
                            'first sign-in.',
                            'The agent records the verification method against the ticket.']},
                 {'name': 'Registering a new MFA device',
                  'steps': ['Sign in to the account security page from a device that is '
                            'already trusted.',
                            'Choose Add method and select the authenticator app or a FIDO2 '
                            'key.',
                            'Complete the registration challenge within the 10 minute window.',
                            'Remove any device that is no longer in use from the registered '
                            'methods list.']},
                 {'name': 'Reporting a suspected credential compromise',
                  'steps': ['Stop using the account immediately and do not attempt to change '
                            'the password yourself.',
                            'Call the service desk and state that this is a suspected '
                            'credential compromise.',
                            'The agent raises a P2 security ticket and revokes all active '
                            'sessions for the account.',
                            'Information Security reviews sign-in logs for the preceding 30 '
                            'days.',
                            'A supervised password and MFA reset is performed once the review '
                            'is complete.']}],
  'troubleshooting': [{'symptom': 'The account is locked after repeated failed sign-ins',
                       'cause': 'The lockout threshold of 10 failed attempts in 15 minutes was '
                                'reached, often by a stale password cached on a phone mail '
                                'client',
                       'resolution': 'Wait for the 30 minute automatic unlock, then remove the '
                                     'saved account from the phone mail client and re-add it. '
                                     'If lockouts repeat, check for a mapped drive or '
                                     'scheduled task still using the old password.',
                       'error_code': 'AADSTS50053'},
                      {'symptom': 'The user receives MFA prompts they did not trigger',
                       'cause': 'Likely prompt bombing following a credential leak',
                       'resolution': 'Instruct the user to deny all prompts and report it '
                                     'immediately. Treat this as a suspected credential '
                                     'compromise and follow that procedure. Do not simply '
                                     'reset the password without a sign-in log review.',
                       'error_code': ''},
                      {'symptom': 'A new phone has no authenticator entries after a handset '
                                  'change',
                       'cause': 'The authenticator was not backed up, or the backup was to a '
                                'personal account that was not restored',
                       'resolution': 'The user must re-register through a verified reset. '
                                     'Identity verification with the line manager on a video '
                                     'call is required before a reset is issued.',
                       'error_code': ''},
                      {'symptom': 'A password change is rejected even though it meets the '
                                  'length rule',
                       'cause': 'The chosen password appears in a known breach corpus, which '
                                'is checked at the point of change',
                       'resolution': 'Ask the user to generate a fresh password in the '
                                     'corporate vault rather than reusing a familiar pattern.',
                       'error_code': 'AADSTS90015'}],
  'faqs': [('How often do I have to change my password?',
            'Standard passwords do not expire on a schedule. You change yours only if there is '
            'reason to suspect it has been compromised.'),
           ('Can I use SMS codes for MFA?',
            'No. Only the authenticator app with number matching and FIDO2 security keys are '
            'accepted.'),
           ('How long is the lockout if I get my password wrong too many times?',
            '30 minutes, applied automatically after 10 failed attempts within 15 minutes.'),
           ('Where should I store passwords?',
            'In the corporate vault. Browser-saved passwords and spreadsheets are '
            'prohibited.')]},
 {'slug': 'laptop-provisioning',
  'title': 'Laptop Provisioning Runbook',
  'category': 'hardware',
  'doc_type': 'runbook',
  'owner': 'Desktop Support',
  'system': 'Microsoft Intune',
  'facts': [('standard laptop build time',
             '6 working hours from stock allocation to handover-ready'),
            ('standard laptop refresh cycle',
             '4 years from the purchase date recorded on the asset record'),
            ('minimum spare laptop buffer held by Desktop Support',
             '18 imaged spare devices across the Meridian Group sites'),
            ('expected Windows Autopilot enrolment window',
             '45 minutes from first boot on a wired connection'),
            ('new starter handover deadline',
             "2 working days before the starter's first working day"),
            ('Meridian Group laptop asset tag format',
             'MG-LT- followed by five digits, for example MG-LT-04172')],
  'definitions': [('Autopilot enrolment',
                   'The process by which a factory-fresh laptop registers itself with '
                   'Microsoft Intune on first boot and pulls the Meridian Group configuration '
                   'profile without a technician imaging it manually.'),
                  ('Golden build',
                   'The approved Windows image and application baseline that Desktop Support '
                   'validates each quarter and applies to every standard Meridian Group '
                   'laptop.'),
                  ('Handover record',
                   'The signed acceptance entry in ServiceNow that links a named asset tag to '
                   'a named employee and starts the warranty and refresh clock.')],
  'policy_statements': ['Every Meridian Group laptop must be enrolled in Microsoft Intune '
                        'before it is handed to an employee, and unenrolled devices must not '
                        'be connected to corporate resources.',
                        'Desktop Support must record the asset tag, serial number and assigned '
                        'user in ServiceNow on the same working day as handover.',
                        'Local administrator rights must not be granted as part of a standard '
                        'build and require a separate approved exception request.',
                        'Laptops returned by leavers must be wiped using the Intune fresh '
                        'start action before they re-enter the spare pool.',
                        'Requests received later than 2 working days before a start date are '
                        'treated as expedited and must be approved by the Desktop Support team '
                        'lead.'],
  'procedures': [{'name': 'Build a standard new starter laptop',
                  'steps': ['Allocate a device from the spare pool and confirm the asset tag '
                            'matches the ServiceNow stock record.',
                            'Connect the laptop to a wired port and power it on to begin '
                            'Windows Autopilot enrolment.',
                            "Sign in with the starter's Entra ID account to trigger the "
                            'Meridian Group configuration profile.',
                            'Confirm in the Intune portal that the device shows as compliant '
                            'and that CrowdStrike has checked in.',
                            'Apply the asset tag label, complete the handover record in '
                            'ServiceNow and set the device state to Assigned.']},
                 {'name': 'Expedite a laptop for a late new starter request',
                  'steps': ['Raise an expedited provisioning task in ServiceNow and link it to '
                            'the original joiner request.',
                            'Obtain written approval from the Desktop Support team lead before '
                            'taking a device from the spare buffer.',
                            'Build the device using the current golden build and skip only the '
                            'optional departmental software.',
                            'Notify the hiring manager by email with the collection time and '
                            'the asset tag.',
                            'Replenish the spare buffer by raising a purchase request the same '
                            'working day.']},
                 {'name': 'Return a leaver laptop to the spare pool',
                  'steps': ['Confirm with the line manager that no local data recovery is '
                            'outstanding.',
                            'Issue the Intune fresh start action and wait for the device to '
                            'report a successful wipe.',
                            'Inspect the chassis, keyboard and battery health and raise a '
                            'repair task if any check fails.',
                            'Re-enrol the device through Autopilot and verify it reaches a '
                            'compliant state.',
                            'Update the ServiceNow asset record to Spare and return the device '
                            'to the stock cupboard.']}],
  'troubleshooting': [{'symptom': 'Autopilot enrolment fails part way through the out of box '
                                  'experience and the laptop returns to the region screen.',
                       'cause': 'The device hardware hash was never uploaded to Intune, so the '
                                'laptop is not recognised as a Meridian Group corporate '
                                'device.',
                       'resolution': 'Collect the hardware hash using the '
                                     'Get-WindowsAutopilotInfo script and upload it to Intune, '
                                     'then reset the device and retry enrolment. Allow a full '
                                     'synchronisation cycle before the second attempt. If '
                                     'enrolment fails again on the same serial number, '
                                     'escalate to the Intune administrators with the enrolment '
                                     'log bundle.',
                       'error_code': 'A-AUTOPILOT-0x801C03F2'},
                      {'symptom': 'A required application in the golden build reports an '
                                  'install failure on a freshly built laptop.',
                       'cause': 'The device is missing a prerequisite runtime because the '
                                'application assignment ran before the dependency finished '
                                'installing.',
                       'resolution': 'Open the Intune device view, check the app install '
                                     'status and trigger a manual sync from the Company '
                                     'Portal. Reinstall the dependency first, then retry the '
                                     'failed application. If the same application fails on '
                                     'more than three builds in a week, escalate to the '
                                     'packaging queue so the dependency order can be '
                                     'corrected.',
                       'error_code': 'A-0x80070643'},
                      {'symptom': 'The laptop shows as non-compliant in Intune immediately '
                                  'after handover even though the build completed.',
                       'cause': 'BitLocker encryption has not finished, so the compliance '
                                'policy evaluates the disk as unprotected.',
                       'resolution': 'Check the BitLocker status on the device and leave it '
                                     'powered on and connected until encryption reaches one '
                                     'hundred per cent. Force a compliance evaluation from the '
                                     'Company Portal afterwards. Escalate to Desktop Support '
                                     'second line if the device is still non-compliant after '
                                     'two evaluation cycles.',
                       'error_code': 'A-INTUNE-0x87D1041C'},
                      {'symptom': 'A spare laptop refuses to start BitLocker and reports a '
                                  'trusted platform module problem.',
                       'cause': 'The trusted platform module is in a cleared or locked state '
                                'after the previous leaver wipe.',
                       'resolution': 'Clear and reinitialise the trusted platform module from '
                                     'firmware settings, then update the firmware to the '
                                     'vendor baseline and retry the build. Record the firmware '
                                     'version in the asset record. If the module still fails, '
                                     'raise a warranty repair with the hardware vendor rather '
                                     'than returning the device to the spare pool.',
                       'error_code': 'A-TPM-0x80284001'}],
  'faqs': [('How long does a standard laptop build take?',
            'A standard build takes 6 working hours from stock allocation to the point where '
            'the device is ready for handover.'),
           ('When am I due a replacement laptop?',
            'Standard laptops are refreshed 4 years from the purchase date held on the asset '
            'record, and Desktop Support contacts you when your device is in scope.'),
           ('How much notice does Desktop Support need for a new starter?',
            'The request must reach Desktop Support so that the laptop is ready 2 working days '
            "before the starter's first working day, otherwise it is handled as an expedited "
            'request.'),
           ('Can I keep my laptop when I move teams?',
            'Yes, the device stays with you and Desktop Support simply updates the assigned '
            'cost centre on the handover record in ServiceNow.')]},
 {'slug': 'email-and-outlook',
  'title': 'Email and Outlook Services Runbook',
  'category': 'productivity',
  'doc_type': 'runbook',
  'owner': 'Messaging Services',
  'system': 'Exchange Online',
  'facts': [('maximum user mailbox size', '100 GB, with a quota warning raised at 90 GB'),
            ('maximum shared mailbox size', '50 GB with no personal archive attached'),
            ('archive policy move window',
             'items older than 1095 days are moved automatically to the online archive'),
            ('recoverable items retention for deleted mail',
             '21 days before items are purged permanently'),
            ('maximum distribution list membership', '2500 recipients per list'),
            ('new mailbox provisioning time',
             '3 hours from the approved joiner request in ServiceNow')],
  'definitions': [('Shared mailbox',
                   'A mailbox with no licensed owner that several named users open alongside '
                   'their own mailbox, used for team addresses such as '
                   'accounts.payable@meridiangroup.example.'),
                  ('Delegation',
                   'A permission that lets one named user send on behalf of, or send as, '
                   'another mailbox without knowing that mailbox password.'),
                  ('Online archive',
                   'The secondary mailbox store in Exchange Online where older mail is moved '
                   'by policy so that the primary mailbox stays under quota.')],
  'policy_statements': ['Mailbox delegation must be requested by the mailbox owner or, for a '
                        'shared mailbox, by the named business owner recorded in ServiceNow.',
                        'Automatic forwarding of Meridian Group mail to external domains is '
                        'blocked by transport rule and requires an approved exception from '
                        'Information Security.',
                        'Shared mailboxes must have a named business owner, and Messaging '
                        'Services disables any shared mailbox whose owner has left and not '
                        'been replaced.',
                        'Users must not use personal email accounts to send Meridian Group '
                        'business correspondence.',
                        'Leaver mailboxes are converted to shared mailboxes for handover only '
                        'when the line manager requests it in writing, and are removed once '
                        'handover is complete.'],
  'procedures': [{'name': 'Create a shared mailbox',
                  'steps': ['Confirm the request names a business owner and the full list of '
                            'members who need access.',
                            'Create the shared mailbox in the Exchange admin centre using the '
                            'agreed address format.',
                            'Create a mail-enabled security group and add the named members to '
                            'it.',
                            'Grant the group full access and send as permissions on the shared '
                            'mailbox.',
                            'Record the business owner and the group name in the ServiceNow '
                            'configuration item and close the request.']},
                 {'name': 'Grant calendar and mailbox delegation',
                  'steps': ['Verify that the mailbox owner has approved the request in '
                            'writing.',
                            'Apply the requested delegate permission level in the Exchange '
                            'admin centre.',
                            'Confirm whether send on behalf of or send as is required and set '
                            'only that permission.',
                            'Ask the delegate to restart Outlook and confirm the mailbox '
                            'appears in their folder list.',
                            'Note the permission and the approval reference on the ServiceNow '
                            'ticket.']},
                 {'name': 'Resolve a mailbox over quota',
                  'steps': ['Check the current mailbox size and the archive status in the '
                            'Exchange admin centre.',
                            'Confirm the archive policy is applied and trigger a managed '
                            'folder assistant run.',
                            'Advise the user to empty the deleted items and junk email '
                            'folders.',
                            'Remove large attachments to a file share or OneDrive location if '
                            'the archive alone is not enough.',
                            'Apply a temporary quota uplift for a maximum of 14 days if the '
                            'user needs time to tidy the mailbox.',
                            'Confirm the mailbox is back under 90 GB and close the ticket.']}],
  'troubleshooting': [{'symptom': 'A user reports that outbound mail is rejected with a '
                                  'message saying the recipient mailbox is full.',
                       'cause': 'The recipient mailbox has reached its quota and Exchange '
                                'Online is refusing further delivery.',
                       'resolution': 'Confirm the recipient is internal and check the mailbox '
                                     'size against the 100 GB limit. Run the archive policy '
                                     'and ask the recipient to clear deleted items, then ask '
                                     'the sender to retry. Escalate to Messaging Services '
                                     'second line if the mailbox cannot be brought under quota '
                                     'within the same working day.',
                       'error_code': 'A-QUOTA-5.2.2'},
                      {'symptom': 'Outlook repeatedly prompts for credentials and will not '
                                  'connect to the mailbox.',
                       'cause': 'A stale cached credential in the Windows credential manager '
                                'is being replayed against Exchange Online.',
                       'resolution': 'Remove the Office and Exchange entries from the Windows '
                                     'credential manager, close Outlook fully and sign in '
                                     "again with the user's Entra ID account. Check that the "
                                     'device is compliant so conditional access does not block '
                                     'the sign-in. Escalate to the identity team if the prompt '
                                     'returns after a second clean sign-in.',
                       'error_code': 'A-MAPI-0x8004010F'},
                      {'symptom': 'A delegate cannot send as a shared mailbox and receives a '
                                  'delivery failure within seconds.',
                       'cause': 'The delegate holds full access only, and send as permission '
                                'was never granted on the shared mailbox.',
                       'resolution': 'Add the send as permission to the security group that '
                                     'fronts the shared mailbox, then wait for directory '
                                     'replication before retesting. Ask the delegate to '
                                     'restart Outlook so the permission cache refreshes. '
                                     'Escalate to Messaging Services if the failure persists '
                                     'more than one hour after the permission change.',
                       'error_code': 'A-EXO-550-5.4.1'},
                      {'symptom': 'Outlook on the web loads to a blank page for one user while '
                                  'the desktop client works normally.',
                       'cause': 'A corrupt mailbox setting or a stale browser session token is '
                                'breaking the web session.',
                       'resolution': 'Ask the user to clear the browser cache and sign in from '
                                     'a private window to rule out the token. If the page is '
                                     'still blank, reset the Outlook on the web settings for '
                                     'that mailbox from the Exchange admin centre. Escalate to '
                                     'Microsoft support with the session identifier if a '
                                     'settings reset does not fix it.',
                       'error_code': 'A-OWA-500-17'}],
  'faqs': [('How large can my mailbox get?',
            'Your mailbox can hold up to 100 GB, and you receive a warning once it passes 90 '
            'GB.'),
           ('Can I recover mail I deleted last week?',
            'Yes, deleted items stay recoverable for 21 days before they are purged '
            'permanently.'),
           ('Why has older mail disappeared from my inbox?',
            'Mail older than 1095 days is moved automatically to your online archive, which '
            'you can still search from Outlook.'),
           ('How quickly will a new joiner get a mailbox?',
            'A mailbox is created within 3 hours of the approved joiner request in '
            'ServiceNow.')]},
 {'slug': 'printing-services',
  'title': 'Printing Services Runbook',
  'category': 'hardware',
  'doc_type': 'runbook',
  'owner': 'Print Services',
  'system': 'PaperCut MF',
  'facts': [('follow-me print job hold time',
             '12 hours before an unreleased job is deleted from the queue'),
            ('minimum supported print driver package version',
             '7.1.4 of the Meridian Group universal driver package'),
            ('maximum scan to email attachment size', '25 MB per scanned document'),
            ('monthly colour printing allowance per user',
             '400 colour pages per calendar month'),
            ('printer fault response target',
             '8 working hours for a device that is the only printer on a floor'),
            ('secure release PIN length',
             '6 digits, set by the user in the PaperCut MF web portal')],
  'definitions': [('Follow-me printing',
                   'A print model where a job is held centrally and only prints once the user '
                   'authenticates at any Meridian Group multifunction device with their badge '
                   'or PIN.'),
                  ('Print queue',
                   'The named shared queue on the print servers that accepts jobs from client '
                   'devices and holds them until release or expiry.'),
                  ('Scan to email',
                   'The multifunction device feature that sends a scanned document directly to '
                   'the signed-in user mailbox at firstname.lastname@meridiangroup.example.')],
  'policy_statements': ['All Meridian Group printing must go through the follow-me queue, and '
                        'direct IP printing to a device is only permitted for approved '
                        'production printers.',
                        'Colour printing is enabled by default for every user up to the '
                        'monthly allowance, and additional colour volume requires line manager '
                        'approval.',
                        'Print drivers must be deployed through Microsoft Intune, and users '
                        'must not install vendor drivers downloaded from the internet.',
                        'Confidential documents must be released at the device by the document '
                        'owner and must not be left on the output tray.',
                        'Print Services must review device placement and volume reporting each '
                        'quarter and remove devices printing fewer than 200 pages a month.'],
  'procedures': [{'name': 'Add a new multifunction device to the follow-me estate',
                  'steps': ['Confirm the network port is active and record the device serial '
                            'number and floor location.',
                            'Register the device in PaperCut MF and assign it to the correct '
                            'site and cost centre.',
                            'Add the device to the follow-me queue and set colour and duplex '
                            'defaults.',
                            'Install the embedded PaperCut MF software on the device and test '
                            'badge release.',
                            'Run a test print and a test scan to email, then publish the '
                            'device name to the floor distribution list.']},
                 {'name': 'Deploy an updated print driver package',
                  'steps': ['Package the new universal driver version and test it against two '
                            'device models in the pilot ring.',
                            'Upload the package to Microsoft Intune and assign it to the pilot '
                            'device group.',
                            'Monitor install success for five working days and review any '
                            'reported failures.',
                            'Expand the assignment to all managed laptops once the pilot ring '
                            'reports no regressions.',
                            'Retire the previous driver package and update the minimum '
                            'supported version in the runbook.']},
                 {'name': 'Set up scan to email for a user',
                  'steps': ['Confirm the user mailbox is active and uses the standard Meridian '
                            'Group address format.',
                            'Check that the user has a badge registered or a secure release '
                            'PIN set in PaperCut MF.',
                            'Ask the user to authenticate at the device and open the scan to '
                            'email workflow.',
                            'Send a one page test scan and confirm it arrives in the user '
                            'mailbox.',
                            'Advise the user to split documents that would exceed the '
                            'attachment limit.']}],
  'troubleshooting': [{'symptom': 'A user releases a job at the device and it prints the first '
                                  'page then stops with a device error.',
                       'cause': 'The device firmware is behind the baseline and is rejecting '
                                'the current driver page description language.',
                       'resolution': 'Update the device firmware to the vendor baseline during '
                                     'the next maintenance window and reprint the job. As an '
                                     'interim step, release the job on a different device on '
                                     'the same floor. Escalate to the print hardware vendor if '
                                     'the fault repeats after the firmware update.',
                       'error_code': 'A-PCMF-1142'},
                      {'symptom': 'Jobs sent from a laptop never appear in the follow-me queue '
                                  'at any device.',
                       'cause': 'The client is still using an old driver package that points '
                                'at a decommissioned print server.',
                       'resolution': 'Remove the old printer object from the laptop, then push '
                                     'the current driver package from Microsoft Intune and '
                                     'confirm the version is 7.1.4 or later. Send a test print '
                                     'and release it at the nearest device. Escalate to Print '
                                     'Services second line if the queue still does not receive '
                                     'jobs after the redeployment.',
                       'error_code': 'A-DRV-0x80070705'},
                      {'symptom': 'Scan to email completes at the device but no email ever '
                                  'arrives.',
                       'cause': 'The scanned file exceeds the attachment limit and the mail '
                                'relay is dropping the message.',
                       'resolution': 'Ask the user to rescan at a lower resolution or split '
                                     'the document so each file stays under the attachment '
                                     'limit. Confirm delivery of the smaller test scan before '
                                     'closing. Escalate to Messaging Services if a small test '
                                     'scan also fails to arrive, because that points at the '
                                     'mail relay rather than the device.',
                       'error_code': 'A-SCAN-SMTP-554'},
                      {'symptom': 'Several users on one floor report that printing hangs with '
                                  'a spooler error after a Windows update.',
                       'cause': 'A point and print restriction introduced by the update is '
                                'blocking the queue connection.',
                       'resolution': 'Confirm the current driver package is installed locally '
                                     'rather than pulled from the server, then restart the '
                                     'print spooler service on the affected laptops. Verify '
                                     'the Intune configuration profile for point and print is '
                                     'applied. Escalate to Desktop Support if more than five '
                                     'users on the same floor are still affected after the '
                                     'profile check.',
                       'error_code': 'A-PRN-0x0000011B'}],
  'faqs': [('How long do my print jobs wait at the device?',
            'Jobs are held for 12 hours and are deleted automatically if you do not release '
            'them in that time.'),
           ('How much colour printing can I do?',
            'Every user has an allowance of 400 colour pages per calendar month, and more '
            'requires line manager approval.'),
           ('Why was my scan rejected?',
            'Scan to email accepts attachments up to 25 MB, so a long or high resolution scan '
            'needs to be split or rescanned at a lower setting.'),
           ('Can I install a printer driver myself?',
            'No, drivers are deployed through Microsoft Intune and the supported package is '
            'version 7.1.4 or later.')]},
 {'slug': 'software-request-and-install',
  'title': 'Software Request and Installation Policy',
  'category': 'software',
  'doc_type': 'policy',
  'owner': 'IT Asset Management',
  'system': 'ServiceNow',
  'facts': [('number of titles in the approved software catalogue', '312 approved titles'),
            ('number of catalogue titles available without approval',
             '74 titles published for self-service install in the Company Portal'),
            ('turnaround for a non-catalogue software request',
             '5 working days from submission to decision'),
            ('licence true-up cadence',
             'quarterly, on the 15th of the month following each quarter end'),
            ('removal deadline for unapproved software',
             '72 hours from the detection alert being raised'),
            ('spend threshold requiring Finance approval',
             'GBP 1,500 per request, including the first year of support')],
  'definitions': [('Approved software catalogue',
                   'The list of titles that IT Asset Management has licensed, security '
                   'reviewed and packaged for deployment to Meridian Group devices.'),
                  ('Self-service install',
                   'A catalogue title a user can install on demand from the Company Portal '
                   'without raising a ServiceNow request, because approval is granted in '
                   'advance.'),
                  ('Unapproved software',
                   'Any application found on a managed device that does not appear in the '
                   'approved software catalogue and has no recorded exception.')],
  'policy_statements': ['All software installed on Meridian Group devices must appear in the '
                        'approved software catalogue or hold a recorded exception approved by '
                        'Information Security.',
                        'Non-catalogue requests must be approved by the requester line manager '
                        'and then by IT Asset Management before any licence is purchased.',
                        'Requests above the Finance approval threshold must also be approved '
                        'by the Finance business partner for the requesting cost centre.',
                        'Users must not install software using personal licences, trial keys '
                        'or licences bought on expenses.',
                        'IT Asset Management must reconcile deployed installs against '
                        'purchased entitlements at every true-up and reclaim unused licences.'],
  'procedures': [{'name': 'Request a title that is not in the catalogue',
                  'steps': ['Raise a software request in ServiceNow and state the business '
                            'need, the number of users and the preferred vendor.',
                            'Attach any vendor quote so the request can be checked against the '
                            'Finance approval threshold.',
                            'Route the request to the line manager for approval.',
                            'Allow IT Asset Management to complete the security and licensing '
                            'review within the published turnaround.',
                            'Accept the decision recorded on the ticket, and if approved wait '
                            'for the packaged title to be assigned to your device.']},
                 {'name': 'Add an approved title to the catalogue',
                  'steps': ['Confirm the signed licence agreement and entitlement count are '
                            'stored against the vendor record.',
                            'Package the title and test it on two pilot devices from the '
                            'requesting team.',
                            'Create the catalogue item in ServiceNow and set whether approval '
                            'is required or the title is self-service.',
                            'Assign the packaged application in Microsoft Intune to the '
                            'matching Entra ID group.',
                            'Publish the new catalogue entry and update the catalogue title '
                            'count.']},
                 {'name': 'Handle an unapproved software detection',
                  'steps': ['Review the detection alert and confirm the title is genuinely '
                            'absent from the catalogue and has no exception.',
                            'Contact the device owner and explain the removal deadline.',
                            'Ask the owner whether a catalogue equivalent meets the same need '
                            'and offer it as a replacement.',
                            'Remove the title through Microsoft Intune if the owner has not '
                            'uninstalled it by the deadline.',
                            'Record the outcome against the device configuration item in '
                            'ServiceNow.']}],
  'troubleshooting': [{'symptom': 'A ServiceNow software request sits at the approval stage '
                                  'with nobody listed as approver.',
                       'cause': 'The requester line manager field in the directory is empty, '
                                'so the approval cannot be routed.',
                       'resolution': 'Correct the manager attribute on the requester record in '
                                     'Entra ID and ask the requester to resubmit the request '
                                     'so the approval routes correctly. Confirm the approval '
                                     'task appears for the manager. Escalate to the HR systems '
                                     'team if the manager attribute is repeatedly blank after '
                                     'a directory sync.',
                       'error_code': 'A-SNOW-REQ-4091'},
                      {'symptom': 'A self-service title fails to install from the Company '
                                  'Portal and reports a generic installer failure.',
                       'cause': 'An older version of the same title is still present and the '
                                'installer cannot upgrade in place.',
                       'resolution': 'Uninstall the previous version, reboot the device and '
                                     'retry the install from the Company Portal. Check the '
                                     'Intune install status to confirm the assignment is '
                                     'targeted at the device. Escalate to the packaging queue '
                                     'if the same title fails on more than two devices.',
                       'error_code': 'A-MSI-1603'},
                      {'symptom': 'A user reports that an application they downloaded from the '
                                  'internet is blocked from running.',
                       'cause': 'The application is not in the approved catalogue, so the '
                                'application control policy is blocking the executable.',
                       'resolution': 'Explain that the block is expected and offer the nearest '
                                     'catalogue equivalent, or help the user raise a '
                                     'non-catalogue request. Do not create an application '
                                     'control exclusion without Information Security approval. '
                                     'Escalate to Information Security only when a '
                                     'business-critical process is stopped and no catalogue '
                                     'alternative exists.',
                       'error_code': 'A-APPLOCKER-8004'},
                      {'symptom': 'A licensed title prompts for activation on a device that '
                                  'should already be entitled.',
                       'cause': 'The device is not a member of the Entra ID group that carries '
                                'the licence assignment.',
                       'resolution': 'Add the device or user to the correct licensing group, '
                                     'then force an Intune sync and reopen the application. '
                                     'Verify the entitlement count has headroom before adding '
                                     'the member. Escalate to IT Asset Management if the '
                                     'entitlement pool is already fully consumed, because a '
                                     'purchase may be needed.',
                       'error_code': 'A-LIC-0x87D13B66'}],
  'faqs': [('How do I get software that is not in the catalogue?',
            'Raise a software request in ServiceNow and expect a decision within 5 working '
            'days once your line manager has approved it.'),
           ('Which software can I install without asking?',
            '74 of the 312 catalogue titles are published for self-service install in the '
            'Company Portal and need no approval.'),
           ('Do I need Finance approval?',
            'Finance approval is needed once a single request exceeds GBP 1,500 including the '
            'first year of support.'),
           ('What happens if unapproved software is found on my laptop?',
            'You are asked to remove it within 72 hours of the detection alert, and IT Asset '
            'Management removes it remotely if it is still there.')]},
 {'slug': 'wifi-and-network-access',
  'title': 'Wi-Fi and Network Access Runbook',
  'category': 'network',
  'doc_type': 'runbook',
  'owner': 'Network Services',
  'system': 'Cisco Identity Services Engine',
  'facts': [('corporate wireless network name and authentication method',
             'MG-CORP, using certificate based EAP-TLS authentication'),
            ('guest Wi-Fi voucher validity', '36 hours from first use of the voucher code'),
            ('guest Wi-Fi bandwidth cap per device', '10 Mbps download and upload'),
            ('device authentication certificate lifetime',
             '400 days, with automatic renewal starting 30 days before expiry'),
            ('wired port activation lead time', '4 working days from the approved request'),
            ('personal device registration limit on MG-BYOD',
             '6 registered personal devices per employee')],
  'definitions': [('EAP-TLS',
                   'A wireless authentication method where the laptop presents a machine '
                   'certificate issued by the Meridian Group certificate authority instead of '
                   'a username and password.'),
                  ('Guest voucher',
                   'A time-limited code issued by reception or a sponsoring employee that '
                   'grants a visitor internet-only access on the MG-GUEST network.'),
                  ('Posture check',
                   'The Cisco Identity Services Engine assessment that confirms a device is '
                   'managed, encrypted and running current endpoint protection before it is '
                   'placed on the corporate network.')],
  'policy_statements': ['Only devices holding a valid Meridian Group machine certificate may '
                        'join MG-CORP, and pre-shared keys must never be used on the corporate '
                        'network.',
                        'Visitors must be sponsored by a named employee, and guest vouchers '
                        'must not be reissued to the same visitor to extend access beyond the '
                        'voucher validity.',
                        'Personal devices may join MG-BYOD only, and must not be connected to '
                        'corporate wired ports.',
                        'Wired ports in meeting rooms and public areas remain disabled by '
                        'default and are enabled only for an approved business need.',
                        'Network Services must review and remove dormant device registrations '
                        'at least once every quarter.'],
  'procedures': [{'name': 'Onboard a managed laptop onto MG-CORP',
                  'steps': ['Confirm the laptop is enrolled in Microsoft Intune and reports as '
                            'compliant.',
                            'Verify the machine certificate is present and within its validity '
                            'period.',
                            'Connect to MG-CORP and allow the posture check to complete.',
                            'Confirm in Cisco Identity Services Engine that the device landed '
                            'in the corporate authorisation profile.',
                            'Record the device MAC address against the asset record if it is a '
                            'new build.']},
                 {'name': 'Issue guest Wi-Fi access for a visitor',
                  'steps': ['Confirm the sponsoring employee name and the date of the visit.',
                            'Create a guest account in the sponsor portal and set the expiry '
                            'to match the voucher validity.',
                            'Hand the voucher code to the visitor at reception and explain the '
                            'bandwidth cap.',
                            'Ask the visitor to connect to MG-GUEST and accept the acceptable '
                            'use notice.',
                            'Let the voucher lapse at expiry rather than extending it.']},
                 {'name': 'Activate a wired network port',
                  'steps': ['Raise a port activation request in ServiceNow with the room '
                            'number and the faceplate label.',
                            'Obtain approval from the site facilities contact and from Network '
                            'Services.',
                            'Trace the faceplate label to the switch port in the patching '
                            'records.',
                            'Configure the switch port with the correct access profile and '
                            'enable it.',
                            'Test with a managed laptop and confirm the port authorises '
                            'through Cisco Identity Services Engine.',
                            'Update the patching records and close the request.']}],
  'troubleshooting': [{'symptom': 'A managed laptop cannot join MG-CORP and reports that '
                                  'authentication failed immediately.',
                       'cause': 'The machine certificate has expired or was never issued, so '
                                'EAP-TLS has nothing to present.',
                       'resolution': 'Check the certificate store on the device and trigger '
                                     'the certificate profile from Microsoft Intune to reissue '
                                     'the machine certificate. Reconnect to MG-CORP once the '
                                     'certificate shows a valid date range. Escalate to the '
                                     'certificate authority team if enrolment fails twice on '
                                     'the same device.',
                       'error_code': 'A-EAPTLS-0x80420012'},
                      {'symptom': 'A laptop connects to MG-CORP but is placed on a restricted '
                                  'network with no access to internal systems.',
                       'cause': 'The posture check failed because the endpoint protection '
                                'agent has not reported in recently.',
                       'resolution': 'Confirm the CrowdStrike agent is running and has checked '
                                     'in, then disconnect and reconnect so the posture check '
                                     'runs again. Review the posture result in Cisco Identity '
                                     'Services Engine. Escalate to Information Security if the '
                                     'agent cannot be brought back into a reporting state.',
                       'error_code': 'A-ISE-11514'},
                      {'symptom': 'A newly activated wired port shows a link light but the '
                                  'laptop receives no usable address.',
                       'cause': 'The switch port is enabled but the correct access profile and '
                                'VLAN were not applied, so the address request is never '
                                'answered.',
                       'resolution': 'Check the switch port configuration against the standard '
                                     'access profile and apply the missing VLAN assignment. '
                                     'Bounce the port and retest with a managed laptop. '
                                     'Escalate to Network Services second line if the port '
                                     'still fails after the configuration is confirmed '
                                     'correct.',
                       'error_code': 'A-DHCP-1056'},
                      {'symptom': 'A user reports they cannot register another personal phone '
                                  'on MG-BYOD.',
                       'cause': 'The user has reached the personal device registration limit '
                                'and the portal is refusing a further registration.',
                       'resolution': 'Ask the user to remove a device they no longer own from '
                                     'the registration portal, then retry the registration. '
                                     'Explain that the limit applies per employee and is not '
                                     'raised on request. Escalate to Network Services only if '
                                     'removed devices still count towards the limit after an '
                                     'hour.',
                       'error_code': 'A-DOT1X-4402'}],
  'faqs': [('Which Wi-Fi network should I use on my work laptop?',
            'Use MG-CORP, which authenticates your laptop automatically with a certificate '
            'rather than a password.'),
           ('How long does a visitor voucher last?',
            'A guest voucher is valid for 36 hours from first use and is not extended.'),
           ('How many personal devices can I register?',
            'You can register up to 6 personal devices on MG-BYOD at any one time.'),
           ('How long will it take to get a desk network port switched on?',
            'Wired port activation takes 4 working days from the point the request is '
            'approved.')]},
 {'slug': 'vdi-virtual-desktop',
  'title': 'Virtual Desktop Services Runbook',
  'category': 'infrastructure',
  'doc_type': 'runbook',
  'owner': 'Infrastructure Services',
  'system': 'Azure Virtual Desktop',
  'facts': [('maximum concurrent user sessions per session host',
             '14 sessions on a standard multi-session host'),
            ('idle session disconnect threshold',
             '25 minutes of inactivity before the session is disconnected'),
            ('disconnected session sign-out threshold',
             '11 hours before a disconnected session is signed out and its host released'),
            ('maximum FSLogix profile container size', '35 GB per user profile'),
            ('number of published applications in the virtual desktop catalogue',
             '46 published applications'),
            ('scaling plan ramp-up window',
             '06:45 to 19:30 United Kingdom time on working days')],
  'definitions': [('Host pool',
                   'A group of identically built Azure Virtual Desktop session hosts that '
                   'share a single set of users, applications and session limits.'),
                  ('Published application',
                   'A single application delivered from a host pool and launched in its own '
                   'window, rather than the user signing in to a full desktop.'),
                  ('FSLogix profile container',
                   'The virtual disk that holds a user Windows profile so that settings, mail '
                   'cache and desktop follow the user between session hosts.')],
  'policy_statements': ['Virtual desktop access must be requested for a named user and is '
                        'granted through the Entra ID group that fronts the relevant host '
                        'pool.',
                        'Users must not store business data on the session host local drives, '
                        'because hosts are rebuilt on each image release.',
                        'Personal host pools are reserved for roles with an approved technical '
                        'justification, and all other users receive multi-session pooled '
                        'desktops.',
                        'Infrastructure Services must apply the monthly image update to every '
                        'host pool within the agreed maintenance window and keep one previous '
                        'image version available for rollback.',
                        'Session limits and the scaling plan must not be changed for an '
                        'individual user, and capacity concerns must be raised as a capacity '
                        'request instead.'],
  'procedures': [{'name': 'Grant a user access to a pooled virtual desktop',
                  'steps': ['Confirm the request names the host pool and has line manager '
                            'approval.',
                            'Add the user to the Entra ID group assigned to that host pool.',
                            'Confirm the FSLogix profile container is created on first '
                            'sign-in.',
                            'Ask the user to launch the desktop from the Windows App and '
                            'confirm the published applications appear.',
                            'Record the host pool and the access group on the ServiceNow '
                            'request.']},
                 {'name': 'Publish a new application to a host pool',
                  'steps': ['Install and test the application on a single session host taken '
                            'out of the pool.',
                            'Bake the application into the next host pool image and validate '
                            'it on two rebuilt hosts.',
                            'Create the application entry in the host pool application group.',
                            'Assign the application group to the Entra ID group for the '
                            'requesting team.',
                            'Confirm the application launches for a pilot user and update the '
                            'published application count.']},
                 {'name': 'Apply a monthly host pool image update',
                  'steps': ['Announce the maintenance window to the affected host pool user '
                            'groups.',
                            'Set the host pool to drain mode so no new sessions land on hosts '
                            'due to be rebuilt.',
                            'Wait for active sessions to end, then rebuild the hosts from the '
                            'new image version.',
                            'Validate sign-in, profile load and two published applications on '
                            'each rebuilt host.',
                            'Remove drain mode, confirm the scaling plan is active and keep '
                            'the previous image version for rollback.']}],
  'troubleshooting': [{'symptom': 'A user signs in to a pooled desktop and receives a '
                                  'temporary profile with none of their settings.',
                       'cause': 'The FSLogix profile container could not be attached, usually '
                                'because it is locked by a previous session or has reached its '
                                'size limit.',
                       'resolution': 'Check whether the container is still attached to another '
                                     'session host and sign the stale session out. Confirm the '
                                     'container is within its size limit and expand only after '
                                     'the data owner has cleared unnecessary cache. Escalate '
                                     'to Infrastructure Services second line if the container '
                                     'fails to attach after the stale session is cleared.',
                       'error_code': 'A-FSLOGIX-0x00000020'},
                      {'symptom': 'Users report that the virtual desktop refuses new '
                                  'connections during the morning peak.',
                       'cause': 'Every session host has reached the concurrent session limit '
                                'and the scaling plan has not yet added capacity.',
                       'resolution': 'Check the host pool session count against the per-host '
                                     'limit and confirm the scaling plan ramp-up window has '
                                     'started. Add session hosts manually if the peak is '
                                     'earlier than the ramp-up window. Escalate as a capacity '
                                     'request to Infrastructure Services if the pool hits its '
                                     'limit on more than three mornings in a month.',
                       'error_code': 'A-AVD-0x3000047'},
                      {'symptom': 'A user is repeatedly dropped out of their virtual desktop '
                                  'while reading long documents.',
                       'cause': 'The session is being treated as idle and disconnected by the '
                                'inactivity policy because no input is registered.',
                       'resolution': 'Explain the idle disconnect threshold and confirm the '
                                     'user can reconnect to the same session without losing '
                                     'work. Check for network instability on the client side '
                                     'if the disconnects happen well inside the threshold. '
                                     'Escalate to Network Services when packet loss is '
                                     'confirmed on the client connection.',
                       'error_code': 'A-RDP-0x204'},
                      {'symptom': 'External users cannot reach the virtual desktop at all '
                                  'while office users connect normally.',
                       'cause': 'The gateway connection is being blocked, commonly by '
                                'conditional access or a client that cannot complete the '
                                'gateway handshake.',
                       'resolution': 'Confirm the user device is compliant so conditional '
                                     'access allows the gateway connection, then update the '
                                     'Windows App client to the current version and retry. '
                                     'Test from a second network to rule out the user home '
                                     'connection. Escalate to Infrastructure Services with the '
                                     'connection activity identifier if the gateway still '
                                     'refuses the session.',
                       'error_code': 'A-RDGW-50331678'}],
  'faqs': [('Why was I disconnected from my virtual desktop?',
            'Sessions are disconnected after 25 minutes of inactivity, and you can reconnect '
            'to the same session without losing your work.'),
           ('How long does a disconnected session stay available?',
            'A disconnected session is signed out after 11 hours, at which point unsaved work '
            'is lost.'),
           ('Can I save files on the virtual desktop itself?',
            'No, store work in OneDrive or an approved network share, because session hosts '
            'are rebuilt with every monthly image release.'),
           ('How large can my virtual desktop profile grow?',
            'The FSLogix profile container is capped at 35 GB per user.')]},
 {'slug': 'file-shares-and-storage',
  'title': 'File Shares and Storage Policy',
  'category': 'storage',
  'doc_type': 'policy',
  'owner': 'Storage and Collaboration',
  'system': 'Microsoft SharePoint Online',
  'facts': [('personal home drive quota', '250 GB per employee'),
            ('default departmental network share quota',
             '2 TB per department, raised only by an approved capacity request'),
            ('OneDrive storage allocation per licensed user', '5 TB per user'),
            ('second stage recycle bin retention',
             '93 days before a deleted item is purged permanently'),
            ('share permission access review cadence',
             'every 180 days, signed off by the named data owner'),
            ('retention period for finance record shares',
             '1825 days from the end of the financial year the records belong to')],
  'definitions': [('Data owner',
                   'The named business manager accountable for who may access a share or '
                   'SharePoint site and for signing off each access review.'),
                  ('Departmental share',
                   'A network share mapped by group policy for a single department, used for '
                   'records that must stay inside the department rather than being shared '
                   'broadly.'),
                  ('Known folder move',
                   'The OneDrive feature that redirects the Desktop, Documents and Pictures '
                   'folders into OneDrive so that local files are backed up automatically.')],
  'policy_statements': ['Every departmental share and SharePoint site must have a named data '
                        'owner recorded in ServiceNow before it is created.',
                        'Access to shares must be granted through Entra ID groups only, and '
                        'direct permissions on folders are not permitted.',
                        'Business data must be stored in OneDrive, SharePoint Online or an '
                        'approved network share, and never only on a laptop local disk.',
                        'Anonymous external sharing links are disabled across Meridian Group, '
                        'and external sharing must use a named guest account.',
                        'Data owners must complete each access review within the review '
                        'cadence, and Storage and Collaboration removes access that is not '
                        'reconfirmed.'],
  'procedures': [{'name': 'Request access to a departmental share',
                  'steps': ['Raise an access request in ServiceNow naming the share and the '
                            'business reason.',
                            'Allow the request to route to the named data owner for approval.',
                            'Wait for Storage and Collaboration to add you to the Entra ID '
                            'access group.',
                            'Sign out and sign back in so the new group membership is picked '
                            'up.',
                            'Confirm you can open the share and report any folder you still '
                            'cannot read.']},
                 {'name': 'Create a new departmental share',
                  'steps': ['Confirm the named data owner and the requested capacity against '
                            'the default quota.',
                            'Create the share on the storage platform and apply the default '
                            'quota.',
                            'Create the read and read-write Entra ID access groups and apply '
                            'them to the share.',
                            'Add the share to the group policy mapping for the department.',
                            'Record the share, data owner and review date in the ServiceNow '
                            'configuration item.']},
                 {'name': 'Run a share access review',
                  'steps': ['Export the current membership of every access group attached to '
                            'the share.',
                            'Send the membership list to the named data owner with the review '
                            'deadline.',
                            'Remove every member the data owner does not reconfirm.',
                            'Record the signed-off review against the configuration item.',
                            'Set the next review date in line with the review cadence.']}],
  'troubleshooting': [{'symptom': 'A user sees an access denied message when opening a '
                                  'departmental share they were just granted.',
                       'cause': 'The group membership has not yet been picked up by the user '
                                'current sign-in token.',
                       'resolution': 'Ask the user to sign out fully and sign back in, then '
                                     'retry the share. Confirm the membership is present in '
                                     'the Entra ID group before investigating further. '
                                     'Escalate to Storage and Collaboration if access is still '
                                     'denied after a clean sign-in and the membership is '
                                     'confirmed.',
                       'error_code': 'A-SMB-1326'},
                      {'symptom': 'OneDrive shows a paused sync and a red cross on the taskbar '
                                  'icon for one user.',
                       'cause': 'A file path exceeds the supported length or contains an '
                                'unsupported character, so the client cannot complete the '
                                'upload.',
                       'resolution': 'Open the OneDrive activity centre, identify the blocked '
                                     'file and shorten the path or rename the file, then '
                                     'resume sync. Advise the user to keep folder nesting '
                                     'shallow under known folder move. Escalate to Storage and '
                                     'Collaboration if sync stays paused once the reported '
                                     'file is fixed.',
                       'error_code': 'A-ODSYNC-0x8004de40'},
                      {'symptom': 'An external partner reports that a SharePoint sharing link '
                                  'does not work for them.',
                       'cause': 'The link was created as an anonymous link, which is disabled '
                                'across the tenant.',
                       'resolution': 'Recreate the link as a specific people link addressed to '
                                     'the partner work email so a named guest account is '
                                     'created. Confirm the partner accepts the guest '
                                     'invitation before testing again. Escalate to Information '
                                     'Security if the partner domain is blocked from guest '
                                     'access.',
                       'error_code': 'A-SPO-403-19'},
                      {'symptom': 'Users cannot save new files to a departmental share '
                                  'although existing files open normally.',
                       'cause': 'The share has reached its quota, so writes are refused while '
                                'reads continue to work.',
                       'resolution': 'Check the share usage against its quota and ask the data '
                                     'owner to archive or delete content that is past its '
                                     'retention point. Raise a capacity request if the '
                                     'department genuinely needs more than the default quota. '
                                     'Escalate to Storage and Collaboration immediately if the '
                                     'share supports a time-critical finance process.',
                       'error_code': 'A-NTFS-0x80070052'}],
  'faqs': [('How much space do I get in OneDrive?',
            'Each licensed user has 5 TB of OneDrive storage, which is separate from the 250 '
            'GB home drive quota.'),
           ('Can I recover a file I deleted a month ago?',
            'Yes, deleted items stay in the second stage recycle bin for 93 days before they '
            'are purged permanently.'),
           ('How often is my share access checked?',
            'Share access is reviewed every 180 days and your access is removed if the data '
            'owner does not reconfirm it.'),
           ('Can I send an open link to someone outside Meridian Group?',
            'No, anonymous links are disabled, so use a specific people link that creates a '
            'named guest account for the recipient.')]},
 {'slug': 'backup-and-restore',
  'title': 'Backup and Restore Runbook',
  'category': 'storage',
  'doc_type': 'runbook',
  'owner': 'Infrastructure Services',
  'system': 'Veeam Backup and Replication',
  'facts': [('backup window for production file servers',
             '21:45 to 04:15 each night, with incremental jobs every 4 hours during the day'),
            ('retention tiers',
             'three tiers: 14 daily restore points, 11 weekly restore points and 37 monthly '
             'restore points'),
            ('recovery point objective for tier 1 systems',
             '12 minutes, delivered by continuous replication'),
            ('recovery time objective for tier 1 systems',
             '2 hours from the declaration of a restore event'),
            ('standard restore request turnaround',
             '6 working hours for a single file and 29 working hours for a full virtual '
             'machine'),
            ('restore test cadence',
             'a sampled restore test of 7 randomly chosen workloads on the second Tuesday of '
             'every month')],
  'definitions': [('Restore point',
                   'a single recoverable copy of a workload captured at one moment in time, '
                   'identified by its job name and timestamp'),
                  ('Synthetic full',
                   'a full backup file assembled from existing increments on the repository '
                   'rather than re-reading the source data'),
                  ('Immutable repository',
                   'backup storage where restore points cannot be deleted or altered until '
                   'their lock period expires')],
  'policy_statements': ['Every production workload must be assigned a backup tier before it is '
                        'released into service.',
                        "Restore requests for another person's data require written approval "
                        "from that person's line manager.",
                        'Backup job failures must be acknowledged by Infrastructure Services '
                        'within 90 minutes of the alert.',
                        'Immutability is enabled on all monthly restore points and may not be '
                        'disabled without Information Security approval.',
                        'No backup data may be copied to removable media or to storage outside '
                        'the approved repositories.'],
  'procedures': [{'name': 'Requesting a single file restore',
                  'steps': ['Raise a request in the service portal under Data Recovery and '
                            'select Single File Restore.',
                            'Supply the full original path, the file name and the date the '
                            'file was last known to be correct.',
                            'Confirm whether the file should be restored in place or to an '
                            'alternative folder.',
                            'Wait for the data owner to approve the request if the file '
                            'belongs to another user.',
                            'Infrastructure Services mounts the nearest valid restore point '
                            'and copies the file to the agreed location.',
                            'Confirm with the requester that the recovered file opens '
                            'correctly, then close the request.']},
                 {'name': 'Running the monthly sampled restore test',
                  'steps': ['Select 7 workloads at random from the protected workload '
                            'inventory.',
                            'Restore each workload into the isolated recovery network, never '
                            'into production.',
                            'Start each restored workload and verify that its primary service '
                            'responds.',
                            'Record the measured restore duration against the tier target for '
                            'each workload.',
                            'Delete the test copies from the recovery network once '
                            'verification is complete.',
                            'File the results in the monthly recovery assurance record.']},
                 {'name': 'Recovering a failed backup job',
                  'steps': ['Open the job in the backup console and read the last session log.',
                            'Confirm the repository has free capacity and that the source '
                            'workload is powered on.',
                            'Clear any stale snapshot left behind by the previous attempt.',
                            'Re-run the job in active full mode if the increment chain is '
                            'reported as broken.',
                            'Escalate to the storage vendor if the job fails a second time '
                            'with the same error.']}],
  'troubleshooting': [{'symptom': 'Nightly job ends with a warning that the snapshot could not '
                                  'be removed.',
                       'cause': 'An earlier session left an orphaned snapshot on the virtual '
                                'machine, so the new snapshot cannot be consolidated.',
                       'resolution': "Open the virtual machine's snapshot manager and "
                                     'consolidate the orphaned snapshot during the next '
                                     'maintenance slot. Re-run the job in incremental mode and '
                                     'confirm the warning clears. If consolidation fails or '
                                     'the snapshot chain is longer than three entries, '
                                     'escalate to Infrastructure Services so the disk chain '
                                     'can be repaired before the next window.',
                       'error_code': 'B-VEEAM-1432'},
                      {'symptom': 'Restore to the original location fails part way through '
                                  'with an access denied message.',
                       'cause': 'The service account used by the restore proxy no longer holds '
                                'write permission on the target folder.',
                       'resolution': 'Check the target folder permissions and re-grant write '
                                     'access to the backup service account. Restart the '
                                     'restore to an alternative folder so the user is not left '
                                     'waiting, then move the data back once permissions are '
                                     'corrected. Escalate to Information Security if the '
                                     'permission change was not requested through the normal '
                                     'access process.',
                       'error_code': 'B-0x80070005'},
                      {'symptom': 'The repository reports that it is full even though old '
                                  'restore points appear to have expired.',
                       'cause': 'Expired monthly restore points are still inside their '
                                'immutability lock period and cannot yet be removed.',
                       'resolution': 'Read the lock expiry date on the oldest monthly restore '
                                     'point and calculate when space will be released. '
                                     'Redirect the affected jobs to the secondary repository '
                                     'for the interim period. Raise a capacity request with '
                                     'Infrastructure Services if the shortfall will last more '
                                     'than two nights.',
                       'error_code': 'B-VEEAM-0x2F19'},
                      {'symptom': 'A user reports that a file they deleted last month cannot '
                                  'be found in any restore point.',
                       'cause': 'The file was created and deleted entirely between two daily '
                                'restore points, so it was never captured.',
                       'resolution': 'Confirm the deletion date against the retention tiers '
                                     'and check the 11 weekly and 37 monthly restore points '
                                     'before concluding the file is unrecoverable. Tell the '
                                     'user plainly if no restore point holds the file. Record '
                                     'the gap so the backup frequency for that share can be '
                                     'reviewed.',
                       'error_code': ''}],
  'faqs': [('How far back can my files be restored?',
            'Backups are kept in three tiers: 14 daily, 11 weekly and 37 monthly restore '
            'points, so the oldest recoverable copy is a little over three years old.'),
           ('How quickly will a single file restore be completed?',
            'A single file restore is completed within 6 working hours of approval, while a '
            'full virtual machine restore takes up to 29 working hours.'),
           ("Can I ask for a colleague's file to be restored?",
            "Yes, but the request needs written approval from that colleague's line manager "
            'before Infrastructure Services will action it.'),
           ('Are restores actually tested?',
            'Yes, 7 randomly chosen workloads are restored and verified in an isolated network '
            'on the second Tuesday of every month.')]},
 {'slug': 'security-incident-response',
  'title': 'Security Incident Response Runbook',
  'category': 'security',
  'doc_type': 'runbook',
  'owner': 'Information Security',
  'system': 'CrowdStrike Falcon',
  'facts': [('severity levels',
             'four levels: Sev1 critical, Sev2 high, Sev3 moderate and Sev4 low'),
            ('Sev1 initial response target',
             '20 minutes from alert to an acknowledged responder'),
            ('Sev2 initial response target',
             '75 minutes from alert to an acknowledged responder'),
            ('authority to declare a Sev1 incident',
             'the on-call Information Security duty manager, with no second approval needed'),
            ('evidence retention period for a closed incident',
             '26 months from the closure date, held in the sealed evidence store'),
            ('post incident review deadline',
             '8 working days after closure for Sev1 and Sev2 incidents')],
  'definitions': [('Containment',
                   'action taken to stop an incident spreading further, such as network '
                   'isolation of a host or disabling an account'),
                  ('Chain of custody',
                   'the written record of everyone who has handled a piece of evidence, with '
                   'the date, time and reason for each handover'),
                  ('Indicator of compromise',
                   'an observable artefact such as a file hash, domain or process name that '
                   'suggests a system has been attacked')],
  'policy_statements': ['Any suspected security incident must be reported to Information '
                        'Security before any attempt is made to fix it locally.',
                        'A compromised endpoint must be network isolated rather than powered '
                        'off, so that volatile evidence is preserved.',
                        'Only Information Security may communicate about an active incident '
                        'outside the response team.',
                        'Evidence must be collected to the sealed evidence store with an '
                        'unbroken chain of custody record.',
                        'No incident may be closed until the containment and eradication '
                        'actions have been independently verified by a second responder.'],
  'procedures': [{'name': 'Declaring a security incident',
                  'steps': ['Capture what was observed, when it was observed and which systems '
                            'or accounts are involved.',
                            'Contact the Information Security duty manager on the published '
                            'on-call number.',
                            'Agree the severity level against the four level scale.',
                            'Open an incident record and assign a lead responder and a scribe.',
                            'Open the incident bridge and invite only the named response team.',
                            'Record the declaration time, which starts the response clock.']},
                 {'name': 'Containing a compromised endpoint',
                  'steps': ['Place the endpoint into network containment from the endpoint '
                            'protection console.',
                            'Leave the endpoint powered on so that memory and running process '
                            'evidence survive.',
                            'Disable the signed in account and revoke its active sessions and '
                            'refresh tokens.',
                            'Collect a triage package from the contained host before any '
                            'remediation is attempted.',
                            'Hand the triage package to the evidence custodian and sign the '
                            'chain of custody record.',
                            'Release containment only after a second responder has verified '
                            'the host is clean.']},
                 {'name': 'Handling incident communications',
                  'steps': ['Confirm with the incident lead which facts have been verified and '
                            'may be shared.',
                            'Draft a single holding statement for internal audiences and have '
                            'the incident lead approve it.',
                            'Send updates on a fixed cadence agreed at declaration rather than '
                            'on request.',
                            'Route all external and regulatory enquiries to Information '
                            'Security without comment.',
                            'Publish the closure notice only after the incident record has '
                            'been formally closed.']}],
  'troubleshooting': [{'symptom': 'The endpoint agent reports the host as contained but the '
                                  'user can still reach internal applications.',
                       'cause': 'The containment policy was applied to a stale device record '
                                'while the user is working on a newly rebuilt device.',
                       'resolution': 'Match the device serial number in the console against '
                                     'the device the user is actually holding and apply '
                                     'containment to the correct record. Confirm loss of '
                                     'connectivity with the user before continuing. Escalate '
                                     'to Information Security immediately if the correct host '
                                     'cannot be identified within the Sev1 response target of '
                                     '20 minutes.',
                       'error_code': 'B-CRWD-4401'},
                      {'symptom': 'A disabled account continues to send mail for a short '
                                  'period after containment.',
                       'cause': 'Existing refresh tokens remained valid because only the '
                                'password was reset and sessions were not revoked.',
                       'resolution': 'Revoke all sessions and refresh tokens for the account '
                                     'in the identity console, then confirm the mailbox stops '
                                     'sending. Check mailbox rules for any forwarding rule '
                                     'added by the attacker. Escalate to the incident lead if '
                                     'mail continues after revocation, as that suggests a '
                                     'second compromised identity.',
                       'error_code': 'B-IR-5512'},
                      {'symptom': 'Triage evidence cannot be uploaded to the sealed evidence '
                                  'store.',
                       'cause': "The responder's account is not a member of the evidence "
                                'custodian group, which is the only group permitted to write '
                                'to the store.',
                       'resolution': 'Hand the package to a named evidence custodian rather '
                                     'than requesting the group membership mid incident. '
                                     'Record the handover in the chain of custody with the '
                                     'time and reason. Escalate to the duty manager if no '
                                     'custodian is reachable, so a temporary custodian can be '
                                     'appointed and logged.',
                       'error_code': 'B-EVD-0x1A7'},
                      {'symptom': 'Two separate incident records have been opened for what '
                                  'turns out to be one event.',
                       'cause': 'Parallel reports from the service desk and the monitoring '
                                'platform were each declared before correlation took place.',
                       'resolution': 'Keep the earliest declared record as the master and link '
                                     'the later record to it as a duplicate. Carry the '
                                     'declaration time of the master record forward so the '
                                     'response clock is not reset. Tell both reporters which '
                                     'record number is now authoritative.',
                       'error_code': ''}],
  'faqs': [('Who can declare a critical security incident?',
            'The on-call Information Security duty manager can declare a Sev1 incident alone, '
            'with no second approval required.'),
           ('How quickly must a Sev1 incident be picked up?',
            'A responder must acknowledge a Sev1 within 20 minutes of the alert, compared with '
            '75 minutes for a Sev2.'),
           ('Should I switch off a machine I think is infected?',
            'No, isolate it from the network and leave it powered on so that memory and '
            'process evidence is preserved for the responders.'),
           ('How long is incident evidence kept?',
            'Evidence is held in the sealed evidence store for 26 months from the date the '
            'incident was closed.')]},
 {'slug': 'phishing-and-email-security',
  'title': 'Phishing and Email Security Policy',
  'category': 'security',
  'doc_type': 'policy',
  'owner': 'Information Security',
  'system': 'Microsoft Defender for Office 365',
  'facts': [('reporting route for suspicious mail',
             'the Report Phishing button in Outlook, which delivers the message to the '
             'Information Security triage queue'),
            ('phishing triage service level',
             'a first assessment within 45 minutes during business hours and within 3 hours '
             'out of hours'),
            ('quarantine release approval',
             'Information Security only; line managers and the service desk cannot release a '
             'quarantined message'),
            ('quarantine retention period',
             '22 days, after which quarantined messages are deleted automatically'),
            ('blocked attachment types',
             'a list of 18 executable and script extensions, including .exe, .js, .vbs, .scr '
             'and .iso'),
            ('simulation programme frequency',
             'a phishing simulation to every employee once per quarter, with a reporting rate '
             'target of 65 percent')],
  'definitions': [('Business email compromise',
                   "an attack in which a trusted sender's account or display name is abused to "
                   'request a payment or a data change'),
                  ('Quarantine',
                   'a holding area where a suspicious message is stored unopened so that it '
                   "cannot reach the recipient's mailbox"),
                  ('Safe link rewriting',
                   'the replacement of a URL in an inbound message with a checking service '
                   'address that inspects the destination at the moment of the click')],
  'policy_statements': ['Suspicious messages must be reported with the Report Phishing button '
                        'and must not be forwarded to colleagues.',
                        'Employees must never act on a payment or bank detail change request '
                        'received by email without separate verbal verification.',
                        'Password and credential entry is only permitted on pages reached from '
                        'a bookmark or from the service portal, never from an email link.',
                        'Automatic external forwarding of company mail to a personal address '
                        'is prohibited for all employees.',
                        'Employees who report a simulated phishing message are never '
                        'penalised, and reporting rates are measured at team level only.'],
  'procedures': [{'name': 'Reporting a suspicious message',
                  'steps': ['Do not click any link or open any attachment in the message.',
                            'Select the message in Outlook and use the Report Phishing button.',
                            'Confirm the report when prompted, which also removes the message '
                            'from the mailbox.',
                            'Tell the service desk separately if credentials were already '
                            'entered or an attachment was already opened.',
                            'Wait for the triage outcome notice rather than retrieving the '
                            'message from the deleted items folder.']},
                 {'name': 'Requesting the release of a quarantined message',
                  'steps': ['Note the quarantine notification identifier and the sender '
                            'address from the daily digest.',
                            'Raise a request in the service portal under Email Security and '
                            'attach the identifier.',
                            'State why the message is expected and what business process '
                            'depends on it.',
                            'Information Security inspects the message and its attachments in '
                            'the analysis sandbox.',
                            'Information Security releases the message to the single recipient '
                            'or confirms that it will stay blocked.']},
                 {'name': 'Responding to a confirmed credential phishing click',
                  'steps': ["Reset the affected user's password immediately and revoke all "
                            'active sessions.',
                            'Check the mailbox for newly created forwarding or inbox rules and '
                            'remove any found.',
                            'Search the mail flow for other recipients of the same campaign '
                            'and purge the message.',
                            'Add the sending domain and any payload URL to the block list.',
                            'Raise a security incident at the appropriate severity if company '
                            'data was submitted.']}],
  'troubleshooting': [{'symptom': 'A legitimate supplier invoice is quarantined every month.',
                       'cause': "The supplier's sending domain has no valid sender "
                                'authentication record, so each message scores as a spoof.',
                       'resolution': 'Release the current message through Information '
                                     'Security, then ask the supplier to publish a valid '
                                     'sender authentication record. Add a narrowly scoped '
                                     'allow entry for that sender while the supplier makes the '
                                     'change, with a review date. Escalate to Information '
                                     'Security if the supplier refuses, as a permanent bypass '
                                     'needs a recorded risk acceptance.',
                       'error_code': 'B-DEF-5503'},
                      {'symptom': 'The Report Phishing button is missing from the Outlook '
                                  'ribbon.',
                       'cause': "The reporting add-in has not been deployed to the user's "
                                'mailbox or the client is running in a cached offline state.',
                       'resolution': 'Ask the user to restart Outlook and confirm they are '
                                     'signed in with their work account. If the button is '
                                     'still absent, check the add-in deployment for that '
                                     'mailbox and redeploy it. In the meantime, have the user '
                                     'send the message as an attachment to the service desk so '
                                     'triage is not delayed beyond the 45 minute target.',
                       'error_code': 'B-OL-0x8004010F'},
                      {'symptom': 'A user cannot open an attachment that a colleague says they '
                                  'received successfully.',
                       'cause': 'The attachment uses one of the 18 blocked executable or '
                                'script extensions and was stripped on delivery.',
                       'resolution': 'Confirm the extension against the blocked list and tell '
                                     'the user the file will not be delivered by email. Ask '
                                     'the sender to share the file through the approved file '
                                     'sharing service instead. Escalate to Information '
                                     'Security only if the file is genuinely required in its '
                                     'executable form, so a controlled transfer can be '
                                     'arranged.',
                       'error_code': 'B-ATT-1189'},
                      {'symptom': 'Quarantine digest links return a message that the item is '
                                  'no longer available.',
                       'cause': 'The message passed the 22 day quarantine retention period and '
                                'was deleted automatically.',
                       'resolution': 'Explain that quarantined mail is removed after 22 days '
                                     'and cannot be recovered afterwards. Ask the sender to '
                                     'resend the message so it can be triaged within the '
                                     'retention window. Record the case if the same sender is '
                                     'repeatedly quarantined, so the sender can be assessed '
                                     'properly.',
                       'error_code': ''}],
  'faqs': [('What should I do with an email I think is phishing?',
            'Use the Report Phishing button in Outlook and do not forward the message to '
            'anyone else.'),
           ('How soon will my phishing report be looked at?',
            'Reports are first assessed within 45 minutes during business hours and within 3 '
            'hours outside business hours.'),
           ('Can my manager release a blocked email for me?',
            'No, only Information Security can release a quarantined message, and quarantined '
            'items are deleted after 22 days.'),
           ('Will I be in trouble for failing a phishing simulation?',
            'No, the quarterly simulations are measured at team level against a 65 percent '
            'reporting target, and individuals are never penalised.')]},
 {'slug': 'data-classification',
  'title': 'Data Classification Policy',
  'category': 'security',
  'doc_type': 'policy',
  'owner': 'Information Governance',
  'system': 'Microsoft Purview Information Protection',
  'facts': [('classification tiers',
             'four tiers: Public, Internal, Confidential and Restricted'),
            ('default label applied to new documents',
             'Internal, applied automatically when no label is chosen'),
            ('mandatory labelling scope',
             'every document and email created in the productivity suite, with no option to '
             'save unlabelled'),
            ('maximum external sharing link lifetime for Confidential data',
             '21 days, after which the link expires and must be reissued'),
            ('external sharing rule for Restricted data',
             'prohibited entirely; Restricted data may only be accessed inside the managed '
             'environment'),
            ('label change approval for a downgrade',
             'the data owner plus Information Governance, recorded against the document '
             'identifier')],
  'definitions': [('Data owner',
                   'the named accountable person for a set of data, responsible for its '
                   'classification and for approving access to it'),
                  ('Label downgrade',
                   'a change that moves a document to a less restrictive tier, for example '
                   'from Confidential to Internal'),
                  ('Sensitivity label',
                   'a persistent marker applied to a file or message that carries the '
                   'classification and the protection settings with the content')],
  'policy_statements': ['Every document and email must carry a sensitivity label before it is '
                        'saved or sent.',
                        'Restricted data must not be copied to removable media, personal '
                        'storage or any unmanaged device.',
                        'Confidential data may be shared externally only through an expiring '
                        'link issued to a named recipient.',
                        "A label may only be downgraded with the data owner's approval and an "
                        'Information Governance record of the reason.',
                        'Printed Confidential or Restricted material must be collected '
                        'immediately and may not be left in a shared area.'],
  'procedures': [{'name': 'Classifying a new document',
                  'steps': ['Decide who may legitimately see the content before writing it.',
                            'Apply the lowest label that still protects the content '
                            'adequately.',
                            'Apply Restricted only where disclosure would cause serious harm '
                            'to the company or an individual.',
                            "Add the data owner's name to the document properties so "
                            'accountability is clear.',
                            'Save the document in the repository that matches the chosen '
                            'label.']},
                 {'name': 'Sharing Confidential data with an external party',
                  'steps': ['Confirm an active agreement with the external party covers the '
                            'data in question.',
                            "Create a sharing link scoped to the named recipient's email "
                            'address only.',
                            'Set the link to expire no later than the 21 day maximum.',
                            'Disable download on the link where the recipient only needs to '
                            'read the content.',
                            'Record the share and its expiry date in the sharing register.',
                            'Revoke the link as soon as the business need ends.']},
                 {'name': 'Requesting a label downgrade',
                  'steps': ['Raise a request in the service portal under Information '
                            'Governance and quote the document identifier.',
                            'State the current label, the requested label and the reason for '
                            'the change.',
                            "Obtain the data owner's written approval on the request.",
                            'Information Governance reviews the content and either applies or '
                            'refuses the downgrade.',
                            'Information Governance records the decision and the reason '
                            'against the document identifier.']}],
  'troubleshooting': [{'symptom': 'A user cannot save a document because the application '
                                  'insists on a label.',
                       'cause': 'Mandatory labelling is in force across the productivity suite '
                                'and no label has been selected on the document.',
                       'resolution': 'Ask the user to pick a label from the sensitivity menu, '
                                     'defaulting to Internal if they are unsure. Explain that '
                                     'Internal is applied automatically to new documents and '
                                     'is safe for everyday work. Escalate to Information '
                                     'Governance only if the label menu itself does not appear '
                                     'after a restart and sign in.',
                       'error_code': 'B-PURV-2209'},
                      {'symptom': 'An external recipient reports that a shared link no longer '
                                  'opens.',
                       'cause': 'The link reached its expiry date, which cannot exceed 21 days '
                                'for Confidential data.',
                       'resolution': 'Confirm the business need still exists, then issue a '
                                     'fresh link to the same named recipient with a new expiry '
                                     'date. Update the sharing register with the reissue. '
                                     'Escalate to Information Governance if the recipient '
                                     'needs standing access, as that calls for a different '
                                     'arrangement than repeated links.',
                       'error_code': 'B-SHR-0x4412'},
                      {'symptom': 'A Restricted file cannot be copied to a USB drive.',
                       'cause': 'Restricted data is blocked from removable media by policy, '
                                'and the block is enforced at the endpoint.',
                       'resolution': 'Explain that the block is intended and that Restricted '
                                     'data stays inside the managed environment. Offer an '
                                     'in-environment alternative such as a shared workspace '
                                     'with the correct label. Do not request a policy '
                                     'exception; escalate to Information Governance if the '
                                     'business process genuinely cannot work any other way.',
                       'error_code': 'B-DLP-7731'},
                      {'symptom': 'A document appears with a lower label than the user '
                                  'remembers applying.',
                       'cause': 'A downgrade was approved and applied through the governance '
                                'process, or the document was recreated from an unlabelled '
                                'template.',
                       'resolution': 'Check the document identifier against the Information '
                                     'Governance downgrade record to see whether an approved '
                                     'change exists. If no record exists, reapply the correct '
                                     'label and report it as a possible mislabelling. Escalate '
                                     'to Information Governance if Confidential or Restricted '
                                     'content was left at a lower tier while it was being '
                                     'shared.',
                       'error_code': ''}],
  'faqs': [('How many classification levels are there?',
            'Four: Public, Internal, Confidential and Restricted.'),
           ('What happens if I forget to pick a label?',
            'New documents receive the Internal label automatically, and the application will '
            'not let you save a document with no label at all.'),
           ('Can I send Restricted data to a client?',
            'No, Restricted data cannot be shared externally at all and must stay inside the '
            'managed environment.'),
           ('How long does an external link to Confidential data last?',
            'No more than 21 days, after which it expires and a new link must be issued to the '
            'named recipient.')]},
 {'slug': 'byod-mobile-devices',
  'title': 'BYOD and Mobile Device Policy',
  'category': 'mobile',
  'doc_type': 'policy',
  'owner': 'End User Computing',
  'system': 'Microsoft Intune',
  'facts': [('enrolment deadline for a new personal device',
             '5 working days from the access request being approved'),
            ('minimum operating system versions',
             'iOS 17.4 or later and Android 14 or later; devices below these floors are '
             'blocked from company data'),
            ('supported device limit per employee', '2 personal mobile devices per employee'),
            ('passcode requirement on an enrolled personal device',
             'a 6 digit passcode or biometric unlock, with a 5 minute screen lock timeout'),
            ('wipe scope on a personal device',
             'selective wipe of the company container only; personal photos, messages and apps '
             'are never removed'),
            ('automatic unenrolment trigger',
             '19 consecutive days with no check-in to the management service')],
  'definitions': [('Containerisation',
                   'the separation of company apps and data into a managed area of the device '
                   'that is encrypted and controlled independently of personal content'),
                  ('Selective wipe',
                   'the removal of only the company container and its data, leaving the '
                   "owner's personal content untouched"),
                  ('Compliance policy',
                   'the set of device conditions, such as operating system version and '
                   'passcode strength, that must be met before company data is released to the '
                   'device')],
  'policy_statements': ['Company data may be accessed on a personal device only after the '
                        'device is enrolled and reported compliant.',
                        'Company data must remain inside the managed container and must not be '
                        'copied into personal apps or personal cloud storage.',
                        'Employees must report a lost or stolen enrolled device to the service '
                        'desk before any other action.',
                        'The company will only ever perform a selective wipe of the company '
                        'container on a personal device.',
                        'Rooted, jailbroken or developer-unlocked devices are refused access '
                        'to company data with no exception process.'],
  'procedures': [{'name': 'Enrolling a personal mobile device',
                  'steps': ['Raise a request in the service portal under Mobile Access and '
                            'accept the acceptable use terms.',
                            'Confirm the device meets the operating system floor of iOS 17.4 '
                            'or Android 14.',
                            "Install the company portal app from the device's official app "
                            'store.',
                            'Sign in with the work account and complete the enrolment prompts.',
                            'Set a 6 digit passcode or biometric unlock when the device asks '
                            'for one.',
                            'Confirm the device shows as compliant in the company portal '
                            'before opening company mail.']},
                 {'name': 'Reporting a lost or stolen enrolled device',
                  'steps': ['Telephone the service desk as soon as the loss is discovered.',
                            'Confirm the device make, model and the approximate time it was '
                            "last in the employee's possession.",
                            "The service desk revokes the work account's active sessions "
                            'immediately.',
                            'End User Computing issues a selective wipe of the company '
                            'container.',
                            'Confirm with the employee that personal content was not affected '
                            'by the wipe.',
                            'Record the device as retired in the mobile inventory.']},
                 {'name': 'Removing a personal device from management',
                  'steps': ['Raise a request in the service portal under Mobile Access and '
                            'choose Unenrol Device.',
                            'Confirm no company data is held outside the managed container.',
                            'End User Computing issues the selective wipe and confirms the '
                            'container is removed.',
                            'Remove the company portal app from the device.',
                            "Confirm the device no longer appears against the employee's 2 "
                            'device allowance.']}],
  'troubleshooting': [{'symptom': 'Company mail stops syncing on a personal phone and the '
                                  'portal shows the device as not compliant.',
                       'cause': 'The device operating system has fallen below the supported '
                                'floor, or the required passcode has been removed.',
                       'resolution': 'Ask the user to update to at least iOS 17.4 or Android '
                                     '14 and to set a 6 digit passcode. Have them open the '
                                     'company portal and run a compliance check so the result '
                                     'is re-evaluated. Escalate to End User Computing if the '
                                     'device still reports non-compliant after a successful '
                                     'update and check.',
                       'error_code': 'B-INTUNE-0x87D1FDE8'},
                      {'symptom': 'Enrolment fails at sign in with a message that the device '
                                  'cannot be registered.',
                       'cause': 'The employee already has 2 enrolled personal devices, which '
                                'is the maximum allowed.',
                       'resolution': "Check the employee's enrolled devices and identify any "
                                     'device no longer in use. Unenrol the retired device, '
                                     'then retry enrolment on the new one. Escalate to End '
                                     'User Computing only where a genuine business case exists '
                                     'for a third device, as the limit needs an owner '
                                     'decision.',
                       'error_code': 'B-INTUNE-0x80180014'},
                      {'symptom': 'A device disappeared from the management console on its '
                                  'own.',
                       'cause': 'The device went 19 consecutive days without checking in and '
                                'was unenrolled automatically.',
                       'resolution': 'Explain that automatic unenrolment happens after 19 days '
                                     'with no check-in and that the device must be enrolled '
                                     'again. Walk the user through a fresh enrolment in the '
                                     'company portal. Escalate if the device was in daily use, '
                                     'since repeated check-in failure points to a network or '
                                     'app problem rather than disuse.',
                       'error_code': 'B-MDM-3374'},
                      {'symptom': 'A user is worried that reporting a lost phone will delete '
                                  'their family photographs.',
                       'cause': 'The user is unaware that only a selective wipe of the company '
                                'container is performed on a personal device.',
                       'resolution': 'Reassure the user that only the company container is '
                                     'removed and that personal photos, messages and apps are '
                                     'never touched. Complete the loss report without delay so '
                                     'sessions can be revoked. Record the reassurance given, '
                                     'as delayed reporting is the real risk here.',
                       'error_code': ''}],
  'faqs': [('Will the company wipe my whole phone?',
            'No, only the company container is removed by a selective wipe; your personal '
            'photos, messages and apps are never deleted.'),
           ('Which phone versions are supported?',
            'iOS 17.4 or later and Android 14 or later; anything older is blocked from company '
            'data.'),
           ('How many personal devices can I enrol?',
            'Two personal mobile devices per employee.'),
           ('Why did my phone drop out of management?',
            'Devices that do not check in for 19 consecutive days are unenrolled automatically '
            'and need to be enrolled again.')]},
 {'slug': 'asset-lifecycle-management',
  'title': 'IT Asset Lifecycle Management Policy',
  'category': 'hardware',
  'doc_type': 'policy',
  'owner': 'IT Asset Management',
  'system': 'ServiceNow IT Asset Management',
  'facts': [('standard laptop refresh cycle', '46 months from the purchase date'),
            ('monitor and peripheral refresh cycle',
             '7 years from the purchase date, or on failure if sooner'),
            ('asset tag format',
             'MG followed by a six digit sequence, for example MG004821, applied before the '
             'device leaves the build room'),
            ('buffer stock level for standard laptops',
             '9 percent of the deployed fleet, with a reorder trigger at 4 percent'),
            ('procurement lead time for a standard laptop',
             '13 working days from approved purchase order to build room receipt'),
            ('data destruction standard at disposal',
             'a certified three pass overwrite, or physical destruction for any drive that '
             'fails the overwrite')],
  'definitions': [('Asset tag',
                   'the unique company identifier applied physically to a device and recorded '
                   'against it in the asset register'),
                  ('Buffer stock',
                   'unallocated built devices held ready so that a replacement can be issued '
                   'without waiting for procurement'),
                  ('Certificate of destruction',
                   'the supplier document confirming that a named drive serial number was '
                   'destroyed or securely overwritten')],
  'policy_statements': ['No device may be issued to an employee until it carries an asset tag '
                        'and a matching asset register record.',
                        'Hardware purchases outside the standard catalogue require IT Asset '
                        'Management approval before any order is raised.',
                        'Devices returned by leavers must be received into the build room '
                        'within 3 working days of the leaving date.',
                        'No storage device may leave company premises for disposal without a '
                        'recorded certificate of destruction.',
                        'Employees are accountable for the devices recorded against their name '
                        'until the return is confirmed in the asset register.'],
  'procedures': [{'name': 'Receiving and tagging a new device',
                  'steps': ['Check the delivered serial numbers against the purchase order '
                            'before signing for the delivery.',
                            'Create the asset record and assign the next asset tag in the MG '
                            'sequence.',
                            'Apply the physical asset tag to the device chassis.',
                            'Run the standard build and record the build version against the '
                            'asset record.',
                            'Move the asset to Available status so it counts towards buffer '
                            'stock.']},
                 {'name': 'Issuing a replacement device on refresh',
                  'steps': ['Identify devices that have reached 46 months from their purchase '
                            'date.',
                            'Contact the device holder and agree a swap date at least a week '
                            'ahead.',
                            'Allocate an available buffer stock device and record the new '
                            'assignment.',
                            "Transfer the user's data and confirm with the user that nothing "
                            'is missing.',
                            'Receive the old device into the build room and set it to Pending '
                            'Disposal.',
                            'Close the refresh record once both asset records show the correct '
                            'holder.']},
                 {'name': 'Disposing of a retired device',
                  'steps': ['Confirm the asset is in Pending Disposal status and has no '
                            'outstanding assignment.',
                            'Run the certified three pass overwrite on every storage device.',
                            'Send any drive that fails the overwrite for physical destruction '
                            'instead.',
                            'Collect the certificate of destruction from the disposal '
                            'supplier.',
                            'Attach the certificate to the asset record and set the asset to '
                            'Disposed.']}],
  'troubleshooting': [{'symptom': 'A device in use has no record in the asset register.',
                       'cause': 'The device was issued before tagging, so the register record '
                                'was never created.',
                       'resolution': 'Capture the serial number and model, create the missing '
                                     'asset record and apply an asset tag at the next '
                                     'opportunity. Confirm the current holder and the '
                                     'approximate issue date so the refresh clock can be set. '
                                     'Escalate to IT Asset Management if the device cannot be '
                                     'matched to any purchase order, as that suggests an '
                                     'unapproved purchase.',
                       'error_code': 'B-SNOW-6621'},
                      {'symptom': 'A replacement laptop cannot be issued because none are '
                                  'available.',
                       'cause': 'Buffer stock has dropped below the 4 percent reorder trigger '
                                'and no order was raised in time.',
                       'resolution': 'Raise the replenishment order immediately, allowing for '
                                     'the 13 working day procurement lead time. Offer the user '
                                     'a temporary loan device from the short term pool so work '
                                     'is not blocked. Escalate to IT Asset Management so the '
                                     'reorder trigger can be checked for why it did not fire.',
                       'error_code': 'B-ASSET-0x3307'},
                      {'symptom': "A leaver's laptop has not been returned two weeks after "
                                  'their leaving date.',
                       'cause': 'The return was not arranged within the 3 working day window '
                                'and no collection was booked.',
                       'resolution': "Contact the former employee's line manager with the "
                                     'asset tag and serial number and book a collection. Keep '
                                     'the asset in Awaiting Return status so it remains '
                                     'visible on the overdue report. Escalate to IT Asset '
                                     'Management and Information Security if the device is '
                                     'still outstanding after a second request, so the data on '
                                     'it can be assessed.',
                       'error_code': 'B-RET-4150'},
                      {'symptom': 'A disposal batch cannot be closed in the asset register.',
                       'cause': 'One or more drive serial numbers in the batch have no '
                                'matching certificate of destruction attached.',
                       'resolution': 'List the serial numbers with no certificate and request '
                                     'the missing documents from the disposal supplier. Hold '
                                     'the batch open until every drive is covered. Escalate to '
                                     'IT Asset Management if the supplier cannot produce a '
                                     'certificate for a drive, because the asset cannot be '
                                     'recorded as Disposed without one.',
                       'error_code': ''}],
  'faqs': [('When will my laptop be replaced?',
            'Standard laptops are refreshed at 46 months from their purchase date, and '
            'monitors and peripherals at 7 years or on failure.'),
           ('How long does a new laptop take to arrive?',
            'A standard laptop takes 13 working days from approved purchase order to arriving '
            'in the build room.'),
           ('What happens to the data on a retired laptop?',
            'Every storage device gets a certified three pass overwrite, and any drive that '
            'fails is physically destroyed, with a certificate recorded either way.'),
           ('When do I need to return a laptop if I leave?',
            'Devices must be received back into the build room within 3 working days of the '
            'leaving date.')]},
 {'slug': 'patching-and-updates',
  'title': 'Patching and Update Management Policy',
  'category': 'infrastructure',
  'doc_type': 'policy',
  'owner': 'Infrastructure Services',
  'system': 'Microsoft Configuration Manager',
  'facts': [('standard server patch window',
             'the third Saturday of each month, 23:30 to 05:00'),
            ('workstation patch deadline for critical severity',
             '72 hours from release to installed'),
            ('workstation patch deadline for important severity',
             '11 calendar days from release to installed'),
            ('workstation patch deadline for moderate and low severity',
             '38 calendar days from release to installed'),
            ('maximum user deferrals of a restart',
             '3 deferrals of 8 hours each, after which the restart is forced'),
            ('emergency patch authority',
             'the Infrastructure Services change lead, who may bypass the normal change board '
             'with a retrospective record within 2 working days')],
  'definitions': [('Patch ring',
                   'a group of devices that receives updates at a defined stage, used to catch '
                   'problems before the whole fleet is updated'),
                  ('Emergency patch',
                   'an out of band update applied outside the normal window because the risk '
                   'of waiting is greater than the risk of deploying'),
                  ('Compliance rate',
                   'the proportion of in-scope devices that have installed a given update by '
                   'its severity deadline')],
  'policy_statements': ['Every managed device must remain within the patch deadline for its '
                        'highest outstanding severity.',
                        'Patches must be released through the pilot ring before any broad '
                        'deployment to the fleet.',
                        'Servers may only be patched inside the agreed window unless an '
                        'emergency patch has been authorised.',
                        'A device that misses its severity deadline is reported to the device '
                        "owner's line manager.",
                        'No update may be permanently excluded from a device without a '
                        'recorded risk acceptance from Information Security.'],
  'procedures': [{'name': 'Running the monthly patch cycle',
                  'steps': ['Review the released updates and assign each a severity against '
                            'the deadline scale.',
                            'Deploy to the pilot ring and hold for observation before going '
                            'wider.',
                            'Check the pilot ring for failed installations and application '
                            'faults.',
                            'Release to the broad rings in sequence once the pilot ring is '
                            'clean.',
                            'Patch the servers inside the third Saturday window.',
                            'Publish the compliance rate per severity at the end of the '
                            'cycle.']},
                 {'name': 'Authorising an emergency patch',
                  'steps': ['Document the vulnerability, the exposure and why waiting for the '
                            'next window is unacceptable.',
                            'Obtain authorisation from the Infrastructure Services change '
                            'lead.',
                            'Deploy to the pilot ring first, even under emergency conditions, '
                            'unless exploitation is already confirmed.',
                            'Deploy to the remaining rings and monitor for failed '
                            'installations.',
                            'File the retrospective change record within 2 working days.']},
                 {'name': 'Chasing a device that has missed its deadline',
                  'steps': ['Confirm the device has checked in and is not simply switched off '
                            'or offline.',
                            'Check whether the user has exhausted the 3 available restart '
                            'deferrals.',
                            'Contact the user with the outstanding update and the deadline '
                            'that was missed.',
                            'Force the restart if the deferral allowance is exhausted and the '
                            'deadline has passed.',
                            "Notify the device owner's line manager if the device remains "
                            'outstanding after contact.']}],
  'troubleshooting': [{'symptom': 'An update repeatedly fails to install on a workstation and '
                                  'rolls back on restart.',
                       'cause': 'The component store is corrupt, so the update cannot be '
                                'staged successfully.',
                       'resolution': 'Run the component store repair, restart the device and '
                                     'retry the update once. If the second attempt also rolls '
                                     'back, rebuild the device rather than retrying further. '
                                     'Escalate to Infrastructure Services if the same failure '
                                     'appears across more than a handful of devices, as that '
                                     'points to a bad package rather than a local fault.',
                       'error_code': 'B-0x80073712'},
                      {'symptom': 'A device shows as non-compliant even though the user says '
                                  'it has restarted.',
                       'cause': 'The management agent has not reported its inventory back '
                                'since the installation completed.',
                       'resolution': 'Trigger a hardware inventory and software update scan '
                                     'cycle on the device and wait for the next check-in. '
                                     'Confirm the device can reach the management point on the '
                                     'network. Escalate to Infrastructure Services if the '
                                     'device still reports stale after a successful scan, '
                                     'since the agent may need reinstalling.',
                       'error_code': 'B-CFGMGR-0x87D00215'},
                      {'symptom': 'Users complain that their machines restarted without '
                                  'warning.',
                       'cause': 'The 3 available deferrals of 8 hours each were used up, so '
                                'the restart was enforced automatically.',
                       'resolution': 'Explain the deferral allowance and the deadline that '
                                     'drove the enforced restart. Advise users to restart at a '
                                     'convenient point rather than deferring to the limit. '
                                     'Escalate to Infrastructure Services only if the restart '
                                     'happened while deferrals were still available, which '
                                     'would indicate a policy misconfiguration.',
                       'error_code': 'B-WUA-0x8024A112'},
                      {'symptom': 'A server was patched outside the agreed window.',
                       'cause': 'An emergency patch was authorised by the change lead and '
                                'deployed before the retrospective record was filed.',
                       'resolution': 'Confirm with the change lead that the emergency patch '
                                     'was authorised and identify the vulnerability involved. '
                                     'Ensure the retrospective change record is filed within '
                                     'the 2 working day limit. Escalate as an unauthorised '
                                     'change if no change lead authorisation can be evidenced.',
                       'error_code': ''}],
  'faqs': [('How quickly do critical patches have to be installed?',
            'Critical severity updates must be installed within 72 hours of release, compared '
            'with 11 calendar days for important and 38 calendar days for moderate and low.'),
           ('Can I put off a restart?',
            'You can defer a restart up to 3 times by 8 hours each, after which the device '
            'restarts automatically.'),
           ('When are servers patched?',
            'Servers are patched in the monthly window on the third Saturday, between 23:30 '
            'and 05:00.'),
           ('Who can approve a patch outside the normal cycle?',
            'The Infrastructure Services change lead can authorise an emergency patch and must '
            'file a retrospective change record within 2 working days.')]},
 {'slug': 'onboarding-new-joiner',
  'title': 'New Joiner IT Onboarding Runbook',
  'category': 'workplace',
  'doc_type': 'runbook',
  'owner': 'Workplace Technology',
  'system': 'ServiceNow HR Service Delivery',
  'facts': [('minimum notice IT requires before a start date',
             '7 working days from the signed HR start record'),
            ('account creation timing',
             'the Entra ID account is created 4 working days before the start date and stays '
             'disabled until 07:00 on day one'),
            ('standard equipment dispatch window',
             'laptop and headset ship 2 working days before the start date to the address on '
             'the HR record'),
            ('induction course completion deadline',
             'the IT Induction module in the learning platform must be completed within 11 '
             'calendar days of the start date'),
            ('day one checklist item count',
             '9 mandatory items, all of which must be ticked in ServiceNow before the record '
             'is closed'),
            ('temporary password validity for a new joiner',
             '36 hours from first issue, after which Workplace Technology must reissue it')],
  'definitions': [('Day one checklist',
                   'the fixed list of 9 items Workplace Technology must complete and tick in '
                   'ServiceNow before a new joiner record can be closed'),
                  ('Pre-boarding window',
                   'the period between the signed HR start record and the start date, during '
                   'which accounts are built but kept disabled'),
                  ('Induction access bundle',
                   'the standard set of group memberships granting a new joiner the intranet, '
                   'learning platform and service portal on day one')],
  'policy_statements': ['No new joiner account may be enabled before 07:00 on the confirmed '
                        'start date.',
                        'Equipment is issued only against a signed HR start record, never on a '
                        'verbal request from a hiring manager.',
                        'A new joiner who has not completed the IT Induction module within 11 '
                        'calendar days has their internet access restricted until it is '
                        'completed.',
                        'The day one checklist must be fully ticked in ServiceNow before the '
                        'onboarding record is closed.',
                        'Line managers are responsible for confirming the delivery address at '
                        'least 7 working days before the start date.'],
  'procedures': [{'name': 'Building a new joiner account',
                  'steps': ['Open the onboarding record in ServiceNow and confirm the HR start '
                            'record is signed.',
                            'Create the Entra ID account as '
                            'firstname.lastname@meridiangroup.example and leave it disabled.',
                            'Add the account to the induction access bundle groups.',
                            'Generate the temporary password and record that it is valid for '
                            '36 hours.',
                            'Set a scheduled enable action for 07:00 on the start date.',
                            'Tick the account creation items on the day one checklist.']},
                 {'name': 'Dispatching new joiner equipment',
                  'steps': ['Confirm the delivery address held on the HR record with the line '
                            'manager.',
                            'Allocate a laptop from the available pool and register the serial '
                            'against the onboarding record.',
                            'Enrol the laptop in device management and confirm it reports as '
                            'compliant.',
                            'Release the shipment so it leaves the warehouse 2 working days '
                            'before the start date.',
                            'Record the courier tracking reference in ServiceNow.']},
                 {'name': 'Completing day one handover',
                  'steps': ['Verify the new joiner has signed in successfully with the '
                            'temporary password.',
                            'Walk the joiner through setting a permanent password and '
                            'registering multi-factor authentication.',
                            'Confirm the induction access bundle resolves by opening the '
                            'intranet and the service portal.',
                            'Assign the IT Induction module and state the 11 calendar day '
                            'deadline.',
                            'Tick the remaining items on the day one checklist and close the '
                            'onboarding record.']}],
  'troubleshooting': [{'symptom': 'The new joiner cannot sign in on the morning of their start '
                                  'date',
                       'cause': 'The scheduled enable action did not run, so the account is '
                                'still disabled',
                       'resolution': 'Open the account in Entra ID and enable it manually, '
                                     'then reissue the temporary password because the original '
                                     '36 hour window has usually lapsed. Confirm the joiner '
                                     'can sign in while still on the call. If the scheduled '
                                     'action has failed for more than one joiner that morning, '
                                     'escalate to Workplace Technology as a possible '
                                     'automation fault.',
                       'error_code': 'C-ONB-4412'},
                      {'symptom': 'The laptop arrives but shows as non-compliant at first '
                                  'sign-in',
                       'cause': 'The device was released from the warehouse before device '
                                'management enrolment finished',
                       'resolution': 'Ask the joiner to connect to a stable network and leave '
                                     'the device powered on for the enrolment to complete, '
                                     'then refresh the compliance state from the management '
                                     'console. Re-run the compliance check after 20 minutes. '
                                     'If it still reports non-compliant, arrange a replacement '
                                     'from the pool rather than troubleshooting on day one.',
                       'error_code': 'C-ONB-0x8007502F'},
                      {'symptom': 'The joiner can sign in but cannot open the learning '
                                  'platform',
                       'cause': 'The induction access bundle groups were not applied because '
                                'the account was created outside the standard ServiceNow task',
                       'resolution': 'Add the account to the induction access bundle groups '
                                     'and ask the joiner to sign out and back in so the new '
                                     'tokens issue. Verify the intranet and service portal '
                                     'also load. Record the manual fix on the onboarding '
                                     'record so the checklist audit stays accurate.',
                       'error_code': 'C-ONB-7730'},
                      {'symptom': 'The hiring manager asks for equipment with only two days '
                                  'notice',
                       'cause': 'The signed HR start record was raised inside the 7 working '
                                'day minimum notice window',
                       'resolution': 'Explain that the dispatch window cannot be met and offer '
                                     'a loan device from the local office pool for the first '
                                     'week. Keep the standard build on the normal schedule. '
                                     'Escalate to the Workplace Technology manager only if no '
                                     'loan device is available in that office.',
                       'error_code': ''}],
  'faqs': [('How much notice does IT need before someone starts?',
            '7 working days from the signed HR start record, which is what allows the account '
            'build and equipment dispatch to land on time.'),
           ('Why is my account not working the day before I start?',
            'Accounts are deliberately left disabled until 07:00 on the confirmed start date, '
            'even though they are built 4 working days earlier.'),
           ('How long is my temporary password valid?',
            '36 hours from when it is first issued, after which Workplace Technology has to '
            'reissue it.'),
           ('When must I finish the IT Induction module?',
            'Within 11 calendar days of your start date, otherwise your internet access is '
            'restricted until it is complete.')]},
 {'slug': 'offboarding-leaver',
  'title': 'Leaver Offboarding Runbook',
  'category': 'workplace',
  'doc_type': 'runbook',
  'owner': 'Identity Operations',
  'system': 'ServiceNow HR Service Delivery',
  'facts': [('access revocation timing for a standard leaver',
             'all interactive access is disabled within 45 minutes of the recorded leaving '
             'time'),
            ('access revocation timing for an immediate dismissal',
             'within 8 minutes of the Human Resources instruction, ahead of any ticket being '
             'raised'),
            ('mailbox retention after departure',
             'converted to a shared mailbox for 13 months, then permanently deleted'),
            ('equipment return deadline',
             '14 calendar days from the leaving date, tracked against the asset record'),
            ('unreturned equipment recharge',
             "the full replacement value is recharged to the leaver's cost centre after 21 "
             'calendar days'),
            ('data handover owner',
             'the line manager, who must confirm handover in ServiceNow within 6 working days '
             'of the leaving date')],
  'definitions': [('Shared mailbox conversion',
                   "the step that turns a departed user's mailbox into a licence-free shared "
                   'mailbox so the line manager can still read historic mail'),
                  ('Immediate dismissal path',
                   'the accelerated offboarding route triggered directly by Human Resources, '
                   'where access is cut before the standard ticket is raised'),
                  ('Data handover confirmation',
                   "the line manager's signed statement in ServiceNow that all business files "
                   'and records held by the leaver have been transferred')],
  'policy_statements': ['Interactive access for a standard leaver is revoked within 45 minutes '
                        'of the recorded leaving time, with no grace period.',
                        "A leaver's mailbox is never deleted on the leaving date; it is "
                        'converted to a shared mailbox and retained for 13 months.',
                        'Line managers must confirm data handover in ServiceNow within 6 '
                        'working days of the leaving date.',
                        'Equipment not returned within 21 calendar days is recharged to the '
                        "leaver's cost centre at full replacement value.",
                        "Personal data held in a leaver's profile is not forwarded to any "
                        'third party, including the leaver, without Information Security '
                        'approval.'],
  'procedures': [{'name': 'Offboarding a standard leaver',
                  'steps': ['Confirm the leaving date and time on the ServiceNow offboarding '
                            'record.',
                            'Disable the Entra ID account and revoke all active sign-in '
                            'sessions and refresh tokens.',
                            'Convert the mailbox to a shared mailbox and grant the line '
                            'manager read access.',
                            'Reclaim all assigned software licences back to the central pool.',
                            'Issue the equipment return pack with the 14 calendar day deadline '
                            'stated.',
                            'Close the record once the line manager has confirmed data '
                            'handover.']},
                 {'name': 'Executing an immediate dismissal',
                  'steps': ['Accept the instruction directly from Human Resources without '
                            'waiting for a ticket.',
                            'Disable the account and revoke all sessions within 8 minutes of '
                            'the instruction.',
                            'Suspend building access and remove the user from all privileged '
                            'groups.',
                            'Preserve the mailbox and files in place and notify Information '
                            'Security.',
                            'Raise the retrospective offboarding record and attach the Human '
                            'Resources instruction.']},
                 {'name': 'Chasing unreturned equipment',
                  'steps': ['Check the asset record on day 14 after the leaving date.',
                            "Send the first reminder to the leaver's personal contact address "
                            'held by Human Resources.',
                            'Notify the line manager and the cost centre owner on day 18.',
                            'Raise the recharge to the cost centre at full replacement value '
                            'on day 21.',
                            'Mark the asset as written off and update the asset register.']}],
  'troubleshooting': [{'symptom': 'A leaver can still open email on a mobile phone hours after '
                                  'their account was disabled',
                       'cause': 'The refresh token on the mobile client was never revoked, so '
                                'the app keeps renewing access',
                       'resolution': 'Revoke all sessions and refresh tokens for the account, '
                                     'then wipe the corporate mail profile from the device '
                                     'through the management console. Confirm the next mail '
                                     'sync fails. Escalate to Information Security if the '
                                     'leaver was an immediate dismissal case.',
                       'error_code': 'C-OFF-5218'},
                      {'symptom': "The line manager reports they cannot read the leaver's "
                                  'mailbox',
                       'cause': 'The mailbox was disabled rather than converted to a shared '
                                'mailbox, so no delegate permission exists',
                       'resolution': 'Reconnect the mailbox, convert it to a shared mailbox '
                                     'and grant the line manager read access. Confirm the '
                                     'manager can open it before closing the ticket. If the '
                                     'mailbox is already past the 13 month retention point, '
                                     'escalate to Information Security rather than attempting '
                                     'a recovery.',
                       'error_code': 'C-OFF-0x8004010F'},
                      {'symptom': 'A shared drive folder is left with no owner after a '
                                  'departure',
                       'cause': 'Data handover was not confirmed within the 6 working day '
                                'window, so ownership was never reassigned',
                       'resolution': 'Assign temporary ownership to the line manager and ask '
                                     'them to complete the data handover confirmation in '
                                     'ServiceNow. Reassign permanent ownership to the named '
                                     'successor once identified. Escalate to the departmental '
                                     'head if the manager does not respond within 2 working '
                                     'days.',
                       'error_code': 'C-OFF-6604'},
                      {'symptom': 'The offboarding record cannot be closed',
                       'cause': 'The data handover confirmation is still outstanding from the '
                                'line manager',
                       'resolution': 'Contact the line manager, explain that closure is '
                                     'blocked and ask them to complete the confirmation in '
                                     'ServiceNow. Keep the record open rather than force '
                                     'closing it. Escalate to Human Resources if the leaving '
                                     'date was more than 6 working days ago.',
                       'error_code': ''}],
  'faqs': [("How quickly is a leaver's access removed?",
            'Within 45 minutes of the recorded leaving time for a standard leaver, or within 8 '
            'minutes of the Human Resources instruction for an immediate dismissal.'),
           ("What happens to a leaver's email?",
            'It is converted to a shared mailbox that the line manager can read, and it is '
            'retained for 13 months before permanent deletion.'),
           ('When does unreturned equipment get charged back?',
            'After 21 calendar days, when the full replacement value is recharged to the '
            "leaver's cost centre."),
           ('Who is responsible for data handover?',
            'The line manager, who must confirm it in ServiceNow within 6 working days of the '
            'leaving date.')]},
 {'slug': 'licence-management',
  'title': 'Software Licence Management Policy',
  'category': 'software',
  'doc_type': 'policy',
  'owner': 'IT Asset Management',
  'system': 'Flexera One',
  'facts': [('inactivity threshold before a licence is reclaimed',
             '52 consecutive days without a sign-in to the licensed application'),
            ('reclaim warning notice',
             'a single email warning sent 9 days before the licence is removed'),
            ('licence pool headroom target',
             'between 3 and 6 per cent spare seats held in each pool'),
            ('annual true-up submission date',
             '15 February each year, covering the preceding calendar year'),
            ('cost centre recharge cycle',
             'recharged monthly on the 4th working day, based on seats assigned on the last '
             'day of the prior month'),
            ('approval route for a premium licence tier',
             'line manager approval plus IT Asset Management review, with a 2 working day '
             'turnaround')],
  'definitions': [('Licence pool',
                   'the central allocation of purchased seats for one product, from which '
                   'individual assignments are drawn and to which reclaimed seats return'),
                  ('True-up',
                   'the annual reconciliation that reports actual deployed seats against the '
                   'contracted entitlement and settles any shortfall'),
                  ('Harvesting',
                   'the automated removal of a licence from a user who has not signed in to '
                   'the application within the inactivity threshold')],
  'policy_statements': ['Software may only be assigned from a managed licence pool recorded in '
                        'Flexera One.',
                        'Licences unused for 52 consecutive days are harvested automatically '
                        'and returned to the pool.',
                        'Each licence pool must retain between 3 and 6 per cent spare seats so '
                        'that new joiners can be provisioned without a purchase.',
                        'Business units are recharged monthly for the seats assigned to their '
                        'cost centre on the last day of the prior month.',
                        'No team may purchase software directly; all purchases are routed '
                        'through IT Asset Management.'],
  'procedures': [{'name': 'Assigning a licence from a pool',
                  'steps': ['Check available headroom for the product in Flexera One.',
                            "Confirm the requester's cost centre on the HR record.",
                            'Assign the seat and record the cost centre against the '
                            'assignment.',
                            'Trigger the application entitlement so the user can sign in.',
                            'Update the recharge schedule so the seat appears in the next '
                            'monthly cycle.']},
                 {'name': 'Running the monthly harvesting cycle',
                  'steps': ['Export the sign-in activity report for every managed product.',
                            'Flag every assignment with no sign-in for 52 consecutive days.',
                            'Send the single warning email 9 days before removal.',
                            'Remove the licence from any user who has still not signed in '
                            'after the warning period.',
                            'Return the reclaimed seats to the pool and confirm headroom is '
                            'back within the 3 to 6 per cent target.']},
                 {'name': 'Preparing the annual true-up',
                  'steps': ['Freeze the deployment position on 31 December and export the '
                            'entitlement report.',
                            'Reconcile deployed seats against the contracted entitlement for '
                            'each product.',
                            'Document any shortfall with the month in which it first occurred.',
                            'Obtain finance sign-off on the shortfall value.',
                            'Submit the completed true-up to the vendor by 15 February.']}],
  'troubleshooting': [{'symptom': 'A user reports the application has stopped opening and asks '
                                  'for their licence back',
                       'cause': 'The licence was harvested after 52 consecutive days without a '
                                'sign-in',
                       'resolution': 'Confirm the harvesting date in Flexera One, reassign a '
                                     'seat from the pool and ask the user to sign in within '
                                     'the next hour so the assignment holds. Explain the '
                                     'inactivity threshold so it does not recur. Escalate to '
                                     'IT Asset Management if no headroom is available in that '
                                     'pool.',
                       'error_code': 'C-LIC-3391'},
                      {'symptom': 'A new joiner cannot be given a seat for a core product',
                       'cause': 'The pool has fallen below the 3 per cent headroom floor, so '
                                'there are no spare seats',
                       'resolution': 'Run an immediate harvesting pass on that product to '
                                     'recover inactive seats, then assign from the recovered '
                                     'seats. If headroom is still below the floor, raise a '
                                     'purchase request to IT Asset Management the same day. Do '
                                     "not borrow a seat from another business unit's "
                                     'allocation.',
                       'error_code': 'C-LIC-0x80070520'},
                      {'symptom': 'A cost centre owner disputes their monthly recharge',
                       'cause': 'The recharge is based on seats assigned on the last day of '
                                'the prior month, so mid-month leavers still appear',
                       'resolution': 'Pull the assignment snapshot for the last day of the '
                                     'prior month and walk the owner through it line by line. '
                                     'Confirm any genuinely wrong assignment and correct it in '
                                     'the following cycle. Escalate to finance only if the '
                                     'correction exceeds a full month of charges.',
                       'error_code': 'C-LIC-8847'},
                      {'symptom': 'The premium tier request has not been actioned after four '
                                  'days',
                       'cause': 'The request is waiting at the line manager approval step and '
                                'has not reached IT Asset Management review',
                       'resolution': 'Check the approval queue, remind the line manager and '
                                     'confirm the 2 working day review turnaround only starts '
                                     'once their approval lands. Reassign the approval if the '
                                     'manager is on leave. Escalate to the departmental head '
                                     'if the request has been pending for more than 5 working '
                                     'days.',
                       'error_code': ''}],
  'faqs': [('Why was my software licence taken away?',
            'Licences are harvested automatically after 52 consecutive days without a sign-in '
            'to that application, and a warning is emailed 9 days before removal.'),
           ('Can my team buy software directly?',
            'No. All purchases go through IT Asset Management so the seats land in a managed '
            'licence pool.'),
           ('When is my department charged for its licences?',
            'Monthly on the 4th working day, based on the seats assigned on the last day of '
            'the prior month.'),
           ('When is the annual true-up submitted?',
            'By 15 February each year, covering the preceding calendar year.')]},
 {'slug': 'collaboration-tools',
  'title': 'Collaboration Tools Runbook',
  'category': 'productivity',
  'doc_type': 'runbook',
  'owner': 'Collaboration Services',
  'system': 'Slack Enterprise Grid',
  'facts': [('message retention period for standard channels',
             '26 months, after which messages are deleted automatically'),
            ('channel creation rights',
             'any employee may create a public channel; private channels require a workspace '
             'owner in Collaboration Services'),
            ('external guest access duration',
             '63 days per invitation, renewable once by the channel owner'),
            ('maximum external guests per channel',
             '18, above which Information Security approval is required'),
            ('dormant channel archive threshold',
             'no messages for 98 days, at which point the channel is archived but not deleted'),
            ('approval route for a new workspace',
             'departmental head approval plus Collaboration Services review, completed within '
             '3 working days')],
  'definitions': [('Enterprise Grid workspace',
                   "a separate Slack workspace inside the organisation's single Grid "
                   "organisation, used to keep one business unit's channels apart from "
                   "another's"),
                  ('External guest',
                   'a named person outside meridiangroup.example invited into specific '
                   'channels only, with no access to the wider workspace or to search'),
                  ('Dormant channel',
                   'a channel with no messages for 98 days, which is archived automatically '
                   'but kept readable')],
  'policy_statements': ['Standard channel messages are retained for 26 months and then deleted '
                        'automatically.',
                        'Private channels may only be created by a workspace owner in '
                        'Collaboration Services.',
                        'External guest invitations last 63 days and may be renewed once by '
                        'the channel owner.',
                        'Confidential information must not be shared in any channel that '
                        'contains an external guest.',
                        'Channels dormant for 98 days are archived automatically and must be '
                        'unarchived through the service portal if needed again.'],
  'procedures': [{'name': 'Creating a private channel',
                  'steps': ['Raise a request in the service portal under Collaboration, '
                            'choosing Private Channel.',
                            'State the business purpose and the intended member list.',
                            'A Collaboration Services workspace owner creates the channel and '
                            'sets the topic.',
                            'Add the requester as channel owner and the named members.',
                            'Confirm the retention setting matches the standard 26 month '
                            'period.']},
                 {'name': 'Inviting an external guest',
                  'steps': ["Confirm the guest's organisation is covered by a signed "
                            'non-disclosure agreement.',
                            'Check the channel currently holds fewer than 18 external guests.',
                            'Send the guest invitation from the channel, which grants 63 days '
                            'of access.',
                            'Record the invitation and its expiry date in the channel topic.',
                            'Renew once if still needed, or let the access lapse.']},
                 {'name': 'Recovering an archived channel',
                  'steps': ['Search the archive list in the service portal for the channel '
                            'name.',
                            'Confirm the requester was a member before archiving.',
                            'Unarchive the channel and restore the original member list.',
                            'Post a message so the 98 day dormancy clock restarts.',
                            'Notify the requester that history before the 26 month retention '
                            'limit is not recoverable.']}],
  'troubleshooting': [{'symptom': 'A user cannot find messages from three years ago',
                       'cause': 'Standard channel retention is 26 months, so the messages have '
                                'already been deleted',
                       'resolution': 'Explain that the retention period has passed and that '
                                     'deleted messages are not recoverable from the product. '
                                     'Check whether the content exists in an approved document '
                                     'store instead. Escalate to Information Security only if '
                                     'the request is part of a legal hold, which has its own '
                                     'process.',
                       'error_code': 'C-SLK-2270'},
                      {'symptom': 'An external guest reports their invitation link no longer '
                                  'works',
                       'cause': 'The 63 day guest access period has lapsed',
                       'resolution': 'Ask the channel owner to confirm the engagement is still '
                                     'active, then issue the single permitted renewal. Record '
                                     'the new expiry date in the channel topic. If the renewal '
                                     'has already been used, escalate to Collaboration '
                                     'Services for a review of the engagement rather than '
                                     'reinviting.',
                       'error_code': 'C-SLK-0x8004A119'},
                      {'symptom': 'A channel owner cannot add a nineteenth external guest',
                       'cause': 'The channel has reached the limit of 18 external guests',
                       'resolution': 'Remove any guests whose engagement has ended, then retry '
                                     'the invitation. If all 18 are genuinely active, raise an '
                                     'Information Security approval request before going above '
                                     'the limit. Do not create a second parallel channel to '
                                     'work around the cap.',
                       'error_code': 'C-SLK-9148'},
                      {'symptom': 'A project channel has disappeared from the sidebar',
                       'cause': 'The channel was archived automatically after 98 days without '
                                'a message',
                       'resolution': 'Search the archive list, unarchive the channel and '
                                     'restore the member list. Post a message so the dormancy '
                                     'clock restarts. No escalation is needed unless the '
                                     'archive list does not contain the channel.',
                       'error_code': ''}],
  'faqs': [('How long are Slack messages kept?',
            'Standard channel messages are retained for 26 months and then deleted '
            'automatically.'),
           ('Can I create a private channel myself?',
            'No. Public channels are open to anyone, but private channels are created by a '
            'workspace owner in Collaboration Services.'),
           ('How long does an external guest keep access?',
            '63 days per invitation, which the channel owner can renew once.'),
           ('Why did my old project channel vanish?',
            'It was archived automatically after 98 days with no messages, and it can be '
            'unarchived through the service portal.')]},
 {'slug': 'video-conferencing',
  'title': 'Video Conferencing Runbook',
  'category': 'productivity',
  'doc_type': 'runbook',
  'owner': 'Collaboration Services',
  'system': 'Zoom Workplace',
  'facts': [('standard meeting room capacity',
             '11 seats per medium room, with a hard booking limit of 14 people'),
            ('cloud recording retention',
             '17 months in cloud storage, then automatic deletion'),
            ('recording consent requirement',
             'a spoken announcement plus the on-screen recording indicator, with any objection '
             'ending the recording'),
            ('dial-in number coverage',
             'toll numbers in 22 countries, with toll-free dial-in in 6 of them'),
            ('large webinar licence threshold',
             'any event expected to exceed 290 attendees must use a webinar licence, not a '
             'standard meeting'),
            ('webinar licence lead time',
             'booked at least 8 working days before the event date')],
  'definitions': [('Meeting room resource',
                   'a bookable physical room with a fixed video endpoint, held as a resource '
                   'account in the calendar system'),
                  ('Webinar licence',
                   'a separate Zoom entitlement required for events above 290 attendees, where '
                   'participants join in view-only mode by default'),
                  ('Dial-in bridge',
                   'the telephone access path into a meeting, used when a participant has no '
                   'usable internet connection')],
  'policy_statements': ['No meeting may be recorded without a spoken announcement and the '
                        'on-screen recording indicator visible to all participants.',
                        'If any participant objects to being recorded, the recording must be '
                        'stopped immediately.',
                        'Cloud recordings are retained for 17 months and then deleted '
                        'automatically.',
                        'Events expected to exceed 290 attendees must be run under a webinar '
                        'licence booked at least 8 working days in advance.',
                        'Meeting room resources must not be booked for more people than the '
                        "room's hard booking limit."],
  'procedures': [{'name': 'Recording a meeting lawfully',
                  'steps': ['Announce at the start that the session will be recorded and why.',
                            'Start the recording and confirm the on-screen indicator is '
                            'visible to all participants.',
                            'Stop the recording immediately if any participant objects.',
                            'Share the recording only with the stated audience.',
                            'Note that the recording is deleted automatically after 17 '
                            'months.']},
                 {'name': 'Booking a large webinar',
                  'steps': ['Confirm the expected attendance exceeds the 290 attendee '
                            'threshold.',
                            'Raise a webinar licence request at least 8 working days before '
                            'the event date.',
                            'Collaboration Services assigns the webinar licence to the host '
                            'account.',
                            'Run a technical rehearsal with the host and any panellists.',
                            'Release the licence back to the pool after the event.']},
                 {'name': 'Setting up a room endpoint for a meeting',
                  'steps': ['Check the room resource is free and the attendee count is within '
                            'the hard booking limit of 14.',
                            'Add the room resource to the calendar invitation so the endpoint '
                            'receives the join details.',
                            'Confirm the endpoint shows the meeting on its panel 10 minutes '
                            'before the start.',
                            'Test camera, microphone and screen share from the room '
                            'controller.',
                            'Add the dial-in details to the invitation for anyone joining by '
                            'telephone.']}],
  'troubleshooting': [{'symptom': 'The room endpoint does not show the meeting on its panel',
                       'cause': 'The room resource was not added to the calendar invitation, '
                                'so the endpoint never received the join details',
                       'resolution': 'Add the room resource to the invitation and send the '
                                     'update, then wait for the panel to refresh. If it still '
                                     'does not appear, join manually by entering the meeting '
                                     'identifier on the controller. Escalate to Collaboration '
                                     'Services if the room resource repeatedly fails to accept '
                                     'invitations.',
                       'error_code': 'C-VID-1163'},
                      {'symptom': 'A participant cannot hear anything after joining by '
                                  'telephone',
                       'cause': 'The participant dialled a toll number for a country outside '
                                'the 22 country coverage list and reached a dead bridge',
                       'resolution': 'Give the participant a dial-in number from the supported '
                                     'country list, or ask them to rejoin over the internet. '
                                     'Confirm audio before continuing the meeting. Escalate to '
                                     "Collaboration Services if a listed country's number is "
                                     'genuinely unreachable.',
                       'error_code': 'C-VID-0x8007273D'},
                      {'symptom': 'The host cannot find a recording from last year',
                       'cause': 'The recording passed the 17 month cloud retention period and '
                                'was deleted automatically',
                       'resolution': 'Confirm the meeting date against the retention period '
                                     'and explain that the recording is not recoverable. Check '
                                     'whether the host saved a local copy or a transcript '
                                     'elsewhere. Escalate to Information Security only if the '
                                     'recording is subject to a legal hold.',
                       'error_code': 'C-VID-4075'},
                      {'symptom': 'Attendees are blocked from joining a large all-hands '
                                  'session',
                       'cause': 'The event was scheduled as a standard meeting even though '
                                'attendance exceeds the 290 attendee threshold',
                       'resolution': 'Move the event to a webinar licence immediately and '
                                     'reissue the join link to attendees. Note that the 8 '
                                     'working day lead time has been missed, so a rehearsal is '
                                     'not possible. Escalate to Collaboration Services to '
                                     'source a spare webinar licence at short notice.',
                       'error_code': ''}],
  'faqs': [('Do I have to tell people I am recording?',
            'Yes. You must announce it out loud and keep the on-screen recording indicator '
            'visible, and you must stop if anyone objects.'),
           ('How long do cloud recordings last?',
            '17 months, after which they are deleted automatically.'),
           ('When do I need a webinar licence instead of a meeting?',
            'Whenever you expect more than 290 attendees, and the licence must be booked at '
            'least 8 working days ahead.'),
           ('Can people join by telephone from anywhere?',
            'Toll dial-in is available in 22 countries, 6 of which also have toll-free '
            'numbers.')]},
 {'slug': 'identity-and-sso',
  'title': 'Identity and Single Sign-On Runbook',
  'category': 'access',
  'doc_type': 'runbook',
  'owner': 'Identity Operations',
  'system': 'Okta Workforce Identity',
  'facts': [('standard SSO onboarding duration for a new application',
             '19 working days from an approved request to production cutover'),
            ('supported federation protocols',
             'SAML 2.0 and OpenID Connect only; header-based and password-vaulting '
             'integrations are not accepted'),
            ('SAML signing certificate lifetime',
             '33 months, with a renewal reminder issued 70 days before expiry'),
            ('group mapping limit per application',
             '27 directory groups per application assignment'),
            ('assertion clock skew tolerance',
             '110 seconds between the identity provider and the application'),
            ('approval route for a new SSO integration',
             'application owner request plus Information Security architecture review, with '
             'Identity Operations as the final approver')],
  'definitions': [('Service provider',
                   'the application that relies on the identity provider to authenticate '
                   'users, and that consumes the SAML assertion or OIDC token'),
                  ('Group mapping',
                   'the configuration that translates a directory group membership into an '
                   'application role or entitlement at sign-in'),
                  ('Clock skew tolerance',
                   'the maximum permitted time difference between the identity provider and '
                   'the application before an assertion is rejected as invalid')],
  'policy_statements': ['All new business applications must authenticate through Okta using '
                        'SAML 2.0 or OpenID Connect.',
                        'Password-vaulting and header-based integrations are not permitted for '
                        'new applications.',
                        'Application access is granted only through directory group mapping, '
                        'never by naming individual users in the application.',
                        'Each application assignment may map at most 27 directory groups.',
                        'SAML signing certificates must be renewed before expiry, with a '
                        'reminder issued 70 days ahead.'],
  'procedures': [{'name': 'Onboarding an application to SSO',
                  'steps': ['Collect the metadata or the entity identifier and assertion '
                            'consumer service URL from the application owner.',
                            'Submit the integration request for Information Security '
                            'architecture review.',
                            'Create the application in Okta using SAML 2.0 or OpenID Connect '
                            'and configure the attribute statements.',
                            'Create the directory groups and map them to application roles, '
                            'staying within the 27 group limit.',
                            'Test sign-in with a pilot user such as '
                            'firstname.lastname@meridiangroup.example.',
                            'Cut over to production and close the request within the 19 '
                            'working day window.']},
                 {'name': 'Rotating a SAML signing certificate',
                  'steps': ['Act on the renewal reminder issued 70 days before expiry.',
                            'Generate the new signing certificate in Okta and keep the '
                            'existing one active.',
                            'Send the updated metadata to the application owner for upload.',
                            'Confirm a test sign-in succeeds against the new certificate.',
                            'Retire the previous certificate and record the new 33 month '
                            'expiry date.']},
                 {'name': 'Adding a group mapping to a live application',
                  'steps': ['Confirm the application assignment currently holds fewer than 27 '
                            'mapped groups.',
                            'Create or identify the directory group that represents the '
                            'required role.',
                            'Map the group to the application role and save the assignment.',
                            'Ask a member of that group to sign in and confirm the correct '
                            'role is applied.',
                            "Record the mapping on the application's access record for "
                            'recertification.']}],
  'troubleshooting': [{'symptom': 'Sign-in fails with an invalid assertion error at the '
                                  'application',
                       'cause': 'The clocks on the identity provider and the application '
                                'differ by more than the 110 second skew tolerance',
                       'resolution': 'Check the time source on the application host and '
                                     'correct it to a reliable network time service, then '
                                     'retry the sign-in. Compare the assertion timestamps in '
                                     'the Okta system log against the application log. '
                                     'Escalate to the application owner if their host cannot '
                                     'hold accurate time.',
                       'error_code': 'C-SAML-7781'},
                      {'symptom': 'Users authenticate successfully but land in the application '
                                  'with no permissions',
                       'cause': 'The directory group is assigned to the application but not '
                                'mapped to an application role',
                       'resolution': 'Open the application assignment in Okta, map the group '
                                     'to the correct role and save it. Ask the user to sign '
                                     'out and back in so a fresh assertion issues. Escalate to '
                                     'the application owner if the role names in the '
                                     'application have changed since the integration was '
                                     'built.',
                       'error_code': 'C-OIDC-3025'},
                      {'symptom': 'All users for one application are suddenly unable to sign '
                                  'in',
                       'cause': 'The SAML signing certificate expired after its 33 month '
                                'lifetime and was not rotated',
                       'resolution': 'Generate a replacement signing certificate in Okta and '
                                     'send the updated metadata to the application owner for '
                                     'immediate upload. Confirm a test sign-in once they have '
                                     'applied it. Escalate to Identity Operations management '
                                     'if the application owner cannot apply the metadata the '
                                     'same day.',
                       'error_code': 'C-SAML-0x8009310B'},
                      {'symptom': 'An application owner asks for a password-vaulting '
                                  'integration instead of SAML',
                       'cause': "The vendor's product does not support a standard federation "
                                'protocol',
                       'resolution': 'Explain that only SAML 2.0 and OpenID Connect are '
                                     'accepted for new applications and ask the vendor for a '
                                     'federation roadmap date. Record the gap on the '
                                     "application's architecture review. Escalate to "
                                     'Information Security for a risk decision if there is no '
                                     'alternative product.',
                       'error_code': ''}],
  'faqs': [('How long does it take to add an application to SSO?',
            '19 working days from an approved request to production cutover.'),
           ('Which SSO protocols are supported?',
            'SAML 2.0 and OpenID Connect only. Password-vaulting and header-based integrations '
            'are not accepted for new applications.'),
           ('How often do SAML certificates need replacing?',
            'Every 33 months, and a renewal reminder is issued 70 days before expiry.'),
           ('Can I be given access to an application directly?',
            'No. Access is granted only through directory group mapping, and an application '
            'may map at most 27 groups.')]},
 {'slug': 'privileged-access',
  'title': 'Privileged Access Management Policy',
  'category': 'security',
  'doc_type': 'policy',
  'owner': 'Information Security',
  'system': 'CyberArk Privilege Cloud',
  'facts': [('maximum just-in-time elevation duration',
             '95 minutes per activation, after which the role expires automatically'),
            ('approval chain for production elevation',
             'the system owner approves first, then the Information Security duty approver, '
             'with no self-approval permitted'),
            ('session recording retention', '4 years for all recorded privileged sessions'),
            ('recertification frequency for privileged roles',
             'every 61 days, with removal if the reviewer does not respond'),
            ('break-glass account count',
             '2 accounts per production platform, with credentials split between Information '
             'Security and Network Operations'),
            ('maximum standing privileged accounts per person',
             '1, which may only be a named break-glass holder role')],
  'definitions': [('Just-in-time elevation',
                   'the temporary activation of a privileged role for a single task, which '
                   'expires automatically after 95 minutes'),
                  ('Standing privilege',
                   'a privileged role held permanently rather than activated on demand, which '
                   'is permitted only for a named break-glass holder'),
                  ('Duty approver',
                   'the rostered Information Security approver who provides the second '
                   'approval for production elevation requests')],
  'policy_statements': ['Privileged access to production systems is granted only through '
                        'just-in-time elevation, never as standing privilege.',
                        'Every production elevation requires approval from the system owner '
                        'and from the Information Security duty approver, and self-approval is '
                        'never permitted.',
                        'All privileged sessions are recorded, and the recordings are retained '
                        'for 4 years.',
                        'Privileged roles are recertified every 61 days and are removed '
                        'automatically if the reviewer does not respond.',
                        'Break-glass credentials are split between Information Security and '
                        'Network Operations so that no single person can use them alone.'],
  'procedures': [{'name': 'Requesting just-in-time elevation',
                  'steps': ['Raise the elevation request in CyberArk Privilege Cloud, naming '
                            'the target system and the task.',
                            'Wait for the system owner approval, then for the Information '
                            'Security duty approver.',
                            'Activate the role and begin work, noting the 95 minute expiry.',
                            'Complete the task and end the session before the role expires.',
                            'Confirm the session recording has been captured against the '
                            'request.']},
                 {'name': 'Using a break-glass account',
                  'steps': ['Declare a major incident so the break-glass use is on record.',
                            'Ask the Information Security holder and the Network Operations '
                            'holder to each supply their credential half.',
                            'Sign in and confirm session recording has started before taking '
                            'any action.',
                            'Carry out only the actions needed to restore service.',
                            'Rotate the break-glass credentials immediately after the session '
                            'and file the usage report.']},
                 {'name': 'Running the privileged role recertification',
                  'steps': ['Generate the privileged role report at the start of each 61 day '
                            'cycle.',
                            'Send each reviewer the list of privileged roles held by their '
                            'team.',
                            'Record every confirmed role against the access register.',
                            'Remove any role the reviewer has not confirmed by the cycle '
                            'close.',
                            'Report the removal count to the Information Security governance '
                            'forum.']}],
  'troubleshooting': [{'symptom': 'An engineer loses administrative rights part way through a '
                                  'change',
                       'cause': 'The just-in-time elevation reached its 95 minute expiry',
                       'resolution': 'Ask the engineer to raise a fresh elevation request and '
                                     'obtain both approvals again, then resume the work. '
                                     'Advise them to break long changes into stages that fit '
                                     'inside the activation window. Escalate to the '
                                     'Information Security duty approver for an out-of-hours '
                                     'approval if the change is mid-flight on a production '
                                     'system.',
                       'error_code': 'C-PAM-6629'},
                      {'symptom': 'An elevation request sits unapproved for hours',
                       'cause': 'The requester is also the system owner, and self-approval is '
                                'blocked by policy',
                       'resolution': 'Reroute the first approval to a deputy system owner '
                                     'recorded on the system register, then let the '
                                     'Information Security duty approver complete the chain. '
                                     'Do not override the self-approval block. Escalate to '
                                     'Information Security if no deputy is recorded for that '
                                     'system.',
                       'error_code': 'C-PAM-0x80070542'},
                      {'symptom': 'A privileged session shows no recording against the request',
                       'cause': 'The engineer connected directly to the target system instead '
                                'of through the privileged session broker',
                       'resolution': 'Terminate the direct connection, have the engineer '
                                     'reconnect through CyberArk Privilege Cloud and confirm '
                                     'the recording indicator is active. Report the unrecorded '
                                     'session to Information Security the same day. Treat any '
                                     'repeat as a policy breach and escalate to the governance '
                                     'forum.',
                       'error_code': 'C-PAM-5183'},
                      {'symptom': 'A team reports their privileged roles disappeared overnight',
                       'cause': 'The reviewer did not respond before the 61 day '
                                'recertification cycle closed, so the roles were removed '
                                'automatically',
                       'resolution': 'Ask the team to raise fresh just-in-time elevation '
                                     'requests for any immediate work. Have the reviewer '
                                     'reconfirm the roles so they are restored at the next '
                                     'cycle. Escalate to the departmental head if the reviewer '
                                     'has missed two consecutive cycles.',
                       'error_code': ''}],
  'faqs': [('How long does a privileged elevation last?',
            '95 minutes per activation, after which the role expires automatically and a fresh '
            'request is needed.'),
           ('Can I approve my own elevation request?',
            'No. The system owner approves first and the Information Security duty approver '
            'second, and self-approval is never permitted.'),
           ('How long are privileged session recordings kept?',
            '4 years for all recorded privileged sessions.'),
           ('How often are privileged roles reviewed?',
            'Every 61 days, and any role the reviewer does not confirm is removed '
            'automatically.')]},
 {'slug': 'account-provisioning',
  'title': 'User Account Provisioning Runbook',
  'category': 'access',
  'doc_type': 'runbook',
  'owner': 'Identity and Access Management',
  'system': 'Entra ID',
  'facts': [('account creation target',
             '4 business hours from receipt of an approved joiner request'),
            ('standard account naming format',
             'firstname.lastname@meridiangroup.example, with a numeric suffix such as .2 only '
             'when the name already exists'),
            ('access recertification cycle',
             'every 120 days for every directory group that grants application access'),
            ('dormant account disable threshold',
             '45 consecutive days without an interactive sign-in'),
            ('maximum direct group memberships per user',
             '60 groups, above which access must be granted through a role package'),
            ('leaver account deletion point',
             '35 days after the account is disabled, once the mailbox export is confirmed')],
  'definitions': [('Role package',
                   'a bundle of directory groups mapped to one job role, assigned as a single '
                   'unit so that joiners receive a consistent baseline'),
                  ('Access recertification',
                   'a scheduled review in which a named group owner confirms, line by line, '
                   'that each member still needs the access'),
                  ('Dormant account',
                   'an enabled account that has recorded no interactive sign-in for 45 '
                   'consecutive days and is therefore a standing security risk')],
  'policy_statements': ['No account is created without an approved joiner request that names '
                        'the line manager and the start date.',
                        'Shared or generic user accounts are prohibited; every account maps to '
                        'one identifiable person.',
                        'Group ownership must be held by a named individual, never by a '
                        'distribution list or a team mailbox.',
                        'Access granted outside a role package must carry a written business '
                        'justification stored against the request.',
                        'A group owner who fails to complete recertification within the 120 '
                        'day cycle has the group placed in read-only mode until the review is '
                        'closed.'],
  'procedures': [{'name': 'Provisioning a new joiner account',
                  'steps': ['Confirm the joiner record in the HR feed shows an approved start '
                            'date and a populated job role.',
                            'Create the account in Entra ID using the firstname.lastname '
                            'naming format.',
                            'Assign the role package that matches the job role rather than '
                            'individual groups.',
                            'Issue the temporary password through the line manager, never '
                            'directly to the joiner.',
                            'Confirm the user completes multi-factor authentication '
                            'registration before the first working day.',
                            'Close the request with the account name and the role package '
                            'recorded in the work notes.']},
                 {'name': 'Adding a user to a directory group',
                  'steps': ['Check whether the required access is already covered by an '
                            'existing role package.',
                            'Raise the request in the service portal and route it to the named '
                            'group owner for approval.',
                            'Verify the user is below the 60 direct membership limit before '
                            'adding the group.',
                            'Add the membership and record the business justification against '
                            'the request.',
                            'Flag the membership for review at the next 120 day '
                            'recertification cycle.']},
                 {'name': 'Processing a leaver',
                  'steps': ['Disable the account in Entra ID on the confirmed last working '
                            'day.',
                            'Revoke all active sessions and refresh tokens so existing logins '
                            'drop immediately.',
                            'Remove the user from every directory group and transfer any group '
                            'ownership to the line manager.',
                            'Place the mailbox on hold and export it to the archive store.',
                            'Delete the account 35 days after disable, once the mailbox export '
                            'is confirmed.']}],
  'troubleshooting': [{'symptom': 'A newly created account cannot sign in and the portal '
                                  'returns D-ENT-4412',
                       'cause': 'The licence assignment has not yet replicated, so the account '
                                'exists in the directory but has no service plan attached',
                       'resolution': 'Open the account in the admin centre and confirm a '
                                     'licence is assigned, then force a licence reprocess and '
                                     'wait 15 minutes. Ask the user to retry in a private '
                                     'browser window. If the error persists beyond one hour, '
                                     'escalate to Identity and Access Management with the '
                                     'account name and the request number.',
                       'error_code': 'D-ENT-4412'},
                      {'symptom': 'Adding a user to a group fails with D-ENT-7190',
                       'cause': 'The user has reached the 60 direct group membership limit',
                       'resolution': "Review the user's memberships and remove any that are "
                                     'already covered by their role package. If all 60 are '
                                     'genuinely needed, migrate the user onto a role package '
                                     'and raise a design request to Identity and Access '
                                     'Management rather than forcing more direct grants.',
                       'error_code': 'D-ENT-7190'},
                      {'symptom': 'A returning employee finds their account disabled',
                       'cause': 'The account crossed the 45 day dormant threshold while the '
                                'employee was on extended leave',
                       'resolution': 'Confirm the employment record is still active in the HR '
                                     'feed, then re-enable the account and reset the password '
                                     'through the line manager. Ask the user to re-register '
                                     'multi-factor authentication if more than one method has '
                                     'lapsed. Record the re-enablement against the original '
                                     'joiner request.',
                       'error_code': ''},
                      {'symptom': 'A group owner reports they cannot add members and see '
                                  'D-ENT-2065',
                       'cause': 'The group is in read-only mode because its recertification '
                                'was not completed inside the 120 day cycle',
                       'resolution': 'Tell the owner to complete the outstanding '
                                     'recertification in the access review portal. Read-only '
                                     'mode lifts automatically within one hour of the review '
                                     'closing. If the owner has left the business, escalate to '
                                     'Identity and Access Management to reassign ownership.',
                       'error_code': 'D-ENT-2065'}],
  'faqs': [('How quickly will a new starter get their account?',
            'Within 4 business hours of an approved joiner request reaching Identity and '
            'Access Management.'),
           ('What will my username be?',
            'firstname.lastname@meridiangroup.example, with a numeric suffix only if that name '
            'is already taken.'),
           ('My account was disabled while I was on leave, why?',
            'Accounts with no interactive sign-in for 45 consecutive days are disabled '
            'automatically; the service desk can re-enable it once your employment record is '
            'confirmed.'),
           ('How often do group owners have to review access?',
            'Every 120 days, and the group becomes read-only until an overdue review is '
            'closed.')]},
 {'slug': 'hardware-repair-and-warranty',
  'title': 'Hardware Repair and Warranty Runbook',
  'category': 'hardware',
  'doc_type': 'runbook',
  'owner': 'Desktop Support',
  'system': 'Dell ProSupport Plus',
  'facts': [('standard warranty term on corporate laptops',
             '36 months from the delivery date, with next business day onsite response'),
            ('fault triage target',
             'a documented diagnostic result within 6 business hours of the device arriving at '
             'a support bench'),
            ('loan device pool size', '18 devices held at each of the three main offices'),
            ('maximum loan device period',
             '10 working days, after which the loan must be re-approved by a line manager'),
            ('accidental damage excess',
             'GBP 150 per claim, with a limit of 2 claims per user in any rolling 12 months'),
            ('battery replacement threshold',
             'a reported battery health figure below 72 per cent of design capacity')],
  'definitions': [('Accidental damage',
                   'physical harm to a device from a single unexpected event such as a drop or '
                   'a liquid spill, as distinct from wear and tear or deliberate misuse'),
                  ('Dead on arrival',
                   'a newly delivered device that fails to power on or complete its first '
                   'boot, which is replaced by the supplier rather than repaired'),
                  ('Loan device',
                   "a pre-imaged spare laptop issued for a fixed period while a user's own "
                   'device is under repair, holding no local data at hand-back')],
  'policy_statements': ['Devices under warranty must be repaired through the supplier channel; '
                        'third party repair voids the warranty and is prohibited.',
                        'No device leaves the business for repair until its disk has been '
                        'confirmed as encrypted and a data wipe record has been raised where '
                        'the disk is to be replaced.',
                        'Accidental damage claims require a written incident description from '
                        'the user before a repair is booked.',
                        'Loan devices are issued with a standard corporate image only; users '
                        'may not install unapproved software on them.',
                        'A device that has had 3 accepted hardware faults inside its warranty '
                        'term is replaced rather than repaired again.'],
  'procedures': [{'name': 'Triaging a reported hardware fault',
                  'steps': ['Record the service tag, the model and the exact symptom in the '
                            'ticket.',
                            'Run the supplier onboard diagnostics and capture the validation '
                            'code.',
                            'Confirm whether the fault reproduces with external peripherals '
                            'removed.',
                            'Check the warranty status and expiry date against the service '
                            'tag.',
                            'Record the diagnostic result in the ticket within 6 business '
                            'hours of bench arrival.']},
                 {'name': 'Raising a warranty claim',
                  'steps': ['Open a supplier case quoting the service tag and the diagnostic '
                            'validation code.',
                            'Attach the fault description and any photographs of physical '
                            'damage.',
                            'Select next business day onsite where the user is at a main '
                            'office, or depot repair otherwise.',
                            'Issue a loan device to the user and record its asset number '
                            'against the ticket.',
                            'Confirm the repair outcome with the engineer and close the '
                            'supplier case.']},
                 {'name': 'Handling an accidental damage claim',
                  'steps': ['Collect a written incident description from the user describing '
                            'how the damage occurred.',
                            'Confirm the user has not already made 2 claims in the rolling 12 '
                            'month period.',
                            "Raise the GBP 150 excess as a cost recharge against the user's "
                            'cost centre.',
                            'Book the repair with the supplier under the accidental damage '
                            'cover.',
                            'Record the claim against the asset so the claim count stays '
                            'accurate.']}],
  'troubleshooting': [{'symptom': 'The supplier portal rejects a claim with D-HW-5531',
                       'cause': 'The service tag is outside its 36 month warranty term',
                       'resolution': 'Confirm the delivery date on the asset record rather '
                                     'than the purchase order date, as the term runs from '
                                     'delivery. If the device is genuinely out of warranty, '
                                     'quote the repair as a chargeable job and route the cost '
                                     "approval to the user's line manager. Escalate to Desktop "
                                     'Support management if the asset record and the supplier '
                                     'record disagree.',
                       'error_code': 'D-HW-5531'},
                      {'symptom': 'A user reports the laptop runs for less than an hour on '
                                  'battery',
                       'cause': 'The battery has degraded below the 72 per cent design '
                                'capacity threshold',
                       'resolution': 'Run the onboard battery report and record the health '
                                     'percentage in the ticket. If it is below 72 per cent, '
                                     'raise a warranty claim for a battery replacement. If it '
                                     'is above 72 per cent, check the power profile and '
                                     'running processes before booking any hardware work.',
                       'error_code': ''},
                      {'symptom': 'A loan device cannot be issued and the stock system shows '
                                  'D-HW-8104',
                       'cause': 'The site loan pool of 18 devices is fully allocated',
                       'resolution': 'Check for loans that have passed the 10 working day '
                                     'limit and chase those users for return. Offer the user a '
                                     'loan from the next nearest office with courier delivery. '
                                     'If the pool is exhausted for more than 2 working days, '
                                     'escalate to Desktop Support management to release buffer '
                                     'stock.',
                       'error_code': 'D-HW-8104'},
                      {'symptom': 'A replacement disk is fitted but the device will not boot '
                                  'and shows D-HW-3377',
                       'cause': 'The recovery image was not re-applied after the disk swap, so '
                                'there is no bootable partition',
                       'resolution': 'Boot the device from the network recovery image and '
                                     're-apply the standard corporate build. Confirm disk '
                                     'encryption completes before returning the device to the '
                                     'user. If the device fails to pick up the recovery image '
                                     'after two attempts, raise it to the build team with the '
                                     'service tag.',
                       'error_code': 'D-HW-3377'}],
  'faqs': [('How long is my laptop covered?',
            '36 months from the delivery date, with next business day onsite response while it '
            'is in warranty.'),
           ('Will I be charged if I drop my laptop?',
            'An excess of GBP 150 per claim is recharged to your cost centre, and only 2 '
            'claims are allowed in any rolling 12 months.'),
           ('How long can I keep a loan laptop?',
            'Up to 10 working days, after which your line manager must re-approve the loan.'),
           ('When does a battery qualify for replacement?',
            'When the onboard battery report shows health below 72 per cent of design '
            'capacity.')]},
 {'slug': 'service-desk-slas',
  'title': 'Service Desk Service Level Policy',
  'category': 'service-management',
  'doc_type': 'policy',
  'owner': 'Service Management Office',
  'system': 'ServiceNow',
  'facts': [('priority matrix basis',
             'impact and urgency combined on a three by three grid, producing priorities P1 to '
             'P4'),
            ('P1 targets',
             '15 minute response and 3 hour resolution, measured around the clock'),
            ('P2 targets', '30 minute response and 9 business hour resolution'),
            ('P3 and P4 targets',
             'P3 is 2 business hour response and 3 business day resolution; P4 is 8 business '
             'hour response and 12 business day resolution'),
            ('escalation trigger points',
             'the shift lead at 50 per cent of the resolution clock and the duty manager at 80 '
             'per cent'),
            ('monthly SLA attainment target',
             '94 per cent of tickets resolved inside target, reviewed at the monthly service '
             'review')],
  'definitions': [('Response time',
                   'the interval between a ticket being created and a named agent recording '
                   'the first substantive update to the user, not an automated '
                   'acknowledgement'),
                  ('Business hours',
                   '08:00 to 18:00 local time on working days, excluding public holidays, used '
                   'for all P2 to P4 clocks'),
                  ('SLA breach',
                   'a ticket whose response or resolution clock passes its target without the '
                   'clock having been validly paused')],
  'policy_statements': ['Priority is set from the impact and urgency grid and may not be '
                        'raised simply because a user requests it.',
                        'The resolution clock pauses only while a ticket is in Pending '
                        'Customer or Pending Third Party, and the pause reason must be '
                        'recorded.',
                        'Every P1 requires a named incident manager and a bridge call opened '
                        'within the 15 minute response target.',
                        'A breached ticket must carry a breach reason code before it can be '
                        'closed.',
                        'Breach reviews are completed within 5 business days of the breach and '
                        'their actions tracked to closure.'],
  'procedures': [{'name': 'Setting the priority of a new ticket',
                  'steps': ['Establish how many users and which services are affected to fix '
                            'the impact rating.',
                            'Establish whether a workaround exists to fix the urgency rating.',
                            'Read the resulting priority from the three by three impact and '
                            'urgency grid.',
                            'Record the impact and urgency reasoning in the ticket work notes.',
                            'Confirm the applied SLA target matches the priority before '
                            'saving.']},
                 {'name': 'Escalating a ticket approaching breach',
                  'steps': ['Monitor the resolution clock on the agent dashboard throughout '
                            'the shift.',
                            'Notify the shift lead once the ticket reaches 50 per cent of its '
                            'resolution clock.',
                            'Notify the duty manager once the ticket reaches 80 per cent of '
                            'its resolution clock.',
                            'Record each escalation and the agreed recovery action in the work '
                            'notes.',
                            'Hand the ticket over with a written summary if the shift ends '
                            'before resolution.']},
                 {'name': 'Handling an SLA breach',
                  'steps': ['Apply the correct breach reason code to the ticket before '
                            'closure.',
                            'Capture the sequence of events and the point at which the clock '
                            'was lost.',
                            'Hold the breach review within 5 business days with the resolving '
                            'team present.',
                            'Raise corrective actions with named owners and due dates.',
                            'Report the breach and its actions at the monthly service review '
                            'against the 94 per cent target.']}],
  'troubleshooting': [{'symptom': 'A ticket shows no SLA attached and the record flags '
                                  'D-SN-6023',
                       'cause': 'The ticket was created without a service or configuration '
                                'item, so no SLA definition matched',
                       'resolution': 'Set the affected service and configuration item on the '
                                     'ticket, then save to trigger SLA attachment. Confirm the '
                                     'clock has started from the original creation time rather '
                                     'than the edit time. If the clock starts late, raise it '
                                     'to the Service Management Office so the record can be '
                                     'corrected.',
                       'error_code': 'D-SN-6023'},
                      {'symptom': 'The resolution clock keeps running while waiting on a user',
                       'cause': 'The ticket was left in an active state instead of being moved '
                                'to Pending Customer with a recorded pause reason',
                       'resolution': 'Move the ticket to Pending Customer and record the pause '
                                     'reason in the work notes. Clocks do not pause '
                                     'retrospectively, so note the lost time in the ticket. '
                                     'Ask the Service Management Office to review the record '
                                     'only where the delay would otherwise cause a breach.',
                       'error_code': ''},
                      {'symptom': 'A P1 cannot be saved and returns D-SN-1148',
                       'cause': 'No incident manager has been assigned, which is mandatory for '
                                'P1',
                       'resolution': 'Assign a named incident manager from the on-call rota '
                                     'and save again. Open the bridge call inside the 15 '
                                     'minute response target. If no incident manager is '
                                     'reachable, escalate immediately to the duty manager '
                                     'rather than downgrading the priority.',
                       'error_code': 'D-SN-1148'},
                      {'symptom': 'A closed ticket reopens automatically and logs D-SN-9072',
                       'cause': 'The closure was attempted without a breach reason code on a '
                                'ticket that had already breached',
                       'resolution': 'Add the correct breach reason code and close the ticket '
                                     'again. Schedule the breach review inside the 5 business '
                                     'day window. If no breach code fits the circumstances, '
                                     'escalate to the Service Management Office rather than '
                                     'selecting an inaccurate code.',
                       'error_code': 'D-SN-9072'}],
  'faqs': [('How fast will a critical outage be picked up?',
            'A P1 carries a 15 minute response target and a 3 hour resolution target, measured '
            'around the clock.'),
           ('Can I ask for my ticket to be made P1?',
            'No. Priority comes from the impact and urgency grid, so the service desk will set '
            'it from the facts rather than on request.'),
           ('What counts as business hours for my P3 ticket?',
            '08:00 to 18:00 local time on working days, excluding public holidays.'),
           ('What happens when an SLA is missed?',
            'A breach reason code is applied and a breach review is held within 5 business '
            'days, with actions tracked to closure.')]},
 {'slug': 'change-management',
  'title': 'Change Management Policy',
  'category': 'service-management',
  'doc_type': 'policy',
  'owner': 'Change Management Office',
  'system': 'ServiceNow Change Management',
  'facts': [('change types in use',
             'standard, normal and emergency, with standard changes drawn from a pre-approved '
             'catalogue'),
            ('normal change lead time',
             '7 calendar days before the Change Advisory Board that will review it'),
            ('Change Advisory Board schedule and quorum',
             'Tuesdays at 14:00, requiring 5 voting members present to be quorate'),
            ('emergency change retrospective deadline', '2 business days after implementation'),
            ('annual freeze periods',
             '18 December to 4 January, and the financial year end window of 25 March to 7 '
             'April'),
            ('change success target',
             '97 per cent of implemented changes closed as successful each quarter')],
  'definitions': [('Standard change',
                   'a low risk, repeatable change already assessed and pre-approved as a '
                   'catalogue item, which does not need Change Advisory Board review'),
                  ('Freeze period',
                   'a declared window in which only emergency changes are permitted, '
                   'protecting the business through year end and financial close'),
                  ('Rollback plan',
                   'the documented, tested sequence of steps that returns a service to its '
                   'prior state if the change fails verification')],
  'policy_statements': ['No change may be implemented in production without an approved change '
                        'record raised before the work starts.',
                        'Every normal and emergency change must carry a rollback plan tested '
                        'within the last 21 days.',
                        'Changes submitted inside the 7 calendar day lead time are deferred to '
                        'the following Change Advisory Board unless raised as emergency.',
                        'Only emergency changes are permitted during a declared freeze period, '
                        'and each needs director level approval.',
                        'A change implemented without an approved record is treated as an '
                        'unauthorised change and raised to the Change Management Office as an '
                        'incident.'],
  'procedures': [{'name': 'Submitting a normal change',
                  'steps': ['Raise the change record with the affected configuration items and '
                            'the implementation window.',
                            'Attach the test evidence and the rollback plan with its most '
                            'recent test date.',
                            'Obtain the service owner approval before the record goes to the '
                            'board.',
                            'Submit the record at least 7 calendar days before the intended '
                            'Tuesday board.',
                            'Present the change at the board and record the decision on the '
                            'record.']},
                 {'name': 'Raising an emergency change',
                  'steps': ['Confirm the change is genuinely required to restore service or '
                            'remove an active risk.',
                            'Obtain verbal approval from the duty director and record who gave '
                            'it.',
                            'Raise the emergency change record before starting work, even if '
                            'it is brief.',
                            'Implement the change with a second engineer observing and '
                            'verifying.',
                            'Submit the retrospective to the Change Management Office within 2 '
                            'business days.']},
                 {'name': 'Executing a change rollback',
                  'steps': ['Declare the change failed as soon as verification testing does '
                            'not pass.',
                            'Notify the service desk so user-facing communications can be '
                            'issued.',
                            'Execute the documented rollback steps in order without '
                            'improvising.',
                            'Verify the service against its pre-change baseline before '
                            'standing down.',
                            'Update the change record with the failure reason and close it as '
                            'unsuccessful.',
                            'Feed the failure into the quarterly review against the 97 per '
                            'cent success target.']}],
  'troubleshooting': [{'symptom': 'A change record will not move to Scheduled and returns '
                                  'D-CHG-2290',
                       'cause': 'The record was submitted inside the 7 calendar day lead time '
                                'for the selected board date',
                       'resolution': 'Move the implementation window to the following board '
                                     'cycle, or convert the record to an emergency change if '
                                     'the business case genuinely supports it. Record which '
                                     'option was chosen and why. Escalate to the Change '
                                     'Management Office if the business needs an exception to '
                                     'the lead time.',
                       'error_code': 'D-CHG-2290'},
                      {'symptom': 'A board decision cannot be recorded and the meeting shows '
                                  'D-CHG-7715',
                       'cause': 'Fewer than 5 voting members were present, so the board was '
                                'not quorate',
                       'resolution': 'Defer the decisions to a reconvened session once quorum '
                                     'is available. Low risk items may instead be reclassified '
                                     'as standard changes if they already exist in the '
                                     'catalogue. Escalate to the Change Management Office if '
                                     'quorum has failed twice in a row.',
                       'error_code': 'D-CHG-7715'},
                      {'symptom': 'An approval request is rejected automatically during '
                                  'December',
                       'cause': 'The implementation date falls inside the 18 December to 4 '
                                'January freeze period',
                       'resolution': 'Reschedule the change to begin on or after 5 January. If '
                                     'the work cannot wait, raise it as an emergency change '
                                     'with director level approval and a clear statement of '
                                     'the risk of waiting. Do not attempt to re-date the '
                                     'record to bypass the freeze check.',
                       'error_code': ''},
                      {'symptom': 'A change record is blocked at approval with D-CHG-4038',
                       'cause': 'The attached rollback plan has no test date within the last '
                                '21 days',
                       'resolution': 'Re-test the rollback plan in a non-production '
                                     'environment and update the test date on the record. '
                                     'Attach the fresh test evidence before resubmitting for '
                                     'approval. Escalate to the Change Management Office if '
                                     'the plan cannot be tested because no suitable '
                                     'environment exists.',
                       'error_code': 'D-CHG-4038'}],
  'faqs': [('How far ahead do I need to submit a normal change?',
            'At least 7 calendar days before the Tuesday Change Advisory Board that will '
            'review it.'),
           ('Do standard changes go to the board?',
            'No. Standard changes come from a pre-approved catalogue and are implemented '
            'without board review.'),
           ('Can I release during the Christmas freeze?',
            'Only as an emergency change with director level approval; the freeze runs from 18 '
            'December to 4 January.'),
           ('How current does my rollback plan have to be?',
            'It must have been tested within the last 21 days, otherwise approval is '
            'blocked.')]},
 {'slug': 'database-access-requests',
  'title': 'Database Access Request Runbook',
  'category': 'data',
  'doc_type': 'runbook',
  'owner': 'Data Platform Engineering',
  'system': 'Microsoft SQL Server',
  'facts': [('approval route for read access',
             'the named data owner alone, recorded against the request'),
            ('approval route for write access',
             'the named data owner plus Information Security, both required'),
            ('maximum temporary grant duration',
             '48 hours, revoked automatically by the access job when it expires'),
            ('masked environment refresh cadence',
             'every 14 days from production, with all direct identifiers replaced'),
            ('standing production write accounts',
             '11 named break-glass accounts, held by Data Platform Engineering and reviewed '
             'each quarter'),
            ('reporting replica query timeout',
             '300 seconds, after which the query is cancelled by the resource governor')],
  'definitions': [('Masked environment',
                   'a non-production copy of a database in which names, contact details and '
                   'account numbers have been replaced with realistic but fictitious values'),
                  ('Temporary grant',
                   'a time-boxed permission issued for a specific piece of work and removed '
                   'automatically after 48 hours without any further action'),
                  ('Break-glass account',
                   'a tightly held account with production write rights, used only when no '
                   'other route exists and subject to full session recording')],
  'policy_statements': ['Analysis and development work must use a masked environment unless a '
                        'written exception from the data owner is attached to the request.',
                        'Write access to production is never granted to an individual named '
                        'user; it is exercised only through a break-glass account.',
                        'Every granted permission is recorded against the originating request '
                        'with the approver and the expiry date.',
                        'Access is granted to a database role, never to an individual login '
                        'directly.',
                        'Database access is recertified every 75 days, and any grant whose '
                        'requester has left the business is removed immediately.'],
  'procedures': [{'name': 'Granting read access to a production database',
                  'steps': ['Confirm the requester cannot do the work in a masked environment.',
                            'Route the request to the named data owner for approval.',
                            'Add the requester to the appropriate read-only database role.',
                            'Record the approver, the role and the expiry date against the '
                            'request.',
                            'Schedule the grant for review at the next 75 day '
                            'recertification.']},
                 {'name': 'Issuing a temporary grant',
                  'steps': ['Capture the specific task and the data the requester needs to '
                            'touch.',
                            'Obtain the data owner approval, and Information Security approval '
                            'if any write is involved.',
                            'Create the grant with a 48 hour expiry set on the access job.',
                            'Notify the requester of the exact start and end time of the '
                            'window.',
                            'Confirm the automatic revocation completed after the window '
                            'closed.']},
                 {'name': 'Refreshing a masked environment',
                  'steps': ['Take the scheduled production backup for the 14 day refresh '
                            'cycle.',
                            'Restore it into the staging instance isolated from user access.',
                            'Run the masking job and confirm it reports zero unmasked '
                            'identifier columns.',
                            'Validate row counts and a sample of masked values before opening '
                            'access.',
                            'Release the environment to users and record the refresh date.']}],
  'troubleshooting': [{'symptom': 'A user loses access mid-task and the log records D-SQL-5542',
                       'cause': 'The 48 hour temporary grant expired and was revoked '
                                'automatically',
                       'resolution': 'Confirm the original request and whether the work is '
                                     'still in progress. Raise a fresh temporary grant with '
                                     'the same approvals rather than extending the expired '
                                     'one. Escalate to Data Platform Engineering if the same '
                                     'task has needed more than two temporary grants, as it '
                                     'probably needs a permanent role.',
                       'error_code': 'D-SQL-5542'},
                      {'symptom': 'A reporting query fails after several minutes with '
                                  'D-SQL-8827',
                       'cause': 'The query exceeded the 300 second resource governor timeout '
                                'on the reporting replica',
                       'resolution': 'Review the query plan for missing filters or a full '
                                     'table scan and add the date range the report actually '
                                     'needs. Advise the user to run very large extracts '
                                     'through the scheduled extract service instead. Escalate '
                                     'to Data Platform Engineering if a well filtered query '
                                     'still exceeds 300 seconds.',
                       'error_code': 'D-SQL-8827'},
                      {'symptom': 'A write access request is rejected despite data owner '
                                  'approval',
                       'cause': 'Information Security approval is also mandatory for write '
                                'access and had not been obtained',
                       'resolution': 'Return the request to the requester and ask them to add '
                                     'Information Security as the second approver. Explain '
                                     'that write access to production is exercised through a '
                                     'break-glass account, not a personal login. Escalate to '
                                     'Information Security if the second approval is '
                                     'outstanding for more than one business day.',
                       'error_code': ''},
                      {'symptom': 'A masked environment shows real customer names and raises '
                                  'D-SQL-1903',
                       'cause': 'The masking job did not complete, so the restored copy was '
                                'released with unmasked identifier columns',
                       'resolution': 'Withdraw user access to the environment immediately and '
                                     'treat it as a data exposure. Re-run the masking job and '
                                     'confirm it reports zero unmasked identifier columns '
                                     'before reopening access. Report the exposure to '
                                     'Information Security the same day.',
                       'error_code': 'D-SQL-1903'}],
  'faqs': [('Who approves read access to a production database?',
            'The named data owner alone, with the approval recorded against the request.'),
           ('How long does a temporary grant last?',
            '48 hours, after which the access job revokes it automatically.'),
           ('Can I get write access to production?',
            'Not as a personal login. Write access is exercised through one of the 11 '
            'break-glass accounts held by Data Platform Engineering.'),
           ('How fresh is the masked test data?',
            'It is refreshed from production every 14 days with all direct identifiers '
            'replaced.')]},
 {'slug': 'crm-application-support',
  'title': 'CRM Application Support Runbook',
  'category': 'applications',
  'doc_type': 'runbook',
  'owner': 'Business Applications',
  'system': 'Salesforce',
  'facts': [('number of supported profiles',
             '9 profiles, with all additional access granted through permission sets'),
            ('import row threshold',
             '50,000 rows through the Data Import Wizard; anything larger must go through Data '
             'Loader'),
            ('sandbox refresh intervals',
             'a full sandbox every 29 days and a partial copy sandbox every 5 days'),
            ('permission set assignment turnaround',
             '1 business day once the CRM product owner has approved'),
            ('daily API request allowance',
             '115,000 requests per rolling 24 hours across all integrations'),
            ('field history retention',
             '24 months of field history, after which entries are purged')],
  'definitions': [('Profile',
                   'the base access definition assigned to a user, controlling object '
                   'permissions and page layouts, of which only 9 are supported'),
                  ('Permission set',
                   'an additive grant layered on top of a profile to give a user extra access '
                   'without creating another profile'),
                  ('Sandbox refresh',
                   'the process of replacing a sandbox with a fresh copy of production '
                   'metadata, which destroys any unreleased work left in that sandbox')],
  'policy_statements': ['New profiles are not created; additional access is delivered through '
                        'permission sets so the supported set stays at 9.',
                        'No data import may run in production without a successful dry run in '
                        'a sandbox and a documented rollback approach.',
                        'Integration users must authenticate with a dedicated integration '
                        'account, never with a named employee login.',
                        'Users must be told at least 3 business days before a sandbox refresh '
                        'so unreleased work can be saved.',
                        'Bulk record deletion in production requires CRM product owner '
                        'approval and must be executed by Business Applications, not by the '
                        'requester.'],
  'procedures': [{'name': 'Assigning a permission set',
                  'steps': ["Confirm the requested access is not already covered by the user's "
                            'profile.',
                            'Route the request to the CRM product owner for approval.',
                            'Assign the permission set to the user rather than editing the '
                            'profile.',
                            'Verify the user can reach the intended records and nothing more.',
                            'Close the request within 1 business day of the approval.']},
                 {'name': 'Running a data import',
                  'steps': ['Validate the source file headers against the target object '
                            'fields.',
                            'Run the import in a sandbox first and review the error file.',
                            'Choose the Data Import Wizard below 50,000 rows and Data Loader '
                            'above it.',
                            'Capture the record identifiers created so the load can be '
                            'reversed if needed.',
                            'Run the production import outside business hours and confirm the '
                            'row counts.',
                            'Attach the success and error files to the ticket.']},
                 {'name': 'Refreshing a sandbox',
                  'steps': ['Confirm the sandbox is past its refresh interval of 29 days for '
                            'full or 5 days for partial copy.',
                            'Notify all sandbox users at least 3 business days in advance.',
                            'Ask developers to commit unreleased work to the version control '
                            'repository.',
                            'Start the refresh and monitor it to completion.',
                            'Reapply the post-refresh configuration such as email '
                            'deliverability and test data.']}],
  'troubleshooting': [{'symptom': 'An integration stops writing records and logs D-SF-17003',
                       'cause': 'The 115,000 daily API request allowance has been exhausted by '
                                'one of the integrations',
                       'resolution': 'Open the API usage report and identify which integration '
                                     'consumed the allowance. Pause that integration and move '
                                     'its bulk work onto the Bulk API, which consumes far '
                                     'fewer requests. Escalate to Business Applications if the '
                                     'allowance is being hit on more than two days in a month, '
                                     'as the integration design needs review.',
                       'error_code': 'D-SF-17003'},
                      {'symptom': 'A data import fails partway and returns D-SF-26114',
                       'cause': 'The file exceeds the 50,000 row limit for the Data Import '
                                'Wizard',
                       'resolution': 'Stop the import and reconcile which rows were created '
                                     'using the captured identifiers. Re-run the load through '
                                     'Data Loader in batches. Escalate to Business '
                                     'Applications if partial records have already triggered '
                                     'downstream automation.',
                       'error_code': 'D-SF-26114'},
                      {'symptom': 'A user cannot see an object their colleague can see',
                       'cause': 'The colleague holds an additional permission set that the '
                                'user has not been assigned',
                       'resolution': 'Compare the two users in the setup audit view to '
                                     'identify the missing permission set. Raise a request to '
                                     'the CRM product owner for approval rather than editing '
                                     'the profile. Assignment completes within 1 business day '
                                     'of approval.',
                       'error_code': ''},
                      {'symptom': 'Unreleased configuration disappears from a sandbox and the '
                                  'log shows D-SF-31508',
                       'cause': 'The sandbox was refreshed on its 29 day cycle and the work '
                                'had not been committed to version control',
                       'resolution': 'Check the version control repository for the last commit '
                                     'and rebuild from there. Confirm the refresh notice was '
                                     'issued 3 business days in advance and record the gap if '
                                     'it was not. Escalate to Business Applications to review '
                                     'the notification process if users were not warned.',
                       'error_code': 'D-SF-31508'}],
  'faqs': [('Can I get a new profile created for my team?',
            'No. The supported set stays at 9 profiles, and extra access is delivered through '
            'permission sets.'),
           ('How many rows can I load with the Data Import Wizard?',
            'Up to 50,000 rows; anything larger must go through Data Loader.'),
           ('How soon will my permission set be assigned?',
            'Within 1 business day of the CRM product owner approving the request.'),
           ('How long is field history kept?',
            '24 months, after which the entries are purged.')]},
 {'slug': 'erp-application-support',
  'title': 'ERP Application Support Runbook',
  'category': 'applications',
  'doc_type': 'runbook',
  'owner': 'ERP Support',
  'system': 'SAP S/4HANA',
  'facts': [('period close support window',
             'the last 3 business days of each month and the first 5 business days of the '
             'next, with extended cover from 07:00 to 22:00'),
            ('transport approval route',
             'two stage approval, the functional lead followed by the Basis team, before any '
             'transport reaches production'),
            ('transport freeze rule',
             'no transports are released to production at any point inside the period close '
             'support window'),
            ('segregation of duties remediation deadline',
             '15 business days from the date a conflict is reported on a role assignment'),
            ('interface monitoring interval',
             'every 8 minutes, with failed documents raised automatically as tickets'),
            ('maximum firefighter session length',
             '90 minutes, after which the elevated access is revoked automatically')],
  'definitions': [('Transport request',
                   'a packaged set of configuration or development changes moved in sequence '
                   'from development through quality assurance to production'),
                  ('Segregation of duties conflict',
                   'a role combination that would let one person both create and approve the '
                   'same transaction, for example raising a purchase order and releasing its '
                   'payment'),
                  ('Firefighter access',
                   'temporary elevated access granted for an urgent production problem, fully '
                   'session logged and limited to 90 minutes')],
  'policy_statements': ['No configuration or development change reaches production except '
                        'through an approved transport request.',
                        'Transports must be imported in the sequence they were released, never '
                        'selectively, to avoid overwriting later objects.',
                        'Role assignments that create a segregation of duties conflict require '
                        'finance director approval and a compensating control.',
                        'Firefighter access is granted only against an open incident and its '
                        'session log is reviewed by ERP Support the next working day.',
                        'Interface failures affecting financial postings must be raised to the '
                        'finance systems lead before the close window ends.'],
  'procedures': [{'name': 'Releasing a transport to production',
                  'steps': ['Confirm the change is not inside the period close support window '
                            'transport freeze.',
                            'Obtain the functional lead approval on the transport request.',
                            'Obtain the Basis team approval as the second stage.',
                            'Import the transport in release sequence and capture the import '
                            'log.',
                            'Verify the change in production with the requesting business '
                            'user.',
                            'Close the transport record with the import log attached.']},
                 {'name': 'Granting firefighter access',
                  'steps': ['Confirm an open incident exists that genuinely needs elevated '
                            'access.',
                            'Obtain approval from the ERP Support lead and record the incident '
                            'number.',
                            'Issue the firefighter session with the 90 minute automatic '
                            'revocation set.',
                            'Watch the session log while the work is carried out.',
                            'Review the completed session log on the next working day and '
                            'attach it to the incident.']},
                 {'name': 'Resolving an interface failure',
                  'steps': ['Open the failed document from the interface monitor that runs '
                            'every 8 minutes.',
                            'Identify whether the failure is data, mapping or connectivity '
                            'related.',
                            'Correct the source data or mapping, keeping the original document '
                            'for audit.',
                            'Reprocess the document and confirm the posting completes.',
                            'Notify the finance systems lead if the posting affects the '
                            'current close.']}],
  'troubleshooting': [{'symptom': 'A transport import is refused and returns D-SAP-M7021',
                       'cause': 'The import was attempted inside the period close support '
                                'window, where the transport freeze applies',
                       'resolution': 'Hold the transport until the close window ends and '
                                     'reschedule the import. If the change is needed to '
                                     'complete the close itself, raise it as an emergency with '
                                     'the finance systems lead and the Basis team. Do not '
                                     'bypass the freeze by importing directly into the '
                                     'production client.',
                       'error_code': 'D-SAP-M7021'},
                      {'symptom': 'A role assignment is blocked at approval with D-SAP-B4455',
                       'cause': 'The requested role combination creates a segregation of '
                                'duties conflict',
                       'resolution': 'Show the requester the conflicting role pair and offer a '
                                     'split that removes the conflict. If the business '
                                     'genuinely needs both, obtain finance director approval '
                                     'and document a compensating control. The conflict must '
                                     'be remediated or formally accepted within 15 business '
                                     'days.',
                       'error_code': 'D-SAP-B4455'},
                      {'symptom': 'Inbound documents stop posting and the monitor logs '
                                  'D-SAP-I9308',
                       'cause': 'The interface partner profile is pointing at a connection '
                                'that is no longer reachable',
                       'resolution': 'Test the connection from the Basis console and confirm '
                                     'the target host and port. Correct the partner profile, '
                                     'then reprocess the queued documents in the order they '
                                     'arrived. Escalate to the Basis team if the connection '
                                     'test still fails, and tell the finance systems lead if '
                                     'any failed posting falls inside the close.',
                       'error_code': 'D-SAP-I9308'},
                      {'symptom': "A user's elevated access disappears while they are mid-task",
                       'cause': 'The firefighter session reached its 90 minute limit and was '
                                'revoked automatically',
                       'resolution': 'Confirm the incident is still open, then issue a fresh '
                                     'firefighter session with a new approval. Ask the user to '
                                     'record progress in the incident so the next session is '
                                     'shorter. Escalate to the ERP Support lead if a single '
                                     'task has needed more than two firefighter sessions.',
                       'error_code': ''}],
  'faqs': [('Can a transport go live during month end close?',
            'No. No transports are released to production inside the period close support '
            'window.'),
           ('Who approves a transport?',
            'Two approvers in sequence: the functional lead, then the Basis team.'),
           ('How long does firefighter access last?',
            '90 minutes, after which the elevated access is revoked automatically.'),
           ('How quickly are interface failures spotted?',
            'The interface monitor runs every 8 minutes and raises failed documents '
            'automatically as tickets.')]}]
