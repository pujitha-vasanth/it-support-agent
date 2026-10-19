---
title: Leaver Offboarding Runbook
doc_type: runbook
category: workplace
owner: Identity Operations
version: 2.1
review_date: 2027-02-09
---

# Leaver Offboarding Runbook

Owner: Identity Operations | System of record: ServiceNow HR Service Delivery | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages leaver offboarding. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Identity Operations team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the workplace estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

ServiceNow HR Service Delivery is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of ServiceNow HR Service Delivery. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Shared mailbox conversion**  
The step that turns a departed user's mailbox into a licence-free shared mailbox so the line manager can still read historic mail. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Immediate dismissal path**  
The accelerated offboarding route triggered directly by Human Resources, where access is cut before the standard ticket is raised. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Data handover confirmation**  
The line manager's signed statement in ServiceNow that all business files and records held by the leaver have been transferred. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Identity Operations. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Identity Operations** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Identity Operations rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Interactive access for a standard leaver is revoked within 45 minutes of the recorded leaving time, with no grace period.

This has been the standing position since the last review. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Identity Operations will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 2. A leaver's mailbox is never deleted on the leaving date; it is converted to a shared mailbox and retained for 13 months.

This is enforced technically wherever the platform allows it. Identity Operations configures ServiceNow HR Service Delivery to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 3. Line managers must confirm data handover in ServiceNow within 6 working days of the leaving date.

Agents should treat this as non-negotiable. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Identity Operations will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 4. Equipment not returned within 21 calendar days is recharged to the leaver's cost centre at full replacement value.

In practice this means the following. Evidence that the control is operating is collected automatically from ServiceNow HR Service Delivery and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Identity Operations reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 5. Personal data held in a leaver's profile is not forwarded to any third party, including the leaver, without Information Security approval.

The reasoning behind this is straightforward. This statement has been tested against the current configuration of ServiceNow HR Service Delivery. Where a platform change makes it unenforceable, Identity Operations raises a risk acceptance rather than quietly dropping the control. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Identity Operations configures in ServiceNow HR Service Delivery. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Access revocation timing for a standard leaver | all interactive access is disabled within 45 minutes of the recorded leaving time |
| Access revocation timing for an immediate dismissal | within 8 minutes of the Human Resources instruction, ahead of any ticket being raised |
| Mailbox retention after departure | converted to a shared mailbox for 13 months, then permanently deleted |
| Equipment return deadline | 14 calendar days from the leaving date, tracked against the asset record |
| Unreturned equipment recharge | the full replacement value is recharged to the leaver's cost centre after 21 calendar days |
| Data handover owner | the line manager, who must confirm handover in ServiceNow within 6 working days of the leaving date |

**Access revocation timing for a standard leaver.** The access revocation timing for a standard leaver is all interactive access is disabled within 45 minutes of the recorded leaving time. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Access revocation timing for an immediate dismissal.** The access revocation timing for an immediate dismissal is within 8 minutes of the Human Resources instruction, ahead of any ticket being raised. This is configured centrally in ServiceNow HR Service Delivery and is not adjustable per user or per team.

**Mailbox retention after departure.** The mailbox retention after departure is converted to a shared mailbox for 13 months, then permanently deleted. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Equipment return deadline.** The equipment return deadline is 14 calendar days from the leaving date, tracked against the asset record. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Unreturned equipment recharge.** The unreturned equipment recharge is the full replacement value is recharged to the leaver's cost centre after 21 calendar days. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Data handover owner.** The data handover owner is the line manager, who must confirm handover in ServiceNow within 6 working days of the leaving date. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of ServiceNow HR Service Delivery diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Identity Operations, and reviewed annually with Information Security.

## Architecture and dependencies

ServiceNow HR Service Delivery is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to ServiceNow HR Service Delivery follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Identity Operations maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Identity Operations raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to ServiceNow HR Service Delivery, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Identity Operations implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Identity Operations rather than skipping it.

