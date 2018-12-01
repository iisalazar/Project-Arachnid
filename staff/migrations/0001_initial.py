# Generated by Django 2.0.5 on 2018-12-01 14:43

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
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=21845)),
                ('file', models.FileField(blank=True, null=True, upload_to='announcement_documents', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx'])])),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=100)),
                ('author_additional_info', models.CharField(blank=True, max_length=100)),
                ('lead_text', models.TextField()),
                ('opening', models.CharField(blank=True, max_length=10000)),
                ('headline', models.TextField()),
                ('headline_image', models.ImageField(blank=True, null=True, upload_to='news_pictures/%Y/%m/%d')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='news_pictures/%Y/%m/%d/cover')),
                ('body_text', models.TextField()),
                ('other_image', models.ImageField(blank=True, null=True, upload_to='news_pictures/%Y/%m/%d')),
                ('other_image_label', models.CharField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, choices=[('Main', 'Main'), ('Core Subject', 'Core Subject'), ('Social Science', 'Social Science'), ('Music and Arts', 'Music and Arts')], max_length=50, null=True)),
                ('logo', models.ImageField(null=True, upload_to='organization/<django.db.models.fields.CharField>/logo')),
                ('acronym', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_year', models.PositiveIntegerField(choices=[(2017, 2017), (2018, 2018)], validators=[django.core.validators.MinValueValidator(2018), django.core.validators.MaxValueValidator(2018)])),
                ('adviser', models.CharField(max_length=100)),
                ('president', models.CharField(max_length=100)),
                ('vice_president', models.CharField(max_length=100)),
                ('secretary', models.CharField(max_length=100)),
                ('treasurer', models.CharField(max_length=100)),
                ('auditor', models.CharField(max_length=100)),
                ('pio', models.CharField(max_length=100)),
                ('g7_rep', models.CharField(max_length=100)),
                ('g8_rep', models.CharField(max_length=100)),
                ('g9_rep', models.CharField(max_length=100)),
                ('g10_rep', models.CharField(max_length=100)),
                ('g11_rep', models.CharField(max_length=100)),
                ('g12_rep', models.CharField(max_length=100)),
                ('adviser_picture', models.ImageField(blank=True, null=True, upload_to='organiation/none/profiles')),
                ('pres_picture', models.ImageField(blank=True, null=True, upload_to='organization/none/profiles')),
                ('vp_picture', models.ImageField(blank=True, null=True, upload_to='organization/none/profiles')),
                ('sec_picture', models.ImageField(blank=True, null=True, upload_to='organization/none/profiles')),
                ('tres_picture', models.ImageField(blank=True, null=True, upload_to='organization/none/profiles')),
                ('aud_picture', models.ImageField(blank=True, null=True, upload_to='organization/None/profiles')),
                ('pio_picture', models.ImageField(blank=True, null=True, upload_to='organization/None/profiles')),
                ('g7_picture', models.ImageField(blank=True, null=True, upload_to='organization/None/profiles')),
                ('g8_picture', models.ImageField(blank=True, null=True, upload_to='organization/None/profiles')),
                ('g9_picture', models.ImageField(blank=True, null=True, upload_to='organization/None/profiles')),
                ('g10_picture', models.ImageField(blank=True, null=True, upload_to='organization/None/profiles')),
                ('g11_picture', models.ImageField(blank=True, null=True, upload_to='organization/None/profiles')),
                ('g12_picture', models.ImageField(blank=True, null=True, upload_to='organization/None/profiles')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officers', to='staff.Organization')),
            ],
        ),
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
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proponents', to='staff.ResearchPaper')),
            ],
        ),
    ]
