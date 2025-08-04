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
class newClass:
  a,b=10,20 #a and b are class variables
  def find(self):
    print(self.a,self.b) #This is to access the class variables
nc=newClass()

nc.find() #10 20
