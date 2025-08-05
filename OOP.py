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

class myClass:
  def m1(self):
    print('This is an instance method')
  @staticmethod
  def m2(num):
    print(num)

myClass.m2(3) #3
#myClass.m1() #Error
mc2=myClass()
mc2.m1() #This is an instance method
mc2.m2(100) #100

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
