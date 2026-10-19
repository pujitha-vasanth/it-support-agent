---
title: BYOD and Mobile Device Policy
doc_type: policy
category: mobile
owner: End User Computing
version: 2.1
review_date: 2027-02-09
---

# BYOD and Mobile Device Policy

Owner: End User Computing | System of record: Microsoft Intune | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages BYOD and mobile device. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The End User Computing team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the mobile estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Microsoft Intune is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Microsoft Intune. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Containerisation**  
The separation of company apps and data into a managed area of the device that is encrypted and controlled independently of personal content. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Selective wipe**  
The removal of only the company container and its data, leaving the owner's personal content untouched. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Compliance policy**  
The set of device conditions, such as operating system version and passcode strength, that must be met before company data is released to the device. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case End User Computing. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**End User Computing** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to End User Computing rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Company data may be accessed on a personal device only after the device is enrolled and reported compliant.

There is a documented exception route, described later in this document. Evidence that the control is operating is collected automatically from Microsoft Intune and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. End User Computing reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 2. Company data must remain inside the managed container and must not be copied into personal apps or personal cloud storage.

In practice this means the following. Evidence that the control is operating is collected automatically from Microsoft Intune and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 3. Employees must report a lost or stolen enrolled device to the service desk before any other action.

The reasoning behind this is straightforward. This statement has been tested against the current configuration of Microsoft Intune. Where a platform change makes it unenforceable, End User Computing raises a risk acceptance rather than quietly dropping the control. Where the control cannot be enforced technically, End User Computing monitors for breaches and follows up with the individual and their line manager.

### 4. The company will only ever perform a selective wipe of the company container on a personal device.

This has been the standing position since the last review. End User Computing configures Microsoft Intune to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 5. Rooted, jailbroken or developer-unlocked devices are refused access to company data with no exception process.

Agents should treat this as non-negotiable. End User Computing configures Microsoft Intune to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what End User Computing configures in Microsoft Intune. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Enrolment deadline for a new personal device | 5 working days from the access request being approved |
| Minimum operating system versions | iOS 17.4 or later and Android 14 or later; devices below these floors are blocked from company data |
| Supported device limit per employee | 2 personal mobile devices per employee |
| Passcode requirement on an enrolled personal device | a 6 digit passcode or biometric unlock, with a 5 minute screen lock timeout |
| Wipe scope on a personal device | selective wipe of the company container only; personal photos, messages and apps are never removed |
| Automatic unenrolment trigger | 19 consecutive days with no check-in to the management service |

**Enrolment deadline for a new personal device.** The enrolment deadline for a new personal device is 5 working days from the access request being approved. This is configured centrally in Microsoft Intune and is not adjustable per user or per team.

**Minimum operating system versions.** The minimum operating system versions is iOS 17.4 or later and Android 14 or later; devices below these floors are blocked from company data. End User Computing set this figure in consultation with Information Security, and it is reviewed annually.

**Supported device limit per employee.** The supported device limit per employee is 2 personal mobile devices per employee. This is configured centrally in Microsoft Intune and is not adjustable per user or per team.

**Passcode requirement on an enrolled personal device.** The passcode requirement on an enrolled personal device is a 6 digit passcode or biometric unlock, with a 5 minute screen lock timeout. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Wipe scope on a personal device.** The wipe scope on a personal device is selective wipe of the company container only; personal photos, messages and apps are never removed. This is configured centrally in Microsoft Intune and is not adjustable per user or per team.

**Automatic unenrolment trigger.** The automatic unenrolment trigger is 19 consecutive days with no check-in to the management service. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Microsoft Intune diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, End User Computing, and reviewed annually with Information Security.

## Architecture and dependencies

Microsoft Intune is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Microsoft Intune follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

End User Computing maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, End User Computing raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Microsoft Intune, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. End User Computing implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to End User Computing rather than skipping it.

