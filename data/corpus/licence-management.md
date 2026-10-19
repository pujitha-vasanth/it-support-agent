---
title: Software Licence Management Policy
doc_type: policy
category: software
owner: IT Asset Management
version: 2.1
review_date: 2027-02-09
---

# Software Licence Management Policy

Owner: IT Asset Management | System of record: Flexera One | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages software licence management. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The IT Asset Management team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the software estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Flexera One is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Flexera One. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Licence pool**  
The central allocation of purchased seats for one product, from which individual assignments are drawn and to which reclaimed seats return. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**True-up**  
The annual reconciliation that reports actual deployed seats against the contracted entitlement and settles any shortfall. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Harvesting**  
The automated removal of a licence from a user who has not signed in to the application within the inactivity threshold. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case IT Asset Management. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**IT Asset Management** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to IT Asset Management rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Software may only be assigned from a managed licence pool recorded in Flexera One.

Agents should treat this as non-negotiable. This statement has been tested against the current configuration of Flexera One. Where a platform change makes it unenforceable, IT Asset Management raises a risk acceptance rather than quietly dropping the control. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 2. Licences unused for 52 consecutive days are harvested automatically and returned to the pool.

This has been the standing position since the last review. Evidence that the control is operating is collected automatically from Flexera One and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Where the control cannot be enforced technically, IT Asset Management monitors for breaches and follows up with the individual and their line manager.

### 3. Each licence pool must retain between 3 and 6 per cent spare seats so that new joiners can be provisioned without a purchase.

In practice this means the following. Evidence that the control is operating is collected automatically from Flexera One and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. IT Asset Management reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 4. Business units are recharged monthly for the seats assigned to their cost centre on the last day of the prior month.

There is a documented exception route, described later in this document. IT Asset Management configures Flexera One to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 5. No team may purchase software directly; all purchases are routed through IT Asset Management.

The reasoning behind this is straightforward. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. IT Asset Management will either confirm the control applies or sponsor an exception, usually within a few working days. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what IT Asset Management configures in Flexera One. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Inactivity threshold before a licence is reclaimed | 52 consecutive days without a sign-in to the licensed application |
| Reclaim warning notice | a single email warning sent 9 days before the licence is removed |
| Licence pool headroom target | between 3 and 6 per cent spare seats held in each pool |
| Annual true-up submission date | 15 February each year, covering the preceding calendar year |
| Cost centre recharge cycle | recharged monthly on the 4th working day, based on seats assigned on the last day of the prior month |
| Approval route for a premium licence tier | line manager approval plus IT Asset Management review, with a 2 working day turnaround |

**Inactivity threshold before a licence is reclaimed.** The inactivity threshold before a licence is reclaimed is 52 consecutive days without a sign-in to the licensed application. IT Asset Management set this figure in consultation with Information Security, and it is reviewed annually.

**Reclaim warning notice.** The reclaim warning notice is a single email warning sent 9 days before the licence is removed. IT Asset Management set this figure in consultation with Information Security, and it is reviewed annually.

**Licence pool headroom target.** The licence pool headroom target is between 3 and 6 per cent spare seats held in each pool. This is configured centrally in Flexera One and is not adjustable per user or per team.

**Annual true-up submission date.** The annual true-up submission date is 15 February each year, covering the preceding calendar year. This is configured centrally in Flexera One and is not adjustable per user or per team.

**Cost centre recharge cycle.** The cost centre recharge cycle is recharged monthly on the 4th working day, based on seats assigned on the last day of the prior month. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Approval route for a premium licence tier.** The approval route for a premium licence tier is line manager approval plus IT Asset Management review, with a 2 working day turnaround. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Flexera One diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, IT Asset Management, and reviewed annually with Information Security.

## Architecture and dependencies

Flexera One is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Flexera One follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

IT Asset Management maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, IT Asset Management raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Flexera One, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. IT Asset Management implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to IT Asset Management rather than skipping it.

### Assigning a licence from a pool

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Check available headroom for the product in Flexera One.
2. Confirm the requester's cost centre on the HR record.
3. Assign the seat and record the cost centre against the assignment.
4. Trigger the application entitlement so the user can sign in.
5. Update the recharge schedule so the seat appears in the next monthly cycle.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Running the monthly harvesting cycle

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Export the sign-in activity report for every managed product.
2. Flag every assignment with no sign-in for 52 consecutive days.
3. Send the single warning email 9 days before removal.
4. Remove the licence from any user who has still not signed in after the warning period.
5. Return the reclaimed seats to the pool and confirm headroom is back within the 3 to 6 per cent target.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Preparing the annual true-up

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Freeze the deployment position on 31 December and export the entitlement report.
2. Reconcile deployed seats against the contracted entitlement for each product.
3. Document any shortfall with the month in which it first occurred.
4. Obtain finance sign-off on the shortfall value.
5. Submit the completed true-up to the vendor by 15 February.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to IT Asset Management with the diagnostic output attached rather than retrying the same steps.

### Symptom: A user reports the application has stopped opening and asks for their licence back


**Error code:** C-LIC-3391

**Cause.** The licence was harvested after 52 consecutive days without a sign-in.

**Resolution.** Confirm the harvesting date in Flexera One, reassign a seat from the pool and ask the user to sign in within the next hour so the assignment holds. Explain the inactivity threshold so it does not recur. Escalate to IT Asset Management if no headroom is available in that pool.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A new joiner cannot be given a seat for a core product


**Error code:** C-LIC-0x80070520

**Cause.** The pool has fallen below the 3 per cent headroom floor, so there are no spare seats.

