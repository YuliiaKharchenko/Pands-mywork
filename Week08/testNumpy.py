import numpy as np
import matplotlib.pyplot as plt
# it is a good idea to have your absolute values set into variables at the
# beginning of your program

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # this is so that the "random" numbers are the same each time 
# to make it easier to debug.

salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
ages = np.random.randint(low=21, high = 65, size = numberOfEntries) # prefer having absolute values set at the top
plt.scatter(ages, salaries, label="salaries") # this will be random
# plt.show()

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself
plt.plot(xpoints, ypoints, color= 'r',label = "x squared")
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
# plt.show() # see how the axis have changed
plt.savefig('prettier-plot.png')
'''
print (salaries)

plt.hist(salaries)
plt.show()

salariesPlus = salaries + 5000 # this will add 5000 to each value
print(salariesPlus)

# you can also multiply
salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print(salariesMult)
# This is a float array, here I convert it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)
'''