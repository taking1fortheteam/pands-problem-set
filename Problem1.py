# Aidan Conlon - 20 March 2019
# This is the solution to Problem 1
# A Program that asks the user to input any positive integer and outputs the
# sum of all numbers between one and that number.

#  Ask user to enter a positive integer
User_Input = input("Enter positive Integer : ")

# I need to decipher if it is an integer an dwhether it is, is it a positive one!


# Check to see if entered characters are a number or string
try:                                    # Try the value entered as an integer? 
    val = int(User_Input)               # Value entered is an integer (i.e. 3)
    if val <= 0:
        print("That is not a positive integer") # Print to screen it is not an integer and finish.
        quit()
    i = val                             # let i equal to integer value            
    while (i > 0):                          # While loop to check for i is not 0
        i = i-1                             # decrement i by 1
        val = (val + i)                     # make val equal to old val plus value of i (i.e. 3 + 2) 
    print ("The sum is" , val)          # Print to screen "The sum is" and the value stored by val.
    quit()                              # Quit

# If value entered is not an integer then:   
except ValueError:              
    print("That is not an integer") # Print to screen it is not an integer and finish.


