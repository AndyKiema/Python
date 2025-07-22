#A list is a collection that is unordered and unindexed
#Written in curly brackets({})
#It is mutable

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

#Find number of items in a set
myset={"apple","banana","cherry"}
print(len(myset)) #3

#Remove item from a set
myset={"apple","banana","cherry"}
myset.remove('banana')
print(myset) #{'apple', 'cherry'}
# myset.remove('grape') 
# print(myset) Returns error
#OR
myset={"apple","banana","cherry"}
myset.discard('banana')
print(myset) #{'cherry', 'apple'}
myset.discard('grape')
print(myset) #{'apple', 'cherry'} The set will still be printed. No error will be thrown. That's the difference between discard and remove

#Clear all items from a set
myset={"apple","banana","cherry"}
myset.clear()
print(myset) #set()
#Delete the set itself
myset={"apple","banana","cherry"}
del myset
print(myset) #THROWS ERROR