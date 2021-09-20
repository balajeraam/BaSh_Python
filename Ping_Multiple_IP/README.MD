Implementation approach as follows :

Using Excel file (.XLSX format) as data source
- Openpyxl module does the heavylifting to read and write data into the file
- Only Three cells i.e timestamp,status and comments in the excel are read / write relevant. This allows user to maintain other relevant details about the ip address.

Pinging the server :
- The Platform module helps in identifying if the system is Windows or non-windows system to decide the number of packets to be sent for ip status verification
- Subprocess module helps in performing the command and capturing the "Exit code" to make meaningful result

Checking if web application is accessible

Periodic running of program :
- This python program can be run as a scheduled task on hourly basis or other frequency that suits the admin needs.
- Date time module helps in capturing details of the last time the project was executed.

Levels explained :
Level 1
- Multiple servers are network-pinged for a response. Response captured, interpreted and saved in log file.
- Module Openpyxl for excel handling 
- Module time for a planned wait time between saving of different rows
- Module datetime to capture the date and time of execution. Since solution updates the same file after every run, it is critical to tag the results to timestamp
- Module subprocess to perform network ping 
- Module platform for identifying whether system is windows or non windows to trigger the right ping command
- Module OS to handle hierarchy separator or delimiter. When we copy a path from file properties. It has "\". However python understands "/"

Level 2 : 
- All capabilities in Level 1 plus the ability to get a http status code if the ip address is a web application
- Sometimes server will be active, but the application might be down or not accessible. This automation will help in identifying at what level it is not accessible.
- Only incremental module used in Level2 is the requests module to reach the web application and get the response code.
