students = []
courses = []
marks = {}
def input_number_of_students():
    return int(input("Enter the number of students in the class: "))
def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    return {"id": student_id, "name": name, "dob": dob}
def input_number_of_courses():
    return int(input("Enter the number of courses: "))
def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}
def input_student_marks():
    print("\nSelect a student:")
    list_students()
    student_id = input("Enter student ID: ")
    print("\nSelect a course:")
    list_courses()
    course_id = input("Enter course ID: ")
    mark = float(input("Enter the mark for the student in this course: "))
    key = (student_id, course_id)
    marks[key] = mark
def list_courses():
    print("\nList of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")
def list_students():
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}")
def show_student_marks():
    print("\nSelect a student:")
    list_students()
    student_id = input("Enter student ID: ")
    print("\nSelect a course:")
    list_courses()
    course_id = input("Enter course ID: ")
    key = (student_id, course_id)
    if key in marks:
        print("Mark for Student ID {student_id} in Course ID {course_id}: {marks[key]}")
    else:
        print("Mark not available for the selected student and course.")
num_students = input_number_of_students()
for _ in range(num_students):
    students.append(input_student_info())
num_courses = input_number_of_courses()
for _ in range(num_courses):
    courses.append(input_course_info())
while True:
    print("\nOptions:")
    print("1. Input student marks")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given course")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        input_student_marks()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        list_students()
    elif choice == "4":
        show_student_marks()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
