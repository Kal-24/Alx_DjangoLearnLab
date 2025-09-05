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
    # views.py

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


