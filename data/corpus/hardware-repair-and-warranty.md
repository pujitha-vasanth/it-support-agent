---
title: Hardware Repair and Warranty Runbook
doc_type: runbook
category: hardware
owner: Desktop Support
version: 2.1
review_date: 2027-02-09
---

# Hardware Repair and Warranty Runbook

Owner: Desktop Support | System of record: Dell ProSupport Plus | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages hardware repair and warranty. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Desktop Support team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the hardware estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Dell ProSupport Plus is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Dell ProSupport Plus. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Accidental damage**  
Physical harm to a device from a single unexpected event such as a drop or a liquid spill, as distinct from wear and tear or deliberate misuse. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Dead on arrival**  
A newly delivered device that fails to power on or complete its first boot, which is replaced by the supplier rather than repaired. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Loan device**  
A pre-imaged spare laptop issued for a fixed period while a user's own device is under repair, holding no local data at hand-back. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

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

### 1. Devices under warranty must be repaired through the supplier channel; third party repair voids the warranty and is prohibited.

There is a documented exception route, described later in this document. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Desktop Support will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 2. No device leaves the business for repair until its disk has been confirmed as encrypted and a data wipe record has been raised where the disk is to be replaced.

This is enforced technically wherever the platform allows it. Desktop Support configures Dell ProSupport Plus to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 3. Accidental damage claims require a written incident description from the user before a repair is booked.

Agents should treat this as non-negotiable. This statement has been tested against the current configuration of Dell ProSupport Plus. Where a platform change makes it unenforceable, Desktop Support raises a risk acceptance rather than quietly dropping the control. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 4. Loan devices are issued with a standard corporate image only; users may not install unapproved software on them.

This has been the standing position since the last review. This statement has been tested against the current configuration of Dell ProSupport Plus. Where a platform change makes it unenforceable, Desktop Support raises a risk acceptance rather than quietly dropping the control. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 5. A device that has had 3 accepted hardware faults inside its warranty term is replaced rather than repaired again.

In practice this means the following. Desktop Support configures Dell ProSupport Plus to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Desktop Support reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Desktop Support configures in Dell ProSupport Plus. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Standard warranty term on corporate laptops | 36 months from the delivery date, with next business day onsite response |
| Fault triage target | a documented diagnostic result within 6 business hours of the device arriving at a support bench |
| Loan device pool size | 18 devices held at each of the three main offices |
| Maximum loan device period | 10 working days, after which the loan must be re-approved by a line manager |
| Accidental damage excess | GBP 150 per claim, with a limit of 2 claims per user in any rolling 12 months |
| Battery replacement threshold | a reported battery health figure below 72 per cent of design capacity |

**Standard warranty term on corporate laptops.** The standard warranty term on corporate laptops is 36 months from the delivery date, with next business day onsite response. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Fault triage target.** The fault triage target is a documented diagnostic result within 6 business hours of the device arriving at a support bench. Desktop Support set this figure in consultation with Information Security, and it is reviewed annually.

**Loan device pool size.** The loan device pool size is 18 devices held at each of the three main offices. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Maximum loan device period.** The maximum loan device period is 10 working days, after which the loan must be re-approved by a line manager. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Accidental damage excess.** The accidental damage excess is GBP 150 per claim, with a limit of 2 claims per user in any rolling 12 months. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Battery replacement threshold.** The battery replacement threshold is a reported battery health figure below 72 per cent of design capacity. Where a user asks for a different figure, the answer is the exception process described later in this document.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Dell ProSupport Plus diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Desktop Support, and reviewed annually with Information Security.

## Architecture and dependencies

Dell ProSupport Plus is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Dell ProSupport Plus follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Desktop Support maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Desktop Support raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Dell ProSupport Plus, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Desktop Support implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Desktop Support rather than skipping it.

### Triaging a reported hardware fault

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Record the service tag, the model and the exact symptom in the ticket.
2. Run the supplier onboard diagnostics and capture the validation code.
3. Confirm whether the fault reproduces with external peripherals removed.
4. Check the warranty status and expiry date against the service tag.
5. Record the diagnostic result in the ticket within 6 business hours of bench arrival.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

### Raising a warranty claim

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Open a supplier case quoting the service tag and the diagnostic validation code.
2. Attach the fault description and any photographs of physical damage.
3. Select next business day onsite where the user is at a main office, or depot repair otherwise.
4. Issue a loan device to the user and record its asset number against the ticket.
5. Confirm the repair outcome with the engineer and close the supplier case.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Handling an accidental damage claim

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Collect a written incident description from the user describing how the damage occurred.
2. Confirm the user has not already made 2 claims in the rolling 12 month period.
3. Raise the GBP 150 excess as a cost recharge against the user's cost centre.
4. Book the repair with the supplier under the accidental damage cover.
5. Record the claim against the asset so the claim count stays accurate.

Record the ticket reference against each step that changes a production configuration, so the change can be traced afterwards.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Desktop Support with the diagnostic output attached rather than retrying the same steps.

### Symptom: The supplier portal rejects a claim with D-HW-5531


**Error code:** D-HW-5531

**Cause.** The service tag is outside its 36 month warranty term.

**Resolution.** Confirm the delivery date on the asset record rather than the purchase order date, as the term runs from delivery. If the device is genuinely out of warranty, quote the repair as a chargeable job and route the cost approval to the user's line manager. Escalate to Desktop Support management if the asset record and the supplier record disagree.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A user reports the laptop runs for less than an hour on battery


**Cause.** The battery has degraded below the 72 per cent design capacity threshold.

**Resolution.** Run the onboard battery report and record the health percentage in the ticket. If it is below 72 per cent, raise a warranty claim for a battery replacement. If it is above 72 per cent, check the power profile and running processes before booking any hardware work.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A loan device cannot be issued and the stock system shows D-HW-8104


