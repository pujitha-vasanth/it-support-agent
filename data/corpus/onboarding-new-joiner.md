---
title: New Joiner IT Onboarding Runbook
doc_type: runbook
category: workplace
owner: Workplace Technology
version: 2.1
review_date: 2027-02-09
---

# New Joiner IT Onboarding Runbook

Owner: Workplace Technology | System of record: ServiceNow HR Service Delivery | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages new joiner IT onboarding. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Workplace Technology team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the workplace estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

ServiceNow HR Service Delivery is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of ServiceNow HR Service Delivery. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Day one checklist**  
The fixed list of 9 items Workplace Technology must complete and tick in ServiceNow before a new joiner record can be closed. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Pre-boarding window**  
The period between the signed HR start record and the start date, during which accounts are built but kept disabled. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Induction access bundle**  
The standard set of group memberships granting a new joiner the intranet, learning platform and service portal on day one. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Workplace Technology. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Workplace Technology** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Workplace Technology rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. No new joiner account may be enabled before 07:00 on the confirmed start date.

There is a documented exception route, described later in this document. Workplace Technology configures ServiceNow HR Service Delivery to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 2. Equipment is issued only against a signed HR start record, never on a verbal request from a hiring manager.

The reasoning behind this is straightforward. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Workplace Technology will either confirm the control applies or sponsor an exception, usually within a few working days. The service desk should record the relevant detail against the ticket so that the audit trail stands up without anyone needing to reconstruct it later.

### 3. A new joiner who has not completed the IT Induction module within 11 calendar days has their internet access restricted until it is completed.

In practice this means the following. This statement has been tested against the current configuration of ServiceNow HR Service Delivery. Where a platform change makes it unenforceable, Workplace Technology raises a risk acceptance rather than quietly dropping the control. Workplace Technology reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 4. The day one checklist must be fully ticked in ServiceNow before the onboarding record is closed.

This is enforced technically wherever the platform allows it. This statement has been tested against the current configuration of ServiceNow HR Service Delivery. Where a platform change makes it unenforceable, Workplace Technology raises a risk acceptance rather than quietly dropping the control. Workplace Technology reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 5. Line managers are responsible for confirming the delivery address at least 7 working days before the start date.

This has been the standing position since the last review. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Workplace Technology will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Workplace Technology configures in ServiceNow HR Service Delivery. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Minimum notice IT requires before a start date | 7 working days from the signed HR start record |
| Account creation timing | the Entra ID account is created 4 working days before the start date and stays disabled until 07:00 on day one |
| Standard equipment dispatch window | laptop and headset ship 2 working days before the start date to the address on the HR record |
| Induction course completion deadline | the IT Induction module in the learning platform must be completed within 11 calendar days of the start date |
| Day one checklist item count | 9 mandatory items, all of which must be ticked in ServiceNow before the record is closed |
| Temporary password validity for a new joiner | 36 hours from first issue, after which Workplace Technology must reissue it |

**Minimum notice IT requires before a start date.** The minimum notice IT requires before a start date is 7 working days from the signed HR start record. Workplace Technology set this figure in consultation with Information Security, and it is reviewed annually.

**Account creation timing.** The account creation timing is the Entra ID account is created 4 working days before the start date and stays disabled until 07:00 on day one. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Standard equipment dispatch window.** The standard equipment dispatch window is laptop and headset ship 2 working days before the start date to the address on the HR record. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Induction course completion deadline.** The induction course completion deadline is the IT Induction module in the learning platform must be completed within 11 calendar days of the start date. Workplace Technology set this figure in consultation with Information Security, and it is reviewed annually.

**Day one checklist item count.** The day one checklist item count is 9 mandatory items, all of which must be ticked in ServiceNow before the record is closed. Workplace Technology set this figure in consultation with Information Security, and it is reviewed annually.

**Temporary password validity for a new joiner.** The temporary password validity for a new joiner is 36 hours from first issue, after which Workplace Technology must reissue it. Workplace Technology set this figure in consultation with Information Security, and it is reviewed annually.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of ServiceNow HR Service Delivery diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Workplace Technology, and reviewed annually with Information Security.

## Architecture and dependencies

