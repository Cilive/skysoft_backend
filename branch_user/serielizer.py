from django.db.models import Q
from rest_framework import  serializers

from company.models import BankAccountMaster, Contact, Deposit, Dispence, FuelMaster, Invoice, Owner, VatMaster
from shared_tenant.models import BranchManager, Branches, Company



class CustomerCraeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
    def save(self):
        manger=BranchManager.objects.get(user=self.context['request'].user)
        print("company=",manger.branches_id)
        company = Company.objects.get(id=manger.company_id)
        print("company=",company)

        conatct = Contact(
            **self.validated_data,
            company = Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id)        )
        conatct.save()
        return conatct
  

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
 

class InvoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        
    def save(self):
        print("bank account serielizer running",self.context['data']['type'])
     
        type=self.context['data']['type']
        print("type=",type)
        last_invoice = Invoice.objects.filter(Q(type=type) ).order_by('id').last()
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
        manger=BranchManager.objects.get(user=self.context['request'].user)


        company = Company.objects.get(id=manger.company_id)
        try:
          vat=VatMaster.objects.get(company=company)
        except VatMaster.DoesNotExist:
           vat = None

       
        invoice = Invoice(
            **self.validated_data,
            invoice_no=new_invoice_int,
            company =Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id),
            vat=vat
            
        )
        invoice.save()
        print("===============invoice created succesfully==========",invoice.id)
        self.instance = invoice
        return self.instance
      


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['date','qty','payment_type','fuel']



class VatRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VatMaster
        fields = '__all__'

    def save(self):
        manger=BranchManager.objects.get(user=self.context['request'].user)        
        # print(type(self.validated_data['vat']))
        vat = VatMaster(
            **self.validated_data,
            company =Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id),

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
        manger=BranchManager.objects.get(user=self.context['request'].user)        

        fuel = FuelMaster(
            name = self.validated_data['name'],
            fuel_vat = self.validated_data['fuel_vat'],
            company =Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id),
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

class BankCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountMaster
        fields = '__all__'
        
    def save(self):
        manger=BranchManager.objects.get(user=self.context['request'].user)        


        bank = BankAccountMaster(
            **self.validated_data,
            company =Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id),
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


class OwnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

    def save(self):
        manger=BranchManager.objects.get(user=self.context['request'].user)        


        if Owner.objects.filter(phone=self.validated_data['phone']).exists():
            raise serializers.ValidationError({'error':'This phone number is already been used'})

        if Owner.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'This email is already exist'})

        owner = Owner(
            **self.validated_data,
            company =Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id),
        )
        owner.save()
        return owner
class OwnerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

    def save(self):       
        manger=BranchManager.objects.get(user=self.context['request'].user)        


        owner = Owner(
            **self.validated_data,
            company =Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id),
        )
        owner.save()
        return owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
    


class DepositCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Deposit
        fields = '__all__'
    
    def save(self):
        manger=BranchManager.objects.get(user=self.context['request'].user)        


        deposit = Deposit(
            amount =self.validated_data['amount'],
            date = self.validated_data['date'],
            owner = self.validated_data['owner'],
            company =Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id),
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
        manger=BranchManager.objects.get(user=self.context['request'].user)        

        dispence = Dispence(
            **self.validated_data,
            company =Company.objects.get(id=manger.company_id),
            branches = Branches.objects.get(id=manger.branches_id),
        )
        dispence.save()
        self.instance = dispence
        return self.instance

class DispenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispence
        fields = '__all__'
