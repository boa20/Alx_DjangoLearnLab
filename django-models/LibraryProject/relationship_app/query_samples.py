from relationship_app.models import *


books = Book.objects.all()

for book in books:
    print(book)

booksByAuthor = Book.objects.filter(author="")

librarian = Librarian.objects.filter(library="")