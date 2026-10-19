---
title: IT Asset Lifecycle Management Policy
doc_type: policy
category: hardware
owner: IT Asset Management
version: 2.1
review_date: 2027-02-09
---

# IT Asset Lifecycle Management Policy

Owner: IT Asset Management | System of record: ServiceNow IT Asset Management | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages IT asset lifecycle management. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The IT Asset Management team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the hardware estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

ServiceNow IT Asset Management is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of ServiceNow IT Asset Management. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Asset tag**  
The unique company identifier applied physically to a device and recorded against it in the asset register. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Buffer stock**  
Unallocated built devices held ready so that a replacement can be issued without waiting for procurement. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Certificate of destruction**  
The supplier document confirming that a named drive serial number was destroyed or securely overwritten. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

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

### 1. No device may be issued to an employee until it carries an asset tag and a matching asset register record.

There is a documented exception route, described later in this document. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. IT Asset Management will either confirm the control applies or sponsor an exception, usually within a few working days. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 2. Hardware purchases outside the standard catalogue require IT Asset Management approval before any order is raised.

Agents should treat this as non-negotiable. Evidence that the control is operating is collected automatically from ServiceNow IT Asset Management and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Where the control cannot be enforced technically, IT Asset Management monitors for breaches and follows up with the individual and their line manager.

### 3. Devices returned by leavers must be received into the build room within 3 working days of the leaving date.

This is enforced technically wherever the platform allows it. IT Asset Management configures ServiceNow IT Asset Management to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 4. No storage device may leave company premises for disposal without a recorded certificate of destruction.

In practice this means the following. IT Asset Management configures ServiceNow IT Asset Management to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 5. Employees are accountable for the devices recorded against their name until the return is confirmed in the asset register.

The reasoning behind this is straightforward. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. IT Asset Management will either confirm the control applies or sponsor an exception, usually within a few working days. Where the control cannot be enforced technically, IT Asset Management monitors for breaches and follows up with the individual and their line manager.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what IT Asset Management configures in ServiceNow IT Asset Management. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Standard laptop refresh cycle | 46 months from the purchase date |
| Monitor and peripheral refresh cycle | 7 years from the purchase date, or on failure if sooner |
| Asset tag format | MG followed by a six digit sequence, for example MG004821, applied before the device leaves the build room |
| Buffer stock level for standard laptops | 9 percent of the deployed fleet, with a reorder trigger at 4 percent |
| Procurement lead time for a standard laptop | 13 working days from approved purchase order to build room receipt |
| Data destruction standard at disposal | a certified three pass overwrite, or physical destruction for any drive that fails the overwrite |

**Standard laptop refresh cycle.** The standard laptop refresh cycle is 46 months from the purchase date. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Monitor and peripheral refresh cycle.** The monitor and peripheral refresh cycle is 7 years from the purchase date, or on failure if sooner. This is configured centrally in ServiceNow IT Asset Management and is not adjustable per user or per team.

**Asset tag format.** The asset tag format is MG followed by a six digit sequence, for example MG004821, applied before the device leaves the build room. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Buffer stock level for standard laptops.** The buffer stock level for standard laptops is 9 percent of the deployed fleet, with a reorder trigger at 4 percent. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Procurement lead time for a standard laptop.** The procurement lead time for a standard laptop is 13 working days from approved purchase order to build room receipt. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Data destruction standard at disposal.** The data destruction standard at disposal is a certified three pass overwrite, or physical destruction for any drive that fails the overwrite. IT Asset Management set this figure in consultation with Information Security, and it is reviewed annually.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of ServiceNow IT Asset Management diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, IT Asset Management, and reviewed annually with Information Security.

## Architecture and dependencies

ServiceNow IT Asset Management is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to ServiceNow IT Asset Management follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

IT Asset Management maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, IT Asset Management raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to ServiceNow IT Asset Management, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. IT Asset Management implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to IT Asset Management rather than skipping it.

