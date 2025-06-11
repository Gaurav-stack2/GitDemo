str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1]) #a

print(str[0:5]) #substring in python

print(str+ str1) #concatenation

print(str3 in str) #substring check and it will return true or false

var = str.split("Academy") #splitting the string
print(var)
print(var[0])

str4 = "     great     " #trimming the white spaces on any side of the string
print(str4.strip())
print(str4.lstrip()) #left or beginning side trim
print(str4.rstrip()) #right or end side trim



