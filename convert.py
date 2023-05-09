from docx2pdf import convert

def docx_to_pdf(input_file, output_file):
    convert(input_file, output_file)