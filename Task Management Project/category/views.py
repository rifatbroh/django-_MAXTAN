from django.shortcuts import render, redirect
from category.forms import CategoryForm
# Create your views here.
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('add_category')
    return render(request, 'category/add_category.html', {'form' : form})