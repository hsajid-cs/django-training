# Generated by Django 5.0.8 on 2024-08-20 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='stock',
            new_name='quantity',
        ),
    ]
