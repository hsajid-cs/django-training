from django.db import models
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return self.name

class Book(models.Model):  # Changed 'Books' to 'Book'
    title = models.CharField(max_length=50)  # Fixed typo from 'CahrField' to 'CharField'
    author = models.CharField(max_length=50)
    summary = models.TextField(help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)  # Changed 'Language' to direct class reference
    
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)  # Fixed typo from 'dateField' to 'DateField'
    date_of_death = models.DateField('Died', null=True, blank=True)
    books = models.ManyToManyField(Book, related_name='authors', help_text='Select a book for this author')  # Changed 'Books' to 'Book'
    
    def __str__(self):
        return self.name

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across the whole library')
    due_back = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)  # Changed 'Books' to 'Book'
    status = models.CharField(max_length=1, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], blank=True, default='m', help_text='Book availability')
    imprint = models.CharField(max_length=200)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.id} ({self.book.title})'
