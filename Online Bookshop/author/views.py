from django.shortcuts import render
from django.views.generic import ListView, DetailView
from author.models import Author
from book.models import Book


class AuthorProfileView(DetailView):
    model = Author
    template_name = 'author/author_profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['pk'])
        context['books'] = Book.objects.filter(author=author)
        context['author'] = author
        return context
    

