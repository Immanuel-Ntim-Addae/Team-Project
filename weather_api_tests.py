import urllib
import json
import requests
import pprint
import datetime

APIKEY = "9X6WQPZFQQMGJY7BNL8JVF8AD"
# location ="Atlanta"
# date1 = "2023-11-17" #Dates should be in the format yyyy-MM-dd Note: When Only entering date 1, gives you weather deatils for that day alone. 
# date2 = "" #
# URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date1}/{date2}?key={APIKEY}"
# with urllib.request.urlopen(URL) as f:
#         response_text = f.read().decode('utf-8')
#         response_data = json.loads(response_text)
        
#pprint.pprint(response_data)

#Maybe use this to get some lattitude and longitude variables.

def get_weather_data(location =str):
        """
        For a given location, retrieves latitude and longitude, precipitation, and temperature data (fahrenheit and celsius)
        """
        #Character control
        location = location.replace(' ','%20')

        date1 = datetime.date.today()
        date2 = ""

        URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date1}/{date2}?key={APIKEY}"
        with urllib.request.urlopen(URL) as f:
                response_text = f.read().decode('utf-8')
                response_data = json.loads(response_text)

                #Get Latitude and Longitude
                lat = response_data['latitude']
                long = response_data['longitude']

                #Get Temperature and Precipitation Results
                noon_time_results = response_data['days'][0]['hours'][12] #Gets us temp data at high noon. 
                temperature = noon_time_results['temp']
                precipitation = noon_time_results['precip']

        return lat,long,temperature,precipitation
                

