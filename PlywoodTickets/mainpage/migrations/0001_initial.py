# Generated by Django 5.0.6 on 2024-06-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id_flights', models.BigIntegerField(primary_key=True, serialize=False)),
                ('id_plane', models.BigIntegerField()),
                ('country_plan', models.TextField()),
                ('to_city', models.TextField()),
                ('from_city', models.TextField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('price', models.DecimalField(decimal_places=16, max_digits=32)),
            ],
        ),
    ]
