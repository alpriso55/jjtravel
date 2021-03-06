# Generated by Django 3.0.6 on 2020-05-18 14:04

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grps', '0004_auto_20200517_2216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantmenu',
            options={},
        ),
        migrations.RemoveField(
            model_name='restaurantmenu',
            name='cost',
        ),
        migrations.AddField(
            model_name='person',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=5),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=5),
        ),
        migrations.AddField(
            model_name='restaurantmenu',
            name='cost_per_person',
            field=models.DecimalField(decimal_places=1, default=10.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='restaurantmenu',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=5),
        ),
        migrations.CreateModel(
            name='RestaurantReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_pax', models.PositiveSmallIntegerField()),
                ('free_pax', models.PositiveSmallIntegerField()),
                ('extra_cost', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('extra_notes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=5)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grps.GroupDetails')),
                ('restaurant_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grps.RestaurantMenu')),
            ],
        ),
    ]
