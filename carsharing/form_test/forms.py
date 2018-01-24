from django.forms import ModelForm
from django import forms
from db_manage.models import TenanceLog,Car,Tenant

class TakeACarForm(ModelForm):
    class Meta():
        model=TenanceLog
        exclude=('end_dt','end_place')

class ReturnACarForm(ModelForm):
    class Meta():
        model=TenanceLog
        exclude=('start_dt','start_place')

class NewTenant(ModelForm):
    class Meta():
        model=Tenant
        exclude=()

class NewCar(ModelForm):
    class Meta():
        model=Car
        exclude=()
