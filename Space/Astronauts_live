# This program captures details of all the astronauts who are currently in space. 
# It uses an "Keyless" API. Since no key is involved, it helps beginners to understand the mechanics of API

# Credits : https://www.dataquest.io/blog/python-api-tutorial/

# import "requests" module through pip install request prior to the code
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=10)
    print(text)


# Here is the API part
response = requests.get("http://api.open-notify.org/astros.json")

# To check if connection is established properly, try first -- print (response.status_code). 
# This should return status 200

jprint(response.json())
