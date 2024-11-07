class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to store assignments and grades

    def add_assignment(self, assignment_name, grade):
        """Add a new assignment and its grade."""
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' with grade {grade} added to {self.name}.")

    def display_grades(self):
        """Display the student's assignments and grades."""
        if self.assignments:
            print(f"\n{self.name}'s Grades:")
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print(f"{self.name} has no assignments yet.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # List to store students enrolled in the course

    def add_student(self, student):
        """Add a student to the course."""
        self.students.append(student)
        print(f"Student {student.name} has been added to the course {self.course_name}.")

    def assign_grade(self, student, assignment_name, grade):
        """Assign a grade to a student's assignment."""
        if student in self.students:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student {student.name} is not enrolled in the course {self.course_name}.")

    def display_all_students(self):
        """Display all students and their grades."""
        print(f"\nStudents in {self.course_name}:")
        for student in self.students:
            student.display_grades()


# Interactive code for instructor to add students and assign grades
def main():
    # Create instructor
    instructor = Instructor("Dr. Smith", "Python Programming 101")

    while True:
        print("\nCourse Management Menu:")
        print("1. Add student")
        print("2. Assign grade to student")
        print("3. Display all students and their grades")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new student
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            # Assign grade to a student
            print("\nStudents enrolled in the course:")
            for i, student in enumerate(instructor.students, start=1):
                print(f"{i}. {student.name}")
            
            student_choice = int(input("Select a student by number: ")) - 1
            if 0 <= student_choice < len(instructor.students):
                student = instructor.students[student_choice]
                assignment_name = input("Enter the assignment name: ")
                grade = input("Enter the grade: ")
                try:
                    grade = float(grade)  # Convert grade to float
                    instructor.assign_grade(student, assignment_name, grade)
                except ValueError:
                    print("Invalid grade entered. Please enter a valid number.")
            else:
                print("Invalid student choice.")

        elif choice == "3":
            # Display all students and their grades
            instructor.display_all_students()

        elif choice == "4":
            print("Exiting the course management system.")
            break  # Exit the loop and terminate the program

        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
1
