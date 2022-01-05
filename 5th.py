#Lists  / /

friends = [1 , "Azoz", True , False , [1 , "islam"]]

print(friends) #Display all the value of the list

print(friends[0]) #Display specefic value from the list

print(friends[1:3]) #print more than one value

friends[4] = "Azoz" #change the specefice value from the list
print(friends)
print(friends[4])


# Lists 2 //
c = ["azo" , "ahnn" , "loool" , "loool"]
b = ["ahmed " , "jasem"]

c.extend(b) #this function combine 2 lists
#or you can do like this
c += b
b += c
print(c)
print (b)

# add value to the list
c.append("yo azoz is alone ")
print(c)
c.insert(2,"abo azoz") #add the value in specific place of the list
print (c)
c.remove("abo azoz") #remove the value from the list
c.clear() #remove all the value of the list
b.pop() #remove the last value of the list
b.index("jasem") #if the value are exist in the list
b.count("jasem") #how many values in the list that have "ahmed" name you can use if you want to check the value is repeated or not
b.sort() #sorting the values of the list

a= b.copy()
print(a)