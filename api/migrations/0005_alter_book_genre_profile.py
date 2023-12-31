# Generated by Django 4.1.4 on 2023-07-22 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_rename_domen_genre_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('1', 'Fantastika'), ('2', 'Gotički roman'), ('3', 'Horor'), ('4', 'Pustolovni roman'), ('5', 'Romantizam'), ('6', 'Saga'), ('7', 'Vestern'), ('8', 'Žanr kriminalistike')], max_length=32, null=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ManyToManyField(to='api.genre')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
