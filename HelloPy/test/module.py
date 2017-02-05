import math
#import simpleSet
import sys
#import classTest
from classTest import classTestMethod1 as ctm1
 
print("moduleModuleName",__name__)

print(math.pow(2, 10))
print(math.pi)

print(dir(math))
print(sys.path)

ctm1()
del ctm1
#classTestMethod1()

def classTestMethod1():
    print("BBBBBBBBBBBBBBBBB")
classTestMethod1()