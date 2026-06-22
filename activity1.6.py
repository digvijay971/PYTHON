import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
class restaurantordermanagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order Management System")
        self.menu_item = {
            "fries": 2.50,
            "burger": 5.00,
            "pizza": 8.00,
            "soda": 1.50,
            "cheese burger": 6.00,
            "chicken nuggets": 4.00,
            "happy meal": 7.00
        }
        self.exchange_rate = 85
        frame = tk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame, text="Menu").grid(row=0, column=0, padx=10, pady=10)
        self.menu_labels = {}
        self.menu_quantity = {}
        for i, (item, price) in enumerate(self.menu_item.items()):
            ttk.Label(frame, text=f"{item} - ${price}").grid(row=i+1, column=0, padx=10, pady=5)
            quantity_entry = ttk.Entry(frame)
            quantity_entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.menu_labels[item] = ttk.Label(frame, text="0")
            self.menu_labels[item].grid(row=i+1, column=2, padx=10, pady=5)
            self.menu_quantity[item] = quantity_entry
        self.currency_var = tk.StringVar()
        self.currency_var.set("USD")
        ttk.Label(frame, text="Select Currency").grid(row=len(self.menu_item)+1, column=0, padx=10, pady=10)
        currency_combo = ttk.Combobox(frame, textvariable=self.currency_var)
        currency_combo['values'] = ("USD", "inr")
        currency_combo.grid(row=len(self.menu_item)+1, column=1, padx=10, pady=10)
        currency_combo.current(0)
        ttk.Button(frame, text="Calculate Total", command=self.calculate_total).grid(row=len(self.menu_item)+2, column=0, padx=10, pady=10)
    def update_menu_price(self,*args):
        currency = self.currency_var.get()
        if currency == "USD":
            for item, price in self.menu_item.items():
                self.menu_labels[item].config(text=f"${price}")
        elif currency == "inr":
            for item, price in self.menu_item.items():
                inr_price = price * self.exchange_rate
                self.menu_labels[item].config(text=f"₹{inr_price:.2f}")
    def calculate_total(self):
        total = 0
        for item, entry in self.menu_quantity.items():
            try:
                quantity = int(entry.get())
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative")
                total += self.menu_item[item] * quantity
            except ValueError:
                messagebox.showerror("Invalid Input", f"Please enter a valid quantity for {item}.")
                return
        currency = self.currency_var.get()
        if currency == "USD":
            messagebox.showinfo("Total Amount", f"Total Amount: ${total:.2f}")
        elif currency == "inr":
            total_inr = total * self.exchange_rate
            messagebox.showinfo("Total Amount", f"Total Amount: ₹{total_inr:.2f}")
if __name__ == "__main__":
    root = tk.Tk()
app = restaurantordermanagement(root)
app.currency_var.trace("w", app.update_menu_price)
root.mainloop()
