
values = [1,2,3.5,"test"]
#List is data type that allows multiple values and can be different data types
print("helo",values)
print(values[3][1])#e of test
print("hello",values[-1])#last value
print(values[1:4])#it starts from 1 but ends at 3

values.insert(3,"testing done")#inserting new values
print(values)

values.append("END")#it adds the value at the end
print(values)

values[2] = "Replacing the value" #updating

del values[0] #deleting the value
print(values)


####Tuples##immutable
val = (1,2,3.5,"test tuple")
print(val)

print(val[1])

###Dictionary - whenever we have strings either key or value, put it in double quotes
dic = {1:"first name",2:334,"abcd":5.678,4:"hello world"}

print(dic[4])#key value 4
print(dic["abcd"])#key value 3

##dynamic dictionaries- we assign the values while programming

dict = {   }

dict["firstname"] = "Testing" #here we are assigning the values to the key rather than giving it intially
dict["lastname"] = "Python"
dict[3]  = 4.5


print(dict)
print(dict[3])
