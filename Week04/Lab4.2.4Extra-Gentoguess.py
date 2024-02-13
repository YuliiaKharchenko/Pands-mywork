# The program generates a random number between 0 and 100 to guess

import random
GenToGuess = random.randint(0,100)
print(GenToGuess)

numberToGuess = GenToGuess 
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
 if guess < numberToGuess:
   print("too low")
 else: # it cant be equal or too low, so it must be too high
   print("too high")
 guess = int(input("Please guess again:"))
print("Well done! Yes the number was ", numberToGuess)