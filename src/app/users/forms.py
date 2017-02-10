#-*- coding:utf-8 -*-
from django import forms
from .models import UserGoldGroup, UserProfile
from goldGroup import settings


class UserGoldGroupForm(forms.ModelForm):

    class Meta:
        model = UserGoldGroup
        fields = [
            'first_name',
            'last_name',
            'first_surname',
            'last_surname',
            'type_document',
            'number_document',
            'gender',
            'birthdate',
            'phone',
            'city_residence',
            'address_residence',
            'email',
            'password'
        ]
        labels ={
            'first_name':'Primer Nombre'  ,
            'last_name':'Segundo Nombre',
            'first_surname':'Primer Apellido',
            'last_surname':'Segundo Apellido',
            'type_document':'Tipo de Documento',
            'number_document':'Numero de Documento',
            'gender':'Sexo',
            'birthdate':'Dia de nacimiento',
            'phone':'Telefono',
            'city_residence':'Ciudad de recidencia',
            'address_residence':'Dirección de recidencia',
            'email':'Correo',
            'password':'Contraseña'
        }
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'first_surname': forms.TextInput(),
            'last_surname': forms.TextInput(),
            'type_document': forms.Select(),
            'number_document': forms.TextInput(),
            'gender': forms.Select(),
            'birthdate': forms.DateInput(attrs={'class':'datepicker'}),
            'phone': forms.TextInput(),
            'city_residence': forms.Select(attrs={'required':'false'}),
            'address_residence':forms.TextInput(),
            'email':forms.EmailInput(),
            'password':forms.PasswordInput()
        }

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'phone_other',
            'bank_account',
            'bank',
            'code',
            'line_cgv'
        ]
        labels = {
            'phone_other':'Celular',
            'bank_account':'Cuenta Bancaria',
            'bank':'Banco',
            'code':'Codigo Digitacion',
            'line_cgv':'Linea Cgv'
        }

        widgets ={
            'phone_other': forms.TextInput(),
            'bank_account': forms.TextInput(),
            'bank': forms.Select(),
            'code': forms.Select(),
            'line_cgv': forms.Select()
        }
