# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
import pyperclip
import json

def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!!")
        return

    try:
        with open("data.json", "r") as file:
            # Load existing data
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    finally:
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for '{website}' exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

tk.Label(text="Website:").grid(row=1, column=0)
tk.Label(text="Email/Username:").grid(row=2, column=0)
tk.Label(text="Password:").grid(row=3, column=0)

website_entry = tk.Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tk.Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

email_entry = tk.Entry(width=40)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "bhavishyanarravula@gmail.com")

password_entry = tk.Entry(width=40)
password_entry.grid(row=3, column=1)

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=50, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