### Enrolling a personal mobile device

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise a request in the service portal under Mobile Access and accept the acceptable use terms.
2. Confirm the device meets the operating system floor of iOS 17.4 or Android 14.
3. Install the company portal app from the device's official app store.
4. Sign in with the work account and complete the enrolment prompts.
5. Set a 6 digit passcode or biometric unlock when the device asks for one.
6. Confirm the device shows as compliant in the company portal before opening company mail.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Reporting a lost or stolen enrolled device

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Telephone the service desk as soon as the loss is discovered.
2. Confirm the device make, model and the approximate time it was last in the employee's possession.
3. The service desk revokes the work account's active sessions immediately.
4. End User Computing issues a selective wipe of the company container.
5. Confirm with the employee that personal content was not affected by the wipe.
6. Record the device as retired in the mobile inventory.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Removing a personal device from management

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise a request in the service portal under Mobile Access and choose Unenrol Device.
2. Confirm no company data is held outside the managed container.
3. End User Computing issues the selective wipe and confirms the container is removed.
4. Remove the company portal app from the device.
5. Confirm the device no longer appears against the employee's 2 device allowance.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to End User Computing with the diagnostic output attached rather than retrying the same steps.

### Symptom: Company mail stops syncing on a personal phone and the portal shows the device as not compliant.


**Error code:** B-INTUNE-0x87D1FDE8

**Cause.** The device operating system has fallen below the supported floor, or the required passcode has been removed..

**Resolution.** Ask the user to update to at least iOS 17.4 or Android 14 and to set a 6 digit passcode. Have them open the company portal and run a compliance check so the result is re-evaluated. Escalate to End User Computing if the device still reports non-compliant after a successful update and check.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: Enrolment fails at sign in with a message that the device cannot be registered.


**Error code:** B-INTUNE-0x80180014

**Cause.** The employee already has 2 enrolled personal devices, which is the maximum allowed..

**Resolution.** Check the employee's enrolled devices and identify any device no longer in use. Unenrol the retired device, then retry enrolment on the new one. Escalate to End User Computing only where a genuine business case exists for a third device, as the limit needs an owner decision.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A device disappeared from the management console on its own.


**Error code:** B-MDM-3374

**Cause.** The device went 19 consecutive days without checking in and was unenrolled automatically..

**Resolution.** Explain that automatic unenrolment happens after 19 days with no check-in and that the device must be enrolled again. Walk the user through a fresh enrolment in the company portal. Escalate if the device was in daily use, since repeated check-in failure points to a network or app problem rather than disuse.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: A user is worried that reporting a lost phone will delete their family photographs.


**Cause.** The user is unaware that only a selective wipe of the company container is performed on a personal device..

**Resolution.** Reassure the user that only the company container is removed and that personal photos, messages and apps are never touched. Complete the loss report without delay so sessions can be revoked. Record the reassurance given, as delayed reporting is the real risk here.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for End User Computing to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: Company mail stops syncing on a personal phone and the portal shows th

Reference: B-INTUNE-0x87D1FDE8.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Intune and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to End User Computing citing the reference above.

### Diagnostics for: Enrolment fails at sign in with a message that the device cannot be re

Reference: B-INTUNE-0x80180014.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Intune and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to End User Computing citing the reference above.

### Diagnostics for: A device disappeared from the management console on its own.

Reference: B-MDM-3374.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Intune and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to End User Computing citing the reference above.

### Diagnostics for: A user is worried that reporting a lost phone will delete their family

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Intune and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to End User Computing citing the reference above.

## Worked examples

### Example: Company mail stops syncing on a personal phone and the portal shows th

A user at Dublin contacts the service desk reporting that company mail stops syncing on a personal phone and the portal shows the device as not compliant.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The device operating system has fallen below the supported floor, or the required passcode has been removed.. Following the documented resolution, ask the user to update to at least iOS 17.4 or Android 14 and to set a 6 digit passcode. Have them open the company portal and run a compliance check so the result is re-evaluated. Escalate to End User Computing if the device still reports non-compliant after a successful update and check.

