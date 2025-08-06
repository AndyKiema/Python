"""class myClass:
  def myfun(self):
    pass
  def display(self,name):
    print('hello',name)"""

#Objects
#mc1=myClass()
#mc2=myClass()
#mc1.myfun()
#mc1.display('Andrew') #hello Andrew

#Instance methods can only be accessed through objects
#Static methods can be accessed through both the class and the objects

"""class myClass:
  def m1(self):
    print('This is an instance method')
  @staticmethod
  def m2(num):
    print(num)

myClass.m2(3) #3
#myClass.m1() #Error
mc2=myClass()
mc2.m1() #This is an instance method
mc2.m2(100) #100"""

#Class variables
"""class newClass:
  a,b=10,20 #a and b are class variables
  def find(self):
    print(self.a,b) #This is to access the class variables
nc=newClass()

nc.find() #10 20"""
"""x,y=10,20 #Global variable
class newClass:
  i,j=5,55 #Class variable
  def pr(self):
    p,q=6,7 #Local variable
    print(x,y) #10 20
    print(self.i,self.j) #5 55
    print(p,q) #6 7

nc=newClass()
nc.pr()"""

x,y=10,20 #Global variable
class newClass:
  x,y=5,55 #Class variable
  def pr(self):
    x,y=6,7 #Local variable
    print(x,y) #6 7 local variable
    print(self.x,self.y) #5 55 class variable
    print(globals()['x'],globals()['y']) #10 20 global variable

nc=newClass()
nc.pr()

class mySecond:
  def __init__(self):
    print("This is a constructor")
  def m3(self):
    print("Hello")

mySecond() #This is a constructor

class myClass:
  def __init__(self,name):
    self.name=name
    print('My name is',name)
myc=myClass('Jeff') #My name is Jeff
print(myc.name) #Jeff

class Employee:
  def __init__(self,name,salary,id):
    self.name=name
    self.salary=salary
    self.id=id
  def display(self):
    print(self.name,self.salary,self.id)

em1=Employee('Andrew','$10,000',3672)
em1.display() #Andrew $10,000 3672

#str constructor- ONLY ONE STRING CAN BE RETURNED
class Employee1:
  def __init__(self,name,salary,id):
    self.name=name
    self.salary=salary
    self.id=id
  def __str__(self):
    return(self.name)
    return(self.salary)
e2=Employee1('Andrew','$10,000',3672)
print(e2) #Andrew