import csv
import urllib.request
import datetime
from bs4 import BeautifulSoup

today = datetime.date.today()

year = today.year

DOWNLOAD_URL = "https://www.numbeo.com/crime/rankings_by_country.jsp?title=2023-mid" #change for flexibility to year.

def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)


def safety_score(html): #rename this for clarity.
    """
    Analyze the Climate Zone HTML, return a dictionary containing all countries and territory climate data.
    """
    soup = BeautifulSoup(html, features="html.parser")
    body = soup.find('tbody')
    tr = body.find_all('tr')

    safety_data = {}

    for country_data in tr:
        #Extract Country Name
        country_name = country_data.find('td',attrs = {'class':'cityOrCountryInIndicesTable'})
        country_name = country_name.string
        country_name = str(country_name).lower().strip()

        if country_name == "bahamas":
            country_name == "the bahamas"

        #Extract Country Crime Index 
        crime_index = country_data.find_all('td')
        crime_index = crime_index[2]
        crime_index = crime_index.string #convert via int()
        crime_index = str(crime_index).strip()
        crime_index = float(crime_index)

        #Extract Safety Index
        safety_index = country_data.find_all('td')
        safety_index = safety_index[3]
        safety_index = safety_index.string 
        safety_index = str(safety_index).strip()
        safety_index = float(safety_index)
        #convert via int()
        #Add country_name as key, and crime index and saefty score as values. 

        safety_data[country_name] = [crime_index,safety_index]
    return safety_data
        

