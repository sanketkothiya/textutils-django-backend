# views.py
# I have created this file - sanket
from django.http import HttpResponse
from django.shortcuts import render

# Code for video: 6
# def index(request):
#     return HttpResponse('''<h1> chose your favorite youtube channale</h1>
#
# <a href="https://www.youtube.com/watch?v=zs2Ux1jfDD0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=6 "> code with harry </a><br><br><hr>
# <a href=" "> Telusco  </a><br><br><hr>
# <a href=" ">thapa technical  </a><br><br><hr>
# <a href=" "> technical guruji </a><br><br><hr>
# <a href=" "> carry minati </a><br><br><hr>''')



# def about(request):
#     return HttpResponse("About Harry Bhai")

# def home(request):
#     return HttpResponse("home")
#
# def storedata(request):
#     x=request.GET.get('text','default')
#     print(x)
#     return HttpResponse("your data")

def index(request):
    # param={ 'name':'sanket','city':'surat'}
    return render(request,'index.html')

def about(request):
    # param={ 'name':'sanket','city':'surat'}
    return render(request,'about.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount= request.POST.get('charcount', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        # print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount== "on"):

        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1


        params = {'purpose': 'count the charater', 'analyzed_text': analyzed}
            # Analyze the text



    if(removepunc != "on" and fullcaps!="on" and  extraspaceremover!="on" and newlineremover != "on" and charcount!= "on" ):
        return HttpResponse("please enter the value and select your textutils")

    return render(request, 'analyze.html', params)



