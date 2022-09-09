#!/bin/python3

import sys
import os
import subprocess
import inspect



# Complete the function below.

def run_process(cmd_args):
    pn = subprocess.Popen
    with pn(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
        out, err = p.communicate()
    return out
    
if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    cmd_args_cnt = 0
    cmd_args_cnt = int(input())
    cmd_args_i = 0
    cmd_args = []
    while cmd_args_i < cmd_args_cnt:
        try:
            cmd_args_item = str(input())
        except:
            cmd_args_item = None
        cmd_args.append(cmd_args_item)
        cmd_args_i += 1


    res = run_process(cmd_args);
    #f.write(res.decode("utf-8") + "\n")
    
   
    
    if 'with' in inspect.getsource(run_process):
        f.write("'with' used in 'run_process' function definition.\n")
    
    if 'Popen' in inspect.getsource(run_process):
        f.write("'Popen' used in 'run_process' function definition.\n")
        f.write('Process Output : %s\n' % (res.decode("utf-8")))

    f.close()

    
