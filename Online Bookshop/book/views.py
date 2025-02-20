from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import FormView, View
from book.models import Book
from review.forms import ReviewForm
from review.models import Review
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
from transactions.models import Transaction


class BookDetailsView(LoginRequiredMixin, FormView):
    template_name = "book/book_details.html"
    form_class = ReviewForm

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        book_categories = book.categories.all()

        related_books = Book.objects.filter(categories=book_categories[0]).exclude(id=book.id).order_by('-borrow_count')[:3]
        form = ReviewForm()
        return render(request, self.template_name, {'book': book, 'form': form, 'related_books' : related_books})

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        book_categories = book.categories.all()
        related_books = Book.objects.filter(categories=book_categories[0]).exclude(id=book.id).order_by('-borrow_count')[:3]

        borrowed_books = request.user.account.borrowed_books.all()
        if book not in borrowed_books:
            messages.error(request, "You can only review books you have borrowed")
            return render(request, self.template_name, {'book': book, 'form': form, 'related_books' : related_books})

        if form.is_valid():
            all_reviews = book.reviews.all()
            if all_reviews.filter(user=request.user).exists():
                messages.error(request, "You have already reviewed this book")
                return render(request, self.template_name, {'book': book, 'form': form, 'related_books' : related_books})

            review = Review.objects.create(
                ratings=form.cleaned_data['ratings'],
                description=form.cleaned_data['description'],
                book=book,
                user=request.user
            )
            book.reviews.add(review)
            messages.success(request, "You have successfully reviewed this book")
        return render(request, self.template_name, {'book': book, 'form': form, 'related_books' : related_books})



    def get_success_url(self):
        return reverse("book_details", kwargs={"pk": self.kwargs["pk"]})


class BorrowBookWithMoney(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])

        if request.user.account.balance < book.price:
            messages.error(request, "You do not have enough money to borrow this book")
            return redirect("book_details", pk=book.id)

        if book.quantity <= 0:
            messages.error(request, "This book is out of stock")
            return redirect("book_details", pk=book.id)
        
        if request.user.account.borrowed_books.filter(id=book.id).exists():
            messages.error(request, "You have already borrowed this book")
            return redirect("book_details", pk=book.id)

        request.user.account.balance -= book.price
        request.user.account.borrowed_books.add(book)
        request.user.account.coins +=  (book.price * Decimal('0.25'))
        book.quantity -= 1
        book.borrow_count += 1
        book.author.total_borrowed += 1
        book.author.popularity += 700

        book.save()
        book.author.save()
        request.user.account.save()
        Transaction.objects.create(
            user=request.user,
            amount=book.price,
            trax_type='Cash',
            action='Borrowed',
            balance_after_transaction=request.user.account.balance
        )
        Transaction.objects.create(
            user=request.user,
            amount=book.price * Decimal('0.25'),
            trax_type='Coin',
            action='Reward',
            balance_after_transaction=request.user.account.coins
        )

        messages.success(request, f"You have successfully borrowed '{book.title}' and received some delicious coins!")
        return redirect("book_details", pk=book.id)


class BorrowBookWithCoins(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])

        if book.quantity <= 0:
            messages.error(request, "This book is out of stock")
            return redirect("book_details", pk=book.id)
        
        if request.user.account.borrowed_books.filter(id=book.id).exists():
            messages.error(request, "You have already borrowed this book")
            return redirect("book_details", pk=book.id)

        if request.user.account.coins < book.price_with_coin:
            messages.error(request, "You do not have enough coins to borrow this book")
            return redirect("book_details", pk=book.id)

        request.user.account.coins -= book.price_with_coin
        request.user.account.borrowed_books.add(book)
        book.quantity -= 1
        book.borrow_count += 1
        book.author.total_borrowed += 1
        book.author.popularity += 700

        book.save()
        book.author.save()
        request.user.account.save()
        Transaction.objects.create(
            user=request.user,
            amount=book.price_with_coin,
            trax_type='Coin',
            action='Borrowed',
            balance_after_transaction=request.user.account.coins
        )

        messages.success(request, f"You have successfully borrowed '{book.title}'!")
        return redirect("book_details", pk=book.id)


class ReturnBook(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        if book not in request.user.account.borrowed_books.all():
            messages.error(request, "You have not borrowed this book")
            return redirect("book_details", pk=book.id)
        
        request.user.account.borrowed_books.remove(book)
        request.user.account.coins +=  (book.price * Decimal('0.25'))
        request.user.account.balance += (book.price / Decimal(2))
        book.quantity += 1

        book.save()
        request.user.account.save()
        Transaction.objects.create(
            user=request.user,
            amount=(book.price / Decimal(2)),
            trax_type='Cash',
            action='Returned',
            balance_after_transaction=request.user.account.balance
        )
        Transaction.objects.create(
            user=request.user,
            amount=(book.price * Decimal(0.25)),
            trax_type='Coin',
            action='Returned',
            balance_after_transaction=request.user.account.coins
        )
        
        messages.success(request, f"You have successfully returned '{book.title}' and received 50% of the book's price and 25% of the book's price in coins!")
        return redirect("accounts:profile")
