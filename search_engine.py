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
            row, category_safety = safety_indexed(safety_score,row)
            row,category_precip = precipitation_index(precip,row)
            #everything from zone onwards has an issue.
            row, category_zone = zoned(zone,row)
            row, category_fah = fahrenheit_index(temp_f,row)
            row, category_cel = celsius_index(temp_c,row)

            if row != 'fail':
                filter_results.append(row)

    if len(filter_results)>5:
        return filter_results[0:5]
    if len(filter_results)<5:
        return filter_results
    if filter_results == []:
        return "Sorry, no data for your query is found. Please try again."
   
            
# q = search_by_csv(safety_score="Safe",zone = "Temperate")

# def top_five(safety_score="",precip="",zone="",temp_f="",temp_c=""):
#     """Takes a list, sorts them, and returns the top five elements in the list."""
#     results = search_by_csv(safety_score,precip,zone, temp_f, temp_c)
#     sorted_list = sorted(results, key=lambda x: x[2], reverse=True)
#     if len(results) >5:
#         return sorted_list [0:5]
#     if len(results)<5:
#         return results 
#     if results == "[]":
#         return "Sorry, we don't have what you're looking for!"

    
    




    


