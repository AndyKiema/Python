a=100
b=200
print(a,b) #this will print both a and b in the same line 100 200
c="Yes"
print(a,b,c) #100 200 Yes
print(c,b,a) #Yes 200 100

#instead of writing x=100 y=100 z=100, just write this:
x=y=z=100
print(z)

b,a=a,b #b has taken the value of a, a has taken the value of b
print(a,b) #200 100 