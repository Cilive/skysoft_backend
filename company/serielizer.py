
from django.db import models
from django.db.models.aggregates import Sum
from django.db.models.fields import CharField
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ChoiceField
from client.models import Client, Domain
from rest_framework import  serializers
from rest_framework.response import Response
from django.db.models import Q



from company.models import BankAccountMaster,  Contact,  Deposit, Dispence, Expense, FuelMaster,  Invoice, Owner, PaymentOut,  VatMaster
from shared_tenant.models import Company, Employee
from shared_tenant.serielizer import CompanySerializer, EmployeeRegistrationSerializer



class CustomerCraeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
    def save(self):
        conatct = Contact(
            **self.validated_data,
            company = Company.objects.get(user=self.context['request'].user)
        )
        conatct.save()
        return conatct
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['company'] = CompanySerializer(instance.bank).data
    #     return response

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class VatRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VatMaster
        fields = '__all__'

    def save(self):
        # print(type(self.validated_data['vat']))
        vat = VatMaster(
            **self.validated_data,

            company = Company.objects.get(user=self.context['request'].user)
        )
        vat.save()
        return vat


class VatSerializer(serializers.ModelSerializer):
    class Meta:
        model = VatMaster
        fields = '__all__'


class FuelRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelMaster
        exclude = ('rate','payable_amt')
        
    def save(self):
        print(Company.objects.get(user=self.context['request'].user))
        fuel = FuelMaster(
            name = self.validated_data['name'],
            fuel_vat = self.validated_data['fuel_vat'],
            branches=self.validated_data['branches'],
            company = Company.objects.get(user=self.context['request'].user)
        )
        fuel.save()
        return fuel
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['company'] = CompanySerializer(instance.bank).data
    #     return response

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelMaster
        fields = ('name','fuel_vat','id')


class FuelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelMaster
        fields = ['name','fuel_vat','id','rate','payable_amt']

# class FuelUpdateSerializer(BulkSerializerMixin, serializers.ModelSerializer):
#     class Meta:
#         model = FuelMaster
#         fields = ('rate','payable_amt','id')
#         list_serializer_class = BulkListSerializer
    



# class SaleCreateSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Sale
#         fields = ['fuel', 'liter', 'total_amt','customer']
    
 
#     def save(self):
#         sale = Sale(
#             **self.validated_data,
#             company = Company.objects.get(user=self.context['request'].user)
#         )
#         sale.save()
#         return sale
#         # try:
#             # # print("save function working sucesfully")
#             # customer = Customer.objects.get(id=3)
#             # company = Company.objects.get(user=self.context['request'].user)
#             # print(customer,"comapny=",company)
#             # # sale = Sale(
#             # #     **self.validated_data,
#             # #    #  customer = Customer.objects.get(id=self.validated_data['customer']),
#             # #     customer = Customer.objects.get(id=3),
#             # #     company = Company.objects.get(user=self.context['request'].user)
#             # #    #  company = Company.objects.get(user=3)
#             # #     )
#             # print(self.validated_data)
#             # print(self.context['request'].user)
#             # sale = Sale(
#             #     **self.validated_data,
#             #     customer = Customer.objects.get(id=self.validated_data['customer']),
#             #     # customer = Customer.objects.get(id=3),
#             #     company = Company.objects.get(user=self.context['request'].user)
#             #    #  company = Company.objects.get(user=3)
#             #     )
#             # print(sale)

#             # sale.save()
#             # return sale
#         # except:
#         #      Response({'errors':serializers.Serializer.ValueError,'msg':'Invalid data'})



class BankCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountMaster
        fields = '__all__'
        
    def save(self):
        bank = BankAccountMaster(
            **self.validated_data,
            company = Company.objects.get(user=self.context['request'].user)
        )
        bank.save()
        return bank
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['company'] = CompanySerializer(instance.bank).data
    #     return response

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountMaster
        fields = '__all__'
class ExpenseCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = '__all__'
        
    def save(self):
        expense = Expense(
            **self.validated_data,
            company = Company.objects.get(user=self.context['request'].user)
        )
        expense.save()
        return expense
        
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['bank'] = BankSerializer(instance.bank).data
    #     response['company'] = CompanySerializer(instance.bank).data
    #     return response
    
class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = '__all__'

class OwnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

    def save(self):

        if Owner.objects.filter(phone=self.validated_data['phone']).exists():
            raise serializers.ValidationError({'error':'This phone number is already been used'})

        if Owner.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'This email is already exist'})

        owner = Owner(
            **self.validated_data,
            company = Company.objects.get(user=self.context['request'].user)
        )
        owner.save()
        return owner

class OwnerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

    def save(self):       

        owner = Owner(
            **self.validated_data,
            company = Company.objects.get(user=self.context['request'].user)
        )
        owner.save()
        return owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model =     Owner
        fields = '__all__'
    


class DepositCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Deposit
        fields = '__all__'
    
    def save(self):
        deposit = Deposit(
            amount =self.validated_data['amount'],
            date = self.validated_data['date'],
            owner = self.validated_data['owner'],
            company = Company.objects.get(user=self.context['request'].user)
        )
        
        deposit.save()
        return deposit
        
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['company'] = CompanySerializer(instance.bank).data
    #     return response
class DepositSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Deposit
        fields = '__all__'


class DispenceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispence
        fields = '__all__'
    def save(self):
        dispence = Dispence(
            **self.validated_data,
            company = Company.objects.get(user=self.context['request'].user)
        )
        dispence.save()
        self.instance = dispence
        return self.instance

class DispenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispence
        fields = '__all__'



class InvoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        
    def save(self):
        print("bank account serielizer running",self.context['data']['type'])
        print("Branches in  serielizer running",self.context['data']['branches'])
     
        type=self.context['data']['type']
        branch=self.context['data']['branches']
        print("type=",type)
        # last_invoice = Invoice.objects.filter(Q(type=type) ).order_by('id').last()
        last_invoice = Invoice.objects.filter(type=2 ).order_by('id').last()
        print("last invoice",last_invoice.invoice_no)
        if not last_invoice:
            new_invoice_int= 1
        else:
            invoice_no = last_invoice.invoice_no
            invoice_int = int(invoice_no)
            new_invoice_int = invoice_int + 1
      
        print(last_invoice)
        print("New invocie number",new_invoice_int)
        print(self.validated_data)


        company = Company.objects.get(user=self.context['request'].user)
        try:
          vat=VatMaster.objects.get(company=company,branches=branch)
        except VatMaster.DoesNotExist:
           vat = None

       
        invoice = Invoice(
            **self.validated_data,
            invoice_no=new_invoice_int,
            company = Company.objects.get(user=self.context['request'].user),
            vat=vat
            
        )
        invoice.save()
        print("===============invoice created succesfully==========",invoice.id)
        
        # for fuel in fuels:
           
        #     print("fuel loop",fuel)
        #     fuel_obj=FuelMaster.objects.filter(id = fuel), 

        #     print("fue object in fuel master",fuel_obj)

        #     invoice_line = InvoiceLines(
        #     fuel=fuel_obj.id
        #     )
        #     invoice_line.save

        # fuel_obj=FuelMaster.objects.filter(pk__in=fuels), 
        # print("fuel objects=",fuel_obj)
        # invoice_id=invoice.id
        # print("invoice id after save and befor loop",invoice_id)
        
        # for each in fuel_obj:
        #     print("each fuel object",each[1])
        #     for obj in each:
        #         invoice_line=InvoiceLines(
        #         fuel=obj,
        #         invoice=Invoice.objects.get(id=invoice_id),
        #         liter=10

        #         )
            
        #         invoice_line.save()

      
        # for fuel in fuels:           
        #     print("fuel loop",fuel)
        #     fuel_obj=FuelMaster.objects.filter(id = fuel), 
        #     for each in fuel_obj:
        #        invoice_line=InvoiceLines()
        #        invoice_line.fuel=each
        #        invoice_line.save()

        return invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['date','qty','payment_type','fuel','paid_amt']




class ReciptCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        
    def save(self):
        print("bank account serielizer running",self.context['data']['type'])
        print("bank account serielizer running",self.context['data']['branches'])
        type=self.context['data']['type']
        branch=self.context['data']['branches']

        print("type=",type)
        last_invoice = Invoice.objects.filter(type=1).order_by('id').last()
        print("last invoice",last_invoice.invoice_no)
        if not last_invoice:
            return 1
        invoice_no = last_invoice.invoice_no
        invoice_int = int(invoice_no)
        new_recipt_int = invoice_int + 1
        print(last_invoice)
        print("New invocie number",new_recipt_int)
        print(self.validated_data)



        company = Company.objects.get(user=self.context['request'].user)
        try:
          vat=VatMaster.objects.get(company=company,branches=branch)
        except VatMaster.DoesNotExist:
           vat = None

        try:
            print("checking is there a bank account")
            bank=BankAccountMaster.objects.get(company=company,branches=branch)
            print("bank object",bank)
        except BankAccountMaster.DoesNotExist:
            bank = None

        invoice = Invoice(
            **self.validated_data,
            invoice_no=new_recipt_int,
            company = Company.objects.get(user=self.context['request'].user), 
            bank=bank     ,      
            vat=vat

        )
        invoice.save()
        return invoice
    
    
class ReciptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class ReciptUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['date','qty','payment_type','fuel']


class SaleReportSerializer(serializers.ModelSerializer):
    # payment_type = ChoiceField(choices=Invoice.PAYMENT_TYPE)
    payment_type = serializers.ChoiceField(choices=Invoice.PAYMENT_TYPE)
    type = ChoiceField(choices=Invoice.TYPE)
    class Meta:
        model = Invoice
        fields = '__all__'
    
    def to_representation(self, instance):
        print("data from view ",self.context['dateto'])
        self.context['request'].user
        response = super().to_representation(instance)
        company_data=CompanySerializer(instance.company).data
        customer_data=CustomerSerializer(instance.contact).data
        kwargs=self.context['data']
        today_min=self.context['datefrom']
        today_max=self.context['dateto']
        gross_amt_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('gross_amt'))  
        net_amount_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('total_amt'))  
        # net_amount = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('net_amount'))  
        print(gross_amt_sum)
        print(net_amount_sum)

        # ids=InvoiceSerializer(instance.id).data
        # print(ids.id)
        # gross_amt_sum=Invoice.objects.filter(instance).aggregate(Sum('gross_amt')) 
        # print("GROSS AMOUNT data",gross_amt_sum)
        fuel=FuelSerializer(instance.fuel).data
        if instance.payment_type=='1':
            response['payment_type']='Cash'        
        try:
            response['company'] = company_data['user']['username']      
            response['fuel']=fuel['name']
            response['contact']=customer_data['en_name']
            response['UOM']="Ltr"
            response['gross_amt_sum']=gross_amt_sum['gross_amt__sum']
            response['net_amount_sum']=net_amount_sum['total_amt__sum']

        except TypeError:
            pass       
        
        return response


class EmployeeSaleReportSerializer(serializers.ModelSerializer):
    payment_type = serializers.ChoiceField(choices=Invoice.PAYMENT_TYPE)
    type = ChoiceField(choices=Invoice.TYPE)
    class Meta:
        model = Invoice
        fields = '__all__'
    
    def to_representation(self, instance):
        # print("data from view ",self.context['dateto'])
        self.context['request'].user
        response = super().to_representation(instance)
        company_data=CompanySerializer(instance.company).data
        # customer_data=CustomerSerializer(instance.contact).data
        kwargs=self.context['data']
        today_min=self.context['datefrom']
        today_max=self.context['dateto']
        gross_amt_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('gross_amt'))  
        net_amount_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('total_amt'))  
        # net_amount = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('net_amount'))  
        # print(gross_amt_sum)
        # print(net_amount_sum)

       
        fuel=FuelSerializer(instance.fuel).data
        if instance.payment_type=='1':
            response['payment_type']='Cash'        
        try:
            response['company'] = company_data['user']['username']      
            response['fuel']=fuel['name']
            # response['contact']=customer_data['en_name']
            response['UOM']="Ltr"
            response['gross_amt_sum']=gross_amt_sum['gross_amt__sum']
            response['net_amount_sum']=net_amount_sum['total_amt__sum']

        except TypeError:
            pass       
        
        return response
            
            

