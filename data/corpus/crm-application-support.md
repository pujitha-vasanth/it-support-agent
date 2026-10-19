---
title: CRM Application Support Runbook
doc_type: runbook
category: applications
owner: Business Applications
version: 2.1
review_date: 2027-02-09
---

# CRM Application Support Runbook

Owner: Business Applications | System of record: Salesforce | Classification: Internal

## Purpose and scope

This document sets out how Meridian Group manages CRM application support. It applies to every employee, contractor and third party who uses Meridian Group systems, regardless of location or working pattern. The Business Applications team owns this document and is accountable for keeping it accurate.

The controls described here exist to keep the applications estate predictable, auditable and supportable. Where this document conflicts with a local practice that has grown up inside a single team, this document takes precedence until a formal exception has been recorded.

Salesforce is the primary platform referenced throughout. Any change to that platform that alters the behaviour described here must be raised through change management before it is applied, and this document must be updated in the same change record.

Readers who only need to resolve a specific problem should go straight to the troubleshooting section. Readers approving a request should read the service parameters and the procedures that follow them.

In scope: all managed endpoints, all Meridian Group identities, and all production instances of Salesforce. Also in scope: contractor and temporary accounts, which follow the same rules with a shorter review interval. Out of scope: isolated laboratory environments that hold no production data and have no route to the corporate network. Those are governed separately.

## Definitions

**Profile**  
The base access definition assigned to a user, controlling object permissions and page layouts, of which only 9 are supported. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Permission set**  
An additive grant layered on top of a profile to give a user extra access without creating another profile. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Sandbox refresh**  
The process of replacing a sandbox with a fresh copy of production metadata, which destroys any unreleased work left in that sandbox. The term is used consistently in this sense throughout Meridian Group documentation, and agents should use it rather than a local synonym when writing up a ticket.

**Service owner**  
The team accountable for the availability and correctness of the service, in this case Business Applications. The service owner approves changes to the parameters in this document.

**Exception**  
A time-bound, written agreement that a specific control in this document will not apply to a named system or user, approved by Information Security and recorded in the exception register.

## Roles and responsibilities

**Business Applications** owns the service, maintains this document, and is the escalation point for anything the service desk cannot resolve within its own authority.

**The Service Desk** is the single point of contact for users. Agents resolve what falls inside the documented procedures below and escalate anything else to Business Applications rather than improvising a workaround.

**Line managers** approve access and equipment requests for their direct reports and are responsible for notifying IT of joiners, movers and leavers in good time.

**Information Security** reviews exceptions, sets the risk thresholds referenced in this document, and may suspend access without notice where there is evidence of compromise.

**Users** are responsible for following the procedures here, for reporting problems promptly through https://help.meridiangroup.example or servicedesk@meridiangroup.example, and for not attempting to work around a control they find inconvenient.

**Internal Audit** samples records produced under this document at least once a year and reports findings to the technology risk committee.

## Operating principles

### 1. New profiles are not created; additional access is delivered through permission sets so the supported set stays at 9.

In practice this means the following. Business Applications configures Salesforce to enforce this wherever the platform exposes the setting, and audits the remainder by sampling. The service desk does not have the authority to waive it on a user's request. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

### 2. No data import may run in production without a successful dry run in a sandbox and a documented rollback approach.

Agents should treat this as non-negotiable. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Business Applications will either confirm the control applies or sponsor an exception, usually within a few working days. Business Applications reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 3. Integration users must authenticate with a dedicated integration account, never with a named employee login.

There is a documented exception route, described later in this document. This statement has been tested against the current configuration of Salesforce. Where a platform change makes it unenforceable, Business Applications raises a risk acceptance rather than quietly dropping the control. Business Applications reviews compliance with this statement as part of the quarterly service review and reports exceptions to Information Security.

### 4. Users must be told at least 3 business days before a sandbox refresh so unreleased work can be saved.

