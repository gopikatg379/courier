from django.db import models
from Adminapp.models import Consignor, Consignee, District, Vehicle, Driver


# Create your models here.

class Booking(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('dispatched', 'Dispatched'),
        ('delivered', 'Delivered'),
    ]
    date = models.DateField()
    booking_id = models.AutoField(primary_key=True)
    consignor = models.ForeignKey(Consignor, on_delete=models.CASCADE)
    consignor_name = models.CharField(max_length=255, default=1)
    consignee = models.ForeignKey(Consignee, on_delete=models.CASCADE)
    consignee_name = models.CharField(max_length=255, default=1)
    consignee_address = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=255, default=1)
    number_of_boxes = models.IntegerField()
    weight = models.IntegerField()
    price = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    processed = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='booked')

    class Meta:
        db_table = 'booking_table'


class Despatch(models.Model):
    date = models.DateField()
    despatch_id = models.AutoField(primary_key=True)
    bookings = models.ManyToManyField(Booking)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=255, default=1)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'despatch_table'


class Delivery(models.Model):
    DELIVERY_STATUS = [
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    ]
    date = models.DateField()
    delivery_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    consignor_name = models.CharField(max_length=200, default=1)
    consignee_name = models.CharField(max_length=200, default=1)
    district_name = models.CharField(max_length=200, default=1)
    status = models.CharField(max_length=9, choices=DELIVERY_STATUS, default='Returned')

    class Meta:
        db_table = 'delivery_table'


class Receipt(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        db_table = 'receipt_table'
