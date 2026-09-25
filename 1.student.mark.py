students = [] #list of tuples, each student have id,name,dob
courses = [] #list of dictionaries, each course have course_id and course_name
marks = {} #dictionary of dictionaries with mark,course_id and mark of student
def input_number_of_std(): #create function number of student
    return int(input("Enter number of students: "))
    
def input_std(number): #func to enter std_id,std_name,dob
    print("\n---Student Info---")
    for _ in range(number):
        s_id = input("Student id: ") #type your student id    
        s_name = input("Student Name: ") #type your student name
        s_dob = input("Date of Birth: ") #type date of birth
        students.append((s_id,s_name,s_dob)) #add value 

def input_number_of_courses():  #function number of course
    return int(input("\nEnter number of courses: "))

def input_courses(num_courses):
    print("\n---Course Info---")
    for _ in range(num_courses):
        c_id = input("Course id: ") #type course id
        c_name = input("Course name: ") #type course name
        courses.append({'id': c_id, 'name': c_name}) #add value 

def input_marks():
    if not courses or not student:
       print("\nInput students and courses to go next ") 
       return

    list_courses()
    course_id = input("\nEnter course id to input mark: ")

    if not any(c['id'] == course_id for c in courses): #check course if it exists 
        print("No course available")
        return

    print(f"\n--- Input Marks for Course: {course_id} ---")
    if course_id not in marks:
        marks[course_id] = {}

    for student in students:
        s_id, s_name, _ = student  
        mark = float(input(f"Enter mark for {s_name} (ID: {s_id}): "))
        marks[course_id][s_id] = mark
def list_courses():
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s[0]} | Name: {s[1]} | DoB: {s[2]}")

def show_student_marks():
    list_courses()
    course_id = input("\nEnter the Course ID to view marks: ")
    
    if course_id not in marks:
        print("No marks have been entered for this course yet.")
        return
    course_name = next((c['name'] for c in courses if c['id'] == course_id), "Unknown")
    
    print(f"\n--- Marks for {course_name} (ID: {course_id}) ---")
    for student in students:
        s_id, s_name, _ = student 
        student_mark = marks[course_id].get(s_id, "N/A")
        print(f"Student: {s_name} (ID: {s_id}) -> Mark: {student_mark}")

def main():
    while True:
        print("\n===============================")
        print(" STUDENT MARK MANAGEMENT SYSTEM")
        print("===============================")
        print("1. Add Students")
        print("2. Add Courses")
        print("3. Input Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks")
        print("0. Exit")
        
        choice = input("\nSelect an option (0-6): ")
        
        if choice == '1':
            num = input_number_of_std()
            input_std(num)
        elif choice == '2':
            num = input_number_of_courses()
            input_courses(num)
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

      
   

