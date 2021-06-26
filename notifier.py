from win10toast import ToastNotifier
import json
import requests
import os
from datetime import datetime

user_api=os.environ['weather_data']
location = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
data= json.dumps(api_data)
final_data=json.loads(data)

#print(final_data)
temp_city = ((final_data['main']['temp']) - 273.15)
weather_desc = final_data['weather'][0]['description']
hmdt = final_data['main']['humidity']
wind_spd = final_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
weather_report= f"Weather Stats for- {location.upper()} || { date_time}\n"f"Current temperature is:{temp_city:.2f} deg C\n" f"Current Humidity:{hmdt} % \n" f"Current wind speed:{wind_spd} kmph\n" f"Current weather desc: {weather_desc}\n"  f"Current wind speed:{wind_spd} kmph\n"
print(weather_report)
n = ToastNotifier()
n.show_toast("Weather Report",weather_report,duration=60, icon_path ="weather.ico" )
