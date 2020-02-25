email = ['me@outlook.com', 'you@gmail.com', 'we@gmail.com']
for item in email:
    if 'gmail' in item:
        print(item)

myList = [1, 2, 3, 4, 5]
for item in myList:
    if item >= 2:
        print(item)

names = ['cyrus', 'georgina', 'joy']
emailDomains = ['@gmail.com', '@outlook.com', '@hotmail.com']

for i,j in zip(names, emailDomains):
    print(i,j)
