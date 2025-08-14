# Model AI Assignment: AI Pair Programming with Hardware-in-the-Loop Verification

**Note: The primary entry point for this submission package is the `index.html` file.**

This document serves as a detailed, single-file overview of the assignment proposal.

---

## Abstract

We introduce an open-ended project-based assignment for introductory programming courses. It positions LLMs as collaborative programmers, while ensuring student agency by requiring feasible hardware validation for the computer programs. The goal is to promote student learning by asking students to complete joint software-hardware tasks that AI agents cannot complete due to the hardware validation requirement. Specifically, the assignment asks students to pick a personal project (from an instructor provided list) and build it with an AI partner. The key step is validating the final code with a real hardware setup. This moves beyond pure simulation and compels students to ground their code, and their understanding, in real-world interactions. Students keep a reflection journal and submit their AI chats, showing their thought process. Using low-cost hardware ensures students are active participants. They must understand, adapt, and verify the AI's output, not just copy it. This fosters a deeper, more authentic learning experience and shows students how to use AI tools. The assignment is highly adaptable, with many personalized project options to promote engagement, agency, and creativity. The list of open-ended projects, instructional material, and steps for integrating hardware components into each project will be available as an open-access resource.

---

## Content for `index.html`

This section provides the metadata required for the [Model AI Assignments](http://modelai.gettysburg.edu/) website.

- **Summary:** This assignment challenges students to build a complete, personalized project by partnering with an AI assistant. Students learn to use the AI as a pair programmer to brainstorm, write, and debug code. The key requirement is that the final project must be verified using physical hardware, ensuring that students can connect their software to real-world outcomes. The process emphasizes practical skills like prompt engineering and critical thinking, and students document their journey in a reflection journal while producing valid and verifiable engineering systems.

- **Topics:**
    - **Primary AI Topic:** AI as a Tool, Human-AI Interaction, AI-assisted Development.
    - **Secondary AI Topics:** Prompt engineering, AI-assisted debugging, LLM capabilities and limitations.
    - **Computer Science Topics:** Introductory Python programming, Hardware interfacing, APIs, Data handling, Simulation.

- **Audience:** This assignment is designed for undergraduate students in their first or second year of study. It is suitable for **CS1/CS2** courses, introductory programming courses for engineers (e.g., "AI for EE"), or introductory AI courses that want to include a practical, hands-on component. No prior experience with AI or hardware is assumed.

- **Difficulty:** **Easy to Medium.** The difficulty is scalable based on the project chosen. The core concepts are accessible to beginners, while more advanced students can choose projects with greater complexity.

- **Strengths:**
    - **High engagement:** Students work on personalized projects they choose, increasing motivation.
    - **Practical skills:** Teaches the modern skill of using AI tools effectively and responsibly in a development workflow.
    - **Authentic assessment:** Hardware verification provides a clear success metric and prevents students from submitting AI-generated code without understanding it.
    - **Demystifies AI:** Provides a concrete understanding of what AI can and cannot do in a programming context.
    - **Flexibility:** Easily adaptable to different course levels, topics, and timeframes.

- **Weaknesses:**
    - **Hardware requirement:** Requires access to low-cost hardware (therefore, requires funds to suppor the project). This is a significant barrier/weakness.
    - **AI variability:** The performance and responses of AI models can be unpredictable.
    - **Instructor overhead:** Requires instructors (and students!) to be comfortable with guiding students through a less deterministic process than traditional assignments.
    - **Potential for over-reliance:** Instructors must actively guide students to think critically and not just copy-paste AI output.

- **Dependencies:**
    - **Software:** Python 3.x, access to a web-based LLM (e.g., ChatGPT, Google Gemini), standard Python libraries (`requests`, `matplotlib`, etc., depending on the project).
    - **Hardware:** A low-cost microcontroller kit. We recommend the Raspberry Pi Pico W or Arduino Uno, along with basic components like LEDs, sensors, and resistors.

- **Variants:**
    - **Group project:** Can be adapted for pairs or small groups of students.
    - **Advanced version:** For upper-level courses, the complexity of the hardware and software can be increased (e.g., using more advanced sensors, requiring communication protocols like MQTT, or analyzing more complex datasets).
    - **Software-only verification:** For courses without a hardware component, the verification step can be replaced with a different form of validation, such as a rigorous unit testing suite, a live user-testing session, or a detailed data validation report against a known dataset.

---

## Assignment Materials

### For Students

- **`assignment_description.md`**: A detailed description of the assignment, learning objectives, and submission requirements. (Adapted from `lab9_fall2024.md`).
- **`project_ideas.md`**: A list of curated project ideas with descriptions, hardware suggestions, and estimated costs.
- **`guide_to_ai_prompts.md`**: A guide with examples of effective and ineffective prompts for interacting with the AI pair programmer.
- **`example_submission/`**: A complete example submission for one of the projects, including the code, reflection journal, and AI transcript.

### For Instructors

- **`instructor_guide.md`**: A guide for instructors on how to run the assignment, common pitfalls to watch for, and tips for grading.
- **`assessment_rubric.md`**: A detailed rubric for grading the student submissions. See the file in `instructor_materials/`.
- **`hardware_recommendations.md`**: A list of recommended hardware kits and components, with links to purchase.

---

## Suggestions for use

- **Scaffolding:** Start with a small in-class exercise where all students use an AI to solve the same simple problem before starting the main project.
- **Check-ins:** Schedule mandatory check-ins or milestones to ensure students are on track and to discuss their AI interaction strategies.
- **Focus on reflection:** Emphasize that the reflection journal is a major part of the grade. This encourages students to think about *how* they are working, not just the final product.
- **Embrace failure:** Encourage students to document their errors and failed attempts in their journals. Frame these as learning opportunities.