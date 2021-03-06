# install pywhatkit module from cmd prompt for Windows >> pip install pywhatkit
# install pywin32 >> pip install pywin32-- I was asked to install this module during the first run

import pywhatkit as pkit
import datetime as dt
import time

#To calculate the current moment
this_moment = dt.datetime.now().strftime("%y%m%d_%H%M%S")

# Adding the current moment to the file name. 
# This will ensure every time the program runs, it creates files with same name and only difference being the date and time.
# This will help in future automation if we have anothder dependent job to pick up files for a particular date.
# Replace << Your path >> with directory you would like to save. Remember to use "/ " and not "\"
file_path = f"Your path_{this_moment}.png"


#Active internet connection is required to execute the following step.
#RGB values decide the ink color of final handwritten message.
#Adding a '\n' to the message gives the same effect of pressing the RETURN KEY in keyboard.
pkit.text_to_handwriting("Dear receiver\nThis hand written message was created using Python.\nSent from a computer using Python\nby\nsender",save_to=file_path,rgb=(120,20,10))

#Introducing a delay to ensure there is enough time given for file generation in previous step
time.sleep(20)

# Replace << Receiver_Phone_Number >> with phone number starting with country code starting in + format. e.g. for Switzerland , start with +41
# Handwritten message is now available as a PNG file."Caption" argument captures the message that will be sent in whatsapp. 
# Replace << Test message >> with message you would like to add using the caption
# Wait time adds a delay. This gives sender an opportunity before the message is sent

pkit.sendwhats_image(phone_no="Receiver_Phone_Number",img_path=file_path,caption="Test Message",wait_time=5,tab_close=True)
