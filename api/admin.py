import os

from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(Genre)
class GenderAdmin(admin.ModelAdmin):
    def image_genre(self, obj):
        return format_html(
            '<a href="{}" target="_blank"><img src="{}" width="auto" height="200px" /></a>'.format(obj.image.src.url,
                                                                                                   obj.image.src.url))

    image_genre.short_description = 'Image'
    image_genre.allow_tags = True

    readonly_fields = ['image_genre']
    fields = ['name', ('image', 'image_genre'), 'description']

    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name', 'description']


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'date_of_death']
    list_display_links = ['name', 'date_of_birth', 'date_of_death']
    list_filter = ['name', 'date_of_birth', 'date_of_death']
    search_fields = ['name', 'about_them']
    fields = ['name', ('date_of_birth', 'date_of_death'), 'genre', 'about_them']
    filter_horizontal = ['genre']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def image_book(self, obj):
        return format_html(
            '<a href="{}" target="_blank"><img src="{}" width="auto" height="200px" /></a>'.format(obj.image.src.url,
                                                                                                   obj.image.src.url))

    image_book.short_description = 'Image'
    image_book.allow_tags = True

    readonly_fields = ['image_book']
    fields = ['name', 'genre', 'writer', 'publisher', 'number_of_page', 'publish_data',
              'description', 'price', 'quantity', ('image', 'image_book')]
    list_display = ['name', 'number_of_page', 'price', 'quantity']
    list_display_links = ['name', 'number_of_page', 'price', 'quantity']
    list_filter = ['genre', 'writer']
    search_fields = ['name', 'description']
    filter_horizontal = ['genre', 'writer']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # fields = ['book', 'user', 'comment', 'rating', 'approved', 'create_at' ]
    readonly_fields = ['create_at']
    list_display = ['user', 'book', 'rating']
    list_display_links = ['user', 'book', 'rating']
    list_filter = ['user', 'book', 'rating']
    search_fields = ['book', 'description']


@admin.register(Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ['user', 'datetime', 'quantity']
    list_display_links = ['user', 'datetime', 'quantity']
    list_filter = ['books', ]
    search_fields = ['datetime']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'quantity', 'created_at', 'updated_at']
    list_display_links = ['user', 'status', 'quantity']
    list_filter = ['user', 'status']
    search_fields = ['status']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['about_them']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def image_profile(self, obj):
        return format_html(
            '<a href="{}" target="_blank"><img src="{}" width="auto" height="200px" /></a>'.format(obj.image.src.url,
                                                                                                   obj.image.src.url))

    image_profile.short_description = 'Image'
    image_profile.allow_tags = True

    readonly_fields = ['image_profile']
    fields = ['user', 'genre', ('image', 'image_profile'), 'about']
    list_display = ['user']
    list_display_links = ['user']
    list_filter = ['genre']
    search_fields = ['user']
    filter_horizontal = ['genre']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            '<a href="{}" target="_blank"><img src="{}" width="auto" height="200px" /></a>'.format(obj.src.url,
                                                                                                   obj.src.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    readonly_fields = ['image_tag']
    fields = ['title', 'alt', ('src', 'image_tag')]
    list_display = ['title', 'alt']
    list_filter = ['title', 'alt']
    search_fields = ['title']
