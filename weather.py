import pyowm

# owm=pyowm.OWM('584375f9faf6841863ba138f9e1b599d')
# mgr=owm.weather_manager()
# observation = mgr.weather_at_place('London,uk')
# w = observation.weather
# print(w.wind(),w.humidity)


# owm=pyowm.OWM('584375f9faf6841863ba138f9e1b599d')
# mgr=owm.weather_manager()
# observation = mgr.weather_at_place('Hong Kong,china')
# w = observation.weather
# print(f"The humidity in Hong Kong is {w.humidity}")

# owm=pyowm.OWM('584375f9faf6841863ba138f9e1b599d')
# mgr=owm.weather_manager()
# observation = mgr.weather_at_place('Tokyo,japan')
# w = observation.weather
# print(w.temperature())

# owm=pyowm.OWM('584375f9faf6841863ba138f9e1b599d')
# mgr=owm.weather_manager()
# observation = mgr.weather_at_place('LaPaz,bolivia')
# w = observation.weather
# print(w.pressure)

# owm=pyowm.OWM('584375f9faf6841863ba138f9e1b599d')
# mgr=owm.weather_manager()
# observation = mgr.weather_at_place('Koforidua,ghana')
# w = observation.weather
# print(w.wind())

from pprint import pprint
import requests
r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=584375f9faf6841863ba138f9e1b599d')
pprint(r.json())

