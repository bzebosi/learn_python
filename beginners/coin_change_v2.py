""" Python Problem: coin_change.py
You have an amount of money in cents, for example 67 cents. 
Write a Python program that figures out how many quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢) make up that amount, 
using the fewest number of coins possible.

Your program should:

Start with a variable amount (in cents).

Use integer division (//) and modulo (%) to find out how many of each coin fits into the amount.

Print out the number of quarters, dimes, nickels, and pennies.


https://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html

chapter 1 and chapter 2
"""

# step 1: Enter the amount of cents you have:
amount = int(input("How much cents do you have : "))

# Step 2: "Integer division" (//) gives us how many times 25 fits into amount
quarter = amount // 25

# modulo (%) give us leftover after taking out quarters (update amount)
amount = amount % 25

# step 3: how many dimes go into the remaining amount i.e. 
# divide the remaining amount after removing quarters by 10
dimes = amount // 10

# modulo (%) give us leftover after taking out dimes (update amount)
amount = amount % 10

# step4 : how many nickels go into the remaining amount
# divide the remaining amount after removing quarters and dimes by 5
nickel = amount // 5

# modulo (%) give us leftover after taking out nickels (update amount)
amount = amount % 5 

# Step 5 : assign pennies to leftover cents
pennies = amount

# Step 6 : prints the results
print ("Quanters:", quarter)
print ("Dimes:", dimes)
print ("Nickel:", nickel)
print ("Pennies:", pennies)



