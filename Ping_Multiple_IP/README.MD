Implementation approach as follows :

- Using Excel file (.XLSX format) as data source
- -Openpyxl module does the heavylifting to read and write data into the file
- -Only Three cells i.e timestamp,status and comments in the excel are read / write relevant. This allows user to maintain other relevant details about the ip address.

- Pinging the server :
- -The Platform module helps in identifying if the system is Windows or non-windows system to decide the number of packets to be sent for ip status verification
- -Subprocess module helps in performing the command and capturing the "Exit code" to make meaningful result

- Periodic running of program :
- -This python program can be run as a scheduled task on hourly basis or other frequency that suits the admin needs.
- -Date time module helps in capturing details of the last time the project was executed.
