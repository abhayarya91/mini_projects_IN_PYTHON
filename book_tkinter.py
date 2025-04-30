import tkinter as tk
from tkinter import ttk, messagebox

# Booking data
movies = {
    "Me Tera Hero": {"time": "08:00 AM to 11:30 AM", "price": 120},
    "Patna se Pakistan": {"time": "12:00 PM to 02:00 PM", "price": 150},
    "Dulhan Chahi Pakistani": {"time": "03:00 PM to 05:00 PM", "price": 180}
}

booked_users = []
seat_count = [100]  # Using list to make mutable in inner function

# GUI setup
root = tk.Tk()
root.title("🎬 Movie Ticket Booking System")
root.geometry("500x500")
root.configure(bg="#282C34")

# Heading
tk.Label(root, text="Movie Ticket Booking", font=("Arial", 18, "bold"), fg="white", bg="#282C34").pack(pady=10)

# Movie dropdown
tk.Label(root, text="Select Movie:", font=("Arial", 12), fg="white", bg="#282C34").pack()
movie_var = tk.StringVar()
movie_dropdown = ttk.Combobox(root, textvariable=movie_var, values=list(movies.keys()), state="readonly")
movie_dropdown.pack(pady=5)

# Name Entry
tk.Label(root, text="Enter your name:", font=("Arial", 12), fg="white", bg="#282C34").pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Age Entry
tk.Label(root, text="Enter your age:", font=("Arial", 12), fg="white", bg="#282C34").pack()
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

# ID Entry
tk.Label(root, text="Enter your ID Number:", font=("Arial", 12), fg="white", bg="#282C34").pack()
id_entry = tk.Entry(root)
id_entry.pack(pady=5)

# Seat Label
seat_label = tk.Label(root, text=f"Seats Available: {seat_count[0]}", font=("Arial", 12, "bold"), fg="yellow", bg="#282C34")
seat_label.pack(pady=10)

# Booking function
def book_ticket():
    movie = movie_var.get()
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    user_id = id_entry.get().strip()

    if not (movie and name and age.isdigit() and user_id):
        messagebox.showwarning("Input Error", "Please fill all fields correctly.")
        return

    user_entry = (name.lower(), user_id)

    if user_entry in booked_users:
        messagebox.showerror("Duplicate Booking", "You have already booked a ticket.")
        return

    if seat_count[0] <= 0:
        messagebox.showinfo("Full", "No seats available.")
        return

    # Add user and reduce seat
    booked_users.append(user_entry)
    seat_count[0] -= 1
    seat_label.config(text=f"Seats Available: {seat_count[0]}")

    movie_time = movies[movie]['time']
    price = movies[movie]['price']
    messagebox.showinfo("Booking Confirmed",
        f"Name: {name}\nAge: {age}\nMovie: {movie}\nTime: {movie_time}\nPrice: ₹{price}\nSeat No: {seat_count[0]+1}\nStatus: Confirmed"
    )

# Button
book_button = tk.Button(root, text="Book Ticket", command=book_ticket, font=("Arial", 12, "bold"),
                        bg="#4CAF50", fg="white", padx=10, pady=5)
book_button.pack(pady=20)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 10), bg="#f44336", fg="white")
exit_button.pack()

root.mainloop()
