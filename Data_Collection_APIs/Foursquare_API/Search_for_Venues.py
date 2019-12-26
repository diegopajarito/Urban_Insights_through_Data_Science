# import all libraries 
import json
from pandas.io.json import json_normalize
import folium
from geopy.geocoders import Nominatim
import pandas as pd
import requests

# open csv file with pandas
df_grid = pd.read_csv('# insert grid created in QGIS')

# extract just the 'left' and 'top' columns
df_grid_2 = df_grid[['left', 'top']]

# extract some specific rows
# (I need this line because I can make max 500 calls per day)
df_grid_4 = df_grid_2.iloc[0:500]

# create an empty list that will have all the dictionaries that I will retrieve inside
list_of_dictionaries = []

# url taken by the Foursquare API developers page -> Places API -> Venues -> Search for venues
url = 'https://api.foursquare.com/v2/venues/search'
# make a for loop to iterate through the points of the grid created in QGIS to extract all lot and lat
for i in df_grid_4.index:
  # this is to extract the lon and lat of each point
  lon = df_grid_4['left'][i]
  lat = df_grid_4['top'][i]
  # convert lon and lat from float to srings so that I can concatenate them
  lon = str(lon)
  lat = str(lat)
  # concatenate lon and lat
  lat_lon = lat + ',' + lon

# parameters taken from the API developers page 'search for venues' (same as above)
  params = dict(
    client_id='insert client_id here',
    client_secret='insert client_secret here',
    v='20180323',
    ll=lat_lon,  # each time it is replaced with new coordinates
    intent='browse',
    radius=30,
    limit=100
  )

  # use the request.get method to ask for the parameters
  resp = requests.get(url=url, params=params)
  print(resp)

  # json.loads method transforms the response into a dictionary
  data = json.loads(resp.text)

  # append to the new dictionary created
  list_of_dictionaries.append(data)

# set new lists to set a dataframe later on
venues_id = []
names = []
latitudes = []
longitudes = []
category = []

# this for loop iterates through the list of dictionaries to extract them one by one
for det_venues in list_of_dictionaries:
  # this second loop retrieves the parameters inside the json format
  for i in det_venues['response']['venues']:

    # add all the ids to the venues_id list
    venues_id.append(i['id'])
    # add all the names to the names list
    names.append(i['name'])
    # add all the latitudes to the latitudes list
    latitudes.append(i['location']['lat'])
    # add all the latitudes to the latitudes list
    longitudes.append(i['location']['lng'])

    # this for loop retrieve all the categories
    for cat in i['categories']:
      # add all the categories to the category list
      category.append(cat['name'])

print('--------------------------- Underneath printed all the lists to check them ---------------------------------')
print('venues id:', venues_id)
print('names:', names)
print('latitudes:', latitudes)
print('longitudes:', longitudes)
print('category:', category)

# create dataframe from lists names, latitudes, longitudes
df_venues = pd.DataFrame(list(zip(venues_id, names, latitudes, longitudes, category)), columns=['Venues_id', 'Name', 'lat', 'lon', 'category'])

# drop rows with same values in column Venues_id
df_venues_search = df_venues.drop_duplicates(subset=['Venues_id'], keep='last')

# reset the row id values
df_venues_search.reset_index(drop=True, inplace=True)

# export dataframe df_venues in csv
df_venues_search.to_csv('insert csv file path')

print('Done')