# Aidan Conlon - 20 March 2019
# This is the solution to Problem 2
# Write a program that outputs whether or not today is a day that begins with the
# letter T.

import datetime

if datetime.datetime.today().weekday() == 1 or 3: # Modnday is 0 and Sunday is 6
  print("Yay! The day begins with a T.")
else:
  print("Unfortunately it does not begin with a T.")