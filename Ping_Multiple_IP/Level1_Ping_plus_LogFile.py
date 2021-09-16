#import relevant modules
import openpyxl
import time
import datetime
import subprocess


# Requesting user to provide the path where XLSX file containing server ip list is stored
path = input("Enter path where .XLSX containing server list is stored  >> ")

# In Windows separator used is "\". We need to modify it to separator "/" that python understands
path = path.replace(os.sep,"/")

wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
for row in range (2,sheet_obj.max_row+1):
    
    ip_address_cell = sheet_obj.cell(row,1)
    # parameter -n is for windows machine
    command = ['ping','-n','3', ip_address_cell.value]
   
    run_time = datetime.datetime.now()
    timestamp_cell = sheet_obj.cell(row,4)
    timestamp_cell.value = run_time

    outcome = subprocess.call((command),stdout=subprocess.DEVNULL)
    ip_status_cell = sheet_obj.cell(row,5)
    ip_status_cell.value = outcome

    comment_cell = sheet_obj.cell(row,6)
    if outcome == 0 :
        comment_cell.value = "Reachable"
    else :
        comment_cell.value = "Not Reachable"
    
    wb_obj.save(path)
    time.sleep(4)
