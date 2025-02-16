# PDF & CSV Merger  

## Overview  
This Python script extracts text from a PDF file, reads data from a CSV file, and generates a new PDF that combines the extracted text with tabular data.  

## Features  
- Extracts text from a PDF file.  
- Reads structured data from a CSV file.  
- Generates a new PDF with extracted text and CSV data using `reportlab`.  
- Handles multi-page output if data exceeds one page.  

## Prerequisites  
Before running the script, ensure you have the following installed:  
- Python 3.7 or later  
- pip (Python package manager)  

## Installation  

1. Clone the repository:  
```bash  
git clone https://github.com/Sachinbisht27/pdf_csv_merger.git  
cd pdf_csv_merger  
```

2. Install required dependencies:  
```bash  
pip install -r requirements.txt  
```

## Dependencies  
Ensure you have the following Python libraries installed:  

```bash  
pip install PyPDF2 pandas reportlab  
```

## Usage  

1. Place your input files in the same directory:  
   - `input.pdf` (PDF file to extract text from)  
   - `data.csv` (CSV file containing structured data)  

2. Run the script:  

```bash  
python script.py  
```

3. The generated output will be saved as `output.pdf` in the same directory.  

## File Structure  

```
pdf_csv_merger/  
│── input.pdf     # Source PDF file  
│── data.csv      # CSV file with data  
│── output.pdf    # Generated PDF file  
│── script.py     # Main Python script  
│── requirements.txt # Required dependencies  
│── README.md     # Project documentation  
```

## Example Output  
The generated PDF (`output.pdf`) will contain:  
- Extracted text from `input.pdf` (truncated if too long).  
- CSV data formatted as plain text.  

## License  
This project is licensed under the MIT License.  
