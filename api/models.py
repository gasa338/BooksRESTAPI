import datetime
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.safestring import mark_safe


class Image(models.Model):
    title = models.CharField(null=True, blank=False, max_length=256)
    alt = models.CharField(null=True, blank=True, max_length=328)
    src = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=32)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)
    description = RichTextField(default='', blank=True)

    def __str__(self):
        return self.name


class Writer(models.Model):
    name = models.CharField(max_length=32, null=True)
    date_of_birth = models.CharField(max_length=32, blank=True, null=True)
    date_of_death = models.CharField(max_length=32, blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    about_them = RichTextField(default="")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=32, null=True)
    about_them = RichTextField(default="")

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=32, null=True)
    genre = models.ManyToManyField(Genre, blank=True)
    writer = models.ManyToManyField(Writer, blank=True)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL)
    number_of_page = models.IntegerField(default=0)
    publish_data = models.DateField("Date", default=datetime.date.today)
    description = RichTextField(default="")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)

    def no_of_ratings(self):
        ratings = Review.objects.filter(book=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Review.objects.filter(book=self)
        for rating in ratings:
            sum += rating.rating

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = RichTextField(default='')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    approved = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('book', 'user'),)
        # index_together = (('book', 'user'),)


class Cart(models.Model):
    books = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=False, null=False, validators=[MinValueValidator(1)])
    choice_status = [("0", 'pristiglo'), ('1', 'U toku'), ('2', 'Otkazano')]
    status = models.CharField(max_length=32, choices=choice_status, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together  = (('user', 'books'),)
        # index_together = (('user', 'books'),)


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    about = RichTextField(default="")
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id', 'user'),)
        # index_together = (('user', 'books'),)

    def __str__(self):
        return 'profile %s' % self.user.username

# class Movie(models.Model):
#     title = models.CharField(max_length=32)
#     description = models.TextField(max_length=360)
#
#     def no_of_ratings(self):
#         ratings = Rating.objects.filter(movie=self)
#         return len(ratings)
#
#     def avg_rating(self):
#         sum = 0
#         ratings = Rating.objects.filter(movie=self)
#         for rating in ratings:
#             sum += rating.stars
#
#         if len(ratings) > 0:
#             return sum / len(ratings)
#         else:
#             return 0
# class Rating(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#
#     class Meta:
#         unique_together = (('user', 'movie'),)
#         index_together = (('user', 'movie'),)
