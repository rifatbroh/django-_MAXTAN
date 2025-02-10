# first_app/views.py
from django.shortcuts import render

def contact(request):
    return render(request, 'first_app/contact.html')
