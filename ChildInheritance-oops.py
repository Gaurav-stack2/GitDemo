

from OOPS_python import Calculator #syntax of inheritance the parent class into the child

class ChildImp(Calculator):  #calling the class name inside the child
    num2 = 200

    def __init__(self):  # we need to call the child constructor if parent has any not default constructor
        Calculator.__init__(self,8,7)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()



obj = ChildImp()
print(obj.getCompleteData())


