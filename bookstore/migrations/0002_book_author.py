# Generated by Django 3.1.6 on 2021-02-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]
