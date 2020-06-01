# Generated by Django 3.0.6 on 2020-05-17 13:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grps', '0003_auto_20200517_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=100), default=list, size=5),
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
            name='phone_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=list, size=5),
        ),
    ]