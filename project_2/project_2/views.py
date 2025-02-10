from django.http import HttpResponse

def home(reqest):
    return HttpResponse("This is Home page")

def about(reqest):
    return HttpResponse("This is about page")

def contact(reqest):
    return HttpResponse("This is contact page")

def test(reqest):
    return HttpResponse("This is test page")

def map(reqest):
    return HttpResponse("This is map page")