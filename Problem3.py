# Aidan Conlon - 21 March 2019
# This is the solution to Problem 3
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible
# by 6 but not 12.

i = 1000                            # Set i to 1000
x = 1000                            # Set x to 1000

#                                    Print to screen following comment
print("The Values divisible by 6 but not divisible by 12 between 1,000 & 10,000 are:")

while i <= 10000:                   # While loop - while i is less than 10001 continue with this loop
    if x % 6 == 0 and x % 12 != 0:         # if x is divisible by 6 (no remainder) AND not divisible by 12 (remainder)
        print(x)                                # print the value of x to the screen
    i = i + 1                               # increment the value of i (for next iteration)
    x = x + 1                                # increment value of x (for next iteration)
quit()                              # Finish