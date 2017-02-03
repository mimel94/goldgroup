from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Administrator(TemplateView):
    template_name = 'admin/administrator/admin_index.html'
