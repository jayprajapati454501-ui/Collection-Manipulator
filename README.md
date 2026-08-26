# 📚 Collection Manipulator – Student Data Organizer

A simple **Python-based Student Data Organizer** that demonstrates how different Python collection types can be used to store and manipulate student information.

---

## 📌 Project Overview

The **Collection Manipulator – Student Data Organizer** is a menu-driven console application developed in Python.

The program allows users to:

* Add new student records
* Display all student records
* Update student information
* Delete student records
* Display unique subjects
* Exit the application

The project demonstrates practical usage of **List, Tuple, Set, and Dictionary** collections in Python.

---

## 🎯 Objectives

The main objectives of this project are:

* Understand Python collection data types.
* Store and organize student information.
* Demonstrate List manipulation.
* Demonstrate Tuple usage.
* Use Sets to maintain unique subjects.
* Use Dictionaries to organize student records.
* Demonstrate mutability and immutability.
* Practice type casting.
* Demonstrate different string formatting methods.
* Use the `del` keyword to remove records.

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Application Type:** Console-based application
* **Collections:** List, Tuple, Set, Dictionary
* **Concepts:** Functions, loops, conditional statements, type casting, string formatting

---

## 🗂️ Data Structures Used

### 1. List

The `students_list` stores all student records.

```python
students_list = []
```

Student records are added using `append()`.

```python
students_list.append(student_record)
```

## The List is mutable, allowing records to be added, modified, and deleted.

### 2. Tuple

Student ID and Date of Birth are stored together in a Tuple.

```python
id_dob_tuple = (student_id, dob)
```

The Tuple is used for information that is intended to remain fixed within the student record.

---

### 3. Set

Subjects are stored using a Set so duplicate subjects are removed.

```python
"subjects": set(subjects_list)
```

The program also maintains an `all_subjects_set` containing subjects collected from the records.

---

### 4. Dictionary

Each student is represented using a Dictionary containing:

* Student ID
* Date of Birth
* Name
* Age
* Grade
* Subjects

Example:

```python
student_record = {
    "id_dob": id_dob_tuple,
    "name": name,
    "age": age,
    "grade": grade,
    "subjects": set(subjects_list)
}
```

The program also uses `students_dict` to associate a Student ID with its record.

---

## ✨ Features

### ➕ Add Student

The user can enter:

* Student ID
* Name
* Age
* Grade
* Date of Birth
* Subjects

The program checks whether the Student ID already exists before creating a new record.

---

### 👀 Display All Students

The program displays every student record with:

* ID
* Date of Birth
* Name
* Age
* Grade
* Subjects

It uses `enumerate()` to number the records.

---

### ✏️ Update Student

The program allows the user to update:

1. Age
2. Subjects

The student is located using the Student ID.

---

### 🗑️ Delete Student

The user can delete a student by entering the Student ID.

The project demonstrates the `del` keyword:

```python
del students_list[target_index]
```

The corresponding Dictionary entry is also deleted.

---

### 📖 Display Unique Subjects

The program displays all subjects stored in `all_subjects_set`.

The subjects are sorted before being displayed.

---

## 📋 Menu Options

```text
==============================
         MENU OPTIONS
==============================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Unique Subjects Offered
6. Exit
```

These six options are implemented in the `main()` function.

---

## 🔄 Program Flow

```text
START
  ↓
Welcome Message
  ↓
Display Menu
  ↓
Enter Choice
  ↓
┌───────────────────────────────┐
│ 1. Add Student                │
│ 2. Display All Students       │
│ 3. Update Student             │
│ 4. Delete Student             │
│ 5. Display Unique Subjects    │
│ 6. Exit                       │
└───────────────────────────────┘
  ↓
Perform Selected Operation
  ↓
Return to Menu
  ↓
Exit
```

---

## 🧩 Functions

The project is divided into the following functions:

| Function                    | Purpose                       |
| --------------------------- | ----------------------------- |
| `welcome_message()`         | Displays the welcome message  |
| `add_student()`             | Adds a new student            |
| `display_all_students()`    | Displays student records      |
| `update_student()`          | Updates age or subjects       |
| `delete_student()`          | Deletes a student             |
| `display_unique_subjects()` | Displays unique subjects      |
| `main()`                    | Controls the application menu |

## The function definitions and their responsibilities are implemented throughout the uploaded program.

## 🧠 Python Concepts Demonstrated

### Type Casting

Age input is converted from a string to an integer:

```python
age = int(input("Enter Age: "))
```

### f-String

```python
print(f"\n[f-string Success]: Student {name} added successfully!")
```

### `.format()` Method

```python
print("Format method info: ID: {}, DOB: {}".format(
    id_dob_tuple[0], id_dob_tuple[1]
))
```

### `%` Formatting

```python
print("Old-style %% formatting info: Age: %d, Grade: %s" % (age, grade))
```

These three formatting approaches are explicitly demonstrated in the project.

---

## 🔐 Validation

The program checks whether a Student ID already exists.

If the ID is already present, the program displays:

```text
Error: Student ID already exists!
```

It also displays appropriate messages when a student cannot be found.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Save the Program

Save the Python file as:

```text
project_3.py
```

### Step 3: Open Terminal

Navigate to the folder containing the Python file.

### Step 4: Run the Program

```bash
python project_3.py
```

The program starts by calling `main()` when the file is executed directly.

---

## 💻 Example

```text
==================================================
 Welcome to the Student Data Organizer
==================================================
This program allows you to store, view, update,
and delete student records using Python collections.
```

Then the application displays the menu and waits for the user's choice.

---

## ✅ Advantages

* Easy-to-use menu-driven interface
* Demonstrates important Python collections
* Supports adding, updating, displaying, and deleting records
* Uses Sets for unique subjects
* Demonstrates different string formatting methods
* Uses separate functions for different operations
* Suitable for learning Python collection manipulation

---

## ⚠️ Limitations

* Student data is stored in memory while the program is running.
* Data is not permanently saved to a file or database.
* The application is command-line based.
* Input validation could be expanded.

---

## 🚀 Future Enhancements

Possible improvements include:

* Add CSV or JSON file storage.
* Add SQLite or MySQL database support.
* Add student search functionality.
* Add sorting and filtering.
* Add a graphical interface using Tkinter.
* Add stronger input validation.
* Generate student reports.
* Add login/authentication functionality.

---

## 📁 Project Structure

```text
Collection-Manipulator/
│
├── project_3.py
└── README.md
```

---

## 👨‍💻 Project Information

**Project:** Collection Manipulator
**Program:** Student Data Organizer
**Language:** Python
**Type:** Console Application
**Main Concepts:** List, Tuple, Set, Dictionary

