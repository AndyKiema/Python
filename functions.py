#Creating a function
def myfun():
  print('Hello')

myfun()

#Functions with parameters
def myfun2(name):
  print('My name is',name)

myfun2('Andrew')

#Multiple parameters
def cal(a,b):
  return(a+b)

sum=cal(2,10)
print(sum)

#None function
def fun():
  i=2

print(fun()) #None
#OR
def func():
  return

print(func()) #None

#Global and Local variables
#Global variables- variables created outside a function
#Local variables- variables created inside a function