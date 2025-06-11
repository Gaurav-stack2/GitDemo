file = open('test1.txt')
#this method will help you read all the contents file
#print(file.read(6)) #we can give number till which we want to read

#dont use both read and readline
#print(file.readline())
#print(file.readline())


#file.close()

# Interview question - print line by line using readline method
#line = file.readline()
#while line !="":   # while loop
#    print(line)
 #   line = file.readline()


for line in file.readlines(): #all thing will print in as the list# print (line)
    print(line)


file.close()


