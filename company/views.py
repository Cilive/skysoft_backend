import datetime
from django.db.models.aggregates import Sum
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status,views,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework import viewsets
from .permissions import (IsCompany)




from company.models import BankAccountMaster, Contact,  Deposit, Dispence, Expense, FuelMaster,  Invoice, Owner,   VatMaster
from company.serielizer import BankCreateSerializer, BankSerializer, CustomerCraeteSerializer, CustomerSerializer, DebtorsReportSerializer,  DepositCreateSerializer, DepositSerializer, DispenceCreateSerializer, DispenceSerializer, EmployeeSaleReportSerializer,  FuelListSerializer,  FuelRegistrationSerializer, FuelSerializer, IncomeReportSerializer, InvoiceCreateSerializer, InvoiceSerializer, InvoiceUpdateSerializer,  OwnerCreateSerializer, OwnerSerializer, OwnerUpdateSerializer, PurchaseReportSerializer, ReciptCreateSerializer, ReciptSerializer, ReciptUpdateSerializer, SaleReportSerializer, SupplierReportSerializer,   VatRegistrationSerializer, VatSerializer
from shared_tenant.models import Company


# Create your views here.



class CustomerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    
    def create(self, request):
        try:
            serializer = CustomerCraeteSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        try:
            customer = Contact.objects.filter(type=1,company=Company.objects.get(user=request.user))
            serializer = CustomerSerializer(customer, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            customer = Contact.objects.filter(pk=pk,type=1)
            if not customer:
                return  Response({'message':"Customer not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = CustomerSerializer(customer[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            customer = Contact.objects.filter(pk=pk,type=1)
            if not customer:
                return  Response({'message':"Customer not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = CustomerSerializer(customer[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            customer = Contact.objects.filter(pk=pk,type=1)
            if not customer:
                return  Response({'message':"Customer not found"},status=status.HTTP_404_NOT_FOUND)
            customer[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class InvoiceViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    
    def create(self, request):
        try:
            print("request",request)
            print("request data",request.data)
            serializer = InvoiceCreateSerializer(data=request.data, context={"request": request,"data":request.data})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        try:
            invoices = Invoice.objects.filter(type=2,company=Company.objects.get(user=request.user))
            serializer = InvoiceSerializer(invoices, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            invoice = Invoice.objects.filter(pk=pk,type=2,company=Company.objects.get(user=request.user))
            if not invoice:
                return  Response({'message':"invoice not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = InvoiceSerializer(invoice[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:

            invoice = Invoice.objects.filter(pk=pk,type=2,company=Company.objects.get(user=request.user))
            if not invoice:
                return  Response({'message':"invoice not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = InvoiceUpdateSerializer(invoice[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:

            invoice = Invoice.objects.filter(pk=pk,type=2,company=Company.objects.get(user=request.user))
            if not invoice:
                return  Response({'message':"invoice not found"},status=status.HTTP_404_NOT_FOUND)
            invoice[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReciptViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class=ReciptCreateSerializer
    
    def create(self, request):
        try:
            print("Recipt request data",request.data)

            serializer = ReciptCreateSerializer(data=request.data, context={"request": request,"data":request.data})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        try:
            recipts = Invoice.objects.filter(type=1,company=Company.objects.get(user=request.user))
            serializer = ReciptSerializer(recipts, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            recipt = Invoice.objects.filter(pk=pk,type=1,company=Company.objects.get(user=request.user))
            if not recipt:
                return  Response({'message':"invoice not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = ReciptSerializer(recipt[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:

            recipt = Invoice.objects.filter(pk=pk,type=1,company=Company.objects.get(user=request.user))
            if not recipt:
                return  Response({'message':"invoice not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = ReciptUpdateSerializer(recipt[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:

            recipt = Invoice.objects.filter(pk=pk,type=1,company=Company.objects.get(user=request.user))
            if not recipt:
                return  Response({'message':"invoice not found"},status=status.HTTP_404_NOT_FOUND)
            recipt[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)



class VatRegistrationViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    
    def create(self, request):
        try:
            serializer = VatRegistrationSerializer(data=request.data, context={"request": request})
            print(type(request.data['vat']))
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':' Vat inserton Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        try:
            vat = VatMaster.objects.filter(company=Company.objects.get(user=request.user))
            serializer = VatSerializer(vat, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

     
    def retrieve(self, request, pk=None):
        try:
            supplier = VatMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not supplier:
                return  Response({'message':"Vat not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = VatSerializer(supplier[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, pk=None):
        try:
            vat = VatMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not vat:
                return  Response({'message':"Vat not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = VatSerializer(vat[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            vat = VatMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not vat:
                return  Response({'message':"Vat not found"},status=status.HTTP_404_NOT_FOUND)
            vat[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class FuelRegistrationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    
    def create(self, request):
        try:
            serializer = FuelRegistrationSerializer(data=request.data,context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Fuel added succesfully', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        try:
            fuel = FuelMaster.objects.filter(company=Company.objects.get(user=request.user))
            serializer = FuelListSerializer(fuel, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, pk=None):
        try:
            fuel = FuelMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not fuel:
                return  Response({'message':"Fuel not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = FuelSerializer(fuel[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            fuel = FuelMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not fuel:
                return  Response({'message':"Fuel not found"},status=status.HTTP_404_NOT_FOUND)
            fuel[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, pk=None):
        try:
            fuel = FuelMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not fuel:
                return  Response({'message':"Fuel not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = FuelSerializer(fuel[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)



   

# class FuelUpdateView(ListBulkCreateUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated,IsOwner]
    
#     queryset = FuelMaster.objects.all()
#     model = FuelMaster
#     serializer_class = FuelUpdateSerializer
#     serializer = FuelUpdateSerializer(queryset, many=True)

    
# class PurchaseViewSet(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request):
#         try:
#             serializer = PurchaseCreateSerializer(data=request.data, context={"request": request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#     def get(self, request):
#         try:
#             purchase = Purchase.objects.filter(company=Company.objects.get(user=request.user))
#             serializer = PurchaseSerializer(purchase, many=True, context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)



#     def put(self, request, pk=None):
#         try:
#             purchase = Purchase.objects.filter(pk=pk)
#             if not purchase:
#                 return  Response({'message':"Purchase not found"},status=status.HTTP_404_NOT_FOUND)
#             serializer = PurchaseSerializer(purchase[0], data=request.data, context={"request": request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#     def delete(self, request, pk=None):
#         try:
#             purchase = Purchase.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
#             if not purchase:
#                 return  Response({'message':"Purchase not found"},status=status.HTTP_404_NOT_FOUND)
#             purchase[0].delete()
#             return Response({'msg':'Success'},status.HTTP_200_OK)
        
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)


# class PurchaseDetails(generics.GenericAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = Purchase.objects.all()    
#     serializer_class=PurchaseSerializer


#     def get(self, request, pk=None):
#         try:
#             purchase = Purchase.objects.filter(pk=pk)
#             if not purchase:
#                 return  Response({'message':"Purchase not found"},status=status.HTTP_404_NOT_FOUND)
#             serializer = PurchaseSerializer(purchase[0], context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)


# class SaleViewSet(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request):
#         try:
#             serializer = SaleCreateSerializer(data=request.data, context={"request": request})
#             print(serializer)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    # def list(self, request):
    #     try:
    #         sale = Sale.objects.filter(company=Company.objects.get(account=request.user))
    #         serializer = SaleSerializer(sale, many=True, context={"request": request})
    #         return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
    #     except:
    #         return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def retrieve(self, request, pk=None):
    #     try:
    #         sale = Sale.objects.filter(pk=pk)
    #         if not sale:
    #             return  Response({'message':"Sale not found"},status=status.HTTP_404_NOT_FOUND)
    #         serializer = SaleSerializer(sale[0], context={"request": request})
    #         return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
    #     except:
    #         return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def update(self, request, pk=None):
    #     try:
    #         sale = Sale.objects.filter(pk=pk)
    #         if not sale:
    #             return  Response({'message':"Sale not found"},status=status.HTTP_404_NOT_FOUND)
    #         serializer = SaleSerializer(sale[0], data=request.data, context={"request": request})
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
    #         return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
    #     except:
    #         return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # def destroy(self, request, pk=None):
    #     try:
    #         sale = Sale.objects.filter(pk=pk)
    #         if not sale:
    #             return  Response({'message':"Sale not found"},status=status.HTTP_404_NOT_FOUND)
    #         sale[0].delete()
    #         return Response({'msg':'Success'},status.HTTP_200_OK)
        
    #     except:
    #         return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

       

# class FuelSaleViewSet(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request):
#         try:
#             serializer = FuelSaleCreateSerializer(data=request.data, context={"request": request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'sale added succesfully', 'data':serializer.data},status.HTTP_201_CREATED)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
#     def get(self, request):
#         try:
#             fuel_sales = FuelSale.objects.filter(company=Company.objects.get(user=request.user))
#             serializer = FuelSaleSerializer(fuel_sales, many=True, context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
#     def put(self, request, pk=None):
#         try:
#             sale = FuelSale.objects.filter(pk=pk)
#             if not sale:
#                 return  Response({'message':"Sale not found"},status=status.HTTP_404_NOT_FOUND)
#             serializer = FuelSaleSerializer(sale[0], data=request.data, context={"request": request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#     def delete(self, request, pk=None):
#         try:
#             sale = FuelSale.objects.filter(pk=pk)
#             if not sale:
#                 return  Response({'message':"Sale not found"},status=status.HTTP_404_NOT_FOUND)
#             sale[0].delete()
#             return Response({'msg':'Success'},status.HTTP_200_OK)
        
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
# class FuelSaleDetails(generics.GenericAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = FuelSale.objects.all()    
#     serializer_class=FuelSaleSerializer


#     def get(self, request, pk=None):
#         try:
#             fuel_sale = FuelSale.objects.filter(pk=pk)
#             if not fuel_sale:
#                 return  Response({'message':"Bank not found"},status=status.HTTP_404_NOT_FOUND)
#             serializer = FuelSaleSerializer(fuel_sale[0], context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
   
        
class BankViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    
    def create(self, request):
        try:
            serializer = BankCreateSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        try:
            bank = BankAccountMaster.objects.filter(company=Company.objects.get(user=request.user))
            serializer = BankSerializer(bank, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
 
  

    def update(self, request, pk=None):
        try:
            bank = BankAccountMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not bank:
                return  Response({'message':"Bank not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = BankSerializer(bank[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            bank = BankAccountMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not bank:
                return  Response({'message':"Bank not found"},status=status.HTTP_404_NOT_FOUND)
            bank[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, pk=None):
        try:
            bank = BankAccountMaster.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not bank:
                return  Response({'message':"Bank not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = BankSerializer(bank[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
     



    
   
# class PaymentOutViewSet(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request):
#         try:
#             serializer = PaymentOutCreateSerializer(data=request.data, context={"request": request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#     def get(self, request):
#         try:
#             payment_out = PaymentOut.objects.filter(company=Company.objects.get(user=request.user))
#             serializer = PaymentOutSerializer(payment_out, many=True, context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)


#     def put(self, request, pk=None):
#         try:
#             payment_out = PaymentOut.objects.filter(pk=pk)
#             if not payment_out:
#                 return  Response({'message':"Payment Out not found"},status=status.HTTP_404_NOT_FOUND)
#             serializer = PaymentOutSerializer(payment_out[0], data=request.data, context={"request": request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#     def delete(self, request, pk=None):
#         try:
#             payment_out = PaymentOut.objects.filter(pk=pk)
#             if not payment_out:
#                 return  Response({'message':"Payment Out not found"},status=status.HTTP_404_NOT_FOUND)
#             payment_out[0].delete()
#             return Response({'msg':'Success'},status.HTTP_200_OK)
        
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
# class PaymentOutDetails(generics.GenericAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = PaymentOut.objects.all()    
#     serializer_class=BankSerializer


#     def get(self, request, pk=None):
#         try:
#             payment_out = PaymentOut.objects.filter(pk=pk)
#             if not payment_out:
#                 return  Response({'message':"Payment Out not found"},status=status.HTTP_404_NOT_FOUND)
#             serializer = PaymentOutSerializer(payment_out[0], context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

# class ExpenseViewSet(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request):
#         try:
#             serializer = ExpenseCreateSerializer(data=request.data, context={"request": request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#     def get(self, request):
#         try:
#             expense = Expense.objects.filter(company=Company.objects.get(user=request.user))
#             serializer = ExpenseSerializer(expense, many=True, context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

   

#     def put(self, request, pk=None):
#         try:
#             expense = Expense.objects.filter(pk=pk)
#             if not expense:
#                 return  Response({'message':"Expense not found"},status=status.HTTP_404_NOT_FOUND)
#             serializer = ExpenseSerializer(expense[0], data=request.data, context={"request": request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#             return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#     def delete(self, request, pk=None):
#         try:
#             expense = Expense.objects.filter(pk=pk)
#             if not expense:
#                 return  Response({'message':"Expense not found"},status=status.HTTP_404_NOT_FOUND)
#             expense[0].delete()
#             return Response({'msg':'Success'},status.HTTP_200_OK)
        
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        
# class ExpenseDetails(generics.GenericAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = PaymentOut.objects.all()    
#     serializer_class=BankSerializer


#     def get(self, request, pk=None):
#         try:
#             expense = Expense.objects.filter(pk=pk)
#             if not expense:
#                 return  Response({'message':"Expense not found"},status=status.HTTP_404_NOT_FOUND)
#             serializer = ExpenseSerializer(expense[0], context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except:
#             return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)



class OwnerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    
    def create(self, request):
        try:
            serializer = OwnerCreateSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:

            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        try:
            owner = Owner.objects.filter(company=Company.objects.get(user=request.user))
            serializer = OwnerSerializer(owner, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except  Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk=None):
        try:
            owner = Owner.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not owner:
                return  Response({'message':"Owner not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = OwnerUpdateSerializer(owner[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)

            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            owner = Owner.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not owner:
                return  Response({'message':"Owner not found"},status=status.HTTP_404_NOT_FOUND)
            owner[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, pk=None):
        try:
            owner = Owner.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not owner:
                return  Response({'message':"Owner not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = OwnerSerializer(owner[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
            





    
class DepositViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    
    def create(self, request):
        try:
            serializer = DepositCreateSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        try:
            deposit = Deposit.objects.filter(company=Company.objects.get(user=request.user))
            serializer = DepositSerializer(deposit, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

  

    def update(self, request, pk=None):
        try:
            deposit = Deposit.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not deposit:
                return  Response({'message':"Deposit not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = DepositSerializer(deposit[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            deposit = Deposit.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not deposit:
                return  Response({'message':"Deposit not found"},status=status.HTTP_404_NOT_FOUND)
            deposit[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, pk=None):
        try:
            deposit = Deposit.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not deposit:
                return  Response({'message':"Deposit not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = DepositSerializer(deposit[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class DispenceViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    
    def create(self, request):
        try:
            serializer = DispenceCreateSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:

            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        try:
            dispence = Dispence.objects.filter(company=Company.objects.get(user=request.user))
            serializer = DispenceSerializer(dispence, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except  Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk=None):
        try:
            dispence = Dispence.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not dispence:
                return  Response({'message':"Dispence not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = DispenceSerializer(dispence[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            dispence = Dispence.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not dispence:
                return  Response({'message':"Dispence not found"},status=status.HTTP_404_NOT_FOUND)
            dispence[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, pk=None):
        try:
            dispence = Dispence.objects.filter(pk=pk,company=Company.objects.get(user=request.user))
            if not dispence:
                return  Response({'message':"Dispence not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = DispenceSerializer(dispence[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)




class SaleReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]     

    def list(self, request, format=None):
        try:           
            all =request.query_params.get('all')
            frm=request.query_params.get('from')
            to=request.query_params.get('to')
            branches=request.query_params.get('branch')
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        
            customer = request.query_params.get('customer')   
        
            kwargs = {}

            if int(all)==1:
                print("all condtion working")
                kwargs['type']=2
                
            if customer:

                kwargs['contact']=customer  
            if frm:
                today_min=frm
            if to:
                today_max=to
            if branches:
                kwargs['branches']=branches           
            
            sale_data = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)) 
            serializer = SaleReportSerializer(sale_data, many=True, context={"request": request,"data":kwargs,"datefrom":today_min,"dateto":today_max})
            return Response({'data': serializer.data, 'msg':'Success'},status=status.HTTP_200_OK)


        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class EmployeeSaleReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]  
    serializer_class=EmployeeSaleReportSerializer
     

    def list(self, request, format=None):
        try:           
            all =request.query_params.get('all')
            frm=request.query_params.get('from')
            emp=request.query_params.get('employee')
            to=request.query_params.get('to')
            branches=request.query_params.get('branch')
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        
            # customer = request.query_params.get('customer')   
        
            kwargs = {}

            if int(all)==1:
                print("all condtion working")
                kwargs['type']=2
                
            # if customer:

            #     kwargs['contact']=customer  
            if frm:
                today_min=frm
            if emp:
                kwargs['emp']=emp  
            
            if to:
                today_max=to
            if branches:
                kwargs['branches']=branches           
            
            sale_data = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)) 
            print(sale_data.query)
            serializer = SaleReportSerializer(sale_data, many=True, context={"request": request,"data":kwargs,"datefrom":today_min,"dateto":today_max})
            return Response({'data': serializer.data, 'msg':'Success'},status=status.HTTP_200_OK)


        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class PurchaseReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]     

    def list(self, request, format=None):
        try:           
            all =request.query_params.get('all')
            frm=request.query_params.get('from')
            to=request.query_params.get('to')
            branches=request.query_params.get('branch')
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        
            supllier = request.query_params.get('supplier')   
        
            kwargs = {}

            if int(all)==1:
                print("all condtion working")
                kwargs['type']=1
                
            if supllier:
                kwargs['contact']=supllier  
            if frm:
                today_min=frm
            if to:
                today_max=to
            if branches:
                kwargs['branches']=branches 
            print("kwargs",kwargs)          
            
            sale_data = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)) 
            serializer = PurchaseReportSerializer(sale_data, many=True, context={"request": request,"data":kwargs,"datefrom":today_min,"dateto":today_max})
            return Response({'data': serializer.data, 'msg':'Success'},status=status.HTTP_200_OK)


        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    



class IncomeReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]     

    def list(self, request, format=None):
        try:           
            # all =request.query_params.get('all')
            frm=request.query_params.get('from')
            to=request.query_params.get('to')
            branches=request.query_params.get('branch')
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        
            customer = request.query_params.get('customer')   
        
            kwargs = {}

            # if int(all)==1:
            #     print("all condtion working")
            #     kwargs['type']=1
                
            # if customer:
            #     kwargs['contact']=customer  
            if frm:
                today_min=frm
            if to:
                today_max=to
            if branches:
                kwargs['branches']=branches 
            print("kwargs",kwargs)        
            total_sale = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max),type=2).aggregate(Sum('total_amt'))  
            # sale_data = Invoice.objects.filter(date__range=(today_min, today_max)).aggregate(Sum('total_amt'))
            serializer = IncomeReportSerializer(total_sale, many=True, context={"request": request,"data":kwargs,"datefrom":today_min,"dateto":today_max})
            return Response({'data': serializer.data, 'msg':'Success'},status=status.HTTP_200_OK)


        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    




class SupplierReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]   

    def list(self, request, format=None):
        try:            
            all =request.query_params.get('all')
            frm=request.query_params.get('from')
            to=request.query_params.get('to')
            branches=request.query_params.get('branch')
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        
            supllier = request.query_params.get('supplier')   
        
            kwargs = {}

            if int(all)==1:
                print("all condtion working")
                kwargs['type']=1
                
            if supllier:
                kwargs['contact']=supllier  
            if frm:
                today_min=frm
            if to:
                today_max=to
            if branches:
                kwargs['branches']=branches 
            print("kwargs",kwargs)          
            
            sale_data = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)) 
            serializer = SupplierReportSerializer(sale_data, many=True, context={"request": request,"data":kwargs,"datefrom":today_min,"dateto":today_max})
            return Response({'data': serializer.data, 'msg':'Success'},status=status.HTTP_200_OK)


        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class DebtorsReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]     

    def list(self, request, format=None):
        try:           
            all =request.query_params.get('all')
            frm=request.query_params.get('from')
            to=request.query_params.get('to')
            branches=request.query_params.get('branch')
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        
            customer = request.query_params.get('customer')   
        
            kwargs = {}

            if int(all)==1:
                print("all condtion working")
                kwargs['type']=2
                
            if customer:

                kwargs['contact']=customer  
            if frm:
                today_min=frm
            if to:
                today_max=to
            if branches:
                kwargs['branches']=branches  

            print("kwargs=",kwargs)         
            
            sale_data = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max),).exclude(contact__isnull=True) 
            print(sale_data.query)

            serializer = DebtorsReportSerializer(sale_data, many=True, context={"request": request,"data":kwargs,"datefrom":today_min,"dateto":today_max})
            return Response({'data': serializer.data, 'msg':'Success'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)