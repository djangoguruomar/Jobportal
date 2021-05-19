# Generated by Django 3.1.7 on 2021-03-22 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myjob.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='job category', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('compnay_name', models.CharField(help_text='Your Company Name', max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('highest_education', models.CharField(help_text='Enter your highest degree', max_length=20)),
                ('institution', models.CharField(help_text='Your last educational institution', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myjob.category')),
                ('group', models.ForeignKey(default=myjob.models.JobSeeker.default_group, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='job title', max_length=200)),
                ('education_rqr', models.CharField(help_text='minimum degree', max_length=200)),
                ('location', models.CharField(help_text='job location', max_length=200)),
                ('max_age', models.IntegerField(help_text='maximum age limit of the candidates')),
                ('experience', models.IntegerField(help_text='minimum work experience required')),
                ('deadline', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myjob.category')),
                ('recruiter', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myjob.recruiter')),
            ],
        ),
    ]