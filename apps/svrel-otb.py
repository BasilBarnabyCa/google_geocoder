import googlemaps
import os
from openpyxl import Workbook, load_workbook
from datetime import datetime
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Variable Declaration
apiKey = os.environ["GOOGLE_MAPS_API_KEY"]
filePath = os.environ["FILE_PATH"]

wb = load_workbook(filename = filePath)	
sheet = wb.active

gMaps = googlemaps.Client(key=apiKey)

geocodeResult = gMaps.geocode("1600 Amphitheatre Parkway, Mountain View, CA")

print(geocodeResult)