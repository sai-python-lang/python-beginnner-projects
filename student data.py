class Student:
  # creating template for storing the details
  
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade
      # all the objects are stored 

    def display_details(self):
        print(f"Roll No: {self.roll_no} | Name: {self.name} | Age: {self.age} | Grade: {self.grade}")

class ManagementSystem:
    def __init__(self):
        self.students = []
      # it creates a empty list to add the details one by one 
  

    def add_student(self):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        
        new_student = Student(roll_no, name, age, grade)
        self.students.append(new_student)
        print("✅ Student added successfully!")

    def show_all_students(self):
        if not self.students:
            print("⚠️ No student records found.")
            return
        print("\n--- Student List ---")
        for s in self.students:
            s.display_details()

    def search_student(self):
        roll_no = input("Enter Roll Number to search: ")
        for s in self.students:
            if s.roll_no == roll_no:
                print("🔍 Student Found:")
                s.display_details()
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("Enter Roll Number to delete: ")
        for s in self.students:
            if s.roll_no == roll_no:
                self.students.remove(s)
                print("🗑️ Student record deleted.")
                return
        print("❌ Student not found.")

def main():
    system = ManagementSystem()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.show_all_students()
        elif choice == '3':
            system.search_student()
        elif choice == '4':
            system.delete_student()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
