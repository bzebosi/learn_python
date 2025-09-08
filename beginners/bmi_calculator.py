""" problem BMI calculator
Write a program that asks the user for:
Weight in kilograms.
Height in meters.
Calculate their Body Mass Index (BMI): https://en.wikipedia.org/wiki/Body_mass_index
Prints the BMI value, rounded to 2 decimal places.
"""

# Ask the user for weight in kg
kgs = float(input("what is your weight in kgs: "))

# Ask the user for height in meters 
height = float(input("what is your height in meters: "))

# Step 2: Calculate BMI
bmi = kgs / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")


