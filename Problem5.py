# Aidan Conlon - 22 March 2019
# This is the solution to Problem 5
# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime. 

UserInput = input("Please enter any positive integer:") # Print to screen the comment and take a value entered by the user.
                                                        # calling it UserInput
try:                                                    # Use Try to see if value entered is an Integer or not.
    y = int(UserInput)                                  # Let y equal to the value entered by the user  as an integer - if possible
    i = int(1)                                          # Using integers as flags for the calculations...i, x & z.
    x = int(0)                                          # x is the sum of the number of itterations resulted in a carry being created
    z = int(0)                                          # z is the sum of the number of itterations resulted in no carry being created i.e. if > 2 then not a prime
    if y <= 0:                                          # If the value entered is less than 0 then it is not a positive integer and 
        print("That is not a positive integer")             # print to screen letting user know it is anot a positive integer and then 
        quit()                                              # quit.
    if y == 1 or y == 2 or y == 3:                      # THis is the checking for conditions of the primes 1, 2 or 3 to be entered by the user.
        print("The number is a prime")                      # print that it is a prime and 
        quit()                                              # quit.
    else:                                               # else we need to check for all other conditions i.e. if not 1, 2 or 3 then is it a prime?
        while i <= y:                                       # while i is less than or equal to y - just creating the divisor in this line (starting at 1)
            if y % i  != 0:                                 # if we have a remainder then                       
                i = i + 1                                       # i gets to be incremented   
                x = x + 1                                       # and also x gets to be incremented - only if value entered by the user has a carry after division
            elif y % i == 0:                                # if we dont have a remainder
                i = i + 1                                       # i still gets incremented 
                z = z + 1                                       # z also gets incremented - only if the value entered by user is divisible by an int 
        if x >= 2 and z == 2:                               # if x > 2 then the value entered has been divisible by more than  1 and itself. and the number is not a prime
                                                            # AND z == 2 (z will be incremented to 2 because it is divisible by 1 and itself - therefore a prime)
            print("The number is a Prime")                      # print to screen that the number is a prime
        else:                                               # or else
            print("The number is not a prime")                  # print to screen that the value is not a prime

except ValueError:                                      # The Try Exception means that the value entered is not an integer so
    print("That is not an integer")                         # Print to screen it is not an integer and 
quit()                                                  # finish.


