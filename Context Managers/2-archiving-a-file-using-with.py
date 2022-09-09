import zipfile
import sys
import os
import inspect

# Define 'writeTo' function below, such that 
# it writes input_text string to filename.
def writeTo(filename, input_text):
    with open(filename, 'w') as f:
        f.write(input_text)    
# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
def archive(zfile, filename):
    with zipfile.ZipFile(zfile, 'w') as zip:
        zip.write(filename)
    

if __name__ == "__main__":
    try:
        filename = str(input())
    except:
        filename = None

    try:
        input_text = str(input())
    except:
        input_text = None

        
    try:
        zip_file = str(input())
    except:
        zip_file = None
        
    res = writeTo(filename, input_text)
    
    if 'with' in inspect.getsource(writeTo):
        print("'with' used in 'writeTo' function definition.")
        
    if os.path.exists(filename):
        print('File :',filename, 'is present on system.')
 
    res = archive(zip_file, filename)
    
    if 'with' in inspect.getsource(archive):
        print("'with' used in 'archive' function definition.")
        
    if os.path.exists(zip_file):
        print('ZipFile :',zip_file, 'is present on system.')    
    

