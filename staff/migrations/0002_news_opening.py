# Generated by Django 2.0.5 on 2018-11-21 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='opening',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]