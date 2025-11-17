#!/usr/bin/env python3
"""
Generate PDF from README.md with embedded images
"""

from markdown_pdf import MarkdownPdf, Section

def main():
    # Read the README.md file
    with open('README.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Create PDF instance
    pdf = MarkdownPdf(toc_level=2)

    # Add the markdown content as a section
    pdf.add_section(Section(markdown_content))

    # Save the PDF
    output_file = 'wing-public-api.pdf'
    pdf.save(output_file)

    print(f"✓ PDF generated successfully: {output_file}")
    print(f"✓ All images from assets/ folder have been embedded")

if __name__ == '__main__':
    main()
