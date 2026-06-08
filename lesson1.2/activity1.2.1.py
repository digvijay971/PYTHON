from tkinter import *
root = Tk()
root.title('number pad')
root.geometry('250x300')
nums = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['*', '0', '#']]
for i in range(4):
    root.columnconfigure(i, weight=1, minsize=50)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = Frame(master=root, relief=RAISED, borderwidth=1)
        frame.grid(row=i, column=j)
        Labe = Label(master=frame, text=nums[i][j], bg='white', fg='black')
        Labe.pack(padx=3, pady=3)
root.mainloop()