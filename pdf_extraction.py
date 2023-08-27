import PyPDF2
a = PyPDF2.PdfFileReader('boiler_list.pdf')
print(a.documentInfo)