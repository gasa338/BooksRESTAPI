# Generated by Django 4.1.4 on 2023-07-22 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_book_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.writer'),
        ),
    ]