### Receiving and tagging a new device

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Check the delivered serial numbers against the purchase order before signing for the delivery.
2. Create the asset record and assign the next asset tag in the MG sequence.
3. Apply the physical asset tag to the device chassis.
4. Run the standard build and record the build version against the asset record.
5. Move the asset to Available status so it counts towards buffer stock.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Issuing a replacement device on refresh

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Identify devices that have reached 46 months from their purchase date.
2. Contact the device holder and agree a swap date at least a week ahead.
3. Allocate an available buffer stock device and record the new assignment.
4. Transfer the user's data and confirm with the user that nothing is missing.
5. Receive the old device into the build room and set it to Pending Disposal.
6. Close the refresh record once both asset records show the correct holder.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Disposing of a retired device

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the asset is in Pending Disposal status and has no outstanding assignment.
2. Run the certified three pass overwrite on every storage device.
3. Send any drive that fails the overwrite for physical destruction instead.
4. Collect the certificate of destruction from the disposal supplier.
5. Attach the certificate to the asset record and set the asset to Disposed.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to IT Asset Management with the diagnostic output attached rather than retrying the same steps.

### Symptom: A device in use has no record in the asset register.


**Error code:** B-SNOW-6621

**Cause.** The device was issued before tagging, so the register record was never created..

**Resolution.** Capture the serial number and model, create the missing asset record and apply an asset tag at the next opportunity. Confirm the current holder and the approximate issue date so the refresh clock can be set. Escalate to IT Asset Management if the device cannot be matched to any purchase order, as that suggests an unapproved purchase.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A replacement laptop cannot be issued because none are available.


**Error code:** B-ASSET-0x3307

**Cause.** Buffer stock has dropped below the 4 percent reorder trigger and no order was raised in time..

**Resolution.** Raise the replenishment order immediately, allowing for the 13 working day procurement lead time. Offer the user a temporary loan device from the short term pool so work is not blocked. Escalate to IT Asset Management so the reorder trigger can be checked for why it did not fire.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A leaver's laptop has not been returned two weeks after their leaving date.


**Error code:** B-RET-4150

**Cause.** The return was not arranged within the 3 working day window and no collection was booked..

**Resolution.** Contact the former employee's line manager with the asset tag and serial number and book a collection. Keep the asset in Awaiting Return status so it remains visible on the overdue report. Escalate to IT Asset Management and Information Security if the device is still outstanding after a second request, so the data on it can be assessed.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A disposal batch cannot be closed in the asset register.


**Cause.** One or more drive serial numbers in the batch have no matching certificate of destruction attached..

**Resolution.** List the serial numbers with no certificate and request the missing documents from the disposal supplier. Hold the batch open until every drive is covered. Escalate to IT Asset Management if the supplier cannot produce a certificate for a drive, because the asset cannot be recorded as Disposed without one.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for IT Asset Management to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A device in use has no record in the asset register.

Reference: B-SNOW-6621.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow IT Asset Management and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to IT Asset Management citing the reference above.

### Diagnostics for: A replacement laptop cannot be issued because none are available.

Reference: B-ASSET-0x3307.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow IT Asset Management and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to IT Asset Management citing the reference above.

### Diagnostics for: A leaver's laptop has not been returned two weeks after their leaving 

Reference: B-RET-4150.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow IT Asset Management and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to IT Asset Management citing the reference above.

### Diagnostics for: A disposal batch cannot be closed in the asset register.

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow IT Asset Management and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to IT Asset Management citing the reference above.

## Worked examples

### Example: A device in use has no record in the asset register.

A user at Dublin contacts the service desk reporting that a device in use has no record in the asset register.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The device was issued before tagging, so the register record was never created.. Following the documented resolution, capture the serial number and model, create the missing asset record and apply an asset tag at the next opportunity. Confirm the current holder and the approximate issue date so the refresh clock can be set. Escalate to IT Asset Management if the device cannot be matched to any purchase order, as that suggests an unapproved purchase.

The agent records the diagnosis against the ticket, confirms with priya.iyer@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to IT Asset Management was needed.

