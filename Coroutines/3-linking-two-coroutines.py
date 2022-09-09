#!/bin/python3

import sys



# Define the function 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def inner(*args, **kwdargs):
        t = coroutine_func(*args, **kwdargs)
        next(t)
        return t
    return inner
# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    try:
        while True:
            x = yield
            print("Expression, {}*x^2 + {}, with x being".format(a,b),x,"equals",str(a*(x**2)+b))
    except GeneratorExit:
        pass    

# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    while True:
        x = yield
        equation1.send(x)
        equation2.send(x)
def main(x):
    n = numberParser()
    n.send(x)
    

if __name__ == "__main__":
    x = float(input())

    res = main(x);
    

