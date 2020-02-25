file = open("example.txt", 'r')

content = file.read()

print("This is the content:\n", content)

file.seek(0)

content = file.readlines()
print(content)

content = [i.rstrip("\n") for i in content]
print(content)
file.close()