#isalum() Checks whether a string only has alphanumeric characters
s='welcome'
print(s.isalnum()) #True
p='welcome2python'
print(p.isalnum()) #True
j='jordan 23'
print(j.isalnum()) #False bcoz there is a space btwn jordan and 23
k='Hey!'
print(k.isalnum())#False because of the exclamation mark is not an alphanumeric character

#isaplha()
print(s.isalpha()) #True
print(p.isalpha()) #False
print(j.isalpha()) #False
print(k.isalpha()) #False
c='welcome to python'
print(c.isalpha()) # False bcoz there are spaces btwn welcome, to and python

#isdigit()
a='123'