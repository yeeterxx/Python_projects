class Students:
    def __init__(self,name):
        self.name= name
        self.grades=[]

    def add_grade(self,grade):
        
        if isinstance(grade, list):
                self.grades.extend(grade)
        else:
                self.grades.append(grade)

    def calculate_average(self):
        if self.grades:
         return sum(self.grades)/len(self.grades)
        
    def get_letter_grade(self):
        avg= self.calculate_average()

        if avg>=90:
             return "A"
        elif avg>=81:
             return "B"
        elif avg>=71:
             return "C"
        elif avg>=61:
             return "D"
        else:
             return "NG"
        
students=[
     Students("max"),
     Students("lewis"),
     Students("carlos"),
     Students("charles"),
     Students("Daniel")

]


def view_all():
     for i,student in enumerate(students):
          print(f'{i}:{student.name}')

while True:
    print("\n*Menu*")
    print("1. Add new student")
    print("2. Add grade to student")
    print("3. View all students")
    print("4. View specific student's report")
    print("5. Quit")

    try:
         choice=int(input("enter the task you want to perform:"))
    except ValueError:
         print("invalid choice!! pick 1-5!")

    if choice==1:
         student_input=input("enter the name of new student:")
         new_std=Students(student_input)
         students.append(new_std)
         print(f"{student_input} sucessfully added!!")
         continue
    
    elif choice==2:
         view_all()
         try:
              chc=int(input("enter the student u want to add grade to: "))
              if 0< chc <= len(students):
                   student=students[chc]
                   grade_input= input(f"enter grade(s) for {student.name} ")
                   if ',' in grade_input:
                        grades= [int(g.strip()) for g in grade_input.split(',')]
                        student.add_grade(grades)
                        print(f"grades added sucessfully for {student.name}!")
                   else:
                        grade=int(input(f"enter grade of student {student.name}: "))
                        student.add_grade(grade)
                        print(f"grade added sucessfully for {student.name}")
         except:
              print("invalid choice!!")
              continue
         
    elif choice==3:
         view_all()
         continue

    elif choice==4:
         view_all()
         try:
              chc=int(input("Enter student you want to view grade of "))
              student=students[chc]

              print(f'report of student {student.name}:\n')
              print(f'grades of {student.name}:{student.grades}')
              print(f"average of this student is {student.calculate_average()}")
              print(f"letter grade of this student is {student.get_letter_grade()}")
         except:
              print("cannot get grade of this student!!")
              continue 

    elif choice==5:
         break
              

    

