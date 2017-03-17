from django.conf.urls import url
from django.contrib.auth.views import logout
from .views import Administrator, CreateSalesman, ActiveSalesman, ActiveSalesmanUpdateState,\
                   MoreInfoSalesman, UpdateSalesman, ListCodes, CreateCode, get_list_salesman_actives,\
                   UpdateStateCode, CreateCgv, ListCgv, UpdateStateCgv



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

    url(r'^busqueda_asesores/$', get_list_salesman_actives, name='seach_saleman_actives'),

    url(r'^administrador/codigo/activos/$',ListCodes.as_view(active='yes'), name='actives_codes'),
    url(r'^administrador/codigo/inactivos/$',ListCodes.as_view(active='no'), name='deactives_codes'),
    url(r'^administrador/codigo/crear/$',CreateCode.as_view(), name='create_code'),
    url(r'^administrador/codigo/actializar/(?P<pk>\d+)/$',UpdateStateCode.as_view(), name='update_code_state'),

    url(r'^administrador/linea_corportativa/crear/$',CreateCgv.as_view(),name='create_cgv'),
    url(r'^administrador/linea_corportativa/activas/$',ListCgv.as_view(actives='yes'),name='actives_cgv'),
    url(r'^administrador/linea_corportativa/inactivas/$',ListCgv.as_view(actives='no'),name='inactives_cgv'),
    url(r'^administrador/linea_corportativa/actualizar/(?P<pk>\d+)$',UpdateStateCgv.as_view(),name='update_line_state'),



]
