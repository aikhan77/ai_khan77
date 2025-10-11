#Assignement 4,5,6,7

class student:
    count_student=0 #for Assignement number 5
    def __init__(self,name,gpa):
        self.name=name
        self.__gpa=gpa
        if type(self) is student: #for Assignement number 5
            student.count_student+=1 #for Assignement number 5

    def get_total_student(self):
            return student.count_student
    
    #for Assignement number 6
    @staticmethod #for Assignement number 6
    def valid_id(student_id):
        if student_id[0]=="S":
            print(f"{student_id} is a Valid ID")
        else:
            print(f"{student_id} is not a Valid ID")

    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(new_gpa):
        if 0.0<=new_gpa<=4.0:
            return new_gpa
        else:
            return "GPA must be between 0.0 and 4.0"

#for Assignment number 7   
class GraduateStudent(student):
    def __init__(self,name,gpa,thesis_title):
        super().__init__(name,gpa)
        self.thesis_title=thesis_title
        print(f"{name}'s GPA is {gpa} and his thesis title is {thesis_title} ")
        
student1=student("Amin",3.2)
print(f"Name: {student1.name} and GPA: {student1.get_gpa()}")
n_gpa=student.set_gpa(2.2)
print(f"Name: {student1.name} and New GPA: {n_gpa}")
student2=student("Momin",2.9)
student3=student("Shahin",3.9)

#for Assignement number 5
print(f"Number of object of Student is {student.count_student}")

#for Assignement number 6
student.valid_id("st1")

#for Assignment number 7
Grad_student1=GraduateStudent("Rafiq",3.22,"Origine of Economics")
print(Grad_student1)   
