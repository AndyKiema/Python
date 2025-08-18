"""print('Starting point')
print('Starting point')
print('Starting point')
print('Starting point')
try:
  print(x)
except:
  print('Exception occured') #This will be executed when print(x) throws an exception
print('Starting point')
print('Starting point')
print('Starting point')
print('Starting point')"""
try:
  x,y=10,5
  print(x/y)
except ZeroDivisionError: #Only do this when you are 100% sure of the name of the error
  print('You cant divide by zero') #You cant divide by zero
except: #If there is another exception apart from ZeroDivisionError
  print('Exception handled')
else: #Will be executed if there is no exception
  print('No exception occured')
finally: #Will be executed regardless 
  print('We are done!')

#Raising exceptions- creating your own exceptions
def enterage(num):
  if num<0:
    raise ValueError('Only integers allowed') #Value error has been created
  if num%2==0:
    print('Number is even')
  else:
    print('Number is odd')

enterage(20) #Number is even
enterage(21) #Number is odd
try:
  enterage(-8) #raise ValueError('Only integers allowed')
except ValueError:
  print('Value error exception occured')
finally:
  print('Program completed')