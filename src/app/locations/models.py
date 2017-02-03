#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __unicode__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250)
    state = models.ForeignKey(State)

    class Meta:        
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __unicode__(self):
        return self.name
