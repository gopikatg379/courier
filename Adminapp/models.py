from django.db import models


# Create your models here.

class Login(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16)

    class Meta:
        db_table = 'login_table'


class Consignor(models.Model):
    CONSIGNOR_STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    consignor_id = models.AutoField(primary_key=True)
    consignor_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    status = models.CharField(max_length=8, choices=CONSIGNOR_STATUS, default='Active')

    class Meta:
        db_table = 'consignor_table'


class Consignee(models.Model):
    CONSIGNEE_STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    consignee_id = models.AutoField(primary_key=True)
    consignee_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    status = models.CharField(max_length=8, choices=CONSIGNEE_STATUS, default='Active')

    class Meta:
        db_table = 'consignee_table'


class District(models.Model):
    DISTRICT_STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    district_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=200)
    district_name = models.CharField(max_length=255)
    status = models.CharField(max_length=8, choices=DISTRICT_STATUS, default='Active')

    class Meta:
        db_table = 'district_table'


class Vehicle(models.Model):
    VEHICLE_STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(max_length=155, default=1)
    status = models.CharField(max_length=8, choices=VEHICLE_STATUS, default='Active')

    class Meta:
        db_table = 'vehicle_table'


class Driver(models.Model):
    DRIVER_STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    status = models.CharField(max_length=8, choices=DRIVER_STATUS, default='Active')

    class Meta:
        db_table = 'driver_table'


class Designation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=200)

    class Meta:
        db_table = 'designation_table'


class Staff(models.Model):
    STAFF_STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=200)
    password = models.CharField(max_length=10, default=1)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    designation_name = models.CharField(max_length=255, default=1)
    phone_number = models.BigIntegerField()
    status = models.CharField(max_length=8, choices=STAFF_STATUS, default='Active')

    class Meta:
        db_table = 'staff_table'


class Ledger(models.Model):
    ledger_id = models.AutoField(primary_key=True)
    ledger_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'ledger_table'