class PurchaseReportSerializer(serializers.ModelSerializer):
    # payment_type = ChoiceField(choices=Invoice.PAYMENT_TYPE)
    payment_type = serializers.ChoiceField(choices=Invoice.PAYMENT_TYPE)
    type = ChoiceField(choices=Invoice.TYPE)
    class Meta:
        model = Invoice
        fields = '__all__'
    
    def to_representation(self, instance):
        print("data from view ",self.context['dateto'])
        self.context['request'].user
        response = super().to_representation(instance)
        company_data=CompanySerializer(instance.company).data
        customer_data=CustomerSerializer(instance.contact).data
        kwargs=self.context['data']
        today_min=self.context['datefrom']
        today_max=self.context['dateto']
        gross_amt_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('gross_amt'))  
        net_amount_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('total_amt'))  
        # net_amount = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('net_amount'))  
        print(gross_amt_sum)
        print(net_amount_sum)

        
        fuel=FuelSerializer(instance.fuel).data
        if instance.payment_type=='1':
            response['payment_type']='Cash'        
        try:
            response['company'] = company_data['user']['username']      
            response['fuel']=fuel['name']
            response['contact']=customer_data['en_name']
            response['UOM']="Ltr"
            response['gross_amt_sum']=gross_amt_sum['gross_amt__sum']
            response['net_amount_sum']=net_amount_sum['total_amt__sum']

        except TypeError:
            pass       
        
        return response


class IncomeReportSerializer(serializers.ModelSerializer):
    # payment_type = ChoiceField(choices=Invoice.PAYMENT_TYPE)
    class Meta:
        model = Invoice
        fields = ['total_amt']
    
    def to_representation(self, instance):
        print("data from view ",self.context['dateto'])
        self.context['request'].user
        response = super().to_representation(instance)
        # company_data=CompanySerializer(instance.company).data
        # customer_data=CustomerSerializer(instance.contact).data
        kwargs=self.context['data']
        today_min=self.context['datefrom']
        today_max=self.context['dateto']
        total_sale = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max),type=2).aggregate(Sum('total_amt'))  
        total_purchase = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max),type=1).aggregate(Sum('total_amt'))  
        # net_amount = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('net_amount'))  
        print("sale=",total_sale)
        print("sale=",total_sale['total_amt__sum'])
        income=float(total_purchase['total_amt__sum'])-float(total_sale['total_amt__sum'])
        print("purchase",total_purchase)

        # ids=InvoiceSerializer(instance.id).data
        # print(ids.id)
        # gross_amt_sum=Invoice.objects.filter(instance).aggregate(Sum('gross_amt')) 
        # print("GROSS AMOUNT data",gross_amt_sum)
        # fuel=FuelSerializer(instance.fuel).data
        # if instance.payment_type=='1':
        #     response['payment_type']='Cash'        
        try:
            response['sale'] = total_sale     
            # response['fuel']=fuel['name']
            response['purchase']=total_purchase
            response['income']=income
            # response['UOM']="Ltr"
            # response['gross_amt_sum']=gross_amt_sum['gross_amt__sum']
            # response['net_amount_sum']=net_amount_sum['total_amt__sum']

        except TypeError:
            pass       
        
        return response




