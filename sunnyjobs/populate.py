import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sunnyjobs.settings')
import django
django.setup()

from faker import Faker
from testapp.models import HydJobs,BngJobs,PuneJobs
from random import *
fake = Faker()#Object creation for Faker class
def phonenumbergen():
	d1 = randint(6,9)
	num = ''+str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('project Manager','Team Lead','Software Engineer','HR','Associate Engineer'))
        faddress = fake.address()
        femail= fake.email()
        fphonenumber = phonenumbergen()
        hyd_jobs_record = HydJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            address = faddress,
            email = femail,
            phonenumber=fphonenumber
        )
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully....')

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('project Manager', 'Team Lead', 'Software Engineer', 'HR', 'Associate Engineer'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        bng_jobs_record = BngJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber
        )
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully....')

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('project Manager', 'Team Lead', 'Software Engineer', 'HR', 'Associate Engineer'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        pune_jobs_record = PuneJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber
        )
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully....')
