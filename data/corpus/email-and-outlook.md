---
title: Email and Outlook Services Runbook
doc_type: runbook
category: productivity
owner: Messaging Services
version: 2.1
review_date: 2027-02-09
---

# Email and Outlook Services Runbook

Owner: Messaging Services | System of record: Exchange Online | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages email and outlook services. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Messaging Services team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the productivity estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Exchange Online is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Exchange Online. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Shared mailbox**  
A mailbox with no licensed owner that several named users open alongside their own mailbox, used for team addresses such as accounts.payable@meridiangroup.example.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Delegation**  
A permission that lets one named user send on behalf of, or send as, another mailbox without knowing that mailbox password.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Online archive**  
The secondary mailbox store in Exchange Online where older mail is moved by policy so that the primary mailbox stays under quota.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Messaging Services. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Messaging Services** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Messaging Services rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Mailbox delegation must be requested by the mailbox owner or, for a shared mailbox, by the named business owner recorded in ServiceNow.

There is a documented exception route, described later in this document. Evidence that the control is operating is collected automatically from Exchange Online and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 2. Automatic forwarding of Meridian Group mail to external domains is blocked by transport rule and requires an approved exception from Information Security.

Agents should treat this as non-negotiable. Messaging Services configures Exchange Online to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Messaging Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 3. Shared mailboxes must have a named business owner, and Messaging Services disables any shared mailbox whose owner has left and not been replaced.

In practice this means the following. Evidence that the control is operating is collected automatically from Exchange Online and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 4. Users must not use personal email accounts to send Meridian Group business correspondence.

This is enforced technically wherever the platform allows it. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Messaging Services will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 5. Leaver mailboxes are converted to shared mailboxes for handover only when the line manager requests it in writing, and are removed once handover is complete.

This has been the standing position since the last review. This statement has been tested against the current configuration of Exchange Online. Where a platform change makes it unenforceable, Messaging Services raises a risk acceptance rather than quietly dropping the control. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Messaging Services configures in Exchange Online. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Maximum user mailbox size | 100 GB, with a quota warning raised at 90 GB |
| Maximum shared mailbox size | 50 GB with no personal archive attached |
| Archive policy move window | items older than 1095 days are moved automatically to the online archive |
| Recoverable items retention for deleted mail | 21 days before items are purged permanently |
| Maximum distribution list membership | 2500 recipients per list |
| New mailbox provisioning time | 3 hours from the approved joiner request in ServiceNow |

**Maximum user mailbox size.** The maximum user mailbox size is 100 GB, with a quota warning raised at 90 GB. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Maximum shared mailbox size.** The maximum shared mailbox size is 50 GB with no personal archive attached. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Archive policy move window.** The archive policy move window is items older than 1095 days are moved automatically to the online archive. This is configured centrally in Exchange Online and is not adjustable per user or per team.

**Recoverable items retention for deleted mail.** The recoverable items retention for deleted mail is 21 days before items are purged permanently. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Maximum distribution list membership.** The maximum distribution list membership is 2500 recipients per list. This is configured centrally in Exchange Online and is not adjustable per user or per team.

**New mailbox provisioning time.** The new mailbox provisioning time is 3 hours from the approved joiner request in ServiceNow. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Exchange Online diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Messaging Services, and reviewed annually with Information Security.

## Architecture and dependencies

Exchange Online is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Exchange Online follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Messaging Services maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Messaging Services raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Exchange Online, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Messaging Services implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Messaging Services rather than skipping it.

