# Generated by Django 4.1.4 on 2023-08-24 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_alter_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.image'),
        ),
    ]