### Offboarding a standard leaver

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the leaving date and time on the ServiceNow offboarding record.
2. Disable the Entra ID account and revoke all active sign-in sessions and refresh tokens.
3. Convert the mailbox to a shared mailbox and grant the line manager read access.
4. Reclaim all assigned software licences back to the central pool.
5. Issue the equipment return pack with the 14 calendar day deadline stated.
6. Close the record once the line manager has confirmed data handover.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Executing an immediate dismissal

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Accept the instruction directly from Human Resources without waiting for a ticket.
2. Disable the account and revoke all sessions within 8 minutes of the instruction.
3. Suspend building access and remove the user from all privileged groups.
4. Preserve the mailbox and files in place and notify Information Security.
5. Raise the retrospective offboarding record and attach the Human Resources instruction.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Chasing unreturned equipment

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Check the asset record on day 14 after the leaving date.
2. Send the first reminder to the leaver's personal contact address held by Human Resources.
3. Notify the line manager and the cost centre owner on day 18.
4. Raise the recharge to the cost centre at full replacement value on day 21.
5. Mark the asset as written off and update the asset register.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Identity Operations with the diagnostic output attached rather than retrying the same steps.

### Symptom: A leaver can still open email on a mobile phone hours after their account was disabled


**Error code:** C-OFF-5218

**Cause.** The refresh token on the mobile client was never revoked, so the app keeps renewing access.

**Resolution.** Revoke all sessions and refresh tokens for the account, then wipe the corporate mail profile from the device through the management console. Confirm the next mail sync fails. Escalate to Information Security if the leaver was an immediate dismissal case.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: The line manager reports they cannot read the leaver's mailbox


**Error code:** C-OFF-0x8004010F

**Cause.** The mailbox was disabled rather than converted to a shared mailbox, so no delegate permission exists.

**Resolution.** Reconnect the mailbox, convert it to a shared mailbox and grant the line manager read access. Confirm the manager can open it before closing the ticket. If the mailbox is already past the 13 month retention point, escalate to Information Security rather than attempting a recovery.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A shared drive folder is left with no owner after a departure


**Error code:** C-OFF-6604

**Cause.** Data handover was not confirmed within the 6 working day window, so ownership was never reassigned.

**Resolution.** Assign temporary ownership to the line manager and ask them to complete the data handover confirmation in ServiceNow. Reassign permanent ownership to the named successor once identified. Escalate to the departmental head if the manager does not respond within 2 working days.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: The offboarding record cannot be closed


**Cause.** The data handover confirmation is still outstanding from the line manager.

**Resolution.** Contact the line manager, explain that closure is blocked and ask them to complete the confirmation in ServiceNow. Keep the record open rather than force closing it. Escalate to Human Resources if the leaving date was more than 6 working days ago.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Identity Operations to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A leaver can still open email on a mobile phone hours after their acco

Reference: C-OFF-5218.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow HR Service Delivery and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Identity Operations citing the reference above.

### Diagnostics for: The line manager reports they cannot read the leaver's mailbox

Reference: C-OFF-0x8004010F.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow HR Service Delivery and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Identity Operations citing the reference above.

### Diagnostics for: A shared drive folder is left with no owner after a departure

Reference: C-OFF-6604.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow HR Service Delivery and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Identity Operations citing the reference above.

### Diagnostics for: The offboarding record cannot be closed

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow HR Service Delivery and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Identity Operations citing the reference above.

## Worked examples

### Example: A leaver can still open email on a mobile phone hours after their acco

A user at Manchester contacts the service desk reporting that a leaver can still open email on a mobile phone hours after their account was disabled. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The refresh token on the mobile client was never revoked, so the app keeps renewing access. Following the documented resolution, revoke all sessions and refresh tokens for the account, then wipe the corporate mail profile from the device through the management console. Confirm the next mail sync fails. Escalate to Information Security if the leaver was an immediate dismissal case.

The agent records the diagnosis against the ticket, confirms with leila.haddad@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Identity Operations was needed.

