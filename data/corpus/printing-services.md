---
title: Printing Services Runbook
doc_type: runbook
category: hardware
owner: Print Services
version: 2.1
review_date: 2027-02-09
---

# Printing Services Runbook

Owner: Print Services | System of record: PaperCut MF | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages printing services. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Print Services team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the hardware estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

PaperCut MF is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of PaperCut MF. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Follow-me printing**  
A print model where a job is held centrally and only prints once the user authenticates at any Meridian Group multifunction device with their badge or PIN.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Print queue**  
The named shared queue on the print servers that accepts jobs from client devices and holds them until release or expiry.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Scan to email**  
The multifunction device feature that sends a scanned document directly to the signed-in user mailbox at firstname.lastname@meridiangroup.example.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Print Services. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Print Services** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Print Services rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. All Meridian Group printing must go through the follow-me queue, and direct IP printing to a device is only permitted for approved production printers.

Agents should treat this as non-negotiable. Print Services configures PaperCut MF to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Print Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 2. Colour printing is enabled by default for every user up to the monthly allowance, and additional colour volume requires line manager approval.

In practice this means the following. Evidence that the control is operating is collected automatically from PaperCut MF and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 3. Print drivers must be deployed through Microsoft Intune, and users must not install vendor drivers downloaded from the internet.

This has been the standing position since the last review. Evidence that the control is operating is collected automatically from PaperCut MF and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 4. Confidential documents must be released at the device by the document owner and must not be left on the output tray.

The reasoning behind this is straightforward. Evidence that the control is operating is collected automatically from PaperCut MF and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Print Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 5. Print Services must review device placement and volume reporting each quarter and remove devices printing fewer than 200 pages a month.

There is a documented exception route, described later in this document. Evidence that the control is operating is collected automatically from PaperCut MF and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Print Services configures in PaperCut MF. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Follow-me print job hold time | 12 hours before an unreleased job is deleted from the queue |
| Minimum supported print driver package version | 7.1.4 of the Meridian Group universal driver package |
| Maximum scan to email attachment size | 25 MB per scanned document |
| Monthly colour printing allowance per user | 400 colour pages per calendar month |
| Printer fault response target | 8 working hours for a device that is the only printer on a floor |
| Secure release PIN length | 6 digits, set by the user in the PaperCut MF web portal |

**Follow-me print job hold time.** The follow-me print job hold time is 12 hours before an unreleased job is deleted from the queue. Print Services set this figure in consultation with Information Security, and it is reviewed annually.

**Minimum supported print driver package version.** The minimum supported print driver package version is 7.1.4 of the Meridian Group universal driver package. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Maximum scan to email attachment size.** The maximum scan to email attachment size is 25 MB per scanned document. This is configured centrally in PaperCut MF and is not adjustable per user or per team.

**Monthly colour printing allowance per user.** The monthly colour printing allowance per user is 400 colour pages per calendar month. Print Services set this figure in consultation with Information Security, and it is reviewed annually.

**Printer fault response target.** The printer fault response target is 8 working hours for a device that is the only printer on a floor. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Secure release PIN length.** The secure release PIN length is 6 digits, set by the user in the PaperCut MF web portal. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of PaperCut MF diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Print Services, and reviewed annually with Information Security.

## Architecture and dependencies

PaperCut MF is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to PaperCut MF follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Print Services maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Print Services raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to PaperCut MF, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Print Services implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Print Services rather than skipping it.

### Add a new multifunction device to the follow-me estate

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the network port is active and record the device serial number and floor location.
2. Register the device in PaperCut MF and assign it to the correct site and cost centre.
3. Add the device to the follow-me queue and set colour and duplex defaults.
4. Install the embedded PaperCut MF software on the device and test badge release.
5. Run a test print and a test scan to email, then publish the device name to the floor distribution list.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Deploy an updated print driver package

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Package the new universal driver version and test it against two device models in the pilot ring.
2. Upload the package to Microsoft Intune and assign it to the pilot device group.
3. Monitor install success for five working days and review any reported failures.
4. Expand the assignment to all managed laptops once the pilot ring reports no regressions.
5. Retire the previous driver package and update the minimum supported version in the runbook.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Set up scan to email for a user

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the user mailbox is active and uses the standard Meridian Group address format.
2. Check that the user has a badge registered or a secure release PIN set in PaperCut MF.
3. Ask the user to authenticate at the device and open the scan to email workflow.
4. Send a one page test scan and confirm it arrives in the user mailbox.
5. Advise the user to split documents that would exceed the attachment limit.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Print Services with the diagnostic output attached rather than retrying the same steps.

### Symptom: A user releases a job at the device and it prints the first page then stops with a device error.


**Error code:** A-PCMF-1142

**Cause.** The device firmware is behind the baseline and is rejecting the current driver page description language..

**Resolution.** Update the device firmware to the vendor baseline during the next maintenance window and reprint the job. As an interim step, release the job on a different device on the same floor. Escalate to the print hardware vendor if the fault repeats after the firmware update.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: Jobs sent from a laptop never appear in the follow-me queue at any device.


**Error code:** A-DRV-0x80070705

**Cause.** The client is still using an old driver package that points at a decommissioned print server..

**Resolution.** Remove the old printer object from the laptop, then push the current driver package from Microsoft Intune and confirm the version is 7.1.4 or later. Send a test print and release it at the nearest device. Escalate to Print Services second line if the queue still does not receive jobs after the redeployment.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: Scan to email completes at the device but no email ever arrives.


**Error code:** A-SCAN-SMTP-554

**Cause.** The scanned file exceeds the attachment limit and the mail relay is dropping the message..

