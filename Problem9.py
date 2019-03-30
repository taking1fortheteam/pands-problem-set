# Aidan Conlon 29 March 2019
# Write a program that reads in a text file and outputs every second line. The program
# should take the filename from an argument on the command line.

import sys                                      # SYS module is required to be able to interpret files 

f = open(sys.argv[1],"r")                       # let f equal to the file that is contained within the command line after teh python file name about to be run

#count = len(open(sys.argv[1]).readlines(  ))   # get total number of lines in the file - this is not needed now
#print(count)                                   # for debugging it was good to set the fcount of the number of lines 

line_number = 0                                 # let the line number variable equal to 0

for line in f:                                  # For statement - basically work through the file "f" as long as there is a line within the file (before the end).
    line_number+=1                                  # increment the line number variable by 1
    if line_number %2 !=0:                          # if the line number has a carry - if divided by 2 then it is not an even number so therefore
        print(line,end = '')                             # print to screen contents of the specific line in the file "f" - but with no spacing between lines printed
f.close()                                       # close the file
quit()                                          # Quit the program

