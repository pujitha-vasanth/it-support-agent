---
title: ERP Application Support Runbook
doc_type: runbook
category: applications
owner: ERP Support
version: 2.1
review_date: 2027-02-09
---

# ERP Application Support Runbook

Owner: ERP Support | System of record: SAP S/4HANA | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages ERP application support. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The ERP Support team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the applications estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

SAP S/4HANA is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of SAP S/4HANA. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Transport request**  
A packaged set of configuration or development changes moved in sequence from development through quality assurance to production. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Segregation of duties conflict**  
A role combination that would let one person both create and approve the same transaction, for example raising a purchase order and releasing its payment. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Firefighter access**  
Temporary elevated access granted for an urgent production problem, fully session logged and limited to 90 minutes. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case ERP Support. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**ERP Support** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to ERP Support rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. No configuration or development change reaches production except through an approved transport request.

There is a documented exception route, described later in this document. This statement has been tested against the current configuration of SAP S/4HANA. Where a platform change makes it unenforceable, ERP Support raises a risk acceptance rather than quietly dropping the control. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 2. Transports must be imported in the sequence they were released, never selectively, to avoid overwriting later objects.

Agents should treat this as non-negotiable. ERP Support configures SAP S/4HANA to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. ERP Support reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 3. Role assignments that create a segregation of duties conflict require finance director approval and a compensating control.

This is enforced technically wherever the platform allows it. ERP Support configures SAP S/4HANA to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Where the control cannot be enforced technically, ERP Support monitors for breaches and follows up with the individual and their line manager.

### 4. Firefighter access is granted only against an open incident and its session log is reviewed by ERP Support the next working day.

In practice this means the following. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. ERP Support will either confirm the control applies or sponsor an exception, usually within a few working days. ERP Support reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 5. Interface failures affecting financial postings must be raised to the finance systems lead before the close window ends.

The reasoning behind this is straightforward. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. ERP Support will either confirm the control applies or sponsor an exception, usually within a few working days. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what ERP Support configures in SAP S/4HANA. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Period close support window | the last 3 business days of each month and the first 5 business days of the next, with extended cover from 07:00 to 22:00 |
| Transport approval route | two stage approval, the functional lead followed by the Basis team, before any transport reaches production |
| Transport freeze rule | no transports are released to production at any point inside the period close support window |
| Segregation of duties remediation deadline | 15 business days from the date a conflict is reported on a role assignment |
| Interface monitoring interval | every 8 minutes, with failed documents raised automatically as tickets |
| Maximum firefighter session length | 90 minutes, after which the elevated access is revoked automatically |

**Period close support window.** The period close support window is the last 3 business days of each month and the first 5 business days of the next, with extended cover from 07:00 to 22:00. ERP Support set this figure in consultation with Information Security, and it is reviewed annually.

**Transport approval route.** The transport approval route is two stage approval, the functional lead followed by the Basis team, before any transport reaches production. ERP Support set this figure in consultation with Information Security, and it is reviewed annually.

**Transport freeze rule.** The transport freeze rule is no transports are released to production at any point inside the period close support window. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Segregation of duties remediation deadline.** The segregation of duties remediation deadline is 15 business days from the date a conflict is reported on a role assignment. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Interface monitoring interval.** The interface monitoring interval is every 8 minutes, with failed documents raised automatically as tickets. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Maximum firefighter session length.** The maximum firefighter session length is 90 minutes, after which the elevated access is revoked automatically. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of SAP S/4HANA diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, ERP Support, and reviewed annually with Information Security.

## Architecture and dependencies

SAP S/4HANA is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to SAP S/4HANA follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

ERP Support maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, ERP Support raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to SAP S/4HANA, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. ERP Support implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to ERP Support rather than skipping it.

### Releasing a transport to production

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the change is not inside the period close support window transport freeze.
2. Obtain the functional lead approval on the transport request.
3. Obtain the Basis team approval as the second stage.
4. Import the transport in release sequence and capture the import log.
5. Verify the change in production with the requesting business user.
6. Close the transport record with the import log attached.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Granting firefighter access

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm an open incident exists that genuinely needs elevated access.
2. Obtain approval from the ERP Support lead and record the incident number.
3. Issue the firefighter session with the 90 minute automatic revocation set.
4. Watch the session log while the work is carried out.
5. Review the completed session log on the next working day and attach it to the incident.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Resolving an interface failure

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Open the failed document from the interface monitor that runs every 8 minutes.
2. Identify whether the failure is data, mapping or connectivity related.
3. Correct the source data or mapping, keeping the original document for audit.
4. Reprocess the document and confirm the posting completes.
5. Notify the finance systems lead if the posting affects the current close.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to ERP Support with the diagnostic output attached rather than retrying the same steps.

### Symptom: A transport import is refused and returns D-SAP-M7021


**Error code:** D-SAP-M7021

**Cause.** The import was attempted inside the period close support window, where the transport freeze applies.

**Resolution.** Hold the transport until the close window ends and reschedule the import. If the change is needed to complete the close itself, raise it as an emergency with the finance systems lead and the Basis team. Do not bypass the freeze by importing directly into the production client.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A role assignment is blocked at approval with D-SAP-B4455


**Error code:** D-SAP-B4455

**Cause.** The requested role combination creates a segregation of duties conflict.

**Resolution.** Show the requester the conflicting role pair and offer a split that removes the conflict. If the business genuinely needs both, obtain finance director approval and document a compensating control. The conflict must be remediated or formally accepted within 15 business days.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: Inbound documents stop posting and the monitor logs D-SAP-I9308


