# Aidan Conlon - 22 March 2019
# This is the solution to Problem 4
# Write a program that asks the user to input any positive integer and outputs the
# successive values of the following calculation. At each step calculate the next value
# by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
# it by three and add one. Have the program end if the current value is one.

UserInput = input("Please enter any positive integer:") # Print to screen the comment and take a value entered by the user.
                                                        # calling it UserInput
try:                                                    # Use Try to see if value entered is an Integer or not.
    y = int(UserInput)                                      # Let y equal to the value entered by the user  as an integer - if possible
    if y <= 0:                                              # If the value entered is less than 0 then it is not a positive integer and 
        print("That is not a positive integer")                # print to screen letting user know it is anot a positive integer and then 
        quit()                                                  # quit.
    while y > 0:                                            # As long as the user entered a positive integer then using a while loop , so long as y is greater than 0 check for the following conditions
        if y == 1:                                          # If y is 1 
            quit()                                              # then quit
        if y %2 != 0:                                   # If y is divisible by 2 with a denominator 
            y = ((y * 3) + 1)                               # multiply y by 3 and add 1
            print(y)                                        # print new value of y to screen
        if y %2 == 0:                                   # If y is divisible by 2 with no denominator then 
            y = y / 2                                       # divide y by 2
            print(y)                                        # and print this new value to screen

except ValueError:                                      # The Try Exception means that the value entered is not an integer so
    print("That is not an integer")                         # Print to screen it is not an integer and 
quit()                                                  # finish.


