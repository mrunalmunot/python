import sys
import os
# Define 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def inner(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        next(c)
        return c
    return inner
# Define coroutine 'linear_equation' as specified in previous exercise
@coroutine_decorator
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
    
    equation1.send(6)
    
    
