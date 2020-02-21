#Function Application
#age = input("Enter our age: \n")
#newAge = float(age) + 50
#print(newAge)

def ageNum(yrs):
    newAge = (yrs) + 50
    return newAge

age = float(input("Enter your current age: \n"))

if age < 150:
    print(ageNum(age))
else:
    print("Wacha kutubeba ufala bana..")