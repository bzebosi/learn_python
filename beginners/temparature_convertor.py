"""temparature convertor
Asks the user to enter a temperature in Celsius and Convert it to Fahrenheit
print both results with two decimal places.
"""

# Step 1 : Ask the user to enter a temp in celsius 
celsius = float(input("Enter the temperature in celsius (C): "))

# Step 2: Convert Celsius → Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Step 3: Print result rounded to 2 decimal places
print(f"{celsius:.2f} Celsius is equal {fahrenheit:.2f} Fahrenheit")
