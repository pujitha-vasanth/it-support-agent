---
title: Laptop Provisioning Runbook
doc_type: runbook
category: hardware
owner: Desktop Support
version: 2.1
review_date: 2027-02-09
---

# Laptop Provisioning Runbook

Owner: Desktop Support | System of record: Microsoft Intune | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages laptop provisioning. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Desktop Support team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the hardware estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Microsoft Intune is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Microsoft Intune. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Autopilot enrolment**  
The process by which a factory-fresh laptop registers itself with Microsoft Intune on first boot and pulls the Meridian Group configuration profile without a technician imaging it manually.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Golden build**  
The approved Windows image and application baseline that Desktop Support validates each quarter and applies to every standard Meridian Group laptop.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Handover record**  
The signed acceptance entry in ServiceNow that links a named asset tag to a named employee and starts the warranty and refresh clock.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Desktop Support. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Desktop Support** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Desktop Support rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Every Meridian Group laptop must be enrolled in Microsoft Intune before it is handed to an employee, and unenrolled devices must not be connected to corporate resources.

This has been the standing position since the last review. Evidence that the control is operating is collected automatically from Microsoft Intune and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 2. Desktop Support must record the asset tag, serial number and assigned user in ServiceNow on the same working day as handover.

Agents should treat this as non-negotiable. Desktop Support configures Microsoft Intune to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 3. Local administrator rights must not be granted as part of a standard build and require a separate approved exception request.

In practice this means the following. Desktop Support configures Microsoft Intune to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 4. Laptops returned by leavers must be wiped using the Intune fresh start action before they re-enter the spare pool.

The reasoning behind this is straightforward. Desktop Support configures Microsoft Intune to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 5. Requests received later than 2 working days before a start date are treated as expedited and must be approved by the Desktop Support team lead.

This is enforced technically wherever the platform allows it. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Desktop Support will either confirm the control applies or sponsor an exception, usually within a few working days. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Desktop Support configures in Microsoft Intune. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Standard laptop build time | 6 working hours from stock allocation to handover-ready |
| Standard laptop refresh cycle | 4 years from the purchase date recorded on the asset record |
| Minimum spare laptop buffer held by Desktop Support | 18 imaged spare devices across the Meridian Group sites |
| Expected Windows Autopilot enrolment window | 45 minutes from first boot on a wired connection |
| New starter handover deadline | 2 working days before the starter's first working day |
| Meridian Group laptop asset tag format | MG-LT- followed by five digits, for example MG-LT-04172 |

**Standard laptop build time.** The standard laptop build time is 6 working hours from stock allocation to handover-ready. Desktop Support set this figure in consultation with Information Security, and it is reviewed annually.

**Standard laptop refresh cycle.** The standard laptop refresh cycle is 4 years from the purchase date recorded on the asset record. This is configured centrally in Microsoft Intune and is not adjustable per user or per team.

**Minimum spare laptop buffer held by Desktop Support.** The minimum spare laptop buffer held by Desktop Support is 18 imaged spare devices across the Meridian Group sites. Desktop Support set this figure in consultation with Information Security, and it is reviewed annually.

**Expected Windows Autopilot enrolment window.** The expected Windows Autopilot enrolment window is 45 minutes from first boot on a wired connection. This is configured centrally in Microsoft Intune and is not adjustable per user or per team.

**New starter handover deadline.** The new starter handover deadline is 2 working days before the starter's first working day. This is configured centrally in Microsoft Intune and is not adjustable per user or per team.

**Meridian Group laptop asset tag format.** The Meridian Group laptop asset tag format is MG-LT- followed by five digits, for example MG-LT-04172. This is configured centrally in Microsoft Intune and is not adjustable per user or per team.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Microsoft Intune diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Desktop Support, and reviewed annually with Information Security.

## Architecture and dependencies

Microsoft Intune is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Microsoft Intune follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Desktop Support maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Desktop Support raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Microsoft Intune, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Desktop Support implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Desktop Support rather than skipping it.

