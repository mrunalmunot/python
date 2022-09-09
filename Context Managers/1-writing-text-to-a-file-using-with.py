#!/bin/python3

import sys
import os
import inspect



# Complete the function below.

def writeTo(filename, input_text):
    with open(filename, 'w') as f:
        f.write(input_text)

if __name__ == "__main__":
    try:
        filename = str(input())
    except:
        filename = None

    try:
        input_text = str(input())
    except:
        input_text = None

    res = writeTo(filename, input_text)
    
    if 'with' in inspect.getsource(writeTo):
        print("'with' used in 'writeTo' function definition.")
        
    if os.path.exists(filename):
        print('File :',filename, 'is present on system.')
        with open(filename) as fp:
            content = fp.read()
        if content == input_text:
            print('File Contents are :', content)
    

