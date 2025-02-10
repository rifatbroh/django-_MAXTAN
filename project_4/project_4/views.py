from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    d = {'author' : 'Rifat', 'age' : 21, 'courses' : [
        {
            id : 1,
            'name' : 'Rifat',
            'salary' : 10000,
        },
        {
            id : 2,
            'name' : 'Sadia',
            'salary' : 20000,
        },
        {
            id : 3,
            'name' : 'Prome',
            'salary' : 30000,
        },
        {
            id : 4,
            'name' : 'Razil',
            'salary' : 40000,
        },
        {
            id : 5,
            'name' : 'Moneem',
            'salary' : 50000,
        },
    ]}
    return render(request, 'index.html', d)

def hello(request):
    return render(request, 'index2.html', )