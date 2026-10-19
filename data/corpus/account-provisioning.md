---
title: User Account Provisioning Runbook
doc_type: runbook
category: access
owner: Identity and Access Management
version: 2.1
review_date: 2027-02-09
---

# User Account Provisioning Runbook

Owner: Identity and Access Management | System of record: Entra ID | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages user account provisioning. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Identity and Access Management team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the access estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Entra ID is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Entra ID. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Role package**  
A bundle of directory groups mapped to one job role, assigned as a single unit so that joiners receive a consistent baseline. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Access recertification**  
A scheduled review in which a named group owner confirms, line by line, that each member still needs the access. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Dormant account**  
An enabled account that has recorded no interactive sign-in for 45 consecutive days and is therefore a standing security risk. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Identity and Access Management. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Identity and Access Management** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Identity and Access Management rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. No account is created without an approved joiner request that names the line manager and the start date.

In practice this means the following. Identity and Access Management configures Entra ID to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 2. Shared or generic user accounts are prohibited; every account maps to one identifiable person.

The reasoning behind this is straightforward. Evidence that the control is operating is collected automatically from Entra ID and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Identity and Access Management reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 3. Group ownership must be held by a named individual, never by a distribution list or a team mailbox.

This is enforced technically wherever the platform allows it. Evidence that the control is operating is collected automatically from Entra ID and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 4. Access granted outside a role package must carry a written business justification stored against the request.

There is a documented exception route, described later in this document. Evidence that the control is operating is collected automatically from Entra ID and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 5. A group owner who fails to complete recertification within the 120 day cycle has the group placed in read-only mode until the review is closed.

This has been the standing position since the last review. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Identity and Access Management will either confirm the control applies or sponsor an exception, usually within a few working days. Where the control cannot be enforced technically, Identity and Access Management monitors for breaches and follows up with the individual and their line manager.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Identity and Access Management configures in Entra ID. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Account creation target | 4 business hours from receipt of an approved joiner request |
| Standard account naming format | firstname.lastname@meridiangroup.example, with a numeric suffix such as .2 only when the name already exists |
| Access recertification cycle | every 120 days for every directory group that grants application access |
| Dormant account disable threshold | 45 consecutive days without an interactive sign-in |
| Maximum direct group memberships per user | 60 groups, above which access must be granted through a role package |
| Leaver account deletion point | 35 days after the account is disabled, once the mailbox export is confirmed |

**Account creation target.** The account creation target is 4 business hours from receipt of an approved joiner request. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Standard account naming format.** The standard account naming format is firstname.lastname@meridiangroup.example, with a numeric suffix such as .2 only when the name already exists. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Access recertification cycle.** The access recertification cycle is every 120 days for every directory group that grants application access. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Dormant account disable threshold.** The dormant account disable threshold is 45 consecutive days without an interactive sign-in. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Maximum direct group memberships per user.** The maximum direct group memberships per user is 60 groups, above which access must be granted through a role package. This is configured centrally in Entra ID and is not adjustable per user or per team.

**Leaver account deletion point.** The leaver account deletion point is 35 days after the account is disabled, once the mailbox export is confirmed. This is configured centrally in Entra ID and is not adjustable per user or per team.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Entra ID diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Identity and Access Management, and reviewed annually with Information Security.

## Architecture and dependencies

Entra ID is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Entra ID follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Identity and Access Management maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Identity and Access Management raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Entra ID, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Identity and Access Management implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Identity and Access Management rather than skipping it.

### Provisioning a new joiner account

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the joiner record in the HR feed shows an approved start date and a populated job role.
2. Create the account in Entra ID using the firstname.lastname naming format.
3. Assign the role package that matches the job role rather than individual groups.
4. Issue the temporary password through the line manager, never directly to the joiner.
5. Confirm the user completes multi-factor authentication registration before the first working day.
6. Close the request with the account name and the role package recorded in the work notes.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Adding a user to a directory group

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Check whether the required access is already covered by an existing role package.
2. Raise the request in the service portal and route it to the named group owner for approval.
3. Verify the user is below the 60 direct membership limit before adding the group.
4. Add the membership and record the business justification against the request.
5. Flag the membership for review at the next 120 day recertification cycle.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Processing a leaver

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Disable the account in Entra ID on the confirmed last working day.
2. Revoke all active sessions and refresh tokens so existing logins drop immediately.
3. Remove the user from every directory group and transfer any group ownership to the line manager.
4. Place the mailbox on hold and export it to the archive store.
5. Delete the account 35 days after disable, once the mailbox export is confirmed.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Identity and Access Management with the diagnostic output attached rather than retrying the same steps.

### Symptom: A newly created account cannot sign in and the portal returns D-ENT-4412


**Error code:** D-ENT-4412

**Cause.** The licence assignment has not yet replicated, so the account exists in the directory but has no service plan attached.

**Resolution.** Open the account in the admin centre and confirm a licence is assigned, then force a licence reprocess and wait 15 minutes. Ask the user to retry in a private browser window. If the error persists beyond one hour, escalate to Identity and Access Management with the account name and the request number.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: Adding a user to a group fails with D-ENT-7190


**Error code:** D-ENT-7190

**Cause.** The user has reached the 60 direct group membership limit.

**Resolution.** Review the user's memberships and remove any that are already covered by their role package. If all 60 are genuinely needed, migrate the user onto a role package and raise a design request to Identity and Access Management rather than forcing more direct grants.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A returning employee finds their account disabled


**Cause.** The account crossed the 45 day dormant threshold while the employee was on extended leave.