**Error code:** D-SAP-I9308

**Cause.** The interface partner profile is pointing at a connection that is no longer reachable.

**Resolution.** Test the connection from the Basis console and confirm the target host and port. Correct the partner profile, then reprocess the queued documents in the order they arrived. Escalate to the Basis team if the connection test still fails, and tell the finance systems lead if any failed posting falls inside the close.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A user's elevated access disappears while they are mid-task


**Cause.** The firefighter session reached its 90 minute limit and was revoked automatically.

**Resolution.** Confirm the incident is still open, then issue a fresh firefighter session with a new approval. Ask the user to record progress in the incident so the next session is shorter. Escalate to the ERP Support lead if a single task has needed more than two firefighter sessions.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for ERP Support to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A transport import is refused and returns D-SAP-M7021

Reference: D-SAP-M7021.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of SAP S/4HANA and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to ERP Support citing the reference above.

### Diagnostics for: A role assignment is blocked at approval with D-SAP-B4455

Reference: D-SAP-B4455.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of SAP S/4HANA and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to ERP Support citing the reference above.

### Diagnostics for: Inbound documents stop posting and the monitor logs D-SAP-I9308

Reference: D-SAP-I9308.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of SAP S/4HANA and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to ERP Support citing the reference above.

### Diagnostics for: A user's elevated access disappears while they are mid-task

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of SAP S/4HANA and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to ERP Support citing the reference above.

## Worked examples

### Example: A transport import is refused and returns D-SAP-M7021

A user at Manchester contacts the service desk reporting that a transport import is refused and returns D-SAP-M7021. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The import was attempted inside the period close support window, where the transport freeze applies. Following the documented resolution, hold the transport until the close window ends and reschedule the import. If the change is needed to complete the close itself, raise it as an emergency with the finance systems lead and the Basis team. Do not bypass the freeze by importing directly into the production client.

The agent records the diagnosis against the ticket, confirms with mira.bell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to ERP Support was needed.

### Example: A role assignment is blocked at approval with D-SAP-B4455

A user at London HQ contacts the service desk reporting that a role assignment is blocked at approval with D-SAP-B4455. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The requested role combination creates a segregation of duties conflict. Following the documented resolution, show the requester the conflicting role pair and offer a split that removes the conflict. If the business genuinely needs both, obtain finance director approval and document a compensating control. The conflict must be remediated or formally accepted within 15 business days.

The agent records the diagnosis against the ticket, confirms with elena.mehta@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to ERP Support was needed.

### Example: Inbound documents stop posting and the monitor logs D-SAP-I9308

A user at Manchester contacts the service desk reporting that inbound documents stop posting and the monitor logs D-SAP-I9308. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The interface partner profile is pointing at a connection that is no longer reachable. Following the documented resolution, test the connection from the Basis console and confirm the target host and port. Correct the partner profile, then reprocess the queued documents in the order they arrived. Escalate to the Basis team if the connection test still fails, and tell the finance systems lead if any failed posting falls inside the close.

The agent records the diagnosis against the ticket, confirms with arjun.vasquez@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to ERP Support was needed.

### Example: releasing a transport to production

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about ERP application support. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the period close support window is flexible or negotiable per user.**

It is not. The period close support window is the last 3 business days of each month and the first 5 business days of the next, with extended cover from 07:00 to 22:00, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the transport approval route is flexible or negotiable per user.**

It is not. The transport approval route is two stage approval, the functional lead followed by the Basis team, before any transport reaches production, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the transport freeze rule is flexible or negotiable per user.**

It is not. The transport freeze rule is no transports are released to production at any point inside the period close support window, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the segregation of duties remediation deadline is flexible or negotiable per user.**

It is not. The segregation of duties remediation deadline is 15 business days from the date a conflict is reported on a role assignment, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: ERP Support can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to ERP application support, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to ERP Support.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of SAP S/4HANA did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, ERP Support produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about ERP application support unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

ERP Support runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Can a transport go live during month end close?**

No. No transports are released to production inside the period close support window.

**Who approves a transport?**

Two approvers in sequence: the functional lead, then the Basis team.

**How long does firefighter access last?**

90 minutes, after which the elevated access is revoked automatically.

**How quickly are interface failures spotted?**

The interface monitor runs every 8 minutes and raises failed documents automatically as tickets.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, ERP Support will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is ERP Support, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for SAP S/4HANA, engaged by ERP Support only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

ERP Support produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about ERP application support. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the change is not inside the period close support window transport freeze.
- [ ] Obtain the functional lead approval on the transport request.
- [ ] Confirm an open incident exists that genuinely needs elevated access.
- [ ] Obtain approval from the ERP Support lead and record the incident number.
- [ ] Open the failed document from the interface monitor that runs every 8 minutes.
- [ ] Identify whether the failure is data, mapping or connectivity related.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Can a transport go live during month end close? No. No transports are released to production inside the period close support window.
- Who approves a transport? Two approvers in sequence: the functional lead, then the Basis team.
- How long does firefighter access last? 90 minutes, after which the elevated access is revoked automatically.
- How quickly are interface failures spotted? The interface monitor runs every 8 minutes and raises failed documents automatically as tickets.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | ERP Support | First published version. |
| 1.1 | 2024-11-02 | ERP Support | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | ERP Support | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | ERP Support | Annual review; figures confirmed against the running configuration of SAP S/4HANA. |
