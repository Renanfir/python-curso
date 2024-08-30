import os
from PyPDF2 import PdfMerger


pdf_dir = "C:\\Users\\Usuario\\Documents\\NovaPasta"

# Lista todos os arquivos PDF no diretório
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# Ordena os arquivos para garantir que as duplas fiquem na ordem certa
pdf_files.sort()


for i in range(0, len(pdf_files), 2):
    merger = PdfMerger()

    pdf1 = os.path.join(pdf_dir, pdf_files[i])
    pdf2 = os.path.join(pdf_dir, pdf_files[i + 1])
    
    
    merger.append(pdf1)
    merger.append(pdf2)
    
    common_name = os.path.splitext(pdf_files[i])[0]  # Nome do primeiro arquivo sem extensão
    
    # Salva o arquivo combinado com o nome da primeira parte do par
    output_filename = f"{common_name} - IRPF.pdf"
    merger.write(os.path.join(pdf_dir, output_filename))
    merger.close()

print("PDFs combinados com sucesso!")
