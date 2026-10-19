---
title: Backup and Restore Runbook
doc_type: runbook
category: storage
owner: Infrastructure Services
version: 2.1
review_date: 2027-02-09
---

# Backup and Restore Runbook

Owner: Infrastructure Services | System of record: Veeam Backup and Replication | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages backup and restore. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Infrastructure Services team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the storage estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Veeam Backup and Replication is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Veeam Backup and Replication. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Restore point**  
A single recoverable copy of a workload captured at one moment in time, identified by its job name and timestamp. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Synthetic full**  
A full backup file assembled from existing increments on the repository rather than re-reading the source data. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Immutable repository**  
Backup storage where restore points cannot be deleted or altered until their lock period expires. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

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

### 1. Every production workload must be assigned a backup tier before it is released into service.

The reasoning behind this is straightforward. This statement has been tested against the current configuration of Veeam Backup and Replication. Where a platform change makes it unenforceable, Infrastructure Services raises a risk acceptance rather than quietly dropping the control. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 2. Restore requests for another person's data require written approval from that person's line manager.

Agents should treat this as non-negotiable. Evidence that the control is operating is collected automatically from Veeam Backup and Replication and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Where the control cannot be enforced technically, Infrastructure Services monitors for breaches and follows up with the individual and their line manager.

### 3. Backup job failures must be acknowledged by Infrastructure Services within 90 minutes of the alert.

This is enforced technically wherever the platform allows it. Infrastructure Services configures Veeam Backup and Replication to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Where the control cannot be enforced technically, Infrastructure Services monitors for breaches and follows up with the individual and their line manager.

### 4. Immutability is enabled on all monthly restore points and may not be disabled without Information Security approval.

In practice this means the following. This statement has been tested against the current configuration of Veeam Backup and Replication. Where a platform change makes it unenforceable, Infrastructure Services raises a risk acceptance rather than quietly dropping the control. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 5. No backup data may be copied to removable media or to storage outside the approved repositories.

There is a documented exception route, described later in this document. Evidence that the control is operating is collected automatically from Veeam Backup and Replication and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Infrastructure Services reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Infrastructure Services configures in Veeam Backup and Replication. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Backup window for production file servers | 21:45 to 04:15 each night, with incremental jobs every 4 hours during the day |
| Retention tiers | three tiers: 14 daily restore points, 11 weekly restore points and 37 monthly restore points |
| Recovery point objective for tier 1 systems | 12 minutes, delivered by continuous replication |
| Recovery time objective for tier 1 systems | 2 hours from the declaration of a restore event |
| Standard restore request turnaround | 6 working hours for a single file and 29 working hours for a full virtual machine |
| Restore test cadence | a sampled restore test of 7 randomly chosen workloads on the second Tuesday of every month |

**Backup window for production file servers.** The backup window for production file servers is 21:45 to 04:15 each night, with incremental jobs every 4 hours during the day. Infrastructure Services set this figure in consultation with Information Security, and it is reviewed annually.

**Retention tiers.** The retention tiers is three tiers: 14 daily restore points, 11 weekly restore points and 37 monthly restore points. Infrastructure Services set this figure in consultation with Information Security, and it is reviewed annually.

**Recovery point objective for tier 1 systems.** The recovery point objective for tier 1 systems is 12 minutes, delivered by continuous replication. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Recovery time objective for tier 1 systems.** The recovery time objective for tier 1 systems is 2 hours from the declaration of a restore event. Infrastructure Services set this figure in consultation with Information Security, and it is reviewed annually.

**Standard restore request turnaround.** The standard restore request turnaround is 6 working hours for a single file and 29 working hours for a full virtual machine. Infrastructure Services set this figure in consultation with Information Security, and it is reviewed annually.

**Restore test cadence.** The restore test cadence is a sampled restore test of 7 randomly chosen workloads on the second Tuesday of every month. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Veeam Backup and Replication diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Infrastructure Services, and reviewed annually with Information Security.

## Architecture and dependencies

Veeam Backup and Replication is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Veeam Backup and Replication follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Infrastructure Services maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Infrastructure Services raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Veeam Backup and Replication, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Infrastructure Services implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Infrastructure Services rather than skipping it.

