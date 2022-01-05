no_list = [1,2,3,4] #general list

d_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]

]

print(d_list)
print(d_list[3])
print(d_list[2][2])

#this is 2 dimentional

for row in d_list:
    print(row)
    ###############
for d in d_list:
    for column in d:
        print(column)

