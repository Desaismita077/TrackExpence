# TrackExpence (Python CLI Application)

A simple command-line based Expense Tracker built using Python.  
This project helps users record daily expenses, view expense history, and calculate total spending.

---

## Features

- Add new expenses with amount, category, and note
- View all saved expenses
- Calculate total expenses
- Stores data locally in a text file for persistence

---

## Technologies Used

- Python 3
- File Handling (Text File)

---

## Project Structure

expense-tracker/
├── expense_tracker.py
├── expenses.txt
└── README.md

---

## How It Works

- Each expense is stored as a single line in a text file.
- The format used is:
  amount,category,note
- The application reads and writes data using file handling in append mode.

---

## How to Run the Project

1. Make sure Python 3 is installed.
2. Clone this repository or download the files.
3. Open a terminal in the project directory.
4. Run the following command:

   python expense_tracker.py

---

## Sample Output

1. Add Expense  
2. View Expenses  
3. Total Expense  
4. Exit  

---

## What I Learned

- Writing clean and modular Python code using functions
- Using file handling to store and retrieve persistent data
- Handling user input and basic validation
- Structuring a small project for readability

---

## Future Improvements

- Add date support for expenses
- Add expense deletion or editing
- Store data using SQLite instead of text file
- Convert the project into a web application

---

## Author

Smita Desai
