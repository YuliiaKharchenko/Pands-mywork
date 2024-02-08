# takes in a float amount of dollars and returns an
# absolute amount in cent.

# Autor Yuliia Kharchenko 

amountdoll = float(input("Please enter an amount: "))
amountcent = int(amountdoll*100)
absolutamountcent=abs(amountcent)
print("That amount in cent is {} ".format(absolutamountcent))