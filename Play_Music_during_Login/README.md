Objective of this project is to play a predefined music when the user logs in to a windows system.

There are two variants of the same automation in this repository
- Level 1 : Simpler variant where full duration of the music file is played. 
- Level 2 : In this variant, we also control duration for which the music will play. A song that actually plays for 60 seconds can be controlled to play only upto 10 seconds

Step 1 - Create the python file that plays music. 
- Playsound module takes care of music playing part. This is very straightforward
- In the Level 2 program, duration to play the music is designed using the threading functionality to run parallel threads
- Using the threading module , create a separate program thread where the music is played
- The thread where music is played is declared as a "daemon" thread. When a thread is declared as daemon thread, it runs in the background
- In the main thread timer is made to run for certain duration e.g. 10 seconds
- Beauty of the using daemon thread is that when the main thread is complete, daemon thread is also stopped automatically.
- Daemon threads by design plays the proverbial second fiddle and supports the main / non - daeomonic threads.


Step 2 - Create a windows batch file that links where python.exe is stored in the system to actual python file.
- Open notepad.
- Copy the content from batch file template.
- Type python.exe on the search bar in windows. This will open up a dialog box. On the header path where this file is stored will appear.
- Replace A with path where python.exe is stored in your computer.
- Replace B with path where the relevant music playing python file (level 1 or level 2 file)  is saved.
- save the note pad with filename and .bat extension.
- Additional info - @echo off command in the batch file ensures that when the program is executed command prompt opens up, but the actual commands are not displayed
- Additional info - "exit 0" will ensure once the the python program is executed, windows command prompt will close automatically.
- Additional info - if "pause" is used in place of "exit 0", after the program gets executed, command prompt needs manual closure.

Step 3 - Create a task in Windows task scheduler to run the batch file.Detailed steps are as follows :
- Open Task Schedule
- Select Create Task
- Provide a Name for the task
- Select Run only when user is logged on
- Create new Trigger
- For "Begin the task", select "At Log on". Select "Specific user" and "User Name"
- Under the Action tab, select new action
- In the Action type, select “Start a new program”
- Browse and choose the file path for the Batch file that links python.exe to python music playing file
- By default , task is started only when the system is connected to AC main supply and not when it is running on battery. It runs when connected to any network
- Please review and adjust default conditions in the  "Conditions" tab before finalizing the task.
