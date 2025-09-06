# Ask user for personal information
name = input("Enter your name: ")
age = input("Enter your age: ")
education = input("Enter your education level: ")
occupation = input("Enter your occupation: ")
gender = input("Enter your gender: ")
marital_status = input("Enter your marital status: ")


# Initial Amount of cents/Ask user how many cents they have
cents = int(input("How many cents do you have? "))

# Number of quarters and remaining cents
quarters = cents // 25
cents = cents % 25

# Number of dimes and remaining cents
dimes = cents // 10
cents = cents % 10

# Number of nickels and remaining cents
nickels = cents // 5
cents = cents % 5

# Number of pennies
pennies = cents

# Print out personal information
print("Collected Information:")
print("Name:", name)
print("Age:", age)
print("Education Level:", education)
print("Occupation:", occupation)
print("Gender:", gender)
print("Marital Status:", marital_status)

# Print out the results
print("Quarters=", quarters)
print("Dimes=", dimes)
print("Nickels=", nickels)
print("Pennies=", pennies)