ServiceNow HR Service Delivery is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to ServiceNow HR Service Delivery follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Workplace Technology maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Workplace Technology raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to ServiceNow HR Service Delivery, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Workplace Technology implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Workplace Technology rather than skipping it.

### Building a new joiner account

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Open the onboarding record in ServiceNow and confirm the HR start record is signed.
2. Create the Entra ID account as firstname.lastname@meridiangroup.example and leave it disabled.
3. Add the account to the induction access bundle groups.
4. Generate the temporary password and record that it is valid for 36 hours.
5. Set a scheduled enable action for 07:00 on the start date.
6. Tick the account creation items on the day one checklist.

If the request came in by email or chat rather than through https://help.meridiangroup.example, raise a ticket first. Work carried out without a ticket cannot be audited.

### Dispatching new joiner equipment

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the delivery address held on the HR record with the line manager.
2. Allocate a laptop from the available pool and register the serial against the onboarding record.
3. Enrol the laptop in device management and confirm it reports as compliant.
4. Release the shipment so it leaves the warehouse 2 working days before the start date.
5. Record the courier tracking reference in ServiceNow.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Completing day one handover

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Verify the new joiner has signed in successfully with the temporary password.
2. Walk the joiner through setting a permanent password and registering multi-factor authentication.
3. Confirm the induction access bundle resolves by opening the intranet and the service portal.
4. Assign the IT Induction module and state the 11 calendar day deadline.
5. Tick the remaining items on the day one checklist and close the onboarding record.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Workplace Technology with the diagnostic output attached rather than retrying the same steps.

### Symptom: The new joiner cannot sign in on the morning of their start date


**Error code:** C-ONB-4412

**Cause.** The scheduled enable action did not run, so the account is still disabled.

**Resolution.** Open the account in Entra ID and enable it manually, then reissue the temporary password because the original 36 hour window has usually lapsed. Confirm the joiner can sign in while still on the call. If the scheduled action has failed for more than one joiner that morning, escalate to Workplace Technology as a possible automation fault.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: The laptop arrives but shows as non-compliant at first sign-in


**Error code:** C-ONB-0x8007502F

**Cause.** The device was released from the warehouse before device management enrolment finished.

**Resolution.** Ask the joiner to connect to a stable network and leave the device powered on for the enrolment to complete, then refresh the compliance state from the management console. Re-run the compliance check after 20 minutes. If it still reports non-compliant, arrange a replacement from the pool rather than troubleshooting on day one.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: The joiner can sign in but cannot open the learning platform


**Error code:** C-ONB-7730

**Cause.** The induction access bundle groups were not applied because the account was created outside the standard ServiceNow task.

**Resolution.** Add the account to the induction access bundle groups and ask the joiner to sign out and back in so the new tokens issue. Verify the intranet and service portal also load. Record the manual fix on the onboarding record so the checklist audit stays accurate.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: The hiring manager asks for equipment with only two days notice


**Cause.** The signed HR start record was raised inside the 7 working day minimum notice window.

**Resolution.** Explain that the dispatch window cannot be met and offer a loan device from the local office pool for the first week. Keep the standard build on the normal schedule. Escalate to the Workplace Technology manager only if no loan device is available in that office.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Workplace Technology to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: The new joiner cannot sign in on the morning of their start date

Reference: C-ONB-4412.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow HR Service Delivery and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Workplace Technology citing the reference above.

### Diagnostics for: The laptop arrives but shows as non-compliant at first sign-in

Reference: C-ONB-0x8007502F.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow HR Service Delivery and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Workplace Technology citing the reference above.

### Diagnostics for: The joiner can sign in but cannot open the learning platform

Reference: C-ONB-7730.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow HR Service Delivery and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Workplace Technology citing the reference above.

### Diagnostics for: The hiring manager asks for equipment with only two days notice

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of ServiceNow HR Service Delivery and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Workplace Technology citing the reference above.

## Worked examples

### Example: The new joiner cannot sign in on the morning of their start date

A user at London HQ contacts the service desk reporting that the new joiner cannot sign in on the morning of their start date. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The scheduled enable action did not run, so the account is still disabled. Following the documented resolution, open the account in Entra ID and enable it manually, then reissue the temporary password because the original 36 hour window has usually lapsed. Confirm the joiner can sign in while still on the call. If the scheduled action has failed for more than one joiner that morning, escalate to Workplace Technology as a possible automation fault.

