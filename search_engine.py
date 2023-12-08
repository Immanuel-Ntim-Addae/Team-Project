#import crackpot coding
from api_functions import get_weather_data, get_safety_score
import csv
from filter import crime_indexed,safety_indexed,precipitation_index,zoned,fahrenheit_index,celsius_index

def search_by_location(location = str): 
    """
    Takes a location from a user input, and returns the location name, country, curent precipitation and temperature, climate zone, and safety score.
    """
    full_weather_data = get_weather_data(location)
    latitude = get_weather_data(location)[0] #returns (lat,long,temp, precip)
    longitude = get_weather_data(location)[1]
    overall_safety = get_safety_score(latitude,longitude)
    return location,full_weather_data, overall_safety

def search_by_csv(crime_index="",safety_score="",precip="",zone="",temp_f="",temp_c=""):
    """
    Takes a users categorical input for the values Crime Index, Safety Score, Annual Rainfall, Climate Zone, Temperature (F), Temperature (C), and filters the data for these values. 
    """
    
    filter_results = []

    with open('data/climate_database.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar = '|')

        next(reader)

        for row in reader:
            #passon_row,category_crime = crime_indexed(crime_index,row)
            passon_row, category_safety = safety_indexed(safety_score,row)
            passon_row,category_precip = precipitation_index(precip,passon_row)
            #everything from zone onwards has an issue.
            passon_row, category_zone = zoned(zone,passon_row)
            passon_row, category_fah = fahrenheit_index(temp_f,passon_row)
            passon_row, category_cel = celsius_index(temp_c,passon_row)

            if passon_row != 'fail':
                filter_results.append(passon_row)
    return filter_results
            
# q = search_by_csv(safety_score="Safe",zone = "Temperate")

def top_five(safety_score="",precip="",zone="",temp_f="",temp_c=""):
    """Takes a list, sorts them, and returns the top five elements in the list."""
    results = search_by_csv(safety_score,precip,zone, temp_f, temp_c)
    sorted_list = sorted(results, key=lambda x: x[2], reverse=True)
    if len(results) >5:
        return sorted_list [0:5]
    else:
        return results
    





    


