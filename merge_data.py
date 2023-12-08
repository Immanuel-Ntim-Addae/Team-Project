from weather_data import temperature_dict, precipitation_dict,download_temperature_page, download_precipitation
from numbeo_scrape import safety_score, download_page
import pprint
import csv

temp_url = "https://weatherandclimate.com/countries"

precip_url = "https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation"

safety_url = "https://www.numbeo.com/crime/rankings_by_country.jsp?title=2023-mid"

def merge_data_set():
    """
    This module merges data from the dictionaries precipitation dict, temperature dict, and safety_data to create one large dictionary, containing (for every country) the Annual Precipitation, the Climate Zone, the Temperature in Farenheit, Temperature in Celsius, Crime Index and Safety Rating. 
    """
    precip_html = download_precipitation(precip_url)
    precip_dict = precipitation_dict(precip_html)

    temp_html = download_temperature_page(temp_url)
    temp_dict = temperature_dict(temp_html)

    safety_html = download_page(safety_url)
    safety_dict = safety_score(safety_html)

    for key in safety_dict:
        try:
            safety_dict[key].append([precip_dict[key][0], temp_dict[key]]) #error due to spelling of Sao Tome. Use exception?
            climate_data = safety_dict
        except KeyError as e:
            pass

    #Removes error values, as they are not in previous sets of data. Removes them so only data in csv is complete.
    remove = ["us virgin islands", "kosovo (disputed territory)", "serbia", "montenegro", "monaco", "hong kong (china)","taiwan","isle of man" ]
    for country in remove:
        del safety_dict[country]

    climate_dict = safety_dict 
    return climate_dict

#Error Notation
# US Virgin Islands not present.
# kosovo is not part of native data set.
# serbia not part of native data set.
# montenegro not part of native set.
# monaco not part of native set
# hong kong not part of native set
# taiwan not part of native set.
# isle of man 
#taiwan error

def convert_to_csv():
     
    climate_data = merge_data_set()

    climate_list = [['Country','Crime Index','Safety Score', 'Annual Rainfall (mm)','Climate Zone','Temperature (F)','Temperature (C)',]]

    for key in climate_data:
        crime_index = climate_data[key][0]
        safety = climate_data[key][1]
        rain = climate_data[key][2][0]
        zone = climate_data[key][2][1][0]
        temp_f = climate_data[key][2][1][1]
        temp_c = climate_data[key][2][1][2]
            
        climate_list.append([key,crime_index,safety,rain,zone,temp_f,temp_c])
        
    with open('data/climate_database.csv','w', newline = '') as file:
        csv_writer = csv.writer(file)
        for row in climate_list:
            csv_writer.writerow(row)

convert_to_csv()


        