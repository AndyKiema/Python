# A collection which is unordered, mutable and indexed
# Written in curly brackets
# Has key-value pairs
mydictionary={101:'x',102:'y',103:'z'}
print(mydictionary) #{101: 'x', 102: 'y', 103: 'z'}

#Access items to a dictionary
mydict={
    'brand':'Buick',
    'model':'Enclave',
    'year': 2021
}
print(mydict['brand']) #Buick
print(mydict['model']) #Enclave
print(mydict['year']) #2021
#OR
x=mydict.get('brand') 
print(x) #Buick

#Change values in a dictionary
mydict={
    'brand':'Buick',
    'model':'Enclave',
    'year': 2021
}
mydict['year']=2022
print(mydict) #{'brand': 'Buick', 'model': 'Enclave', 'year': 2022}

#Reading items from a dictionary using a loop
mydict={
    'brand':'Buick',
    'model':'Enclave',
    'year': 2021
}
#Read keys only
for i in mydict:
    print(i) #brand model year
#Read values only
for i in mydict:
    print(mydict[i]) #Buick Enclave 2021
#Read keys and values
for x,y in mydict.items():
    print(x,y) #brand Buick model Enclave year 2021

#Check if key exist in dictionary
mydict={
    'brand':'Buick',
    'model':'Enclave',
    'year': 2021
}
if 'brand' in mydict:
    print('Brand exists')
else:
    print('Brand doesnt exist')
    #Brand exists
if 'country' in mydict:
    print('Country exists')
else:
    print('Country doesnt exist')
    #Country doesnt exist
#OR
print('brand' in mydict) #True
print('country' in mydict) #False

#Find number of items in a dictionary
mydict={
    'brand':'Buick',
    'model':'Enclave',
    'year': 2021
}
print(len(mydict)) #3