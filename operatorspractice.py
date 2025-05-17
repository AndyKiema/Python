a=100
b=50
sum=a+b
print(sum) #150
diff=a-b
print(diff)#50
print(type(sum)) #<class 'int'>
mult=a*b
print(mult) #5000
print(type(mult)) #<class 'int>
divi=a/b
print(divi) #2.0
print(type(divi)) #<class float>
coef=3//2
print(coef) #1
print(type(coef)) #<class 'int'>
remai=3%2
print(remai) #1
print(type(remai)) #<class 'int'>
print(3<2) #False
x=True
print(type(x)) #<class 'bool'>
print(a and b) #50
print(a or b) #100
m=90
n=0
print(m and n) #0
print(m or n) #90  

#OR returns the first truthy value and the last falsy value it finds
#AND returns the first falsy value and last truthy value it 
p=0
q=90
print(p and q) #0
print(p or q) #90  

d=0
e=10
f=20
print(d and e and f) #0
print(d or e or f) #10
