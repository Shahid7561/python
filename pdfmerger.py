import PyPDF2

def merge_pdfs(input_pdf1, input_pdf2, output_pdf):
    # Open the first PDF file in read-binary mode
    with open(input_pdf1, 'rb') as pdf1_file:
        # Create a PDF object
        pdf1 = PyPDF2.PdfReader(pdf1_file)

        # Open the second PDF file in read-binary mode
        with open(input_pdf2, 'rb') as pdf2_file:
            # Create a PDF object
            pdf2 = PyPDF2.PdfReader(pdf2_file)

            # Create a new PDF writer
            pdf_writer = PyPDF2.PdfWriter()

            # Add all pages from the first PDF
            for page_num in range(len(pdf1.pages)):
                page = pdf1.pages[page_num]
                pdf_writer.add_page(page)

            # Add all pages from the second PDF
            for page_num in range(len(pdf2.pages)):
                page = pdf2.pages[page_num]
                pdf_writer.add_page(page)

            # Write the merged PDF to the output file
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

    print(f"Merged {input_pdf1} and {input_pdf2} into {output_pdf}")

if __name__ == "__main__":
    input_pdf1 = "input1.pdf"
    input_pdf2 = "input2.pdf"
    output_pdf = "output.pdf"
    
    merge_pdfs(input_pdf1, input_pdf2, output_pdf)
