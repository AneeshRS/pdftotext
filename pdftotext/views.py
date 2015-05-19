from django.shortcuts import render
from utilities import pdf_to_text, tokenize, histogram, get_count
from pdftotext.models import PdfText
import os

# global variable for setting case sensitivity
IS_CASE_SENSITIVE = False

def home(request):
    data = {'title': "pdf converter"}
    if request.method == 'GET':
        return render(request, 'pdftotext/home.html', data)
    elif request.method == 'POST':
        data['pdf-to-text'] = ""
        data['is_converted'] = False
        if request.FILES["pdf-file"]:
            pdf = request.FILES["pdf-file"]
            keywords = request.POST.get("key-words")
            pdfText = PdfText(pdf=pdf)
            pdfText.save()
            pdfPath = pdfText.pdf.path
            text = pdf_to_text(pdfPath)
            data['pdf_to_text'] = text
            data['is_converted'] = True

            global IS_CASE_SENSITIVE
            if not IS_CASE_SENSITIVE :
                text = text.lower()
                keywords = keywords.lower()
            
            histogramDict = histogram(tokenize(text))
            keywords = tokenize(keywords)
            keywordCount = dict()
            for keyword in keywords:
                count = get_count(keyword, histogramDict)
                keywordCount[keyword] = count
            data['keywords'] = keywordCount



            # # start
            print "------------------------------------"
            # hist = histogram(tokenize(histogram))
            # for key, value in histogramDict.items():
            #   print str(key) + ":" + str(value)
            # # end

        return render(request, 'pdftotext/home.html', data)