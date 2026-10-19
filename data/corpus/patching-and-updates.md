---
title: Patching and Update Management Policy
doc_type: policy
category: infrastructure
owner: Infrastructure Services
version: 2.1
review_date: 2027-02-09
---

# Patching and Update Management Policy

Owner: Infrastructure Services | System of record: Microsoft Configuration Manager | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages patching and update management. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Infrastructure Services team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the infrastructure estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Microsoft Configuration Manager is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Microsoft Configuration Manager. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Patch ring**  
A group of devices that receives updates at a defined stage, used to catch problems before the whole fleet is updated. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Emergency patch**  
An out of band update applied outside the normal window because the risk of waiting is greater than the risk of deploying. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Compliance rate**  
The proportion of in-scope devices that have installed a given update by its severity deadline. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Infrastructure Services. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Infrastructure Services** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Infrastructure Services rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Every managed device must remain within the patch deadline for its highest outstanding severity.

Agents should treat this as non-negotiable. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Infrastructure Services will either confirm the control applies or sponsor an exception, usually within a few working days. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 2. Patches must be released through the pilot ring before any broad deployment to the fleet.

In practice this means the following. Infrastructure Services configures Microsoft Configuration Manager to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 3. Servers may only be patched inside the agreed window unless an emergency patch has been authorised.

This has been the standing position since the last review. This statement has been tested against the current configuration of Microsoft Configuration Manager. Where a platform change makes it unenforceable, Infrastructure Services raises a risk acceptance rather than quietly dropping the control. Where the control cannot be enforced technically, Infrastructure Services monitors for breaches and follows up with the individual and their line manager.

### 4. A device that misses its severity deadline is reported to the device owner's line manager.

There is a documented exception route, described later in this document. This statement has been tested against the current configuration of Microsoft Configuration Manager. Where a platform change makes it unenforceable, Infrastructure Services raises a risk acceptance rather than quietly dropping the control. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 5. No update may be permanently excluded from a device without a recorded risk acceptance from Information Security.

This is enforced technically wherever the platform allows it. Evidence that the control is operating is collected automatically from Microsoft Configuration Manager and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Infrastructure Services configures in Microsoft Configuration Manager. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Standard server patch window | the third Saturday of each month, 23:30 to 05:00 |
| Workstation patch deadline for critical severity | 72 hours from release to installed |
| Workstation patch deadline for important severity | 11 calendar days from release to installed |
| Workstation patch deadline for moderate and low severity | 38 calendar days from release to installed |
| Maximum user deferrals of a restart | 3 deferrals of 8 hours each, after which the restart is forced |
| Emergency patch authority | the Infrastructure Services change lead, who may bypass the normal change board with a retrospective record within 2 working days |

**Standard server patch window.** The standard server patch window is the third Saturday of each month, 23:30 to 05:00. This is configured centrally in Microsoft Configuration Manager and is not adjustable per user or per team.

**Workstation patch deadline for critical severity.** The workstation patch deadline for critical severity is 72 hours from release to installed. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Workstation patch deadline for important severity.** The workstation patch deadline for important severity is 11 calendar days from release to installed. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Workstation patch deadline for moderate and low severity.** The workstation patch deadline for moderate and low severity is 38 calendar days from release to installed. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Maximum user deferrals of a restart.** The maximum user deferrals of a restart is 3 deferrals of 8 hours each, after which the restart is forced. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Emergency patch authority.** The emergency patch authority is the Infrastructure Services change lead, who may bypass the normal change board with a retrospective record within 2 working days. Infrastructure Services set this figure in consultation with Information Security, and it is reviewed annually.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Microsoft Configuration Manager diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Infrastructure Services, and reviewed annually with Information Security.

## Architecture and dependencies

Microsoft Configuration Manager is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Microsoft Configuration Manager follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Infrastructure Services maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Infrastructure Services raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Microsoft Configuration Manager, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Infrastructure Services implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Infrastructure Services rather than skipping it.

### Running the monthly patch cycle

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Review the released updates and assign each a severity against the deadline scale.
2. Deploy to the pilot ring and hold for observation before going wider.
3. Check the pilot ring for failed installations and application faults.
4. Release to the broad rings in sequence once the pilot ring is clean.
5. Patch the servers inside the third Saturday window.
6. Publish the compliance rate per severity at the end of the cycle.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Authorising an emergency patch

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Document the vulnerability, the exposure and why waiting for the next window is unacceptable.
2. Obtain authorisation from the Infrastructure Services change lead.
3. Deploy to the pilot ring first, even under emergency conditions, unless exploitation is already confirmed.
4. Deploy to the remaining rings and monitor for failed installations.
5. File the retrospective change record within 2 working days.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Chasing a device that has missed its deadline

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the device has checked in and is not simply switched off or offline.
2. Check whether the user has exhausted the 3 available restart deferrals.
3. Contact the user with the outstanding update and the deadline that was missed.
4. Force the restart if the deferral allowance is exhausted and the deadline has passed.
5. Notify the device owner's line manager if the device remains outstanding after contact.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Infrastructure Services with the diagnostic output attached rather than retrying the same steps.

### Symptom: An update repeatedly fails to install on a workstation and rolls back on restart.


**Error code:** B-0x80073712

**Cause.** The component store is corrupt, so the update cannot be staged successfully..

**Resolution.** Run the component store repair, restart the device and retry the update once. If the second attempt also rolls back, rebuild the device rather than retrying further. Escalate to Infrastructure Services if the same failure appears across more than a handful of devices, as that points to a bad package rather than a local fault.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A device shows as non-compliant even though the user says it has restarted.


**Error code:** B-CFGMGR-0x87D00215

**Cause.** The management agent has not reported its inventory back since the installation completed..

