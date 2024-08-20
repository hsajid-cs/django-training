from task.models import Genre, Language, User, Book, Author, BookInstance
import uuid

# Creating Genre instances
genre1 = Genre.objects.create(name="Science Fiction")
genre2 = Genre.objects.create(name="Romance")
genre3 = Genre.objects.create(name="Mystery")
genre4 = Genre.objects.create(name="Fantasy")
genre5 = Genre.objects.create(name="Thriller")

# Creating Language instances
language1 = Language.objects.create(name="English")
language2 = Language.objects.create(name="French")
language3 = Language.objects.create(name="Spanish")
language4 = Language.objects.create(name="German")
language5 = Language.objects.create(name="Italian")

# Creating User instances
user1 = User.objects.create(name="John Doe", email="john@example.com")
user2 = User.objects.create(name="Jane Smith", email="jane@example.com")
user3 = User.objects.create(name="Alice Brown", email="alice@example.com")
user4 = User.objects.create(name="Bob Johnson", email="bob@example.com")
user5 = User.objects.create(name="Carol Davis", email="carol@example.com")

# Creating Book instances
book1 = Book.objects.create(
    title="The Space Odyssey",
    author="Arthur Clarke",
    summary="A journey through space and time.",
    isbn="1234567890123",
    language=language1
)
book1.genre.add(genre1, genre4)

book2 = Book.objects.create(
    title="Romantic Escapade",
    author="Jane Austen",
    summary="A love story in the Victorian era.",
    isbn="9876543210987",
    language=language2
)
book2.genre.add(genre2)

book3 = Book.objects.create(
    title="The Mysterious Affair",
    author="Agatha Christie",
    summary="A detective story full of twists.",
    isbn="5678901234567",
    language=language3
)
book3.genre.add(genre3, genre5)

book4 = Book.objects.create(
    title="Fantasy World",
    author="J.R.R. Tolkien",
    summary="An epic fantasy adventure.",
    isbn="1122334455667",
    language=language4
)
book4.genre.add(genre1, genre4)

book5 = Book.objects.create(
    title="Thriller Nights",
    author="Stephen King",
    summary="A gripping thriller novel.",
    isbn="9988776655443",
    language=language5
)
book5.genre.add(genre5)

# Creating Author instances
author1 = Author.objects.create(name="Arthur Clarke")
author1.books.add(book1)

author2 = Author.objects.create(name="Jane Austen")
author2.books.add(book2)

author3 = Author.objects.create(name="Agatha Christie")
author3.books.add(book3)

author4 = Author.objects.create(name="J.R.R. Tolkien")
author4.books.add(book4)

author5 = Author.objects.create(name="Stephen King")
author5.books.add(book5)

# Creating BookInstance instances
book_instance1 = BookInstance.objects.create(
    id=uuid.uuid4(),
    book=book1,
    imprint="First Edition",
    status="a",
    borrower=user1
)

book_instance2 = BookInstance.objects.create(
    id=uuid.uuid4(),
    book=book2,
    imprint="Second Edition",
    status="o",
    borrower=user2
)

book_instance3 = BookInstance.objects.create(
    id=uuid.uuid4(),
    book=book3,
    imprint="Third Edition",
    status="r",
    borrower=user3
)

book_instance4 = BookInstance.objects.create(
    id=uuid.uuid4(),
    book=book4,
    imprint="Fourth Edition",
    status="a",
    borrower=user4
)

book_instance5 = BookInstance.objects.create(
    id=uuid.uuid4(),
    book=book5,
    imprint="Fifth Edition",
    status="o",
    borrower=user5
)

print("Data has been successfully created!")

'''
>>> first_book = Book.objects.first()
>>> print(first_book)
The Space Odyssey
'''

'''
>>> books = Book.objects.exclude(genre__name="Science Fiction")
>>> print(books)
<QuerySet [<Book: Romantic Escapade>, <Book: The Mysterious Affair>, <Book: Thriller Nights>]>
'''