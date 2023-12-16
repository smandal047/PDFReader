from PyPDF2 import PdfReader


def read_pdf(path):
    # creating a pdf reader object
    reader = PdfReader(path, strict=False)

    total_pages = len(reader.pages)

    # printing number of pages in pdf file 
    print('No of pages to read ', total_pages)

    for p in range(total_pages):
        # yeilding pages from the pdf file
        yield reader.pages[p].extract_text()


if __name__ == '__main__':

    for i in read_pdf('FI/Background and Orientation – Varsity by Zerodha.pdf'):
        print(i.replace('\n', ' '))
