# This program captures details of time at which Internation Space Station (ISS) passes over your city. 
# It uses an "Keyless" API. Since no key is involved, it helps beginners to understand mechanics of API

# Credits : https://www.dataquest.io/blog/python-api-tutorial/

# import "requests" module through pip install request prior to the code
import requests
import json
from datetime import datetime

lat = input("Please input latitude of your city >> ")
lon = input("Please input longitute of your city >> ")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=10)
    print(text)


# Here is the API part. 
response = requests.get("http://api.open-notify.org/iss-pass.json?lat="+ lat + "&"+"lon="+lon)

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

# command << print(risetimes) >> will show a "epoch" time. This will be converted into normal time.


times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