This is enforced technically wherever the platform allows it. Evidence that the control is operating is collected automatically from Salesforce and retained for audit. Agents do not need to collect it manually unless the automated report has gaps. Repeated breaches are treated as a line management matter rather than a technical one, and are reported through the usual route.

### 5. Bulk record deletion in production requires CRM product owner approval and must be executed by Business Applications, not by the requester.

This has been the standing position since the last review. A user who believes this control blocks legitimate work should raise the case through https://help.meridiangroup.example with their line manager copied in. Business Applications will either confirm the control applies or sponsor an exception, usually within a few working days. Requests to vary this must go through the exception process rather than being agreed informally with an engineer.

## Service parameters

The parameters below are the operative numbers for this service. They are the values the service desk should quote to users, and they are what Business Applications configures in Salesforce. Any value that differs from this table in a running system is a defect and should be raised as such.

| Parameter | Value |
| --- | --- |
| Number of supported profiles | 9 profiles, with all additional access granted through permission sets |
| Import row threshold | 50,000 rows through the Data Import Wizard; anything larger must go through Data Loader |
| Sandbox refresh intervals | a full sandbox every 29 days and a partial copy sandbox every 5 days |
| Permission set assignment turnaround | 1 business day once the CRM product owner has approved |
| Daily API request allowance | 115,000 requests per rolling 24 hours across all integrations |
| Field history retention | 24 months of field history, after which entries are purged |

**Number of supported profiles.** The number of supported profiles is 9 profiles, with all additional access granted through permission sets. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Import row threshold.** The import row threshold is 50,000 rows through the Data Import Wizard; anything larger must go through Data Loader. This is configured centrally in Salesforce and is not adjustable per user or per team.

**Sandbox refresh intervals.** The sandbox refresh intervals is a full sandbox every 29 days and a partial copy sandbox every 5 days. Where a user asks for a different figure, the answer is the exception process described later in this document.

**Permission set assignment turnaround.** The permission set assignment turnaround is 1 business day once the CRM product owner has approved. This is configured centrally in Salesforce and is not adjustable per user or per team.

**Daily API request allowance.** The daily API request allowance is 115,000 requests per rolling 24 hours across all integrations. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

**Field history retention.** The field history retention is 24 months of field history, after which entries are purged. Agents should quote this figure directly to users rather than estimating, because an incorrect estimate generates a repeat contact.

These values are reviewed at each annual review of this document, and may be changed sooner if Information Security revises the underlying risk assessment. Users occasionally ask for these to be relaxed for convenience. The answer is the exception process, not an informal adjustment by an engineer. Where a figure here is expressed in business hours, that means 08:00 to 18:00 local time on working days, excluding public holidays in the user's country.

## Risk rationale

The controls in this document address a small number of specific risks. Stating them makes it easier to judge an exception request on its merits rather than on how urgently it is asked for.

**Unauthorised access to corporate data.** The access controls and approval routes described above exist to make sure that access is granted deliberately, by someone accountable, and removed when it is no longer needed. An exception that removes the approval step does not reduce this risk, it transfers it.

**Loss of availability.** The parameters in this document are chosen so that the service stays within its supported operating envelope. Raising a published limit for one team without a capacity review moves the risk to every other user of the service.

**Inability to demonstrate control.** Several requirements here exist because the control must be evidenced to an auditor, not only operated. Work done outside a ticket may be perfectly correct and still fail an audit, because there is nothing to sample.

**Configuration drift.** Where the running state of Salesforce diverges from the parameters published here, users receive inconsistent answers and the service desk loses credibility. Drift is tracked as a defect with a named owner, not as an acceptable variation.

Residual risk after these controls is accepted by the service owner, Business Applications, and reviewed annually with Information Security.

## Architecture and dependencies

Salesforce is the system of record for this service. It integrates with the corporate directory for identity, with the service management platform for ticketing, and with the logging platform for audit. A failure in any of those three dependencies will present to users as a failure of this service, so agents should check dependency status before diagnosing an individual fault.

