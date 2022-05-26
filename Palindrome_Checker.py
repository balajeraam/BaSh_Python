input_word = input("Enter your word please >> ").lower()

word_length = len(input_word)

reverse_word=""
count = 0
for i in input_word :
    character_position= word_length-count
    reverse_index=character_position-1
    reverse_character = input_word[reverse_index]
    reverse_word+=reverse_character
    count+=1

if input_word == reverse_word :
    print("This word is a Palindrome")
else:
    print("This word is NOT a Palindrome")
