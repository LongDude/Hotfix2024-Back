# Generated by Django 5.0.6 on 2024-06-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalLocker', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.TextField(null=True),
        ),
    ]