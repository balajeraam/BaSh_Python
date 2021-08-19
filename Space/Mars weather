#This program relies on mars curiosity rover data exposed via maas
#Keyless API used

import requests
import json

# Getting data using API and converting into dictionary format that will be easy to read data

response = requests.get("https://api.maas2.apollorion.com").json()

# Finding value for the "Key" : Sol. This is the martian day passed since the landing
sol = response['sol']

# Converting martian days to Earth days
day = int(sol * (3299/3212))

print("Time passed since the landing of Curiosity Rover")
print("*"*48)
print(">> Martian days (Sols) : ",sol)
print(">> Earth days passed   : ",day)
print("Weather forecast for Tosol (equivalent of today) ")
print(" ")
print("*"*48)
print(">> Minimum temperature : ",response['min_temp'], "Celsius")
print(">> Maximum temperature : ",response['max_temp'],"Celsius")
print(">> Sunrise at          : ",response['sunrise'])
print(">> Sunset at           : ",response['sunset'])
