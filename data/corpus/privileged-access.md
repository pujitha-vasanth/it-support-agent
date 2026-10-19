---
title: Privileged Access Management Policy
doc_type: policy
category: security
owner: Information Security
version: 2.1
review_date: 2027-02-09
---

# Privileged Access Management Policy

Owner: Information Security | System of record: CyberArk Privilege Cloud | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages privileged access management. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Information Security team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the security estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

CyberArk Privilege Cloud is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of CyberArk Privilege Cloud. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Just-in-time elevation**  
The temporary activation of a privileged role for a single task, which expires automatically after 95 minutes. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Standing privilege**  
A privileged role held permanently rather than activated on demand, which is permitted only for a named break-glass holder. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Duty approver**  
The rostered Information Security approver who provides the second approval for production elevation requests. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Information Security. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Information Security** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Information Security rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Privileged access to production systems is granted only through just-in-time elevation, never as standing privilege.

Agents should treat this as non-negotiable. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Security will either confirm the control applies or sponsor an exception, usually within a few working days. Where the control cannot be enforced technically, Information Security monitors for breaches and follows up with the individual and their line manager.

### 2. Every production elevation requires approval from the system owner and from the Information Security duty approver, and self-approval is never permitted.

The reasoning behind this is straightforward. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Security will either confirm the control applies or sponsor an exception, usually within a few working days. Where the control cannot be enforced technically, Information Security monitors for breaches and follows up with the individual and their line manager.

### 3. All privileged sessions are recorded, and the recordings are retained for 4 years.

In practice this means the following. Evidence that the control is operating is collected automatically from CyberArk Privilege Cloud and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 4. Privileged roles are recertified every 61 days and are removed automatically if the reviewer does not respond.

This has been the standing position since the last review. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Security will either confirm the control applies or sponsor an exception, usually within a few working days. Where the control cannot be enforced technically, Information Security monitors for breaches and follows up with the individual and their line manager.

### 5. Break-glass credentials are split between Information Security and Network Operations so that no single person can use them alone.

This is enforced technically wherever the platform allows it. Information Security configures CyberArk Privilege Cloud to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Information Security configures in CyberArk Privilege Cloud. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Maximum just-in-time elevation duration | 95 minutes per activation, after which the role expires automatically |
| Approval chain for production elevation | the system owner approves first, then the Information Security duty approver, with no self-approval permitted |
| Session recording retention | 4 years for all recorded privileged sessions |
| Recertification frequency for privileged roles | every 61 days, with removal if the reviewer does not respond |
| Break-glass account count | 2 accounts per production platform, with credentials split between Information Security and Network Operations |
| Maximum standing privileged accounts per person | 1, which may only be a named break-glass holder role |

**Maximum just-in-time elevation duration.** The maximum just-in-time elevation duration is 95 minutes per activation, after which the role expires automatically. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Approval chain for production elevation.** The approval chain for production elevation is the system owner approves first, then the Information Security duty approver, with no self-approval permitted. Information Security set this figure in consultation with Information Security, and it is reviewed annually.

**Session recording retention.** The session recording retention is 4 years for all recorded privileged sessions. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Recertification frequency for privileged roles.** The recertification frequency for privileged roles is every 61 days, with removal if the reviewer does not respond. Information Security set this figure in consultation with Information Security, and it is reviewed annually.

**Break-glass account count.** The break-glass account count is 2 accounts per production platform, with credentials split between Information Security and Network Operations. This is configured centrally in CyberArk Privilege Cloud and is not adjustable per user or per team.

**Maximum standing privileged accounts per person.** The maximum standing privileged accounts per person is 1, which may only be a named break-glass holder role. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of CyberArk Privilege Cloud diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Information Security, and reviewed annually with Information Security.

## Architecture and dependencies

CyberArk Privilege Cloud is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to CyberArk Privilege Cloud follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Information Security maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Information Security raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to CyberArk Privilege Cloud, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Information Security implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Information Security rather than skipping it.

### Requesting just-in-time elevation

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise the elevation request in CyberArk Privilege Cloud, naming the target system and the task.
2. Wait for the system owner approval, then for the Information Security duty approver.
3. Activate the role and begin work, noting the 95 minute expiry.
4. Complete the task and end the session before the role expires.
5. Confirm the session recording has been captured against the request.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Using a break-glass account

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Declare a major incident so the break-glass use is on record.
2. Ask the Information Security holder and the Network Operations holder to each supply their credential half.
3. Sign in and confirm session recording has started before taking any action.
4. Carry out only the actions needed to restore service.
5. Rotate the break-glass credentials immediately after the session and file the usage report.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Running the privileged role recertification

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Generate the privileged role report at the start of each 61 day cycle.
2. Send each reviewer the list of privileged roles held by their team.
3. Record every confirmed role against the access register.
4. Remove any role the reviewer has not confirmed by the cycle close.
5. Report the removal count to the Information Security governance forum.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Information Security with the diagnostic output attached rather than retrying the same steps.

### Symptom: An engineer loses administrative rights part way through a change


**Error code:** C-PAM-6629

**Cause.** The just-in-time elevation reached its 95 minute expiry.

**Resolution.** Ask the engineer to raise a fresh elevation request and obtain both approvals again, then resume the work. Advise them to break long changes into stages that fit inside the activation window. Escalate to the Information Security duty approver for an out-of-hours approval if the change is mid-flight on a production system.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: An elevation request sits unapproved for hours


