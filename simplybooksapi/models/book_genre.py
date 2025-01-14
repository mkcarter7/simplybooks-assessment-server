from django.db import models  # Import base class from Django stdlib
from .book import Book
from .genre import Genre

class BookGenre(models.Model):  # Must inherit from this base class
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="bookgenres")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="genrebooks")
