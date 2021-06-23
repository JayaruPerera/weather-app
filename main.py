from typing import TextIO

import requests
#import os
from datetime import datetime

api_key = '72e62811de4daecec1f9e9e32677aee7'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

out= open('weather.txt', 'a')
out.write("-------------------------------------------------------------"+'\n')
out.write("Weather Stats for - {}  || {}".format(location.upper(), date_time) + '\n')
out.write("-------------------------------------------------------------" + '\n')

out.write("Current temperature is: {:.2f} deg C".format(temp_city) + '\n')
out.write("Current weather desc  :" + weather_desc + '\n')
out.write("Current Humidity      :")
out.write(str(hmdt))
out.write('%' + '\n')
out.write("Current wind speed    :")
out.write(str(wind_spd))
out.write('kmph' + '\n')

out.close()