---
title: Phishing and Email Security Policy
doc_type: policy
category: security
owner: Information Security
version: 2.1
review_date: 2027-02-09
---

# Phishing and Email Security Policy

Owner: Information Security | System of record: Microsoft Defender for Office 365 | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages phishing and email security. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Information Security team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the security estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Microsoft Defender for Office 365 is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Microsoft Defender for Office 365. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Business email compromise**  
An attack in which a trusted sender's account or display name is abused to request a payment or a data change. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Quarantine**  
A holding area where a suspicious message is stored unopened so that it cannot reach the recipient's mailbox. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Safe link rewriting**  
The replacement of a URL in an inbound message with a checking service address that inspects the destination at the moment of the click. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

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

### 1. Suspicious messages must be reported with the Report Phishing button and must not be forwarded to colleagues.

This is enforced technically wherever the platform allows it. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Security will either confirm the control applies or sponsor an exception, usually within a few working days. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 2. Employees must never act on a payment or bank detail change request received by email without separate verbal verification.

There is a documented exception route, described later in this document. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Security will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 3. Password and credential entry is only permitted on pages reached from a bookmark or from the service portal, never from an email link.

This has been the standing position since the last review. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Security will either confirm the control applies or sponsor an exception, usually within a few working days. Where the control cannot be enforced technically, Information Security monitors for breaches and follows up with the individual and their line manager.

### 4. Automatic external forwarding of company mail to a personal address is prohibited for all employees.

Agents should treat this as non-negotiable. Evidence that the control is operating is collected automatically from Microsoft Defender for Office 365 and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 5. Employees who report a simulated phishing message are never penalised, and reporting rates are measured at team level only.

The reasoning behind this is straightforward. This statement has been tested against the current configuration of Microsoft Defender for Office 365. Where a platform change makes it unenforceable, Information Security raises a risk acceptance rather than quietly dropping the control. Information Security reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Information Security configures in Microsoft Defender for Office 365. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Reporting route for suspicious mail | the Report Phishing button in Outlook, which delivers the message to the Information Security triage queue |
| Phishing triage service level | a first assessment within 45 minutes during business hours and within 3 hours out of hours |
| Quarantine release approval | Information Security only; line managers and the service desk cannot release a quarantined message |
| Quarantine retention period | 22 days, after which quarantined messages are deleted automatically |
| Blocked attachment types | a list of 18 executable and script extensions, including .exe, .js, .vbs, .scr and .iso |
| Simulation programme frequency | a phishing simulation to every employee once per quarter, with a reporting rate target of 65 percent |

**Reporting route for suspicious mail.** The reporting route for suspicious mail is the Report Phishing button in Outlook, which delivers the message to the Information Security triage queue. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Phishing triage service level.** The phishing triage service level is a first assessment within 45 minutes during business hours and within 3 hours out of hours. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Quarantine release approval.** The quarantine release approval is Information Security only; line managers and the service desk cannot release a quarantined message. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Quarantine retention period.** The quarantine retention period is 22 days, after which quarantined messages are deleted automatically. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Blocked attachment types.** The blocked attachment types is a list of 18 executable and script extensions, including .exe, .js, .vbs, .scr and .iso. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Simulation programme frequency.** The simulation programme frequency is a phishing simulation to every employee once per quarter, with a reporting rate target of 65 percent. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Microsoft Defender for Office 365 diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Information Security, and reviewed annually with Information Security.

## Architecture and dependencies

Microsoft Defender for Office 365 is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Microsoft Defender for Office 365 follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Information Security maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Information Security raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Microsoft Defender for Office 365, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Information Security implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Information Security rather than skipping it.

### Reporting a suspicious message

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Do not click any link or open any attachment in the message.
2. Select the message in Outlook and use the Report Phishing button.
3. Confirm the report when prompted, which also removes the message from the mailbox.
4. Tell the service desk separately if credentials were already entered or an attachment was already opened.
5. Wait for the triage outcome notice rather than retrieving the message from the deleted items folder.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Requesting the release of a quarantined message

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Note the quarantine notification identifier and the sender address from the daily digest.
2. Raise a request in the service portal under Email Security and attach the identifier.
3. State why the message is expected and what business process depends on it.
4. Information Security inspects the message and its attachments in the analysis sandbox.
5. Information Security releases the message to the single recipient or confirms that it will stay blocked.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Responding to a confirmed credential phishing click

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Reset the affected user's password immediately and revoke all active sessions.
2. Check the mailbox for newly created forwarding or inbox rules and remove any found.
3. Search the mail flow for other recipients of the same campaign and purge the message.
4. Add the sending domain and any payload URL to the block list.
5. Raise a security incident at the appropriate severity if company data was submitted.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Information Security with the diagnostic output attached rather than retrying the same steps.

### Symptom: A legitimate supplier invoice is quarantined every month.


**Error code:** B-DEF-5503

**Cause.** The supplier's sending domain has no valid sender authentication record, so each message scores as a spoof..

**Resolution.** Release the current message through Information Security, then ask the supplier to publish a valid sender authentication record. Add a narrowly scoped allow entry for that sender while the supplier makes the change, with a review date. Escalate to Information Security if the supplier refuses, as a permanent bypass needs a recorded risk acceptance.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: The Report Phishing button is missing from the Outlook ribbon.


**Error code:** B-OL-0x8004010F

**Cause.** The reporting add-in has not been deployed to the user's mailbox or the client is running in a cached offline state..

**Resolution.** Ask the user to restart Outlook and confirm they are signed in with their work account. If the button is still absent, check the add-in deployment for that mailbox and redeploy it. In the meantime, have the user send the message as an attachment to the service desk so triage is not delayed beyond the 45 minute target.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A user cannot open an attachment that a colleague says they received successfully.


