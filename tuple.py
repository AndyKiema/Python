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

 #Getting length of a tuple
 mytuple3=('kale','spinach','cabbage')
 print(len(mytuple3)) #3

#Add items in a tuple
#Must be converted to a list first
 mytuple3=('kale','spinach','cabbage')
veglist=list(mytuple3)
veglist.append('sprout')
print(veglist) #['kale', 'spinach', 'cabbage', 'sprout']
mytuple3=tuple(veglist)
print(mytuple3)
#OR
mytuple3=('kale','spinach','cabbage')
veglist=list(mytuple3)
veglist.insert(2,'sprout')
print(veglist) #['kale', 'spinach', 'sprout', 'cabbage']
mytuple3=tuple(veglist)
print(mytuple3) #('kale', 'spinach', 'sprout', 'cabbage')

#Remove items from a tuple
mytuple3=('kale','spinach','cabbage')
veglist=list(mytuple3)
veglist.pop(2)
print(veglist) #['kale', 'spinach']
mytuple3=tuple(veglist)
print(mytuple3) #('kale', 'spinach')

#Copy a tuple
mytuple3=('kale','spinach','cabbage')
mytuple4=tuple(mytuple3)
print(mytuple4)