---
title: Database Access Request Runbook
doc_type: runbook
category: data
owner: Data Platform Engineering
version: 2.1
review_date: 2027-02-09
---

# Database Access Request Runbook

Owner: Data Platform Engineering | System of record: Microsoft SQL Server | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages database access request. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Data Platform Engineering team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the data estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Microsoft SQL Server is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Microsoft SQL Server. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Masked environment**  
A non-production copy of a database in which names, contact details and account numbers have been replaced with realistic but fictitious values. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Temporary grant**  
A time-boxed permission issued for a specific piece of work and removed automatically after 48 hours without any further action. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Break-glass account**  
A tightly held account with production write rights, used only when no other route exists and subject to full session recording. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Data Platform Engineering. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Data Platform Engineering** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Data Platform Engineering rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Analysis and development work must use a masked environment unless a written exception from the data owner is attached to the request.

Agents should treat this as non-negotiable. Data Platform Engineering configures Microsoft SQL Server to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Where the control cannot be enforced technically, Data Platform Engineering monitors for breaches and follows up with the individual and their line manager.

### 2. Write access to production is never granted to an individual named user; it is exercised only through a break-glass account.

This has been the standing position since the last review. Data Platform Engineering configures Microsoft SQL Server to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 3. Every granted permission is recorded against the originating request with the approver and the expiry date.

This is enforced technically wherever the platform allows it. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Data Platform Engineering will either confirm the control applies or sponsor an exception, usually within a few working days. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 4. Access is granted to a database role, never to an individual login directly.

There is a documented exception route, described later in this document. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Data Platform Engineering will either confirm the control applies or sponsor an exception, usually within a few working days. Data Platform Engineering reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 5. Database access is recertified every 75 days, and any grant whose requester has left the business is removed immediately.

In practice this means the following. Data Platform Engineering configures Microsoft SQL Server to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Data Platform Engineering configures in Microsoft SQL Server. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Approval route for read access | the named data owner alone, recorded against the request |
| Approval route for write access | the named data owner plus Information Security, both required |
| Maximum temporary grant duration | 48 hours, revoked automatically by the access job when it expires |
| Masked environment refresh cadence | every 14 days from production, with all direct identifiers replaced |
| Standing production write accounts | 11 named break-glass accounts, held by Data Platform Engineering and reviewed each quarter |
| Reporting replica query timeout | 300 seconds, after which the query is cancelled by the resource governor |

**Approval route for read access.** The approval route for read access is the named data owner alone, recorded against the request. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Approval route for write access.** The approval route for write access is the named data owner plus Information Security, both required. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Maximum temporary grant duration.** The maximum temporary grant duration is 48 hours, revoked automatically by the access job when it expires. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Masked environment refresh cadence.** The masked environment refresh cadence is every 14 days from production, with all direct identifiers replaced. This is configured centrally in Microsoft SQL Server and is not adjustable per user or per team.

**Standing production write accounts.** The standing production write accounts is 11 named break-glass accounts, held by Data Platform Engineering and reviewed each quarter. Data Platform Engineering set this figure in consultation with Information Security, and it is reviewed annually.

**Reporting replica query timeout.** The reporting replica query timeout is 300 seconds, after which the query is cancelled by the resource governor. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Microsoft SQL Server diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Data Platform Engineering, and reviewed annually with Information Security.

## Architecture and dependencies

Microsoft SQL Server is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Microsoft SQL Server follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Data Platform Engineering maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Data Platform Engineering raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Microsoft SQL Server, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Data Platform Engineering implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Data Platform Engineering rather than skipping it.

### Granting read access to a production database

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the requester cannot do the work in a masked environment.
2. Route the request to the named data owner for approval.
3. Add the requester to the appropriate read-only database role.
4. Record the approver, the role and the expiry date against the request.
5. Schedule the grant for review at the next 75 day recertification.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Issuing a temporary grant

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Capture the specific task and the data the requester needs to touch.
2. Obtain the data owner approval, and Information Security approval if any write is involved.
3. Create the grant with a 48 hour expiry set on the access job.
4. Notify the requester of the exact start and end time of the window.
5. Confirm the automatic revocation completed after the window closed.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Refreshing a masked environment

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Take the scheduled production backup for the 14 day refresh cycle.
2. Restore it into the staging instance isolated from user access.
3. Run the masking job and confirm it reports zero unmasked identifier columns.
4. Validate row counts and a sample of masked values before opening access.
5. Release the environment to users and record the refresh date.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Data Platform Engineering with the diagnostic output attached rather than retrying the same steps.

### Symptom: A user loses access mid-task and the log records D-SQL-5542


**Error code:** D-SQL-5542

**Cause.** The 48 hour temporary grant expired and was revoked automatically.

**Resolution.** Confirm the original request and whether the work is still in progress. Raise a fresh temporary grant with the same approvals rather than extending the expired one. Escalate to Data Platform Engineering if the same task has needed more than two temporary grants, as it probably needs a permanent role.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A reporting query fails after several minutes with D-SQL-8827


**Error code:** D-SQL-8827

**Cause.** The query exceeded the 300 second resource governor timeout on the reporting replica.

**Resolution.** Review the query plan for missing filters or a full table scan and add the date range the report actually needs. Advise the user to run very large extracts through the scheduled extract service instead. Escalate to Data Platform Engineering if a well filtered query still exceeds 300 seconds.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A write access request is rejected despite data owner approval


