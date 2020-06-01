# Generated by Django 3.0.6 on 2020-05-30 11:00

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Tour Guide', max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Job Position',
                'verbose_name_plural': 'Job Positions',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=20, verbose_name='Last Name')),
                ('nickname', models.CharField(max_length=20, verbose_name='Nickname')),
                ('phoneList', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), blank=True, default=list, size=5, verbose_name='Phone List')),
                ('emailList', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=100), blank=True, default=list, size=5, verbose_name='Email List')),
                ('extraNotes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, default=list, size=5, verbose_name='Extra Notes')),
                ('jobPosition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.JobPosition', verbose_name='Job Position')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'ordering': ['lastname'],
            },
        ),
    ]