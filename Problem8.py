# Aidan Conlon 28 March 2019
# Write a program that outputs today’s date and time in the format “Monday, January
# 10th 2019 at 1:15pm”.

import datetime
x = datetime.datetime.now()

if int(x.strftime("%d")) == 1 or int(x.strftime("%d")) == 21 or int(x.strftime("%d")) == 31:
    i = "st"

if int(x.strftime("%d")) >= 4 and int(x.strftime("%d")) <= 20 or int(x.strftime("%d")) >= 24 and int(x.strftime("%d")) <= 30:
    i = "th"

if int(x.strftime("%d")) == 2 or int(x.strftime("%d")) == 22:
    i = "nd"

if int(x.strftime("%d")) == 3 or int(x.strftime("%d")) == 23:
    i = "rd"


print(x.strftime("%A,"), x.strftime("%B"), x.strftime("%d")+i, x.strftime("%Y"),"at", x.strftime("%I:%M"), x.strftime("%p"))

quit()
