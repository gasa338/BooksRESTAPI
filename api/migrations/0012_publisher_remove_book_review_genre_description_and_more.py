# Generated by Django 4.1.4 on 2023-07-22 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_book_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('about_them', models.TextField(blank=True, max_length=360, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, max_length=360, null=True),
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField()),
                ('about_them', models.TextField(blank=True, max_length=360, null=True)),
                ('genre', models.ManyToManyField(to='api.genre')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='api.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='writer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.writer'),
        ),
    ]