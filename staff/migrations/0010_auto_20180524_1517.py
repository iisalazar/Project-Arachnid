# Generated by Django 2.0.5 on 2018-05-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20180524_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='headline_image',
            field=models.ImageField(blank=True, null=True, upload_to='news_pictures/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='news',
            name='other_image',
            field=models.ImageField(blank=True, null=True, upload_to='news_pictures/%Y/%m/%d'),
        ),
    ]
