# Generated by Django 3.0.6 on 2020-05-19 05:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grps', '0008_auto_20200519_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=100), default=list, size=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='email_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=100), default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=5),
        ),
    ]
