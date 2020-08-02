import pyttsx3
import PyPDF2

book = open("book.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speak = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speak.say(text)
    speak.runAndWait()
