# Generated by Django 5.0.6 on 2024-06-07 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0007_remove_driver_vehicle_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('designation_id', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'designation_table',
            },
        ),
        migrations.AlterField(
            model_name='staff',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.designation'),
        ),
    ]
