---
title: Security Incident Response Runbook
doc_type: runbook
category: security
owner: Information Security
version: 2.1
review_date: 2027-02-09
---

# Security Incident Response Runbook

Owner: Information Security | System of record: CrowdStrike Falcon | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages security incident response. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Information Security team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the security estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

CrowdStrike Falcon is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of CrowdStrike Falcon. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Containment**  
Action taken to stop an incident spreading further, such as network isolation of a host or disabling an account. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Chain of custody**  
The written record of everyone who has handled a piece of evidence, with the date, time and reason for each handover. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Indicator of compromise**  
An observable artefact such as a file hash, domain or process name that suggests a system has been attacked. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

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

### 1. Any suspected security incident must be reported to Information Security before any attempt is made to fix it locally.

The reasoning behind this is straightforward. Evidence that the control is operating is collected automatically from CrowdStrike Falcon and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Information Security reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 2. A compromised endpoint must be network isolated rather than powered off, so that volatile evidence is preserved.

This has been the standing position since the last review. Evidence that the control is operating is collected automatically from CrowdStrike Falcon and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Where the control cannot be enforced technically, Information Security monitors for breaches and follows up with the individual and their line manager.

### 3. Only Information Security may communicate about an active incident outside the response team.

Agents should treat this as non-negotiable. This statement has been tested against the current configuration of CrowdStrike Falcon. Where a platform change makes it unenforceable, Information Security raises a risk acceptance rather than quietly dropping the control. Where the control cannot be enforced technically, Information Security monitors for breaches and follows up with the individual and their line manager.

### 4. Evidence must be collected to the sealed evidence store with an unbroken chain of custody record.

In practice this means the following. Information Security configures CrowdStrike Falcon to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Information Security reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 5. No incident may be closed until the containment and eradication actions have been independently verified by a second responder.

This is enforced technically wherever the platform allows it. Evidence that the control is operating is collected automatically from CrowdStrike Falcon and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Information Security configures in CrowdStrike Falcon. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Severity levels | four levels: Sev1 critical, Sev2 high, Sev3 moderate and Sev4 low |
| Sev1 initial response target | 20 minutes from alert to an acknowledged responder |
| Sev2 initial response target | 75 minutes from alert to an acknowledged responder |
| Authority to declare a Sev1 incident | the on-call Information Security duty manager, with no second approval needed |
| Evidence retention period for a closed incident | 26 months from the closure date, held in the sealed evidence store |
| Post incident review deadline | 8 working days after closure for Sev1 and Sev2 incidents |

**Severity levels.** The severity levels is four levels: Sev1 critical, Sev2 high, Sev3 moderate and Sev4 low. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Sev1 initial response target.** The Sev1 initial response target is 20 minutes from alert to an acknowledged responder. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Sev2 initial response target.** The Sev2 initial response target is 75 minutes from alert to an acknowledged responder. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Authority to declare a Sev1 incident.** The authority to declare a Sev1 incident is the on-call Information Security duty manager, with no second approval needed. Information Security set this figure in consultation with Information Security, and it is reviewed annually.

**Evidence retention period for a closed incident.** The evidence retention period for a closed incident is 26 months from the closure date, held in the sealed evidence store. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Post incident review deadline.** The post incident review deadline is 8 working days after closure for Sev1 and Sev2 incidents. This is configured centrally in CrowdStrike Falcon and is not adjustable per user or per team.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of CrowdStrike Falcon diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Information Security, and reviewed annually with Information Security.

## Architecture and dependencies

CrowdStrike Falcon is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to CrowdStrike Falcon follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Information Security maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Information Security raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to CrowdStrike Falcon, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Information Security implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Information Security rather than skipping it.

### Declaring a security incident

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Capture what was observed, when it was observed and which systems or accounts are involved.
2. Contact the Information Security duty manager on the published on-call number.
3. Agree the severity level against the four level scale.
4. Open an incident record and assign a lead responder and a scribe.
5. Open the incident bridge and invite only the named response team.
6. Record the declaration time, which starts the response clock.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Containing a compromised endpoint

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Place the endpoint into network containment from the endpoint protection console.
2. Leave the endpoint powered on so that memory and running process evidence survive.
3. Disable the signed in account and revoke its active sessions and refresh tokens.
4. Collect a triage package from the contained host before any remediation is attempted.
5. Hand the triage package to the evidence custodian and sign the chain of custody record.
6. Release containment only after a second responder has verified the host is clean.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Handling incident communications

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm with the incident lead which facts have been verified and may be shared.
2. Draft a single holding statement for internal audiences and have the incident lead approve it.
3. Send updates on a fixed cadence agreed at declaration rather than on request.
4. Route all external and regulatory enquiries to Information Security without comment.
5. Publish the closure notice only after the incident record has been formally closed.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Information Security with the diagnostic output attached rather than retrying the same steps.

### Symptom: The endpoint agent reports the host as contained but the user can still reach internal applications.


**Error code:** B-CRWD-4401

**Cause.** The containment policy was applied to a stale device record while the user is working on a newly rebuilt device..

**Resolution.** Match the device serial number in the console against the device the user is actually holding and apply containment to the correct record. Confirm loss of connectivity with the user before continuing. Escalate to Information Security immediately if the correct host cannot be identified within the Sev1 response target of 20 minutes.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A disabled account continues to send mail for a short period after containment.


**Error code:** B-IR-5512

**Cause.** Existing refresh tokens remained valid because only the password was reset and sessions were not revoked..

**Resolution.** Revoke all sessions and refresh tokens for the account in the identity console, then confirm the mailbox stops sending. Check mailbox rules for any forwarding rule added by the attacker. Escalate to the incident lead if mail continues after revocation, as that suggests a second compromised identity.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: Triage evidence cannot be uploaded to the sealed evidence store.


