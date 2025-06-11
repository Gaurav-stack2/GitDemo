
#####methods to fail the test and validate the test case
ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart !=2:    #raise Exception ("Products cart count not matching")
    pass

assert(ItemsInCart ==0) # assertion will fail if the condition is not true and
                        #we should only mention true condition in assert


######methods to not fail the test and catch the execption or give customise errors
#try, catch(exception)
try:
    with open('test2.txt','r') as reader:
        reader.read()

except: #here we can give our own customize message rather than system error,like skipping the pop up
    print("somehow how i reached this block because there is failure in try block")


#this block will help running the code even it fails as the exception
#is handled

try:
    with open('test2.txt','r') as reader:
        reader.read()

except Exception as e: # in this it will capture the error what python throws but it wont intrupt the test execution
    print(e)


finally:
    print("cleaning up resources")

#use finally with try and except. it is use to execute the code of data that
# will be executed no matter what like cleaning up the junk or cookies of the test data

