from django.db import models

class Car(models.Model):
    class Meta():
        db_table = 'cars'
    car_number = models.CharField('Гос.номер',max_length=16,unique=True)
    car_model = models.CharField('Марка',max_length=64,unique=True)

    def __str__(self):
        return "%s %s" % (self.car_model,self.car_number)

class Tenant(models.Model):
    class Meta():
        db_table = 'tenants'
    sname =  models.CharField('Фамилия',max_length=64,unique=True)
    fname =  models.CharField('Имя',max_length=64,unique=True)
    mname =  models.CharField('Отчество',max_length=64,unique=True)

    def __str__(self):
        return "%s %s %s" % (self.sname,self.fname,self.mname)

class TenanceLog(models.Model):
    PLACES = (
    ('Par', 'Парковый'),
    ('Bal', 'Балатово'),
    ('Cro', 'Крохалева'),
    ('Cnt', 'Центр'),
    ('Mot', 'Мотовилиха'),
    ('Zak', 'Закамск'),
    )
    class Meta():
        db_table = 'tenance_log'
    car = models.ForeignKey(Car, to_field='car_number', verbose_name='Автомобиль', on_delete=models.DO_NOTHING,related_name='+')
    #c_model = models.ForeignKey(Car, to_field='car_model', verbose_name='Марка', on_delete=models.DO_NOTHING,related_name='+')
    t_fio =  models.ForeignKey(Tenant, to_field='sname', verbose_name='ФИО', on_delete=models.DO_NOTHING,related_name='+')
    #f_name =  models.ForeignKey(Tenant, to_field='fname', verbose_name='Имя',  on_delete=models.DO_NOTHING,related_name='+')
    #m_name =  models.ForeignKey(Tenant, to_field='mname', verbose_name='Отчество', on_delete=models.DO_NOTHING,related_name='+')
    start_dt = models.DateTimeField(null=True,auto_now_add=True,verbose_name='Дата аренды')
    end_dt = models.DateTimeField(null=True,auto_now=True,verbose_name='Дата возврата')
    start_place = models.CharField(null=True,verbose_name='Точка аренды',max_length=3, choices=PLACES)
    end_place = models.CharField(null=True,verbose_name='Точка возврата',max_length=3, choices=PLACES)

    def __str__(self):
        return "%s %s" % (self.car,self.t_fio)
