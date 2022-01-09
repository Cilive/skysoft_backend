from django.db import models
from shared_tenant.models import Branches, Company, Employee


# Create your models here.

    


class VatMaster(models.Model):
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    vat = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'vat_master'

class FuelMaster(models.Model):
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    fuel_vat = models.IntegerField()
    rate = models.FloatField(null=True)
    payable_amt = models.FloatField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'fuel_master'
        
    def __str__(self):
        return str(self.id)








class BankAccountMaster(models.Model):
    # date = models.DateField()
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)
    bank_name = models.CharField(max_length=30)
    acc_holder_name = models.CharField(max_length=30)
    acc_no = models.CharField(max_length=30)
    initial_balance = models.FloatField(null=True)
    balance = models.FloatField(null=True)
    branch = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'bank_account_master'
        
    def __str__(self):
        return self.bank_name


class PaymentOut(models.Model):
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)

    date = models.DateTimeField(auto_now_add=True)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,null=True,verbose_name='supplier')
    bank = models.ForeignKey(BankAccountMaster, on_delete=models.CASCADE,null=True,verbose_name='bank')
    ref_no = models.CharField(max_length=30)
    paid_amt = models.FloatField()
    # balance_amt = models.FloatField() # auto
    paid_type = models.CharField(max_length=30)
    total_amt = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'payment_out'
        
    def __str__(self):
        return str(self.id)

class Expense(models.Model):
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)


    date = models.DateTimeField(auto_now_add=True)
    exp_type = models.CharField(max_length=30)
    bank = models.ForeignKey(BankAccountMaster, on_delete=models.CASCADE,null=True,verbose_name='bank')
    ref_no = models.CharField(max_length=30)
    paid_amt = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'expense'
        
    def __str__(self):
        return str(self.id)


class Owner(models.Model):
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                            null=True)
    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100,unique=True)

class Deposit(models.Model):
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)


    amount = models.FloatField()
    date = models.DateTimeField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    company =  models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'deposit'
        
    def __str__(self):
        return str(self.id)

class Dispence(models.Model):
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)


    name = models.CharField(max_length=30)
    company =  models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'dispence'
        
    def __str__(self):
        return str(self.name)



class MeterReading(models.Model):
    # branch=models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    start_reading = models.FloatField()
    end_reading = models.FloatField()
    # previous_reading = models.FloatField()
    payable_amt = models.FloatField()
    # liter = models.FloatField() # auto
    # stock = models.FloatField() # auto
    dispence =  models.ForeignKey(Dispence, on_delete=models.CASCADE,
                            null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                            null=True, related_name='meter_reading_company')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'meter_reading'
        
    def __str__(self):
        return str(self.date)



class Contact(models.Model):
    USER_CHOICES = (
    ("1", "customer"),
    ("2", "supplier"),   
    )

    en_name = models.CharField(max_length=30)
    ar_name = models.CharField(max_length=30)
    en_place = models.CharField(max_length=30)
    ar_place = models.CharField(max_length=30)
    en_district = models.CharField(max_length=30)
    ar_district = models.CharField(max_length=30)
    vat_no = models.CharField(max_length=15)
    lan_no = models.CharField(max_length=15)
    mobile_no = models.CharField(max_length=15,unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=15,choices = USER_CHOICES,default = '1')
    class Meta:
        db_table = 'contact'
    def __str__(self):
        return self.en_name




class Invoice(models.Model):
    PAYMENT_TYPE = (
    ("1", "CASH"),
    ("2", "BANK"),   
    ("3", "CREDIT"),   
    )
    TYPE = (
    ("1", "in_invoice"),
    ("2", "out_invoice"),   
    )

    invoice_no = models.BigIntegerField( null=True, blank=True,default=None)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,null=True,verbose_name='contact',blank=True)

    emp = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True,verbose_name='employee',blank=True)
    date = models.DateTimeField(auto_now_add=True)
    fuel = models.ForeignKey(FuelMaster, on_delete=models.CASCADE,null=True,verbose_name='fuel')
    qty = models.FloatField() 
    gross_amt = models.FloatField(null=True, blank=True) # auto
    payment_type = models.CharField(max_length=15,choices = PAYMENT_TYPE,default = '1')
    type = models.CharField(max_length=15,choices = TYPE,default = '1')
    total_amt = models.FloatField(null=True, blank=True) # auto
    credit_amount=models.FloatField( null=True, blank=True) 
    account_number=models.CharField(max_length=15,null=True, blank=True)   
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    vat=models.ForeignKey(VatMaster, on_delete=models.CASCADE, null=True)
    bank=models.ForeignKey(BankAccountMaster, on_delete=models.CASCADE, null=True)
    vat_percenatge=models.FloatField( null=True, blank=True) 
    vat_amount=models.FloatField( null=True, blank=True)
    paid_amt= models.FloatField( null=True, blank=True,default=0)
    balance_amt= models.FloatField( null=True, blank=True,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'invoice'
    
    @property
    def get_gross_amt(self):
        gross_amt = self.qty*self.fuel.payable_amt  
        return gross_amt 
    
    @property
    def get_vat_percentage(self):
        if self.vat:
            vat_percentage = self.vat.vat 
        else:
            vat_percentage=0        
        return vat_percentage 
    
    
 
    
    @property
    def get_account_number(self):
        if self.bank:
            account_number = self.bank.acc_no 
        else:
            account_number=None

        return account_number 
    
    
    @property
    def get_total_amount(self):
        common_vat=self.gross_amt*self.vat_percenatge/100
        total=self.gross_amt+common_vat
        return total 

    @property
    def get_vat_amount(self):
        vat_amount=self.gross_amt*self.vat_percenatge/100               
        return vat_amount 
    
    @property
    def get_balance_amt(self):
        # total_amt=
        try:
            balance=0
            print("total amount",self.total_amt)
            print("type ",self.type)
            print("type ",type(self.type))
            if int(self.type)==1:
                print("Its a purchase")
                if self.paid_amt==0:
                    balance=0
                elif self.paid_amt==self.total_amt:
                    balance=0
                else:
                    balance=self.total_amt-self.paid_amt  
            if int(self.type)==2:               
                if self.paid_amt==self.total_amt:
                    balance=0
                else:
                    balance=self.total_amt-self.paid_amt  
        except:
            pass
        
        return balance 




    def save(self, *args, **kwargs):         
            self.gross_amt = self.get_gross_amt
            self.vat_percenatge = self.get_vat_percentage
            self.total_amt = self.get_total_amount
            self.vat_amount = self.get_vat_amount
            self.account_number = self.get_account_number
            self.balance_amt = self.get_balance_amt
            super(Invoice, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.invoice_no)