Changes to Salesforce follow the change management policy. Standard changes are pre-approved and can be applied inside the normal maintenance window. Anything that alters a parameter published in this document is a normal change and requires review, because the published figure and the running configuration must not diverge.

Business Applications maintains a runbook for recovering the service after a platform outage. That runbook is held separately because it contains credentials references and is restricted to the on-call rota. The service desk does not need it; during a platform outage the service desk follows the major incident communications process instead.

Capacity for this service is reviewed monthly against the parameters above. Where usage is trending towards a published limit, Business Applications raises the increase through change management ahead of the limit being reached, rather than waiting for users to hit it. Capacity requests raised reactively, after a limit has already been reached, are treated as incidents rather than changes, and are reported as such in the monthly service review so that the underlying planning gap stays visible.

## Interfaces with other services

This service does not operate in isolation, and several common faults are actually faults in an adjacent service presenting here.

**Identity.** Account state, group membership and multi-factor registration all originate in the identity platform. If a user cannot authenticate to Salesforce, confirm the account is enabled and the required group membership is present before investigating further.

**Endpoint management.** Device compliance state, patch level and encryption status are owned by End User Computing. Where a control in this document depends on device posture, the authoritative source is the endpoint management console, not what the user reports.

**Networking.** Connectivity, name resolution and certificate distribution are owned by Network Operations. A symptom that affects one office and not another is almost always a network matter.

**Service management.** Ticket routing, priority assignment and service level measurement are owned by the Service Management Office. Queue names referenced in this document are maintained there, and a queue rename is a change that must be reflected in this document.

**Information Security.** Risk thresholds, exception approval and incident declaration sit with Information Security. Business Applications implements the thresholds but does not set them.

## Procedures

The procedures in this section are the supported way to carry out common tasks against this service. Follow them in order. If a step cannot be completed as written, stop and escalate to Business Applications rather than skipping it.

### Assigning a permission set

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the requested access is not already covered by the user's profile.
2. Route the request to the CRM product owner for approval.
3. Assign the permission set to the user rather than editing the profile.
4. Verify the user can reach the intended records and nothing more.
5. Close the request within 1 business day of the approval.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Running a data import

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Validate the source file headers against the target object fields.
2. Run the import in a sandbox first and review the error file.
3. Choose the Data Import Wizard below 50,000 rows and Data Loader above it.
4. Capture the record identifiers created so the load can be reversed if needed.
5. Run the production import outside business hours and confirm the row counts.
6. Attach the success and error files to the ticket.

Where approval is required, the approval must be captured in the ticket. A verbal approval is not sufficient on its own.

### Refreshing a sandbox

This procedure is carried out by the service desk unless a step says otherwise. Before starting, confirm the requester is who they say they are and that a ticket exists.

1. Confirm the sandbox is past its refresh interval of 29 days for full or 5 days for partial copy.
2. Notify all sandbox users at least 3 business days in advance.
3. Ask developers to commit unreleased work to the version control repository.
4. Start the refresh and monitor it to completion.
5. Reapply the post-refresh configuration such as email deliverability and test data.

Expect this to take longer the first time. Agents new to the service should pair with a colleague for their first few requests.

## Troubleshooting

This section covers the faults the service desk sees most often against this service. Each entry gives the symptom as the user is likely to describe it, the underlying cause, and the resolution. If the symptom matches but the resolution does not work, escalate to Business Applications with the diagnostic output attached rather than retrying the same steps.

### Symptom: An integration stops writing records and logs D-SF-17003


**Error code:** D-SF-17003

**Cause.** The 115,000 daily API request allowance has been exhausted by one of the integrations.

**Resolution.** Open the API usage report and identify which integration consumed the allowance. Pause that integration and move its bulk work onto the Bulk API, which consumes far fewer requests. Escalate to Business Applications if the allowance is being hit on more than two days in a month, as the integration design needs review.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Capture the exact wording of any on-screen message before you change anything. It is frequently the fastest route to the cause.

