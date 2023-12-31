# Generated by Django 4.1.4 on 2023-08-15 20:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0032_remove_cart_books_cart_books'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'books')},
        ),
        migrations.AlterIndexTogether(
            name='cart',
            index_together={('user', 'books')},
        ),
    ]
