from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    date = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline