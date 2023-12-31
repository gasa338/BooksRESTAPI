# Generated by Django 4.1.4 on 2023-07-23 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_genre_description_alter_review_comment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=None,
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together=None,
        ),
        migrations.RemoveField(
            model_name='rating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
