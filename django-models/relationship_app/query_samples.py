from relationship_app.models import Library, Librarian, Author, Book


library_name = Library.objects.create(name="Novels")
library.save()

librarian = Librarian.objects.create(name="Baning Adjei", library="Novels")
librarian.save()

author1 = Author.objects.create(name="George S. Clason")
author1.save()
author2 = Author.objects.create(name="Louisa May Alcott")
author2.save()
author3 = Author.objects.create(name="Charles Duhigg")
author3.save()

book1 = Book.objects.create(title="The Richest Man in Babylon", author= "George S. Clason")
book1.save()
book2 = Book.objects.create(title="Little Women", author= "Louisa May Alcott")
book2.save()
book3 = Book.objects.create(title="The Power of Habit", author= "Charles Duhigg")
book3.save()

Library.objects.get(name="Novels")
books = Library.books.all()

for book in books:
    print(book)

booksByAuthor = Book.objects.filter(author="Charles Duhigg")

librarian = Librarian.objects.filter(library=library_name)