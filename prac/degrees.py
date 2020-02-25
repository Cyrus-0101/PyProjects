# Converting degrees Fahrenheit to Celsius

def fahrTemp(deg):
    newTemp = ((deg) - 32) * (5/9) 
    return newTemp

temp = float(input("Enter the current temperature feels in Fahrenheit: \n"))

if temp < 150:
    print("\nThe current temperature in Celsius is: ", fahrTemp(temp))
    print("Thanks for using 0101 Solutions. \n")
elif temp > -273 or temp > 150:
    print("Wacha kutubeba ufala bana..\n")
else:
    print("\nWacha kutubeba ufala bana..\n")

# Converting degrees Celsius to Fahrenheit

def celTemp(deg):
    newTemp = ((deg) + 32) * (9/5) 
    return newTemp

temp = float(input("Enter the current temperature feels in Celsius: \n"))

if temp < -273 or temp < 150:
    print("\nThe current temperature in Fahrenheit is: ", celTemp(temp))
    print("Thanks for using 0101 Solutions")
elif temp > -273 or temp > 150:
    print("Wacha kutubeba ufala bana..")
else:
    print("Wacha kutubeba ufala bana..")