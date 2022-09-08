import inspect

from abc import ABC, abstractmethod

# Define the abstract class 'Animal' below
# with abstract method 'say'
class Animal(ABC):
    @abstractmethod
    def say(self):
        pass

# Define class Dog derived from Animal
# Also define 'say' method inside 'Dog' class
class Dog(Animal):
    def say(self):
        return "I speak Booooo"

if __name__ == '__main__':
    
    if issubclass(Animal, ABC):
        print("'Animal' is an abstract class" )
    
    if '@abstractmethod' in inspect.getsource(Animal.say):
        print("'say' is an abstract method")
        
    if issubclass(Dog, Animal):
        print("'Dog' is dervied from 'Animal' class" )
    
    d1 = Dog()
    print("Dog,'d1', says :", d1.say())
