#Single inheritance
class A:
  def m1(self):
    print('This is m1 method from class A')
class B(A):
  def m2(self):
    print('This is m2 method from class B')

b1=B()
b1.m1() #This is m1 method from class A
b1.m2() #This is m2 method from class B

class C:
  x,y=10,20
  def m3(self):
    print(self.x,self.y)

class D(C):
  a,b=100,200
  def m4(self):
    print(self.a+self.b)

d1=D()
d1.m3() #10 20
d1.m4() #300

#Mutli-level inheritance
"""class E:
  c,d=1,2
  def m5(self):
    print(self.c,self.d)

class F(E):
  i,j=100,200
  def m6(self):
    print(self.i,self.j)

class G(F):
  k,l=50,60
  def m7(self):
    print(self.k,self.l)

g1=G()
g1.m5() #1 2
g1.m6() #100 200
g1.m7() #50 60

f1=F()
f1.m5() #1 2
f1.m6() #100 200
#f1.m7()""" #Error bcoz class F doesnt have m7()

#Hierarchy inheritance
class E:
  c,d=1,2
  def m5(self):
    print(self.c,self.d)

class F(E):
  i,j=100,200
  def m6(self):
    print(self.i,self.j)

class G(E):
  k,l=50,60
  def m7(self):
    print(self.k,self.l)

g1=G()
g1.m5() #1 2
#g1.m6() #Error bcoz class G has no relationship with class F
g1.m7() #50 60

f1=F()
f1.m5() #1 2
f1.m6() #100 200
f1.m7() #Error bcoz class F had no relationship with class G
