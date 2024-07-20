# Generated by Django 5.0.6 on 2024-06-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('consignee_id', models.AutoField(primary_key=True, serialize=False)),
                ('consignee_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'consignee_table',
            },
        ),
        migrations.CreateModel(
            name='Consignor',
            fields=[
                ('consignor_id', models.AutoField(primary_key=True, serialize=False)),
                ('consignor_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'consignor_table',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district_id', models.AutoField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'district_table',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('driver_name', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
            ],
            options={
                'db_table': 'driver_table',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'login_table',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'staff_table',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=155)),
            ],
            options={
                'db_table': 'vehicle_table',
            },
        ),
    ]
