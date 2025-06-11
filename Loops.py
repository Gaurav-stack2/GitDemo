greeting = "Good Morning"

if greeting == "Good Morning":
    print("Its a match")
    print("second line")
else:
    print("condition do not match")

print("if else condition is completed here")

a = 4
if a > 2:
    print("Its true")
    print("second line")
else:
    print("condition do not match")

print("if else condition is completed here")

#####   For Loop  ####

obj = [2,3,4,5,7,8,9]
for i in obj:
    print(i*2)

#sum of first natural numbers 1+2+3+4+5 = 15
summ = 0
for j in range(1,6): #for (i=0;i<5;i++)in java    #range(i,j)-> i to j-1
    summ = summ+j
    print(summ)#if written inside the for loop, it will display all the iterations.

print(summ) #if written here outside the for loop it will wait for loop to complete and show the final output which is 15

print("*******************************")
for k in range(1,10,2): #this is how we can pass the index like increment by 2 or more, by default it will be 1
    print(k)

print("************skipping first initial index")
for m in range(10):#default it will take as 0 the initial value
    print(m)