### Symptom: A data import fails partway and returns D-SF-26114


**Error code:** D-SF-26114

**Cause.** The file exceeds the 50,000 row limit for the Data Import Wizard.

**Resolution.** Stop the import and reconcile which rows were created using the captured identifiers. Re-run the load through Data Loader in batches. Escalate to Business Applications if partial records have already triggered downstream automation.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Confirm with the user that the issue is resolved before closing the ticket. A ticket closed on assumption usually reopens.

### Symptom: A user cannot see an object their colleague can see


**Cause.** The colleague holds an additional permission set that the user has not been assigned.

**Resolution.** Compare the two users in the setup audit view to identify the missing permission set. Raise a request to the CRM product owner for approval rather than editing the profile. Assignment completes within 1 business day of approval.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

### Symptom: Unreleased configuration disappears from a sandbox and the log shows D-SF-31508


**Error code:** D-SF-31508

**Cause.** The sandbox was refreshed on its 29 day cycle and the work had not been committed to version control.

**Resolution.** Check the version control repository for the last commit and rebuild from there. Confirm the refresh notice was issued 3 business days in advance and record the gap if it was not. Escalate to Business Applications to review the notification process if users were not warned.

**Before escalating.** Capture the device name, the signed-in account, the exact time of the failure and any on-screen message. Check whether other users are reporting the same symptom before treating it as an individual fault. A cluster usually means a platform change.

## Diagnostics

Diagnostics are gathered before any change is made. The sequence below produces enough evidence for Business Applications to take an escalation without coming back for more detail, which is the usual reason an escalated ticket bounces.

### Diagnostics for: An integration stops writing records and logs D-SF-17003

Reference: D-SF-17003.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Salesforce and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Business Applications citing the reference above.

### Diagnostics for: A data import fails partway and returns D-SF-26114

Reference: D-SF-26114.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Salesforce and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Business Applications citing the reference above.

### Diagnostics for: A user cannot see an object their colleague can see

Reference: no code reported.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Salesforce and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Business Applications citing the reference above.

### Diagnostics for: Unreleased configuration disappears from a sandbox and the log shows D

Reference: D-SF-31508.

1. Record the exact time of the failure and the time zone the user is in.
2. Capture the device name, serial or asset tag, and the signed-in account.
3. Confirm whether the symptom reproduces on a second device for the same user, and on the same device for a second user. That pair of checks separates an account problem from a device problem faster than anything else.
4. Check the status of Salesforce and its directory and logging dependencies before treating this as an individual fault.
5. Collect the relevant log bundle and attach it to the ticket rather than pasting fragments into the ticket notes.

If all five checks are clean and the symptom persists, escalate to Business Applications citing the reference above.

## Worked examples

### Example: An integration stops writing records and logs D-SF-17003

A user at London HQ contacts the service desk reporting that an integration stops writing records and logs D-SF-17003. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The 115,000 daily API request allowance has been exhausted by one of the integrations. Following the documented resolution, open the API usage report and identify which integration consumed the allowance. Pause that integration and move its bulk work onto the Bulk API, which consumes far fewer requests. Escalate to Business Applications if the allowance is being hit on more than two days in a month, as the integration design needs review.

The agent records the diagnosis against the ticket, confirms with tariq.santos@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Business Applications was needed.

### Example: A data import fails partway and returns D-SF-26114

A user at Singapore contacts the service desk reporting that a data import fails partway and returns D-SF-26114. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The file exceeds the 50,000 row limit for the Data Import Wizard. Following the documented resolution, stop the import and reconcile which rows were created using the captured identifiers. Re-run the load through Data Loader in batches. Escalate to Business Applications if partial records have already triggered downstream automation.

The agent records the diagnosis against the ticket, confirms with tobias.vasquez@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Business Applications was needed.

### Example: A user cannot see an object their colleague can see

