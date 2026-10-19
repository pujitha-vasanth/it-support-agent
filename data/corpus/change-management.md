---
title: Change Management Policy
doc_type: policy
category: service-management
owner: Change Management Office
version: 2.1
review_date: 2027-02-09
---

# Change Management Policy

Owner: Change Management Office | System of record: ServiceNow Change Management | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages change management. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Change Management Office team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the service-management estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

ServiceNow Change Management is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of ServiceNow Change Management. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Standard change**  
A low risk, repeatable change already assessed and pre-approved as a catalogue item, which does not need Change Advisory Board review. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Freeze period**  
A declared window in which only emergency changes are permitted, protecting the business through year end and financial close. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Rollback plan**  
The documented, tested sequence of steps that returns a service to its prior state if the change fails verification. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Change Management Office. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Change Management Office** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Change Management Office rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. No change may be implemented in production without an approved change record raised before the work starts.

This is enforced technically wherever the platform allows it. This statement has been tested against the current configuration of ServiceNow Change Management. Where a platform change makes it unenforceable, Change Management Office raises a risk acceptance rather than quietly dropping the control. Where the control cannot be enforced technically, Change Management Office monitors for breaches and follows up with the individual and their line manager.

### 2. Every normal and emergency change must carry a rollback plan tested within the last 21 days.

The reasoning behind this is straightforward. Evidence that the control is operating is collected automatically from ServiceNow Change Management and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 3. Changes submitted inside the 7 calendar day lead time are deferred to the following Change Advisory Board unless raised as emergency.

This has been the standing position since the last review. Evidence that the control is operating is collected automatically from ServiceNow Change Management and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Where the control cannot be enforced technically, Change Management Office monitors for breaches and follows up with the individual and their line manager.

### 4. Only emergency changes are permitted during a declared freeze period, and each needs director level approval.

In practice this means the following. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Change Management Office will either confirm the control applies or sponsor an exception, usually within a few working days. Change Management Office reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 5. A change implemented without an approved record is treated as an unauthorised change and raised to the Change Management Office as an incident.

There is a documented exception route, described later in this document. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Change Management Office will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Change Management Office configures in ServiceNow Change Management. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Change types in use | standard, normal and emergency, with standard changes drawn from a pre-approved catalogue |
| Normal change lead time | 7 calendar days before the Change Advisory Board that will review it |
| Change Advisory Board schedule and quorum | Tuesdays at 14:00, requiring 5 voting members present to be quorate |
| Emergency change retrospective deadline | 2 business days after implementation |
| Annual freeze periods | 18 December to 4 January, and the financial year end window of 25 March to 7 April |
| Change success target | 97 per cent of implemented changes closed as successful each quarter |

**Change types in use.** The change types in use is standard, normal and emergency, with standard changes drawn from a pre-approved catalogue. Change Management Office set this figure in consultation with Information Security, and it is reviewed annually.

**Normal change lead time.** The normal change lead time is 7 calendar days before the Change Advisory Board that will review it. Change Management Office set this figure in consultation with Information Security, and it is reviewed annually.

**Change Advisory Board schedule and quorum.** The Change Advisory Board schedule and quorum is Tuesdays at 14:00, requiring 5 voting members present to be quorate. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Emergency change retrospective deadline.** The emergency change retrospective deadline is 2 business days after implementation. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Annual freeze periods.** The annual freeze periods is 18 December to 4 January, and the financial year end window of 25 March to 7 April. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Change success target.** The change success target is 97 per cent of implemented changes closed as successful each quarter. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of ServiceNow Change Management diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Change Management Office, and reviewed annually with Information Security.

## Architecture and dependencies

ServiceNow Change Management is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to ServiceNow Change Management follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Change Management Office maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Change Management Office raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to ServiceNow Change Management, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Change Management Office implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Change Management Office rather than skipping it.

### Submitting a normal change

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise the change record with the affected configuration items and the implementation window.
2. Attach the test evidence and the rollback plan with its most recent test date.
3. Obtain the service owner approval before the record goes to the board.
4. Submit the record at least 7 calendar days before the intended Tuesday board.
5. Present the change at the board and record the decision on the record.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Raising an emergency change

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the change is genuinely required to restore service or remove an active risk.
2. Obtain verbal approval from the duty director and record who gave it.
3. Raise the emergency change record before starting work, even if it is brief.
4. Implement the change with a second engineer observing and verifying.
5. Submit the retrospective to the Change Management Office within 2 business days.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Executing a change rollback

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Declare the change failed as soon as verification testing does not pass.
2. Notify the service desk so user-facing communications can be issued.
3. Execute the documented rollback steps in order without improvising.
4. Verify the service against its pre-change baseline before standing down.
5. Update the change record with the failure reason and close it as unsuccessful.
6. Feed the failure into the quarterly review against the 97 per cent success target.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Change Management Office with the diagnostic output attached rather than retrying the same steps.

### Symptom: A change record will not move to Scheduled and returns D-CHG-2290


**Error code:** D-CHG-2290

**Cause.** The record was submitted inside the 7 calendar day lead time for the selected board date.

**Resolution.** Move the implementation window to the following board cycle, or convert the record to an emergency change if the business case genuinely supports it. Record which option was chosen and why. Escalate to the Change Management Office if the business needs an exception to the lead time.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A board decision cannot be recorded and the meeting shows D-CHG-7715


**Error code:** D-CHG-7715

**Cause.** Fewer than 5 voting members were present, so the board was not quorate.

