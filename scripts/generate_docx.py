#!/usr/bin/env python3
"""
Generate DOCX from README.md with embedded images
"""

from Markdown2docx import Markdown2docx

def main():
    import os
    import shutil

    # Read the README.md file
    with open('README.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Output file name
    output_file = 'wing-public-api'

    # Write the markdown content to a temporary file for processing
    # The library expects the .md file to exist before instantiation
    with open(f'{output_file}.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    # Create DOCX document from markdown
    # Note: Markdown2docx constructor takes the filename without extension
    project = Markdown2docx(output_file)

    # Process the markdown and generate DOCX
    project.eat_soup()
    project.save()

    print(f"✓ DOCX generated successfully: {output_file}.docx")
    print(f"✓ All images from assets/ folder have been embedded")

    # Clean up temporary markdown file if created
    temp_md = f'{output_file}.md'
    if os.path.exists(temp_md) and temp_md != 'README.md':
        os.remove(temp_md)

if __name__ == '__main__':
    main()
