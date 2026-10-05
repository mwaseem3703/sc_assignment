# Lab 5: NLP for Requirements Engineering

## **Student Information**

- Course: CSE325 Software Construction and Development
- Student: M. Waseem (SP24-BSE-053)
- Lab Title: NLP for Requirements Engineering

---

## **Task 1: Extraction and Traceability**

The stakeholder notes were analyzed to extract both functional and non-functional requirements and to trace each requirement to its corresponding source statement. This step is essential to ensure that each requirement is evidence-based and supported by the original domain context.

| Requirement ID | Requirement Statement                                                 | Type           | Source Evidence                                   | Validation               |
| -------------- | --------------------------------------------------------------------- | -------------- | ------------------------------------------------- | ------------------------ |
| REQ-1          | Students must be able to log in using their university email address. | Functional     | “let students log in with their university email” | Valid                    |
| REQ-2          | The system should be efficient and responsive.                        | Non-Functional | “It should be fast”                               | Valid                    |
| REQ-3          | The system must provide secure access and operations.                 | Non-Functional | “and secure.”                                     | Valid                    |
| REQ-4          | Students must be able to register for events.                         | Functional     | “Students register for events”                    | Valid                    |
| REQ-5          | Students should receive a reminder before each event.                 | Functional     | “get a reminder before each event.”               | Valid                    |
| REQ-6          | Administrators must be able to add and remove events.                 | Functional     | “Admins can add or remove events.”                | Valid                    |
| REQ-7          | Login should be quick and efficient.                                  | Non-Functional | “Login must also be quick.”                       | Valid                    |
| REQ-8          | The system should handle a high volume of users.                      | Non-Functional | “handle many users.”                              | Valid                    |
| REQ-9          | The system should support multiple languages.                         | Non-Functional | No direct source in the stakeholder notes         | Rejected as hallucinated |

### **Interpretation of Task 1**

Eight requirements were identified as valid and traceable to the raw stakeholder inputs. REQ-9 was excluded because it was not supported by explicit textual evidence and therefore represents an AI-generated invention rather than a legitimate requirement.

---

## **Task 2: AI Invention and Hallucination Review**

This task evaluates the extent to which artificial intelligence introduced requirements without adequate evidence from the source material.

### **Hallucinated Requirement Identified**

The requirement concerning support for multiple languages is an example of hallucination. The phrase “handle many users” was incorrectly interpreted as a need for multilingual support, which is not stated anywhere in the stakeholder notes. A second AI output also invented a requirement involving ID card integration, which was likewise unsupported by the original requirement source.

### **Reason for Rejection**

- The source text discusses scalability and capacity, not localization.
- “Handle many users” refers to system load and performance, not language features.
- No mention of identification cards, language support, or other unrelated features appears in the stakeholder notes.

### **Conclusion for Task 2**

The requirement extraction process must always remain evidence-based. Requirements must be traceable to source text, and unsupported assumptions should be rejected to preserve the integrity of the software specification.

---

## **Task 3: Testable Requirement Rewrites**

The original notes contained vague statements that were not sufficiently measurable for implementation or validation. These were rewritten into testable requirements using clear performance thresholds and acceptance criteria.

### **Rewrite 1: Performance of Login**

| Field                | Details                                                                       |
| -------------------- | ----------------------------------------------------------------------------- |
| Original Statement   | “It should be fast”                                                           |
| Revised Requirement  | Login must complete in under 2 seconds on campus Wi-Fi for 95% of requests.   |
| Validation Method    | Conduct testing with JMeter on the campus network using 1,000 login requests. |
| Acceptance Criterion | The 95th percentile response time must be less than 2.0 seconds.              |

### **Rewrite 2: Scalability of the System**

| Field                | Details                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Original Statement   | “handle many users”                                                                                                    |
| Revised Requirement  | The system must support 5,000 concurrent active users without degrading response time beyond the acceptable threshold. |
| Validation Method    | Perform a cloud-based load test with 5,000 virtual users.                                                              |
| Acceptance Criterion | Server response time remains below 2.0 seconds during the test.                                                        |

### **Importance of Testable Requirements**

The conversion of vague requirements into measurable criteria enhances clarity, supports validation, and reduces the risk of ambiguity during design and implementation. Testable requirements are essential in ensuring that stakeholder expectations are met and that software quality can be evaluated objectively.

---

## **Task 4: Duplicates and Contradictions**

This task identifies overlapping requirements and competing constraints that should be clarified before final system specification.

| Issue Type | Requirement(s)                             | Explanation                                                                                             | Recommended Resolution                                                   |
| ---------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Duplicate  | “fast” and “quick”                         | Both statements describe the same concern: login performance should be rapid.                           | Combine into a single requirement to avoid redundancy.                   |
| Conflict   | “fast / handle many users” versus “secure” | Strong security mechanisms such as MFA and encryption can increase login latency and reduce throughput. | Stakeholder priority must be clarified between performance and security. |

### **Analysis of Duplicates and Contradictions**

The requirement set contains a redundancy in the performance criteria and a significant trade-off between speed and security. While speed is important for usability, high security requirements may introduce latency and additional processing overhead. This indicates that the final specification should include explicit priority guidance from the stakeholder to resolve the conflict.

---

## **Conclusion**

The stakeholder requirements highlight a system focused on secure student authentication, event registration, reminder notifications, and administrative event management. However, the specification must be refined through traceability, validation, and conflict resolution. In particular, unsupported AI-generated requirements must be removed, vague statements must be rewritten as measurable constraints, and performance-security trade-offs must be aligned with stakeholder priorities to produce a reliable and implementable requirements specification.

---

## **Final Summary**

Overall, this lab demonstrates the importance of disciplined requirements engineering. Reliable requirements must be evidence-based, traceable, testable, and free from hallucinations or unnecessary assumptions. By applying these principles, a software team can create a specification that is both academically sound and practically implementable.