A user at Manchester contacts the service desk reporting that a user cannot see an object their colleague can see. The agent confirms the identity of the requester, checks whether anyone else has reported the same symptom in the last hour, and finds no cluster.

The agent recognises the pattern: The colleague holds an additional permission set that the user has not been assigned. Following the documented resolution, compare the two users in the setup audit view to identify the missing permission set. Raise a request to the CRM product owner for approval rather than editing the profile. Assignment completes within 1 business day of approval.

The agent records the diagnosis against the ticket, confirms with amara.santos@meridiangroup.example that the problem is resolved, and closes the ticket within the service level target. No escalation to Business Applications was needed.

### Example: assigning a permission set

A line manager raises a request through https://help.meridiangroup.example. The agent checks the request carries the approvals this document requires, then works through the documented steps in order, recording the ticket reference against each step that changes a production configuration.

The most common reason this procedure stalls is a missing approval rather than a technical fault. Agents should check that first rather than opening a vendor case. Once complete, the agent confirms the outcome with the requester and closes the ticket.

## Common misconceptions

The following come up repeatedly in contacts about CRM application support. Correcting them early in a conversation shortens the call and reduces repeat contacts.

**Misconception: the number of supported profiles is flexible or negotiable per user.**

It is not. The number of supported profiles is 9 profiles, with all additional access granted through permission sets, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the import row threshold is flexible or negotiable per user.**

It is not. The import row threshold is 50,000 rows through the Data Import Wizard; anything larger must go through Data Loader, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the sandbox refresh intervals is flexible or negotiable per user.**

It is not. The sandbox refresh intervals is a full sandbox every 29 days and a partial copy sandbox every 5 days, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: the permission set assignment turnaround is flexible or negotiable per user.**

It is not. The permission set assignment turnaround is 1 business day once the CRM product owner has approved, it is set centrally, and the service desk cannot vary it. A user who needs a different figure should be directed to the exception process rather than being told that it might be possible. Setting that expectation accurately at first contact is the difference between one ticket and three.

**Misconception: Business Applications can be asked directly over chat.**

Work requested outside a ticket is invisible to reporting, does not accrue against a service level target, and cannot be audited. Agents should route the request through https://help.meridiangroup.example even when they have a direct line to the engineer concerned.

## Measurement and reporting

The following measures are reported monthly to the technology leadership team for this service.

- Volume of contacts to the service desk relating to CRM application support, split by the troubleshooting categories in this document.
- Proportion resolved at first line without escalation to Business Applications.
- Mean time to resolve, measured against the priority assigned at the point the ticket was raised.
- Number of open exceptions against the controls in this document, and the age of the oldest.
- Count of configuration drift findings, meaning cases where the running state of Salesforce did not match the published parameters.

A sustained rise in first line contact volume for a single symptom is treated as a signal that either the control is poorly understood or the user guidance is wrong. In either case the remedy is to fix the documentation rather than to absorb the contact volume indefinitely.

Where a measure misses target for two consecutive months, Business Applications produces an improvement plan with named actions and dates, and reports progress at the quarterly service review.

## Training and competency

Service desk agents are expected to be competent in the procedures and troubleshooting entries in this document before taking contacts about CRM application support unsupervised.

Competency is demonstrated by working through the procedures with an experienced colleague, handling a small number of live contacts under observation, and being able to quote the service parameters without looking them up. The last of those matters more than it sounds: an agent who hesitates on a published figure invites the user to negotiate it.

Business Applications runs a refresher whenever a parameter changes, whenever a new troubleshooting entry is added, and at least once a year. Attendance is recorded against the agent's training record.

New entries are added to the troubleshooting section when a symptom has been seen three times and the resolution is stable. Adding an entry after the first occurrence tends to enshrine a workaround that later turns out to be wrong.

## Frequently asked questions

**Can I get a new profile created for my team?**

No. The supported set stays at 9 profiles, and extra access is delivered through permission sets.

