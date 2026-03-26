
#student Class with (student ID, Name, List of grades, Grade level)
    #Print student Grade Level|ID|Name|Grades
    #add Grade

#Gradebook class with (list of students)
class Gradebook:
    def __init__(self):
        self.students=[]
    #Search by Name 
    def name_search(self):
        sname=input("What is the name of the student you want to search?").capitalize()
        for student in self.students:
            if f"{student.name}"==sname:
                print(student)
            else:
                print("Student not Found")
    #search by ID
    def id_search(self):
        while True:
            sid=input("What is the ID of the student you want to search?")
            if f"{sid}".isnumeric():
                break
            else:
                print("Student IDs are only comprised of numbers")
        for student in self.students:
            if f"{student.id}"==sid:
                print(student)
            else:
                print("Student not Found")
    #print all students
    def __str__(self):
        string=""
        for i in self.students:
            string=f"{string}{i}\n"
        return string
    #print Highest Grade, Lowest grade and Average grade
    def grade_summary(self):
        grades=[]
        for i in self.students:
            grades.append({i.grade})
        grades.sort()
        student=len(grades)
        num=0
        for i in grades:
            num+=i
        avg=num/student
        print(f"Students:{student}\nHighest Grade:{grades[0]}\nLowest Grade:{grades[student-1]}\nClass Average:{avg}")
    #Search by Grade Level
    def grade_search(self):
        while True:
            sgrade=input("What grade level you want to search?")
            if f"{sgrade}".isnumeric():
                break
            else:
                print("Please enter Grade level as a number")
        for student in self.students:
            if f"{student.grade_level}"==sgrade:
                print(student)
            else:
                print("No students found in grade level")
    #add student
    #Print students Level|ID|Name|Average grade
    #add Grade(specify student)

#Menu function
    #select from options
        #1 Search by ID
        #2 Search by Name
        #3 Print all Students
        #4 Print grades
        #5 add student
        #6 add grade