
#from datatime import date
class Student :
    no_of_students = 0
    def __init__(self,name , age ,courses):
        self.__name = name #private variable
        self.__age = age
        self.__courses  = courses
        Student.no_of_students += 1


    def get_name(self):
            return self.__name

    def set_name(self,new_name):
            self.__name = new_name

student_1 = Student("islam",40,['science'])
student_1.name = "mohammed"
print(student_1.get_name())

student_1.set_name("ahmed")
print(student_1.get_name())

#classmethod
'''
     @classmethod
     def initFromBirthYear(cls,name,birthYear):
         return cls (name,date.today().year - birthYear)
'''

class Pizza:
         def __init__(self,ingredients):
             self.ingredients = ingredients

         @classmethod
         def veg (cls):
             return cls (['mushrooms','olices','onions'])

         @classmethod
         def margherita(cls):
             return cls (['mozarella','saude'])

         def __str__(self):
             return f"pizza ingredients are {self.ingredients}"

pizza1 = Pizza(['tomatoes', "olices"])
pizza2 = Pizza.veg()
pizza3 = Pizza.margherita()

print(pizza3,pizza2,pizza1)
