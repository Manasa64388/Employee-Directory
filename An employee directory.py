#Applying all the foundational building blocks of programming inside this code.
#goal - Create a program that lets a user view a list of employees and add a new employee to the list.

import json

# Define the file name for our data
FILE_NAME = "employees.json"

def load_employees():
    """Loads employee data from a JSON file."""
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list
        return []

def save_employees(employees_list):
    """Saves employee data to a JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(employees_list, file, indent=4)
        print(f"Employee data saved to {FILE_NAME}.")

def view_employees(employees_list):
    """Prints a list of all employees."""
    print("\n--- Current Employees ---")
    if not employees_list:
        print("No employees in the directory.")
    else:
        for employee in employees_list:
            print(f"Name: {employee['name']}, Position: {employee['position']}")
    print("-------------------------")

def add_employee(employees_list):
    """Prompts for new employee info and adds it to the list."""
    name = input("Enter new employee's name: ")
    position = input("Enter new employee's position: ")
    new_employee = {
        "name": name,
        "position": position
    }
    employees_list.append(new_employee)
    print(f"\n{name} has been added.")

def main_menu():
    """Displays the main menu and handles user choices."""
    employees = load_employees()  # Load data at the start

    while True:
        print("\n--- Employee Directory Menu ---")
        print("1. View all employees")
        print("2. Add a new employee")
        print("3. Exit")
        
        try:

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                view_employees(employees)
            elif choice == "2":
                add_employee(employees)
            elif choice == "3":
                save_employees(employees)  # Save data on exit
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1,2, or 3).")

# Run the program
main_menu()