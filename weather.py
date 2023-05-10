import requests 
from pprint import pprint
# to generate api key you need to register yourself to openweathermap
API_Key='cb771e45ac79a4e8e2205c0ce66ff633'

city=input("Enter a city:")

base_url="http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data=requests.get(base_url).json()

pprint(weather_data)