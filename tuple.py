#A tuple is a collection which is ordered and unchangeable
#Written with round brackets ()
#Is immutable- values cant be changed, removed or added

#Printing a tuple
mytuple=('apple','banana','cherry')
print(mytuple) #('apple', 'banana', 'cherry')

#Accessing items from a tuple
mytuple=('apple','banana','cherry')
print(mytuple[0]) #apple
print(mytuple[-1]) #cherry
tuple1=()
print(tuple1) #()

#Printing range 
mytuple=('apple','banana','cherry')
print(mytuple[0:2]) #('apple', 'banana')
print(mytuple[-2:]) #('banana', 'cherry')

#Printing tuple items using a loop
mytuple=('apple','banana','cherry')
for i in mytuple:
 print(i)

 #Checking if item exists in tuple or not
mytuple3=('kale','spinach','cabbage')
if 'brocolli' in mytuple3:
 print('brocolli exists')
else:
 print('brocolli is not there')