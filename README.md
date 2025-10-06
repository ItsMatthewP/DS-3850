# Customer Data Entry & Viewer

A simple desktop application built with Python and Tkinter for entering and viewing customer information. Data is stored locally in an SQLite database.

---

## Description

This project consists of two main graphical interfaces:

1.  **Data Entry GUI (`fpFive.py`)**: A user-friendly form for inputting customer details, which are then saved directly into the database.
2.  **Data Viewer GUI (`readDatabase.py`)**: A clean, read-only table that displays all the customer records currently stored in the database.

This application is lightweight and runs entirely on your local machine without needing any external servers or complex setup.

---

## Features

* 📝 **Easy Data Entry**: A simple form to add new customer records.
* 💾 **Persistent Storage**: All data is saved in an `SQLite` database file (`customers.db`).
* 📊 **Clean Data Display**: View all records in a neat, scrollable table with alternating row colors for readability.
* 📦 **No External Dependencies**: Runs using Python's standard libraries.

---

## Repository Structure

.
├── customers.db
├── fpFive.py
└── readDatabase.py


* **`fpFive.py`**: The main application script that launches the GUI for customers to enter their data.
* **`readDatabase.py`**: A script that launches a separate GUI to read and display all entries from the database.
* **`customers.db`**: The SQLite database file that stores all the customer information.

---

## Getting Started

### Prerequisites

You need to have **Python 3** installed on your system. This project uses the built-in **Tkinter** library for the GUI, so no external packages need to be installed.

### How to Use

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd YOUR_REPOSITORY_NAME
    ```

3.  **To add a new customer:**
    Run the `fpFive.py` script from your terminal. The data entry form will appear.
    ```bash
    python fpFive.py
    ```

4.  **To view all customers:**
    Run the `readDatabase.py` script. A new window will open, displaying the table of all saved records.
    ```bash
    python readDatabase.py
    ```

---

## Screenshots

**COMING SOON