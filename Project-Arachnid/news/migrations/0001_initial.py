# Generated by Django 2.0.5 on 2019-04-10 01:32

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=100)),
                ('author_additional_info', models.CharField(blank=True, max_length=100)),
                ('lead_text', models.TextField()),
                ('opening', models.CharField(blank=True, max_length=10000)),
                ('headline', models.CharField(max_length=200)),
                ('headline_image', models.ImageField(blank=True, null=True, upload_to=news.models.news_image_handler, validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg', 'JPG'])])),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to=news.models.news_image_handler)),
                ('body_text', models.TextField()),
                ('other_image', models.ImageField(blank=True, null=True, upload_to=news.models.news_image_handler)),
                ('other_image_label', models.CharField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
