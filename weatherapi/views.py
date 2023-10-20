from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from datetime import datetime, date, timedelta
from .models import Weather
from .serializers import WeatherSerializer
import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = os.path.join(Path(__file__).resolve().parent.parent, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound
    
class WeatherApi(APIView):
    def get(self, request):
        # get 30 minutes ago
        half_h_ago = datetime.now() - timedelta(minutes=30)
        # get city from requests
        try:
            city = request.query_params['city'].strip().lower()
        except:
            return Response({'error':'Use param "city" in your request'})
        # make request to bd
        try:
            weather = Weather.objects.get(city_name=city, date_created__gte=half_h_ago)
            weather_ser = WeatherSerializer(instance=weather)
            return Response(weather_ser.data)
        except:
            pass
            
        # if weather doesnt exist make request to geocoder api and get lat and long
        api_key_geocoder = os.getenv("API_GEOCODER")
        url_yndex_geocoder = f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key_geocoder}&geocode={city}&format=json'
        try:
            response_api_geocoder = requests.get(url_yndex_geocoder).json()
            city_position = response_api_geocoder['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        except:
            return Response({'error':'Problem with name of city! Enter another city!'})
        city_lat = float(city_position.split(' ')[1])
        city_lon = float(city_position.split(' ')[0])

        # make request to weather api and get weather
        api_key_weather = os.getenv("API_WEATHER")

        url_yndex_weather = f'https://api.weather.yandex.ru/v2/informers/?lat={city_lat}&lon={city_lon}&lang=ru_RU'
        response_api_weather = requests.get(url_yndex_weather, headers={'X-Yandex-API-Key': api_key_weather}).json()
        temp = response_api_weather['fact']['temp']
        pressure_mm = response_api_weather['fact']['pressure_mm']
        wind_speed = response_api_weather['fact']['wind_speed']
        # create new weather and send it
        weather_new = Weather(city_name=city, temperature=temp, pressure=pressure_mm, wind=wind_speed)
        weather_new.save()
        weather_ser = WeatherSerializer(instance=weather_new)
        return Response(weather_ser.data)
