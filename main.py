import os

file_dir='./'
#os.system("python pdf2txt.py -o ")
def pdf2Txt(pdf_file_dir,txt_file_dir):
    for root,dir,files in os.walk(pdf_file_dir):
        for pdf_file_name in files:
            term = "python pdf2txt.py -o " + txt_file_dir + '/'
            txt_file_name = pdf_file_name[:-3] + 'txt '
            term = term + txt_file_name + ' ' + pdf_file_dir + '/'
            term = term + pdf_file_name
            #print(term)
            os.system(term)

if __name__=='__main__':
    pdf_file_dir = file_dir + 'mzy'
    txt_file_dir = pdf_file_dir + 'Txt'
    if not os.path.exists(txt_file_dir):
        os.mkdir(txt_file_dir)
    pdf2Txt(pdf_file_dir,txt_file_dir)

