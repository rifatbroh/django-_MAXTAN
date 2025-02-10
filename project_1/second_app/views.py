from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def front(request):
    return HttpResponse("This is our second app Home page")

def about(requst):
    return HttpResponse("This is out second app about page")

def testomonial(request):
    return HttpResponse("This is our second app Testomonial page")

def contact(requst):
    return HttpResponse("This is out second app contact page")