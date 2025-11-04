from fee_tracker import FeeTracker

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def student_menu(tracker):
    while True:
        print("\n--- Student Management ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            program = input("Enter Program: ")
            campus = input("Enter Campus: ")
            year = get_int_input("Enter Year of Study: ")
            tracker.add_student(student_id, name, program, campus, year)
        elif choice == '2':
            tracker.view_all_students()
        elif choice == '3':
            student_id = input("Enter Student ID to edit: ")
            if not tracker.get_student(student_id):
                print("Student not found.")
                continue
            name = input("Enter New Name: ")
            program = input("Enter New Program: ")
            campus = input("Enter New Campus: ")
            year = get_int_input("Enter New Year of Study: ")
            tracker.edit_student(student_id, name, program, campus, year)
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            tracker.delete_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def fee_menu(tracker):
    while True:
        print("\n--- Fee Structure Management ---")
        print("1. Add Fee Structure")
        print("2. View All Fee Structures")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            program = input("Enter Program: ")
            year = get_int_input("Enter Year: ")
            total_fee = get_int_input("Enter Total Fee: ")
            tracker.add_fee_structure(program, year, total_fee)
        elif choice == '2':
            tracker.view_fee_structures()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

def payment_menu(tracker):
    print("\n--- Record Payment ---")
    student_id = input("Enter Student ID: ")
    amount = get_int_input("Enter Amount Paid: ")
    tracker.record_payment(student_id, amount)

def report_menu(tracker):
    while True:
        print("\n--- Reports ---")
        print("1. Full Student Report")
        print("2. Per-Program Report")
        print("3. Overall Income Summary")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            tracker.generate_student_report()
        elif choice == '2':
            tracker.generate_program_report()
        elif choice == '3':
            tracker.generate_overall_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

def main_menu():
    tracker = FeeTracker()
    
    while True:
        print("\n====== Student Fee Management System ======")
        print("1. Student Management")
        print("2. Fee Structure Management")
        print("3. Record Payment")
        print("4. Generate Reports")
        print("5. Exit")
        
        main_choice = input("Enter choice: ")
        
        if main_choice == '1':
            student_menu(tracker)
        elif main_choice == '2':
            fee_menu(tracker)
        elif main_choice == '3':
            payment_menu(tracker)
        elif main_choice == '4':
            report_menu(tracker)
        elif main_choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main_menu()