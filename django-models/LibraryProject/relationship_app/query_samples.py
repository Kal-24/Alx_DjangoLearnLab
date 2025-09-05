import os
import django

# Setup Django environment (ensure this path matches your project)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'")

# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books:
            print(f" - {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Uses related_name='librarian'
        print(f"\nLibrarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library.name}")

# Run sample queries
if __name__ == '__main__':
    books_by_author("George Orwell")
    books_in_library("Downtown Library")
    librarian_for_library("Downtown Library")
