# Aidan Conlon 28 March 2019
# Write a program that outputs today’s date and time in the format “Monday, January
# 10th 2019 at 1:15pm”.

import datetime                                                                                                                 # Import date time from system
x = datetime.datetime.now()                                                                                                     # Let X equal to current date and time values

                                                                                                                                # The following lines are just if statements in order to figure 
                                                                                                                                # out if the date should be followed by a st, nd, rd, or th 
                                                                                                                                #i.e. 1st, 2nd, 3rd, or 4th.

if int(x.strftime("%d")) == 1 or int(x.strftime("%d")) == 21 or int(x.strftime("%d")) == 31:                                    #If the date equals 1, 21 or 31 
    i = "st"                                                                                                                    #Let i equal to the value st (so it is 1st or 21st or 31st)

if int(x.strftime("%d")) >= 4 and int(x.strftime("%d")) <= 20 or int(x.strftime("%d")) >= 24 and int(x.strftime("%d")) <= 30:   # If the date equales a value between 4 and 20 or between 24 and 30
    i = "th"                                                                                                                    # then let i = th (i.e. th, 5th, 24th, 25th)

if int(x.strftime("%d")) == 2 or int(x.strftime("%d")) == 22:                                                                   # If the day of month equals 2 or 22 then
    i = "nd"                                                                                                                    # let i equal to nd (i.e. 2nd or 22nd)

if int(x.strftime("%d")) == 3 or int(x.strftime("%d")) == 23:                                                                   # And finally if the day of month equals 3 or 23 then 
    i = "rd"                                                                                                                    # let i equal to rd (i.e. 3rd or 23rd)

                # Day of week       Month       Date (1-31)+i             Year   at               Hours:Minutes       PM or AM
print(x.strftime("%A,"), x.strftime("%B"), x.strftime("%d")+i, x.strftime("%Y"),"at", x.strftime("%I:%M"), x.strftime("%p"))    # Print to the screen the various items 

quit()                                                                                                                          # QUit
