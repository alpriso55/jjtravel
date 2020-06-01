# Generated by Django 3.0.6 on 2020-05-30 11:00

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('grps', '0015_auto_20200527_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoteldeposit',
            name='hotel_reservation',
        ),
        migrations.RemoveField(
            model_name='hotelreservation',
            name='group',
        ),
        migrations.RemoveField(
            model_name='hotelreservation',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='hotelroomreservation',
            name='hotel_reservation',
        ),
        migrations.RemoveField(
            model_name='person',
            name='jobPosition',
        ),
        migrations.RemoveField(
            model_name='restaurantmenu',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='restaurantreservation',
            name='group',
        ),
        migrations.RemoveField(
            model_name='restaurantreservation',
            name='restaurant_menu',
        ),
        migrations.RemoveField(
            model_name='sitevisit',
            name='group',
        ),
        migrations.RemoveField(
            model_name='sitevisit',
            name='site',
        ),
        migrations.AlterModelOptions(
            name='groupdetail',
            options={'ordering': ['group_name'], 'verbose_name': 'Group Detail', 'verbose_name_plural': 'Group Details'},
        ),
        migrations.AlterModelOptions(
            name='groupname',
            options={'ordering': ['departure_date'], 'verbose_name': 'Group Name', 'verbose_name_plural': 'Group Names'},
        ),
        migrations.AddField(
            model_name='groupdetail',
            name='extra_notes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, default=list, size=5, verbose_name='Extra Notes'),
        ),
        migrations.AlterField(
            model_name='groupdetail',
            name='tour_guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Person', verbose_name='Tour Guide'),
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='HotelDeposit',
        ),
        migrations.DeleteModel(
            name='HotelReservation',
        ),
        migrations.DeleteModel(
            name='HotelRoomReservation',
        ),
        migrations.DeleteModel(
            name='JobPosition',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.DeleteModel(
            name='RestaurantMenu',
        ),
        migrations.DeleteModel(
            name='RestaurantReservation',
        ),
        migrations.DeleteModel(
            name='Site',
        ),
        migrations.DeleteModel(
            name='SiteVisit',
        ),
    ]