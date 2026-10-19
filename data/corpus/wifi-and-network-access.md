---
title: Wi-Fi and Network Access Runbook
doc_type: runbook
category: network
owner: Network Services
version: 2.1
review_date: 2027-02-09
---

# Wi-Fi and Network Access Runbook

Owner: Network Services | System of record: Cisco Identity Services Engine | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages wi-fi and network access. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Network Services team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the network estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Cisco Identity Services Engine is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Cisco Identity Services Engine. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**EAP-TLS**  
A wireless authentication method where the laptop presents a machine certificate issued by the Meridian Group certificate authority instead of a username and password.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Guest voucher**  
A time-limited code issued by reception or a sponsoring employee that grants a visitor internet-only access on the MG-GUEST network.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Posture check**  
The Cisco Identity Services Engine assessment that confirms a device is managed, encrypted and running current endpoint protection before it is placed on the corporate network.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Network Services. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Network Services** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Network Services rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Only devices holding a valid Meridian Group machine certificate may join MG-CORP, and pre-shared keys must never be used on the corporate network.

This has been the standing position since the last review. This statement has been tested against the current configuration of Cisco Identity Services Engine. Where a platform change makes it unenforceable, Network Services raises a risk acceptance rather than quietly dropping the control. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 2. Visitors must be sponsored by a named employee, and guest vouchers must not be reissued to the same visitor to extend access beyond the voucher validity.

This is enforced technically wherever the platform allows it. Evidence that the control is operating is collected automatically from Cisco Identity Services Engine and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 3. Personal devices may join MG-BYOD only, and must not be connected to corporate wired ports.

The reasoning behind this is straightforward. Evidence that the control is operating is collected automatically from Cisco Identity Services Engine and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Network Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 4. Wired ports in meeting rooms and public areas remain disabled by default and are enabled only for an approved business need.

Agents should treat this as non-negotiable. Network Services configures Cisco Identity Services Engine to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Where the control cannot be enforced technically, Network Services monitors for breaches and follows up with the individual and their line manager.

### 5. Network Services must review and remove dormant device registrations at least once every quarter.

In practice this means the following. Evidence that the control is operating is collected automatically from Cisco Identity Services Engine and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Network Services configures in Cisco Identity Services Engine. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Corporate wireless network name and authentication method | MG-CORP, using certificate based EAP-TLS authentication |
| Guest Wi-Fi voucher validity | 36 hours from first use of the voucher code |
| Guest Wi-Fi bandwidth cap per device | 10 Mbps download and upload |
| Device authentication certificate lifetime | 400 days, with automatic renewal starting 30 days before expiry |
| Wired port activation lead time | 4 working days from the approved request |
| Personal device registration limit on MG-BYOD | 6 registered personal devices per employee |

**Corporate wireless network name and authentication method.** The corporate wireless network name and authentication method is MG-CORP, using certificate based EAP-TLS authentication. Network Services set this figure in consultation with Information Security, and it is reviewed annually.

**Guest Wi-Fi voucher validity.** The guest Wi-Fi voucher validity is 36 hours from first use of the voucher code. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Guest Wi-Fi bandwidth cap per device.** The guest Wi-Fi bandwidth cap per device is 10 Mbps download and upload. This is configured centrally in Cisco Identity Services Engine and is not adjustable per user or per team.

**Device authentication certificate lifetime.** The device authentication certificate lifetime is 400 days, with automatic renewal starting 30 days before expiry. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Wired port activation lead time.** The wired port activation lead time is 4 working days from the approved request. Network Services set this figure in consultation with Information Security, and it is reviewed annually.

**Personal device registration limit on MG-BYOD.** The personal device registration limit on MG-BYOD is 6 registered personal devices per employee. Network Services set this figure in consultation with Information Security, and it is reviewed annually.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Cisco Identity Services Engine diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Network Services, and reviewed annually with Information Security.

## Architecture and dependencies

Cisco Identity Services Engine is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Cisco Identity Services Engine follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Network Services maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Network Services raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Cisco Identity Services Engine, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Network Services implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Network Services rather than skipping it.

