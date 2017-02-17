from django.conf.urls import url
from django.contrib.auth.views import logout
from .views import Administrator, CreateSalesman, ActiveSalesman, ActiveSalesmanUpdateState,\
                   MoreInfoSalesman, UpdateSalesman


urlpatterns = [
    url(r'^administrador/inicio/$',Administrator.as_view(), name='index_administrator'),
    url(r'^salir/$', logout, {'next_page':'/'},name='logout'),

    url(r'^administrador/crear_asesor/$',CreateSalesman.as_view(), name='create_salesman'),
    url(r'^administrador/vendedores_activos/$',ActiveSalesman.as_view(active="yes"), name='actives_salesman'),
    url(r'^administrador/vendedores_inactivos/$',ActiveSalesman.as_view(active="no"), name='inactives_saleman'),
    url(r'^administrador/vendedores_actualizar/estado/(?P<pk>\d+)/$',ActiveSalesmanUpdateState.as_view(),
        name='update_state_salesman'),
    url(r'^administrador/vendedores/mas_informacion/(?P<pk>\d+)/$',MoreInfoSalesman.as_view(),
        name='more_info_salesman'),
    url(r'^administrador/vendedores/actualizar/(?P<pk>\d+)/$',UpdateSalesman.as_view(),
        name='update_salesman'),


]
