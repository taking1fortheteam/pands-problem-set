# Aidan Conlon 30 March 2019
# Write a program that displays a plot of the functions x, x^2 and 2^x in the range [0, 4]

import matplotlib.pyplot as plt                             # Import plotting library                            
import numpy as np                                          # Import numpty library - computing scientifically
import pylab                                                # Import pylab - library similar to matlab 


x = np.arange(0.0, 4.0, 0.1)                                # set parameters for the graph -> start at 0, to 4 with steps of 0.1
y = (x*1)                                                   # set y equal to output of first function
x_to_power_of_2 = (x*x)                                     # set variable (x_to_power_of_2) equal to output of 2nd function (x*x)
two_to_power_of_x = (2**x)                                  # set variable (two_to_power_of_x) equal to output of 3rd function (2^x)

fig, plot = plt.subplots()                                  # the figure plot is set equal to the plotted subplots function

p1, = plt.plot(x , y, label ="y = x")                       # P1 - plot 1st function with label "y=x"
p2, = plt.plot(x , x_to_power_of_2, label ="y = x ^ 2")     # P2 - plot 2nd function with label "y=x^2"
p3, = plt.plot(x , two_to_power_of_x, label ="y = 2 ^ x")   # P3 - plot 3rd function with label "y=2^x"

plt.title('3 Plots - Problem 10')                           # Add Title of the Graph
plt.xlabel('Value of X')                                    # Add Title of X Axis
plt.ylabel('Value of Y')                                    # Add Title of Y Axis

plt.legend()                                                # Plot the legend for the graph
plt.grid()                                                  # Plot the grid for the graph
plt.show()                                                  # Show graphic

quit()                                                      # Quit