The agent records the diagnosis against the ticket, confirms with rohan.oconnell@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Workplace Technology was needed.

### Example: The laptop arrives but shows as non-compliant at first sign-in

A user at London HQ contacts the service desk reporting that the laptop arrives but shows as non-compliant at first sign-in. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The device was released from the warehouse before device management enrolment finished. Following the documented resolution, ask the joiner to connect to a stable network and leave the device powered on for the enrolment to complete, then refresh the compliance state from the management console. Re-run the compliance check after 20 minutes. If it still reports non-compliant, arrange a replacement from the pool rather than troubleshooting on day one.

The agent records the diagnosis against the ticket, confirms with marcus.demir@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Workplace Technology was needed.

### Example: The joiner can sign in but cannot open the learning platform

A user at Manchester contacts the service desk reporting that the joiner can sign in but cannot open the learning platform. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The induction access bundle groups were not applied because the account was created outside the standard ServiceNow task. Following the documented resolution, add the account to the induction access bundle groups and ask the joiner to sign out and back in so the new tokens issue. Verify the intranet and service portal also load. Record the manual fix on the onboarding record so the checklist audit stays accurate.

The agent records the diagnosis against the ticket, confirms with hana.moreau@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Workplace Technology was needed.

### Example: building a new joiner account

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about new joiner IT onboarding. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the minimum notice IT requires before a start date is flexible or negotiable per user.**

It is not. The minimum notice IT requires before a start date is 7 working days from the signed HR start record, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the account creation timing is flexible or negotiable per user.**

It is not. The account creation timing is the Entra ID account is created 4 working days before the start date and stays disabled until 07:00 on day one, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the standard equipment dispatch window is flexible or negotiable per user.**

It is not. The standard equipment dispatch window is laptop and headset ship 2 working days before the start date to the address on the HR record, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the induction course completion deadline is flexible or negotiable per user.**

It is not. The induction course completion deadline is the IT Induction module in the learning platform must be completed within 11 calendar days of the start date, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Workplace Technology can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to new joiner IT onboarding, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Workplace Technology.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of ServiceNow HR Service Delivery did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Workplace Technology produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about new joiner IT onboarding unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Workplace Technology runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How much notice does IT need before someone starts?**

7 working days from the signed HR start record, which is what allows the account build and equipment dispatch to land on time.

**Why is my account not working the day before I start?**

Accounts are deliberately left disabled until 07:00 on the confirmed start date, even though they are built 4 working days earlier.

**How long is my temporary password valid?**

36 hours from when it is first issued, after which Workplace Technology has to reissue it.

**When must I finish the IT Induction module?**

Within 11 calendar days of your start date, otherwise your internet access is restricted until it is complete.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Workplace Technology will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Workplace Technology, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for ServiceNow HR Service Delivery, engaged by Workplace Technology only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Workplace Technology produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about new joiner IT onboarding. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Open the onboarding record in ServiceNow and confirm the HR start record is signed.
- [ ] Create the Entra ID account as firstname.lastname@meridiangroup.example and leave it disabled.
- [ ] Confirm the delivery address held on the HR record with the line manager.
- [ ] Allocate a laptop from the available pool and register the serial against the onboarding record.
- [ ] Verify the new joiner has signed in successfully with the temporary password.
- [ ] Walk the joiner through setting a permanent password and registering multi-factor authentication.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How much notice does IT need before someone starts? 7 working days from the signed HR start record, which is what allows the account build and equipment dispatch to land on time.
- Why is my account not working the day before I start? Accounts are deliberately left disabled until 07:00 on the confirmed start date, even though they are built 4 working days earlier.
- How long is my temporary password valid? 36 hours from when it is first issued, after which Workplace Technology has to reissue it.
- When must I finish the IT Induction module? Within 11 calendar days of your start date, otherwise your internet access is restricted until it is complete.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Workplace Technology | First published version. |
| 1.1 | 2024-11-02 | Workplace Technology | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Workplace Technology | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Workplace Technology | Annual review; figures confirmed against the running configuration of ServiceNow HR Service Delivery. |
