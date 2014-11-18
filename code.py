import time
from geopy.geocoders import GoogleV3
geolocator=GoogleV3()

with open("hh.csv", "r") as csvfile:
	rows=csvfile.read().splitlines()

	for index, row in enumerate(rows):
		rows[index] = row.split(",")

	header = rows.pop(0)

	nestdict={}
	for index, row in enumerate(rows):
		line = {key:value for key, value in zip(header,row)}
		nestdict[index]=line


#	for key, value in zip(header,row):
#		line[key]=value
#		nestdict[index]=line

GeoJSON_objects=[]

for key in nestdict:
	time.sleep(1)
	
	try:
		address,(latitude, longitude) = geolocator.geocode(nestdict[key]["Address"])
	
	except:
		print "Unable to find", nestdict[key]["Name"]

	else: 
		object={
			"type": "Feature",
			"geometry": {
					"type" : "Point",
					"coordinates": [longitude, latitude]
			},
			"properties":{
				"marker-symbol": "bar",
				"Name": nestdict[key]["Name"],
				"Address": nestdict[key]["Address"],
				"Days": nestdict[key]["Day"],
				"Specials": nestdict[key]["Details"],
				#"Hours": nestdict[key]["Time"],
			}
		}

		GeoJSON_objects.append(object)

geo={
			"type":"FeatureCollection",
			"features": GeoJSON_objects

}

import json

with open("file_name.json", "w") as jsonfile:
	jsonfile.write(json.dumps(geo, indent=4, sort_keys=True))

print "done"
