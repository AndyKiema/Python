#.endswith() Checks whether a string ends with a specific suffix
s='Python'
print(s.endswith('hon')) #True
print(s.endswith('ni')) #False

#.startswith() Checks whether a string starts with a specific substring
print(s.startswith('Py')) #True
print(s.startswith('py')) #False bcoz s starts with P in uppercase

#.find() Checks whether a string contains a specific substring and returns the index of its first occurence
print(s.find('th')) #2- the index of t which is its first occurence
print(s.find('P')) #0
print(s.find('i')) #-1 
print(s.find('p')) #-1 bcoz s starts with P in uppercase
print(s.find('Pi')) #-1 bcoz there is no 'Pi' in 'Python'