# Generated by Django 2.0.5 on 2018-05-31 13:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0028_organization_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2018), django.core.validators.MaxValueValidator(2018)])),
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
            ],
        ),
        migrations.RemoveField(
            model_name='organization',
            name='adviser',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='adviser_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='aud_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='auditor',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g10_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g10_rep',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g11_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g11_rep',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g12_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g12_rep',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g7_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g7_rep',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g8_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g8_rep',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g9_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='g9_rep',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='pio',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='pio_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='pres_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='president',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='sec_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='secretary',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='treasurer',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='tres_picture',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='vice_president',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='vp_picture',
        ),
        migrations.AddField(
            model_name='organizationofficer',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officers', to='staff.Organization'),
        ),
    ]
