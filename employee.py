class employee :
    def __init__(self,name , age , department , is_manager,rating,salary ):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
        self.rating = rating
        self.salary = salary
    def is_excellent(self):
        if self.rating >= 4 :
            return True
        else:
            return False


    def bonus (self):
        if self.is_manager == False:
            self.salary += 500
            print("your salary after bonus is : "+str(self.salary))
        else:
            print("no bonus " + str(self.salary))

class student :
    def __init__(self,name , age , gpa , major ):
        self.name=name
        self.age = age
        self.gpa = gpa
        self.major = major


