from tkinter import *
import tkinter as tk
import requests
import json
import playsound

response = requests.get("https://api.maas2.apollorion.com").json()
sol = response['sol']
day = int(sol * (3299/3212))

win = Tk()
win.title("Mars Weather Forecast")
win.geometry("400x350")
win.config(bg='grey')

#Replace <<File path>> with actual file path
#Additional argument 0 ensures the soundfile is played in background when other parts of code are executed 
#If Zero argument is not used , python file is play the sound component first and then initiates the content display 
playsound.playsound("C:/Users/balaj/Downloads/PinkPanther30.wav",0)


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

win.after(45000,win.destroy)

win.mainloop()
