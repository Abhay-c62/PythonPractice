class Student:
    def __init__(self, name, age, grade, course):
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Course: {self.course}")

file_name="students.txt"

def add_student(student):
    with open(file_name, "a") as file:
        file.write(f"{student.name},{student.age},{student.grade},{student.course}\n")

def view_students():
    try:
        with open(file_name, "r") as file:
            students = file.readlines()
            if not students:
                print("No students found.")
                return
            for student in students:
                name, age, grade, course = student.strip().split(",")
                print(f"Name: {name}, Age: {age}, Grade: {grade}, Course: {course}")
    except FileNotFoundError:
        print("No students found.")

def search_student(name):
    try:
        with open(file_name, "r") as file:
            students = file.readlines()
            for student in students:
                student_name, age, grade, course = student.strip().split(",")
                if student_name.lower() == name.lower():
                    print(f"Name: {student_name}, Age: {age}, Grade: {grade}, Course: {course}")
                    return
            print("Student not found.")
    except FileNotFoundError:
        print("No students found.")

def update_student(name, new_age=None, new_grade=None, new_course=None):
    try:
        with open(file_name, "r") as file:
            students = file.readlines()
        updated_students = []
        found = False
        for student in students:
            student_name, age, grade, course = student.strip().split(",")
            if student_name.lower() == name.lower():
                found = True
                age = new_age if new_age is not None else age
                grade = new_grade if new_grade is not None else grade
                course = new_course if new_course is not None else course
            updated_students.append(f"{student_name},{age},{grade},{course}\n")
        if found:
            with open(file_name, "w") as file:
                file.writelines(updated_students)
            print("Student information updated.")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("No students found.")

def delete_student(name):
    try:
        with open(file_name, "r") as file:
            students = file.readlines()
        updated_students = []
        found = False
        for student in students:
            student_name, age, grade, course = student.strip().split(",")
            if student_name.lower() == name.lower():
                found = True
                continue  # Skip adding this student to the updated list
            updated_students.append(f"{student_name},{age},{grade},{course}\n")
        if found:
            with open(file_name, "w") as file:
                file.writelines(updated_students)
            print("Student deleted.")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("No students found.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            course = input("Enter course: ")
            student = Student(name, age, grade, course)
            add_student(student)
            print("Student added successfully.")
        elif choice == "2":
            view_students()
        elif choice == "3":
            name = input("Enter name to search: ")
            search_student(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            new_age = input("Enter new age (leave blank to keep current): ")
            new_grade = input("Enter new grade (leave blank to keep current): ")
            new_course = input("Enter new course (leave blank to keep current): ")
            update_student(name, new_age if new_age else None, new_grade if new_grade else None, new_course if new_course else None)
        elif choice == "5":
            name = input("Enter name to delete: ")
            delete_student(name)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()