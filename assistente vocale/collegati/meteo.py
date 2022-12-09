import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = '1cf92d304b093f943e7558a89dcf2361'
CITY = "Milan"
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit (temp_kelvin)
velocità_vento= response['wind']['speed']
umidità = response['main']['humidity'] 
situazione_meterologica = response['weather'][0]['description']

print("la temperatura a",CITY,"é:",int(temp_celsius),"gradi")
print("la velocità del vento",CITY,"è:",velocità_vento,"m/s")
print("l'umidità a",CITY,"è:",umidità,"%")
print("la situazione a ",CITY,"è:",situazione_meterologica)


 

 

