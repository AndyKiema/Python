import sys
sys.path.append('C:/Users/Administrator/Desktop/python/package2')
import module3
import module4
obj=module3.Third()
obj.display() #This is from module 3
obj2=module4.Fourth()
obj2.show() #This is from module 4
from module3 import* #(* means all public names)
from module4 import*
  
obj=Third() 
obj.display()#This is from module 3

obj2=Fourth()
obj2.show() #This is from module 4
