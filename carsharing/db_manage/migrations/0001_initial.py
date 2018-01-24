# Generated by Django 2.0.1 on 2018-01-22 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=16, unique=True, verbose_name='Гос.номер')),
                ('car_model', models.CharField(max_length=64, unique=True, verbose_name='Марка')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='TenanceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_dt', models.DateTimeField(auto_now_add=True)),
                ('end_dt', models.DateTimeField()),
                ('start_place', models.CharField(choices=[('Par', 'Parkoviy'), ('Bal', 'Balatovo'), ('Cro', 'Crohaleva'), ('Cnt', 'Centr'), ('Mot', 'Motovilikha'), ('Zak', 'Zakamsk')], max_length=3)),
                ('end_place', models.CharField(choices=[('Par', 'Parkoviy'), ('Bal', 'Balatovo'), ('Cro', 'Crohaleva'), ('Cnt', 'Centr'), ('Mot', 'Motovilikha'), ('Zak', 'Zakamsk')], max_length=3)),
                ('c_model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='db_manage.Car', to_field='car_model', verbose_name='Марка')),
                ('c_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='db_manage.Car', to_field='car_number', verbose_name='Гос.номер')),
            ],
            options={
                'db_table': 'tenance_log',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=64, unique=True, verbose_name='Фамилия')),
                ('fname', models.CharField(max_length=64, unique=True, verbose_name='Имя')),
                ('mname', models.CharField(max_length=64, unique=True, verbose_name='Отчество')),
            ],
            options={
                'db_table': 'tenants',
            },
        ),
        migrations.AddField(
            model_name='tenancelog',
            name='f_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='db_manage.Tenant', to_field='fname', verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='tenancelog',
            name='m_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='db_manage.Tenant', to_field='mname', verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='tenancelog',
            name='s_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='db_manage.Tenant', to_field='sname', verbose_name='Фамилия'),
        ),
    ]
