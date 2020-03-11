from tkinter import *

#This is is window function on Python 
window = Tk()

#This is testing the program output. Very necessary.
def kmToMiles():
    #This command is injected into main function
    print(e1.value.get())
    t1.insert(END, e1_value.get())

b1 = Button(window, text = "Execute", command=kmToMiles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row=0, column=2)

#This is the main function that keep it looping. Allocates resources.
window.mainloop()