# Program to claculate the number of elements in a string
def strLen(myStr):
    if type(myStr) == int:
        return("Sorry, please insert a string to proceed with this function")
    elif type(myStr) == float:
        return("Sorry, please insert a string to proceed with this function")
    else:
        return len(myStr)

leng = 300.22
print(strLen(leng))