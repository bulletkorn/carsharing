"""db_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from db_manage.models import Car,Tenant,TenanceLog
from form_test import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cars/$', ListView.as_view(queryset=Car.objects.all().order_by("car_model")[:30],template_name="form_test/cars.html"),name='cars_list'),
    url(r'^tenants/$', ListView.as_view(queryset=Tenant.objects.all().order_by("sname")[:30],template_name="form_test/tenants.html"),name='tenants_list'),
    url(r'^history/$', ListView.as_view(queryset=TenanceLog.objects.all().order_by("car")[:30],template_name="form_test/tenance_log.html"),name='tenance_log'),
    url(r'^$',views.service,name='service'),
    url(r'^take/',views.car_take,name='car_take'),
    url(r'^return/',views.car_return,name='car_return'),
    url(r'^add_tenant/',views.tenant_add,name='tenant_add'),
    url(r'^add_car/',views.car_add,name='car_add'),
]