**Resolution.** Trigger a hardware inventory and software update scan cycle on the device and wait for the next check-in. Confirm the device can reach the management point on the network. Escalate to Infrastructure Services if the device still reports stale after a successful scan, since the agent may need reinstalling.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: Users complain that their machines restarted without warning.


**Error code:** B-WUA-0x8024A112

**Cause.** The 3 available deferrals of 8 hours each were used up, so the restart was enforced automatically..

**Resolution.** Explain the deferral allowance and the deadline that drove the enforced restart. Advise users to restart at a convenient point rather than deferring to the limit. Escalate to Infrastructure Services only if the restart happened while deferrals were still available, which would indicate a policy misconfiguration.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: A server was patched outside the agreed window.


**Cause.** An emergency patch was authorised by the change lead and deployed before the retrospective record was filed..

**Resolution.** Confirm with the change lead that the emergency patch was authorised and identify the vulnerability involved. Ensure the retrospective change record is filed within the 2 working day limit. Escalate as an unauthorised change if no change lead authorisation can be evidenced.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Infrastructure Services to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: An update repeatedly fails to install on a workstation and rolls back 

Reference: B-0x80073712.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Configuration Manager and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: A device shows as non-compliant even though the user says it has resta

Reference: B-CFGMGR-0x87D00215.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Configuration Manager and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: Users complain that their machines restarted without warning.

Reference: B-WUA-0x8024A112.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Configuration Manager and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: A server was patched outside the agreed window.

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Configuration Manager and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

## Worked examples

### Example: An update repeatedly fails to install on a workstation and rolls back 

A user at London HQ contacts the service desk reporting that an update repeatedly fails to install on a workstation and rolls back on restart.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The component store is corrupt, so the update cannot be staged successfully.. Following the documented resolution, run the component store repair, restart the device and retry the update once. If the second attempt also rolls back, rebuild the device rather than retrying further. Escalate to Infrastructure Services if the same failure appears across more than a handful of devices, as that points to a bad package rather than a local fault.

The agent records the diagnosis against the ticket, confirms with aisha.moreau@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: A device shows as non-compliant even though the user says it has resta

A user at Remote contacts the service desk reporting that a device shows as non-compliant even though the user says it has restarted.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The management agent has not reported its inventory back since the installation completed.. Following the documented resolution, trigger a hardware inventory and software update scan cycle on the device and wait for the next check-in. Confirm the device can reach the management point on the network. Escalate to Infrastructure Services if the device still reports stale after a successful scan, since the agent may need reinstalling.

The agent records the diagnosis against the ticket, confirms with viktor.nakamura@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: Users complain that their machines restarted without warning.

A user at Manchester contacts the service desk reporting that users complain that their machines restarted without warning.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The 3 available deferrals of 8 hours each were used up, so the restart was enforced automatically.. Following the documented resolution, explain the deferral allowance and the deadline that drove the enforced restart. Advise users to restart at a convenient point rather than deferring to the limit. Escalate to Infrastructure Services only if the restart happened while deferrals were still available, which would indicate a policy misconfiguration.

The agent records the diagnosis against the ticket, confirms with dmitri.oconnell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: running the monthly patch cycle

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about patching and update management. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the standard server patch window is flexible or negotiable per user.**

It is not. The standard server patch window is the third Saturday of each month, 23:30 to 05:00, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the workstation patch deadline for critical severity is flexible or negotiable per user.**

It is not. The workstation patch deadline for critical severity is 72 hours from release to installed, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the workstation patch deadline for important severity is flexible or negotiable per user.**

It is not. The workstation patch deadline for important severity is 11 calendar days from release to installed, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the workstation patch deadline for moderate and low severity is flexible or negotiable per user.**

It is not. The workstation patch deadline for moderate and low severity is 38 calendar days from release to installed, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Infrastructure Services can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to patching and update management, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Infrastructure Services.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Microsoft Configuration Manager did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Infrastructure Services produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about patching and update management unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Infrastructure Services runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How quickly do critical patches have to be installed?**

Critical severity updates must be installed within 72 hours of release, compared with 11 calendar days for important and 38 calendar days for moderate and low.

**Can I put off a restart?**

You can defer a restart up to 3 times by 8 hours each, after which the device restarts automatically.

**When are servers patched?**

Servers are patched in the monthly window on the third Saturday, between 23:30 and 05:00.

**Who can approve a patch outside the normal cycle?**

The Infrastructure Services change lead can authorise an emergency patch and must file a retrospective change record within 2 working days.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Infrastructure Services will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Infrastructure Services, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Microsoft Configuration Manager, engaged by Infrastructure Services only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Infrastructure Services produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about patching and update management. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Review the released updates and assign each a severity against the deadline scale.
- [ ] Deploy to the pilot ring and hold for observation before going wider.
- [ ] Document the vulnerability, the exposure and why waiting for the next window is unacceptable.
- [ ] Obtain authorisation from the Infrastructure Services change lead.
- [ ] Confirm the device has checked in and is not simply switched off or offline.
- [ ] Check whether the user has exhausted the 3 available restart deferrals.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How quickly do critical patches have to be installed? Critical severity updates must be installed within 72 hours of release, compared with 11 calendar days for important and 38 calendar days for moderate and low.
- Can I put off a restart? You can defer a restart up to 3 times by 8 hours each, after which the device restarts automatically.
- When are servers patched? Servers are patched in the monthly window on the third Saturday, between 23:30 and 05:00.
- Who can approve a patch outside the normal cycle? The Infrastructure Services change lead can authorise an emergency patch and must file a retrospective change record within 2 working days.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Infrastructure Services | First published version. |
| 1.1 | 2024-11-02 | Infrastructure Services | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Infrastructure Services | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Infrastructure Services | Annual review; figures confirmed against the running configuration of Microsoft Configuration Manager. |