**Resolution.** Defer the decisions to a reconvened session once quorum is available. Low risk items may instead be reclassified as standard changes if they already exist in the catalogue. Escalate to the Change Management Office if quorum has failed twice in a row.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: An approval request is rejected automatically during December


**Cause.** The implementation date falls inside the 18 December to 4 January freeze period.

**Resolution.** Reschedule the change to begin on or after 5 January. If the work cannot wait, raise it as an emergency change with director level approval and a clear statement of the risk of waiting. Do not attempt to re-date the record to bypass the freeze check.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A change record is blocked at approval with D-CHG-4038


**Error code:** D-CHG-4038

**Cause.** The attached rollback plan has no test date within the last 21 days.

**Resolution.** Re-test the rollback plan in a non-production environment and update the test date on the record. Attach the fresh test evidence before resubmitting for approval. Escalate to the Change Management Office if the plan cannot be tested because no suitable environment exists.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Change Management Office to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A change record will not move to Scheduled and returns D-CHG-2290

Reference: D-CHG-2290.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow Change Management and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Change Management Office citing the reference above.

### Diagnostics for: A board decision cannot be recorded and the meeting shows D-CHG-7715

Reference: D-CHG-7715.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow Change Management and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Change Management Office citing the reference above.

### Diagnostics for: An approval request is rejected automatically during December

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow Change Management and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Change Management Office citing the reference above.

### Diagnostics for: A change record is blocked at approval with D-CHG-4038

Reference: D-CHG-4038.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow Change Management and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Change Management Office citing the reference above.

## Worked examples

### Example: A change record will not move to Scheduled and returns D-CHG-2290

A user at Singapore contacts the service desk reporting that a change record will not move to Scheduled and returns D-CHG-2290. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The record was submitted inside the 7 calendar day lead time for the selected board date. Following the documented resolution, move the implementation window to the following board cycle, or convert the record to an emergency change if the business case genuinely supports it. Record which option was chosen and why. Escalate to the Change Management Office if the business needs an exception to the lead time.

The agent records the diagnosis against the ticket, confirms with renu.chaudhry@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Change Management Office was needed.

### Example: A board decision cannot be recorded and the meeting shows D-CHG-7715

A user at Remote contacts the service desk reporting that a board decision cannot be recorded and the meeting shows D-CHG-7715. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Fewer than 5 voting members were present, so the board was not quorate. Following the documented resolution, defer the decisions to a reconvened session once quorum is available. Low risk items may instead be reclassified as standard changes if they already exist in the catalogue. Escalate to the Change Management Office if quorum has failed twice in a row.

The agent records the diagnosis against the ticket, confirms with rohan.iyer@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Change Management Office was needed.

### Example: An approval request is rejected automatically during December

A user at Manchester contacts the service desk reporting that an approval request is rejected automatically during December. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The implementation date falls inside the 18 December to 4 January freeze period. Following the documented resolution, reschedule the change to begin on or after 5 January. If the work cannot wait, raise it as an emergency change with director level approval and a clear statement of the risk of waiting. Do not attempt to re-date the record to bypass the freeze check.

The agent records the diagnosis against the ticket, confirms with sofia.kowalski@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Change Management Office was needed.

### Example: submitting a normal change

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about change management. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the change types in use is flexible or negotiable per user.**

It is not. The change types in use is standard, normal and emergency, with standard changes drawn from a pre-approved catalogue, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the normal change lead time is flexible or negotiable per user.**

It is not. The normal change lead time is 7 calendar days before the Change Advisory Board that will review it, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the Change Advisory Board schedule and quorum is flexible or negotiable per user.**

It is not. The Change Advisory Board schedule and quorum is Tuesdays at 14:00, requiring 5 voting members present to be quorate, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the emergency change retrospective deadline is flexible or negotiable per user.**

It is not. The emergency change retrospective deadline is 2 business days after implementation, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Change Management Office can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to change management, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Change Management Office.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of ServiceNow Change Management did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Change Management Office produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about change management unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Change Management Office runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How far ahead do I need to submit a normal change?**

At least 7 calendar days before the Tuesday Change Advisory Board that will review it.

**Do standard changes go to the board?**

No. Standard changes come from a pre-approved catalogue and are implemented without board review.

**Can I release during the Christmas freeze?**

Only as an emergency change with director level approval; the freeze runs from 18 December to 4 January.

**How current does my rollback plan have to be?**

It must have been tested within the last 21 days, otherwise approval is blocked.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Change Management Office will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Change Management Office, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for ServiceNow Change Management, engaged by Change Management Office only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Change Management Office produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about change management. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Raise the change record with the affected configuration items and the implementation window.
- [ ] Attach the test evidence and the rollback plan with its most recent test date.
- [ ] Confirm the change is genuinely required to restore service or remove an active risk.
- [ ] Obtain verbal approval from the duty director and record who gave it.
- [ ] Declare the change failed as soon as verification testing does not pass.
- [ ] Notify the service desk so user-facing communications can be issued.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How far ahead do I need to submit a normal change? At least 7 calendar days before the Tuesday Change Advisory Board that will review it.
- Do standard changes go to the board? No. Standard changes come from a pre-approved catalogue and are implemented without board review.
- Can I release during the Christmas freeze? Only as an emergency change with director level approval; the freeze runs from 18 December to 4 January.
- How current does my rollback plan have to be? It must have been tested within the last 21 days, otherwise approval is blocked.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Change Management Office | First published version. |
| 1.1 | 2024-11-02 | Change Management Office | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Change Management Office | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Change Management Office | Annual review; figures confirmed against the running configuration of ServiceNow Change Management. |
