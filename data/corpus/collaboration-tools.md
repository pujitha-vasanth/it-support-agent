---
title: Collaboration Tools Runbook
doc_type: runbook
category: productivity
owner: Collaboration Services
version: 2.1
review_date: 2027-02-09
---

# Collaboration Tools Runbook

Owner: Collaboration Services | System of record: Slack Enterprise Grid | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages collaboration tools. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Collaboration Services team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the productivity estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Slack Enterprise Grid is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Slack Enterprise Grid. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Enterprise Grid workspace**  
A separate Slack workspace inside the organisation's single Grid organisation, used to keep one business unit's channels apart from another's. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**External guest**  
A named person outside meridiangroup.example invited into specific channels only, with no access to the wider workspace or to search. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Dormant channel**  
A channel with no messages for 98 days, which is archived automatically but kept readable. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

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

### 1. Standard channel messages are retained for 26 months and then deleted automatically.

Agents should treat this as non-negotiable. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Collaboration Services will either confirm the control applies or sponsor an exception, usually within a few working days. Where the control cannot be enforced technically, Collaboration Services monitors for breaches and follows up with the individual and their line manager.

### 2. Private channels may only be created by a workspace owner in Collaboration Services.

This is enforced technically wherever the platform allows it. This statement has been tested against the current configuration of Slack Enterprise Grid. Where a platform change makes it unenforceable, Collaboration Services raises a risk acceptance rather than quietly dropping the control. Collaboration Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 3. External guest invitations last 63 days and may be renewed once by the channel owner.

The reasoning behind this is straightforward. Evidence that the control is operating is collected automatically from Slack Enterprise Grid and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Where the control cannot be enforced technically, Collaboration Services monitors for breaches and follows up with the individual and their line manager.

### 4. Confidential information must not be shared in any channel that contains an external guest.

There is a documented exception route, described later in this document. Evidence that the control is operating is collected automatically from Slack Enterprise Grid and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 5. Channels dormant for 98 days are archived automatically and must be unarchived through the service portal if needed again.

In practice this means the following. This statement has been tested against the current configuration of Slack Enterprise Grid. Where a platform change makes it unenforceable, Collaboration Services raises a risk acceptance rather than quietly dropping the control. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Collaboration Services configures in Slack Enterprise Grid. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Message retention period for standard channels | 26 months, after which messages are deleted automatically |
| Channel creation rights | any employee may create a public channel; private channels require a workspace owner in Collaboration Services |
| External guest access duration | 63 days per invitation, renewable once by the channel owner |
| Maximum external guests per channel | 18, above which Information Security approval is required |
| Dormant channel archive threshold | no messages for 98 days, at which point the channel is archived but not deleted |
| Approval route for a new workspace | departmental head approval plus Collaboration Services review, completed within 3 working days |

**Message retention period for standard channels.** The message retention period for standard channels is 26 months, after which messages are deleted automatically. Collaboration Services set this figure in consultation with Information Security, and it is reviewed annually.

**Channel creation rights.** The channel creation rights is any employee may create a public channel; private channels require a workspace owner in Collaboration Services. Collaboration Services set this figure in consultation with Information Security, and it is reviewed annually.

**External guest access duration.** The external guest access duration is 63 days per invitation, renewable once by the channel owner. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Maximum external guests per channel.** The maximum external guests per channel is 18, above which Information Security approval is required. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Dormant channel archive threshold.** The dormant channel archive threshold is no messages for 98 days, at which point the channel is archived but not deleted. Collaboration Services set this figure in consultation with Information Security, and it is reviewed annually.

**Approval route for a new workspace.** The approval route for a new workspace is departmental head approval plus Collaboration Services review, completed within 3 working days. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Slack Enterprise Grid diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Collaboration Services, and reviewed annually with Information Security.

## Architecture and dependencies

Slack Enterprise Grid is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Slack Enterprise Grid follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Collaboration Services maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Collaboration Services raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Slack Enterprise Grid, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Collaboration Services implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Collaboration Services rather than skipping it.

### Creating a private channel

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise a request in the service portal under Collaboration, choosing Private Channel.
2. State the business purpose and the intended member list.
3. A Collaboration Services workspace owner creates the channel and sets the topic.
4. Add the requester as channel owner and the named members.
5. Confirm the retention setting matches the standard 26 month period.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Inviting an external guest

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the guest's organisation is covered by a signed non-disclosure agreement.
2. Check the channel currently holds fewer than 18 external guests.
3. Send the guest invitation from the channel, which grants 63 days of access.
4. Record the invitation and its expiry date in the channel topic.
5. Renew once if still needed, or let the access lapse.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Recovering an archived channel

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Search the archive list in the service portal for the channel name.
2. Confirm the requester was a member before archiving.
3. Unarchive the channel and restore the original member list.
4. Post a message so the 98 day dormancy clock restarts.
5. Notify the requester that history before the 26 month retention limit is not recoverable.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Collaboration Services with the diagnostic output attached rather than retrying the same steps.

### Symptom: A user cannot find messages from three years ago


**Error code:** C-SLK-2270

**Cause.** Standard channel retention is 26 months, so the messages have already been deleted.

**Resolution.** Explain that the retention period has passed and that deleted messages are not recoverable from the product. Check whether the content exists in an approved document store instead. Escalate to Information Security only if the request is part of a legal hold, which has its own process.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: An external guest reports their invitation link no longer works


