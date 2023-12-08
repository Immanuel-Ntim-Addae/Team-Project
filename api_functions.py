import urllib
import json
import requests
import pprint
import datetime
from amadeus import ResponseError, Client

APIKEY = "9X6WQPZFQQMGJY7BNL8JVF8AD"
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
                
def get_safety_score(lat,long):
    """
    For a given latitude and longitude value, return the overall safety score of a lat,long pair.
    """
    amadeus = Client(
    client_id='u7CW0MiGzYOXiiikD9q6VXaGkfB3KKnY',
    client_secret='NEuOMTpe0o7jL2CD'
    )

    try:
        '''
        Returns safety information for a location in Barcelona based on geolocation coordinates
        '''
        response = amadeus.safety.safety_rated_locations.get(latitude = lat, longitude = long )
        test = type(response.data)
        if test != type(None):
            return response.data[0]['safetyScores']['overall']
        else:
             return "Check Country Score"
    except ResponseError as error:
        raise error
q = get_weather_data("Rome")
print(q)
a,b = q[0],q[1] 
print(get_safety_score(a,b))

