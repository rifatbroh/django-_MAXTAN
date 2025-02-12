from django.shortcuts import render

# amra ekhane theke user request pathabo
def home(request):
    return render(request, 'home.html')