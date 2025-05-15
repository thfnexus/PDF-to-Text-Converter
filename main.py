"""
📄 Project 7: PDF to Text Converter
👨‍💻 Created by: Hashir Adnan  
🌐 Website: www.techthf.xyz  
🗓️ Date: [Insert today's date]

🧠 Description:
This Python script extracts all text content from a PDF file and prints it in plain text format.
It’s useful for reading or processing PDF documents programmatically, such as resumes, reports, or invoices.

📦 Features:
- Loads any standard (non-scanned) PDF file
- Extracts text from all pages
- Handles PDF reading errors gracefully
- Displays the extracted text in terminal or console

🧰 Tools & Modules Used:
- pdfplumber: for extracting text from PDF pages
- Exception handling: to detect and handle corrupted or invalid PDF files

💡 How to Use:
1. Place a valid PDF file (e.g., `sample.pdf`) in your project folder.
2. Set the `pdf_path` variable to that file’s path.
3. Run the script with: `python main.py`
4. The text will be printed to the console.

✅ Example:
Input File: sample.pdf  
Output: Full text content from each page printed to screen.

🔒 Note:
This does NOT work on scanned PDFs (images of text). It only works on PDFs that contain real, digital text.
"""

import pdfplumber

def pdf_to_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text
pdf_path = r'C:\Users\ads\Desktop\py\proj 7\amhashir1617Resume (1).pdf'

text = pdf_to_text(pdf_path)
print(text)
