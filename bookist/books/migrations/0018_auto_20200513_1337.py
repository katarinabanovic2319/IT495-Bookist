# Generated by Django 3.0.6 on 2020-05-13 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20200513_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='review_score',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
