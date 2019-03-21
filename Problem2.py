# Aidan Conlon - 21 March 2019
# This is the solution to Problem 2
# Write a program that outputs whether or not today is a day that begins with the
# letter T.

import datetime                                     # Import the date and time
                                                    # Do a  check to see if the current day is 1 - TUesday or 3 - Thursday
if datetime.datetime.today().weekday() == 1 or 3:   # Monday is 0 and Sunday is 6
  print("Yay! The day begins with a T.")                # If result is Tuesday or Thursday print to screen comment.
else:                                               # If day is not Tuesday or Thursday then 
  print("Unfortunately it does not begin with a T.")    # Print comment to screen


x = datetime.datetime.now()                         # As a checksum - let x equal to the current date / time.
print(x.strftime("%A"))                             # Print to screen the Day - strftime converts datetime to a  string
                                                    # %A reprsents the full Day ie. Wednesday instead of Wednesday to be printed.