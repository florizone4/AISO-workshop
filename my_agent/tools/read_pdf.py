import pdfplumber


def read_pdf(file_path: str) -> str:
    """Extract text content from a PDF file.

    Use this tool whenever a question references a PDF file and you need to
    read its contents. For PDFs that contain tables, prefer read_pdf_tables.

    Args:
        file_path: The absolute or relative path to the PDF file.

    Returns:
        The full text content of the PDF, with pages separated by a divider.
        Returns an error message if the file cannot be opened or read.
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            pages = []
            for i, page in enumerate(pdf.pages, start=1):
                text = page.extract_text() or ""
                pages.append(f"--- Page {i} ---\n{text}")
    except Exception as e:
        return f"Error: could not open '{file_path}': {e}"

    if not pages:
        return "The PDF contains no extractable text."

    return "\n\n".join(pages)
