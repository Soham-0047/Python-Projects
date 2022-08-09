# import phonenumbers
# from text import number

# from phonenumbers import geocoder

# c_num = phonenumbers.parse(number,"CH")
# print(geocoder.description_for_number(c_num,"en"))


# from phonenumbers import carrier

# service_pro = phonenumbers.parse(number,"RO")
# print(carrier.name_for_number(service_pro,"en"))

##Different Project 

from concurrent.futures import process
from unittest import result
import phonenumbers
import opencage
import folium
import config
from text import number
from phonenumbers import geocoder



pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier

service_pr = phonenumbers.parse(number)
print(carrier.name_for_number(service_pr,"en"))

from opencage.geocoder import OpenCageGeocode


key = config.api_key
geocoder = OpenCageGeocode(key)
query = str(location)

results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)


mymap = folium.Map(location=[lat,lng],zoom_start =9)

folium.Marker([lat,lng],popup=location).add_to(mymap)

mymap.save("mylocation.html")