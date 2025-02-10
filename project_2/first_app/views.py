from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def CSE(request):
    return HttpResponse("This is CSE dept!")

def EEE(request):
    return HttpResponse("This is EEE dept!")

def Cvil(request):
    return HttpResponse("This is Civil dept!")

def ENG(request):
    return HttpResponse("This is ENG dept!")

def BBA(request):
    return HttpResponse("This is BBA dept!")
