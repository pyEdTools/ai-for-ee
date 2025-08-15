import os
import markdown

def create_html_from_markdown(md_path, html_path):
    """Reads a markdown file, converts it to HTML, and wraps it in a styled HTML document."""

    # Simple CSS for readability
    css_style = """
    <style>
        body { font-family: sans-serif; line-height: 1.6; margin: 2em; max-width: 800px; margin-left: auto; margin-right: auto; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 1em; }
        th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; vertical-align: top; }
        th { background-color: #f2f2f2; }
        code { background-color: #eee; padding: 2px 4px; border-radius: 3px; font-family: monospace; }
        pre { background-color: #eee; padding: 1em; border-radius: 3px; overflow-x: auto; }
        h1, h2, h3 { border-bottom: 1px solid #ccc; padding-bottom: 0.3em; }
    </style>
    """

    try:
        with open(md_path, 'r', encoding='utf-8') as f_md:
            md_content = f_md.read()
    except IOError as e:
        print(f"Error reading {md_path}: {e}")
        return False

    # Convert markdown to HTML
    html_body = markdown.markdown(md_content, extensions=['tables'])

    # Get the title from the first line of markdown if it's a h1
    title = "Assignment Document"
    first_line = md_content.strip().split('\n')[0]
    if first_line.startswith('# '):
        title = first_line[2:]

    # Wrap in a full HTML document
    full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {css_style}
</head>
<body>
    {html_body}
</body>
</html>
"""

    try:
        with open(html_path, 'w', encoding='utf-8') as f_html:
            f_html.write(full_html)
        print(f"Successfully converted {md_path} to {html_path}")
        return True
    except IOError as e:
        print(f"Error writing {html_path}: {e}")
        return False


def main():
    """Main function to walk through the directory and convert all .md files."""
    submission_dir = 'EAAI-Model-AI-Submission'
    if not os.path.isdir(submission_dir):
        print(f"Error: Directory '{submission_dir}' not found.")
        return

    converted_files = 0
    for root, _, files in os.walk(submission_dir):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(root, file)
                html_file_path = md_file_path[:-3] + ".html"

                if create_html_from_markdown(md_file_path, html_file_path):
                    # If conversion is successful, remove the original markdown file
                    try:
                        os.remove(md_file_path)
                        print(f"Removed original markdown file: {md_file_path}")
                        converted_files += 1
                    except OSError as e:
                        print(f"Error removing {md_file_path}: {e}")

    print(f"\nConversion complete. Converted {converted_files} files to HTML.")


if __name__ == '__main__':
    main()
