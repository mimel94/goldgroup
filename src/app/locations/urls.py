from django.conf.urls import url
from .views import get_countries, get_states, get_cities

urlpatterns = [
    url(r'^countries/$', get_countries, name="get_countries"),
    url(r'^states/$', get_states, name="get_states"),
    url(r'^cities/$', get_cities, name="get_cities"),
]
