import pyowm
import os
from dotenv import load_dotenv

load_dotenv() 
api_key=os.getenv('api_key')


owm=pyowm.OWM(api_key)
mgr=owm.weather_manager()
observation = mgr.weather_at_place('London,uk')
w = observation.weather
print(w.wind(),w.humidity)


owm=pyowm.OWM(api_key)
mgr=owm.weather_manager()
observation = mgr.weather_at_place('Hong Kong,china')
w = observation.weather
print(f"The humidity in Hong Kong is {w.humidity}")

owm=pyowm.OWM(api_key)
mgr=owm.weather_manager()
observation = mgr.weather_at_place('Tokyo,japan')
w = observation.weather
print(w.temperature())

owm=pyowm.OWM(api_key)
mgr=owm.weather_manager()
observation = mgr.weather_at_place('LaPaz,bolivia')
w = observation.weather
print(w.pressure)

owm=pyowm.OWM(api_key)
mgr=owm.weather_manager()
observation = mgr.weather_at_place('Koforidua,ghana')
w = observation.weather
print(w.wind())

from pprint import pprint
import requests
r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=api_key')
pprint(r.json())

