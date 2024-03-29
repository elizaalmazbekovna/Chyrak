# Generated by Django 4.1.7 on 2023-05-22 10:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField()),
                ('place_of_birth', models.CharField(max_length=30)),
                ('place_of_death', models.CharField(max_length=30)),
                ('nationality', models.TextField(blank=True, default='', null=True)),
                ('blame', models.TextField(blank=True, null=True)),
                ('rehabilitated', models.CharField(blank=True, max_length=30, null=True)),
                ('occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('bedfellow', models.CharField(blank=True, max_length=30, null=True)),
                ('children', models.CharField(blank=True, max_length=30, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('desc_of_photo', models.TextField(blank=True, default='', null=True)),
                ('desc_of_file', models.TextField(blank=True, default='', null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('date_of_publish', models.DateField(default=datetime.datetime.now)),
                ('up_vote', models.IntegerField(default=0)),
                ('is_proven', models.BooleanField(default=False)),
                ('before_edit_content', models.TextField(default='')),
                ('after_edit_content', models.TextField(default='')),
                ('date_of_editing', models.DateField(default=datetime.datetime.now)),
                ('x', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
        ),
    ]
