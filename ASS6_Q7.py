class Student:
    pass

class Marks:
    pass

# Create instances
student_instance = Student()
marks_instance = Marks()

# Check instance types
if isinstance(student_instance, Student):
    print("student_instance is an instance of the Student class.")
else:
    print("student_instance is not an instance of the Student class.")

if isinstance(marks_instance, Marks):
    print("marks_instance is an instance of the Marks class.")
else:
    print("marks_instance is not an instance of the Marks class.")

# Check class hierarchy
if issubclass(Student, object):
    print("Student is a subclass of the object class.")
else:
    print("Student is not a subclass of the object class.")

if issubclass(Marks, object):
    print("Marks is a subclass of the object class.")
else:
    print("Marks is not a subclass of the object class.")