### Onboard a managed laptop onto MG-CORP

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the laptop is enrolled in Microsoft Intune and reports as compliant.
2. Verify the machine certificate is present and within its validity period.
3. Connect to MG-CORP and allow the posture check to complete.
4. Confirm in Cisco Identity Services Engine that the device landed in the corporate authorisation profile.
5. Record the device MAC address against the asset record if it is a new build.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Issue guest Wi-Fi access for a visitor

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the sponsoring employee name and the date of the visit.
2. Create a guest account in the sponsor portal and set the expiry to match the voucher validity.
3. Hand the voucher code to the visitor at reception and explain the bandwidth cap.
4. Ask the visitor to connect to MG-GUEST and accept the acceptable use notice.
5. Let the voucher lapse at expiry rather than extending it.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Activate a wired network port

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise a port activation request in ServiceNow with the room number and the faceplate label.
2. Obtain approval from the site facilities contact and from Network Services.
3. Trace the faceplate label to the switch port in the patching records.
4. Configure the switch port with the correct access profile and enable it.
5. Test with a managed laptop and confirm the port authorises through Cisco Identity Services Engine.
6. Update the patching records and close the request.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Network Services with the diagnostic output attached rather than retrying the same steps.

### Symptom: A managed laptop cannot join MG-CORP and reports that authentication failed immediately.


**Error code:** A-EAPTLS-0x80420012

**Cause.** The machine certificate has expired or was never issued, so EAP-TLS has nothing to present..

**Resolution.** Check the certificate store on the device and trigger the certificate profile from Microsoft Intune to reissue the machine certificate. Reconnect to MG-CORP once the certificate shows a valid date range. Escalate to the certificate authority team if enrolment fails twice on the same device.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A laptop connects to MG-CORP but is placed on a restricted network with no access to internal systems.


**Error code:** A-ISE-11514

**Cause.** The posture check failed because the endpoint protection agent has not reported in recently..

**Resolution.** Confirm the CrowdStrike agent is running and has checked in, then disconnect and reconnect so the posture check runs again. Review the posture result in Cisco Identity Services Engine. Escalate to Information Security if the agent cannot be brought back into a reporting state.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: A newly activated wired port shows a link light but the laptop receives no usable address.


**Error code:** A-DHCP-1056

**Cause.** The switch port is enabled but the correct access profile and VLAN were not applied, so the address request is never answered..

**Resolution.** Check the switch port configuration against the standard access profile and apply the missing VLAN assignment. Bounce the port and retest with a managed laptop. Escalate to Network Services second line if the port still fails after the configuration is confirmed correct.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A user reports they cannot register another personal phone on MG-BYOD.


**Error code:** A-DOT1X-4402

**Cause.** The user has reached the personal device registration limit and the portal is refusing a further registration..

**Resolution.** Ask the user to remove a device they no longer own from the registration portal, then retry the registration. Explain that the limit applies per employee and is not raised on request. Escalate to Network Services only if removed devices still count towards the limit after an hour.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Network Services to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A managed laptop cannot join MG-CORP and reports that authentication f

Reference: A-EAPTLS-0x80420012.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Cisco Identity Services Engine and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Network Services citing the reference above.

### Diagnostics for: A laptop connects to MG-CORP but is placed on a restricted network wit

Reference: A-ISE-11514.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Cisco Identity Services Engine and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Network Services citing the reference above.

### Diagnostics for: A newly activated wired port shows a link light but the laptop receive

Reference: A-DHCP-1056.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Cisco Identity Services Engine and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Network Services citing the reference above.

### Diagnostics for: A user reports they cannot register another personal phone on MG-BYOD.

Reference: A-DOT1X-4402.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Cisco Identity Services Engine and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Network Services citing the reference above.

## Worked examples

### Example: A managed laptop cannot join MG-CORP and reports that authentication f

