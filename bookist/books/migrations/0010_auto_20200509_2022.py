# Generated by Django 3.0.6 on 2020-05-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20200509_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_list',
        ),
        migrations.AddField(
            model_name='booklist',
            name='list_book',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