**Error code:** C-SLK-0x8004A119

**Cause.** The 63 day guest access period has lapsed.

**Resolution.** Ask the channel owner to confirm the engagement is still active, then issue the single permitted renewal. Record the new expiry date in the channel topic. If the renewal has already been used, escalate to Collaboration Services for a review of the engagement rather than reinviting.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A channel owner cannot add a nineteenth external guest


**Error code:** C-SLK-9148

**Cause.** The channel has reached the limit of 18 external guests.

**Resolution.** Remove any guests whose engagement has ended, then retry the invitation. If all 18 are genuinely active, raise an Information Security approval request before going above the limit. Do not create a second parallel channel to work around the cap.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A project channel has disappeared from the sidebar


**Cause.** The channel was archived automatically after 98 days without a message.

**Resolution.** Search the archive list, unarchive the channel and restore the member list. Post a message so the dormancy clock restarts. No escalation is needed unless the archive list does not contain the channel.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Collaboration Services to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A user cannot find messages from three years ago

Reference: C-SLK-2270.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Slack Enterprise Grid and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Collaboration Services citing the reference above.

### Diagnostics for: An external guest reports their invitation link no longer works

Reference: C-SLK-0x8004A119.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Slack Enterprise Grid and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Collaboration Services citing the reference above.

### Diagnostics for: A channel owner cannot add a nineteenth external guest

Reference: C-SLK-9148.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Slack Enterprise Grid and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Collaboration Services citing the reference above.

### Diagnostics for: A project channel has disappeared from the sidebar

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Slack Enterprise Grid and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Collaboration Services citing the reference above.

## Worked examples

### Example: A user cannot find messages from three years ago

A user at Dublin contacts the service desk reporting that a user cannot find messages from three years ago. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Standard channel retention is 26 months, so the messages have already been deleted. Following the documented resolution, explain that the retention period has passed and that deleted messages are not recoverable from the product. Check whether the content exists in an approved document store instead. Escalate to Information Security only if the request is part of a legal hold, which has its own process.

The agent records the diagnosis against the ticket, confirms with priya.bell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Collaboration Services was needed.

### Example: An external guest reports their invitation link no longer works

A user at Remote contacts the service desk reporting that an external guest reports their invitation link no longer works. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The 63 day guest access period has lapsed. Following the documented resolution, ask the channel owner to confirm the engagement is still active, then issue the single permitted renewal. Record the new expiry date in the channel topic. If the renewal has already been used, escalate to Collaboration Services for a review of the engagement rather than reinviting.

The agent records the diagnosis against the ticket, confirms with beatrix.bergmann@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Collaboration Services was needed.

### Example: A channel owner cannot add a nineteenth external guest

A user at Dublin contacts the service desk reporting that a channel owner cannot add a nineteenth external guest. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The channel has reached the limit of 18 external guests. Following the documented resolution, remove any guests whose engagement has ended, then retry the invitation. If all 18 are genuinely active, raise an Information Security approval request before going above the limit. Do not create a second parallel channel to work around the cap.

The agent records the diagnosis against the ticket, confirms with arjun.okafor@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Collaboration Services was needed.

### Example: creating a private channel

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about collaboration tools. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the message retention period for standard channels is flexible or negotiable per user.**

It is not. The message retention period for standard channels is 26 months, after which messages are deleted automatically, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the channel creation rights is flexible or negotiable per user.**

It is not. The channel creation rights is any employee may create a public channel; private channels require a workspace owner in Collaboration Services, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the external guest access duration is flexible or negotiable per user.**

It is not. The external guest access duration is 63 days per invitation, renewable once by the channel owner, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the maximum external guests per channel is flexible or negotiable per user.**

It is not. The maximum external guests per channel is 18, above which Information Security approval is required, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Collaboration Services can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to collaboration tools, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Collaboration Services.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Slack Enterprise Grid did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Collaboration Services produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about collaboration tools unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Collaboration Services runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How long are Slack messages kept?**

Standard channel messages are retained for 26 months and then deleted automatically.

**Can I create a private channel myself?**

No. Public channels are open to anyone, but private channels are created by a workspace owner in Collaboration Services.

**How long does an external guest keep access?**

63 days per invitation, which the channel owner can renew once.

**Why did my old project channel vanish?**

It was archived automatically after 98 days with no messages, and it can be unarchived through the service portal.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Collaboration Services will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Collaboration Services, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Slack Enterprise Grid, engaged by Collaboration Services only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Collaboration Services produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about collaboration tools. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Raise a request in the service portal under Collaboration, choosing Private Channel.
- [ ] State the business purpose and the intended member list.
- [ ] Confirm the guest's organisation is covered by a signed non-disclosure agreement.
- [ ] Check the channel currently holds fewer than 18 external guests.
- [ ] Search the archive list in the service portal for the channel name.
- [ ] Confirm the requester was a member before archiving.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How long are Slack messages kept? Standard channel messages are retained for 26 months and then deleted automatically.
- Can I create a private channel myself? No. Public channels are open to anyone, but private channels are created by a workspace owner in Collaboration Services.
- How long does an external guest keep access? 63 days per invitation, which the channel owner can renew once.
- Why did my old project channel vanish? It was archived automatically after 98 days with no messages, and it can be unarchived through the service portal.

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
| 2.1 | 2026-02-09 | Collaboration Services | Annual review; figures confirmed against the running configuration of Slack Enterprise Grid. |
