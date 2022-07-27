from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileMerger
import os
from sys import argv


class Jpg2pdf():

    # Constructor
    def __init__(self):
        if "-i" in argv:
            self.img_path = f'{argv[argv.index("-i")+1]}/'
        else:
            self.img_path = "./imagens/"

        if "-p" in argv:
            self.img_path = f'{argv[argv.index("-p")+1]}/'
        else:
            self.pdf_path = "./pdf/"

    #propriedades
    def __str__(self):
        return "Teste"


    # metodos
    def jpf_to_pdf(self):
        for jpg in os.listdir(self.img_path):
            imagem = Image.open(f'{self.img_path}{jpg}').convert('RGB')
            imagem.save(f'{self.pdf_path}{jpg.replace("jpg", "pdf")}')
        print("Arquivos PDFs criados")

    def merge_pdf(self):
        dir = self.pdf_path
        pdf_files = [file for file in os.listdir(dir) if file.endswith("pdf")]
        merger = PdfFileMerger()

        for pdf in pdf_files:
            merger.append(PdfFileReader(
                os.path.join(dir, pdf), "rb"))
        merger.write(os.path.join(dir, "pdf_mesclado.pdf"))
        print("Arquivos PDFs mesclados")
