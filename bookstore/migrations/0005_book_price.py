# Generated by Django 3.1.6 on 2021-02-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_book_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(default='', max_length=50),
        ),
    ]
