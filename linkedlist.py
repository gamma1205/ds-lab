class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # Add new student
    def add_student(self, roll, name, marks):
        new_node = Student(roll, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Student added successfully!")

    # Delete a student by roll
    def delete_student(self, roll):
        temp = self.head
        prev = None
        while temp:
            if temp.roll == roll:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Student with Roll {roll} deleted.")
                return
            prev = temp
            temp = temp.next
        print("Student not found.")

    # Display all students
    def display(self):
        if self.head is None:
            print("No students in the list.")
            return
        temp = self.head
        print("\nRoll\tName\tMarks")
        while temp:
            print(f"{temp.roll}\t{temp.name}\t{temp.marks}")
            temp = temp.next

    # Update student details
    def update_student(self, roll, new_name, new_marks):
        temp = self.head
        while temp:
            if temp.roll == roll:
                temp.name = new_name
                temp.marks = new_marks
                print(f"Student {roll} updated successfully.")
                return
            temp = temp.next
        print("Student not found.")

    # Search by roll number
    def search_by_roll(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"\nStudent found: Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
                return
            temp = temp.next
        print("Student not found.")

    # Sort students
    def sort_students(self, field, rev):
        students = []
        temp = self.head
        while temp:
            students.append({"roll": temp.roll, "name": temp.name, "marks": temp.marks})
            temp = temp.next

        students.sort(key=lambda x: x[field], reverse=rev)
        print(f"\nSorted by {field} ({'Descending' if rev else 'Ascending'})")
        print("Roll\tName\tMarks")
        for s in students:
            print(f"{s['roll']}\t{s['name']}\t{s['marks']}")


# --- MAIN PROGRAM ---
slist = StudentList()

while True:
    print("\n====== Student Record Management System ======")
    print("1. Add Student")
    print("2. Display All")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Sort Students")
    print("7. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        slist.add_student(roll, name, marks)

    elif ch == '2':
        slist.display()

    elif ch == '3':
        roll = int(input("Enter Roll No to Search: "))
        slist.search_by_roll(roll)

    elif ch == '4':
        roll = int(input("Enter Roll No to Delete: "))
        slist.delete_student(roll)

    elif ch == '5':
        roll = int(input("Enter Roll No to Update: "))
        name = input("Enter New Name: ")
        marks = float(input("Enter New Marks: "))
        slist.update_student(roll, name, marks)

    elif ch == '6':
        field = input("Sort by 'roll' or 'marks': ").lower()
        order = input("Sort in descending order? (y/n): ").lower()
        rev = True if order == 'y' else False
        slist.sort_students(field, rev)

    elif ch == '7':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
