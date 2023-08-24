import os
import tkinter as tk
from tkinter import Toplevel, Text, Scrollbar
from calendar import calendar
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def text_to_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.setFont("Courier", 10)
    x = 100  # start x-position
    y = height - 100  # start y-position
    for line in text.split("\n"):
        c.drawString(x, y, line)
        y -= 14  # decrease y-position for next line, adjust for line spacing
    c.save()

def print_text(text):
    # Create a temporary PDF file
    temp_filename = "temp_calendar.pdf"
    text_to_pdf(text, temp_filename)
    
    # Open the PDF file in the default PDF viewer in print mode
    os.startfile(temp_filename)

def show_calendar():
    # Get the year from the Entry widget
    year_input = year_entry.get()

    # Validate input and fetch calendar
    try:
        year = int(year_input)
        cal_text = calendar(year, 2, 1, 8, 3)

        # Create the indented version for Preview
        indented_cal_text = "\n".join(["         " + line for line in cal_text.split("\n")])

        # Create a new window for Preview
        new_window = Toplevel(root)
        new_window.title(f"Calendar for {year}")

        # Set the dimensions of the output window
        new_window.geometry("800x600")  # Change this value to adjust the size

        # Add a Text widget and Scrollbar to display the indented calendar
        text_widget = Text(new_window, wrap=tk.NONE)
        scrollbar_x = Scrollbar(new_window, orient="horizontal", command=text_widget.xview)
        scrollbar_y = Scrollbar(new_window, orient="vertical", command=text_widget.yview)
        text_widget.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

        text_widget.insert(tk.END, indented_cal_text)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Add a Print button to the new window
        # Use the non-indented cal_text for generating the PDF
        print_button = tk.Button(new_window, text="Print", command=lambda: print_text(cal_text))
        print_button.pack(pady=10)

    except ValueError:
        print("Please enter a valid year.")


root = tk.Tk()
root.title("Enter Year")

# Set the dimensions of the main window
root.geometry("400x300")  # Change this value to adjust the size

# Label
tk.Label(root, text="Enter Year:").pack(pady=10)

# Entry widget with default value 2023
year_entry = tk.Entry(root, font=('Arial', 14))  # Increase font size
year_entry.pack(pady=10)
year_entry.insert(0, "2023")

# Preview button
tk.Button(root, text="Preview", command=show_calendar, font=('Arial', 14)).pack(pady=20)  # Increase font size

root.mainloop()