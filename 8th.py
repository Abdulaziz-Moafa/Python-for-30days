is_hungry = True
wants_to_eat = False

#and condition
if is_hungry and wants_to_eat == True:
    print("go eat")
else:
    print("keep it up ")
#### Or condition
if is_hungry or wants_to_eat == True:
    print("go eat")
else:
    print("keep it up ")
#and not condition
if is_hungry and not wants_to_eat :
        print("go eat")
else:
        print("keep it up ")


        ######### comparison

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num1
    else:
        return num3

print(max_num(2,4,6))

#this function alrady exixst in python //
print(max(3,4,4646,3434,545,224))

def str_cop(str1,str2):
    if str1 == str2:
        return "the strings do match"
    else:
        return "the string dont match"
print(str_cop("azozh","azoz"))

 



