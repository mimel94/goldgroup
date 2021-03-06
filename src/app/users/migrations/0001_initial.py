# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 00:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGoldGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('first_surname', models.CharField(max_length=60)),
                ('last_surname', models.CharField(blank=True, max_length=60, null=True)),
                ('type_document', models.CharField(choices=[('CC', 'C\xe9dula de Ciudadan\xeda'), ('TI', 'Tarjeta de Identidad'), ('CE', 'C\xe9dula de Extranjer\xeda'), ('NIT', 'NIT')], max_length=3)),
                ('number_document', models.CharField(max_length=20, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(max_length=20)),
                ('address_residence', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('is_employee', models.BooleanField()),
                ('is_salesman', models.BooleanField()),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('city_residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.City')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='LineCgv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_other', models.CharField(max_length=20)),
                ('bank_account', models.CharField(max_length=50)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Bank')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Code')),
                ('line_cgv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.LineCgv')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de usuario',
                'verbose_name_plural': 'Perfiles de Usuarios',
            },
        ),
    ]
