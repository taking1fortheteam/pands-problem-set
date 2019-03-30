# Aidan Conlon 30 March 2019
# Write a program that displays a plot of the functions x, x^2 and 2^x in the range [0, 4]

import matplotlib.pyplot as plt

title: "Plots of x, x^2 and 2^x"
p1, = plt.plot([0, 1, 2, 3, 4], [0, 1, 2, 3, 4], label="x=x")
plt.plot([0, 1, 2, 3, 4], [1, 2, 4, 8, 16])
plt.plot([0, 1, 2, 3, 4], [0, 2, 4, 6, 8])

plt.ylabel('Values of Y')
plt.xlabel('Values of X')
plt.show()

quit()
