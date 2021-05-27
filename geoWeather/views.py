from django.http.response import HttpResponse
from django.shortcuts import render
from forecastUpdater.forecastApi import ForecastAPI

# Create your views here.
def index(request):
    return render(request, 'geoWeather/index.html')

def getcidade(request, cidade, pais):  
    api = ForecastAPI(cidade, pais)
    json_response = api.get_forecast()  

    return HttpResponse(json_response)    