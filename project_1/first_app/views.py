from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is courses page")

def rifatbroh(request):
    return HttpResponse("Hello jonogon, this is rifatbroh")

def home(request):
    return HttpResponse("this is first app home page")

def test(request):
    return HttpResponse("I love sadia")