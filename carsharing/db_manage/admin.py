from django.contrib import admin
from .models import Car,Tenant,TenanceLog

admin.site.register(Car)
admin.site.register(Tenant)
admin.site.register(TenanceLog)
