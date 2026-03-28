import json
import os

FILE_NAME = "students.json"

# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student(data):
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    marks = input("Enter Marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    data.append(student)
    save_data(data)
    print("✅ Student added successfully!")

# View students
def view_students(data):
    if not data:
        print("No records found.")
        return

    for student in data:
        print(student)

# Search student
def search_student(data):
    roll = input("Enter Roll Number: ")
    for student in data:
        if student["roll"] == roll:
            print(student)
            return
    print("❌ Student not found.")

# Update student
def update_student(data):
    roll = input("Enter Roll Number to update: ")
    for student in data:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["marks"] = input("Enter new marks: ")
            save_data(data)
            print("✅ Updated successfully!")
            return
    print("❌ Student not found.")

# Delete student
def delete_student(data):
    roll = input("Enter Roll Number to delete: ")
    for student in data:
        if student["roll"] == roll:
            data.remove(student)
            save_data(data)
            print("✅ Deleted successfully!")
            return
    print("❌ Student not found.")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
