"""
URL configuration for Courier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Adminapp import views as admin_views
from Staffapp import views as staff_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', admin_views.login),
                  path('add_user', admin_views.add_user),
                  path('list_user', admin_views.list_user),
                  path('dashboard', admin_views.dashboard),
                  path('add_booking', staff_views.add_booking),
                  path('list_booking', staff_views.list_booking),
                  path('add_consignee', admin_views.add_consignee),
                  path('list_consignee', admin_views.list_consignee),
                  path('add_consignor', admin_views.add_consignor),
                  path('list_consignor', admin_views.list_consignor),
                  path('add_delivery', staff_views.add_delivery),
                  path('list_delivery', staff_views.list_delivery),
                  path('add_despatch', staff_views.add_despatch),
                  path('list_despatch', staff_views.list_despatch),
                  path('add_district', admin_views.add_district),
                  path('list_district', admin_views.list_district),
                  path('add_vehicle', admin_views.add_vehicle),
                  path('list_vehicle', admin_views.list_vehicle),
                  path('add_driver', admin_views.add_driver),
                  path('list_driver', admin_views.list_driver),
                  path('add_ledger', admin_views.add_ledger),
                  path('list_ledger', admin_views.list_ledger),
                  path('payment', admin_views.payment),
                  path('receipt', admin_views.receipt),
                  path('cash_balance', admin_views.cash_balance),
                  path('designation', admin_views.designation),
                  path('delete_dis/<int:district_id>/', admin_views.delete_dis),
                  path('edit_dis/<int:district_id>/', admin_views.edit_dis),
                  path('delete_user/<int:staff_id>/', admin_views.delete_user),
                  path('edit_user/<int:staff_id>/', admin_views.edit_user),
                  path('delete_consignor/<int:consignor_id>/', admin_views.delete_consignor),
                  path('edit_consignor/<int:consignor_id>/', admin_views.edit_consignor),
                  path('delete_consignee/<int:consignee_id>/', admin_views.delete_consignee),
                  path('edit_consignee/<int:consignee_id>/', admin_views.edit_consignee),
                  path('delete_driver/<int:driver_id>/', admin_views.delete_driver),
                  path('edit_driver/<int:driver_id>/', admin_views.edit_driver),
                  path('delete_vehicle/<int:vehicle_id>/', admin_views.delete_vehicle),
                  path('delete_booking/<int:booking_id>/', staff_views.delete_booking),
                  path('delete_despatch/<int:despatch_id>/', staff_views.delete_despatch),
                  path('delete_delivery/<int:delivery_id>', staff_views.delete_delivery)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
