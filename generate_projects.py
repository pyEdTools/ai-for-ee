import json

def get_verification_method(categories):
    """Determines the verification method based on project categories."""
    if 'hardware' in categories:
        return "**Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors)."
    elif 'data' in categories:
        return "**Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results."
    elif 'simulations' in categories:
        return "**Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly."
    elif 'game' in categories:
        return "**Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described."
    else:
        return "**Verification Method:** The program's output must be compared against a known-correct source or calculation to prove its accuracy."

def main():
    """Reads project data from JSON and generates a comprehensive markdown file."""
    try:
        # This script runs from the root, so the JSON file is at the top level.
        with open('all_cs1_projects.json', 'r') as f:
            projects = json.load(f)
    except FileNotFoundError:
        print("Error: all_cs1_projects.json not found in the root directory.")
        return

    markdown_content = "# Project Ideas\n\n"
    markdown_content += "This document provides a comprehensive list of potential projects that can be assigned to students. Each project includes a tangible verification method, ensuring students connect their software with a real-world or demonstrable outcome. The complexity can be scaled to suit different student levels.\n\n---\n\n"

    for project in projects:
        title = project.get('title', 'No Title')
        description = project.get('description', 'No description available.')
        categories = project.get('categories', [])

        verification = get_verification_method(categories)

        markdown_content += f"### {title}\n"
        markdown_content += f"- **Description:** {description}\n"
        markdown_content += f"- {verification}\n\n"
        markdown_content += "---\n\n"

    try:
        # The target file is inside the submission directory.
        output_path = 'EAAI-Model-AI-Submission/project_ideas.md'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully generated {output_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == '__main__':
    main()
