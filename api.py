import urllib.request
import urllib.parse
import json

BASE_OPENWEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'
OPENWEATHER_API_KEY = 'a97d18f6f613cdaacb9af32e9c0bcd52'

def build_url(city_id: str) -> str:
    '''
    Creates the URL for the location.
    '''
    parameters = [
        ('APPID', OPENWEATHER_API_KEY), ('id', city_id), ('units', 'imperial')
    ]
    return BASE_OPENWEATHER_URL + '?' + urllib.parse.urlencode(parameters)

def get_result(url: str) -> 'json text':
    '''
    Returns the result from reading the URL
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.load(response)
    finally:
        if response!= None:
            response.close()
