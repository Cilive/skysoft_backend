from django.shortcuts import render
from rest_framework import generics,status,views,permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.db import connection






from shared_tenant.serielizer import BranchManagerRegistrationSerializer, BranchManagerSerializer, BranchesRegistrationSerializer, BranchesSerializer, ComapanyTokenObtainPairSerializer, CompanyRegistrationSerializer, CompanySerializer, CompanyUpdationSerializer, EmployeeRegistrationSerializer, EmployeeSerializer, EmployeeUpdateSerializer
from shared_tenant.permissions import IsCompany, IsSuperUser
from .models import BranchManager, Branches, Company, Employee, User
from rest_framework.response import Response



# Create your views here.

class CompanyTokenObtainPairView(TokenObtainPairView):
    serializer_class = ComapanyTokenObtainPairSerializer



class CompanyRegistration(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated,IsSuperUser]
    queryset = Company.objects.all()    
    serializer_class=CompanyRegistrationSerializer
    
    def create(self, request, format=None):
        try:
            serializer = CompanyRegistrationSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'msg':'Invalid data','error':serializer.errors},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'message':"Server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # def get(self):
    #         comapnies=Company.objects.all()
    #         serializer=CompanySerializer(comapnies,many=True)
    #         return Response(serializer.data)
    def list(self, request):
        try:
            comapnies=Company.objects.all()
            serializer = CompanySerializer(comapnies, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            comapany = Company.objects.filter(pk=pk)
            if not comapany:
                return  Response({'message':"Company not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = CompanySerializer(comapany[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk, format=None):
            company=Company.objects.get(id=pk)
            serializer=CompanySerializer(data=request.data)
            serializer = CompanyUpdationSerializer(instance=company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def destroy(self, request, pk=None):
        try:
            print("delete condition working")
            company = Company.objects.filter(pk=pk)
            if not company:
                return  Response({'message':"company not found"},status=status.HTTP_404_NOT_FOUND)
            print(company)
            print(connection.queries)
            company.delete().query
            print(company.query)
            return Response({'msg':'Success'},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)  

# @api_view(['GET'])
# def EmployeeList(self,request):
#         try:
#             employee = Employee.objects.filter(company=Company.objects.get(user=request.user))
#             serializer = EmployeeSerializer(employee, many=True, context={"request": request})
#             return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
#         except  Exception as e:
#             print(e)
#             return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmployeeRegistration(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsCompany]
    queryset = Employee.objects.all()    
    serializer_class=EmployeeRegistrationSerializer


    def list(self,request):
        try:
            employee = Employee.objects.filter(company=Company.objects.get(user=request.user))
            serializer = EmployeeSerializer(employee, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except  Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)


   
    def create(self, request, format=None):
        print("request user from toke",request)
        # user=self.context['request'].user
        print("request user from toke",request.user)
        user=request.user
        co=Company.objects.get(user=user),
        print("user from request",co)
        try:
            serializer = EmployeeRegistrationSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'msg':'Invalid data','error':serializer.errors},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'message':"Server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

    def retrieve(self, request, pk=None):
        try:
            employee = Employee.objects.filter(pk=pk)
            if not employee:
                return  Response({'message':"Employee not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = EmployeeSerializer(employee[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            employee = Employee.objects.filter(pk=pk)
            if not employee:
                return  Response({'message':"Employee not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = EmployeeUpdateSerializer(employee[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk=None):
        try:
            employee = Employee.objects.filter(pk=pk)
            if not employee:
                return  Response({'message':"Employee not found"},status=status.HTTP_404_NOT_FOUND)
            print(connection.queries)
            
            employee[0].delete()
            print(connection.queries)

            return Response({'msg':'Success'},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class BranchesViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Branches.objects.all()    
    serializer_class=BranchesRegistrationSerializer

    def create(self, request, format=None):
        try:
            company = Company.objects.get(user=request.user)
            branch_count = Branches.objects.filter(company=company.id).count()    
            print("branch count",branch_count)            
            if int(branch_count)>=int(company.branch_count):
                    print("cannot add more branches outer serielizer condition")
                    return Response({'msg':'Branch adding limit exceeded', },status.HTTP_201_CREATED)

            else:
                serializer = BranchesRegistrationSerializer(data=request.data, context={"request": request})
                if serializer.is_valid():     
                    serializer.save()
                    return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'msg':'Invalid data','error':serializer.errors},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'message':"Server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        try:
            branch = Branches.objects.filter(company=Company.objects.get(user=request.user))
            serializer = BranchesRegistrationSerializer(branch, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, pk=None):
        try:
            branch = Branches.objects.filter(pk=pk)
            if not branch:
                return  Response({'message':"branch not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = BranchesSerializer(branch[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
   

    def destroy(self, request, pk=None):
        try:
            customer = Branches.objects.filter(pk=pk)
            if not customer:
                return  Response({'message':"branch not found"},status=status.HTTP_404_NOT_FOUND)
            customer[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def retrieve(self, request, pk=None):
        try:
            customer = Branches.objects.filter(pk=pk)
            if not customer:
                return  Response({'message':"Customer not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = BranchesSerializer(customer[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

class BranchMangerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BranchManager.objects.all()    
    serializer_class=BranchManagerRegistrationSerializer

    def create(self, request, format=None):
        try:
            serializer = BranchManagerRegistrationSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_201_CREATED)
            return Response({'msg':'Invalid data','error':serializer.errors},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({'message':"Server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        try:
            branch = BranchManager.objects.filter(company=Company.objects.get(user=request.user))
            serializer = BranchManagerSerializer(branch, many=True, context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, pk=None):
        try:
            branch = BranchManager.objects.filter(pk=pk)
            if not branch:
                return  Response({'message':"branch not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = BranchManagerSerializer(branch[0], data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
            return Response({'errors':serializer.errors,'msg':'Invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            customer = BranchManager.objects.filter(pk=pk)
            if not customer:
                return  Response({'message':"branch not found"},status=status.HTTP_404_NOT_FOUND)
            customer[0].delete()
            return Response({'msg':'Success'},status.HTTP_200_OK)
        
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def retrieve(self, request, pk=None):
        try:
            customer = BranchManager.objects.filter(pk=pk)
            if not customer:
                return  Response({'message':"Customer not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = BranchManagerSerializer(customer[0], context={"request": request})
            return Response({'msg':'Success', 'data':serializer.data},status.HTTP_200_OK)
        except:
            return Response({'msg':'Server error' },status.HTTP_500_INTERNAL_SERVER_ERROR)

