#A list is a collection that is ordered and changeable
#Written in square brackets ([])
#Is mutable- values can be changed, removed or added
#Can contain different data types

list1=[10,20,30,40]
list2=['apple','banana','cherry']
list3=[10,'apple',30.1]
list4=list() #Empty list

#Printing a list
print(list1) #[10, 20, 30, 40]
print(list2) #['apple', 'banana', 'cherry']
print(list3) #[10, 'apple', 30.1]
print(list4) #[]

#Accessing items from a list
list2=['apple','banana','cherry'] #Lists are zero indexed
print(list2[0]) #apple
print(list2[2]) #cherry
print(list2[-1]) #cherry -1 means the last one/the first one from the end
print(list2[-2]) #banana -2 means the second last one/the second one from the end

#Printing range 
list5=['ali','frazier','foreman','liston','patterson','louis']
print(list5[2:4]) #['foreman', 'liston'] Starting index is zero index, ending index is one indexed
print(list5[1:5]) #['frazier','foreman','liston','patterson']
print(list5[-4:-1]) #['foreman', 'liston', 'patterson'] When indexes are negative, the first one is one indexed, the second one is zero indexed
print(list5[1:-2]) #['frazier','foreman','liston']
print(list5[-5:3]) #['frazier','foreman']

#Change list item values
list2=['apple','banana','cherry']
print(list2)
list2[0]='orange' #Change apple to orange
print(list2)

#Printing list items using a loop
list2=['apple','banana','cherry']
for i in list2:
    print(i)

#Checking if item exists in list or not
list2=['apple','banana','cherry']
if 'apple' in list2:
    print('Apple exists')
else:
    print("Apple doesn't exist")

if 'mango' in list2:
    print("Mango exists")
else:
    print("Mango doesn't exist")

#Getting length of a list
list2=['apple','banana','cherry']
print(len(list2)) #3

#Add items in a list
list2=['apple','banana','cherry']
list2.append('orange') #append() adds it to the end of the list
print(list2) #['apple', 'banana', 'cherry', 'orange']
list2=['apple','banana','cherry']
list2.insert(2,'orange') #insert() adds it to a particular position
print(list2) #['apple', 'banana', 'orange', 'cherry']

#Remove items from a list
list2=['apple','banana','cherry']
list2.pop(0)
print(list2) #['banana', 'cherry']
#OR
list2=['apple','banana','cherry']
del list2[0]
print(list2) #['banana', 'cherry']
#OR
list2=['apple','banana','cherry']
list2.clear()
print(list2) #[]

#Copy a list
list2=['apple','banana','cherry']
list3=list(list2)
print(list3)
#OR
list2=['apple','banana','cherry']
list4=list2.copy()
print(list4)