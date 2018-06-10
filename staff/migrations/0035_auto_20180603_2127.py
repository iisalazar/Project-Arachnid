# Generated by Django 2.0.5 on 2018-06-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0034_auto_20180531_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='news_pictures/%Y/%m/%d/cover'),
        ),
        migrations.AddField(
            model_name='news',
            name='lead_text',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.CharField(blank=True, max_length=10000000),
        ),
    ]
