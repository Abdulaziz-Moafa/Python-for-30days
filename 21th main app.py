from employee import employee  #first one for file and next one for the class
from employee import student


employee1 = employee("azoz", 49 , "loool",True,5,2000)
employee2 = employee ("ahemd ",39,"dif",False,3,700)
print(employee1.age)

print(employee1.is_excellent())
print(employee2.is_excellent())


print(employee1.salary)
employee1.bonus()
print(employee2.salary)
employee2.bonus()


student1 = student("azoz",35 ,4.5,"CS")
print(student1.name,student1.age,student1.major,)
