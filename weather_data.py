import csv
import urllib.request
from bs4 import BeautifulSoup

DOWNLOAD_URL = "https://weatherandclimate.com/countries"

def download_temperature_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)


def temperature_dict(html): #rename this for clarity.
    """
    Analyze the Climate Zone HTML, return a dictionary containing all countries and territory climate data.
    """
    soup = BeautifulSoup(html, features="html.parser")
    country_list = soup.find("tbody")
    temperature_data =dict()
    country_list.tr.decompose() #removes the first table row that contains the table headings.
    
    for country_data in country_list.find_all("tr"): #iterates through a list of country and territory data.

        #Extract Country Name
        country_data_a = country_data.find("a") #finds all 'a' tags within the variable 'country_data'
        country_data_a.i.decompose() #removes the 'i' tags within the variable 'country_data'
        country_data_a = country_data_a.string
        country_name = str(country_data_a.strip())
        country_name = country_name.lower()

        #corrections for merging dataset
        if country_name == "the bahamas":
            country_name = "bahamas"
        if country_name == "cote d'ivoire":
            country_name = "ivory coast"
        if country_name == "czechia":
            country_name = "czech republic"
        
        #Prepares a list of <td> tags found in the row for a country in the HTML Document
        td_tags = country_data.find_all('td')
        
        #Extracts Climate_Zone for Country or Territory
        climate_zone = td_tags[1].string

        #Extracts Temperature in Farenheit
        try:
            temp_farenheit = td_tags[2].string
            temp_farenheit = str(temp_farenheit)
            temp_farenheit = temp_farenheit.strip()
            
            temp_farenheit = float(temp_farenheit)
        except ValueError as e:
            temp_farenheit = 0 #later, convert all zero values to NA in Excel File.
        

        #Extracts Temperature in Celsius
        try:
            temp_celsius = td_tags[3].string
            temp_celsius = str(temp_celsius)
            temp_celsius = temp_celsius.strip()
            temp_celsius = float(temp_celsius)
        except ValueError as e:
            temp_celsius = 0

        #Adds all Climate Zone and Temperate (Farenheit and Celsius) as keys to weather_data dictionary
        temperature_data[country_name] = [climate_zone,temp_farenheit,temp_celsius]
    return temperature_data
       




DOWNLOAD_URL_2 = "https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation"
def download_precipitation(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)

def precipitation_dict(html):
    """
    Analyze the Wikipedia Precipitation per Country data page, and return a dictionary of country and annual precipitation.
    """ 
    soup = BeautifulSoup(html, features="html.parser")

    precipitation_list = soup.find("tbody")
    precipitation_data = dict()
    precipitation_tr=precipitation_list.find_all('tr')
    for td in precipitation_tr[1:]: 
    
        #Extract Country Name
        country_name = td.find("a")
        country_name = country_name.string
        country_name = str(country_name)
        country_name = country_name.lower()
        
        #Make Country Names the Same as Country Names in Temperature Data for use in merging data sets.
        if country_name == "são tomé and príncipe":
            country_name = "sao tome and principe"
        if country_name == "congo":
            country_name = "republic of the congo"
        if country_name == "dr congo":
            country_name = "democratic republic of the congo"
        if country_name == "east timor":
            country_name = "timor-leste"
        if country_name == "gambia":
            country_name = "the gambia"

        
        #Extract Annual Precipitation and Convert it to an Numerical Value
        try:
            annual_precipitation_values = td.find_all('td') #Finds all td values
            annual_precipitation = annual_precipitation_values[2]
            annual_precipitation = annual_precipitation.string
            annual_precipitation = str(annual_precipitation)
            annual_precipitation = annual_precipitation.replace(',','')
            annual_precipitation = int(annual_precipitation)
        except IndexError as e: #Index Error Arises due to value 'mm' being accepted as a country variable
            annual_precipitation = '3200'

        precipitation_data[country_name] = [annual_precipitation]
    return precipitation_data


    


        





