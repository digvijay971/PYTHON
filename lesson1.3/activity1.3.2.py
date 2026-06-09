from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("curse spirit detector")
window.geometry("200x200")
def msg():
    messagebox.showinfo("warning","you have been detected by the spacial grade curse spirit call saturo gojo")
button = Button(window,text="detect",command=msg)
place = button.place(x=50,y=50)
window.mainloop()