# Project: Collection Manipulator
# Program: Student Data 

students_list = []

students_dict = {}

all_subjects_set = set()


def welcome_message():

    print("=" * 50)
    print(" Welcome to the Student Data Organizer ")
    print("=" * 50)
    print("This program allows you to store, view, update,")
    print("and delete student records using Python collections.\n")


def add_student():
    print("\n--- Add New Student ---")
    
    student_id = input("Enter Student ID: ").strip()
    
    for s in students_list:
        if s["id_dob"][0] == student_id:
            print("Error: Student ID already exists!")
            return

    name = input("Enter Name: ").strip()
    age = int(input("Enter Age: "))  # Type casting to int
    grade = input("Enter Grade (e.g., A, B, C): ").strip()
    dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
    
    subjects_input = input("Enter Subjects (comma-separated): ")
    
    subjects_list = [s.strip() for s in subjects_input.split(",") if s.strip()]
    
    all_subjects_set.update(subjects_list)

    id_dob_tuple = (student_id, dob)

    student_record = {
        "id_dob": id_dob_tuple,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": set(subjects_list)
    }

    students_list.append(student_record)
    students_dict[student_id] = student_record
    print(f"\n[f-string Success]: Student {name} added successfully!")
    print("Format method info: ID: {}, DOB: {}".format(id_dob_tuple[0], id_dob_tuple[1]))
    print("Old-style %% formatting info: Age: %d, Grade: %s" % (age, grade))


def display_all_students():
    print("\n--- All Student Records ---")
    if not students_list:
        print("No student records found.")
        return

    for idx, student in enumerate(students_list, 1):
        s_id, dob = student["id_dob"]
        subjects_str = ", ".join(student["subjects"])
        
        # student details
        print(f"\nRecord #{idx}:")
        print(f"  ID         : {s_id}")
        print("  DOB        : {}".format(dob))
        print("  Name       : %s" % student["name"])
        print(f"  Age        : {student['age']}")
        print(f"  Grade      : {student['grade']}")
        print(f"  Subjects   : {subjects_str}")


def update_student():
    print("\n--- Update Student Information ---")
    s_id = input("Enter Student ID to update: ").strip()

    student_to_update = None
    for student in students_list:
        if student["id_dob"][0] == s_id:
            student_to_update = student
            break

    if not student_to_update:
        print("Student ID not found.")
        return

    print("What would you like to update?")
    print("1. Age")
    print("2. Subjects")
    choice = input("Enter choice (1-2): ").strip()

    if choice == '1':
        new_age = int(input("Enter new age: "))
        student_to_update["age"] = new_age  # Modifying list item (Mutability)
        print(f"Updated age to {new_age} successfully.")
    elif choice == '2':
        new_sub = input("Enter new subjects (comma-separated): ")
        new_sub_list = [s.strip() for s in new_sub.split(",") if s.strip()]
        
        student_to_update["subjects"] = set(new_sub_list)
        all_subjects_set.update(new_sub_list)
        print("Updated subjects successfully.")
    else:
        print("Invalid choice.")


def delete_student():
    print("\n--- Delete Student Record ---")
    s_id = input("Enter Student ID to delete: ").strip()

    target_index = None
    for idx, student in enumerate(students_list):
        if student["id_dob"][0] == s_id:
            target_index = idx
            break

    if target_index is not None:
        # Using the del keyword to delete record from List
        del students_list[target_index]
        
        if s_id in students_dict:
            del students_dict[s_id]
            
        print(f"Student ID {s_id} has been deleted successfully.")
    else:
        print("Student ID not found.")


def display_unique_subjects():
    print("\n--- All Unique Subjects Offered ---")
    if not all_subjects_set:
        print("No subjects recorded yet.")
    else:
        print("Unique Subjects List:")
        for sub in sorted(all_subjects_set):
            print(f"- {sub}")


def main():
    welcome_message()
    
    while True:
        print("\n" + "="*30)
        print("         MENU OPTIONS")
        print("="*30)
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Unique Subjects Offered")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_unique_subjects()
        elif choice == '6':
            print("\nThank you for using the Student Data Organizer! Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()