The agent records the diagnosis against the ticket, confirms with leila.whitfield@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to End User Computing was needed.

### Example: Enrolment fails at sign in with a message that the device cannot be re

A user at Singapore contacts the service desk reporting that enrolment fails at sign in with a message that the device cannot be registered.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The employee already has 2 enrolled personal devices, which is the maximum allowed.. Following the documented resolution, check the employee's enrolled devices and identify any device no longer in use. Unenrol the retired device, then retry enrolment on the new one. Escalate to End User Computing only where a genuine business case exists for a third device, as the limit needs an owner decision.

The agent records the diagnosis against the ticket, confirms with hana.mehta@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to End User Computing was needed.

### Example: A device disappeared from the management console on its own.

A user at Dublin contacts the service desk reporting that a device disappeared from the management console on its own.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The device went 19 consecutive days without checking in and was unenrolled automatically.. Following the documented resolution, explain that automatic unenrolment happens after 19 days with no check-in and that the device must be enrolled again. Walk the user through a fresh enrolment in the company portal. Escalate if the device was in daily use, since repeated check-in failure points to a network or app problem rather than disuse.

The agent records the diagnosis against the ticket, confirms with amara.demir@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to End User Computing was needed.

### Example: enrolling a personal mobile device

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about BYOD and mobile device. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the enrolment deadline for a new personal device is flexible or negotiable per user.**

It is not. The enrolment deadline for a new personal device is 5 working days from the access request being approved, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the minimum operating system versions is flexible or negotiable per user.**

It is not. The minimum operating system versions is iOS 17.4 or later and Android 14 or later; devices below these floors are blocked from company data, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the supported device limit per employee is flexible or negotiable per user.**

It is not. The supported device limit per employee is 2 personal mobile devices per employee, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the passcode requirement on an enrolled personal device is flexible or negotiable per user.**

It is not. The passcode requirement on an enrolled personal device is a 6 digit passcode or biometric unlock, with a 5 minute screen lock timeout, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: End User Computing can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to BYOD and mobile device, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to End User Computing.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Microsoft Intune did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, End User Computing produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about BYOD and mobile device unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

End User Computing runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Will the company wipe my whole phone?**

No, only the company container is removed by a selective wipe; your personal photos, messages and apps are never deleted.

**Which phone versions are supported?**

iOS 17.4 or later and Android 14 or later; anything older is blocked from company data.

**How many personal devices can I enrol?**

Two personal mobile devices per employee.

**Why did my phone drop out of management?**

Devices that do not check in for 19 consecutive days are unenrolled automatically and need to be enrolled again.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, End User Computing will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is End User Computing, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Microsoft Intune, engaged by End User Computing only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

End User Computing produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about BYOD and mobile device. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Raise a request in the service portal under Mobile Access and accept the acceptable use terms.
- [ ] Confirm the device meets the operating system floor of iOS 17.4 or Android 14.
- [ ] Telephone the service desk as soon as the loss is discovered.
- [ ] Confirm the device make, model and the approximate time it was last in the employee's possession.
- [ ] Raise a request in the service portal under Mobile Access and choose Unenrol Device.
- [ ] Confirm no company data is held outside the managed container.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Will the company wipe my whole phone? No, only the company container is removed by a selective wipe; your personal photos, messages and apps are never deleted.
- Which phone versions are supported? iOS 17.4 or later and Android 14 or later; anything older is blocked from company data.
- How many personal devices can I enrol? Two personal mobile devices per employee.
- Why did my phone drop out of management? Devices that do not check in for 19 consecutive days are unenrolled automatically and need to be enrolled again.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | End User Computing | First published version. |
| 1.1 | 2024-11-02 | End User Computing | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | End User Computing | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | End User Computing | Annual review; figures confirmed against the running configuration of Microsoft Intune. |
