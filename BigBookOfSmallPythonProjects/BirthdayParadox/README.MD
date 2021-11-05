Credits for the problem - Big book of Small Python Projects by Al Sweigart Level 1 solution is a solution designed by me before looking into the actual solution in the book 

Objective is to design a program that does the following :
- User will provide number of trials
- User will provide group size
- Based on the group size , system should generate random birthdates.
- System to calculate the probability of two people in a group having same birthday for a given number of trial

Approach to the problem
- Instead of working with dates, my version of the program is designed to generate a random number between 1 and 365 , which is equivalent to generating a date
- In every iteration, original list is created using randomly generated numbers that matches the group size (using for loop)
- De-duplicated version of the list is calculated by the system (again using for loop)
- If length of original list and de-duplicated list are same, there was no duplicates in the original list , else original list had duplicates.
- In the iteration, after every trial, if length was different between the two lists, variable "has_duplicates" got increased by 1
- Ratio of  final count of has_duplicates to total trial size will give us the probability.
