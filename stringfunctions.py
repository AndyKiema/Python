#isalum() Checks whether a string only has alphanumeric characters
s='welcome'
print(s.isalnum()) #True
p='welcome2python'
print(p.isalnum()) #True
j='jordan 23'
print(j.isalnum()) #False bcoz there is a space btwn jordan and 23
k='Hey!'
print(k.isalnum())#False because of the exclamation mark is not an alphanumeric character

#isaplha() Checks whether a string only has alphabetic characters
print(s.isalpha()) #True
print(p.isalpha()) #False
print(j.isalpha()) #False
print(k.isalpha()) #False
c='welcome to python'
print(c.isalpha()) # False bcoz there are spaces btwn welcome, to and python

#isdigit() Checks whether a string only has numeric characters
a='123'
print(a.isdigit()) #True
b='jordan'
print(b.isdigit()) #False
c='jordan 23'
print(c.isdigit()) #False bcoz of the space and jordan
d='12,000'
print(d.isdigit()) #False bcoz of the comma

#isidentifier() Checks whether a string is a valid identifier
#Rules for a valid identifier:
  #1.Starts with a letter/underscore(_)
  #2.Can contain letters, numbers or underscores
  #3.Cant start with a digit
e='yes'
print(e.isidentifier()) #True
f='2sharp'
print(f.isidentifier()) #False bcoz it starts with a number
g='_no'
print(g.isidentifier()) #True
k='Hey!'
print(k.isidentifier()) #False bcoz it has an exclamation mark
