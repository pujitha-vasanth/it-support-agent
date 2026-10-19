---
title: VPN and Remote Access Policy
doc_type: policy
category: network
owner: Network Operations
version: 2.1
review_date: 2027-02-09
---

# VPN and Remote Access Policy

Owner: Network Operations | System of record: Ivanti Secure Access | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages VPN and remote access. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Network Operations team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the network estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Ivanti Secure Access is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Ivanti Secure Access. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Split tunnelling**  
A configuration where only corporate-bound traffic crosses the VPN and everything else goes direct to the internet. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Break-glass access**  
A pre-approved emergency account used only during a declared major incident, with all sessions recorded. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Posture check**  
An automated inspection of a device's patch level, disk encryption and antivirus state before the tunnel is allowed to establish. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Network Operations. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Network Operations** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Network Operations rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Remote access to internal systems is permitted only through the approved VPN client on a managed device.

In practice this means the following. This statement has been tested against the current configuration of Ivanti Secure Access. Where a platform change makes it unenforceable, Network Operations raises a risk acceptance rather than quietly dropping the control. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 2. Personal devices may not establish a VPN tunnel unless enrolled in the mobile device management programme.

The reasoning behind this is straightforward. Network Operations configures Ivanti Secure Access to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 3. All VPN sessions are logged, and connection metadata is retained for 180 days.

This is enforced technically wherever the platform allows it. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Network Operations will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 4. Users must not share VPN credentials or certificates under any circumstances.

This has been the standing position since the last review. Evidence that the control is operating is collected automatically from Ivanti Secure Access and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 5. Any device failing a posture check is placed in a remediation network with access only to the patching service.

Agents should treat this as non-negotiable. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Network Operations will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Network Operations configures in Ivanti Secure Access. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Maximum VPN session duration | 12 hours, after which re-authentication is required |
| Idle disconnect threshold | 30 minutes of inactivity |
| Concurrent device limit per user | 3 enrolled devices |
| Split tunnelling status | disabled for all users except the Network Operations break-glass group |
| VPN client version floor | Ivanti Secure Access 22.6R2 or later; older clients are blocked at the gateway |
| Approval route for contractor VPN access | line manager approval plus Information Security sign-off, valid for 90 days |

**Maximum VPN session duration.** The maximum VPN session duration is 12 hours, after which re-authentication is required. This is configured centrally in Ivanti Secure Access and is not adjustable per user or per team.

**Idle disconnect threshold.** The idle disconnect threshold is 30 minutes of inactivity. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Concurrent device limit per user.** The concurrent device limit per user is 3 enrolled devices. Network Operations set this figure in consultation with Information Security, and it is reviewed annually.

**Split tunnelling status.** The split tunnelling status is disabled for all users except the Network Operations break-glass group. This is configured centrally in Ivanti Secure Access and is not adjustable per user or per team.

**VPN client version floor.** The VPN client version floor is Ivanti Secure Access 22.6R2 or later; older clients are blocked at the gateway. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Approval route for contractor VPN access.** The approval route for contractor VPN access is line manager approval plus Information Security sign-off, valid for 90 days. Network Operations set this figure in consultation with Information Security, and it is reviewed annually.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Ivanti Secure Access diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Network Operations, and reviewed annually with Information Security.

## Architecture and dependencies

Ivanti Secure Access is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Ivanti Secure Access follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Network Operations maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Network Operations raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Ivanti Secure Access, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Network Operations implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Network Operations rather than skipping it.

### Requesting VPN access for a new employee

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the employee record exists in the HR system and has an active start date.
2. Raise a request in the service portal under Network Access, choosing Standard VPN Profile.
3. The line manager approves the request; approval expires if not actioned within 5 business days.
4. Network Operations assigns the user to the VPN-Standard-Users group in the directory.
5. The user signs in to the client once on the corporate network so the device certificate is issued.
6. Confirm the tunnel establishes and the posture check returns a compliant result.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Revoking VPN access

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Remove the user from the VPN-Standard-Users group in the directory.
2. Revoke the device certificate in the certificate authority console.
3. Terminate any active sessions from the gateway administration page.
4. Record the revocation against the original access request for audit.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Raising the concurrent device limit

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. The user submits a justification through the service portal.
2. Information Security reviews the justification against the device inventory.
3. If approved, Network Operations raises the limit to a maximum of 5 devices.
4. The raised limit is reviewed at the next quarterly access recertification.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Network Operations with the diagnostic output attached rather than retrying the same steps.

### Symptom: The VPN client reports error IVE-3105 and refuses to connect


**Error code:** IVE-3105

**Cause.** The device failed the posture check, almost always because disk encryption is off or the antivirus definitions are more than 14 days old.

**Resolution.** Open the endpoint protection console on the device, run a definition update, confirm disk encryption is enabled, then retry the connection. If it still fails, collect the client log bundle and raise a ticket to Network Operations.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: The tunnel drops roughly every half hour


**Cause.** The idle disconnect threshold of 30 minutes is being reached because the user's work is entirely local.

**Resolution.** This is expected behaviour, not a fault. Advise the user to reconnect, or if their role genuinely requires a persistent tunnel, raise a request for the Extended Session profile.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: The user can connect but cannot reach any internal web applications


