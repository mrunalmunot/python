import os

def stringops():
    a=input("Enter a string: ")
    print(a[3:5])
    print(a[6:9])    
    print(len(a))  
    b=a  
    print(b.strip())
    print(a.replace(a[5], 'p'))
    print(a.lower())
    

def stringopss():
    a=input("Enter a string: ")
    print(a.count(a[4]))
    print(a.encode())
    print(a.isdigit())
    print(a.find('l', 2, 5))
    print(a.rfind('W'))    
    
def listup():
    lst = []    
    for i in range(5):
        lst.append(int(input()))
    
    print(lst[1::2])
    print(lst[0::2])
    print(len(tuple(lst)))
    lst[1]=5
    print(tuple(lst))
    

stringops()
stringopss()
listup()
