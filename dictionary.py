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