**How many rows can I load with the Data Import Wizard?**

Up to 50,000 rows; anything larger must go through Data Loader.

**How soon will my permission set be assigned?**

Within 1 business day of the CRM product owner approving the request.

**How long is field history kept?**

24 months, after which the entries are purged.

**Who do I contact if my question is not answered here?**

Raise a ticket through https://help.meridiangroup.example or email servicedesk@meridiangroup.example. Include the system you were using, what you expected to happen, and what actually happened. If a question comes up often enough to be worth answering here, Business Applications will add it at the next review of this document.

**Can the service desk make an exception for me?**

No. The service desk operates the controls in this document but does not own them. Exceptions are requested in writing, carry a named business owner and an end date, and are approved by Information Security. An agent who agrees an informal variation creates a finding at the next audit, so please do not ask them to.

## Escalation

First line is the service desk, reachable through https://help.meridiangroup.example or servicedesk@meridiangroup.example. Agents work to the priority matrix in the service level policy.

Second line is Business Applications, engaged through the ticket rather than by direct message, so that the work remains visible and the clock on the service level target keeps running against the right queue.

Third line is the vendor for Salesforce, engaged by Business Applications only. The service desk should not open vendor cases directly, because the entitlement is held centrally and a duplicate case slows the real one down.

Major incidents follow the security incident response runbook instead of this escalation path, and are declared by the duty incident manager.

## Compliance, exceptions and audit

Records produced under this document are retained for the period set out in the data classification policy for the relevant tier.

Exceptions must be requested in writing through https://help.meridiangroup.example, must carry a named business owner and an end date, and are approved by Information Security. An exception without an end date will not be approved.

Approved exceptions are logged in the exception register and reviewed at expiry. A lapsed exception reverts to the standard control automatically.

Business Applications produces a compliance report each quarter showing the number of exceptions open, the number of breaches detected, and the mean time to close.

Where a control in this document cannot be met for a specific system, the compensating control must be documented in the exception record and reviewed at the same cadence.

## Appendices

### Appendix A: service desk checklist

Use this when handling a contact about CRM application support. It is a shortened form of the procedures above and is not a substitute for them.

- [ ] Confirm the identity of the requester.
- [ ] Confirm a ticket exists and is in the correct queue.
- [ ] Check whether the symptom matches a known entry in the troubleshooting section.
- [ ] Confirm the requested access is not already covered by the user's profile.
- [ ] Route the request to the CRM product owner for approval.
- [ ] Validate the source file headers against the target object fields.
- [ ] Run the import in a sandbox first and review the error file.
- [ ] Confirm the sandbox is past its refresh interval of 29 days for full or 5 days for partial copy.
- [ ] Notify all sandbox users at least 3 business days in advance.
- [ ] Record the outcome and confirm resolution with the user before closing.

### Appendix B: user-facing guidance

The text below can be pasted into a reply to a user without modification. It has been reviewed for tone and for accuracy against the parameters in this document.

- Can I get a new profile created for my team? No. The supported set stays at 9 profiles, and extra access is delivered through permission sets.
- How many rows can I load with the Data Import Wizard? Up to 50,000 rows; anything larger must go through Data Loader.
- How soon will my permission set be assigned? Within 1 business day of the CRM product owner approving the request.
- How long is field history kept? 24 months, after which the entries are purged.

### Appendix C: related documents

- Service Desk Service Level Policy
- Data Classification Policy
- Change Management Policy
- Security Incident Response Runbook
- Password and Multi-Factor Authentication Policy

### Appendix D: revision history

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2024-03-11 | Business Applications | First published version. |
| 1.1 | 2024-11-02 | Business Applications | Parameters reviewed, no change to control intent. |
| 2.0 | 2025-06-18 | Business Applications | Restructured to the standard template; troubleshooting section added. |
| 2.1 | 2026-02-09 | Business Applications | Annual review; figures confirmed against the running configuration of Salesforce. |
