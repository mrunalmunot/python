import inspect
import re
import unittest
import math

class Circle:
    
    def __init__(self, radius):
        # Define initialization method:
        if isinstance(radius, str):
            raise TypeError("radius must be a number")
        if radius>1000 or radius < 0:
            raise ValueError("radius must be between 0 and 1000 inclusive")
        
        self.radius = radius
        
    def area(self):
        # Define area functionality:
        return round(self.radius*self.radius*math.pi, 2)
    def circumference(self):
        # Define circumference functionality:
        return round(self.radius*2*math.pi, 2)
        
class TestCircleArea(unittest.TestCase):
    
    def test_circlearea_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # its area is 19.63.
        c1 = Circle(2.5)
        x = c1.area()
        self.assertEqual(x, 19.63)        
        
    def test_circlearea_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if 
        # its area is 0.
        c2 = Circle(0)
        x = c2.area()
        self.assertEqual(x, 0)        
        
    def test_circlearea_with_max_radius(self):
        # Define a circle 'c3' with radius 1000.1. and check if 
        # its area is 3141592.65.
        c3 = Circle(1000)
        x = c3.area()
        self.assertEqual(x, 3141592.65)
        
if __name__ == '__main__':
    
    fptr = open('output.txt', 'w')
    
    runner = unittest.TextTestRunner(fptr)
    
    unittest.main(testRunner=runner, exit=False)
    
    fptr.close()
    
    with open('output.txt') as fp:
        output_lines = fp.readlines()
        #print(output_lines)
    
    
    pass_count = [ len(re.findall(r'\.', line)) for line in output_lines if line.startswith('.')
                     and line.endswith('.\n')]
    
    pass_count = pass_count[0]
                       
    print(str(pass_count))
                       
    doc1 = inspect.getsource(TestCircleArea.test_circlearea_with_random_numeric_radius)
    doc2 = inspect.getsource(TestCircleArea.test_circlearea_with_min_radius)
    doc3 = inspect.getsource(TestCircleArea.test_circlearea_with_max_radius)
    
    assert1_count = len(re.findall(r'assertEqual', doc1))
    
    print(str(assert1_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc2))
    
    print(str(assert1_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc3))
    
    print(str(assert1_count))
