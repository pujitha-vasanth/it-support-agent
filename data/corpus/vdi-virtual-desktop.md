---
title: Virtual Desktop Services Runbook
doc_type: runbook
category: infrastructure
owner: Infrastructure Services
version: 2.1
review_date: 2027-02-09
---

# Virtual Desktop Services Runbook

Owner: Infrastructure Services | System of record: Azure Virtual Desktop | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages virtual desktop services. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Infrastructure Services team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the infrastructure estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Azure Virtual Desktop is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Azure Virtual Desktop. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Host pool**  
A group of identically built Azure Virtual Desktop session hosts that share a single set of users, applications and session limits.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Published application**  
A single application delivered from a host pool and launched in its own window, rather than the user signing in to a full desktop.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**FSLogix profile container**  
The virtual disk that holds a user Windows profile so that settings, mail cache and desktop follow the user between session hosts.. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

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

### 1. Virtual desktop access must be requested for a named user and is granted through the Entra ID group that fronts the relevant host pool.

This is enforced technically wherever the platform allows it. Evidence that the control is operating is collected automatically from Azure Virtual Desktop and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 2. Users must not store business data on the session host local drives, because hosts are rebuilt on each image release.

The reasoning behind this is straightforward. Infrastructure Services configures Azure Virtual Desktop to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Infrastructure Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 3. Personal host pools are reserved for roles with an approved technical justification, and all other users receive multi-session pooled desktops.

Agents should treat this as non-negotiable. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Infrastructure Services will either confirm the control applies or sponsor an exception, usually within a few working days. Where the control cannot be enforced technically, Infrastructure Services monitors for breaches and follows up with the individual and their line manager.

### 4. Infrastructure Services must apply the monthly image update to every host pool within the agreed maintenance window and keep one previous image version available for rollback.

There is a documented exception route, described later in this document. Infrastructure Services configures Azure Virtual Desktop to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 5. Session limits and the scaling plan must not be changed for an individual user, and capacity concerns must be raised as a capacity request instead.

This has been the standing position since the last review. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Infrastructure Services will either confirm the control applies or sponsor an exception, usually within a few working days. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Infrastructure Services configures in Azure Virtual Desktop. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Maximum concurrent user sessions per session host | 14 sessions on a standard multi-session host |
| Idle session disconnect threshold | 25 minutes of inactivity before the session is disconnected |
| Disconnected session sign-out threshold | 11 hours before a disconnected session is signed out and its host released |
| Maximum FSLogix profile container size | 35 GB per user profile |
| Number of published applications in the virtual desktop catalogue | 46 published applications |
| Scaling plan ramp-up window | 06:45 to 19:30 United Kingdom time on working days |

**Maximum concurrent user sessions per session host.** The maximum concurrent user sessions per session host is 14 sessions on a standard multi-session host. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Idle session disconnect threshold.** The idle session disconnect threshold is 25 minutes of inactivity before the session is disconnected. This is configured centrally in Azure Virtual Desktop and is not adjustable per user or per team.

**Disconnected session sign-out threshold.** The disconnected session sign-out threshold is 11 hours before a disconnected session is signed out and its host released. Infrastructure Services set this figure in consultation with Information Security, and it is reviewed annually.

**Maximum FSLogix profile container size.** The maximum FSLogix profile container size is 35 GB per user profile. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Number of published applications in the virtual desktop catalogue.** The number of published applications in the virtual desktop catalogue is 46 published applications. Infrastructure Services set this figure in consultation with Information Security, and it is reviewed annually.

**Scaling plan ramp-up window.** The scaling plan ramp-up window is 06:45 to 19:30 United Kingdom time on working days. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Azure Virtual Desktop diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Infrastructure Services, and reviewed annually with Information Security.

## Architecture and dependencies

Azure Virtual Desktop is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Azure Virtual Desktop follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Infrastructure Services maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Infrastructure Services raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Azure Virtual Desktop, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Infrastructure Services implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Infrastructure Services rather than skipping it.