**Cause.** Internal DNS is not being used because a third-party DNS setting on the device is overriding the tunnel configuration.

**Resolution.** Reset the network adapter DNS to automatic, reconnect the tunnel, and confirm name resolution against an internal host. Permanent overrides should be removed by Desktop Support.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A fourth device cannot be enrolled


**Error code:** IVE-2240

**Cause.** The concurrent device limit of 3 enrolled devices has been reached.

**Resolution.** Ask the user to retire an unused device through the self-service page, or submit a justification to raise the limit to a maximum of 5.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Network Operations to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: The VPN client reports error IVE-3105 and refuses to connect

Reference: IVE-3105.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Ivanti Secure Access and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Network Operations citing the reference above.

### Diagnostics for: The tunnel drops roughly every half hour

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Ivanti Secure Access and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Network Operations citing the reference above.

### Diagnostics for: The user can connect but cannot reach any internal web applications

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Ivanti Secure Access and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Network Operations citing the reference above.

### Diagnostics for: A fourth device cannot be enrolled

Reference: IVE-2240.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Ivanti Secure Access and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Network Operations citing the reference above.

## Worked examples

### Example: The VPN client reports error IVE-3105 and refuses to connect

A user at Dublin contacts the service desk reporting that the VPN client reports error IVE-3105 and refuses to connect. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The device failed the posture check, almost always because disk encryption is off or the antivirus definitions are more than 14 days old. Following the documented resolution, open the endpoint protection console on the device, run a definition update, confirm disk encryption is enabled, then retry the connection. If it still fails, collect the client log bundle and raise a ticket to Network Operations.

The agent records the diagnosis against the ticket, confirms with mira.bergmann@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Network Operations was needed.

### Example: The tunnel drops roughly every half hour

A user at London HQ contacts the service desk reporting that the tunnel drops roughly every half hour. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The idle disconnect threshold of 30 minutes is being reached because the user's work is entirely local. Following the documented resolution, this is expected behaviour, not a fault. Advise the user to reconnect, or if their role genuinely requires a persistent tunnel, raise a request for the Extended Session profile.

The agent records the diagnosis against the ticket, confirms with noor.mehta@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Network Operations was needed.

### Example: The user can connect but cannot reach any internal web applications

A user at Manchester contacts the service desk reporting that the user can connect but cannot reach any internal web applications. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Internal DNS is not being used because a third-party DNS setting on the device is overriding the tunnel configuration. Following the documented resolution, reset the network adapter DNS to automatic, reconnect the tunnel, and confirm name resolution against an internal host. Permanent overrides should be removed by Desktop Support.

The agent records the diagnosis against the ticket, confirms with tariq.mehta@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Network Operations was needed.

### Example: requesting vpn access for a new employee

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about VPN and remote access. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the maximum VPN session duration is flexible or negotiable per user.**

It is not. The maximum VPN session duration is 12 hours, after which re-authentication is required, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the idle disconnect threshold is flexible or negotiable per user.**

It is not. The idle disconnect threshold is 30 minutes of inactivity, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the concurrent device limit per user is flexible or negotiable per user.**

It is not. The concurrent device limit per user is 3 enrolled devices, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the split tunnelling status is flexible or negotiable per user.**

It is not. The split tunnelling status is disabled for all users except the Network Operations break-glass group, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Network Operations can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to VPN and remote access, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Network Operations.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Ivanti Secure Access did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Network Operations produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about VPN and remote access unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Network Operations runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Can I use the VPN from a personal laptop?**

Only if that laptop is enrolled in the mobile device management programme. An unmanaged personal device will fail the posture check.

**Why do I have to sign in again every morning?**

Sessions are capped at 12 hours, so a session started during the working day will always expire overnight.

**Does my home internet traffic go through the company network?**

Yes. Split tunnelling is disabled, so all traffic crosses the VPN while connected.

**How long does contractor VPN access last?**

90 days, after which it must be renewed with fresh manager and Information Security approval.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Network Operations will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Network Operations, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Ivanti Secure Access, engaged by Network Operations only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Network Operations produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about VPN and remote access. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the employee record exists in the HR system and has an active start date.
- [ ] Raise a request in the service portal under Network Access, choosing Standard VPN Profile.
- [ ] Remove the user from the VPN-Standard-Users group in the directory.
- [ ] Revoke the device certificate in the certificate authority console.
- [ ] The user submits a justification through the service portal.
- [ ] Information Security reviews the justification against the device inventory.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Can I use the VPN from a personal laptop? Only if that laptop is enrolled in the mobile device management programme. An unmanaged personal device will fail the posture check.
- Why do I have to sign in again every morning? Sessions are capped at 12 hours, so a session started during the working day will always expire overnight.
- Does my home internet traffic go through the company network? Yes. Split tunnelling is disabled, so all traffic crosses the VPN while connected.
- How long does contractor VPN access last? 90 days, after which it must be renewed with fresh manager and Information Security approval.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Network Operations | First published version. |
| 1.1 | 2024-11-02 | Network Operations | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Network Operations | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Network Operations | Annual review; figures confirmed against the running configuration of Ivanti Secure Access. |
