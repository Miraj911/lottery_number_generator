"""
ॐ नमः शिवाय
"""

import tkinter as tk
import random
from tkinter import messagebox

# Global variables to store the current batch and user preferences
current_entries = []
iterations_running = False  # Flag to track whether iterations are running

# Function to toggle full-screen mode
def toggle_fullscreen():
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
        root.resizable(True, True)  # Allow resizing
    else:
        root.attributes('-fullscreen', True)
        root.resizable(False, False)  # Prevent resizing in full-screen

# Function to generate entries based on selected options
def generate_entries():
    global current_entries
    entries_list.delete(0, tk.END)  # Clear the listbox
    current_entries = []

    try:
        num_numbers = int(num_numbers_entry.get())
        num_entries = int(num_entries_entry.get())
        include_powerball = include_powerball_var.get()
        number_range_start = int(num_range_start_entry.get())
        number_range_end = int(num_range_end_entry.get())
        powerball_range_start = int(powerball_range_start_entry.get())
        powerball_range_end = int(powerball_range_end_entry.get())

        if num_numbers < 1 or num_entries < 1:
            raise ValueError("Number of numbers and entries must be greater than 0.")
        if number_range_start >= number_range_end:
            raise ValueError("Invalid number range.")
        if include_powerball and powerball_range_start >= powerball_range_end:
            raise ValueError("Invalid Powerball range.")

        for i in range(1, num_entries + 1):
            numbers = random.sample(range(number_range_start, number_range_end + 1), num_numbers)
            formatted_numbers = "   ".join(f"{num:02}" for num in sorted(numbers))
            if include_powerball:
                powerball = random.randint(powerball_range_start, powerball_range_end)
                entry = f"Entry {i:02}:   [ {formatted_numbers} ]     Powerball: {powerball:02}"
                current_entries.append((sorted(numbers), powerball))
            else:
                entry = f"Entry {i:02}:   [ {formatted_numbers} ]"
                current_entries.append((sorted(numbers), None))
            entries_list.insert(tk.END, entry)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")



# Function to quit the program properly
def quit_program():
    global iterations_running
    iterations_running = False  # Stop any ongoing iterations
    root.quit()  # Quit the Tkinter main loop

# Create the main window
root = tk.Tk()
root.title("Powerball and Lottery Generator ॐ नमः शिवाय")

# Header
label = tk.Label(root, text="🎉ॐ Lottery Number Generator ॐ🎉", font=("Arial", 16, "bold"), fg="purple")
label.pack(pady=10)

# Lottery Options
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

tk.Label(options_frame, text="Numbers per Entry:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
num_numbers_entry = tk.Entry(options_frame, font=("Arial", 12), width=5)
num_numbers_entry.grid(row=0, column=1, padx=5)
num_numbers_entry.insert(0, "7")  # Default to Powerball

tk.Label(options_frame, text="Number of Entries:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
num_entries_entry = tk.Entry(options_frame, font=("Arial", 12), width=5)
num_entries_entry.grid(row=0, column=3, padx=5)
num_entries_entry.insert(0, "50")  # Default batch size

include_powerball_var = tk.BooleanVar(value=True)
tk.Checkbutton(options_frame, text="Include Powerball", variable=include_powerball_var, font=("Arial", 12)).grid(row=0, column=4, padx=5)

# Range Inputs
range_frame = tk.Frame(root)
range_frame.pack(pady=10)

tk.Label(range_frame, text="Number Range (Start - End):", font=("Arial", 12)).grid(row=0, column=0, padx=5)
num_range_start_entry = tk.Entry(range_frame, font=("Arial", 12), width=5)
num_range_start_entry.grid(row=0, column=1, padx=5)
num_range_start_entry.insert(0, "1")
num_range_end_entry = tk.Entry(range_frame, font=("Arial", 12), width=5)
num_range_end_entry.grid(row=0, column=2, padx=5)
num_range_end_entry.insert(0, "35")

tk.Label(range_frame, text="Powerball Range (Start - End):", font=("Arial", 12)).grid(row=1, column=0, padx=5)
powerball_range_start_entry = tk.Entry(range_frame, font=("Arial", 12), width=5)
powerball_range_start_entry.grid(row=1, column=1, padx=5)
powerball_range_start_entry.insert(0, "1")
powerball_range_end_entry = tk.Entry(range_frame, font=("Arial", 12), width=5)
powerball_range_end_entry.grid(row=1, column=2, padx=5)
powerball_range_end_entry.insert(0, "20")

# Generate Numbers Button
generate_button = tk.Button(root, text="Generate Numbers", command=generate_entries, font=("Arial", 14), bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

# Listbox to display entries with a scrollbar
entries_frame = tk.Frame(root)
entries_frame.pack(pady=10)

scrollbar = tk.Scrollbar(entries_frame, orient="vertical")
entries_list = tk.Listbox(entries_frame, width=80, height=20, font=("Courier", 12), bg="#f0f0f0", fg="black", yscrollcommand=scrollbar.set)
scrollbar.config(command=entries_list.yview)
entries_list.pack(side="left")
scrollbar.pack(side="right", fill="y")




# Full-Screen Toggle Button
fullscreen_button = tk.Button(root, text="Toggle Full Screen", command=toggle_fullscreen, font=("Arial", 12), bg="orange", fg="black")
fullscreen_button.pack(pady=5)

# Quit Button
quit_button = tk.Button(root, text="Quit", command=quit_program, font=("Arial", 12), bg="red", fg="white")
quit_button.pack(pady=5)

# Run the GUI loop
root.mainloop()
