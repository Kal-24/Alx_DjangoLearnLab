from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        if title and author:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('book_list')  # Make sure you have a URL named 'book_list'
        else:
            return render(request, 'bookshelf/create_book.html', {'error': 'Title and Author are required.'})
    return render(request, 'bookshelf/create_book.html')


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect after deletion
    return render(request, 'bookshelf/delete_book.html', {'book': book})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books}) from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        query = form.cleaned_data['query']
        # ORM automatically escapes inputs, preventing SQL injection
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})

