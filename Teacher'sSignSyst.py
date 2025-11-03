import csv
from datetime import datetime
import os

# --- Configuration ---
LOG_FILE = "teacher_log.csv"
# The columns for our CSV file
CSV_FIELDS = ["TeacherID", "Date", "Time", "Action"]

def get_last_action(teacher_id):
    """
    Checks the log file for the last action (SIGN_IN or SIGN_OUT)
    by a specific teacher on the current day.
    """
    try:
        with open(LOG_FILE, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            today_str = datetime.now().strftime("%Y-%m-%d")
            last_action = None
            
            # This is not super-efficient for large files, but
            # it is the simplest to read all actions for the teacher today.
            for row in reader:
                if row["TeacherID"] == teacher_id and row["Date"] == today_str:
                    last_action = row["Action"]
            return last_action
            
    except FileNotFoundError:
        # The log file doesn't exist yet
        return None

def log_action(teacher_id, action):
    """
    Appends a new action (SIGN_IN or SIGN_OUT) to the CSV log file.
    """
    # 1. Get current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    # 2. Check if the log file already exists
    file_exists = os.path.isfile(LOG_FILE)
    
    # 3. Open the file in 'append' mode
    with open(LOG_FILE, 'a', newline='') as csvfile:
        # Use DictWriter to write rows as dictionaries
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDS)
        
        # 4. Write the header row if the file is new
        if not file_exists:
            writer.writeheader()
            
        # 5. Write the new action record
        writer.writerow({
            "TeacherID": teacher_id,
            "Date": date_str,
            "Time": time_str,
            "Action": action
        })

def sign_in():
    """Handles the Teacher Sign-In logic."""
    teacher_id = input("Enter your Teacher ID to SIGN IN: ").strip().upper()
    if not teacher_id:
        print("Invalid ID. Returning to menu.")
        return

    last_action = get_last_action(teacher_id)
    
    if last_action == "SIGN_IN":
        print(f"Error: Teacher {teacher_id} is already signed in today.")
    else:
        log_action(teacher_id, "SIGN_IN")
        print(f"Welcome, {teacher_id}. You are now SIGNED IN.")
        print(f"Time: {datetime.now().strftime('%H:%M:%S')}")

def sign_out():
    """Handles the Teacher Sign-Out logic."""
    teacher_id = input("Enter your Teacher ID to SIGN OUT: ").strip().upper()
    if not teacher_id:
        print("Invalid ID. Returning to menu.")
        return

    last_action = get_last_action(teacher_id)
    
    if last_action == "SIGN_OUT":
        print(f"Error: Teacher {teacher_id} is already signed out.")
    elif last_action is None:
        print(f"Error: Teacher {teacher_id} was never signed in today.")
    else:
        # This means their last action was "SIGN_IN", so they can sign out.
        log_action(teacher_id, "SIGN_OUT")
        print(f"Goodbye, {teacher_id}. You are now SIGNED OUT.")
        print(f"Time: {datetime.now().strftime('%H:%M:%S')}")

def main_menu():
    """
    Displays the main menu and handles user input.
    """
    while True:
        print("\n--- Teacher Attendance System ---")
        print("1. Sign In")
        print("2. Sign Out")
        print("3. Exit")
        choice = input("Please choose an option (1-3): ").strip()
        
        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_out()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# --- This is where the program starts ---
if __name__ == "__main__":
    main_menu()
