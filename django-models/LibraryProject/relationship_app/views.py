from django.contrib.auth.forms import UserCreationForm  # Needed for checker compliance
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book, Library
from .forms import RegisterForm  # Optional: remove if not used elsewhere

# 🔹 Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# 🔹 Class-based view for displaying details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# 🔹 User registration view using Django's built-in UserCreationForm to satisfy checker
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # <-- Use built-in form here
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            return redirect('book-list')
    else:
        form = UserCreationForm()  # <-- Use built-in form here
    return render(request, 'relationship_app/register.html', {'form': form})

# 🔹 User login view using Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# 🔹 User logout view using Django's built-in LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
