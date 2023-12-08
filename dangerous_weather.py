from search_engine import search_by_location, search_by_csv
import pprint
print("\nWelcome to Project Dangerous Weather.\n ---")

print("Ever wanted to travel? Ever considered the risks of travelling to some locaions? Or who is specifically at risk wherever you go? If you have been, this Project is tailor made for you.")
print("How Project Dangerous Weather Works")
print("Project Dangerous Weather allows you to search countries for countries that fit within a specific envrionmental and risk criteria, or allows you to directly search for cities for discover environmental and risk data. Try it out!\n ---")

user_input = input("Are you searching for a specific place? Enter Yes or No:")
if user_input == "Yes":
    user_location = input("Please enter a specific city or location around the world:")
    results = search_by_location(user_location)
    name = results[0]
    temperature = results[1][2]
    precipitation = results[1][3]
    safety = results[2]    

    print(f"You type in {name}. Right now in {name}, the temperature is {temperature}, precipitation is {precipitation}. Right now {name} has a safety score of {safety}")
if user_input == "No":
    print("You typed No. Would you like some suggestions on where to go depending on a few factors? I can look through my files and see what I've got.")
    main_search = input("Would you like that? Please type in Yes or No.")
    main_search = main_search.lower()
    if main_search == "yes":
        safety = input("\nAre you looking for a safe trip or dangerous one? Please type in one of the following - \nVery Dangerous, \nDangerous, \nModerately Dangerous, \nSafe, or \nVery Safe :")
        precipitation = input("\nPlease type in an annual rainfal type - \nLow Rainfall Region, \nLow Moderate Rainfall Region, \nHigh Moderate Rainfall Region or \nHigh Rainfall Region:")
        zone_op = input("\nAre you a tropical guy, or a temperate person? Please select one of the following to indicate your climate preference - \nTropical, \nDry, \nTemperate, \nContinental, \nPolar:")
       
        print("Read the below in as Country, Crime Index, Safety Score, Precipitation, Specific Climate Zone, Temperature in Fahrenheit, and Temperature in Celsius")
        pprint.pprint(search_by_csv(safety_score=safety,precip=precipitation,zone=zone_op))
    if main_search == "no":
        print("Then please Have a wonderful day.")
    




