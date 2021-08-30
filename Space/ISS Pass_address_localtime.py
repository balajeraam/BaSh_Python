# This program captures details of time (local) at which ISS passes over an address
# 2 APIs used 
# -- Finding GPS coordinates from address : Opencage API 
# -- Finding ISS fly by time over coordinates -- Open Notify API

# install opencage using command << pip3 install opencage >> in the windows command prompt
from opencage.geocoder import OpenCageGeocode

key = 'YOUR API KEY'
# << YOUR API KEY >> to be replaced by the free trial API Key from https://opencagedata.com/api

geocoder = OpenCageGeocode(key)

query = input (" Your address please >> ")
results = geocoder.geocode(query)

la = results[0]['geometry']['lat']
lo = results[0]['geometry']['lng']
ofs = results[0]['annotations']['timezone']['offset_sec']

sla = str(la)
slo = str(lo)
print ("Location latitude :  ",sla)
print ("Location longitude:  ",slo)

# Credits for ISS Pass time retrieval --  https://www.dataquest.io/blog/python-api-tutorial/

# import "requests" module through pip install request prior to the code
import requests
import json
from datetime import datetime , timedelta


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=10)
    print(text)


# Here is the API part. 
response = requests.get("http://api.open-notify.org/iss-pass.json?lat="+ sla + "&"+"lon="+ slo)

# To check if connection is established properly, try first -- print (response.status_code). 
# This should return status 200

# Typing the command << jprint(response.json()) >> will result in a response that has 3 components.
# i.e message status, request and response details

pass_times = response.json()['response']
# We are trying to ignore the request status and request details. Hence giving the Key field response

# Response has duration and rise time component. In the next step , we are carving out a risetime tuple.
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

# command << print(risetimes) >> will show a "epoch" UTC time. This needs conversion to local time. 
# Dataquest.io article shows date in UTC. In this program we have additionally converted UTC to local time using offset time retrieved from OpenCage API
# UTC to local time conversion is done by retrieving local time offset from opencage API response and using timedelta function in python datetime module

ltimes = []

print(" International Space Station (ISS) will pass over the location at (Local time) : ")
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    ltime = time + timedelta(seconds= ofs)
    ltimes.append(ltime)
    print(ltime)
