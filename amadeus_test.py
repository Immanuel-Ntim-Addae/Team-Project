from amadeus import ResponseError, Client

# amadeus = Client(
#     client_id='u7CW0MiGzYOXiiikD9q6VXaGkfB3KKnY',
#     client_secret='NEuOMTpe0o7jL2CD'
# )

# try:
#     '''
#     Returns safety information for a location in Barcelona based on geolocation coordinates
#     '''
#     response = amadeus.safety.safety_rated_locations.get(latitude=40.719074, longitude=-74.0431)
#     print(response.data[0]['safetyScores']['overall'])
# except ResponseError as error:
#     raise error

# Safety Scores from This API are out of 100. 
#Now we need to convert a given location into a latitude longitude, then feed it into safety api to get our safety score

#Function
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
        return response.data[0]['safetyScores']['overall']
    except ResponseError as error:
        raise error

