#read the file and store all the lines in list
#reverse the file
#write all the list back to file


with open('test2.txt','r') as reader: #this line will open and close the file automatically
    content = reader.readlines() #it will be stored as list
    reversed(content)
    with open('test2.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)

