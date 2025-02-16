import PyPDF2
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def read_pdf(file_path):
    """Reads text from a PDF file."""
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def read_csv(file_path):
    """Reads data from a CSV file."""
    return pd.read_csv(file_path)

def create_pdf(output_path, base_text, csv_data):
    """Generates a new PDF with data from CSV appended to base text."""
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Add the base text to the PDF
    c.drawString(50, height - 50, "Base PDF Text:")
    c.drawString(50, height - 70, base_text[:200] + "...")  # Display truncated base text

    # Add data from the CSV
    c.drawString(50, height - 120, "Data from CSV:")
    y_position = height - 140
    for index, row in csv_data.iterrows():
        row_data = ", ".join(map(str, row.values))
        c.drawString(50, y_position, row_data)
        y_position -= 20
        if y_position < 50:  # Start a new page if space runs out
            c.showPage()
            y_position = height - 50

    c.save()

def main():
    # Paths for input/output
    input_pdf = "input.pdf"
    input_csv = "data.csv"
    output_pdf = "output.pdf"

    # Process files
    base_text = read_pdf(input_pdf)
    csv_data = read_csv(input_csv)
    create_pdf(output_pdf, base_text, csv_data)
    print(f"New PDF generated: {output_pdf}")

if __name__ == "__main__":
    main()
