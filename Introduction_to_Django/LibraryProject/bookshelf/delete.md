# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
# Output:
# <QuerySet []>

---

### How to create it quickly:

```bash
cd LibraryProject/bookshelf
touch delete.md
