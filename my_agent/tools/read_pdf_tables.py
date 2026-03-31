import pdfplumber


def read_pdf_tables(file_path: str) -> str:
    """Extract tables from a PDF file as CSV-formatted text.

    Use this tool instead of read_pdf when the PDF contains tabular data
    (e.g. lists, inventories, spreadsheets). Returns each table as CSV so
    values can be counted or compared precisely.

    When filtering rows, consider ALL relevant status values. For example,
    "not on shelves" includes both "Checked Out" AND "Overdue" rows — not
    just one of them. Count every matching row across all pages.

    Args:
        file_path: The absolute or relative path to the PDF file.

    Returns:
        All tables found in the PDF, labelled by page and table index.
        Returns an error message if the file cannot be opened or read.
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            results = []
            headers = None
            for i, page in enumerate(pdf.pages, start=1):
                for j, table in enumerate(page.extract_tables(), start=1):
                    rows = []
                    for row in table:
                        cells = [cell or "" for cell in row]
                        # Use the first non-empty row as headers; carry them across pages
                        if headers is None and any(cells):
                            headers = cells
                            rows.append("Columns: " + " | ".join(headers))
                            continue
                        # Skip rows that look like section headers (only one non-empty cell)
                        if sum(bool(c) for c in cells) <= 1:
                            rows.append(" | ".join(cells))
                            continue
                        if headers:
                            rows.append(" | ".join(f"{h}: {v}" for h, v in zip(headers, cells)))
                        else:
                            rows.append(" | ".join(cells))
                    results.append(f"--- Page {i}, Table {j} ---\n" + "\n".join(rows))
    except Exception as e:
        return f"Error: could not open '{file_path}': {e}"

    if not results:
        return "No tables found in the PDF."

    return "\n\n".join(results)
