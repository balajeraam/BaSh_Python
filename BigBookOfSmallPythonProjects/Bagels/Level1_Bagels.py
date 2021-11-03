# Pico - Right digit in wrong place , Fermi - Right digit in right place, Bagels if no digit matches numbers
import random
from random import randint

random_number = str(random.randint(100,999))

attempt = 1
while attempt < 12 :
    
    if attempt == 11:
        print("Sorry. You crossed 10 attempts")
        print(f"{random_number}  is the right answer")
        break
    
    input_number = str(input("input 3 digit number between 100 and 999 >> "))

    if random_number == input_number :
        print(f"yes ..{random_number}  is the right answer")
        print(f"you cracked it in {attempt} number of attempts")
        break

    else : 

        i0 = input_number[0]
        i1 = input_number[1]
        i2 = input_number[2]
        r0 = random_number[0]
        r1 = random_number[1]
        r2 = random_number[2]

        i_inx = 0
        stater = " "
        
        for i in input_number :
            r_inx = 0
            for r in random_number :
                if (random_number[r_inx] == input_number[i_inx] ) and (r_inx == i_inx ) :
                    stater = "Fermi"
                    break
                elif (random_number[r_inx] == input_number[i_inx] ) :
                    stater = "Pico"
                    break
                r_inx+=1
            i_inx+=1

        if (stater !="Pico") and (stater !="Fermi") :
            stater = "Bagels"
        
        print(stater)

    attempt+=1
