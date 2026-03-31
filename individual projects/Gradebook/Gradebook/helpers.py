
#student Class with (student ID, Name, List of grades, Grade level)
class Student:
    def __init__(self, id, name, grades, level):
        self.id=id
        self.name=name
        self.grades=grades
        self.level=level
    #Print student Grade Level|ID|Name|Grades
    def __str__(self):
        if self.grades>=90:
            return f'{self.level}|{self.id}|{self.name}|{self.grades}%(A)|Honor Roll'
        elif self.grades>=80:
            return f'{self.level}|{self.id}|{self.name}|{self.grades}%(B)|Good Standing'
        elif self.grades>=70:
            return f'{self.level}|{self.id}|{self.name}|{self.grades}%(C)|Could Use Improvement'
        elif self.grades>=60:
            return f'{self.level}|{self.id}|{self.name}|{self.grades}%(D)|Could Use Improvement'
        else:
            return f'{self.level}|{self.id}|{self.name}|{self.grades}%(F)|Could Use Improvement'
    #add Grade
    def cgrade(self):
        while True:
            sgrades=int(input("What is the new grade you would like to give the student?"))
            if f"{sgrades}".isnumeric() and sgrades<=120 and sgrades>=0:
                break
            elif f"{sgrades}".isnumeric():
                print("Please enter a valid grade")
            else:
                print("Please enter Grade level as a number")
        self.grades=sgrades


#Gradebook class with (list of students)
class Gradebook:
    def __init__(self):
        self.students=[]
    #Search by Name 
    def name_search(self):
        sname=input("What is the name of the student you want to search?").capitalize()
        print(f'Grade level|ID|Name|Grade|Standing')
        for student in self.students:
            if f"{student.name}"==sname:
                print(student)
                return student
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
        print(f'Grade level|ID|Name|Grade|Standing')
        for student in self.students:
            if f"{student.id}"==sid:
                print(student)
                return student
            else:
                print("Student not Found")
    #print all students
    def p_students(self):
        print(f'Grade level|ID|Name|Grade|Standing')
        for i in self.students:
            print(i)
    #print Highest Grade, Lowest grade and Average grade
    def grade_summary(self):
        grades=[]
        for i in self.students:
            grades.append(i.grades)
        grades.sort()
        student=len(grades)
        num=0
        print(grades)
        for i in grades:
            num+=int(i)
        avg=num/student
        print(f"Students:{student}\nHighest Grade:{grades[0]}\nLowest Grade:{grades[student-1]}\nClass Average:{avg}\n")
    #Search by Grade Level
    def grade_search(self):
        while True:
            sgrade=input("What grade level you want to search?")
            if f"{sgrade}".isnumeric():
                break
            else:
                print("Please enter Grade level as a number")
        print(f'Grade level|ID|Name|Grade|Standing')
        for student in self.students:
            if f"{student.level}"==sgrade:
                print(student)
            else:
                print("No students found in grade level")
    #add student
    def add_student(self):
        while True:
            sid=input("What ID number of the student")
            if f"{sid}".isnumeric():
                break
            else:
                print("Please enter ID as a number")
        while True:
            sgrade=input("What is the grade level of the student?")
            if f"{sgrade}".isnumeric():
                break
            else:
                print("Please enter Grade level as a number")
        sname=input("What is the name of the student you want to search?").capitalize()
        while True:
            sgrades=int(input("What is the grade of the student?"))
            if f"{sgrades}".isnumeric() and sgrades<=120 and sgrades>=0:
                break
            elif f"{sgrades}".isnumeric():
                print("Please enter a valid grade")
            else:
                print("Please enter Grade level as a number")
        nstudent=Student(sid,sname,sgrades,sgrade)
        self.students.append(nstudent)

#Menu function
def menu():
    gradebook=Gradebook()
    while True:
        inp=input("Add Student[1]\nGrade Search[2]\nGrade Summary[3]\nName Search[4]\nID Search[5]\nView Students[6]\nEnd Session[7]\n")
        #select from options
        match inp:
            #1 Add student
            case "1":
                gradebook.add_student()
            #2 Search by Grade
            case "2":
                gradebook.grade_search()
            #3 Print grades
            case "3":
                gradebook.grade_summary()
            #4 search by name
            case "4":
                stu=gradebook.name_search()
                inp=input("Change Grade [1]\nReturn[2]\n")
                match inp:
                    case "1":
                        stu.cgrade()
                    case _:
                        continue
            #5 search by id
            case "5":
                gradebook.id_search()
                inp=input("Change Grade [1]\nReturn[2]\n")
                match inp:
                    case "1":
                        stu.cgrade()
                    case _:
                        continue
            #6 view students
            case "6":
                gradebook.p_students()
            case "7":
                break
            case _:
                print("please enter a valid input")