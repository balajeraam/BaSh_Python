class VignereEncryption:
    def __init__(self,input_message,vignere_key):
        self.input_message = input_message
        self.vignere_key=vignere_key
        self.alphabet_list_sequence = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
    def text_to_list_converter(self,text_input):# To convert input text, vignere text into list
        final_list=[]
        for i in text_input:
            final_list.append(i)
        return final_list
    
    def get_vignere_message(self):# Generating vignere message
        vignere_message = ""
        inx=0
        for character in self.input_message :
            if character in self.alphabet_list_sequence :
                vignere_character = self.vignere_key[inx]
                if inx == len (self.vignere_key) -1 :
                    inx = 0
                else :
                    inx+=1
            else :
                vignere_character = character
            vignere_message+=vignere_character
        return vignere_message
    
    def get_output_message(self,inplist,viglist,encdec):# Engine to generate encrypted / decrypted output
            output_message=""
            cmx=0
            for character in inplist :
                if character in self.alphabet_list_sequence :
                    vignere_character = viglist[cmx]
                    shift = self.alphabet_list_sequence.index(vignere_character) 
                    encrypted_alphabet_sequence = []
                    inx=0
                    for alphabet in self.alphabet_list_sequence :
                        if (inx+int(shift)) == len(self.alphabet_list_sequence):
                            inx = -1*(shift)
                
                        encrypted_alphabet_sequence.append(self.alphabet_list_sequence[(inx+(shift))])
                        inx+=1
                    if encdec =="enc" :# identifying output character for encryption
                        alphabet_position = self.alphabet_list_sequence.index(character)    
                        output_character = encrypted_alphabet_sequence[alphabet_position]
                    
                    else:# identifying output character for decryption
                        alphabet_position = encrypted_alphabet_sequence.index(character)  
                        output_character = self.alphabet_list_sequence[alphabet_position]                        
                
                else:
                    output_character = character
                output_message+=output_character
                cmx+=1
            print("Output Message >> ",output_message)

inpt_msg = input("Please enter text that needs encryption or decryption >> ").lower()
vig_key = input ("Please enter the Vignere Encryption key >> ").lower()
encr_decr = input ("For encryption enter ENC, for decryption enter DEC >> ").lower()

vig_transform = VignereEncryption(input_message=inpt_msg,vignere_key=vig_key)
vig_msg = vig_transform.get_vignere_message()
alist=vig_transform.text_to_list_converter(inpt_msg)
blist = vig_transform.text_to_list_converter(vig_msg)
vig_transform.get_output_message(inplist=alist,viglist=blist,encdec=encr_decr)   
