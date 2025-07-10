from tkinter import *

def convert():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 2)
        kilometer_result_label.config(text=f"{km}")
    except ValueError:
        kilometer_result_label.config(text="0")

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=100, pady=100)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