### Example: A replacement laptop cannot be issued because none are available.

A user at Dublin contacts the service desk reporting that a replacement laptop cannot be issued because none are available.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Buffer stock has dropped below the 4 percent reorder trigger and no order was raised in time.. Following the documented resolution, raise the replenishment order immediately, allowing for the 13 working day procurement lead time. Offer the user a temporary loan device from the short term pool so work is not blocked. Escalate to IT Asset Management so the reorder trigger can be checked for why it did not fire.

The agent records the diagnosis against the ticket, confirms with tobias.whitfield@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to IT Asset Management was needed.

### Example: A leaver's laptop has not been returned two weeks after their leaving 

A user at Manchester contacts the service desk reporting that a leaver's laptop has not been returned two weeks after their leaving date.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The return was not arranged within the 3 working day window and no collection was booked.. Following the documented resolution, contact the former employee's line manager with the asset tag and serial number and book a collection. Keep the asset in Awaiting Return status so it remains visible on the overdue report. Escalate to IT Asset Management and Information Security if the device is still outstanding after a second request, so the data on it can be assessed.

The agent records the diagnosis against the ticket, confirms with viktor.sorensen@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to IT Asset Management was needed.

### Example: receiving and tagging a new device

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about IT asset lifecycle management. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the standard laptop refresh cycle is flexible or negotiable per user.**

It is not. The standard laptop refresh cycle is 46 months from the purchase date, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the monitor and peripheral refresh cycle is flexible or negotiable per user.**

It is not. The monitor and peripheral refresh cycle is 7 years from the purchase date, or on failure if sooner, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the asset tag format is flexible or negotiable per user.**

It is not. The asset tag format is MG followed by a six digit sequence, for example MG004821, applied before the device leaves the build room, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the buffer stock level for standard laptops is flexible or negotiable per user.**

It is not. The buffer stock level for standard laptops is 9 percent of the deployed fleet, with a reorder trigger at 4 percent, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: IT Asset Management can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to IT asset lifecycle management, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to IT Asset Management.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of ServiceNow IT Asset Management did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, IT Asset Management produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about IT asset lifecycle management unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

IT Asset Management runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**When will my laptop be replaced?**

Standard laptops are refreshed at 46 months from their purchase date, and monitors and peripherals at 7 years or on failure.

**How long does a new laptop take to arrive?**

A standard laptop takes 13 working days from approved purchase order to arriving in the build room.

**What happens to the data on a retired laptop?**

Every storage device gets a certified three pass overwrite, and any drive that fails is physically destroyed, with a certificate recorded either way.

**When do I need to return a laptop if I leave?**

Devices must be received back into the build room within 3 working days of the leaving date.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, IT Asset Management will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is IT Asset Management, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for ServiceNow IT Asset Management, engaged by IT Asset Management only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

IT Asset Management produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about IT asset lifecycle management. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Check the delivered serial numbers against the purchase order before signing for the delivery.
- [ ] Create the asset record and assign the next asset tag in the MG sequence.
- [ ] Identify devices that have reached 46 months from their purchase date.
- [ ] Contact the device holder and agree a swap date at least a week ahead.
- [ ] Confirm the asset is in Pending Disposal status and has no outstanding assignment.
- [ ] Run the certified three pass overwrite on every storage device.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- When will my laptop be replaced? Standard laptops are refreshed at 46 months from their purchase date, and monitors and peripherals at 7 years or on failure.
- How long does a new laptop take to arrive? A standard laptop takes 13 working days from approved purchase order to arriving in the build room.
- What happens to the data on a retired laptop? Every storage device gets a certified three pass overwrite, and any drive that fails is physically destroyed, with a certificate recorded either way.
- When do I need to return a laptop if I leave? Devices must be received back into the build room within 3 working days of the leaving date.

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
| 2.1 | 2026-02-09 | IT Asset Management | Annual review; figures confirmed against the running configuration of ServiceNow IT Asset Management. |
