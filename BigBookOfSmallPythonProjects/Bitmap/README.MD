Credits for the problem - Big book of Small Python Projects by Al Sweigart

Except for the split line idea, all other solution components designed by me.: 

Objective is to convert a reference bitmap file  with string input provided by user :

- Reference bitmap images was taken from  https://inventwithpython.com/bitmapworld.txt . Again credit to Al Sweigart
- Since original bitmap is a multi-line text, it is important to split full text into individual lines and perform the transformation
- Outer "for" loop : splitting of text results in list containing every single line. Outer loop helps us in iterating across the lines.
- inner "for" loop : within the line, every character needs transformation. 
- An empty text is taken, every character inside the line is transformed and concatenated to the empty text and final text is printed for every line.