**Cause.** Information Security approval is also mandatory for write access and had not been obtained.

**Resolution.** Return the request to the requester and ask them to add Information Security as the second approver. Explain that write access to production is exercised through a break-glass account, not a personal login. Escalate to Information Security if the second approval is outstanding for more than one business day.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A masked environment shows real customer names and raises D-SQL-1903


**Error code:** D-SQL-1903

**Cause.** The masking job did not complete, so the restored copy was released with unmasked identifier columns.

**Resolution.** Withdraw user access to the environment immediately and treat it as a data exposure. Re-run the masking job and confirm it reports zero unmasked identifier columns before reopening access. Report the exposure to Information Security the same day.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Data Platform Engineering to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A user loses access mid-task and the log records D-SQL-5542

Reference: D-SQL-5542.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft SQL Server and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Data Platform Engineering citing the reference above.

### Diagnostics for: A reporting query fails after several minutes with D-SQL-8827

Reference: D-SQL-8827.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft SQL Server and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Data Platform Engineering citing the reference above.

### Diagnostics for: A write access request is rejected despite data owner approval

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft SQL Server and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Data Platform Engineering citing the reference above.

### Diagnostics for: A masked environment shows real customer names and raises D-SQL-1903

Reference: D-SQL-1903.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft SQL Server and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Data Platform Engineering citing the reference above.

## Worked examples

### Example: A user loses access mid-task and the log records D-SQL-5542

A user at Remote contacts the service desk reporting that a user loses access mid-task and the log records D-SQL-5542. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The 48 hour temporary grant expired and was revoked automatically. Following the documented resolution, confirm the original request and whether the work is still in progress. Raise a fresh temporary grant with the same approvals rather than extending the expired one. Escalate to Data Platform Engineering if the same task has needed more than two temporary grants, as it probably needs a permanent role.

The agent records the diagnosis against the ticket, confirms with viktor.haddad@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Data Platform Engineering was needed.

### Example: A reporting query fails after several minutes with D-SQL-8827

A user at Manchester contacts the service desk reporting that a reporting query fails after several minutes with D-SQL-8827. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The query exceeded the 300 second resource governor timeout on the reporting replica. Following the documented resolution, review the query plan for missing filters or a full table scan and add the date range the report actually needs. Advise the user to run very large extracts through the scheduled extract service instead. Escalate to Data Platform Engineering if a well filtered query still exceeds 300 seconds.

The agent records the diagnosis against the ticket, confirms with mira.bergmann@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Data Platform Engineering was needed.

### Example: A write access request is rejected despite data owner approval

A user at Manchester contacts the service desk reporting that a write access request is rejected despite data owner approval. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Information Security approval is also mandatory for write access and had not been obtained. Following the documented resolution, return the request to the requester and ask them to add Information Security as the second approver. Explain that write access to production is exercised through a break-glass account, not a personal login. Escalate to Information Security if the second approval is outstanding for more than one business day.

The agent records the diagnosis against the ticket, confirms with sofia.bell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Data Platform Engineering was needed.

### Example: granting read access to a production database

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about database access request. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the approval route for read access is flexible or negotiable per user.**

It is not. The approval route for read access is the named data owner alone, recorded against the request, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the approval route for write access is flexible or negotiable per user.**

It is not. The approval route for write access is the named data owner plus Information Security, both required, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the maximum temporary grant duration is flexible or negotiable per user.**

It is not. The maximum temporary grant duration is 48 hours, revoked automatically by the access job when it expires, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the masked environment refresh cadence is flexible or negotiable per user.**

It is not. The masked environment refresh cadence is every 14 days from production, with all direct identifiers replaced, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Data Platform Engineering can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to database access request, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Data Platform Engineering.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Microsoft SQL Server did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Data Platform Engineering produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about database access request unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Data Platform Engineering runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Who approves read access to a production database?**

The named data owner alone, with the approval recorded against the request.

**How long does a temporary grant last?**

48 hours, after which the access job revokes it automatically.

**Can I get write access to production?**

Not as a personal login. Write access is exercised through one of the 11 break-glass accounts held by Data Platform Engineering.

**How fresh is the masked test data?**

It is refreshed from production every 14 days with all direct identifiers replaced.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Data Platform Engineering will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Data Platform Engineering, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Microsoft SQL Server, engaged by Data Platform Engineering only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Data Platform Engineering produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about database access request. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the requester cannot do the work in a masked environment.
- [ ] Route the request to the named data owner for approval.
- [ ] Capture the specific task and the data the requester needs to touch.
- [ ] Obtain the data owner approval, and Information Security approval if any write is involved.
- [ ] Take the scheduled production backup for the 14 day refresh cycle.
- [ ] Restore it into the staging instance isolated from user access.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Who approves read access to a production database? The named data owner alone, with the approval recorded against the request.
- How long does a temporary grant last? 48 hours, after which the access job revokes it automatically.
- Can I get write access to production? Not as a personal login. Write access is exercised through one of the 11 break-glass accounts held by Data Platform Engineering.
- How fresh is the masked test data? It is refreshed from production every 14 days with all direct identifiers replaced.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Data Platform Engineering | First published version. |
| 1.1 | 2024-11-02 | Data Platform Engineering | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Data Platform Engineering | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Data Platform Engineering | Annual review; figures confirmed against the running configuration of Microsoft SQL Server. |
