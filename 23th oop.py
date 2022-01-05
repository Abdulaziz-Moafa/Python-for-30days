 ##@staticmethod

class Math:

     @staticmethod
     def add5(num):
         return num + 5

     @staticmethod
     def add10(num):
         return num + 10
y = Math.add5(5)
z = Math.add10(y)
print(y,z)