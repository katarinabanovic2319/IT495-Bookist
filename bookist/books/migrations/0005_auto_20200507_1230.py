# Generated by Django 3.0.6 on 2020-05-07 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200507_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookgenre',
            old_name='name',
            new_name='genre_name',
        ),
    ]
