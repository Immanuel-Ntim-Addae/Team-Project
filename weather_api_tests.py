import urllib
import json
import requests


APIKEY = "9X6WQPZFQQMGJY7BNL8JVF8AD"
location ="Boston"
date1 = "2023-11-17" #Dates should be in the format yyyy-MM-dd Note: When Only entering date 1, gives you weather deatils for that day alone. 
date2 = "" #
URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date1}/{date2}?key={APIKEY}"
with urllib.request.urlopen(URL) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        
print(response_data) #Operates 