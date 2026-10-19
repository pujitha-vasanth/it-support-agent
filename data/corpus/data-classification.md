---
title: Data Classification Policy
doc_type: policy
category: security
owner: Information Governance
version: 2.1
review_date: 2027-02-09
---

# Data Classification Policy

Owner: Information Governance | System of record: Microsoft Purview Information Protection | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages data classification. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Information Governance team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the security estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Microsoft Purview Information Protection is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Microsoft Purview Information Protection. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Data owner**  
The named accountable person for a set of data, responsible for its classification and for approving access to it. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Label downgrade**  
A change that moves a document to a less restrictive tier, for example from Confidential to Internal. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Sensitivity label**  
A persistent marker applied to a file or message that carries the classification and the protection settings with the content. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Information Governance. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Information Governance** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Information Governance rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. Every document and email must carry a sensitivity label before it is saved or sent.

The reasoning behind this is straightforward. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Governance will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 2. Restricted data must not be copied to removable media, personal storage or any unmanaged device.

Agents should treat this as non-negotiable. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Governance will either confirm the control applies or sponsor an exception, usually within a few working days. Information Governance reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 3. Confidential data may be shared externally only through an expiring link issued to a named recipient.

There is a documented exception route, described later in this document. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Information Governance will either confirm the control applies or sponsor an exception, usually within a few working days. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 4. A label may only be downgraded with the data owner's approval and an Information Governance record of the reason.

In practice this means the following. This statement has been tested against the current configuration of Microsoft Purview Information Protection. Where a platform change makes it unenforceable, Information Governance raises a risk acceptance rather than quietly dropping the control. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 5. Printed Confidential or Restricted material must be collected immediately and may not be left in a shared area.

This has been the standing position since the last review. Evidence that the control is operating is collected automatically from Microsoft Purview Information Protection and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Information Governance configures in Microsoft Purview Information Protection. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Classification tiers | four tiers: Public, Internal, Confidential and Restricted |
| Default label applied to new documents | Internal, applied automatically when no label is chosen |
| Mandatory labelling scope | every document and email created in the productivity suite, with no option to save unlabelled |
| Maximum external sharing link lifetime for Confidential data | 21 days, after which the link expires and must be reissued |
| External sharing rule for Restricted data | prohibited entirely; Restricted data may only be accessed inside the managed environment |
| Label change approval for a downgrade | the data owner plus Information Governance, recorded against the document identifier |

**Classification tiers.** The classification tiers is four tiers: Public, Internal, Confidential and Restricted. This is configured centrally in Microsoft Purview Information Protection and is not adjustable per user or per team.

**Default label applied to new documents.** The default label applied to new documents is Internal, applied automatically when no label is chosen. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Mandatory labelling scope.** The mandatory labelling scope is every document and email created in the productivity suite, with no option to save unlabelled. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Maximum external sharing link lifetime for Confidential data.** The maximum external sharing link lifetime for Confidential data is 21 days, after which the link expires and must be reissued. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**External sharing rule for Restricted data.** The external sharing rule for Restricted data is prohibited entirely; Restricted data may only be accessed inside the managed environment. This is configured centrally in Microsoft Purview Information Protection and is not adjustable per user or per team.

**Label change approval for a downgrade.** The label change approval for a downgrade is the data owner plus Information Governance, recorded against the document identifier. This is configured centrally in Microsoft Purview Information Protection and is not adjustable per user or per team.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Microsoft Purview Information Protection diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Information Governance, and reviewed annually with Information Security.

## Architecture and dependencies

Microsoft Purview Information Protection is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Microsoft Purview Information Protection follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Information Governance maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Information Governance raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Microsoft Purview Information Protection, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Information Governance implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Information Governance rather than skipping it.

### Classifying a new document

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Decide who may legitimately see the content before writing it.
2. Apply the lowest label that still protects the content adequately.
3. Apply Restricted only where disclosure would cause serious harm to the company or an individual.
4. Add the data owner's name to the document properties so accountability is clear.
5. Save the document in the repository that matches the chosen label.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Sharing Confidential data with an external party

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm an active agreement with the external party covers the data in question.
2. Create a sharing link scoped to the named recipient's email address only.
3. Set the link to expire no later than the 21 day maximum.
4. Disable download on the link where the recipient only needs to read the content.
5. Record the share and its expiry date in the sharing register.
6. Revoke the link as soon as the business need ends.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Requesting a label downgrade

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Raise a request in the service portal under Information Governance and quote the document identifier.
2. State the current label, the requested label and the reason for the change.
3. Obtain the data owner's written approval on the request.
4. Information Governance reviews the content and either applies or refuses the downgrade.
5. Information Governance records the decision and the reason against the document identifier.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Information Governance with the diagnostic output attached rather than retrying the same steps.

### Symptom: A user cannot save a document because the application insists on a label.


**Error code:** B-PURV-2209

**Cause.** Mandatory labelling is in force across the productivity suite and no label has been selected on the document..

**Resolution.** Ask the user to pick a label from the sensitivity menu, defaulting to Internal if they are unsure. Explain that Internal is applied automatically to new documents and is safe for everyday work. Escalate to Information Governance only if the label menu itself does not appear after a restart and sign in.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: An external recipient reports that a shared link no longer opens.


**Error code:** B-SHR-0x4412

**Cause.** The link reached its expiry date, which cannot exceed 21 days for Confidential data..

**Resolution.** Confirm the business need still exists, then issue a fresh link to the same named recipient with a new expiry date. Update the sharing register with the reissue. Escalate to Information Governance if the recipient needs standing access, as that calls for a different arrangement than repeated links.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: A Restricted file cannot be copied to a USB drive.


