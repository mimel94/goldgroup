# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from app.locations.models import City
from django.utils import timezone
from django.contrib.auth.hashers import make_password
# Create your models here.

choice_document = (
    ('CC', 'Cédula de Ciudadanía'),
    ('TI', 'Tarjeta de Identidad'),
    ('CE', 'Cédula de Extranjería'),
    ('NIT', 'NIT'),
)

choice_gender = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class MyUserGoldGroupManager(BaseUserManager):

    def _create_user(self, email, password=None, admin=False, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener dirección de correo')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.password = make_password(raw_password)
        #user.set_password(password)
        if admin:
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
        user.save(using=self._db)
        return user

    def create(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, admin=True, **extra_fields)


class UserGoldGroup(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    first_surname = models.CharField(max_length=60)
    last_surname = models.CharField(max_length=60, blank=True, null=True)
    type_document = models.CharField(max_length=3, choices=choice_document)
    number_document = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=choice_gender)
    birthdate = models.DateField()
    phone = models.CharField(max_length=20)
    city_residence = models.ForeignKey(City, null=True)
    address_residence = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_salesman = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'number_document'
    REQUIRED_FIELDS =[
        'type_document',
        'first_name',
        'first_surname',
        'gender',
        'birthdate',
        'phone',
        'city_residence',
        'address_residence',
        'email'
    ]

    objects = MyUserGoldGroupManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    #def set_password(self, raw_password):
    #    self.password = make_password(raw_password)

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.first_surname)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()

    def __unicode__(self):
        return u'{0}'.format(self.get_full_name())


class Bank(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Code(models.Model):
    number = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.number

    def __unicode__(self):
        return u'{0}'.format(self.number)

class LineCgv(models.Model):
    number = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.number

    def __unicode__(self):
        return u'{0}'.format(self.number)

class UserProfile(models.Model):
    user = models.OneToOneField(UserGoldGroup)
    phone_other = models.CharField(max_length=20, blank=True, null=True)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    bank = models.ForeignKey(Bank, blank=True, null=True)
    code = models.ForeignKey(Code, blank=True, null=True)
    line_cgv = models.ForeignKey(LineCgv, blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de Usuarios'

    def __str__(self):
        return self.user

    def __unicode__(self):
        return u'{0}'.format(self.user)