### Create a shared mailbox

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the request names a business owner and the full list of members who need access.
2. Create the shared mailbox in the Exchange admin centre using the agreed address format.
3. Create a mail-enabled security group and add the named members to it.
4. Grant the group full access and send as permissions on the shared mailbox.
5. Record the business owner and the group name in the ServiceNow configuration item and close the request.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Grant calendar and mailbox delegation

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Verify that the mailbox owner has approved the request in writing.
2. Apply the requested delegate permission level in the Exchange admin centre.
3. Confirm whether send on behalf of or send as is required and set only that permission.
4. Ask the delegate to restart Outlook and confirm the mailbox appears in their folder list.
5. Note the permission and the approval reference on the ServiceNow ticket.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Resolve a mailbox over quota

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Check the current mailbox size and the archive status in the Exchange admin centre.
2. Confirm the archive policy is applied and trigger a managed folder assistant run.
3. Advise the user to empty the deleted items and junk email folders.
4. Remove large attachments to a file share or OneDrive location if the archive alone is not enough.
5. Apply a temporary quota uplift for a maximum of 14 days if the user needs time to tidy the mailbox.
6. Confirm the mailbox is back under 90 GB and close the ticket.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Messaging Services with the diagnostic output attached rather than retrying the same steps.

### Symptom: A user reports that outbound mail is rejected with a message saying the recipient mailbox is full.


**Error code:** A-QUOTA-5.2.2

**Cause.** The recipient mailbox has reached its quota and Exchange Online is refusing further delivery..

**Resolution.** Confirm the recipient is internal and check the mailbox size against the 100 GB limit. Run the archive policy and ask the recipient to clear deleted items, then ask the sender to retry. Escalate to Messaging Services second line if the mailbox cannot be brought under quota within the same working day.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: Outlook repeatedly prompts for credentials and will not connect to the mailbox.


**Error code:** A-MAPI-0x8004010F

**Cause.** A stale cached credential in the Windows credential manager is being replayed against Exchange Online..

**Resolution.** Remove the Office and Exchange entries from the Windows credential manager, close Outlook fully and sign in again with the user's Entra ID account. Check that the device is compliant so conditional access does not block the sign-in. Escalate to the identity team if the prompt returns after a second clean sign-in.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A delegate cannot send as a shared mailbox and receives a delivery failure within seconds.


**Error code:** A-EXO-550-5.4.1

**Cause.** The delegate holds full access only, and send as permission was never granted on the shared mailbox..

**Resolution.** Add the send as permission to the security group that fronts the shared mailbox, then wait for directory replication before retesting. Ask the delegate to restart Outlook so the permission cache refreshes. Escalate to Messaging Services if the failure persists more than one hour after the permission change.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: Outlook on the web loads to a blank page for one user while the desktop client works normally.


**Error code:** A-OWA-500-17

**Cause.** A corrupt mailbox setting or a stale browser session token is breaking the web session..

**Resolution.** Ask the user to clear the browser cache and sign in from a private window to rule out the token. If the page is still blank, reset the Outlook on the web settings for that mailbox from the Exchange admin centre. Escalate to Microsoft support with the session identifier if a settings reset does not fix it.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Messaging Services to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A user reports that outbound mail is rejected with a message saying th

Reference: A-QUOTA-5.2.2.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Exchange Online and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Messaging Services citing the reference above.

### Diagnostics for: Outlook repeatedly prompts for credentials and will not connect to the

Reference: A-MAPI-0x8004010F.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Exchange Online and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Messaging Services citing the reference above.

### Diagnostics for: A delegate cannot send as a shared mailbox and receives a delivery fai

Reference: A-EXO-550-5.4.1.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Exchange Online and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Messaging Services citing the reference above.

### Diagnostics for: Outlook on the web loads to a blank page for one user while the deskto

Reference: A-OWA-500-17.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Exchange Online and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Messaging Services citing the reference above.

## Worked examples

### Example: A user reports that outbound mail is rejected with a message saying th

A user at London HQ contacts the service desk reporting that a user reports that outbound mail is rejected with a message saying the recipient mailbox is full.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The recipient mailbox has reached its quota and Exchange Online is refusing further delivery.. Following the documented resolution, confirm the recipient is internal and check the mailbox size against the 100 GB limit. Run the archive policy and ask the recipient to clear deleted items, then ask the sender to retry. Escalate to Messaging Services second line if the mailbox cannot be brought under quota within the same working day.

