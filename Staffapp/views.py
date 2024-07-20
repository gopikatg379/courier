from django.shortcuts import render, redirect
from .models import Booking, Delivery, Despatch, Consignor, Consignee, District, Driver, Vehicle
from django.contrib import messages


# Create your views here.

def add_booking(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        consignor_id = request.POST.get('consignor_name')
        consignee_id = request.POST.get('consignee_name')
        district_id = request.POST.get('district_name')
        number = request.POST.get('number')
        weight = request.POST.get('weight')
        price = request.POST.get('price')
        remark = request.POST.get('remark')
        try:
            consignor = Consignor.objects.get(consignor_id=consignor_id)
        except Consignor.DoesNotExist:
            messages.error(request, 'Invalid consignor selected')
            return redirect('/add_booking')
        try:
            consignee = Consignee.objects.get(consignee_id=consignee_id)
        except Consignee.DoesNotExist:
            messages.error(request, 'Invalid consignee selected')
            return redirect('/add_booking')
        try:
            district = District.objects.get(district_id=district_id)
        except District.DoesNotExist:
            messages.error(request, 'Invalid district selected')
            return redirect('/add_booking')
        try:
            price = float(request.POST.get('price'))
        except (ValueError, TypeError):
            messages.error(request, 'Invalid price value')
            return redirect('/add_booking')

        add_obj = Booking(
            date=date,
            consignor=consignor,
            consignor_name=consignor.consignor_name,
            consignee=consignee,
            consignee_name=consignee.consignee_name,
            district=district,
            district_name=district.district_name,
            number_of_boxes=number,
            weight=weight,
            price=price,
            remark=remark
        )
        add_obj.save()
        messages.success(request, 'Consignment booked successfully!')
        return redirect('/add_booking')
    data1 = Consignor.objects.all()
    data2 = Consignee.objects.all()
    data3 = District.objects.all()
    return render(request, 'add_booking.html', {'Consignor': data1, 'Consignee': data2, 'District': data3})


def list_booking(request):
    data = Booking.objects.all()
    return render(request, 'list_booking.html', {'booking_data': data})


def add_delivery(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        booking_id = request.POST.get('booking_id')
        del_status = request.POST.get('del_status')
        ret_status = request.POST.get('ret_status')
        if del_status:
            status = 'Delivered'
        elif ret_status:
            status = 'Returned'
        else:
            status = 'pending'

        try:
            booking = Booking.objects.get(booking_id=booking_id)
        except Booking.DoesNotExist:
            messages.error(request, 'Invalid booking selected')
            return redirect('/add_delivery')

        add_obj = Delivery(
            date=date,
            booking=booking,
            status=status,
            consignor_name=booking.consignor_name,
            consignee_name=booking.consignee_name,
            district_name=booking.district_name
        )
        add_obj.save()

        if status == 'Delivered':
            booking.status = 'delivered'
        else:
            booking.status = 'returned'
        booking.save()

        messages.success(request, 'Delivery recorded successfully')
        return redirect('/add_delivery')

    data1 = Booking.objects.all()
    return render(request, 'add_delivery.html', {'Booking': data1})


def list_delivery(request):
    data = Delivery.objects.all()
    return render(request, 'list_delivery.html', {'del_data': data})


def add_despatch(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        driver_id = request.POST.get('driver_name')
        vehicle_id = request.POST.get('vehicle_name')
        booking_ids = request.POST.getlist('booking_id')

        try:
            driver = Driver.objects.get(driver_id=driver_id)
        except Driver.DoesNotExist:
            messages.error(request, 'Invalid driver selected')
            return redirect('/add_despatch')

        try:
            vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
        except Vehicle.DoesNotExist:
            messages.error(request, 'Invalid vehicle selected')
            return redirect('/add_despatch')

        bookings = Booking.objects.filter(booking_id__in=booking_ids)
        if not bookings.exists():
            messages.error(request, 'Invalid booking(s) selected')
            return redirect('/add_despatch')

        add_obj = Despatch(
            date=date,
            driver=driver,
            driver_name=driver.driver_name,
            vehicle=vehicle,
            vehicle_name=vehicle.vehicle_number,
        )
        add_obj.save()
        add_obj.bookings.add(*bookings)
        add_obj.save()

        bookings.update(processed=True)

        messages.success(request, 'Despatch created successfully')
        return redirect('/add_despatch')

    data1 = Booking.objects.filter(processed=False)
    data2 = Driver.objects.all()
    data3 = Vehicle.objects.all()
    return render(request, 'add_despatch.html', {'despatch_data': data1, 'Driver': data2, 'Vehicle': data3})


def list_despatch(request):
    data = Despatch.objects.all().prefetch_related('bookings')
    return render(request, 'list_despatch.html', {'des_data': data})


def delete_booking(request, booking_id):
    booking_data = Booking.objects.get(booking_id=booking_id)
    booking_data.delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('/list_booking')


def delete_despatch(request, despatch_id):
    despatch_data = Despatch.objects.get(despatch_id=despatch_id)
    despatch_data.delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('/list_despatch')


def delete_delivery(request, delivery_id):
    data = Delivery.objects.get(delivery_id=delivery_id)
    data.delete()
    messages.success(request, 'Data deleted successfully')
    return redirect('/list_delivery')

