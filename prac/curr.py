def cureConv(rate, euros):
    dollars = euros * rate
    return dollars

r = float(input("Enter the rate: \n"))
e = float(input("Enter amount of euros: \n"))

print(cureConv(r, e))