# Fermi - Right digit in right place
# Pico - Right digit in wrong place
# Bagels if no digit matches numbers
import random
from random import randint

class BagelGame:
    def __init__(self,input_nr,rand_nr,stater="to_be_identified"):
        self.input_nr = input_nr
        self.rand_nr = rand_nr
        self.stater = stater
        i0 = self.input_nr[0]
        i1 = self.input_nr[1]
        i2 = self.input_nr[2]
        r0 = self.rand_nr[0]
        r1 = self.rand_nr[1]
        r2 = self.rand_nr[2]

    def check_fermi(self):   
        i_inx = 0 
        for i in self.input_nr :
            r_inx = 0
            for r in self.rand_nr:
                if (self.rand_nr[r_inx] == self.input_nr[i_inx] ) and (r_inx == i_inx ) :
                    self.stater = "Fermi"
                    break
                r_inx+=1
            i_inx+=1
        return(self.stater)

    def check_pico(self):
        i_inx = 0
        for i in self.input_nr :
            r_inx = 0
            for r in self.rand_nr:
                if (self.rand_nr[r_inx] == self.input_nr[i_inx] )  :
                    self.stater = "Pico"
                    break
                r_inx+=1
            i_inx+=1 
        return(self.stater)


random_number = str(random.randint(100,999))
attempt = 1
while attempt < 12 :
    print("Attempt  >> ",attempt)
    if attempt == 11:
        print("Sorry. You crossed 10 attempts")
        print(f"{random_number}  is the right answer")
        break

    input_number = str(input("input 3 digit number between 100 and 999 >> "))

    if random_number == input_number :
        print(f"Yes ..{random_number}  is the right answer")
        print(f"You cracked it in {attempt} attempts")
        break

    else:
        trial = BagelGame(input_nr=input_number,rand_nr=random_number)
        fermi_output = trial.check_fermi()
        pico_output = trial.check_pico()
        if fermi_output =="Fermi":
            print(fermi_output)
        elif pico_output == "Pico":
            print(pico_output)  
        else :
            print("Bagels")
    attempt+=1
