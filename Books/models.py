from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(null=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    publish_date = models.DateTimeField(null=True)
    isbn_code = models.CharField(max_length=15, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

