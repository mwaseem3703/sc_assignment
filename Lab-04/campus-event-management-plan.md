# Campus Event Management System Plan

## Step 1: Functional Modules

- **Event discovery**
  - **E1:** Display upcoming published events with their title, date, time, location, and summary.
  - **E2:** Show an event’s full details and whether registration is available.
  - **E3:** Let students search events by title and filter by date or category.
- **Registration**
  - **R1:** Record a student’s registration for a selected event.
  - **R2:** Prevent the same student from registering for the same event more than once.
  - **R3:** Let students cancel their registration before the event.
- **Reminders**
  - **N1:** Schedule a reminder for each registered student before the event.
  - **N2:** Send the reminder with the event’s title, time, and location.
  - **N3:** Track reminder delivery and retry after a temporary delivery failure.
- **Event administration**
  - **A1:** Let an admin create and publish an event.
  - **A2:** Let an admin remove an event from the published listings.
  - **A3:** Validate required event details before an event is published.

## Steps 2–3: User Stories and MoSCoW

### Event discovery

- **E1** As a student, I want to browse upcoming events with their key details so that I can find events I may want to attend.
  - **Must** — Browsing upcoming events is the system’s core student-facing capability.
- **E2** As a student, I want to view an event’s full details and registration availability so that I can decide whether to register.
  - **Must** — Students need event details and availability to make an informed registration decision.
- **E3** As a student, I want to search and filter events so that I can find relevant events more quickly.
  - **Should** — Search and filtering improve discovery but are not essential to basic browsing.

### Registration

- **R1** As a student, I want to register for an event so that my attendance is recorded.
  - **Must** — Event registration is one of the system’s central requirements.
- **R2** As a student, I want duplicate registrations to be prevented so that my registration status remains accurate.
  - **Must** — Duplicate records could make attendance and registration counts unreliable.
- **R3** As a student, I want to cancel my registration before an event so that I can release my place if my plans change.
  - **Could** — The brief does not request registration cancellation, though it may be useful later.

### Reminders

- **N1** As a registered student, I want to receive a reminder before an event so that I do not forget to attend.
  - **Must** — The brief explicitly requires reminders for students.
- **N2** As a registered student, I want the reminder to include the event’s time and location so that I know when and where to go.
  - **Should** — These details make reminders actionable, although the brief does not specify their contents.
- **N3** As an admin, I want failed reminders to be tracked and retried so that temporary delivery problems do not silently prevent notifications.
  - **Could** — Delivery tracking and retries improve reliability but are not specified in the brief.

### Event administration

- **A1** As an admin, I want to create and publish events so that students can discover and register for them.
  - **Must** — The brief explicitly requires admins to add events.
- **A2** As an admin, I want to remove events from published listings so that students do not register for events that are no longer available.
  - **Must** — The brief explicitly requires admins to remove events.
- **A3** As an admin, I want required event details to be validated before publishing so that students see usable event information.
  - **Should** — Validation prevents incomplete listings but is not explicitly required by the brief.

## Lab Follow-Through

The two additional prompts below are examples, not a truthful record of prior attempts. Since they were not run before the detailed prompt, do not present them as historical log entries. For a valid log, run and record your own two superseded attempts before the final prompt:

- “Plan an event system for me.”
- “Give me a campus events app plan.”

After reviewing the plan, do your own audit: identify a task outside the brief and explain why it goes beyond scope; record two requirements you believe the response missed; defend three Must stories in your own words; and add one requirement grounded in COMSATS University Vehari Campus. The response covers the brief’s four stated capabilities, so don’t claim it forgot one of those unless you can point to a specific omission.
