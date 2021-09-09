Step 1 - Create the python file that can generate reminders. 

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

Step 3 - Create a task in Windows task scheduler and provide batch file as input. For further details, please refer to the attached word document.

Step 4 - Provide criteria in the task scheduler e.g. when to start , what frequency, conditions like should the user be logged in ? etc          
