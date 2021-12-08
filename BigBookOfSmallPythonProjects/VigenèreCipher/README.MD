Credits for the problem - Big book of Small Python Projects by Al Sweigart 

Please note that I have created the program without looking into the actual solution approach in the book. Hence solution approach will be different.

Objective is to design a program that can perform both encryption and decryption of message based on Vigenère cipher. 

Prerequisite – Knowledge of Caesar Cipher. Please refer to the other folder in Github where I have explained code creation approach for Caesar Cipher.

Vigenère Table forms the basis for Vigenère Cipher. Please refer to the picture in the folder.
Image credit: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html

•	When Vigenère encryption key “fun” is applied on input text “What is your name?”, Vigenère message will become “funf un fu nfun?” and final encrypted output will become “bbny cf dihw hnry?” based on the Vigenère table. Please note all special characters are kept as such in the Vigenère message

Approach to the problem

•	By using the "class" approach, we have re-usable block of code that can be used for both encryption and decryption.

•	Step 1: Generate Vigenère message. 

•	Step 2: Convert input message & Vigenère message into list using the custom  “text_to_list” method created within our “VigenèreEncryption” class. Converting into list will help us easily identify position within a particular list and a character that belongs to that position.

•	Step 3: We use the same “get_output_message” method for both encrypted and decrypted output. Only the last step in identifying the output character will differ. During encryption, we take the input character, find it’s position in a standard alphabet sequence and check in that position what character exist in an encrypted alphabet sequence. This logic is reversed for decryption.
