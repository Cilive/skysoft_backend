from django.urls import path,include


from . import views
from rest_framework import routers
from .views import CustomerViewSet,BankViewSet, DepositViewSet, DispenceViewSet, FuelRegistrationViewSet, InvoiceViewSet, OwnerViewSet, VatRegistrationViewset


router = routers.DefaultRouter()


router.register("customer", CustomerViewSet, basename="customer")
router.register("invoice", InvoiceViewSet, basename="invoice")
# router.register("recipt", ReciptViewSet, basename="recipt")
router.register("vatmaster", VatRegistrationViewset, basename="vat_master")
router.register("fuelmaster", FuelRegistrationViewSet, basename="fuel_master")
router.register("bank", BankViewSet, basename="bank")
router.register("owner", OwnerViewSet, basename="owner")
router.register("deposit", DepositViewSet, basename="deposit")
router.register("dispense", DispenceViewSet, basename="dispense")





urlpatterns = [
    path('', include(router.urls)),    
  

]

# urlpatterns = format_suffix_patterns(urlpatterns)
