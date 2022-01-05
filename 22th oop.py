class Student :
    no_of_students = 0
    def __init__(self,name , age ,courses):
        self.name = name
        self.age = age
        self.courses  = courses
        Student.no_of_students += 1


student_1 = Student("islam",30,['cs','math'])
student_2= Student("islam",30,['cs','math'])
print(id(student_2),id(student_1))

#- -------------------------------------

class Student :
    no_of_students = 0 #return the number of object -- line 31
    def __init__(self,name , age =0,courses=None):
        self.name = name
        self.age = age
        self.courses  = courses
        Student.no_of_students += 1

    def describe(self):
        print(f"my name is {self.name} and my age is {self.age} ")
        #or
        print("my name is {} and my age is {}".format(self.name , self.age))

    def is_old(self,num):
        if self.age <= num:
            print("student is not old")
        else:
            print("student is old")

student_1 = Student("islam",34)
student_2= Student("islam",30,['cs','math'])
print(student_2.age,student_1.age)#print student 1 with defult value
student_1.name = "abdulaziz" #change the value of the student 1
print(student_1.name)

print(Student.no_of_students)

student_1.describe()


student_1.is_old(30)






