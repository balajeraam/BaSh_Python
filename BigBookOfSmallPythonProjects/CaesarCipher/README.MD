Credits for the problem - Big book of Small Python Projects by Al Sweigart Level 1 solution is a solution designed by me before looking into the actual solution in the book

Objective is to design a program that can perform both encrpytion and decryption of message based on Caesar cipher.
Caeser cipher works on the basis of "shift". A "shift" value of 1 make the word "go" become "hp" where the original letters are shifted by a letter in the alphabet sequence

Approach to the problem

- By using the "class" approach, we have re-usable block of code that can be utilized both for encryption and decryption.
- get_shifted_message method first converts the standard alphabet sequence into a sequence after the shift. e.g.. shift of 1 will result in b,c,d,e...a
- Input message is taken, position of the character in alphabet sequence is checked.For e.g. if the character is b, the position of b in alphabet sequence
- In the next step, in the same position, we identify the character present in the shifted alphabet sequence. so program will find identify c in our example
- All characters in the message are identified and encrypted message is built. When a character is not present in the original alphabet list, that character is retained as such.
- Encryption :User input is taken for both message and shift value and passed into the class to print the encrpyted message 
- Decryption : Only user input is taken and a while loop is set to run for all shift values between 1 and 25
