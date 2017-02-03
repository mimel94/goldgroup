from django.conf.urls import url
from django.contrib.auth.views import logout
from .views import Administrator

urlpatterns = [
    url(r'^administrador/inicio/$',Administrator.as_view(),name='index_administrator'),
    url(r'^salir/$', logout, {'next_page':'/'},name='logout'),

]
