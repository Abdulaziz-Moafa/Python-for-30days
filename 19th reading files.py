workers_File = open("wokers.txt","r")# r+ read and write
print(workers_File.read())
workers_File.close()




## writing files

#w write with truncate mood > delete all data and rewrite
#a complete writing

workers_File = open("workers.txt","w")
workers_File.write("hunter x hunter is a sniper ")
workers_File.close()