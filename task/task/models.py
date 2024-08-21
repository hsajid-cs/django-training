from django.db import models
import uuid

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True) 
    
    def __str__(self):
        return self.name

class Publisher (models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(null=True, blank=True) 
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    isbn = models.CharField('ISBN', max_length=13)
    
    def __str__(self):
        return self.title

class Store(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, through ='Stock')
    
    def __str__(self):
        return self.name

class Stock(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    stock = models.IntegerField()
    
    def __str__(self):
        return f'{self.store.name} has {self.quantity} copies of {self.book.title}'