### Build a standard new starter laptop

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Allocate a device from the spare pool and confirm the asset tag matches the ServiceNow stock record.
2. Connect the laptop to a wired port and power it on to begin Windows Autopilot enrolment.
3. Sign in with the starter's Entra ID account to trigger the Meridian Group configuration profile.
4. Confirm in the Intune portal that the device shows as compliant and that CrowdStrike has checked in.
5. Apply the asset tag label, complete the handover record in ServiceNow and set the device state to Assigned.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Expedite a laptop for a late new starter request

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise an expedited provisioning task in ServiceNow and link it to the original joiner request.
2. Obtain written approval from the Desktop Support team lead before taking a device from the spare buffer.
3. Build the device using the current golden build and skip only the optional departmental software.
4. Notify the hiring manager by email with the collection time and the asset tag.
5. Replenish the spare buffer by raising a purchase request the same working day.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Return a leaver laptop to the spare pool

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm with the line manager that no local data recovery is outstanding.
2. Issue the Intune fresh start action and wait for the device to report a successful wipe.
3. Inspect the chassis, keyboard and battery health and raise a repair task if any check fails.
4. Re-enrol the device through Autopilot and verify it reaches a compliant state.
5. Update the ServiceNow asset record to Spare and return the device to the stock cupboard.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Desktop Support with the diagnostic output attached rather than retrying the same steps.

### Symptom: Autopilot enrolment fails part way through the out of box experience and the laptop returns to the region screen.


**Error code:** A-AUTOPILOT-0x801C03F2

**Cause.** The device hardware hash was never uploaded to Intune, so the laptop is not recognised as a Meridian Group corporate device..

**Resolution.** Collect the hardware hash using the Get-WindowsAutopilotInfo script and upload it to Intune, then reset the device and retry enrolment. Allow a full synchronisation cycle before the second attempt. If enrolment fails again on the same serial number, escalate to the Intune administrators with the enrolment log bundle.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A required application in the golden build reports an install failure on a freshly built laptop.


**Error code:** A-0x80070643

**Cause.** The device is missing a prerequisite runtime because the application assignment ran before the dependency finished installing..

**Resolution.** Open the Intune device view, check the app install status and trigger a manual sync from the Company Portal. Reinstall the dependency first, then retry the failed application. If the same application fails on more than three builds in a week, escalate to the packaging queue so the dependency order can be corrected.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: The laptop shows as non-compliant in Intune immediately after handover even though the build completed.


**Error code:** A-INTUNE-0x87D1041C

**Cause.** BitLocker encryption has not finished, so the compliance policy evaluates the disk as unprotected..

**Resolution.** Check the BitLocker status on the device and leave it powered on and connected until encryption reaches one hundred per cent. Force a compliance evaluation from the Company Portal afterwards. Escalate to Desktop Support second line if the device is still non-compliant after two evaluation cycles.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A spare laptop refuses to start BitLocker and reports a trusted platform module problem.


**Error code:** A-TPM-0x80284001

**Cause.** The trusted platform module is in a cleared or locked state after the previous leaver wipe..

**Resolution.** Clear and reinitialise the trusted platform module from firmware settings, then update the firmware to the vendor baseline and retry the build. Record the firmware version in the asset record. If the module still fails, raise a warranty repair with the hardware vendor rather than returning the device to the spare pool.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Desktop Support to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: Autopilot enrolment fails part way through the out of box experience a

Reference: A-AUTOPILOT-0x801C03F2.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Intune and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Desktop Support citing the reference above.

### Diagnostics for: A required application in the golden build reports an install failure 

Reference: A-0x80070643.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Intune and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Desktop Support citing the reference above.

### Diagnostics for: The laptop shows as non-compliant in Intune immediately after handover

Reference: A-INTUNE-0x87D1041C.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Intune and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Desktop Support citing the reference above.

### Diagnostics for: A spare laptop refuses to start BitLocker and reports a trusted platfo

Reference: A-TPM-0x80284001.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Intune and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Desktop Support citing the reference above.

## Worked examples

### Example: Autopilot enrolment fails part way through the out of box experience a

A user at Rotterdam contacts the service desk reporting that autopilot enrolment fails part way through the out of box experience and the laptop returns to the region screen.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The device hardware hash was never uploaded to Intune, so the laptop is not recognised as a Meridian Group corporate device.. Following the documented resolution, collect the hardware hash using the Get-WindowsAutopilotInfo script and upload it to Intune, then reset the device and retry enrolment. Allow a full synchronisation cycle before the second attempt. If enrolment fails again on the same serial number, escalate to the Intune administrators with the enrolment log bundle.

