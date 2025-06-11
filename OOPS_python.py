#classes are user defined blueprint or prototype
#under classes it will have methods, class variables, instance variables, constructor etc, object also
# Functions when defined under Classes are known as Methods, both are same.
#for calling a class we need to create objects which are outside the class

########IMP######
#self keyword is mandatory for calling variables names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object.


class Calculator:
    num = 100 #class variable, they are constant
#default constructor
    def __init__(self,a,b): #instance variable as the value is coming from outside of the class
        self.firstNumber=a
        self.secondNumber=b
        print("i am called automatically when the object is created")


    def getdata(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber+self.secondNumber + Calculator.num
        # or use self.num for class variables its optional
    #Self saves the obj inside it and through self only obj will be able to call the methods inside the class


obj = Calculator(2,3) #syntax to create objects in python and assigning a class
obj.getdata()
print(obj.Summation())

obj1 = Calculator(4,5) #instance variable values will change according to the requirement, but class variable values will be constant
obj1.getdata()
print(obj1.Summation())


