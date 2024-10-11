import PyPDF2

def pdf_text_extractor(file_path):
    """
    Extract all text from the provided PDF file.
    
    :param file_path: Path to the PDF file
    :return: Extracted text from the PDF
    """
    try:
        text = ""
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() + "\n\n"
        return text
    except Exception as e:
        print(e)
        return ""