from http.client import HTTPResponse
import json
import re
from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def test(request):













    return JsonResponse({'foo': 'bar'})


def makes(request):
    makes_dict = {
        'makes': [
            {'id':0,'name':'all'}
        ]
    }
    url = "https://api.row52.com/odata/Makes?$orderby=name%20asc"
    resp = requests.get(url).json()['value']
    # print(resp)
    [makes_dict['makes'].append(x) for x in resp]


    return JsonResponse(makes_dict)

def models(request):
    models_dict = {
        'models': [
            
        ]
    }
    url = "https://api.row52.com/odata/Models?$orderby=name%20asc"
    resp = requests.get(url).json()['value']
    # print(resp)
    [models_dict['models'].append(x) for x in resp]


    return JsonResponse(models_dict)

def results(request, make=0, model=0, distance=25, zip=97223):
    print(make, model, distance, zip)
    cars_dict = {
        'locations': [

        ],
    }
    try:
        url = f"https://www.picknpull.com/api/vehicle/search?&makeId={make}&modelId={model}&year=&distance={distance}&zip={zip}"
        resp = requests.get(url).json()
        print(resp)
        # print(resp)
        [cars_dict['locations'].append({'name':location_obj['location']['name'], 'vehicles':[veh for veh in location_obj['vehicles']]}) for location_obj in resp]
        # [cars_dict['vehicles'].append(x) for x in resp['vehicles']]

    except:
        return JsonResponse({'error':'error on fetch of cars'})


    return JsonResponse(cars_dict)