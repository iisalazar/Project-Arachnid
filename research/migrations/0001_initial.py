# Generated by Django 2.0.5 on 2019-04-10 01:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('abstract', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='research_papers/<django.db.models.fields.textfield>', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('category', models.CharField(blank=True, choices=[('Applied', 'Applied Science'), ('Life', 'Life Science')], default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchProponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proponents', to='research.ResearchPaper')),
            ],
        ),
    ]