from django.utils import timezone
import requests
from weather.models import Forecast
import json

class ForecastAPI:
    __url = 'http://api.openweathermap.org/data/2.5/weather'
    __api_key = 'aed5f71b0f9aed0ebf9969ac12e54605'
    lang = 'pt_br'

    def __init__(self, cidade, pais):
        self.cidade = cidade
        self.pais = self.__translate_country(pais)

    def __get_forecast_json(self):
        url = self.__url
        api_key = self.__api_key
        cidade = self.cidade
        pais = self.pais
        lang = self.lang

        r = requests.get(f'{url}?q={cidade},{pais}&appid={api_key}&lang={lang}')

        try:
            r.raise_for_status()
            return r.json()
        except:
            return None

    def __translate_country(self, country):
        translation_dict = {
            "Brazil": "br"
        }

        return translation_dict[country] if country in translation_dict.keys() else "br" 

    def get_forecast(self):
        json_res = self.__get_forecast_json()
        
        if json_res is not None:
            try:
                forecast = {
                    "cidade"      : json_res['name'],
                    "descricao"   : json_res['weather'][0]['description'],
                    "temperatura" : json_res['main']['temp'] - 273.15
                }           
                return json.dumps(forecast)
            except:
                pass

def __get_forecast_json():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    id_cidade = '3398269'
    api_key = 'aed5f71b0f9aed0ebf9969ac12e54605'
    lang = 'pt_br'

    r = requests.get(f'{url}?id={id_cidade}&appid={api_key}&lang={lang}')

    try:
        r.raise_for_status()
        return r.json()
    except:
        return None

def atualizar_forecast():
    json = __get_forecast_json()

    if json is not None:
        try:
            fore = Forecast(
                cidade      = json['name'],
                descricao   = json['weather'][0]['description'],
                temperatura = json['main']['temp'] - 273.15
                )
            fore.save()
            print(timezone.now() + 'Salvando...\n' + fore)
        except:
            pass