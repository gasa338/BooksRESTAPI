# Generated by Django 4.2.3 on 2023-09-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_review_appruved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='appruved',
            new_name='approved',
        ),
    ]