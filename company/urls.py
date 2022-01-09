from django.urls import path,include
# from . import views
from .views import  BankViewSet, CustomerViewSet, DebtorsReportViewSet, DepositViewSet,  DispenceViewSet, EmployeeSaleReportViewSet,FuelRegistrationViewSet, IncomeReportViewSet,  InvoiceViewSet,  OwnerViewSet, PurchaseReportViewSet, ReciptViewSet, SaleReportViewSet, SupplierReportViewSet, VatRegistrationViewset
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers



router = routers.DefaultRouter()


router.register("customer", CustomerViewSet, basename="customer")
router.register("invoice", InvoiceViewSet, basename="invoice")
router.register("recipt", ReciptViewSet, basename="recipt")
router.register("vatmaster", VatRegistrationViewset, basename="vat_master")
router.register("fuelmaster", FuelRegistrationViewSet, basename="fuel_master")
router.register("bank", BankViewSet, basename="bank")
router.register("owner", OwnerViewSet, basename="owner")
router.register("deposit", DepositViewSet, basename="deposit")
router.register("dispense", DispenceViewSet, basename="dispense")
router.register("report/sale", SaleReportViewSet, basename="sale_report")
router.register("sale/employee", EmployeeSaleReportViewSet, basename="sale_employee_report")
router.register("report/purchase", PurchaseReportViewSet, basename="purchase_report")
router.register("report/income", IncomeReportViewSet, basename="income")
router.register("report/supplier", SupplierReportViewSet, basename="supplier_statement")
router.register("report/debtors", DebtorsReportViewSet, basename="debtors_statement")





urlpatterns = [
    path('', include(router.urls)), 

]

# urlpatterns = format_suffix_patterns(urlpatterns)
