from django.db import models
from datetime import date

class InterestTable(models.Model):
    class Meta:
        permissions = [('can_create', 'Can Create'),('can_verify', 'Can Verify')]
    name=models.CharField(max_length=25)

    def __str__(self):
        return str(self.id)+" "+self.name


class InterestTableVersion(models.Model):

    name = models.ForeignKey(InterestTable,on_delete=models.CASCADE)
    interest_rate = models.FloatField()
    applicable_from=models.DateField()
    def __str__(self):
        return str(self.id)


class Scheme(models.Model):
    code=models.CharField(max_length=5)
    name=models.CharField(max_length=100)
    interest_applicable_choices=[('Y','YES'),('N','NO')]
    interest_debit_applicable=models.CharField(max_length=1,choices=interest_applicable_choices)
    interest_credit_applicable = models.CharField(max_length=1, choices=interest_applicable_choices)
    interest_debit_table=models.ForeignKey(to=InterestTable,on_delete=models.CASCADE,blank=True,null=True)
    interest_credit_table = models.ForeignKey(to=InterestTable,related_name='creditinterst_table', on_delete=models.CASCADE,null=True,blank=True)
    frequency_choices=[('M','Monthly'),('H','Half Yearly'),('Y','Yearly')]
    frequency=models.CharField(max_length=1,choices=frequency_choices)
    interest_account_choices = [('S', 'Same Account'), ('O', 'Other Account')]
    debit_interest_account=models.CharField(max_length=1,choices=interest_account_choices,blank=True,null=True)
    credit_interest_account = models.CharField(max_length=1,choices=interest_account_choices,blank=True,null=True)
    def __str__(self):
        return str(self.id) + " " +self.name


class AccountHeads(models.Model):
    name = models.CharField(max_length=100)
    category=models.ForeignKey(to='self',null=True,blank=True,on_delete=models.CASCADE)
    scheme=models.ForeignKey(to=Scheme,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.name


class CustomerID(models.Model):
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100,null=True,blank=True)
    husband_name=models.CharField(max_length=100,null=True,blank=True)
    gender_choices=[('M','Male'),('F','Female')]
    gender=models.CharField(max_length=1,choices=gender_choices)
    customer_types=[('I','Individual'),('A','Artificial Person')]
    customer_type=models.CharField(max_length=1,choices=customer_types)
    residential_address1=models.CharField(max_length=25,null=True,blank=True)
    residential_address2=models.CharField(max_length=25,null=True,blank=True)
    residential_address3 = models.CharField(max_length=25,null=True,blank=True)
    residential_address4 = models.CharField(max_length=25,null=True,blank=True)
    residential_address5 = models.CharField(max_length=25,null=True,blank=True)
    city=models.CharField(max_length=26,null=True,blank=True)
    state_code=models.IntegerField(null=True,blank=True)
    state_name=models.CharField(max_length=25,null=True,blank=True)
    country_code=models.IntegerField(null=True,blank=True)
    country_name=models.CharField(max_length=25,null=True,blank=True)
    pan_number=models.CharField(max_length=10)
    voter_card=models.CharField(max_length=16,null=True,blank=True)
    driving_licence=models.CharField(max_length=16,null=True,blank=True)
    ration_card=models.CharField(max_length=16,null=True,blank=True)
    adhar_number=models.CharField(max_length=16,null=True,blank=True)
    mobile_number1=models.CharField(max_length=10)
    mobile_number2 = models.CharField(max_length=10,null=True,blank=True)
    phone_home=models.CharField(max_length=10,null=True,blank=True)
    phone_office=models.CharField(max_length=10,null=True,blank=True)
    office_address1 = models.CharField(max_length=25,null=True,blank=True)
    office_address2 = models.CharField(max_length=25,null=True,blank=True)
    office_address3 = models.CharField(max_length=25,null=True,blank=True)
    office_address4 = models.CharField(max_length=25,null=True,blank=True)
    office_address5 = models.CharField(max_length=25,null=True,blank=True)
    office_city = models.CharField(max_length=26,null=True,blank=True)
    office_state_code = models.IntegerField(null=True,blank=True)
    office_state_name = models.CharField(max_length=25,null=True,blank=True)
    office_country_code = models.IntegerField(null=True,blank=True)
    office_country_name = models.CharField(max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id) + " " +self.name



class Account(models.Model):
    name=models.CharField(max_length=100)
    head=models.ForeignKey(to=AccountHeads,on_delete=models.CASCADE,null=False,blank=False)
    customer_id=models.ForeignKey(to=CustomerID,on_delete=models.CASCADE,null=True,blank=True)
    yes_no_choices = [('Y', 'YES'), ('N', 'NO')]
    system_account=models.CharField(max_length=1,choices=yes_no_choices)

    def __str__(self):
        if self.head.scheme!=None:
            return self.name + " " + str(self.head.scheme.name)+ " "+ str(self.head.scheme.code)
        else:
            return self.name

class Transaction(models.Model):
    transaction_id=models.IntegerField()
    value_date=models.DateField(default=date.today())
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    debit_credit_choices=[('D','Debit'),('C','Credit')]
    debit_credit =models.CharField(max_length=1,choices=debit_credit_choices)
    amount=models.FloatField()
    narration=models.CharField(max_length=100)
    transaction_types=[('IN','Interest'),('LD','Loan Disbursement'),('CW','Cash Withdrwal'),('EM','EMI Payments'),('DP','Cash Deposit')]
    transaction_type=models.CharField(max_length=2,choices=transaction_types)
    def __str__(self):
        return str(self.transaction_id)


