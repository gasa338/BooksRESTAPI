# Generated by Django 4.1.4 on 2023-07-22 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='datum',
            new_name='date_now',
        ),
    ]
