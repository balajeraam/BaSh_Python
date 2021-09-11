# Please refer to the README.MD file for detailed explanation of code
# import relevant python modules
import playsound
import time
from threading import Thread

#Replace << >> with path where the music file (.mp3 or .wav) is stored.
music_path= "<< >>"

# Define custom class to play music
def PlayMusic() : 
    playsound.playsound(music_path)

# Start a thread where the music is played
t1=Thread(target=PlayMusic)
# Marking the thread as daemon thread , this becomes a background thread and shutsdown whenever the mainthread is closed
t1.daemon = True
#start the thread
t1.start()

# Main thread is the timer 
start_time=time.time()
# In this example 15 second timer is set . Modify timer value to suit the need
while (time.time()-start_time) < 15 :
    # Since there is no output or action expected when the mainthread is running, "pass" is used
    pass
