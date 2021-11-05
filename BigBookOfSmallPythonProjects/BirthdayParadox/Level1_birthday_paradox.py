import random

group_size = input("Please enter the group size >> ")
trial_size = input("Please input the number of trials >> ")

has_duplicates = 0
no_duplicates = 0
for i in range (int(trial_size)):
    print(f"Trial number {i+1} in progress..")
    randomlist = []
    for i in range(0,int(group_size)):
        n = random.randint(1,365)
        randomlist.append(n)
    randomlist.sort()
    
    dedup_randomlist = []
    inx =0
    for i in range(0,int(group_size)):
        if randomlist[inx] not in dedup_randomlist:
            dedup_randomlist.append(randomlist[inx])
        inx+=1
    
    if len(randomlist) == len (dedup_randomlist):
        no_duplicates+=1
    else:
        has_duplicates+=1

probability = (has_duplicates*100/int(trial_size))
print(f"A group of {group_size} people, based on {trial_size} number of random birthday generation ")
print(f"trials, there is a {probability}% probability,that atleast two of them share same birthday")  
