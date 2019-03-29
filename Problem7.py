# Aidan Conlon 28 March 2019
# This is the solution to Problem 7
# Write a program that takes a positive floating point number as input and outputs an approximation of its square root

import math                                                                             # This will import math module

UserInput = float(input("Please enter a positive number: "))                            # Ask user to input a value to perform square root calculation on.
                                                                                        # The input number is declared as a float and is given name UserInput
UserOutput = math.sqrt(UserInput)                                                       # Perform the Square ROot function on the value entered by ser and call result - UserOutput
RoundedUserOutput = round(UserOutput, 2)                                                # Use round function to round the resul toof the square root calculation to 2 decimal places 
                                                                                        # and call the result of this operation RoundedUserOutput    
if (UserInput % UserOutput == 0):                                                       # To check if the result is square root with no decimal values, divide the User entered value by the 
                                                                                        # new derived user output value to see if there is any carry in the calculation.
    print("The Square Root of %0.f is precisely %0.f." %(UserInput, RoundedUserOutput))   # If there is no carry then the answer is precise and not approx. so output the text and value to screen. 
else:                                                                                   # But if the division does result in a  carry the it is not exact and therefore
    print("The Square Root of %f is approx. %0.1f!" %(UserInput, RoundedUserOutput))    # the value is an approximate value rounded to 1 decimal point and this value is outpuit to screen with text. 
quit()                                                                                  # Quit program    

# I would like to improve this code to remove the trailing zeros from the float value I output at the end i.e. instead of "The square root of 81.90000 is approx 9!"
# it would be best if this would display "The square root of 81.9 is approx 9!"
# If I get time I will see if I can rememdy this before final deadline