# Generated by Django 2.0.5 on 2018-05-31 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0031_auto_20180531_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationofficer',
            name='school_year',
            field=models.PositiveIntegerField(choices=[(2017, 2017), (2017, 2018), (2018, 2017), (2018, 2018)], validators=[django.core.validators.MinValueValidator(2018), django.core.validators.MaxValueValidator(2018)]),
        ),
    ]
