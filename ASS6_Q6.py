def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)
    if student_name:
        print("Student Name:", student_name)
    if student_class:
        print("Student Class:", student_class)

# Printing only the student ID
student_data(123456)

# Printing student ID, name, and class
student_data(123456, "John Doe", "Class A")

# Printing student ID and name (no class provided)
student_data(123456, "John Doe")