**Error code:** D-HW-8104

**Cause.** The site loan pool of 18 devices is fully allocated.

**Resolution.** Check for loans that have passed the 10 working day limit and chase those users for return. Offer the user a loan from the next nearest office with courier delivery. If the pool is exhausted for more than 2 working days, escalate to Desktop Support management to release buffer stock.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A replacement disk is fitted but the device will not boot and shows D-HW-3377


**Error code:** D-HW-3377

**Cause.** The recovery image was not re-applied after the disk swap, so there is no bootable partition.

**Resolution.** Boot the device from the network recovery image and re-apply the standard corporate build. Confirm disk encryption completes before returning the device to the user. If the device fails to pick up the recovery image after two attempts, raise it to the build team with the service tag.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Desktop Support to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: The supplier portal rejects a claim with D-HW-5531

Reference: D-HW-5531.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Dell ProSupport Plus and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Desktop Support citing the reference above.

### Diagnostics for: A user reports the laptop runs for less than an hour on battery

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Dell ProSupport Plus and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Desktop Support citing the reference above.

### Diagnostics for: A loan device cannot be issued and the stock system shows D-HW-8104

Reference: D-HW-8104.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Dell ProSupport Plus and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Desktop Support citing the reference above.

### Diagnostics for: A replacement disk is fitted but the device will not boot and shows D-

Reference: D-HW-3377.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Dell ProSupport Plus and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Desktop Support citing the reference above.

## Worked examples

### Example: The supplier portal rejects a claim with D-HW-5531

A user at Remote contacts the service desk reporting that the supplier portal rejects a claim with D-HW-5531. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The service tag is outside its 36 month warranty term. Following the documented resolution, confirm the delivery date on the asset record rather than the purchase order date, as the term runs from delivery. If the device is genuinely out of warranty, quote the repair as a chargeable job and route the cost approval to the user's line manager. Escalate to Desktop Support management if the asset record and the supplier record disagree.

The agent records the diagnosis against the ticket, confirms with jonas.sorensen@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Desktop Support was needed.

### Example: A user reports the laptop runs for less than an hour on battery

A user at London HQ contacts the service desk reporting that a user reports the laptop runs for less than an hour on battery. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The battery has degraded below the 72 per cent design capacity threshold. Following the documented resolution, run the onboard battery report and record the health percentage in the ticket. If it is below 72 per cent, raise a warranty claim for a battery replacement. If it is above 72 per cent, check the power profile and running processes before booking any hardware work.

The agent records the diagnosis against the ticket, confirms with dmitri.bell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Desktop Support was needed.

### Example: A loan device cannot be issued and the stock system shows D-HW-8104

A user at London HQ contacts the service desk reporting that a loan device cannot be issued and the stock system shows D-HW-8104. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The site loan pool of 18 devices is fully allocated. Following the documented resolution, check for loans that have passed the 10 working day limit and chase those users for return. Offer the user a loan from the next nearest office with courier delivery. If the pool is exhausted for more than 2 working days, escalate to Desktop Support management to release buffer stock.

The agent records the diagnosis against the ticket, confirms with mira.whitfield@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Desktop Support was needed.

### Example: triaging a reported hardware fault

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about hardware repair and warranty. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the standard warranty term on corporate laptops is flexible or negotiable per user.**

It is not. The standard warranty term on corporate laptops is 36 months from the delivery date, with next business day onsite response, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the fault triage target is flexible or negotiable per user.**

It is not. The fault triage target is a documented diagnostic result within 6 business hours of the device arriving at a support bench, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the loan device pool size is flexible or negotiable per user.**

It is not. The loan device pool size is 18 devices held at each of the three main offices, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the maximum loan device period is flexible or negotiable per user.**

It is not. The maximum loan device period is 10 working days, after which the loan must be re-approved by a line manager, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Desktop Support can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to hardware repair and warranty, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Desktop Support.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Dell ProSupport Plus did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Desktop Support produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about hardware repair and warranty unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Desktop Support runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How long is my laptop covered?**

36 months from the delivery date, with next business day onsite response while it is in warranty.

**Will I be charged if I drop my laptop?**

An excess of GBP 150 per claim is recharged to your cost centre, and only 2 claims are allowed in any rolling 12 months.

**How long can I keep a loan laptop?**

Up to 10 working days, after which your line manager must re-approve the loan.

**When does a battery qualify for replacement?**

When the onboard battery report shows health below 72 per cent of design capacity.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Desktop Support will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Desktop Support, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Dell ProSupport Plus, engaged by Desktop Support only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Desktop Support produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about hardware repair and warranty. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Record the service tag, the model and the exact symptom in the ticket.
- [ ] Run the supplier onboard diagnostics and capture the validation code.
- [ ] Open a supplier case quoting the service tag and the diagnostic validation code.
- [ ] Attach the fault description and any photographs of physical damage.
- [ ] Collect a written incident description from the user describing how the damage occurred.
- [ ] Confirm the user has not already made 2 claims in the rolling 12 month period.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How long is my laptop covered? 36 months from the delivery date, with next business day onsite response while it is in warranty.
- Will I be charged if I drop my laptop? An excess of GBP 150 per claim is recharged to your cost centre, and only 2 claims are allowed in any rolling 12 months.
- How long can I keep a loan laptop? Up to 10 working days, after which your line manager must re-approve the loan.
- When does a battery qualify for replacement? When the onboard battery report shows health below 72 per cent of design capacity.

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
| 2.1 | 2026-02-09 | Desktop Support | Annual review; figures confirmed against the running configuration of Dell ProSupport Plus. |
