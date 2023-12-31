# Generated by Django 4.2.3 on 2023-07-22 18:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_book_quantity_cart_quantity_reservation_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=ckeditor.fields.RichTextField(default=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='about_them',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='writer',
            name='about_them',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