### Grant a user access to a pooled virtual desktop

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the request names the host pool and has line manager approval.
2. Add the user to the Entra ID group assigned to that host pool.
3. Confirm the FSLogix profile container is created on first sign-in.
4. Ask the user to launch the desktop from the Windows App and confirm the published applications appear.
5. Record the host pool and the access group on the ServiceNow request.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Publish a new application to a host pool

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Install and test the application on a single session host taken out of the pool.
2. Bake the application into the next host pool image and validate it on two rebuilt hosts.
3. Create the application entry in the host pool application group.
4. Assign the application group to the Entra ID group for the requesting team.
5. Confirm the application launches for a pilot user and update the published application count.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Apply a monthly host pool image update

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Announce the maintenance window to the affected host pool user groups.
2. Set the host pool to drain mode so no new sessions land on hosts due to be rebuilt.
3. Wait for active sessions to end, then rebuild the hosts from the new image version.
4. Validate sign-in, profile load and two published applications on each rebuilt host.
5. Remove drain mode, confirm the scaling plan is active and keep the previous image version for rollback.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Infrastructure Services with the diagnostic output attached rather than retrying the same steps.

### Symptom: A user signs in to a pooled desktop and receives a temporary profile with none of their settings.


**Error code:** A-FSLOGIX-0x00000020

**Cause.** The FSLogix profile container could not be attached, usually because it is locked by a previous session or has reached its size limit..

**Resolution.** Check whether the container is still attached to another session host and sign the stale session out. Confirm the container is within its size limit and expand only after the data owner has cleared unnecessary cache. Escalate to Infrastructure Services second line if the container fails to attach after the stale session is cleared.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: Users report that the virtual desktop refuses new connections during the morning peak.


**Error code:** A-AVD-0x3000047

**Cause.** Every session host has reached the concurrent session limit and the scaling plan has not yet added capacity..

**Resolution.** Check the host pool session count against the per-host limit and confirm the scaling plan ramp-up window has started. Add session hosts manually if the peak is earlier than the ramp-up window. Escalate as a capacity request to Infrastructure Services if the pool hits its limit on more than three mornings in a month.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A user is repeatedly dropped out of their virtual desktop while reading long documents.


**Error code:** A-RDP-0x204

**Cause.** The session is being treated as idle and disconnected by the inactivity policy because no input is registered..

**Resolution.** Explain the idle disconnect threshold and confirm the user can reconnect to the same session without losing work. Check for network instability on the client side if the disconnects happen well inside the threshold. Escalate to Network Services when packet loss is confirmed on the client connection.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: External users cannot reach the virtual desktop at all while office users connect normally.


**Error code:** A-RDGW-50331678

**Cause.** The gateway connection is being blocked, commonly by conditional access or a client that cannot complete the gateway handshake..

**Resolution.** Confirm the user device is compliant so conditional access allows the gateway connection, then update the Windows App client to the current version and retry. Test from a second network to rule out the user home connection. Escalate to Infrastructure Services with the connection activity identifier if the gateway still refuses the session.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Infrastructure Services to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A user signs in to a pooled desktop and receives a temporary profile w

Reference: A-FSLOGIX-0x00000020.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Azure Virtual Desktop and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: Users report that the virtual desktop refuses new connections during t

Reference: A-AVD-0x3000047.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Azure Virtual Desktop and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: A user is repeatedly dropped out of their virtual desktop while readin

Reference: A-RDP-0x204.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Azure Virtual Desktop and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: External users cannot reach the virtual desktop at all while office us

Reference: A-RDGW-50331678.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Azure Virtual Desktop and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

## Worked examples

### Example: A user signs in to a pooled desktop and receives a temporary profile w

A user at London HQ contacts the service desk reporting that a user signs in to a pooled desktop and receives a temporary profile with none of their settings.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The FSLogix profile container could not be attached, usually because it is locked by a previous session or has reached its size limit.. Following the documented resolution, check whether the container is still attached to another session host and sign the stale session out. Confirm the container is within its size limit and expand only after the data owner has cleared unnecessary cache. Escalate to Infrastructure Services second line if the container fails to attach after the stale session is cleared.

