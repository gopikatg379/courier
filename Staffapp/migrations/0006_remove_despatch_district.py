# Generated by Django 5.0.6 on 2024-06-20 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Staffapp', '0005_despatch_vehicle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='despatch',
            name='district',
        ),
    ]
