"""name='John'
age=30
salary=50000.00"""

#Instead of writing three lines of code, just write like this:
name,age,salary='John',30,50000.00
print(name) #John
print(age) #30
print(salary) #50000
print(name,age,salary) #John 30 50000

print("My name is",name)#My name is John
print("My age is",age)#My age is 30
print("My salary is",salary,"dollars")#My salary is 50000 dollars
print("My name is %s My age is %d My salary is %g"%(name,age,salary)) # %s=string, %d=digit, %g=decimal number
print("My name is {} My age is {} My salary is {}".format(name,age,salary)) #My name is John My age is 30 My salary is 50000.0
print("My name is {} My age is {} My salary is {}".format(salary,age,name)) #My name is 50000.0 My age is 30 My salary is John