# Generated by Django 4.1.4 on 2023-08-05 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.publisher'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='writer',
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.ManyToManyField(blank=True, to='api.writer'),
        ),
    ]