### Example: The line manager reports they cannot read the leaver's mailbox

A user at Singapore contacts the service desk reporting that the line manager reports they cannot read the leaver's mailbox. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The mailbox was disabled rather than converted to a shared mailbox, so no delegate permission exists. Following the documented resolution, reconnect the mailbox, convert it to a shared mailbox and grant the line manager read access. Confirm the manager can open it before closing the ticket. If the mailbox is already past the 13 month retention point, escalate to Information Security rather than attempting a recovery.

The agent records the diagnosis against the ticket, confirms with hana.bergmann@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Identity Operations was needed.

### Example: A shared drive folder is left with no owner after a departure

A user at Rotterdam contacts the service desk reporting that a shared drive folder is left with no owner after a departure. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Data handover was not confirmed within the 6 working day window, so ownership was never reassigned. Following the documented resolution, assign temporary ownership to the line manager and ask them to complete the data handover confirmation in ServiceNow. Reassign permanent ownership to the named successor once identified. Escalate to the departmental head if the manager does not respond within 2 working days.

The agent records the diagnosis against the ticket, confirms with sofia.lindqvist@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Identity Operations was needed.

### Example: offboarding a standard leaver

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about leaver offboarding. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the access revocation timing for a standard leaver is flexible or negotiable per user.**

It is not. The access revocation timing for a standard leaver is all interactive access is disabled within 45 minutes of the recorded leaving time, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the access revocation timing for an immediate dismissal is flexible or negotiable per user.**

It is not. The access revocation timing for an immediate dismissal is within 8 minutes of the Human Resources instruction, ahead of any ticket being raised, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the mailbox retention after departure is flexible or negotiable per user.**

It is not. The mailbox retention after departure is converted to a shared mailbox for 13 months, then permanently deleted, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the equipment return deadline is flexible or negotiable per user.**

It is not. The equipment return deadline is 14 calendar days from the leaving date, tracked against the asset record, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Identity Operations can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to leaver offboarding, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Identity Operations.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of ServiceNow HR Service Delivery did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Identity Operations produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about leaver offboarding unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Identity Operations runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How quickly is a leaver's access removed?**

Within 45 minutes of the recorded leaving time for a standard leaver, or within 8 minutes of the Human Resources instruction for an immediate dismissal.

**What happens to a leaver's email?**

It is converted to a shared mailbox that the line manager can read, and it is retained for 13 months before permanent deletion.

**When does unreturned equipment get charged back?**

After 21 calendar days, when the full replacement value is recharged to the leaver's cost centre.

**Who is responsible for data handover?**

The line manager, who must confirm it in ServiceNow within 6 working days of the leaving date.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Identity Operations will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Identity Operations, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for ServiceNow HR Service Delivery, engaged by Identity Operations only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Identity Operations produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about leaver offboarding. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the leaving date and time on the ServiceNow offboarding record.
- [ ] Disable the Entra ID account and revoke all active sign-in sessions and refresh tokens.
- [ ] Accept the instruction directly from Human Resources without waiting for a ticket.
- [ ] Disable the account and revoke all sessions within 8 minutes of the instruction.
- [ ] Check the asset record on day 14 after the leaving date.
- [ ] Send the first reminder to the leaver's personal contact address held by Human Resources.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How quickly is a leaver's access removed? Within 45 minutes of the recorded leaving time for a standard leaver, or within 8 minutes of the Human Resources instruction for an immediate dismissal.
- What happens to a leaver's email? It is converted to a shared mailbox that the line manager can read, and it is retained for 13 months before permanent deletion.
- When does unreturned equipment get charged back? After 21 calendar days, when the full replacement value is recharged to the leaver's cost centre.
- Who is responsible for data handover? The line manager, who must confirm it in ServiceNow within 6 working days of the leaving date.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Identity Operations | First published version. |
| 1.1 | 2024-11-02 | Identity Operations | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Identity Operations | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Identity Operations | Annual review; figures confirmed against the running configuration of ServiceNow HR Service Delivery. |
