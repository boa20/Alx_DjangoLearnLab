from relationship_app.models import *

Library.objects.get(name='')
books = Library.books.all()

for book in books:
    print(book)

booksByAuthor = Book.objects.filter(author="")

librarian = Librarian.objects.filter(library="")