### Requesting a single file restore

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise a request in the service portal under Data Recovery and select Single File Restore.
2. Supply the full original path, the file name and the date the file was last known to be correct.
3. Confirm whether the file should be restored in place or to an alternative folder.
4. Wait for the data owner to approve the request if the file belongs to another user.
5. Infrastructure Services mounts the nearest valid restore point and copies the file to the agreed location.
6. Confirm with the requester that the recovered file opens correctly, then close the request.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

### Running the monthly sampled restore test

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Select 7 workloads at random from the protected workload inventory.
2. Restore each workload into the isolated recovery network, never into production.
3. Start each restored workload and verify that its primary service responds.
4. Record the measured restore duration against the tier target for each workload.
5. Delete the test copies from the recovery network once verification is complete.
6. File the results in the monthly recovery assurance record.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Recovering a failed backup job

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Open the job in the backup console and read the last session log.
2. Confirm the repository has free capacity and that the source workload is powered on.
3. Clear any stale snapshot left behind by the previous attempt.
4. Re-run the job in active full mode if the increment chain is reported as broken.
5. Escalate to the storage vendor if the job fails a second time with the same error.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Infrastructure Services with the diagnostic output attached rather than retrying the same steps.

### Symptom: Nightly job ends with a warning that the snapshot could not be removed.


**Error code:** B-VEEAM-1432

**Cause.** An earlier session left an orphaned snapshot on the virtual machine, so the new snapshot cannot be consolidated..

**Resolution.** Open the virtual machine's snapshot manager and consolidate the orphaned snapshot during the next maintenance slot. Re-run the job in incremental mode and confirm the warning clears. If consolidation fails or the snapshot chain is longer than three entries, escalate to Infrastructure Services so the disk chain can be repaired before the next window.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: Restore to the original location fails part way through with an access denied message.


**Error code:** B-0x80070005

**Cause.** The service account used by the restore proxy no longer holds write permission on the target folder..

**Resolution.** Check the target folder permissions and re-grant write access to the backup service account. Restart the restore to an alternative folder so the user is not left waiting, then move the data back once permissions are corrected. Escalate to Information Security if the permission change was not requested through the normal access process.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: The repository reports that it is full even though old restore points appear to have expired.


**Error code:** B-VEEAM-0x2F19

**Cause.** Expired monthly restore points are still inside their immutability lock period and cannot yet be removed..

**Resolution.** Read the lock expiry date on the oldest monthly restore point and calculate when space will be released. Redirect the affected jobs to the secondary repository for the interim period. Raise a capacity request with Infrastructure Services if the shortfall will last more than two nights.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: A user reports that a file they deleted last month cannot be found in any restore point.


**Cause.** The file was created and deleted entirely between two daily restore points, so it was never captured..

**Resolution.** Confirm the deletion date against the retention tiers and check the 11 weekly and 37 monthly restore points before concluding the file is unrecoverable. Tell the user plainly if no restore point holds the file. Record the gap so the backup frequency for that share can be reviewed.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Infrastructure Services to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: Nightly job ends with a warning that the snapshot could not be removed

Reference: B-VEEAM-1432.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Veeam Backup and Replication and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: Restore to the original location fails part way through with an access

Reference: B-0x80070005.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Veeam Backup and Replication and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: The repository reports that it is full even though old restore points 

Reference: B-VEEAM-0x2F19.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Veeam Backup and Replication and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

### Diagnostics for: A user reports that a file they deleted last month cannot be found in 

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Veeam Backup and Replication and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Infrastructure Services citing the reference above.

## Worked examples

### Example: Nightly job ends with a warning that the snapshot could not be removed

A user at Dublin contacts the service desk reporting that nightly job ends with a warning that the snapshot could not be removed.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: An earlier session left an orphaned snapshot on the virtual machine, so the new snapshot cannot be consolidated.. Following the documented resolution, open the virtual machine's snapshot manager and consolidate the orphaned snapshot during the next maintenance slot. Re-run the job in incremental mode and confirm the warning clears. If consolidation fails or the snapshot chain is longer than three entries, escalate to Infrastructure Services so the disk chain can be repaired before the next window.

