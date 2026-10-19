---
title: File Shares and Storage Policy
doc_type: policy
category: storage
owner: Storage and Collaboration
version: 2.1
review_date: 2027-02-09
---

# File Shares and Storage Policy

Owner: Storage and Collaboration | System of record: Microsoft SharePoint Online | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages file shares and storage. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Storage and Collaboration team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the storage estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Microsoft SharePoint Online is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Microsoft SharePoint Online. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Data owner**  
The named business manager accountable for who may access a share or SharePoint site and for signing off each access review.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Departmental share**  
A network share mapped by group policy for a single department, used for records that must stay inside the department rather than being shared broadly.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Known folder move**  
The OneDrive feature that redirects the Desktop, Documents and Pictures folders into OneDrive so that local files are backed up automatically.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Storage and Collaboration. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Storage and Collaboration** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Storage and Collaboration rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Every departmental share and SharePoint site must have a named data owner recorded in ServiceNow before it is created.

There is a documented exception route, described later in this document. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Storage and Collaboration will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 2. Access to shares must be granted through Entra ID groups only, and direct permissions on folders are not permitted.

Agents should treat this as non-negotiable. This statement has been tested against the current configuration of Microsoft SharePoint Online. Where a platform change makes it unenforceable, Storage and Collaboration raises a risk acceptance rather than quietly dropping the control. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 3. Business data must be stored in OneDrive, SharePoint Online or an approved network share, and never only on a laptop local disk.

This is enforced technically wherever the platform allows it. This statement has been tested against the current configuration of Microsoft SharePoint Online. Where a platform change makes it unenforceable, Storage and Collaboration raises a risk acceptance rather than quietly dropping the control. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 4. Anonymous external sharing links are disabled across Meridian Group, and external sharing must use a named guest account.

The reasoning behind this is straightforward. Evidence that the control is operating is collected automatically from Microsoft SharePoint Online and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 5. Data owners must complete each access review within the review cadence, and Storage and Collaboration removes access that is not reconfirmed.

This has been the standing position since the last review. Storage and Collaboration configures Microsoft SharePoint Online to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Storage and Collaboration configures in Microsoft SharePoint Online. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Personal home drive quota | 250 GB per employee |
| Default departmental network share quota | 2 TB per department, raised only by an approved capacity request |
| OneDrive storage allocation per licensed user | 5 TB per user |
| Second stage recycle bin retention | 93 days before a deleted item is purged permanently |
| Share permission access review cadence | every 180 days, signed off by the named data owner |
| Retention period for finance record shares | 1825 days from the end of the financial year the records belong to |

**Personal home drive quota.** The personal home drive quota is 250 GB per employee. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Default departmental network share quota.** The default departmental network share quota is 2 TB per department, raised only by an approved capacity request. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**OneDrive storage allocation per licensed user.** The OneDrive storage allocation per licensed user is 5 TB per user. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Second stage recycle bin retention.** The second stage recycle bin retention is 93 days before a deleted item is purged permanently. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Share permission access review cadence.** The share permission access review cadence is every 180 days, signed off by the named data owner. Storage and Collaboration set this figure in consultation with Information Security, and it is reviewed annually.

**Retention period for finance record shares.** The retention period for finance record shares is 1825 days from the end of the financial year the records belong to. Storage and Collaboration set this figure in consultation with Information Security, and it is reviewed annually.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Microsoft SharePoint Online diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Storage and Collaboration, and reviewed annually with Information Security.

## Architecture and dependencies

Microsoft SharePoint Online is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Microsoft SharePoint Online follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Storage and Collaboration maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Storage and Collaboration raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Microsoft SharePoint Online, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Storage and Collaboration implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Storage and Collaboration rather than skipping it.

### Request access to a departmental share

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise an access request in ServiceNow naming the share and the business reason.
2. Allow the request to route to the named data owner for approval.
3. Wait for Storage and Collaboration to add you to the Entra ID access group.
4. Sign out and sign back in so the new group membership is picked up.
5. Confirm you can open the share and report any folder you still cannot read.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Create a new departmental share

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the named data owner and the requested capacity against the default quota.
2. Create the share on the storage platform and apply the default quota.
3. Create the read and read-write Entra ID access groups and apply them to the share.
4. Add the share to the group policy mapping for the department.
5. Record the share, data owner and review date in the ServiceNow configuration item.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Run a share access review

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Export the current membership of every access group attached to the share.
2. Send the membership list to the named data owner with the review deadline.
3. Remove every member the data owner does not reconfirm.
4. Record the signed-off review against the configuration item.
5. Set the next review date in line with the review cadence.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Storage and Collaboration with the diagnostic output attached rather than retrying the same steps.

### Symptom: A user sees an access denied message when opening a departmental share they were just granted.


**Error code:** A-SMB-1326

**Cause.** The group membership has not yet been picked up by the user current sign-in token..

**Resolution.** Ask the user to sign out fully and sign back in, then retry the share. Confirm the membership is present in the Entra ID group before investigating further. Escalate to Storage and Collaboration if access is still denied after a clean sign-in and the membership is confirmed.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: OneDrive shows a paused sync and a red cross on the taskbar icon for one user.


**Error code:** A-ODSYNC-0x8004de40

**Cause.** A file path exceeds the supported length or contains an unsupported character, so the client cannot complete the upload..

**Resolution.** Open the OneDrive activity centre, identify the blocked file and shorten the path or rename the file, then resume sync. Advise the user to keep folder nesting shallow under known folder move. Escalate to Storage and Collaboration if sync stays paused once the reported file is fixed.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: An external partner reports that a SharePoint sharing link does not work for them.


**Error code:** A-SPO-403-19

**Cause.** The link was created as an anonymous link, which is disabled across the tenant..

