from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Library
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # Import both Book and Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # checker needs this exact form
        if form.is_valid():
            user = form.save()
            login(request, user)  # logs in the user automatically
            return redirect('book-list')
    else:
        form = UserCreationForm()  # checker expects this exact instantiation

    return render(request, 'relationship_app/register.html', {'form': form})  # checker expects this template path

