from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics,status


from rest_framework.permissions import IsAuthenticated
from company.models import BankAccountMaster, Contact, Deposit, Dispence, FuelMaster, Invoice, Owner, VatMaster

from .serielizer import BankCreateSerializer, BankSerializer, CustomerCraeteSerializer, CustomerSerializer, DepositCreateSerializer, DepositSerializer, DispenceCreateSerializer, DispenceSerializer, FuelListSerializer, FuelRegistrationSerializer, FuelSerializer, InvoiceCreateSerializer, InvoiceSerializer, InvoiceUpdateSerializer, OwnerCreateSerializer, OwnerSerializer, OwnerUpdateSerializer, VatRegistrationSerializer, VatSerializer
from shared_tenant.models import BranchManager, Branches, Company
from .permissions import (IsManager)




# Create your views here.





class CustomerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
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
            manger=BranchManager.objects.get(user=request.user)

            customer = Contact.objects.filter(company=Company.objects.get(id=manger.company_id), branches=Branches.objects.get(id=manger.branches_id))
            serializer = CustomerSerializer(customer, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            manger=BranchManager.objects.get(user=request.user)

            customer = Contact.objects.filter(pk=pk,company=Company.objects.get(id=manger.company_id), branches=Branches.objects.get(id=manger.branches_id))
            if not customer:
                return  Response({'message':"Customer not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = CustomerSerializer(customer[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            manger=BranchManager.objects.get(user=request.user)

            customer = Contact.objects.filter(pk=pk,company=Company.objects.get(id=manger.company_id), branches=Branches.objects.get(id=manger.branches_id))
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
            customer = Contact.objects.filter(pk=pk)
            if not customer:
                return  Response({'message':"Customer not found"},status=status.HTTP_404_NOT_FOUND)
            customer[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class InvoiceViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        try:
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
            manger=BranchManager.objects.get(user=request.user)
            invoices = Invoice.objects.filter(company=Company.objects.get(id=manger.company_id), branches=Branches.objects.get(id=manger.branches_id))
            serializer = InvoiceSerializer(invoices, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)
            invoice = Invoice.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not invoice:
                return  Response({'message':"invoice not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = InvoiceSerializer(invoice[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            invoice = Invoice.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
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
            manager=BranchManager.objects.get(user=request.user)

            invoice = Invoice.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not invoice:
                return  Response({'message':"invoice not found"},status=status.HTTP_404_NOT_FOUND)
            invoice[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

class VatRegistrationViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
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
            manager=BranchManager.objects.get(user=request.user)

            vat = VatMaster.objects.filter(company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            serializer = VatSerializer(vat, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            supplier = VatMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not supplier:
                return  Response({'message':"Vat not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = VatSerializer(supplier[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            vat = VatMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
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
            manager=BranchManager.objects.get(user=request.user)

            vat = VatMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not vat:
                return  Response({'message':"Vat not found"},status=status.HTTP_404_NOT_FOUND)
            vat[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        




class FuelRegistrationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
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
            manager=BranchManager.objects.get(user=request.user)

            fuel = FuelMaster.objects.filter(company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            serializer = FuelListSerializer(fuel, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)



    def update(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            fuel = FuelMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
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
            manager=BranchManager.objects.get(user=request.user)

            fuel = FuelMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not fuel:
                return  Response({'message':"Fuel not found"},status=status.HTTP_404_NOT_FOUND)
            fuel[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            fuel = FuelMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not fuel:
                return  Response({'message':"Fuel not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = FuelSerializer(fuel[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)


class BankViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
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
            manager=BranchManager.objects.get(user=request.user)

            bank = BankAccountMaster.objects.filter(company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            serializer = BankSerializer(bank, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
 
  

    def update(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            bank = BankAccountMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
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
            manager=BranchManager.objects.get(user=request.user)

            bank = BankAccountMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not bank:
                return  Response({'message':"Bank not found"},status=status.HTTP_404_NOT_FOUND)
            bank[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            bank = BankAccountMaster.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not bank:
                return  Response({'message':"Bank not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = BankSerializer(bank[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class OwnerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
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
            manager=BranchManager.objects.get(user=request.user)

            owner = Owner.objects.filter(company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            serializer = OwnerSerializer(owner, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except  Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            owner = Owner.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
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
            manager=BranchManager.objects.get(user=request.user)

            owner = Owner.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not owner:
                return  Response({'message':"Owner not found"},status=status.HTTP_404_NOT_FOUND)
            owner[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            owner = Owner.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not owner:
                return  Response({'message':"Owner not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = OwnerSerializer(owner[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            




    
class DepositViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
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
            manager=BranchManager.objects.get(user=request.user)
            deposit = Deposit.objects.filter(company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            serializer = DepositSerializer(deposit, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

  

    def update(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            deposit = Deposit.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
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
            manager=BranchManager.objects.get(user=request.user)

            deposit = Deposit.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not deposit:
                return  Response({'message':"Deposit not found"},status=status.HTTP_404_NOT_FOUND)
            deposit[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def retrieve(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            deposit = Deposit.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not deposit:
                return  Response({'message':"Deposit not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = DepositSerializer(deposit[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class DispenceViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsManager]
    
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
            manager=BranchManager.objects.get(user=request.user)

            dispence = Dispence.objects.filter(company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            serializer = DispenceSerializer(dispence, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except  Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            dispence = Dispence.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
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
            manager=BranchManager.objects.get(user=request.user)

            dispence = Dispence.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not dispence:
                return  Response({'message':"Dispence not found"},status=status.HTTP_404_NOT_FOUND)
            dispence[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, pk=None):
        try:
            manager=BranchManager.objects.get(user=request.user)

            dispence = Dispence.objects.filter(pk=pk,company=Company.objects.get(id=manager.company_id), branches=Branches.objects.get(id=manager.branches_id))
            if not dispence:
                return  Response({'message':"Dispence not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = DispenceSerializer(dispence[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)




      
   




