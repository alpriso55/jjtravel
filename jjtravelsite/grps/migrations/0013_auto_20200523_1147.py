# Generated by Django 3.0.6 on 2020-05-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grps', '0012_hotel_hoteldeposit_hotelreservation_hotelroomreservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of archeological site', max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('transportationMean', models.CharField(choices=[('BUS', 'Bus'), ('FER', 'Ferry'), ('AIR', 'Airplane'), ('TRA', 'Train'), ('WAL', 'Walk'), ('TEL', 'Teleferik'), ('KAT', 'Katamaran')], default='BUS', max_length=3)),
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='email_list',
            new_name='emailList',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='extra_notes',
            new_name='extraNotes',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='job_position',
            new_name='jobPosition',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='phone_list',
            new_name='phoneList',
        ),
    ]