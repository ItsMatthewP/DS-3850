import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- Database Functions ---

def setup_database():
    """
    Creates the database file and the 'customers' table if they don't already exist.
    This ensures the application is ready to store data upon first launch.
    """
    # Connect to (or create) a database file named 'customers.db'
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    
    # Execute SQL to create a table with the required fields
    # 'IF NOT EXISTS' prevents errors on subsequent runs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            contact_method TEXT
        )
    ''')
    
    # Save the changes and close the connection
    conn.commit()
    conn.close()

def add_customer_to_db(name, birthday, email, phone, address, contact_method):
    """
    Inserts a new customer record into the database using the provided details.
    """
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    
    # Use '?' as placeholders to prevent SQL injection vulnerabilities
    cursor.execute('''
        INSERT INTO customers (name, birthday, email, phone, address, contact_method)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, birthday, email, phone, address, contact_method))
    
    conn.commit()
    conn.close()

# --- GUI and Form Logic ---

def submit_form():
    """
    Handles the 'Submit' button click event. It gathers data from the form,
    validates it, saves it to the database, and then clears the form.
    """
    # Retrieve data from the GUI input fields
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    contact_method = contact_method_var.get()

    # Simple validation to ensure the name field is not empty
    if not name:
        messagebox.showerror("Input Error", "The 'Name' field is required.")
        return

    # Add the collected data to the database
    add_customer_to_db(name, birthday, email, phone, address, contact_method)

    # Clear the form for the next entry
    clear_form()

    # Show a success message to the user
    messagebox.showinfo("Success", "Customer information has been submitted successfully!")

def clear_form():
    """
    Clears all the input fields in the GUI, resetting the form for a new entry.
    """
    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_method_var.set(contact_options[0]) # Reset dropdown to the first option

# --- Main Application Setup ---

# 1. Initialize the database to ensure the table is ready
setup_database()

# 2. Create the main application window
root = tk.Tk()
root.title("Customer Information Management System")
root.geometry("450x300") # Set window size

# Create a frame to hold the form widgets for better organization
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(expand=True, fill="both")

# 3. Create GUI Labels and Input Fields
labels_text = [
    "Name:", "Birthday (YYYY-MM-DD):", "Email:", 
    "Phone:", "Address:", "Preferred Contact:"
]

# Create and place each label on the grid
for i, text in enumerate(labels_text):
    label = tk.Label(form_frame, text=text, anchor="w")
    label.grid(row=i, column=0, padx=5, pady=8, sticky="w")

# Create entry widgets
name_entry = tk.Entry(form_frame)
birthday_entry = tk.Entry(form_frame)
email_entry = tk.Entry(form_frame)
phone_entry = tk.Entry(form_frame)
address_entry = tk.Entry(form_frame)

# Place entry widgets on the grid
entries = [name_entry, birthday_entry, email_entry, phone_entry, address_entry]
for i, entry in enumerate(entries):
    entry.grid(row=i, column=1, padx=5, pady=8, sticky="ew")

# 4. Create the Dropdown Menu for Contact Method
contact_options = ["Email", "Phone", "Mail"]
contact_method_var = tk.StringVar(root)
contact_method_var.set(contact_options[0]) # Set the default value

contact_menu = tk.OptionMenu(form_frame, contact_method_var, *contact_options)
contact_menu.grid(row=5, column=1, padx=5, pady=8, sticky="ew")

# 5. Create and place the Submit Button
submit_button = tk.Button(form_frame, text="Submit", command=submit_form, font=('Helvetica', 10, 'bold'))
submit_button.grid(row=6, column=0, columnspan=2, pady=20)

# Configure the grid layout to expand with the window
form_frame.grid_columnconfigure(1, weight=1)

# 6. Start the GUI event loop
root.mainloop()