**Error code:** B-ATT-1189

**Cause.** The attachment uses one of the 18 blocked executable or script extensions and was stripped on delivery..

**Resolution.** Confirm the extension against the blocked list and tell the user the file will not be delivered by email. Ask the sender to share the file through the approved file sharing service instead. Escalate to Information Security only if the file is genuinely required in its executable form, so a controlled transfer can be arranged.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: Quarantine digest links return a message that the item is no longer available.


**Cause.** The message passed the 22 day quarantine retention period and was deleted automatically..

**Resolution.** Explain that quarantined mail is removed after 22 days and cannot be recovered afterwards. Ask the sender to resend the message so it can be triaged within the retention window. Record the case if the same sender is repeatedly quarantined, so the sender can be assessed properly.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Information Security to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A legitimate supplier invoice is quarantined every month.

Reference: B-DEF-5503.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Defender for Office 365 and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: The Report Phishing button is missing from the Outlook ribbon.

Reference: B-OL-0x8004010F.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Defender for Office 365 and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: A user cannot open an attachment that a colleague says they received s

Reference: B-ATT-1189.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Defender for Office 365 and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: Quarantine digest links return a message that the item is no longer av

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Defender for Office 365 and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

## Worked examples

### Example: A legitimate supplier invoice is quarantined every month.

A user at London HQ contacts the service desk reporting that a legitimate supplier invoice is quarantined every month.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The supplier's sending domain has no valid sender authentication record, so each message scores as a spoof.. Following the documented resolution, release the current message through Information Security, then ask the supplier to publish a valid sender authentication record. Add a narrowly scoped allow entry for that sender while the supplier makes the change, with a review date. Escalate to Information Security if the supplier refuses, as a permanent bypass needs a recorded risk acceptance.

The agent records the diagnosis against the ticket, confirms with aisha.moreau@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: The Report Phishing button is missing from the Outlook ribbon.

A user at Manchester contacts the service desk reporting that the Report Phishing button is missing from the Outlook ribbon.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The reporting add-in has not been deployed to the user's mailbox or the client is running in a cached offline state.. Following the documented resolution, ask the user to restart Outlook and confirm they are signed in with their work account. If the button is still absent, check the add-in deployment for that mailbox and redeploy it. In the meantime, have the user send the message as an attachment to the service desk so triage is not delayed beyond the 45 minute target.

The agent records the diagnosis against the ticket, confirms with yusuf.kowalski@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: A user cannot open an attachment that a colleague says they received s

A user at Singapore contacts the service desk reporting that a user cannot open an attachment that a colleague says they received successfully.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The attachment uses one of the 18 blocked executable or script extensions and was stripped on delivery.. Following the documented resolution, confirm the extension against the blocked list and tell the user the file will not be delivered by email. Ask the sender to share the file through the approved file sharing service instead. Escalate to Information Security only if the file is genuinely required in its executable form, so a controlled transfer can be arranged.

The agent records the diagnosis against the ticket, confirms with tariq.haddad@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: reporting a suspicious message

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about phishing and email security. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the reporting route for suspicious mail is flexible or negotiable per user.**

It is not. The reporting route for suspicious mail is the Report Phishing button in Outlook, which delivers the message to the Information Security triage queue, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the phishing triage service level is flexible or negotiable per user.**

It is not. The phishing triage service level is a first assessment within 45 minutes during business hours and within 3 hours out of hours, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the quarantine release approval is flexible or negotiable per user.**

It is not. The quarantine release approval is Information Security only; line managers and the service desk cannot release a quarantined message, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the quarantine retention period is flexible or negotiable per user.**

It is not. The quarantine retention period is 22 days, after which quarantined messages are deleted automatically, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Information Security can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to phishing and email security, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Information Security.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Microsoft Defender for Office 365 did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Information Security produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about phishing and email security unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Information Security runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**What should I do with an email I think is phishing?**

Use the Report Phishing button in Outlook and do not forward the message to anyone else.

**How soon will my phishing report be looked at?**

Reports are first assessed within 45 minutes during business hours and within 3 hours outside business hours.

**Can my manager release a blocked email for me?**

No, only Information Security can release a quarantined message, and quarantined items are deleted after 22 days.

**Will I be in trouble for failing a phishing simulation?**

No, the quarterly simulations are measured at team level against a 65 percent reporting target, and individuals are never penalised.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Information Security will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Information Security, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Microsoft Defender for Office 365, engaged by Information Security only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Information Security produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about phishing and email security. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Do not click any link or open any attachment in the message.
- [ ] Select the message in Outlook and use the Report Phishing button.
- [ ] Note the quarantine notification identifier and the sender address from the daily digest.
- [ ] Raise a request in the service portal under Email Security and attach the identifier.
- [ ] Reset the affected user's password immediately and revoke all active sessions.
- [ ] Check the mailbox for newly created forwarding or inbox rules and remove any found.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- What should I do with an email I think is phishing? Use the Report Phishing button in Outlook and do not forward the message to anyone else.
- How soon will my phishing report be looked at? Reports are first assessed within 45 minutes during business hours and within 3 hours outside business hours.
- Can my manager release a blocked email for me? No, only Information Security can release a quarantined message, and quarantined items are deleted after 22 days.
- Will I be in trouble for failing a phishing simulation? No, the quarterly simulations are measured at team level against a 65 percent reporting target, and individuals are never penalised.

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
| 2.1 | 2026-02-09 | Information Security | Annual review; figures confirmed against the running configuration of Microsoft Defender for Office 365. |
