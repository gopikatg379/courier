from django.shortcuts import render, redirect
from .models import Login, Vehicle, Driver, District, Consignee, Consignor, Staff, Designation
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def login(request):
    if request.method == 'POST':
        staff_name = request.POST.get('staff_name')
        password = request.POST.get('password')
        try:
            staff = Staff.objects.get(staff_name=staff_name, password=password)
            request.session['staff_id'] = staff.staff_id
            messages.success(request, f'{staff_name} login successfully')
            return redirect('/dashboard')
        except Staff.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def dashboard(request):
    if 'staff_id' in request.session:
        return render(request, 'dashboard.html')
    else:
        return redirect('/')


def add_consignor(request):
    if request.method == 'POST':
        consignor_name = request.POST.get('consignor_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        status = request.POST.get('status')

        if status is None:
            status = 'inactive'
        else:
            status = 'active'

        add_obj = Consignor(
            consignor_name=consignor_name,
            address=address,
            phone_number=phone_number,
            status=status
        )
        add_obj.save()
        messages.success(request, 'Consignor added successfully!')
        return redirect('/add_consignor')

    return render(request, 'add_consignor.html')


def list_consignor(request):
    consignor_data = Consignor.objects.all()
    search_data = consignor_data
    if request.method == 'POST':
        search = request.POST.get('consignorName', '')
        if search:
            search_data = Consignor.objects.filter(consignor_name__icontains=search)
    return render(request, 'list_consignor.html', {'data': search_data})


def add_consignee(request):
    if request.method == 'POST':
        consignee_name = request.POST.get('consignee_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        status = request.POST.get('status')
        if status is None:
            status = 'inactive'
        else:
            status = 'active'

        add_obj = Consignee(
            consignee_name=consignee_name,
            address=address,
            phone_number=phone_number,
            status=status
        )
        add_obj.save()
        messages.success(request, 'Consignee added successfully!')
        return redirect('/add_consignee')

    return render(request, 'add_consignee.html')


def list_consignee(request):
    data = Consignee.objects.all()
    return render(request, 'list_consignee.html', {'con_data': data})


def add_user(request):
    if request.method == 'POST':
        staff_name = request.POST.get('staff_name')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        designation_id = request.POST.get('designation')
        status = request.POST.get('status')
        if status is None:
            status = 'inactive'
        else:
            status = 'active'
        try:
            designation = Designation.objects.get(designation_id=designation_id)
        except Designation.DoesNotExist:
            messages.error(request, 'Invalid designation selected')
            return redirect('/add_user')

        add_obj = Staff(
            staff_name=staff_name,
            password=password,
            designation=designation,
            designation_name=designation.designation,
            phone_number=phone_number,
            status=status
        )
        add_obj.save()
        messages.success(request, 'User created successfully!')
        return redirect('/add_user')

    data = Designation.objects.all()
    return render(request, 'add_user.html', {'designation': data})


def list_user(request):
    user_data = Staff.objects.all()
    return render(request, 'list_user.html', {'user_data': user_data})


def add_district(request):
    if request.method == 'POST':
        state = request.POST.get('state')
        district_name = request.POST.get('district_name')
        status = request.POST.get('status')
        if status is None:
            status = 'inactive'
        else:
            status = 'active'

        add_obj = District(
            state=state,
            district_name=district_name,
            status=status
        )
        add_obj.save()
        messages.success(request, 'District created successfully!')
        return redirect('/add_district')
    return render(request, 'add_district.html')


def list_district(request):
    district_data = District.objects.all()
    return render(request, 'list_district.html', {'district_data': district_data})


def add_vehicle(request):
    if request.method == 'POST':
        vehicle_number = request.POST.get('vehicle_number')
        status = request.POST.get('status')
        if status is None:
            status = 'inactive'
        else:
            status = 'active'
        add_obj = Vehicle(
            vehicle_number=vehicle_number,
            status=status
        )
        add_obj.save()
        messages.success(request, 'Vehicle added successfully!')
        return redirect('/add_vehicle')
    return render(request, 'add_vehicle.html')


def list_vehicle(request):
    data = Vehicle.objects.all()
    return render(request, 'list_vehicle.html', {'vehicle_data': data})


def add_driver(request):
    if request.method == 'POST':
        driver_name = request.POST.get('driver_name')
        phone_number = request.POST.get('phone_number')
        status = request.POST.get('status')
        if status is None:
            status = 'inactive'
        else:
            status = 'active'
        add_obj = Driver(
            driver_name=driver_name,
            phone_number=phone_number,
            status=status
        )
        add_obj.save()
        messages.success(request, 'Driver added successfully!')
    return render(request, 'add_driver.html')


def list_driver(request):
    driver_data = Driver.objects.all()
    return render(request, 'list_driver.html', {'data': driver_data})


def add_ledger(request):
    if request.method == 'POST':
        ledger_name = request.POST.get('ledger_name')
    return render(request, 'add_ledger.html')


def list_ledger(request):
    return render(request, 'list_ledger.html')


def cash_balance(request):
    return render(request, 'cash_balance.html')


def receipt(request):
    return render(request, 'receipt.html')


def payment(request):
    return render(request, 'payment.html')


def designation(request):
    add_obj = Designation()
    if request.method == 'POST':
        add_obj.designation = request.POST.get('designation')
        add_obj.save()
        return redirect('/designation')
    return render(request, 'designation.html')


def delete_dis(request, district_id):
    dis_obj = District.objects.get(district_id=district_id)
    dis_obj.delete()
    messages.success(request, 'District deleted successfully!')
    return redirect('/list_district')


def edit_dis(request, district_id):
    add_obj = District.objects.get(district_id=district_id)
    if request.method == 'POST':
        add_obj = District.objects.get(district_id=district_id)
        add_obj.state = request.POST.get('state')
        add_obj.district_name = request.POST.get('district_name')
        add_obj.status = request.POST.get('status')
        if add_obj.status is None:
            add_obj.status = 'inactive'
        else:
            add_obj.status = 'active'
        add_obj.save()
        messages.success(request, 'District edited successfully!')
        return redirect('/list_user')
    return render(request, 'update_district.html', {'dis_obj': add_obj})


def delete_user(request, staff_id):
    user_obj = Staff.objects.get(staff_id=staff_id)
    user_obj.delete()
    return redirect('/list_user')


def edit_user(request, staff_id):
    user_obj = Staff.objects.get(staff_id=staff_id)
    if request.method == 'POST':
        user_obj = Staff.objects.get(staff_id=staff_id)
        user_obj.staff_name = request.POST.get('staff_name')
        user_obj.phone_number = request.POST.get('phone_number')
        user_obj.status = request.POST.get('status')
        user_obj.save()
        if user_obj.status is None:
            user_obj.status = 'inactive'
        else:
            user_obj.status = 'active'
        designation_id = request.POST.get('designation_id')
        try:
            designation = Designation.objects.get(designation_id=designation_id)
            user_obj.designation = designation
        except Designation.DoesNotExist:
            messages.error(request, 'Invalid designation selected')
            return redirect('/list_user')

        return redirect('/list_user')
    data = Designation.objects.all()
    return render(request, 'update_user.html', {'user_data': user_obj, 'designation': data})


def delete_consignor(request, consignor_id):
    consignor_data = Consignor.objects.get(consignor_id=consignor_id)
    consignor_data.delete()
    messages.success(request, 'Consignor deleted successfully!')
    return redirect('/list_consignor')


def edit_consignor(request, consignor_id):
    consignor_obj = Consignor.objects.get(consignor_id=consignor_id)
    if request.method == 'POST':
        consignor_obj = Consignor.objects.get(consignor_id=consignor_id)
        consignor_obj.consignor_name = request.POST.get('consignor_name')
        consignor_obj.address = request.POST.get('address')
        consignor_obj.phone_number = request.POST.get('phone_number')
        consignor_obj.status = request.POST.get('status')
        if consignor_obj.status is None:
            consignor_obj.status = 'inactive'
        else:
            consignor_obj.status = 'active'
        consignor_obj.save()
        messages.success(request, 'Data edited successfully!')
        return redirect('/list_consignor')
    return render(request, 'update_consignor.html', {'data': consignor_obj})


def delete_consignee(request, consignee_id):
    data = Consignee.objects.get(consignee_id=consignee_id)
    data.delete()
    messages.success(request, 'Consignee deleted successfully!')
    return redirect('/list_consignee')


def edit_consignee(request, consignee_id):
    consignee_obj = Consignee.objects.get(consignee_id=consignee_id)
    if request.method == 'POST':
        consignee_obj = Consignee.objects.get(consignee_id=consignee_id)
        consignee_obj.consignee_name = request.POST.get('consignee_name')
        consignee_obj.address = request.POST.get('address')
        consignee_obj.phone_number = request.POST.get('phone_number')
        consignee_obj.status = request.POST.get('status')
        if consignee_obj.status is None:
            consignee_obj.status = 'inactive'
        else:
            consignee_obj.status = 'active'
        messages.success(request, 'Data edited successfully!')
        consignee_obj.save()
        return redirect('/list_consignee')
    return render(request, 'update_consignee.html', {'data': consignee_obj})


def delete_driver(request, driver_id):
    data = Driver.objects.get(driver_id=driver_id)
    data.delete()
    messages.success(request, 'Driver deleted Successfully!')
    return redirect('/list_driver')


def edit_driver(request, driver_id):
    driver_data = Driver.objects.get(driver_id=driver_id)
    if request.method == 'POST':
        driver_data = Driver.objects.get(driver_id=driver_id)
        driver_data.driver_name = request.POST.get('driver_name')
        driver_data.phone_number = request.POST.get('phone_number')
        driver_data.status = request.POST.get('status')
        if driver_data.status is None:
            driver_data.status = 'inactive'
        else:
            driver_data.status = 'active'
        driver_data.save()
        messages.success(request, 'Data edited successfully!')
        return redirect('/list_driver')
    return render(request, 'update_driver.html', {'data': driver_data})


def delete_vehicle(request, vehicle_id):
    vehicle_data = Vehicle.objects.get(vehicle_id=vehicle_id)
    vehicle_data.delete()
    messages.success(request, 'Vehicle removed successfully!')
    return redirect('/list_vehicle')
