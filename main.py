class StudentManagementSystem:
    def __init__(self):
        self.students = set()

    def add_student(self, student_id, name, year, division):
        student_info = (student_id, name, year, division)
        self.students.add(student_info)

    def remove_student(self, student_id):
        found_students = [student for student in self.students if student[0] == student_id]
        if found_students:
            self.students.difference_update(found_students)
            print(f"Student with ID {student_id} removed from the system.")
        else:
            print(f"Student with ID {student_id} not found in the system.")

    def display_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("All Students:")
            for student in self.students:
                print(f"ID: {student[0]}, Name: {student[1]}, Year: {student[2]}, Division: {student[3]}")

    def common_students(self, other_students):
        common_students = set()
        for student in other_students:
            if student in self.students:
                common_students.add(student)
        if common_students:
            print("Common Students:")
            for student in common_students:
                print(f"ID: {student[0]}, Name: {student[1]}, Year: {student[2]}, Division: {student[3]}")
        else:
            print("No common students found.")

    def unique_students(self, other_students):
        all_students = self.students.union(other_students)
        if all_students:
            print("All Students:")
            for student in all_students:
                print(f"ID: {student[0]}, Name: {student[1]}, Year: {student[2]}, Division: {student[3]}")
        else:
            print("No students found.")


def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display All Students")
        print("4. Find Common Students")
        print("5. Find Unique Students")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            student_info = input("Enter student details separated by spaces (ID Name Year Division): ").split()
            sms.add_student(*student_info)

        elif choice == '2':
            student_id = input("Enter the student's ID to remove: ")
            sms.remove_student(student_id)

        elif choice == '3':
            sms.display_all_students()

        elif choice == '4':
            num_students = int(input("Enter the number of students to compare: "))
            other_students = set()
            for _ in range(num_students):
                student_info = tuple(input("Enter student details separated by spaces (ID Name Year Division): ").split())
                other_students.add(student_info)
            sms.common_students(other_students)

        elif choice == '5':
            num_students = int(input("Enter the number of students to compare: "))
            other_students = set()
            for _ in range(num_students):
                student_info = tuple(input("Enter student details separated by spaces (ID Name Year Division): ").split())
                other_students.add(student_info)
            sms.unique_students(other_students)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()