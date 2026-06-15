import tkinter as tk
from tkinter import messagebox
def calculate_intrest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        intrest = (principal * rate * time) / 100
        total = principal + intrest
        result_label.config(text=f"Intrest: ${intrest:.2f}\nTotal Amount: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for principal, rate, and time.")
window = tk.Tk()
window.title("Simple Intrest Calculator")
window.geometry("300x200")
label_principal = tk.Label(window, text="simple intrest calculator")
label_principal.pack()
entry_principal = tk.Entry(window)
entry_principal.pack()
tk.Label(window, text="Rate of Intrest (%)").pack()
entry_rate = tk.Entry(window)
entry_rate.pack()
tk.Label(window, text="Time (years)").pack()
entry_time = tk.Entry(window)
entry_time.pack()
calculate_button = tk.Button(window, text="Calculate", command=calculate_intrest)
calculate_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()