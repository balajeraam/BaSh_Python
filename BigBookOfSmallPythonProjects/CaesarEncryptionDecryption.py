class CaesarEncryption:
    def __init__(self,input_message,shift):
        self.input_message = input_message
        self.shift=shift

    def get_shifted_message(self):
        alphabet_list_sequence = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        encrypted_alphabet_sequence =[]
        inx=0
        for alphabet in alphabet_list_sequence :
    
            if (inx+int(self.shift)) == len(alphabet_list_sequence):
                inx = -1*(self.shift)
        
            encrypted_alphabet_sequence.append(alphabet_list_sequence[(inx+(self.shift))])
            inx+=1
        

        #This section handles creation of the encrypted message
        encrypted_message = "" 
        for character in self.input_message :
            if character in alphabet_list_sequence :
                chindex = alphabet_list_sequence.index(character)
                encrypted_character = encrypted_alphabet_sequence[chindex]  
                encrypted_message+=encrypted_character
            else :
                encrypted_message+=character
            
        print(" ")
        print("Shift "+str(self.shift),">>","Message: "+ encrypted_message)
        print(" ")

print(" ")
enc_dec = input("""For Encryption ,type "enc",for Brute-Force Decryption: type "dec" >> """).lower()
print(" ")

if enc_dec == "enc" :
    in_message = input("Enter text that needs encryption >> ").lower()
    print(" ")
    print("-Shift is the number of position to be shifted in the alphabet sequence")
    print("-For e.g. when shift value of 1 is applied ,car becomes dbs ")
    print("-Value of shift should fall between 1 and 25,both 1 & 25 inclusive")
    print(" ")
    
    sft = int(input("Enter the value for shift in alphabet >> "))
    encryption = CaesarEncryption (input_message=in_message,shift=sft)
    encryption.get_shifted_message()

elif enc_dec == "dec":
    in_message = input("Enter text that needs decryption >> ").lower()
    print("-Shift is the number of position to be shifted in the alphabet sequence")
    print("-For e.g. when shift value of 1 is applied ,car becomes dbs ")
    print("-Value of shift should falls between 1 and 25,both 1 & 25 inclusive")
    sft =1
    while sft < 26 :
        decryption = CaesarEncryption (input_message=in_message,shift=sft)
        decryption.get_shifted_message()
        sft+=1
