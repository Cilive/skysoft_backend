
from rest_framework import  serializers
from company.models import  FuelMaster,Invoice, MeterReading, VatMaster
from shared_tenant.models import Company, Employee
from django.db.models import Q
from shared_tenant.serielizer import EmployeeSerializer





class InvoiceGenerateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = '__all__'
        # fields = ('id', 'invoice_no','gross_amt','fuel','qty','type' )
    
  
     
    def save(self):
        last_invoice = Invoice.objects.filter(Q(type=2) ).order_by('id').last()
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

        emp=Employee.objects.get(user=self.context['request'].user)
     
        invoice = Invoice(
            **self.validated_data,
            invoice_no=new_invoice_int,
            emp = Employee.objects.get(user=self.context['request'].user),
            company = Company.objects.get(id=emp.company_id)         
        )
        invoice.save()   
        self.instance = invoice
        return self.instance
      
 


class MeterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = '__all__'
    

    def save(self):
        emp=Employee.objects.get(user=self.context['request'].user)

        meter_reading = MeterReading(
            **self.validated_data,
            company =Company.objects.get(id=emp.company_id)        
        )
        meter_reading.save()
        return meter_reading

class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = '__all__'