The agent records the diagnosis against the ticket, confirms with tariq.kowalski@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: Restore to the original location fails part way through with an access

A user at Remote contacts the service desk reporting that restore to the original location fails part way through with an access denied message.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The service account used by the restore proxy no longer holds write permission on the target folder.. Following the documented resolution, check the target folder permissions and re-grant write access to the backup service account. Restart the restore to an alternative folder so the user is not left waiting, then move the data back once permissions are corrected. Escalate to Information Security if the permission change was not requested through the normal access process.

The agent records the diagnosis against the ticket, confirms with viktor.vasquez@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: The repository reports that it is full even though old restore points 

A user at Manchester contacts the service desk reporting that the repository reports that it is full even though old restore points appear to have expired.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Expired monthly restore points are still inside their immutability lock period and cannot yet be removed.. Following the documented resolution, read the lock expiry date on the oldest monthly restore point and calculate when space will be released. Redirect the affected jobs to the secondary repository for the interim period. Raise a capacity request with Infrastructure Services if the shortfall will last more than two nights.

The agent records the diagnosis against the ticket, confirms with leila.oconnell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Infrastructure Services was needed.

### Example: requesting a single file restore

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about backup and restore. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the backup window for production file servers is flexible or negotiable per user.**

It is not. The backup window for production file servers is 21:45 to 04:15 each night, with incremental jobs every 4 hours during the day, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the retention tiers is flexible or negotiable per user.**

It is not. The retention tiers is three tiers: 14 daily restore points, 11 weekly restore points and 37 monthly restore points, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the recovery point objective for tier 1 systems is flexible or negotiable per user.**

It is not. The recovery point objective for tier 1 systems is 12 minutes, delivered by continuous replication, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the recovery time objective for tier 1 systems is flexible or negotiable per user.**

It is not. The recovery time objective for tier 1 systems is 2 hours from the declaration of a restore event, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Infrastructure Services can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to backup and restore, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Infrastructure Services.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Veeam Backup and Replication did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Infrastructure Services produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about backup and restore unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Infrastructure Services runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How far back can my files be restored?**

Backups are kept in three tiers: 14 daily, 11 weekly and 37 monthly restore points, so the oldest recoverable copy is a little over three years old.

**How quickly will a single file restore be completed?**

A single file restore is completed within 6 working hours of approval, while a full virtual machine restore takes up to 29 working hours.

**Can I ask for a colleague's file to be restored?**

Yes, but the request needs written approval from that colleague's line manager before Infrastructure Services will action it.

**Are restores actually tested?**

Yes, 7 randomly chosen workloads are restored and verified in an isolated network on the second Tuesday of every month.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Infrastructure Services will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Infrastructure Services, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Veeam Backup and Replication, engaged by Infrastructure Services only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Infrastructure Services produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about backup and restore. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Raise a request in the service portal under Data Recovery and select Single File Restore.
- [ ] Supply the full original path, the file name and the date the file was last known to be correct.
- [ ] Select 7 workloads at random from the protected workload inventory.
- [ ] Restore each workload into the isolated recovery network, never into production.
- [ ] Open the job in the backup console and read the last session log.
- [ ] Confirm the repository has free capacity and that the source workload is powered on.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How far back can my files be restored? Backups are kept in three tiers: 14 daily, 11 weekly and 37 monthly restore points, so the oldest recoverable copy is a little over three years old.
- How quickly will a single file restore be completed? A single file restore is completed within 6 working hours of approval, while a full virtual machine restore takes up to 29 working hours.
- Can I ask for a colleague's file to be restored? Yes, but the request needs written approval from that colleague's line manager before Infrastructure Services will action it.
- Are restores actually tested? Yes, 7 randomly chosen workloads are restored and verified in an isolated network on the second Tuesday of every month.

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
| 2.1 | 2026-02-09 | Infrastructure Services | Annual review; figures confirmed against the running configuration of Veeam Backup and Replication. |
