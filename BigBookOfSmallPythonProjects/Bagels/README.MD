Credits for the problem - Big book of Small Python Projects by Al Sweigart
Level 1 solution is a solution designed by me before looking into the actual solution in the book
Objective is to design a game with following criteria :
- User will have to guess a random 3 digit number defined by the system
- A maximum of 10 attempts are possible
- System gives clue after every attempt
- System clues : "Pico" - Right digit in wrong place, "Fermi" - Right digit in right place, "Bagels" if no digit matches numbers
Enhancements in Level2 solution
-This solution is based on Class
-In Level 1 solution, depending on which digit system checked before the break statement, it is possible to get either Fermi or Pico status
-Level 2 solution prioritizes Fermi status over Pico status.
