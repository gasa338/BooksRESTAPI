# Generated by Django 4.2.3 on 2023-09-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_genre_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='appruved',
            field=models.BooleanField(default=False),
        ),
    ]
