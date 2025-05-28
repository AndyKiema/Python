num1=input("Enter first number:")
num2=input("Enter second number:")
print(type(num1)) #<class 'str'>
print(type(num2)) #<class 'str'>
#Input from user is a string unless the data type is specified
print(num1+num2) #If num1=5 and num2=5, the result for this will be 55
num3=int(input("Enter third number:")) #Data type has been specified as int
num4=int(input("Enter fourth number:")) #Data type has been specified as int
print(type(num3))#<class 'int'>
print(type(num4))#<class 'int'>
print(num3+num4) #If num3=5 and num4=5, the result for this will be 10
#THIS CAN ALSO WORK
num5=input("Enter the fifth number:")
num6=input("Enter the sixth number:")
print(int(num5)+int(num6))#If num 5=5 and num6=5, the result for this will be 10
#LET'S TRY WITH FLOAT NOW
num7=input("Enter the seventh number:")
num8=input("Enter the eighth number:")
print(float(num7)+float(num8))#If num7=1.5 and num8=2.5, the result will be 4.0