The agent records the diagnosis against the ticket, confirms with paulo.sorensen@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Messaging Services was needed.

### Example: Outlook repeatedly prompts for credentials and will not connect to the

A user at Singapore contacts the service desk reporting that outlook repeatedly prompts for credentials and will not connect to the mailbox.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: A stale cached credential in the Windows credential manager is being replayed against Exchange Online.. Following the documented resolution, remove the Office and Exchange entries from the Windows credential manager, close Outlook fully and sign in again with the user's Entra ID account. Check that the device is compliant so conditional access does not block the sign-in. Escalate to the identity team if the prompt returns after a second clean sign-in.

The agent records the diagnosis against the ticket, confirms with aisha.nakamura@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Messaging Services was needed.

### Example: A delegate cannot send as a shared mailbox and receives a delivery fai

A user at Rotterdam contacts the service desk reporting that a delegate cannot send as a shared mailbox and receives a delivery failure within seconds.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The delegate holds full access only, and send as permission was never granted on the shared mailbox.. Following the documented resolution, add the send as permission to the security group that fronts the shared mailbox, then wait for directory replication before retesting. Ask the delegate to restart Outlook so the permission cache refreshes. Escalate to Messaging Services if the failure persists more than one hour after the permission change.

The agent records the diagnosis against the ticket, confirms with lucas.okafor@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Messaging Services was needed.

### Example: create a shared mailbox

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about email and outlook services. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the maximum user mailbox size is flexible or negotiable per user.**

It is not. The maximum user mailbox size is 100 GB, with a quota warning raised at 90 GB, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the maximum shared mailbox size is flexible or negotiable per user.**

It is not. The maximum shared mailbox size is 50 GB with no personal archive attached, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the archive policy move window is flexible or negotiable per user.**

It is not. The archive policy move window is items older than 1095 days are moved automatically to the online archive, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the recoverable items retention for deleted mail is flexible or negotiable per user.**

It is not. The recoverable items retention for deleted mail is 21 days before items are purged permanently, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Messaging Services can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to email and outlook services, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Messaging Services.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Exchange Online did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Messaging Services produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about email and outlook services unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Messaging Services runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How large can my mailbox get?**

Your mailbox can hold up to 100 GB, and you receive a warning once it passes 90 GB.

**Can I recover mail I deleted last week?**

Yes, deleted items stay recoverable for 21 days before they are purged permanently.

**Why has older mail disappeared from my inbox?**

Mail older than 1095 days is moved automatically to your online archive, which you can still search from Outlook.

**How quickly will a new joiner get a mailbox?**

A mailbox is created within 3 hours of the approved joiner request in ServiceNow.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Messaging Services will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Messaging Services, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Exchange Online, engaged by Messaging Services only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Messaging Services produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about email and outlook services. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the request names a business owner and the full list of members who need access.
- [ ] Create the shared mailbox in the Exchange admin centre using the agreed address format.
- [ ] Verify that the mailbox owner has approved the request in writing.
- [ ] Apply the requested delegate permission level in the Exchange admin centre.
- [ ] Check the current mailbox size and the archive status in the Exchange admin centre.
- [ ] Confirm the archive policy is applied and trigger a managed folder assistant run.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How large can my mailbox get? Your mailbox can hold up to 100 GB, and you receive a warning once it passes 90 GB.
- Can I recover mail I deleted last week? Yes, deleted items stay recoverable for 21 days before they are purged permanently.
- Why has older mail disappeared from my inbox? Mail older than 1095 days is moved automatically to your online archive, which you can still search from Outlook.
- How quickly will a new joiner get a mailbox? A mailbox is created within 3 hours of the approved joiner request in ServiceNow.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Messaging Services | First published version. |
| 1.1 | 2024-11-02 | Messaging Services | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Messaging Services | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Messaging Services | Annual review; figures confirmed against the running configuration of Exchange Online. |
