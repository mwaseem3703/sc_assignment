# Context

Course: CSE325 Software Construction and Development
Student: M. Waseem (SP24-BSE-053)
Lab 5: NLP for Requirements Engineering

# Raw Stakeholder Notes

"We need the app to let students log in with their university email. It should be fast and secure. Students register for events and get a reminder before each event. Admins can add or remove events. Login must also be quick. The system should handle many users."

# Task 1: Extraction & Traceability

REQ-1: Students log in with university email (Functional) - Source: "let students log in with their university email"
REQ-2: System should be fast (Non-Functional) - Source: "It should be fast"
REQ-3: System must be secure (Non-Functional) - Source: "and secure."
REQ-4: Register for events (Functional) - Source: "Students register for events"
REQ-5: Reminders before events (Functional) - Source: "get a reminder before each event."
REQ-6: Admins add/remove events (Functional) - Source: "Admins can add or remove events."
REQ-7: Login time quick (Non-Functional) - Source: "Login must also be quick."
REQ-8: Handle high volume (Non-Functional) - Source: "handle many users."
REQ-9: Support multiple languages (Non-Functional) - UNSOURCED (AI Hallucination)

# Task 2: AI Invention

The AI hallucinated REQ-9. It over-read the phrase "handle many users" and assumed we needed internationalization. On a second run, it invented "ID card integration".

# Task 3: Testable Rewrites

Vague 1: "It should be fast"
Strict: Login completes in under 2 seconds on campus WiFi, 95% of the time.
Test: Use JMeter on campus network; 1000 requests, 95th percentile < 2.0s.

Vague 2: "handle many users"
Strict: Support 5,000 concurrent active users without degrading response time.
Test: Cloud load test with 5,000 virtual users; server response remains < 2.0s.

# Task 4: Duplicates & Contradictions

Duplicate: "fast" (Sentence 2) and "quick" (Sentence 5) are the exact same requirement.
Conflict: "Fast/many users" conflicts with "secure." Heavy security (MFA, encryption) inherently slows down login times. We need to ask the stakeholder which takes priority.