**Resolution.** Ask the user to rescan at a lower resolution or split the document so each file stays under the attachment limit. Confirm delivery of the smaller test scan before closing. Escalate to Messaging Services if a small test scan also fails to arrive, because that points at the mail relay rather than the device.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: Several users on one floor report that printing hangs with a spooler error after a Windows update.


**Error code:** A-PRN-0x0000011B

**Cause.** A point and print restriction introduced by the update is blocking the queue connection..

**Resolution.** Confirm the current driver package is installed locally rather than pulled from the server, then restart the print spooler service on the affected laptops. Verify the Intune configuration profile for point and print is applied. Escalate to Desktop Support if more than five users on the same floor are still affected after the profile check.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Print Services to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A user releases a job at the device and it prints the first page then 

Reference: A-PCMF-1142.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of PaperCut MF and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Print Services citing the reference above.

### Diagnostics for: Jobs sent from a laptop never appear in the follow-me queue at any dev

Reference: A-DRV-0x80070705.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of PaperCut MF and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Print Services citing the reference above.

### Diagnostics for: Scan to email completes at the device but no email ever arrives.

Reference: A-SCAN-SMTP-554.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of PaperCut MF and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Print Services citing the reference above.

### Diagnostics for: Several users on one floor report that printing hangs with a spooler e

Reference: A-PRN-0x0000011B.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of PaperCut MF and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Print Services citing the reference above.

## Worked examples

### Example: A user releases a job at the device and it prints the first page then 

A user at Remote contacts the service desk reporting that a user releases a job at the device and it prints the first page then stops with a device error.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The device firmware is behind the baseline and is rejecting the current driver page description language.. Following the documented resolution, update the device firmware to the vendor baseline during the next maintenance window and reprint the job. As an interim step, release the job on a different device on the same floor. Escalate to the print hardware vendor if the fault repeats after the firmware update.

The agent records the diagnosis against the ticket, confirms with yusuf.moreau@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Print Services was needed.

### Example: Jobs sent from a laptop never appear in the follow-me queue at any dev

A user at Manchester contacts the service desk reporting that jobs sent from a laptop never appear in the follow-me queue at any device.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The client is still using an old driver package that points at a decommissioned print server.. Following the documented resolution, remove the old printer object from the laptop, then push the current driver package from Microsoft Intune and confirm the version is 7.1.4 or later. Send a test print and release it at the nearest device. Escalate to Print Services second line if the queue still does not receive jobs after the redeployment.

The agent records the diagnosis against the ticket, confirms with jonas.novak@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Print Services was needed.

### Example: Scan to email completes at the device but no email ever arrives.

A user at Manchester contacts the service desk reporting that scan to email completes at the device but no email ever arrives.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The scanned file exceeds the attachment limit and the mail relay is dropping the message.. Following the documented resolution, ask the user to rescan at a lower resolution or split the document so each file stays under the attachment limit. Confirm delivery of the smaller test scan before closing. Escalate to Messaging Services if a small test scan also fails to arrive, because that points at the mail relay rather than the device.

The agent records the diagnosis against the ticket, confirms with renu.nakamura@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Print Services was needed.

### Example: add a new multifunction device to the follow-me estate

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about printing services. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the follow-me print job hold time is flexible or negotiable per user.**

It is not. The follow-me print job hold time is 12 hours before an unreleased job is deleted from the queue, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the minimum supported print driver package version is flexible or negotiable per user.**

It is not. The minimum supported print driver package version is 7.1.4 of the Meridian Group universal driver package, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the maximum scan to email attachment size is flexible or negotiable per user.**

It is not. The maximum scan to email attachment size is 25 MB per scanned document, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the monthly colour printing allowance per user is flexible or negotiable per user.**

It is not. The monthly colour printing allowance per user is 400 colour pages per calendar month, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Print Services can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to printing services, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Print Services.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of PaperCut MF did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Print Services produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about printing services unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Print Services runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How long do my print jobs wait at the device?**

Jobs are held for 12 hours and are deleted automatically if you do not release them in that time.

**How much colour printing can I do?**

Every user has an allowance of 400 colour pages per calendar month, and more requires line manager approval.

**Why was my scan rejected?**

Scan to email accepts attachments up to 25 MB, so a long or high resolution scan needs to be split or rescanned at a lower setting.

**Can I install a printer driver myself?**

No, drivers are deployed through Microsoft Intune and the supported package is version 7.1.4 or later.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Print Services will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Print Services, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for PaperCut MF, engaged by Print Services only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Print Services produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about printing services. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the network port is active and record the device serial number and floor location.
- [ ] Register the device in PaperCut MF and assign it to the correct site and cost centre.
- [ ] Package the new universal driver version and test it against two device models in the pilot ring.
- [ ] Upload the package to Microsoft Intune and assign it to the pilot device group.
- [ ] Confirm the user mailbox is active and uses the standard Meridian Group address format.
- [ ] Check that the user has a badge registered or a secure release PIN set in PaperCut MF.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How long do my print jobs wait at the device? Jobs are held for 12 hours and are deleted automatically if you do not release them in that time.
- How much colour printing can I do? Every user has an allowance of 400 colour pages per calendar month, and more requires line manager approval.
- Why was my scan rejected? Scan to email accepts attachments up to 25 MB, so a long or high resolution scan needs to be split or rescanned at a lower setting.
- Can I install a printer driver myself? No, drivers are deployed through Microsoft Intune and the supported package is version 7.1.4 or later.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Print Services | First published version. |
| 1.1 | 2024-11-02 | Print Services | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Print Services | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Print Services | Annual review; figures confirmed against the running configuration of PaperCut MF. |
