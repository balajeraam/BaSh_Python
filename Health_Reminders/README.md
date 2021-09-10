This project handles steps required to trigger automated health reminders on a Windows system.

Step 1 - Create the python file that generates reminders. Tkinter module takes care of the following aspects:
- Pop up of window containing reminders
- Bell sound when the message window pops up
- Automatic closure of window after certain time e.g.10 seconds.

Step 2 - Create a windows batch file that links where python.exe is stored in the system to actual python file. 
- Open notepad.
- Copy the content from batch file template.
- Type python.exe on the search bar in windows. This will open up a dialog box. On the header path where this file is stored will appear.
- Replace A with path where python.exe is stored in your computer.
- Replace B with path where the reminder python file is saved.
- save the note pad with filename and .bat extension.
- Additional info - @echo off command in the batch file ensures that when the program is executed command prompt opens up, but the actual commands are not displayed
- Additional info - "exit 0" will ensure once the the python program is executed, windows command prompt will close automatically. 
- Additional info - if "pause" is used in place of "exit 0", after the program gets executed, command prompt needs manual closure.

Step 3 - Create a task in Windows task scheduler to run the batch file.Detailed steps are as follows :
- Open Task Schedule
-	Select Create Task
-	Provide a Name for the task 
-	Select Run only when user is logged on  
-	Create new Trigger
-	Select the start time for reminder, run daily and repeat every 1 hour. “Indefinitely” to be selected for “For a duration of” 
-	Under the Action tab, select new action 
-	In the Action type, select “Start a new program”
-	Browse and choose the file path for the Batch file that links python.exe to python reminder file
-	Create additional conditions if required e.g. should it run when computer is running on battery, on a preferred network etc
