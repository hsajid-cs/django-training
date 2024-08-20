# using AI to insert dummy data into the database

from datetime import date
from myapp.models import Author, Publisher, Book, Store, Stock

# Create Authors
author1 = Author.objects.create(name="Jane Austen", date_of_birth=date(1775, 12, 16))
author2 = Author.objects.create(name="George Orwell", date_of_birth=date(1903, 6, 25))
author3 = Author.objects.create(name="J.K. Rowling", date_of_birth=date(1965, 7, 31))

# Create Publishers
publisher1 = Publisher.objects.create(name="Penguin Books", city="London")
publisher2 = Publisher.objects.create(name="HarperCollins", city="New York")

# Create Books
book1 = Book.objects.create(title="Pride and Prejudice", publication_date=date(1813, 1, 28), publisher=publisher1, isbn="9780141199078")
book2 = Book.objects.create(title="1984", publication_date=date(1949, 6, 8), publisher=publisher2, isbn="9780451524935")
book3 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", publication_date=date(1997, 6, 26), publisher=publisher1, isbn="9780747532743")

# Add Authors to Books (Many-to-Many relationship)
book1.authors.add(author1)  # Jane Austen authored Pride and Prejudice
book2.authors.add(author2)  # George Orwell authored 1984
book3.authors.add(author3)  # J.K. Rowling authored Harry Potter and the Philosopher's Stone

# Create Stores
store1 = Store.objects.create(name="Bookstore A")
store2 = Store.objects.create(name="Bookstore B")

# Create Stock instances (Many-to-Many through 'Stock')
stock1 = Stock.objects.create(store=store1, book=book1, quantity=5)
stock2 = Stock.objects.create(store=store1, book=book2, quantity=3)
stock3 = Stock.objects.create(store=store2, book=book3, quantity=10)
stock4 = Stock.objects.create(store=store2, book=book1, quantity=2)

"""
# Using shell to filter books written by Jane Austen
book_jane = Book.objects.filter(authors__name="Jane Austen")

"""

"""
# Using shell to filter books with their publishers
>>> books_with_publishers = Book.objects.select_related('publisher').all()
>>> for book in books_with_publishers:
...     print(f"Book: {book.title}, Publisher: {book.publisher.name}")
Book: Pride and Prejudice, Publisher: Penguin Books
Book: 1984, Publisher: HarperCollins
Book: Harry Potter and the Philosopher's Stone, Publisher: Penguin Books
"""