**Resolution.** Confirm the employment record is still active in the HR feed, then re-enable the account and reset the password through the line manager. Ask the user to re-register multi-factor authentication if more than one method has lapsed. Record the re-enablement against the original joiner request.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A group owner reports they cannot add members and see D-ENT-2065


**Error code:** D-ENT-2065

**Cause.** The group is in read-only mode because its recertification was not completed inside the 120 day cycle.

**Resolution.** Tell the owner to complete the outstanding recertification in the access review portal. Read-only mode lifts automatically within one hour of the review closing. If the owner has left the business, escalate to Identity and Access Management to reassign ownership.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Identity and Access Management to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A newly created account cannot sign in and the portal returns D-ENT-44

Reference: D-ENT-4412.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Entra ID and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Identity and Access Management citing the reference above.

### Diagnostics for: Adding a user to a group fails with D-ENT-7190

Reference: D-ENT-7190.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Entra ID and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Identity and Access Management citing the reference above.

### Diagnostics for: A returning employee finds their account disabled

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Entra ID and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Identity and Access Management citing the reference above.

### Diagnostics for: A group owner reports they cannot add members and see D-ENT-2065

Reference: D-ENT-2065.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Entra ID and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Identity and Access Management citing the reference above.

## Worked examples

### Example: A newly created account cannot sign in and the portal returns D-ENT-44

A user at London HQ contacts the service desk reporting that a newly created account cannot sign in and the portal returns D-ENT-4412. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The licence assignment has not yet replicated, so the account exists in the directory but has no service plan attached. Following the documented resolution, open the account in the admin centre and confirm a licence is assigned, then force a licence reprocess and wait 15 minutes. Ask the user to retry in a private browser window. If the error persists beyond one hour, escalate to Identity and Access Management with the account name and the request number.

The agent records the diagnosis against the ticket, confirms with beatrix.bell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Identity and Access Management was needed.

### Example: Adding a user to a group fails with D-ENT-7190

A user at Dublin contacts the service desk reporting that adding a user to a group fails with D-ENT-7190. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The user has reached the 60 direct group membership limit. Following the documented resolution, review the user's memberships and remove any that are already covered by their role package. If all 60 are genuinely needed, migrate the user onto a role package and raise a design request to Identity and Access Management rather than forcing more direct grants.

The agent records the diagnosis against the ticket, confirms with ingrid.whitfield@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Identity and Access Management was needed.

### Example: A returning employee finds their account disabled

A user at London HQ contacts the service desk reporting that a returning employee finds their account disabled. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The account crossed the 45 day dormant threshold while the employee was on extended leave. Following the documented resolution, confirm the employment record is still active in the HR feed, then re-enable the account and reset the password through the line manager. Ask the user to re-register multi-factor authentication if more than one method has lapsed. Record the re-enablement against the original joiner request.

The agent records the diagnosis against the ticket, confirms with samir.nakamura@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Identity and Access Management was needed.

### Example: provisioning a new joiner account

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about user account provisioning. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the account creation target is flexible or negotiable per user.**

It is not. The account creation target is 4 business hours from receipt of an approved joiner request, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the standard account naming format is flexible or negotiable per user.**

It is not. The standard account naming format is firstname.lastname@meridiangroup.example, with a numeric suffix such as .2 only when the name already exists, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the access recertification cycle is flexible or negotiable per user.**

It is not. The access recertification cycle is every 120 days for every directory group that grants application access, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the dormant account disable threshold is flexible or negotiable per user.**

It is not. The dormant account disable threshold is 45 consecutive days without an interactive sign-in, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Identity and Access Management can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to user account provisioning, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Identity and Access Management.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Entra ID did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Identity and Access Management produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about user account provisioning unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Identity and Access Management runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How quickly will a new starter get their account?**

Within 4 business hours of an approved joiner request reaching Identity and Access Management.

**What will my username be?**

firstname.lastname@meridiangroup.example, with a numeric suffix only if that name is already taken.

**My account was disabled while I was on leave, why?**

Accounts with no interactive sign-in for 45 consecutive days are disabled automatically; the service desk can re-enable it once your employment record is confirmed.

**How often do group owners have to review access?**

Every 120 days, and the group becomes read-only until an overdue review is closed.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Identity and Access Management will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Identity and Access Management, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Entra ID, engaged by Identity and Access Management only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Identity and Access Management produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about user account provisioning. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the joiner record in the HR feed shows an approved start date and a populated job role.
- [ ] Create the account in Entra ID using the firstname.lastname naming format.
- [ ] Check whether the required access is already covered by an existing role package.
- [ ] Raise the request in the service portal and route it to the named group owner for approval.
- [ ] Disable the account in Entra ID on the confirmed last working day.
- [ ] Revoke all active sessions and refresh tokens so existing logins drop immediately.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How quickly will a new starter get their account? Within 4 business hours of an approved joiner request reaching Identity and Access Management.
- What will my username be? firstname.lastname@meridiangroup.example, with a numeric suffix only if that name is already taken.
- My account was disabled while I was on leave, why? Accounts with no interactive sign-in for 45 consecutive days are disabled automatically; the service desk can re-enable it once your employment record is confirmed.
- How often do group owners have to review access? Every 120 days, and the group becomes read-only until an overdue review is closed.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Identity and Access Management | First published version. |
| 1.1 | 2024-11-02 | Identity and Access Management | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Identity and Access Management | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Identity and Access Management | Annual review; figures confirmed against the running configuration of Entra ID. |
