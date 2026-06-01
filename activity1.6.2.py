from tkinter import *
from datetime import date
root = Tk()
root.title("My second GUI Program")
root.geometry('400x300')
lbl = Label(root, text="Hello World!", font=("Arial Bold", 20))
name_lbl = Label(root, text="Enter your name:", bg="yellow", fg="red", font=("Arial Bold", 15))
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    greeting = "Hello " + name + "!"
    message = "happy birthday grandma!"
    text_box.insert(END, greeting)
    text_box.insert(END, "\n")
    text_box.insert(END, message)
    text_box.insert(END, "\n")
    text_box.insert(END, "Today's date is: " + str(date.today()))
text_box = Text(root, height=10, width=40)
btn = Button(root, text="Submit", command=display)
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()