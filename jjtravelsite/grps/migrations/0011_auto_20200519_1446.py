# Generated by Django 3.0.6 on 2020-05-19 05:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grps', '0010_auto_20200519_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='appetizer_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='dessert_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='drink_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='main_dish_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='salad_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='soup_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, size=5),
        ),
        migrations.AlterField(
            model_name='restaurantreservation',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, default=list, size=5),
        ),
    ]
