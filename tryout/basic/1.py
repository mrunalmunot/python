import os
import math
#Import the necessary packages


def sim_int(p,n,r): 
    si = p*n*r/100
    print("The Simple Interest is",si)
    print(dir())

def ceil_floor(a,b):
    
    print(math.ceil(eval(a)))
    print(math.floor(eval(b)))

from math import sqrt
def lists():
    lst=[]
    for i in range(5):
        lst.append(round(sqrt(int(input())), 2))
    print(lst)
    print(type(lst[-1]))
    
# Driver code
p= int(input())
n= int(input())
r= int(input())    
sim_int(p,n,r)


a=input()
b=input()
ceil_floor(a,b)

lists()
