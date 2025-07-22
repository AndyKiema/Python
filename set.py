#A list is a collection that is unordered and unindexed
#Written in curly brackets({})

#Creating a set
myset={"apple","banana","cherry"}
print(myset) #{'cherry', 'apple', 'banana'} NOTICE HOW ORDER HASN'T BEEN MAINTAINED

#Accessing items from a set
#NOT POSSIBLE BECAUSE A SET IS UNINDEXED

#Check if value exists in set
myset={"apple","banana","cherry"}
if 'banana' in myset:
    print('Banana is present')
else:
    print('No banana')
#OR
print('banana' in myset) #True
print('mango' in myset) #False

#Adding items to set
#add()- add a single item
#update()- add multiple items
myset={"apple","banana","cherry"}
myset.add('orange')
print(myset) #{'banana', 'orange', 'apple', 'cherry'}
myset.update(['mango','lemon','strawberry'])
print(myset) #{'orange', 'lemon', 'banana', 'apple', 'strawberry', 'cherry', 'mango'}