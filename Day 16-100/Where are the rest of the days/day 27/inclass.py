# from tkinter import *
#
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)
#
# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)
#
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)
#
# window.mainloop()

# import tkinter as tk
#
# # Create the main window
# root = tk.Tk()
# root.title("Hello, World!")
#
# # Create a label widget
# label = tk.Label(root, text="Hello, World!")
# label.pack()
#
# # Start the Tkinter event loop
# root.mainloop()

import tkinter as tk

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    print(f"Name: {name}, Email: {email}")

root = tk.Tk()
root.title("Simple Form")
window = tk.Frame(root)
window.config(padx=100, pady=100)

tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
