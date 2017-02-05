#encoding: utf-8
from telnetlib import theNULL

def plus(value1, value2):
    return int(value1) + int(value2)

def minus(value1, value2):
    "This module is integer Sum"
    return int(value1) - int(value2)

def noneReturn(Value):
    a=0
    
def immuTest():
    return bbb + 1

def mmuTest():
    ccc[0]="TTT"
    return ccc

print(plus(1,2))
print(minus(5,10))
print(plus("3",5))
#print(plus("a",5))

print(id(plus(0,3)))
print(id(plus("1",2)))
print(id(plus(2,2)))

#print(noneReturn())
bbb = 0
ccc = [1,2,3]
print(immuTest())
print(bbb)
print(mmuTest())
print(ccc)


gVal=10
def gValTest(isGlobalUse):
    if isGlobalUse == True:
        print("true in")
        gVal = 5
        print(gVal)
    else:
        print("false in")
        #global gVal
        gVal = 5
        print(gVal)
    return 0

gValTest(True)
print(gVal)


def dictValTest(value, **dictValue):
    print(value)
    print(dictValue)
    
dictValTest("leehan", name="han", age=30, man=True)

g=lambda x,y: x+y
print(g(333,5))
print((lambda x,y,z: x+y*z)(1,2,3))


help(minus)

ia='asdf'
iterA = iter(ia)
for x in iterA:
    print(x)

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for char in reverse('asdf'):
    print(char)
    
    
def cusIter(*value):
    for returnVal in value:
        yield returnVal
        
iterB = iter(cusIter("efv",22,33,"edfv"))
for x in iterB:
    print(x)


