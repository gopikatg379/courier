# Generated by Django 5.0.6 on 2024-06-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staffapp', '0009_rename_booking_despatch_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='consignee_name',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='delivery',
            name='consignor_name',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='delivery',
            name='district_name',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
