from django.shortcuts import render, get_object_or_404
from book.models import Book, Category
from author.models import Author
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(user, amount, subject, template):
    message = render_to_string(template,{
        'user' : user,
        'amount' : amount
    })

    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()



def home_view(request, slug = None):
    books = Book.objects.all()
    categories = Category.objects.all()

    authors = Author.objects.order_by('-popularity')
    top_10_authors = authors[:10]
    x = 1
    for author in authors:
        author.rank = x
        author.save()
        x += 1

    curr_category = None

    top_selling = Book.objects.order_by('-borrow_count')[:10]

    if slug is not None:
        category = get_object_or_404(Category, slug=slug)
        curr_category = category.name
        books = Book.objects.filter(categories=category)
        return render(request, 'core/index.html', {'books' : books, 'categories' : categories, 'curr_category' : curr_category, 'book_title' : 'Showing Results for ', 'top_selling' : top_selling, 'top_authors' : top_10_authors})
    
    return render(request, 'core/index.html', {'books' : books, 'categories' : categories, 'curr_category' : curr_category, 'book_title' : 'Newly Added Books', 'top_selling' : top_selling, 'top_authors' : top_10_authors})
