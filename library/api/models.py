from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    isbn_number = models.CharField(max_length=13)
    avtor = models.CharField(max_length=50)
    date = models.DateTimeField()

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name
