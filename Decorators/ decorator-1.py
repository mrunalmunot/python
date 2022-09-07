#!/bin/python3

import sys
import os
import datetime as dt


#Add log function and inner function implementation here
def log(func):
    def inner(*args, **kwdargs):
        STDOUT = "Accessed the function -'{}' with arguments {} {}".format(func.__name__, 
        args, kwdargs)
        return STDOUT
    return inner

@log
def greet(msg):
    'Greeting Message : ' + msg
    
#greet = log(greet)

'''Check the Tail section for input/output'''

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        res_lst.append(greet(str(input())))
        fout.write("{}".format(*res_lst))
