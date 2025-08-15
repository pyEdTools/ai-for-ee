# Instructor's Guide

## 1. Assignment philosophy

This assignment is designed to teach modern programming skills in a way that is both engaging and authentic. The core philosophy rests on two pillars:

1.  **AI as a pair programmer:** We position AI not as a magic black box, but as a "pair programmer." This requires students to learn the crucial skill of **prompt engineering** how to ask good questions to get good answers. It teaches them to be critical of AI-generated code and to use it as a starting point, not a final product.

2.  **Hardware-in-the-loop verification:** The requirement to validate code with physical hardware is the cornerstone of the assignment's authenticity. An AI can write code, but it cannot build a circuit or verify that the code works in the real world. This forces students to understand, adapt, and debug the code, ensuring they are active participants in their learning.

## 2. Learning objectives

After completing this assignment, students will be able to:

-   Effectively use an LLM as a pair programmer to brainstorm, generate, and debug code.
-   Apply prompt engineering principles to elicit desired responses from an AI.
-   Interface a microcontroller (Pico or Arduino) with sensors and actuators.
-   Write a complete, functional program that solves a problem using hardware I/O.
-   Maintain a detailed log of their development process.
-   Critically reflect on the capabilities and limitations of AI in software development.

## 3. Suggested timeline (6-Week example)

This assignment can be adapted, but a 6-week timeline is often effective (in a semester long course).

-   **Week 1: Introduction and setup**
    -   Introduce the assignment, the philosophy, and the submission requirements.
    -   Lecture on AI pair programming and walk through the `guide_to_ai_prompts.md`.
    -   **Lab/Homework:** Students select their project, acquire their hardware, and perform a "Hello World" equivalent for their hardware (e.g., blinking an LED) to ensure their setup works. They should write their first journal entry.

-   **Week 2: Core Development**
    -   This week is dedicated to working on the project.
    -   **Check-in:** It is highly recommended to have a mandatory check-in (in person or via a short progress report) to ensure students are making progress and not getting stuck. This is a good time to discuss their AI interactions.

-   **Week 3: Finalizing & Submission**
    -   Students should be finishing their code, finalizing their hardware setup, and recording their verification video.
    -   A significant portion of this week should be spent on writing the final reflection essay in their journal.
    -   **Due Date:** End of Week 3.

## 4. Common student challenges and how to help

-   **"The AI's code doesn't work!"**
    -   This is a feature, not a bug, of the assignment. Guide the student to treat this as a debugging challenge. Ask them: "What was your prompt? What was the error? How could you rephrase your prompt to be more specific? What have you tried so far to fix it yourself?"

-   **Over-reliance on the AI:**
    -   Some students may try to have the AI write the entire project at once. The reflection journal and AI transcript are your primary tools to combat this. Emphasize that a huge block of code pasted from the AI with no iterative dialogue will be graded poorly. The process is as important as the product.

-   **Hardware/wiring issues:**
(use of Learning assistant)
    -   Encourage students to start with the simplest possible circuit (like blinking an LED) to verify that their board and computer are communicating correctly before they add sensors. Have them double-check their wiring against a diagram.

-   **Vague prompts and frustration:**
    -   If a student is frustrated, ask to see their AI conversation. Often, they are using vague prompts like "it's broken." Walk them through creating a better prompt using the "Four C's" from the guide.

## 5. Grading and assessment

Refer to the `assessment_rubric.md` for detailed criteria. Key points for grading:

-   **The reflection journal is key:** This is where you will see the student's learning process. A good journal shows evidence of trial and error, critical thinking about the AI's suggestions, and a clear narrative of their project's development. A lazy journal is a red flag.
-   **The AI transcript tells a story:** Look for an iterative process. Does the student ask follow-up questions? Do they refine their prompts? Or did they just ask the AI to "write the whole thing"?
-   **Hardware video:** The video doesn't need to be high-production. It simply needs to clearly show the circuit and the corresponding software output, proving that the project works as intended.

## 6. Hardware management

-   **Student-purchased kits:** This is often the simplest approach logistically. Provide students with a link to the `hardware_recommendations.md` file and a list of 2-3 specific kits you recommend from online retailers.
-   **Department-provided kits:** If the department provides kits, ensure you have a good system for checking them in and out. It can be helpful to have a lab session dedicated to ensuring all the components in the kits are working at the start of the assignment.
