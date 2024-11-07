class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Display the details of the employee."""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

    def update_salary(self, new_salary):
        """Update the employee's salary."""
        self.salary = new_salary
        print(f"{self.name}'s salary has been updated to ${self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store employees in the department

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)
        print(f"Employee {employee.name} has been added to the {self.department_name} department.")

    def calculate_total_salary(self):
        """Calculate and display the total salary expenditure for the department."""
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"\nTotal salary expenditure for the {self.department_name} department: ${total_salary}")

    def display_employees(self):
        """Display all employees in the department."""
        if self.employees:
            print(f"\nEmployees in the {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
                print("----------------------")
        else:
            print(f"There are no employees in the {self.department_name} department.")


# Interactive code to manage employees and departments
def main():
    # Create a department
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\nDepartment Management Menu:")
        print("1. Add employee to department")
        print("2. Update employee salary")
        print("3. Display all employees in department")
        print("4. Display total salary expenditure")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new employee
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee's ID: ")
            salary = float(input("Enter employee's salary: $"))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            # Update an employee's salary
            employee_id = input("Enter the employee's ID to update salary: ")
            employee_found = False
            for employee in department.employees:
                if employee.employee_id == employee_id:
                    new_salary = float(input("Enter the new salary: $"))
                    employee.update_salary(new_salary)
                    employee_found = True
                    break
            if not employee_found:
                print(f"Employee with ID {employee_id} not found in the department.")

        elif choice == "3":
            # Display all employees in the department
            department.display_employees()

        elif choice == "4":
            # Calculate and display total salary expenditure
            department.calculate_total_salary()

        elif choice == "5":
            print("Exiting the department management system.")
            break  # Exit the loop and terminate the program

        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
