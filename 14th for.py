
for char in "godz": # the variable char print every letter  in godz in new line
    print(char)

buddies = ["azoz","grand","ahmed"]

for List_word in buddies:
    print (List_word)

for x in range(5):
    print(x)\

print("\n")

for v in range (5,9):
    print(v)
s = 0


print("\n")
print(len("abdulazi"))

for u in range(len(buddies)):
    print(u)

for t in range (len(buddies)):
    print(buddies[t]) ###understand this print the list


for index in range (10):
     if index % 2 == 0 :
          print (index,"is an even number ")
     else:
         print(index,"is an odd number ")
### the same program by while loop
print("\n")
m = 0
while m <= 10 :
    if m % 2 == 0 :
        print(m,"is an odd number ")
    else:
        print(m,"is an even number ")
    m += 1

####
for buddy in range (len(buddies)):
    if buddies[buddy] == "khaled":
        print(buddy,"is the winer")
    else:
        print(buddy,"is the loser")

for buddy in buddies :
    if buddy == "azozf":
        print(buddy,"is he your friend ")
        break
else:
    print("not found")