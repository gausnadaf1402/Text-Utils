#i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')
    # file=open('C://Users//acer//Desktop//demo1.txt')
    # # return HttpResponse(file.read())

# def about(request):
#     return HttpResponse('''<h1>about gaus bhai</h1> <br><a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django code with harry tutorial playlist</a>''')

# def contact(request):
#     return HttpResponse(9067096226)

# def home(request):
#     return HttpResponse('home gaus bhai')

def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')

    #check checkbox values
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    halfcaps=request.GET.get('halfcaps','off')
    NewLineRemover=request.GET.get('NewLineRemover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charactercounter=request.GET.get('charactercounter','off')

    #check which checkbox is on
    if(removepunc=='on'):
        # analyzed=djtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuation','Analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params) 
    if(fullcaps=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'change to uppercase','Analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if(halfcaps=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.lower()
        params={'purpose':'change to lowercase','Analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if(NewLineRemover=='on'):
        analyzed=''
        for char in djtext:
            if char !='\n':
                analyzed=analyzed+char
        params={'purpose':'New Line Remover','Analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if(extraspaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose':'New Line Remover','Analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if(charactercounter=='on'):
        analyzed=len(djtext)
        params={'purpose':'count number of characters','Analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    else:
        return HttpResponse('Error')
    return render(request,'analyze.html',params)

def about(request):
    return render(request,'about.html')

def navigation(request):
    s="<h2>Navigation Bar</h2> <a href='https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>Django with harry bhai</a><br> <a href='https://www.facebook.com'>Facebook</a><br> <a href='https://www.flipKart.com'>Flipkart</a><br> <a href='https://www.hindustantimes.com'>news</a><br> "
    return HttpResponse(s)
    
    
# def capfirst(request):
#     return HttpResponse('capitalize first')

# def newlineremove(request):
#     # print(request.GET.get('text','default'))
#     return HttpResponse("<button>new line remove</button>")

# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse('character count')

# def services(request):
#     d={'name':'gaus','lname':'nadaf'}
#     return render(request,'index1.html',d)