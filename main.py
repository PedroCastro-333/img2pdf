import jpg2pdf
from sys import argv

convert = jpg2pdf.Jpg2pdf()


def main():
    convert.jpf_to_pdf()

    if "-m" in argv:
        convert.merge_pdf()

if __name__ == "__main__":
    main()
