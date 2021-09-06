from tkinter import *
import tkinter as tk
import requests
import json

# Keyless API to source weather information from curiosity rover
response = requests.get("https://api.maas2.apollorion.com").json()
sol = response['sol']
day = int(sol * (3299/3212))

# Tkinter output window design
win = Tk()
win.title("Mars Weather Forecast")
win.geometry("400x350")
win.config(bg='grey')

# Create a reusable label creation and pack template for a given text
def LabelTemplate(texte):
    label_name = Label(win,text=texte,font=("calibri",12,"bold"),bg="grey",foreground="white")
    label_name.pack(anchor = W)


LabelTemplate(texte="Time passed since the landing of Curiosity Rover")

star="*"*42
LabelTemplate(texte=star)

mars_days=">> "+str(sol)+" Martian days (Sols) passed"
LabelTemplate(texte=mars_days)

earth_days=">> "+str(day)+" Earth days passed"
LabelTemplate(texte=earth_days)

blank=" "
LabelTemplate(texte=blank)

weather_forecast = "Weather forecast for Tosol (equivalent of today) "
LabelTemplate(texte=weather_forecast)

LabelTemplate(texte=star)

min_temp = ">> Minimum temperature : "+ str(response['min_temp']) + " degree Celsius"
LabelTemplate(texte=min_temp)

max_temp = ">> Maximum temperature : "+ str(response['max_temp']) + " degree Celsius"
LabelTemplate(texte=max_temp)

sunrise = ">> Sunrise at          : " + str(response['sunrise'])
LabelTemplate(texte=sunrise)

sunset = ">> Sunset at           : " + str(response['sunset'])
LabelTemplate(texte=sunset)

# Output window will close automatically after 30 seconds.
win.after(30000,win.destroy)

win.mainloop()
