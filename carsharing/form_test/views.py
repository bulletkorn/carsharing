from django.shortcuts import render
from django.http import HttpResponse
from .forms import TakeACarForm,ReturnACarForm,NewCar,NewTenant
#from db_manage.models import TenanceLog

# Create your views here.
def service(request):
    return render(request,'form_test/service.html')

def car_take(request):
    if request.method == 'POST':
        form = TakeACarForm(request.POST)
        if form.is_valid():
            take = form.save(commit=False)
            take.save()
    else:
        form = TakeACarForm()
    return render(request,'form_test/take.html',{'form':form})

def car_return(request):
    if request.method == 'POST':
        form = ReturnACarForm(request.POST)
        if form.is_valid():
            #row = TenanceLog.objects.get(t_fio=form["t_fio"],car=form["car"])
            ret = form.save(commit=False)
            ret.save()
    else:
        form = ReturnACarForm()
    return render(request,'form_test/return.html',{'form':form})

def car_add(request):
    if request.method == 'POST':
        form = NewCar(request.POST)
        if form.is_valid():
            newcar = form.save(commit=False)
            newcar.save()
    else:
        form = NewCar()
    return render(request,'form_test/add_car.html',{'form':form})

def tenant_add(request):
    if request.method == 'POST':
        form = NewTenant(request.POST)
        if form.is_valid():
            newtenant = form.save(commit=False)
            newtenant.save()
    else:
        form = NewTenant()
    return render(request,'form_test/add_tenant.html',{'form':form})

def email(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']
			recipients = ['anton-kornilkov@yandex.ru']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recipients.append(sender)
			try:
				send_mail(subject, message, 'anton-kornilkov@yandex.ru', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return HttpResponseRedirect('/contacts/thanks/')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'contacts/feedback.html', {'form': form})
