#-*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView, View, UpdateView
from .models import UserProfile, UserGoldGroup
from .forms import UserGoldGroupForm, UserProfileForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.hashers import make_password

# Create your views here.

class Administrator(TemplateView):
    template_name = 'admin/administrator/admin_index.html'

class CreateSalesman(CreateView):
    model = UserProfile
    template_name = 'admin/salesman/create_salesman.html'
    form_class = UserGoldGroupForm
    second_form_class = UserProfileForm
    success_url = reverse_lazy("index_administrator")

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs ):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            form.instance.is_salesman = True
            form.instance.is_active = True
            form.instance.password = make_password(form.instance.password)
            print 'la contraseña : ',form.instance.password
            UserProfile = form2.save(commit=False)
            UserProfile.user = form.save()
            UserProfile.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')
            context = {'form':form,'form2':form2, 'country':country,
                        'state':state, 'city':city}
            return render(request, self.template_name, context)

class ActiveSalesman(ListView):
    model = UserProfile
    template_name = 'admin/salesman/actives_salesman.html'
    active = ''

    def get_context_data(self, **kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        if self.active == 'yes':
            context_active = True
        else:
            context_active = False
        context['salesmen'] = self.model.objects.filter(
            user__is_active=context_active,
            user__is_salesman=True
        )
        context['active']=context_active
        return context

class ActiveSalesmanUpdateState(UpdateView):
    model = UserProfile
    template_name = 'admin/salesman/actives_salesman.html'

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user.is_active:
            salesman = self.model.objects.get(pk=self.object.pk)
            obj_user = UserGoldGroup.objects.get(id=salesman.user.id)
            obj_user.is_active = False
            obj_user.save()
            return HttpResponseRedirect(reverse('actives_salesman'))
        else:
            salesman = self.model.objects.get(pk=self.object.pk)
            obj_user = UserGoldGroup.objects.get(id=salesman.user.id)
            obj_user.is_active = True
            obj_user.save()
            return HttpResponseRedirect(reverse('inactives_saleman'))
