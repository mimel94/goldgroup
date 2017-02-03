# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class IndexView(View):
    template_name='website/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, )

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('user')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse_lazy('index_administrator'))
                else:
                    context = {'error':'Error cuenta desactivada '}
            else:
                context = {'error': 'Usuario o contraseña no validas' }
        else:
            context = {'error': 'Completa los campos'}
        return render(request, self.template_name, context)
