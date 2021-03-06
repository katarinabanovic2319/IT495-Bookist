# Generated by Django 3.0.6 on 2020-05-16 13:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0021_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_ratings',
            field=models.ManyToManyField(through='books.BookReview', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='bookreview',
            unique_together={('review_user', 'review_book')},
        ),
    ]