**Error code:** C-PAM-0x80070542

**Cause.** The requester is also the system owner, and self-approval is blocked by policy.

**Resolution.** Reroute the first approval to a deputy system owner recorded on the system register, then let the Information Security duty approver complete the chain. Do not override the self-approval block. Escalate to Information Security if no deputy is recorded for that system.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A privileged session shows no recording against the request


**Error code:** C-PAM-5183

**Cause.** The engineer connected directly to the target system instead of through the privileged session broker.

**Resolution.** Terminate the direct connection, have the engineer reconnect through CyberArk Privilege Cloud and confirm the recording indicator is active. Report the unrecorded session to Information Security the same day. Treat any repeat as a policy breach and escalate to the governance forum.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A team reports their privileged roles disappeared overnight


**Cause.** The reviewer did not respond before the 61 day recertification cycle closed, so the roles were removed automatically.

**Resolution.** Ask the team to raise fresh just-in-time elevation requests for any immediate work. Have the reviewer reconfirm the roles so they are restored at the next cycle. Escalate to the departmental head if the reviewer has missed two consecutive cycles.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Information Security to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: An engineer loses administrative rights part way through a change

Reference: C-PAM-6629.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of CyberArk Privilege Cloud and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: An elevation request sits unapproved for hours

Reference: C-PAM-0x80070542.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of CyberArk Privilege Cloud and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: A privileged session shows no recording against the request

Reference: C-PAM-5183.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of CyberArk Privilege Cloud and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: A team reports their privileged roles disappeared overnight

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of CyberArk Privilege Cloud and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

## Worked examples

### Example: An engineer loses administrative rights part way through a change

A user at Remote contacts the service desk reporting that an engineer loses administrative rights part way through a change. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The just-in-time elevation reached its 95 minute expiry. Following the documented resolution, ask the engineer to raise a fresh elevation request and obtain both approvals again, then resume the work. Advise them to break long changes into stages that fit inside the activation window. Escalate to the Information Security duty approver for an out-of-hours approval if the change is mid-flight on a production system.

The agent records the diagnosis against the ticket, confirms with viktor.novak@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: An elevation request sits unapproved for hours

A user at Remote contacts the service desk reporting that an elevation request sits unapproved for hours. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The requester is also the system owner, and self-approval is blocked by policy. Following the documented resolution, reroute the first approval to a deputy system owner recorded on the system register, then let the Information Security duty approver complete the chain. Do not override the self-approval block. Escalate to Information Security if no deputy is recorded for that system.

The agent records the diagnosis against the ticket, confirms with oscar.nakamura@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: A privileged session shows no recording against the request

A user at London HQ contacts the service desk reporting that a privileged session shows no recording against the request. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The engineer connected directly to the target system instead of through the privileged session broker. Following the documented resolution, terminate the direct connection, have the engineer reconnect through CyberArk Privilege Cloud and confirm the recording indicator is active. Report the unrecorded session to Information Security the same day. Treat any repeat as a policy breach and escalate to the governance forum.

The agent records the diagnosis against the ticket, confirms with dmitri.chaudhry@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: requesting just-in-time elevation

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about privileged access management. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the maximum just-in-time elevation duration is flexible or negotiable per user.**

It is not. The maximum just-in-time elevation duration is 95 minutes per activation, after which the role expires automatically, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the approval chain for production elevation is flexible or negotiable per user.**

It is not. The approval chain for production elevation is the system owner approves first, then the Information Security duty approver, with no self-approval permitted, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the session recording retention is flexible or negotiable per user.**

It is not. The session recording retention is 4 years for all recorded privileged sessions, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the recertification frequency for privileged roles is flexible or negotiable per user.**

It is not. The recertification frequency for privileged roles is every 61 days, with removal if the reviewer does not respond, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Information Security can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to privileged access management, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Information Security.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of CyberArk Privilege Cloud did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Information Security produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about privileged access management unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Information Security runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How long does a privileged elevation last?**

95 minutes per activation, after which the role expires automatically and a fresh request is needed.

**Can I approve my own elevation request?**

No. The system owner approves first and the Information Security duty approver second, and self-approval is never permitted.

**How long are privileged session recordings kept?**

4 years for all recorded privileged sessions.

**How often are privileged roles reviewed?**

Every 61 days, and any role the reviewer does not confirm is removed automatically.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Information Security will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Information Security, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for CyberArk Privilege Cloud, engaged by Information Security only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Information Security produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about privileged access management. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Raise the elevation request in CyberArk Privilege Cloud, naming the target system and the task.
- [ ] Wait for the system owner approval, then for the Information Security duty approver.
- [ ] Declare a major incident so the break-glass use is on record.
- [ ] Ask the Information Security holder and the Network Operations holder to each supply their credential half.
- [ ] Generate the privileged role report at the start of each 61 day cycle.
- [ ] Send each reviewer the list of privileged roles held by their team.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How long does a privileged elevation last? 95 minutes per activation, after which the role expires automatically and a fresh request is needed.
- Can I approve my own elevation request? No. The system owner approves first and the Information Security duty approver second, and self-approval is never permitted.
- How long are privileged session recordings kept? 4 years for all recorded privileged sessions.
- How often are privileged roles reviewed? Every 61 days, and any role the reviewer does not confirm is removed automatically.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Information Security | First published version. |
| 1.1 | 2024-11-02 | Information Security | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Information Security | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Information Security | Annual review; figures confirmed against the running configuration of CyberArk Privilege Cloud. |