A user at Dublin contacts the service desk reporting that a managed laptop cannot join MG-CORP and reports that authentication failed immediately.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The machine certificate has expired or was never issued, so EAP-TLS has nothing to present.. Following the documented resolution, check the certificate store on the device and trigger the certificate profile from Microsoft Intune to reissue the machine certificate. Reconnect to MG-CORP once the certificate shows a valid date range. Escalate to the certificate authority team if enrolment fails twice on the same device.

The agent records the diagnosis against the ticket, confirms with kwame.haddad@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Network Services was needed.

### Example: A laptop connects to MG-CORP but is placed on a restricted network wit

A user at London HQ contacts the service desk reporting that a laptop connects to MG-CORP but is placed on a restricted network with no access to internal systems.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The posture check failed because the endpoint protection agent has not reported in recently.. Following the documented resolution, confirm the CrowdStrike agent is running and has checked in, then disconnect and reconnect so the posture check runs again. Review the posture result in Cisco Identity Services Engine. Escalate to Information Security if the agent cannot be brought back into a reporting state.

The agent records the diagnosis against the ticket, confirms with paulo.moreau@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Network Services was needed.

### Example: A newly activated wired port shows a link light but the laptop receive

A user at Manchester contacts the service desk reporting that a newly activated wired port shows a link light but the laptop receives no usable address.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The switch port is enabled but the correct access profile and VLAN were not applied, so the address request is never answered.. Following the documented resolution, check the switch port configuration against the standard access profile and apply the missing VLAN assignment. Bounce the port and retest with a managed laptop. Escalate to Network Services second line if the port still fails after the configuration is confirmed correct.

The agent records the diagnosis against the ticket, confirms with yusuf.kaur@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Network Services was needed.

### Example: onboard a managed laptop onto mg-corp

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about wi-fi and network access. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the corporate wireless network name and authentication method is flexible or negotiable per user.**

It is not. The corporate wireless network name and authentication method is MG-CORP, using certificate based EAP-TLS authentication, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the guest Wi-Fi voucher validity is flexible or negotiable per user.**

It is not. The guest Wi-Fi voucher validity is 36 hours from first use of the voucher code, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the guest Wi-Fi bandwidth cap per device is flexible or negotiable per user.**

It is not. The guest Wi-Fi bandwidth cap per device is 10 Mbps download and upload, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the device authentication certificate lifetime is flexible or negotiable per user.**

It is not. The device authentication certificate lifetime is 400 days, with automatic renewal starting 30 days before expiry, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Network Services can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to wi-fi and network access, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Network Services.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Cisco Identity Services Engine did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Network Services produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about wi-fi and network access unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Network Services runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Which Wi-Fi network should I use on my work laptop?**

Use MG-CORP, which authenticates your laptop automatically with a certificate rather than a password.

**How long does a visitor voucher last?**

A guest voucher is valid for 36 hours from first use and is not extended.

**How many personal devices can I register?**

You can register up to 6 personal devices on MG-BYOD at any one time.

**How long will it take to get a desk network port switched on?**

Wired port activation takes 4 working days from the point the request is approved.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Network Services will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Network Services, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Cisco Identity Services Engine, engaged by Network Services only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Network Services produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about wi-fi and network access. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the laptop is enrolled in Microsoft Intune and reports as compliant.
- [ ] Verify the machine certificate is present and within its validity period.
- [ ] Confirm the sponsoring employee name and the date of the visit.
- [ ] Create a guest account in the sponsor portal and set the expiry to match the voucher validity.
- [ ] Raise a port activation request in ServiceNow with the room number and the faceplate label.
- [ ] Obtain approval from the site facilities contact and from Network Services.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Which Wi-Fi network should I use on my work laptop? Use MG-CORP, which authenticates your laptop automatically with a certificate rather than a password.
- How long does a visitor voucher last? A guest voucher is valid for 36 hours from first use and is not extended.
- How many personal devices can I register? You can register up to 6 personal devices on MG-BYOD at any one time.
- How long will it take to get a desk network port switched on? Wired port activation takes 4 working days from the point the request is approved.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Network Services | First published version. |
| 1.1 | 2024-11-02 | Network Services | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Network Services | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Network Services | Annual review; figures confirmed against the running configuration of Cisco Identity Services Engine. |
