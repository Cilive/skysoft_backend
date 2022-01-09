from django.urls import path,include
from rest_framework import routers

from employee.views import EmployeeInvoiceViewSet, MeterReadingViewSet



router = routers.DefaultRouter()

router.register("generate_invoice", EmployeeInvoiceViewSet, basename="generate_invoice")
router.register("meterreading", MeterReadingViewSet, basename="meter_reading")




urlpatterns = [
    path('', include(router.urls)),

  
]

