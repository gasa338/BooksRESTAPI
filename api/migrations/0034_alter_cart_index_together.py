# Generated by Django 4.1.4 on 2023-08-15 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_alter_cart_unique_together_alter_cart_index_together'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='cart',
            index_together=set(),
        ),
    ]