**Resolution.** Recreate the link as a specific people link addressed to the partner work email so a named guest account is created. Confirm the partner accepts the guest invitation before testing again. Escalate to Information Security if the partner domain is blocked from guest access.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: Users cannot save new files to a departmental share although existing files open normally.


**Error code:** A-NTFS-0x80070052

**Cause.** The share has reached its quota, so writes are refused while reads continue to work..

**Resolution.** Check the share usage against its quota and ask the data owner to archive or delete content that is past its retention point. Raise a capacity request if the department genuinely needs more than the default quota. Escalate to Storage and Collaboration immediately if the share supports a time-critical finance process.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Storage and Collaboration to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A user sees an access denied message when opening a departmental share

Reference: A-SMB-1326.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft SharePoint Online and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Storage and Collaboration citing the reference above.

### Diagnostics for: OneDrive shows a paused sync and a red cross on the taskbar icon for o

Reference: A-ODSYNC-0x8004de40.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft SharePoint Online and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Storage and Collaboration citing the reference above.

### Diagnostics for: An external partner reports that a SharePoint sharing link does not wo

Reference: A-SPO-403-19.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft SharePoint Online and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Storage and Collaboration citing the reference above.

### Diagnostics for: Users cannot save new files to a departmental share although existing 

Reference: A-NTFS-0x80070052.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft SharePoint Online and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Storage and Collaboration citing the reference above.

## Worked examples

### Example: A user sees an access denied message when opening a departmental share

A user at Singapore contacts the service desk reporting that a user sees an access denied message when opening a departmental share they were just granted.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The group membership has not yet been picked up by the user current sign-in token.. Following the documented resolution, ask the user to sign out fully and sign back in, then retry the share. Confirm the membership is present in the Entra ID group before investigating further. Escalate to Storage and Collaboration if access is still denied after a clean sign-in and the membership is confirmed.

The agent records the diagnosis against the ticket, confirms with yusuf.vasquez@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Storage and Collaboration was needed.

### Example: OneDrive shows a paused sync and a red cross on the taskbar icon for o

A user at Singapore contacts the service desk reporting that oneDrive shows a paused sync and a red cross on the taskbar icon for one user.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: A file path exceeds the supported length or contains an unsupported character, so the client cannot complete the upload.. Following the documented resolution, open the OneDrive activity centre, identify the blocked file and shorten the path or rename the file, then resume sync. Advise the user to keep folder nesting shallow under known folder move. Escalate to Storage and Collaboration if sync stays paused once the reported file is fixed.

The agent records the diagnosis against the ticket, confirms with priya.vasquez@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Storage and Collaboration was needed.

### Example: An external partner reports that a SharePoint sharing link does not wo

A user at Singapore contacts the service desk reporting that an external partner reports that a SharePoint sharing link does not work for them.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The link was created as an anonymous link, which is disabled across the tenant.. Following the documented resolution, recreate the link as a specific people link addressed to the partner work email so a named guest account is created. Confirm the partner accepts the guest invitation before testing again. Escalate to Information Security if the partner domain is blocked from guest access.

The agent records the diagnosis against the ticket, confirms with oscar.novak@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Storage and Collaboration was needed.

### Example: request access to a departmental share

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about file shares and storage. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the personal home drive quota is flexible or negotiable per user.**

It is not. The personal home drive quota is 250 GB per employee, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the default departmental network share quota is flexible or negotiable per user.**

It is not. The default departmental network share quota is 2 TB per department, raised only by an approved capacity request, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the OneDrive storage allocation per licensed user is flexible or negotiable per user.**

It is not. The OneDrive storage allocation per licensed user is 5 TB per user, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the second stage recycle bin retention is flexible or negotiable per user.**

It is not. The second stage recycle bin retention is 93 days before a deleted item is purged permanently, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Storage and Collaboration can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to file shares and storage, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Storage and Collaboration.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Microsoft SharePoint Online did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Storage and Collaboration produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about file shares and storage unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Storage and Collaboration runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How much space do I get in OneDrive?**

Each licensed user has 5 TB of OneDrive storage, which is separate from the 250 GB home drive quota.

**Can I recover a file I deleted a month ago?**

Yes, deleted items stay in the second stage recycle bin for 93 days before they are purged permanently.

**How often is my share access checked?**

Share access is reviewed every 180 days and your access is removed if the data owner does not reconfirm it.

**Can I send an open link to someone outside Meridian Group?**

No, anonymous links are disabled, so use a specific people link that creates a named guest account for the recipient.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Storage and Collaboration will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Storage and Collaboration, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Microsoft SharePoint Online, engaged by Storage and Collaboration only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Storage and Collaboration produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about file shares and storage. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Raise an access request in ServiceNow naming the share and the business reason.
- [ ] Allow the request to route to the named data owner for approval.
- [ ] Confirm the named data owner and the requested capacity against the default quota.
- [ ] Create the share on the storage platform and apply the default quota.
- [ ] Export the current membership of every access group attached to the share.
- [ ] Send the membership list to the named data owner with the review deadline.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How much space do I get in OneDrive? Each licensed user has 5 TB of OneDrive storage, which is separate from the 250 GB home drive quota.
- Can I recover a file I deleted a month ago? Yes, deleted items stay in the second stage recycle bin for 93 days before they are purged permanently.
- How often is my share access checked? Share access is reviewed every 180 days and your access is removed if the data owner does not reconfirm it.
- Can I send an open link to someone outside Meridian Group? No, anonymous links are disabled, so use a specific people link that creates a named guest account for the recipient.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Storage and Collaboration | First published version. |
| 1.1 | 2024-11-02 | Storage and Collaboration | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Storage and Collaboration | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Storage and Collaboration | Annual review; figures confirmed against the running configuration of Microsoft SharePoint Online. |
