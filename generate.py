import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudproject.settings')
import django
django.setup()
from crudapp.models import *                                      ### create this file in same as manage.py located (and run separately in cmd like python generate.py)
from faker import Faker
from random import *                                              ##### to generate fake data for huge amount of data creation,testing purpose
faker =Faker()
def generate(n):
    for i in range(n):
        fname=faker.name()
        fage=randint(1,100)
        fcity=faker.city()
        fmarks=randint(30,100)
        student_record=Student.objects.get_or_create(name=fname,age=fage,city=fcity,marks=fmarks)
generate(15)