**Resolution.** Run an immediate harvesting pass on that product to recover inactive seats, then assign from the recovered seats. If headroom is still below the floor, raise a purchase request to IT Asset Management the same day. Do not borrow a seat from another business unit's allocation.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A cost centre owner disputes their monthly recharge


**Error code:** C-LIC-8847

**Cause.** The recharge is based on seats assigned on the last day of the prior month, so mid-month leavers still appear.

**Resolution.** Pull the assignment snapshot for the last day of the prior month and walk the owner through it line by line. Confirm any genuinely wrong assignment and correct it in the following cycle. Escalate to finance only if the correction exceeds a full month of charges.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: The premium tier request has not been actioned after four days


**Cause.** The request is waiting at the line manager approval step and has not reached IT Asset Management review.

**Resolution.** Check the approval queue, remind the line manager and confirm the 2 working day review turnaround only starts once their approval lands. Reassign the approval if the manager is on leave. Escalate to the departmental head if the request has been pending for more than 5 working days.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for IT Asset Management to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A user reports the application has stopped opening and asks for their 

Reference: C-LIC-3391.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Flexera One and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to IT Asset Management citing the reference above.

### Diagnostics for: A new joiner cannot be given a seat for a core product

Reference: C-LIC-0x80070520.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Flexera One and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to IT Asset Management citing the reference above.

### Diagnostics for: A cost centre owner disputes their monthly recharge

Reference: C-LIC-8847.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Flexera One and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to IT Asset Management citing the reference above.

### Diagnostics for: The premium tier request has not been actioned after four days

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Flexera One and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to IT Asset Management citing the reference above.

## Worked examples

### Example: A user reports the application has stopped opening and asks for their 

A user at Manchester contacts the service desk reporting that a user reports the application has stopped opening and asks for their licence back. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The licence was harvested after 52 consecutive days without a sign-in. Following the documented resolution, confirm the harvesting date in Flexera One, reassign a seat from the pool and ask the user to sign in within the next hour so the assignment holds. Explain the inactivity threshold so it does not recur. Escalate to IT Asset Management if no headroom is available in that pool.

The agent records the diagnosis against the ticket, confirms with arjun.whitfield@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to IT Asset Management was needed.

### Example: A new joiner cannot be given a seat for a core product

A user at Manchester contacts the service desk reporting that a new joiner cannot be given a seat for a core product. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The pool has fallen below the 3 per cent headroom floor, so there are no spare seats. Following the documented resolution, run an immediate harvesting pass on that product to recover inactive seats, then assign from the recovered seats. If headroom is still below the floor, raise a purchase request to IT Asset Management the same day. Do not borrow a seat from another business unit's allocation.

The agent records the diagnosis against the ticket, confirms with tariq.farouk@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to IT Asset Management was needed.

### Example: A cost centre owner disputes their monthly recharge

A user at Remote contacts the service desk reporting that a cost centre owner disputes their monthly recharge. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The recharge is based on seats assigned on the last day of the prior month, so mid-month leavers still appear. Following the documented resolution, pull the assignment snapshot for the last day of the prior month and walk the owner through it line by line. Confirm any genuinely wrong assignment and correct it in the following cycle. Escalate to finance only if the correction exceeds a full month of charges.

The agent records the diagnosis against the ticket, confirms with aisha.nakamura@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to IT Asset Management was needed.

### Example: assigning a licence from a pool

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about software licence management. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the inactivity threshold before a licence is reclaimed is flexible or negotiable per user.**

It is not. The inactivity threshold before a licence is reclaimed is 52 consecutive days without a sign-in to the licensed application, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the reclaim warning notice is flexible or negotiable per user.**

It is not. The reclaim warning notice is a single email warning sent 9 days before the licence is removed, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the licence pool headroom target is flexible or negotiable per user.**

It is not. The licence pool headroom target is between 3 and 6 per cent spare seats held in each pool, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the annual true-up submission date is flexible or negotiable per user.**

It is not. The annual true-up submission date is 15 February each year, covering the preceding calendar year, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: IT Asset Management can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to software licence management, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to IT Asset Management.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Flexera One did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, IT Asset Management produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about software licence management unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

IT Asset Management runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Why was my software licence taken away?**

Licences are harvested automatically after 52 consecutive days without a sign-in to that application, and a warning is emailed 9 days before removal.

**Can my team buy software directly?**

No. All purchases go through IT Asset Management so the seats land in a managed licence pool.

**When is my department charged for its licences?**

Monthly on the 4th working day, based on the seats assigned on the last day of the prior month.

**When is the annual true-up submitted?**

By 15 February each year, covering the preceding calendar year.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, IT Asset Management will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is IT Asset Management, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Flexera One, engaged by IT Asset Management only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

IT Asset Management produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about software licence management. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Check available headroom for the product in Flexera One.
- [ ] Confirm the requester's cost centre on the HR record.
- [ ] Export the sign-in activity report for every managed product.
- [ ] Flag every assignment with no sign-in for 52 consecutive days.
- [ ] Freeze the deployment position on 31 December and export the entitlement report.
- [ ] Reconcile deployed seats against the contracted entitlement for each product.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Why was my software licence taken away? Licences are harvested automatically after 52 consecutive days without a sign-in to that application, and a warning is emailed 9 days before removal.
- Can my team buy software directly? No. All purchases go through IT Asset Management so the seats land in a managed licence pool.
- When is my department charged for its licences? Monthly on the 4th working day, based on the seats assigned on the last day of the prior month.
- When is the annual true-up submitted? By 15 February each year, covering the preceding calendar year.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | IT Asset Management | First published version. |
| 1.1 | 2024-11-02 | IT Asset Management | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | IT Asset Management | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | IT Asset Management | Annual review; figures confirmed against the running configuration of Flexera One. |
