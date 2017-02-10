from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Country, State, City

# Create your views here.

def get_countries(request):
    obj_countries = Country.objects.all()
    dict_country = {}
    for obj_country in obj_countries:
        dict_country[obj_country.id] = obj_country.name
    data = {"status": "success", "result": dict_country}
    return HttpResponse(json.dumps(data))


def get_states(request):
    obj_states = State.objects.filter(country=request.GET["countryId"])
    dict_state = {}
    for obj_state in obj_states:
        dict_state[obj_state.id] = obj_state.name
    data = {"status": "success", "result": dict_state}
    return HttpResponse(json.dumps(data))

def get_cities(request):
    obj_cities = City.objects.filter(state=request.GET["stateId"])
    dict_city = {}
    for obj_city in obj_cities:
        dict_city[obj_city.id] = obj_city.name
    data = {"status": "success", "result": dict_city}
    return HttpResponse(json.dumps(data))
