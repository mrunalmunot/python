import math
from math import sqrt

def sim_int(p,n,r): 
    si = p*n*r/100
    print("The Simple Interest is",si)
    print("Variables used: ", dir())

def ceil_floor(a,b):    
    print(math.ceil(eval(a)), math.ceil(eval(b)))


def list_of_sqrt(num_of_ele):
    lst=[]
    for i in range(num_of_ele):
        lst.append(round(sqrt(int(input('val {0} =>'.format(i+1)))), 2))
    print("Square Roots: ", lst)
    
# Driver code
print("Get Simple Interest")
p= int(input('p=> '))
n= int(input('n=> '))
r= int(input('r=> '))    
sim_int(p,n,r)

print("\nGet Ceil values")
a=input('a=> ')
b=input('b=> ')
ceil_floor(a,b)

print("\nGet Square Roots values")
num_of_ele=int(input('Enter Num Of Elements: '))
list_of_sqrt(num_of_ele)
