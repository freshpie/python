#encoding: utf-8

a=1
if a and 10/a:
    print(a)
else:
    print("else")

if int(a) & int(10/a):
    print(a)
else:
    print("else")

t1=["a1","a2","a33","a4"]
t2=["b1","b2","b3","b4"]
print([i for i in t1 if len(i)==3])
print([x+y for x in t1 for y in t2])

l1 = [10,25,30]
iterL1= filter(None, l1)
for i in iterL1:
    print("1item : {0} {1} {2}".format(i,i+1,i+i))

def filter1(i):
    return i>20
    
iterL2 = filter(filter1, l1)
for i in iterL2:
    print("2item : {0} {1} {2}".format(i,i+1,i+i))

iterL3 = filter(lambda i:i>29, l1)
for i in iterL3:
    print("3item : {0} {1} {2}".format(i,i+1,i+i))
    
    
print(range(10))
print(range(3,8))
print(range(10,0,-2))
print(range(0,10,3))

x=[1,2,3]
y=[5,2,2]
def mapSum(inputVal):
    return inputVal + 10
def mapSum2(inputVal1, inputVal2):
    if inputVal1 == None:
        inputVal1 = 0
    if inputVal2 == None:
        inputVal2 = 0
    return inputVal1 + inputVal2
print(map(lambda i:i+3, x))
print(map(mapSum, x))
print(map(mapSum2, x, y))
print(x)
print(y)