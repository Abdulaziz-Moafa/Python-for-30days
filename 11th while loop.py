i = 0

while i <= 100:
    print (i)
    i = i+5
    #or i += 5

print("the loop has ended")

# while True
# use ot when you wont infenet loop
n = 1
while n <= 10:
    n += 1
    if n == 5:
        continue #skip
    print(n)

z = 1
while z <= 10:
    z+=1
    if z == 6:
        break #end of while loop 
    print(z)
