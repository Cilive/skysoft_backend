from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from employee.serielizer import  InvoiceGenerateSerializer, MeterCreateSerializer, MeterSerializer
from employee.permissions import IsEmployee
from company.models import MeterReading
from shared_tenant.models import Company, Employee


class EmployeeInvoiceViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsEmployee]
    
    def create(self, request):
        try:
            serializer = InvoiceGenerateSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():

                print("valid condition working")
                serializer.save()
                print("seirlizer after print",serializer.data)
                return Response({'msg':'sale added succesfully', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
  
# class GetAmount(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         try:
#             # vat = VatMaster.objects.values_list('vat').first()
#             # print("function working",request.query_params)
#             fuel = request.query_params.get('fuel')
#             print(fuel)
#             liter = request.query_params.get('liter')
#             print(liter)            
          
#             fuel_data = FuelMaster.objects.get(id=fuel)
#             # fuel_data = FuelMaster.objects.filter(id=fuel)
#             print("fuel=",fuel_data)            
#             # print("fuel=",FuelMaster.__dict__)            
#             serializer = FuelSerializer(fuel_data)
#             # amt = (vat + serializer.data.get('fuel_vat') + serializer.data.get('rate')) * liter
#             # 
#             amt = (serializer.data.get('vat') + serializer.data.get('fuel_vat') + serializer.data.get('rate'))* float(liter)
#             #  
#             return Response({'data': amt, 'data':amt},status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)






class MeterReadingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        try:
            serializer = MeterCreateSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        try:
            emp=Employee.objects.get(user=request.user)
            print(emp)
            meter_reading = MeterReading.objects.filter(company=Company.objects.get(id=emp.company_id))
            serializer = MeterSerializer(meter_reading, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except  Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            meter_reading = MeterReading.objects.filter(pk=pk)
            if not meter_reading:
                return  Response({'message':"Meter Reading not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = MeterSerializer(meter_reading[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            meter_reading = MeterReading.objects.filter(pk=pk)
            if not meter_reading:
                return  Response({'message':"Meter Reading not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = MeterSerializer(meter_reading[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            meter_reading = MeterReading.objects.filter(pk=pk)
            if not meter_reading:
                return  Response({'message':"Meter Reading not found"},status=status.HTTP_404_NOT_FOUND)
            meter_reading[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
 