# Retrieve Operation

```python
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)
# Output:
# 1984 George Orwell 1949

---

### To create and edit the file quickly (Linux/macOS terminal):

```bash
cd LibraryProject/bookshelf
touch retrieve.md
