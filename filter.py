#This acts as the primary way I filter through the data in order to provide complete travel suggestions based upon country. 

def crime_indexed(target_crime_index=str, row = list):
    """
    Given a Target Crime Index to find, and a row containing a crime index, the function will find the category the crime index fits into, and then will compare that category to the target crime index category. If the current values category is equal to th crime index category, the function will return the category, and the row. The row will be passed into the next function.
    """
    if target_crime_index == "":
        return row, "move"
    if type(row) == str:
        return 'fail','fail'
    else:

        value = row[1]
        value = float(value)
        if value < 20 and target_crime_index == "Very Low": 
            return row, "Very Low"
        if 20< value <40 and target_crime_index == "Low":
            return row, "Low"
        if 40 < value <60 and target_crime_index =="Moderate":
            return row, "Moderate"
        if 60< value <80 and target_crime_index == "High":
            return row, "High"
        if value > 80 and target_crime_index == "Very High":
            return row, "Very High"
        else:
            return 'fail','fail'

def safety_indexed(target_crime_index, row):
    """
    Temp: Reads a 'String' Value, converts it to numerical, and then categorizes it.
    """
    if target_crime_index == "":
        return row, "move"
    if type(row) == str:
        return 'fail','fail'
    else:
        value = row[2]
        value = float(value)
        if value < 20 and target_crime_index == "Very Dangerous": 
            return row, value
        if 20< value <40 and target_crime_index == "Dangerous":
            return row, value
        if 40 < value <60 and target_crime_index =="Moderately Dangerous":
            return row, "Moderately Dangerous"
        if 60< value <80 and target_crime_index == "Safe":
            return row, value
        if value > 80 and target_crime_index == "Very Safe":
            return row, value
        else:
            return 'fail','fail'


def precipitation_index(target_precip_index,row):
    """
    For a given target 
    """
    if target_precip_index == "":
        return row, "move"
    if type(row) == str:
        return 'fail','fail'
    else:
        value = row[3]
        value = float(value)
        if value < 600 and target_precip_index == "Low Rainfall Region": 
            return row, "Low Rainfall Region"
        if 600< value <900 and target_precip_index == "Low Moderate Rainfall Region":
            return row, "Moderate Rainfall Region"
        if 900 < value <1600 and target_precip_index =="High Moderate Rainfall Region":
            return row, "High Moderate Rainfall Region"
        if value > 1600 and target_precip_index == "High Rainfall Region":
            return row, "High Rainfall"
        else:
            return 'fail','fail'



def zoned(target_zone,row):
    """
    Takes a target_zone value and a list row, and searches for it within a dictionary value set.If the value is in the dictionary, and the key is equal to target zone, returns list row. 
    """
    

    zones = {'Tropical':['AF','AM','AW','AS'],'Dry':['BWH','BASH','BWK','BSK'],'Temperate':['CSA','CSB','CSC','CWA','CFB','CWC'],'Continental':['DSA','DSB','DSC','DSD', 'DWA','DWB','DWC','DWD','DFA','DFB','DFC','DFD'],'Polar':['ET','EF']}

    if target_zone == "":
        return row, "move"
    if type(row) == str:
        return 'fail','fail'
    else:
        country_zone = row[4]
        if country_zone in zones['Tropical'] and target_zone == 'Tropical':
            return row, 'Tropical'
        if country_zone in zones['Dry'] and target_zone == 'Dry':
            return  row, 'Dry'
        if country_zone in zones['Temperate'] and target_zone == 'Temperate':
            return  row,'Temperate'
        if country_zone in zones['Continental'] and target_zone == 'Continental':
            return  row, 'Contin'
        if country_zone in zones['Polar'] and target_zone == 'Polar':
            return  row, 'Polar'
        else:
            return 'fail','fail'

def fahrenheit_index(target_fah_index,row):
    """
    For a given target temperature, provide a 
    """
    if target_fah_index == "":
        return row, "move"
    if type(row) == str:
        return 'fail','fail'
    else:
        value = row[5]
        value = float(value)
        if 30 < value < 55 and target_fah_index == "Low Temperature Region": 
            return row, "Low Temperature Region"
        if 55< value <70 and target_fah_index == "Low Moderate Temperature Region":
            return row, "Low Moderate Temperature Region"
        if 70 < value <80 and target_fah_index =="High Moderate Temperature Region":
            return row, "High Moderate Temperature Region"
        if value > 80 and target_fah_index == "Hot Region":
            return row, "Hot Region"
        else:
            return 'fail','fail'

def celsius_index(target_celsius_index,row):
    """
    For a given target 
    """
    if target_celsius_index == "":
        return row, "move"
    if type(row) == str:
        return 'fail','fail'
    else:
        value = row[6]
        value = float(value)
        if 0 < value < 12 and target_celsius_index == "Low Temperature Region": 
            return row, "Low Temperature Region"
        if 12< value <19 and target_celsius_index == "Low Moderate Temperature Region":
            return row, "Low Moderate Temperature Region"
        if 19 < value <26 and target_celsius_index =="High Moderate Temperature Region":
            return row, "High Moderate Temperature Region"
        if 26 <value < 31 and target_celsius_index == "Hot Region":
            return row, "Hot Region"
        else:
            return 'fail','fail'


    
