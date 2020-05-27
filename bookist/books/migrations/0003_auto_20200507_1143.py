# Generated by Django 3.0.6 on 2020-05-07 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.BookAuthor'),
        ),
    ]
