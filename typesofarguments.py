#Positional arguments- arguments passed to a function in the correct positional order
def funct(i,j):
  print(i,j)

funct(1,2) #1 2

#Keyword arguments- arguments passed to a function by explicitly specifying the parameter name
funct(j=2,i=1) #1 2

def funk(i,j=10):
  print(i,j)
funk(100,200) #100 200
funk(100) #100 10

def my_fun(a,b,c):
  print(a,b,c)

my_fun(10,20,30) #10 20 30
my_fun(a=10,b=20,c=30) #10 20 30
my_fun(10,b=20,c=30) #10 20 30
my_fun(10,20,c=30) #10 20 30
##my_fun(a=10,20,c=30) #Error bcoz positional arguments must come before keyword arguments
my_fun(10,20,b=30) #Error bcoz there are multiple values for b
