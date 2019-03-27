# Aidan Conlon - 27 March 2019
# This is the solution to Problem 6
# Write a program that takes a user input string and outputs every second word.

UserInput = input("Please enter a string of text:")    # Print to screen the comment and take a value entered by the user.

for i, word in enumerate(UserInput.split()):           # Use a for loop to pull each word from the sentence using a split function
    if i %2 == 0:                                      # if i is divisible by 2 with no carry then it is the 1st, 3rd, 5th word etc. in the entered sentence.
        print("%s" % (word), sep=' ', end=' ')         # Print the string given the value of word (for this iteration of i), usng concatenation of each word seperated by a space 
quit()                                                 # Quit the program