class supplierStatementReportSerializer(serializers.ModelSerializer):
    # payment_type = ChoiceField(choices=Invoice.PAYMENT_TYPE)
  
    class Meta:
        model = Invoice
        fields = '__all__'
    
    def to_representation(self, instance):
        print("data from view ",self.context['dateto'])
        self.context['request'].user
        response = super().to_representation(instance)
        company_data=CompanySerializer(instance.company).data
        customer_data=CustomerSerializer(instance.contact).data
        kwargs=self.context['data']
        today_min=self.context['datefrom']
        today_max=self.context['dateto']
        gross_amt_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('gross_amt'))  
        net_amount_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('total_amt'))  
        # net_amount = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('net_amount'))  
        print(gross_amt_sum)
        print(net_amount_sum)        
        fuel=FuelSerializer(instance.fuel).data
        if instance.payment_type=='1':
            response['payment_type']='Cash'        
        try:
            response['company'] = company_data['user']['username']      
            response['fuel']=fuel['name']
            response['contact']=customer_data['en_name']
            response['UOM']="Ltr"
            response['gross_amt_sum']=gross_amt_sum['gross_amt__sum']
            response['net_amount_sum']=net_amount_sum['total_amt__sum']

        except TypeError:
            pass              
        return response


class SupplierReportSerializer(serializers.ModelSerializer):
    # payment_type = ChoiceField(choices=Invoice.PAYMENT_TYPE)
    payment_type = serializers.ChoiceField(choices=Invoice.PAYMENT_TYPE)
    type = ChoiceField(choices=Invoice.TYPE)
    class Meta:
        model = Invoice
        fields = '__all__'
    
    def to_representation(self, instance):
        print("data from view ",self.context['dateto'])
        self.context['request'].user
        response = super().to_representation(instance)
        company_data=CompanySerializer(instance.company).data
        customer_data=CustomerSerializer(instance.contact).data
        kwargs=self.context['data']
        today_min=self.context['datefrom']
        today_max=self.context['dateto']
        gross_amt_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('gross_amt'))  
        net_amount_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('total_amt'))  
        # net_amount = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('net_amount'))  
        print(gross_amt_sum)
        print(net_amount_sum)

        
        fuel=FuelSerializer(instance.fuel).data
        if instance.payment_type=='1':
            response['payment_type']='Cash'        
        try:
            response['company'] = company_data['user']['username']      
            response['fuel']=fuel['name']
            response['contact']=customer_data['en_name']
            response['UOM']="Ltr"
            response['gross_amt_sum']=gross_amt_sum['gross_amt__sum']
            response['net_amount_sum']=net_amount_sum['total_amt__sum']

        except TypeError:
            pass       
        
        return response


class DebtorsReportSerializer(serializers.ModelSerializer):
    # payment_type = ChoiceField(choices=Invoice.PAYMENT_TYPE)
    payment_type = serializers.ChoiceField(choices=Invoice.PAYMENT_TYPE)
    type = ChoiceField(choices=Invoice.TYPE)
    class Meta:
        model = Invoice
        fields = '__all__'
    
    def to_representation(self, instance):
        print("data from view ",self.context['dateto'])
        self.context['request'].user
        response = super().to_representation(instance)
        company_data=CompanySerializer(instance.company).data
        customer_data=CustomerSerializer(instance.contact).data
        kwargs=self.context['data']
        today_min=self.context['datefrom']
        today_max=self.context['dateto']
        gross_amt_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('gross_amt'))  
        net_amount_sum = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('total_amt'))  
        # net_amount = Invoice.objects.filter(**kwargs,date__range=(today_min, today_max)).aggregate(Sum('net_amount'))  
        print(gross_amt_sum)
        print(net_amount_sum)

        # ids=InvoiceSerializer(instance.id).data
        # print(ids.id)
        # gross_amt_sum=Invoice.objects.filter(instance).aggregate(Sum('gross_amt')) 
        # print("GROSS AMOUNT data",gross_amt_sum)
        fuel=FuelSerializer(instance.fuel).data
        if instance.payment_type=='1':
            response['payment_type']='Cash'        
        try:
            response['company'] = company_data['user']['username']      
            response['fuel']=fuel['name']
            response['contact']=customer_data['en_name']
            response['UOM']="Ltr"
            response['gross_amt_sum']=gross_amt_sum['gross_amt__sum']
            response['net_amount_sum']=net_amount_sum['total_amt__sum']

        except TypeError:
            pass       
        
        return response
