# Generated by Django 2.1.2 on 2018-11-01 17:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagger', '0005_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='height',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='width',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
