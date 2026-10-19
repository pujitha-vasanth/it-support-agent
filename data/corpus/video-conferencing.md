---
title: Video Conferencing Runbook
doc_type: runbook
category: productivity
owner: Collaboration Services
version: 2.1
review_date: 2027-02-09
---

# Video Conferencing Runbook

Owner: Collaboration Services | System of record: Zoom Workplace | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages video conferencing. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Collaboration Services team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the productivity estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Zoom Workplace is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Zoom Workplace. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Meeting room resource**  
A bookable physical room with a fixed video endpoint, held as a resource account in the calendar system. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Webinar licence**  
A separate Zoom entitlement required for events above 290 attendees, where participants join in view-only mode by default. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Dial-in bridge**  
The telephone access path into a meeting, used when a participant has no usable internet connection. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Collaboration Services. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Collaboration Services** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Collaboration Services rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. No meeting may be recorded without a spoken announcement and the on-screen recording indicator visible to all participants.

This is enforced technically wherever the platform allows it. Evidence that the control is operating is collected automatically from Zoom Workplace and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Collaboration Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 2. If any participant objects to being recorded, the recording must be stopped immediately.

There is a documented exception route, described later in this document. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Collaboration Services will either confirm the control applies or sponsor an exception, usually within a few working days. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 3. Cloud recordings are retained for 17 months and then deleted automatically.

The reasoning behind this is straightforward. Collaboration Services configures Zoom Workplace to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Where the control cannot be enforced technically, Collaboration Services monitors for breaches and follows up with the individual and their line manager.

### 4. Events expected to exceed 290 attendees must be run under a webinar licence booked at least 8 working days in advance.

This has been the standing position since the last review. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Collaboration Services will either confirm the control applies or sponsor an exception, usually within a few working days. Collaboration Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 5. Meeting room resources must not be booked for more people than the room's hard booking limit.

Agents should treat this as non-negotiable. Collaboration Services configures Zoom Workplace to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Collaboration Services configures in Zoom Workplace. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Standard meeting room capacity | 11 seats per medium room, with a hard booking limit of 14 people |
| Cloud recording retention | 17 months in cloud storage, then automatic deletion |
| Recording consent requirement | a spoken announcement plus the on-screen recording indicator, with any objection ending the recording |
| Dial-in number coverage | toll numbers in 22 countries, with toll-free dial-in in 6 of them |
| Large webinar licence threshold | any event expected to exceed 290 attendees must use a webinar licence, not a standard meeting |
| Webinar licence lead time | booked at least 8 working days before the event date |

**Standard meeting room capacity.** The standard meeting room capacity is 11 seats per medium room, with a hard booking limit of 14 people. Collaboration Services set this figure in consultation with Information Security, and it is reviewed annually.

**Cloud recording retention.** The cloud recording retention is 17 months in cloud storage, then automatic deletion. Collaboration Services set this figure in consultation with Information Security, and it is reviewed annually.

**Recording consent requirement.** The recording consent requirement is a spoken announcement plus the on-screen recording indicator, with any objection ending the recording. This is configured centrally in Zoom Workplace and is not adjustable per user or per team.

**Dial-in number coverage.** The dial-in number coverage is toll numbers in 22 countries, with toll-free dial-in in 6 of them. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Large webinar licence threshold.** The large webinar licence threshold is any event expected to exceed 290 attendees must use a webinar licence, not a standard meeting. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Webinar licence lead time.** The webinar licence lead time is booked at least 8 working days before the event date. This is configured centrally in Zoom Workplace and is not adjustable per user or per team.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Zoom Workplace diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Collaboration Services, and reviewed annually with Information Security.

## Architecture and dependencies

Zoom Workplace is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Zoom Workplace follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Collaboration Services maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Collaboration Services raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Zoom Workplace, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Collaboration Services implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Collaboration Services rather than skipping it.

### Recording a meeting lawfully

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Announce at the start that the session will be recorded and why.
2. Start the recording and confirm the on-screen indicator is visible to all participants.
3. Stop the recording immediately if any participant objects.
4. Share the recording only with the stated audience.
5. Note that the recording is deleted automatically after 17 months.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Booking a large webinar

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the expected attendance exceeds the 290 attendee threshold.
2. Raise a webinar licence request at least 8 working days before the event date.
3. Collaboration Services assigns the webinar licence to the host account.
4. Run a technical rehearsal with the host and any panellists.
5. Release the licence back to the pool after the event.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Setting up a room endpoint for a meeting

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Check the room resource is free and the attendee count is within the hard booking limit of 14.
2. Add the room resource to the calendar invitation so the endpoint receives the join details.
3. Confirm the endpoint shows the meeting on its panel 10 minutes before the start.
4. Test camera, microphone and screen share from the room controller.
5. Add the dial-in details to the invitation for anyone joining by telephone.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Collaboration Services with the diagnostic output attached rather than retrying the same steps.

### Symptom: The room endpoint does not show the meeting on its panel


**Error code:** C-VID-1163

**Cause.** The room resource was not added to the calendar invitation, so the endpoint never received the join details.

**Resolution.** Add the room resource to the invitation and send the update, then wait for the panel to refresh. If it still does not appear, join manually by entering the meeting identifier on the controller. Escalate to Collaboration Services if the room resource repeatedly fails to accept invitations.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A participant cannot hear anything after joining by telephone


**Error code:** C-VID-0x8007273D

**Cause.** The participant dialled a toll number for a country outside the 22 country coverage list and reached a dead bridge.

**Resolution.** Give the participant a dial-in number from the supported country list, or ask them to rejoin over the internet. Confirm audio before continuing the meeting. Escalate to Collaboration Services if a listed country's number is genuinely unreachable.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: The host cannot find a recording from last year


