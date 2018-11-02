# Generated by Django 2.1.2 on 2018-11-01 18:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filepopulator', '0008_auto_20181101_1816'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='filename',
            field=models.FilePathField(match='\\.[j|J][p|P][e|E]*[g|G]$', max_length=255, path='/images', validators=[django.core.validators.RegexValidator(message='Filename must be a JPG', regex='\\.[j|J][p|P][e|E]*[g|G]$')]),
        ),
    ]
