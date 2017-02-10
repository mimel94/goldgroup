from django.conf.urls import url
from django.contrib.auth.views import logout
from .views import Administrator, CreateSalesman

urlpatterns = [
    url(r'^administrador/inicio/$',Administrator.as_view(), name='index_administrator'),
    url(r'^salir/$', logout, {'next_page':'/'},name='logout'),

    url(r'^administrador/crear_asesor/$',CreateSalesman.as_view(), name='create_salesman'),

]