The agent records the diagnosis against the ticket, confirms with amara.santos@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Desktop Support was needed.

### Example: A required application in the golden build reports an install failure 

A user at Rotterdam contacts the service desk reporting that a required application in the golden build reports an install failure on a freshly built laptop.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The device is missing a prerequisite runtime because the application assignment ran before the dependency finished installing.. Following the documented resolution, open the Intune device view, check the app install status and trigger a manual sync from the Company Portal. Reinstall the dependency first, then retry the failed application. If the same application fails on more than three builds in a week, escalate to the packaging queue so the dependency order can be corrected.

The agent records the diagnosis against the ticket, confirms with tobias.vasquez@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Desktop Support was needed.

### Example: The laptop shows as non-compliant in Intune immediately after handover

A user at Manchester contacts the service desk reporting that the laptop shows as non-compliant in Intune immediately after handover even though the build completed.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: BitLocker encryption has not finished, so the compliance policy evaluates the disk as unprotected.. Following the documented resolution, check the BitLocker status on the device and leave it powered on and connected until encryption reaches one hundred per cent. Force a compliance evaluation from the Company Portal afterwards. Escalate to Desktop Support second line if the device is still non-compliant after two evaluation cycles.

The agent records the diagnosis against the ticket, confirms with renu.demir@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Desktop Support was needed.

### Example: build a standard new starter laptop

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about laptop provisioning. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the standard laptop build time is flexible or negotiable per user.**

It is not. The standard laptop build time is 6 working hours from stock allocation to handover-ready, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the standard laptop refresh cycle is flexible or negotiable per user.**

It is not. The standard laptop refresh cycle is 4 years from the purchase date recorded on the asset record, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the minimum spare laptop buffer held by Desktop Support is flexible or negotiable per user.**

It is not. The minimum spare laptop buffer held by Desktop Support is 18 imaged spare devices across the Meridian Group sites, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the expected Windows Autopilot enrolment window is flexible or negotiable per user.**

It is not. The expected Windows Autopilot enrolment window is 45 minutes from first boot on a wired connection, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Desktop Support can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to laptop provisioning, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Desktop Support.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Microsoft Intune did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Desktop Support produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about laptop provisioning unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Desktop Support runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How long does a standard laptop build take?**

A standard build takes 6 working hours from stock allocation to the point where the device is ready for handover.

**When am I due a replacement laptop?**

Standard laptops are refreshed 4 years from the purchase date held on the asset record, and Desktop Support contacts you when your device is in scope.

**How much notice does Desktop Support need for a new starter?**

The request must reach Desktop Support so that the laptop is ready 2 working days before the starter's first working day, otherwise it is handled as an expedited request.

**Can I keep my laptop when I move teams?**

Yes, the device stays with you and Desktop Support simply updates the assigned cost centre on the handover record in ServiceNow.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Desktop Support will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Desktop Support, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Microsoft Intune, engaged by Desktop Support only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Desktop Support produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about laptop provisioning. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Allocate a device from the spare pool and confirm the asset tag matches the ServiceNow stock record.
- [ ] Connect the laptop to a wired port and power it on to begin Windows Autopilot enrolment.
- [ ] Raise an expedited provisioning task in ServiceNow and link it to the original joiner request.
- [ ] Obtain written approval from the Desktop Support team lead before taking a device from the spare buffer.
- [ ] Confirm with the line manager that no local data recovery is outstanding.
- [ ] Issue the Intune fresh start action and wait for the device to report a successful wipe.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How long does a standard laptop build take? A standard build takes 6 working hours from stock allocation to the point where the device is ready for handover.
- When am I due a replacement laptop? Standard laptops are refreshed 4 years from the purchase date held on the asset record, and Desktop Support contacts you when your device is in scope.
- How much notice does Desktop Support need for a new starter? The request must reach Desktop Support so that the laptop is ready 2 working days before the starter's first working day, otherwise it is handled as an expedited request.
- Can I keep my laptop when I move teams? Yes, the device stays with you and Desktop Support simply updates the assigned cost centre on the handover record in ServiceNow.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Desktop Support | First published version. |
| 1.1 | 2024-11-02 | Desktop Support | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Desktop Support | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Desktop Support | Annual review; figures confirmed against the running configuration of Microsoft Intune. |
