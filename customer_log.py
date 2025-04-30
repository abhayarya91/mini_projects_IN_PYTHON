import tkinter as tk
from tkinter import messagebox, simpledialog

customers = {"Name": [], "c_id": [], "email": [], "sales": [], "logs": []}

def customer_add():
    name = entry_name.get()
    try:
        cid = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Customer ID must be an integer.")
        return
    email = entry_email.get()

    if cid in customers["c_id"]:
        messagebox.showwarning("Duplicate ID", "Customer ID already exists.")
        return

    customers["Name"].append(name)
    customers["c_id"].append(cid)
    customers["email"].append(email)
    customers["sales"].append(0)
    customers["logs"].append("")

    messagebox.showinfo("Success", "Customer added successfully.")
    entry_name.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def add_log():
    try:
        cid = int(simpledialog.askstring("Customer ID", "Enter Customer ID:"))
    except:
        return
    if cid in customers["c_id"]:
        log = simpledialog.askstring("Log Entry", "Enter log for customer:")
        index = customers["c_id"].index(cid)
        customers["logs"][index] = log
        messagebox.showinfo("Success", f"Log updated for {customers['Name'][index]}")
    else:
        messagebox.showerror("Not Found", "Customer ID not found.")

def update_sales():
    try:
        cid = int(simpledialog.askstring("Customer ID", "Enter Customer ID:"))
    except:
        return
    if cid in customers["c_id"]:
        try:
            sale = int(simpledialog.askstring("Sale Amount", "Enter sale amount:"))
        except:
            return
        index = customers["c_id"].index(cid)
        customers["sales"][index] += sale
        messagebox.showinfo("Success", f"Sales updated for {customers['Name'][index]}")
    else:
        messagebox.showerror("Not Found", "Customer ID not found.")

def print_customers():
    display.delete("1.0", tk.END)
    if not customers["Name"]:
        display.insert(tk.END, "No customer data available.\n")
    else:
        for i in range(len(customers["Name"])):
            display.insert(tk.END, f"\nCustomer {i+1}:\n")
            display.insert(tk.END, f"Name   : {customers['Name'][i]}\n")
            display.insert(tk.END, f"ID     : {customers['c_id'][i]}\n")
            display.insert(tk.END, f"Email  : {customers['email'][i]}\n")
            display.insert(tk.END, f"Sales  : {customers['sales'][i]}\n")
            display.insert(tk.END, f"Logs   : {customers['logs'][i]}\n")

# GUI setup
root = tk.Tk()
root.title("Customer Management System")
root.geometry("550x500")
root.config(bg="#f0f0f0")

# Labels and Entries
tk.Label(root, text="Customer Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Customer ID:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_id = tk.Entry(root)
entry_id.grid(row=1, column=1)

tk.Label(root, text="Customer Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Customer", bg="#4CAF50", fg="white", command=customer_add).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="Add Log by ID", bg="#2196F3", fg="white", command=add_log).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Update Sales by ID", bg="#FF9800", fg="white", command=update_sales).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(root, text="Show Customer Details", bg="#9C27B0", fg="white", command=print_customers).grid(row=6, column=0, columnspan=2, pady=5)

# Display area
display = tk.Text(root, height=15, width=60)
display.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
