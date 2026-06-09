from tkinter import *
window = Tk()
window.title("lol a simple button")
window.geometry("100x100")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>" , handle_keypress)
def handle_click():
    print("clicked")
button = Button(text="muahahaha")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()