**Error code:** B-EVD-0x1A7

**Cause.** The responder's account is not a member of the evidence custodian group, which is the only group permitted to write to the store..

**Resolution.** Hand the package to a named evidence custodian rather than requesting the group membership mid incident. Record the handover in the chain of custody with the time and reason. Escalate to the duty manager if no custodian is reachable, so a temporary custodian can be appointed and logged.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: Two separate incident records have been opened for what turns out to be one event.


**Cause.** Parallel reports from the service desk and the monitoring platform were each declared before correlation took place..

**Resolution.** Keep the earliest declared record as the master and link the later record to it as a duplicate. Carry the declaration time of the master record forward so the response clock is not reset. Tell both reporters which record number is now authoritative.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Information Security to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: The endpoint agent reports the host as contained but the user can stil

Reference: B-CRWD-4401.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of CrowdStrike Falcon and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: A disabled account continues to send mail for a short period after con

Reference: B-IR-5512.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of CrowdStrike Falcon and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: Triage evidence cannot be uploaded to the sealed evidence store.

Reference: B-EVD-0x1A7.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of CrowdStrike Falcon and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

### Diagnostics for: Two separate incident records have been opened for what turns out to b

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of CrowdStrike Falcon and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Security citing the reference above.

## Worked examples

### Example: The endpoint agent reports the host as contained but the user can stil

A user at Singapore contacts the service desk reporting that the endpoint agent reports the host as contained but the user can still reach internal applications.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The containment policy was applied to a stale device record while the user is working on a newly rebuilt device.. Following the documented resolution, match the device serial number in the console against the device the user is actually holding and apply containment to the correct record. Confirm loss of connectivity with the user before continuing. Escalate to Information Security immediately if the correct host cannot be identified within the Sev1 response target of 20 minutes.

The agent records the diagnosis against the ticket, confirms with imogen.bell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: A disabled account continues to send mail for a short period after con

A user at Manchester contacts the service desk reporting that a disabled account continues to send mail for a short period after containment.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Existing refresh tokens remained valid because only the password was reset and sessions were not revoked.. Following the documented resolution, revoke all sessions and refresh tokens for the account in the identity console, then confirm the mailbox stops sending. Check mailbox rules for any forwarding rule added by the attacker. Escalate to the incident lead if mail continues after revocation, as that suggests a second compromised identity.

The agent records the diagnosis against the ticket, confirms with elena.santos@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: Triage evidence cannot be uploaded to the sealed evidence store.

A user at Manchester contacts the service desk reporting that triage evidence cannot be uploaded to the sealed evidence store.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The responder's account is not a member of the evidence custodian group, which is the only group permitted to write to the store.. Following the documented resolution, hand the package to a named evidence custodian rather than requesting the group membership mid incident. Record the handover in the chain of custody with the time and reason. Escalate to the duty manager if no custodian is reachable, so a temporary custodian can be appointed and logged.

The agent records the diagnosis against the ticket, confirms with elena.demir@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Security was needed.

### Example: declaring a security incident

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about security incident response. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the severity levels is flexible or negotiable per user.**

It is not. The severity levels is four levels: Sev1 critical, Sev2 high, Sev3 moderate and Sev4 low, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the Sev1 initial response target is flexible or negotiable per user.**

It is not. The Sev1 initial response target is 20 minutes from alert to an acknowledged responder, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the Sev2 initial response target is flexible or negotiable per user.**

It is not. The Sev2 initial response target is 75 minutes from alert to an acknowledged responder, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the authority to declare a Sev1 incident is flexible or negotiable per user.**

It is not. The authority to declare a Sev1 incident is the on-call Information Security duty manager, with no second approval needed, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Information Security can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to security incident response, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Information Security.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of CrowdStrike Falcon did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Information Security produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about security incident response unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Information Security runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Who can declare a critical security incident?**

The on-call Information Security duty manager can declare a Sev1 incident alone, with no second approval required.

**How quickly must a Sev1 incident be picked up?**

A responder must acknowledge a Sev1 within 20 minutes of the alert, compared with 75 minutes for a Sev2.

**Should I switch off a machine I think is infected?**

No, isolate it from the network and leave it powered on so that memory and process evidence is preserved for the responders.

**How long is incident evidence kept?**

Evidence is held in the sealed evidence store for 26 months from the date the incident was closed.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Information Security will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Information Security, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for CrowdStrike Falcon, engaged by Information Security only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Information Security produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about security incident response. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Capture what was observed, when it was observed and which systems or accounts are involved.
- [ ] Contact the Information Security duty manager on the published on-call number.
- [ ] Place the endpoint into network containment from the endpoint protection console.
- [ ] Leave the endpoint powered on so that memory and running process evidence survive.
- [ ] Confirm with the incident lead which facts have been verified and may be shared.
- [ ] Draft a single holding statement for internal audiences and have the incident lead approve it.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Who can declare a critical security incident? The on-call Information Security duty manager can declare a Sev1 incident alone, with no second approval required.
- How quickly must a Sev1 incident be picked up? A responder must acknowledge a Sev1 within 20 minutes of the alert, compared with 75 minutes for a Sev2.
- Should I switch off a machine I think is infected? No, isolate it from the network and leave it powered on so that memory and process evidence is preserved for the responders.
- How long is incident evidence kept? Evidence is held in the sealed evidence store for 26 months from the date the incident was closed.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Information Security | First published version. |
| 1.1 | 2024-11-02 | Information Security | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Information Security | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Information Security | Annual review; figures confirmed against the running configuration of CrowdStrike Falcon. |
