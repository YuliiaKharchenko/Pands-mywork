# program that prints out a random number between 1 and 10


# import random
# number = random.randint(1,10)
# print("here is a random number {}".format(number))  # This method is an alias for randrange(start, stop+1).

import random
number = random.randrange(1,10,2)
print("here is a random number {}".format(number))   # random.randrange(start, stop, step)