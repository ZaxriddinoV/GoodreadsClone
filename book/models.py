from django.utils import timezone

from users.models import CustomUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    dascription = models.TextField()
    inbn = models.CharField(max_length=17)
    book_picter = models.ImageField(default='download.png')


    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookAutor(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    autor = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} -  {self.autor}"

class BookReview(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    comment = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(5)]

    )
    created_at = models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.stars_given} starts for {self.book.title} by {self.user.username}"


