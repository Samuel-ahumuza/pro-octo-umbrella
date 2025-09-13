def record_attendance(students, attendance_record):
    """Records attendance for a list of students."""
    print("\n--- Recording Attendance ---")
    for student in students:
        while True:
            response = input(f"Is {student} present? (y/n): ").lower()
            if response in ['y', 'n']:
                attendance_record[student] = 'Present' if response == 'y' else 'Absent'
                break
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
    print("Attendance recorded successfully!")

def view_attendance(attendance_record):
    """Displays the attendance record."""
    print("\n--- Attendance Record ---")
    if not attendance_record:
        print("No attendance has been recorded yet.")
        return

    for student, status in attendance_record.items():
        print(f"{student}: {status}")

def main():
    """Main function to run the attendance application."""
    students = ["Alice", "Bob", "Charlie", "Diana"]
    attendance_record = {}

    while True:
        print("\n--- Student Attendance System ---")
        print("1. Record Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            record_attendance(students, attendance_record)
        elif choice == '2':
            view_attendance(attendance_record)
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()