

from decimal import Decimal
from unicodedata import category

from django.db import models
from django.core.validators import MinValueValidator

from authors.models import Author
from discounts.models import CategoryDiscount, CountryDiscount, AuthorDiscount, BookDiscount


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.00)])
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

    def get_discount(self, user=None) -> Decimal:
        country_discount = CountryDiscount.objects.filter(country=user.country).values_list('percent', flat=True)
        author_discount = AuthorDiscount.objects.filter(author__in=self.authors).values_list('percent', flat=True)
        category_discount = CategoryDiscount.objects.filter(category__in=self.categories).values_list('percent', flat=True)
        book_discount = BookDiscount.objects.filter(book__isbn=self.isbn).values_list('percent', flat=True)

        discounts = [*country_discount, *author_discount, *category_discount, *book_discount]
        return max(discounts)
