import numpy as np
import matplotlib.pyplot as plt

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10


salaries = np.random.normal(maxSalary,size = numberOfEntries)
print(salaries)

plt.plot(salaries)
# plt.show()

plt.savefig('plot.png')