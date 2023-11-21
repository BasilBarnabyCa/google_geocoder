import googlemaps
import os
from datetime import datetime
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Variable Declaration
apiKey = os.environ["GOOGLE_MAPS_API_KEY"]

gMaps = googlemaps.Client(key=apiKey)

geocodeResult = gMaps.geocode("1600 Amphitheatre Parkway, Mountain View, CA")

print(geocodeResult)