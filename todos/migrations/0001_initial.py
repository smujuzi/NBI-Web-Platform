# Generated by Django 3.0 on 2020-01-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NBI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.TextField()),
                ('mda', models.TextField()),
                ('mda_site', models.TextField()),
                ('location', models.TextField()),
                ('district', models.TextField()),
                ('period_of_nbi_extension', models.TextField()),
                ('status', models.TextField()),
                ('internet', models.TextField()),
                ('leased_mda', models.TextField()),
                ('leased_ifms', models.TextField()),
                ('dark_fibre', models.TextField()),
                ('fy_period_of_connectivity', models.TextField()),
                ('date_of_connection_internet_bandwidth', models.TextField()),
                ('date_of_connection_ifms', models.TextField()),
                ('date_of_connection_leased_lines', models.TextField()),
                ('date_of_connection_dark_fibre', models.TextField()),
                ('internet_capacity', models.TextField()),
                ('leased_mda_capacity', models.TextField()),
                ('leased_ifms_capacity', models.TextField()),
                ('dark_fibre_quantity', models.TextField()),
                ('fibre_done', models.TextField()),
                ('odf_installed', models.TextField()),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