The agent records the diagnosis against the ticket, confirms with ingrid.mehta@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: Users report that the virtual desktop refuses new connections during t

A user at Rotterdam contacts the service desk reporting that users report that the virtual desktop refuses new connections during the morning peak.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Every session host has reached the concurrent session limit and the scaling plan has not yet added capacity.. Following the documented resolution, check the host pool session count against the per-host limit and confirm the scaling plan ramp-up window has started. Add session hosts manually if the peak is earlier than the ramp-up window. Escalate as a capacity request to Infrastructure Services if the pool hits its limit on more than three mornings in a month.

The agent records the diagnosis against the ticket, confirms with viktor.farouk@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: A user is repeatedly dropped out of their virtual desktop while readin

A user at Rotterdam contacts the service desk reporting that a user is repeatedly dropped out of their virtual desktop while reading long documents.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The session is being treated as idle and disconnected by the inactivity policy because no input is registered.. Following the documented resolution, explain the idle disconnect threshold and confirm the user can reconnect to the same session without losing work. Check for network instability on the client side if the disconnects happen well inside the threshold. Escalate to Network Services when packet loss is confirmed on the client connection.

The agent records the diagnosis against the ticket, confirms with dmitri.bergmann@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: grant a user access to a pooled virtual desktop

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about virtual desktop services. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the maximum concurrent user sessions per session host is flexible or negotiable per user.**

It is not. The maximum concurrent user sessions per session host is 14 sessions on a standard multi-session host, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the idle session disconnect threshold is flexible or negotiable per user.**

It is not. The idle session disconnect threshold is 25 minutes of inactivity before the session is disconnected, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the disconnected session sign-out threshold is flexible or negotiable per user.**

It is not. The disconnected session sign-out threshold is 11 hours before a disconnected session is signed out and its host released, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the maximum FSLogix profile container size is flexible or negotiable per user.**

It is not. The maximum FSLogix profile container size is 35 GB per user profile, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Infrastructure Services can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to virtual desktop services, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Infrastructure Services.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Azure Virtual Desktop did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Infrastructure Services produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about virtual desktop services unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Infrastructure Services runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Why was I disconnected from my virtual desktop?**

Sessions are disconnected after 25 minutes of inactivity, and you can reconnect to the same session without losing your work.

**How long does a disconnected session stay available?**

A disconnected session is signed out after 11 hours, at which point unsaved work is lost.

**Can I save files on the virtual desktop itself?**

No, store work in OneDrive or an approved network share, because session hosts are rebuilt with every monthly image release.

**How large can my virtual desktop profile grow?**

The FSLogix profile container is capped at 35 GB per user.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Infrastructure Services will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Infrastructure Services, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Azure Virtual Desktop, engaged by Infrastructure Services only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Infrastructure Services produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about virtual desktop services. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the request names the host pool and has line manager approval.
- [ ] Add the user to the Entra ID group assigned to that host pool.
- [ ] Install and test the application on a single session host taken out of the pool.
- [ ] Bake the application into the next host pool image and validate it on two rebuilt hosts.
- [ ] Announce the maintenance window to the affected host pool user groups.
- [ ] Set the host pool to drain mode so no new sessions land on hosts due to be rebuilt.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Why was I disconnected from my virtual desktop? Sessions are disconnected after 25 minutes of inactivity, and you can reconnect to the same session without losing your work.
- How long does a disconnected session stay available? A disconnected session is signed out after 11 hours, at which point unsaved work is lost.
- Can I save files on the virtual desktop itself? No, store work in OneDrive or an approved network share, because session hosts are rebuilt with every monthly image release.
- How large can my virtual desktop profile grow? The FSLogix profile container is capped at 35 GB per user.

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
| 2.1 | 2026-02-09 | Infrastructure Services | Annual review; figures confirmed against the running configuration of Azure Virtual Desktop. |
