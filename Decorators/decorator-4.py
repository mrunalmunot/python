import os
import sys

def bold_tag(func):
    
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'
        
    return inner

#Implement italic_tag below
def italic_tag(func):
    def inner(*args, **kwdargs):
        return '<i>'+ func(*args, **kwdargs) +'</i>'
    return inner

@italic_tag
def say(msg):
    return msg
    
'''Check the Tail section for input/output'''
if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        res_lst.append(say(input()))
        fout.write("{}".format(*res_lst))