**Error code:** B-DLP-7731

**Cause.** Restricted data is blocked from removable media by policy, and the block is enforced at the endpoint..

**Resolution.** Explain that the block is intended and that Restricted data stays inside the managed environment. Offer an in-environment alternative such as a shared workspace with the correct label. Do not request a policy exception; escalate to Information Governance if the business process genuinely cannot work any other way.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. If this recurs for the same user more than twice in a month, raise a problem record rather than another incident.

### Symptom: A document appears with a lower label than the user remembers applying.


**Cause.** A downgrade was approved and applied through the governance process, or the document was recreated from an unlabelled template..

**Resolution.** Check the document identifier against the Information Governance downgrade record to see whether an approved change exists. If no record exists, reapply the correct label and report it as a possible mislabelling. Escalate to Information Governance if Confidential or Restricted content was left at a lower tier while it was being shared.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Information Governance to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: A user cannot save a document because the application insists on a lab

Reference: B-PURV-2209.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Purview Information Protection and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Governance citing the reference above.

### Diagnostics for: An external recipient reports that a shared link no longer opens.

Reference: B-SHR-0x4412.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Purview Information Protection and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Governance citing the reference above.

### Diagnostics for: A Restricted file cannot be copied to a USB drive.

Reference: B-DLP-7731.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Purview Information Protection and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Governance citing the reference above.

### Diagnostics for: A document appears with a lower label than the user remembers applying

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Microsoft Purview Information Protection and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Information Governance citing the reference above.

## Worked examples

### Example: A user cannot save a document because the application insists on a lab

A user at London HQ contacts the service desk reporting that a user cannot save a document because the application insists on a label.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Mandatory labelling is in force across the productivity suite and no label has been selected on the document.. Following the documented resolution, ask the user to pick a label from the sensitivity menu, defaulting to Internal if they are unsure. Explain that Internal is applied automatically to new documents and is safe for everyday work. Escalate to Information Governance only if the label menu itself does not appear after a restart and sign in.

The agent records the diagnosis against the ticket, confirms with noor.iyer@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Governance was needed.

### Example: An external recipient reports that a shared link no longer opens.

A user at Singapore contacts the service desk reporting that an external recipient reports that a shared link no longer opens.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The link reached its expiry date, which cannot exceed 21 days for Confidential data.. Following the documented resolution, confirm the business need still exists, then issue a fresh link to the same named recipient with a new expiry date. Update the sharing register with the reissue. Escalate to Information Governance if the recipient needs standing access, as that calls for a different arrangement than repeated links.

The agent records the diagnosis against the ticket, confirms with imogen.haddad@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Governance was needed.

### Example: A Restricted file cannot be copied to a USB drive.

A user at Manchester contacts the service desk reporting that a Restricted file cannot be copied to a USB drive.. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: Restricted data is blocked from removable media by policy, and the block is enforced at the endpoint.. Following the documented resolution, explain that the block is intended and that Restricted data stays inside the managed environment. Offer an in-environment alternative such as a shared workspace with the correct label. Do not request a policy exception; escalate to Information Governance if the business process genuinely cannot work any other way.

The agent records the diagnosis against the ticket, confirms with beatrix.whitfield@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Information Governance was needed.

### Example: classifying a new document

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about data classification. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the classification tiers is flexible or negotiable per user.**

It is not. The classification tiers is four tiers: Public, Internal, Confidential and Restricted, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the default label applied to new documents is flexible or negotiable per user.**

It is not. The default label applied to new documents is Internal, applied automatically when no label is chosen, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the mandatory labelling scope is flexible or negotiable per user.**

It is not. The mandatory labelling scope is every document and email created in the productivity suite, with no option to save unlabelled, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the maximum external sharing link lifetime for Confidential data is flexible or negotiable per user.**

It is not. The maximum external sharing link lifetime for Confidential data is 21 days, after which the link expires and must be reissued, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Information Governance can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to data classification, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Information Governance.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Microsoft Purview Information Protection did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Information Governance produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about data classification unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Information Governance runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**How many classification levels are there?**

Four: Public, Internal, Confidential and Restricted.

**What happens if I forget to pick a label?**

New documents receive the Internal label automatically, and the application will not let you save a document with no label at all.

**Can I send Restricted data to a client?**

No, Restricted data cannot be shared externally at all and must stay inside the managed environment.

**How long does an external link to Confidential data last?**

No more than 21 days, after which it expires and a new link must be issued to the named recipient.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Information Governance will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Information Governance, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Microsoft Purview Information Protection, engaged by Information Governance only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Information Governance produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about data classification. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Decide who may legitimately see the content before writing it.
- [ ] Apply the lowest label that still protects the content adequately.
- [ ] Confirm an active agreement with the external party covers the data in question.
- [ ] Create a sharing link scoped to the named recipient's email address only.
- [ ] Raise a request in the service portal under Information Governance and quote the document identifier.
- [ ] State the current label, the requested label and the reason for the change.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- How many classification levels are there? Four: Public, Internal, Confidential and Restricted.
- What happens if I forget to pick a label? New documents receive the Internal label automatically, and the application will not let you save a document with no label at all.
- Can I send Restricted data to a client? No, Restricted data cannot be shared externally at all and must stay inside the managed environment.
- How long does an external link to Confidential data last? No more than 21 days, after which it expires and a new link must be issued to the named recipient.

### Appendix C: related documents

- Service Desk Service Level Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Information Governance | First published version. |
| 1.1 | 2024-11-02 | Information Governance | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Information Governance | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Information Governance | Annual review; figures confirmed against the running configuration of Microsoft Purview Information Protection. |