**Error code:** C-VID-4075

**Cause.** The recording passed the 17 month cloud retention period and was deleted automatically.

**Resolution.** Confirm the meeting date against the retention period and explain that the recording is not recoverable. Check whether the host saved a local copy or a transcript elsewhere. Escalate to Information Security only if the recording is subject to a legal hold.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: Attendees are blocked from joining a large all-hands session


**Cause.** The event was scheduled as a standard meeting even though attendance exceeds the 290 attendee threshold.

**Resolution.** Move the event to a webinar licence immediately and reissue the join link to attendees. Note that the 8 working day lead time has been missed, so a rehearsal is not possible. Escalate to Collaboration Services to source a spare webinar licence at short notice.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Collaboration Services to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: The room endpoint does not show the meeting on its panel

Reference: C-VID-1163.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Zoom Workplace and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Collaboration Services citing the reference above.

### Diagnostics for: A participant cannot hear anything after joining by telephone

Reference: C-VID-0x8007273D.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Zoom Workplace and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Collaboration Services citing the reference above.

### Diagnostics for: The host cannot find a recording from last year

Reference: C-VID-4075.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Zoom Workplace and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Collaboration Services citing the reference above.

### Diagnostics for: Attendees are blocked from joining a large all-hands session

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Zoom Workplace and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Collaboration Services citing the reference above.

## Worked examples

### Example: The room endpoint does not show the meeting on its panel

A user at London HQ contacts the service desk reporting that the room endpoint does not show the meeting on its panel. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The room resource was not added to the calendar invitation, so the endpoint never received the join details. Following the documented resolution, add the room resource to the invitation and send the update, then wait for the panel to refresh. If it still does not appear, join manually by entering the meeting identifier on the controller. Escalate to Collaboration Services if the room resource repeatedly fails to accept invitations.

The agent records the diagnosis against the ticket, confirms with paulo.mehta@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Collaboration Services was needed.

### Example: A participant cannot hear anything after joining by telephone

A user at Dublin contacts the service desk reporting that a participant cannot hear anything after joining by telephone. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The participant dialled a toll number for a country outside the 22 country coverage list and reached a dead bridge. Following the documented resolution, give the participant a dial-in number from the supported country list, or ask them to rejoin over the internet. Confirm audio before continuing the meeting. Escalate to Collaboration Services if a listed country's number is genuinely unreachable.

The agent records the diagnosis against the ticket, confirms with priya.lindqvist@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Collaboration Services was needed.

### Example: The host cannot find a recording from last year

A user at Remote contacts the service desk reporting that the host cannot find a recording from last year. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The recording passed the 17 month cloud retention period and was deleted automatically. Following the documented resolution, confirm the meeting date against the retention period and explain that the recording is not recoverable. Check whether the host saved a local copy or a transcript elsewhere. Escalate to Information Security only if the recording is subject to a legal hold.

The agent records the diagnosis against the ticket, confirms with kwame.novak@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Collaboration Services was needed.

### Example: recording a meeting lawfully

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about video conferencing. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the standard meeting room capacity is flexible or negotiable per user.**

It is not. The standard meeting room capacity is 11 seats per medium room, with a hard booking limit of 14 people, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the cloud recording retention is flexible or negotiable per user.**

It is not. The cloud recording retention is 17 months in cloud storage, then automatic deletion, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the recording consent requirement is flexible or negotiable per user.**

It is not. The recording consent requirement is a spoken announcement plus the on-screen recording indicator, with any objection ending the recording, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the dial-in number coverage is flexible or negotiable per user.**

It is not. The dial-in number coverage is toll numbers in 22 countries, with toll-free dial-in in 6 of them, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Collaboration Services can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to video conferencing, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Collaboration Services.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Zoom Workplace did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Collaboration Services produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about video conferencing unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Collaboration Services runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Do I have to tell people I am recording?**

Yes. You must announce it out loud and keep the on-screen recording indicator visible, and you must stop if anyone objects.

**How long do cloud recordings last?**

17 months, after which they are deleted automatically.

**When do I need a webinar licence instead of a meeting?**

Whenever you expect more than 290 attendees, and the licence must be booked at least 8 working days ahead.

**Can people join by telephone from anywhere?**

Toll dial-in is available in 22 countries, 6 of which also have toll-free numbers.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Collaboration Services will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Collaboration Services, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Zoom Workplace, engaged by Collaboration Services only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Collaboration Services produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about video conferencing. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Announce at the start that the session will be recorded and why.
- [ ] Start the recording and confirm the on-screen indicator is visible to all participants.
- [ ] Confirm the expected attendance exceeds the 290 attendee threshold.
- [ ] Raise a webinar licence request at least 8 working days before the event date.
- [ ] Check the room resource is free and the attendee count is within the hard booking limit of 14.
- [ ] Add the room resource to the calendar invitation so the endpoint receives the join details.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Do I have to tell people I am recording? Yes. You must announce it out loud and keep the on-screen recording indicator visible, and you must stop if anyone objects.
- How long do cloud recordings last? 17 months, after which they are deleted automatically.
- When do I need a webinar licence instead of a meeting? Whenever you expect more than 290 attendees, and the licence must be booked at least 8 working days ahead.
- Can people join by telephone from anywhere? Toll dial-in is available in 22 countries, 6 of which also have toll-free numbers.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Collaboration Services | First published version. |
| 1.1 | 2024-11-02 | Collaboration Services | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Collaboration Services | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Collaboration Services | Annual review; figures confirmed against the running configuration of Zoom Workplace. |
