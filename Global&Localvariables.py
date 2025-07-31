global_var=20 #Global variable
def func():
  local_var=10 #Local variable
  print(global_var) #20
  print(local_var) #10
print(global_var) #20
##print(local_var) #Error

#NB: LOCAL VARIABLES CAN ONLY BE ACCESSED WITHIN A FUNCTION
    # GLOBAL VARIABLES CAN BE ACCESSED ANYWHERE
func()
#Using Global variable in function and update value
xy=100

def cool():
  global xy
  xy=200
  print(xy)

cool() #200 If this function isnt called first, print(xy) below will be 100
print(xy) #200

def cool2():
  global x
  x=150
  print(x)

cool2() #150 If this function isnt called first, print(x) below will be an error
print(x) #150

