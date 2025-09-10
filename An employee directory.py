#Applying all the foundational building blocks of programming inside this code.
#goal - Create a program that lets a user view a list of employees and add a new employee to the list.

employees = [
    {
        "name" : "Manasa",
        "position" : "HR Manager"
    },
    {
        "name" : "Manu",
        "position" : "Software Engineer"
    }
]

def view_employees():
    print("\n----CURRENTS EMPLOYEES----")
    for employee in employees:
        print(f"Name :{employee['name']}, Position: {employee['position']}")
    print("-------------------")

def add_employee():
    name = input("Enter new employee's name: ")
    position = input("Enter new employee's position: ")
    new_employee = { 
        "name" : name,
        "position" : position
    }
    employees.append(new_employee)
    print(f"\n{name} has been added.")

def main_menu():
    while True:
        print("\n--------EMPLOYEE DAIRY---------")
        print("\n 1. View All Employee")
        print("\n 2. Add New Employee")    
        print("\n 3. Exit")
        choice = int(input("Enter your choice here: "))

        if choice == 1:
            view_employees()
        elif choice == 2:
            add_employee()
        elif choice == 3:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()