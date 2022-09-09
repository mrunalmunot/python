#!/bin/python3

import sys



# Define the coroutine function 'linear_equation' below.

def linear_equation(a, b):
    try:
        while True:
            x = yield
            print("Expression, {}*x^2 + {}, with x being".format(a,b),x,"equals",str(a*(x**2)+b))
    except GeneratorExit:
        pass    
        
if __name__ == "__main__":
    a = float(input())

    b = float(input())

    equation1 = linear_equation(a, b)
    
    next(equation1)
    
    equation1.send(6)
    
    

