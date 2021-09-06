# Install xml to dict from command prompt -- pip install xmltodict
import os
import datetime as dt
import time
import csv
import json
import xmltodict

# Requesting user to provide the directory where XML files are stored
source_dir= input("Enter directory where XML files are stored  >> ")

# In Windows separator used is "\". We need to modify it to separator "/" that python understands
source_dir= source_dir.replace(os.sep,"/")

# Calculating current time in yymmdd_HHMMSS format , with time in 24 hr format. 
this_moment = dt.datetime.now().strftime("%y%m%d_%H%M%S")


new_dir=f"{source_dir}/{this_moment}"

# Create a new sub-folder with name same as that of timestamp. This will be used to save converted files
if not os.path.exists(new_dir):
  os.makedirs(new_dir)

# Create a summary file that captures details of all files processed . 
# Summary file will also be created and saved within the exclusive sub-folder.
summary_file_path = f"{new_dir}/Summary_{this_moment}.csv"
summary_file = open(summary_file_path,'w')
summary_file.close()

# Delay (in seconds) introduced to ensure file is saved before we proceed to next steps
# Decide if it is necessary in your case and adjust the time based on the scenario
time.sleep(10)

# Writing the header row in the summary csv file
summary_file_header = ['File_Name','Extension']
with open(summary_file_path, 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)

    # write the header row in Summary file
    writer.writerow(summary_file_header)

# Delay (in seconds) introduced to ensure file is saved before we proceed to next steps
# Decide if it is necessary in your case and adjust the time based on the scenario
time.sleep(5)

# Looping inside the folder and capture file name, file extension and individual file path.
for filename_with_extension in os.listdir(source_dir):
    file_name,file_extension = os.path.splitext(filename_with_extension)
    summary_file_item = [file_name,file_extension]
    ind_file_path = f"{source_dir}/{filename_with_extension}"
    
    # Applying special rule for files that have a "xml" extension
    if filename_with_extension.endswith(".xml"):

      # open the input xml file and read data and convert them to json data 
      with open(ind_file_path) as xml_file: 
        my_dict = xmltodict.parse(xml_file.read())
        # Adding the "indent" and "sort keys" arguments results in pretty printed i.e.human read friendly format 
        json_data = json.dumps(my_dict,indent=4,sort_keys=True)
        
        # write Json data to a individual files
        # Converted files have same file name as that of original with time stamp appended
        target_name= f"{new_dir}/{file_name}_{this_moment}.json"
        with open (target_name,"w") as json_file:
          json_file.write(json_data) 
          json_file.close()

      # After every file is converted, program also updates the summary file
      with open(summary_file_path, 'a', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)

        # write the individual item row
        writer.writerow(summary_file_item)
        # Delay (in seconds) introduced to ensure file is saved before we proceed to next steps
        # Decide if it is necessary in your case and adjust the time based on the scenario
        time.sleep(5)
