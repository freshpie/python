#encoding: utf-8

class Person:
    PersonName = "leehan"
    
    def classPrint(self):
        print(self.PersonName)
        
p1 = Person()

p1.classPrint()

Person.title="ttileeeee!!!"

p2 = Person()

print(p1.title)
print(p2.title)

p1.age = 34
p2.age = 22
p2.title = "eeeeeeeeeeee"
print(p1.age)
print(p2.age)

print(p1.title)
print(p2.title)

print(isinstance(p1, Person))


class InitClass:
    inVal=""
    def __init__(self, value):
        self.inVal = value
        print("InitClass __init__ : " , value)
        #print(self)
        
    def __del__(self):
        print("InitClass __del__ : " , self.inVal)
        #print(self)
        
class InitClass2:
    inVal=""
    def __init__(self, value):
        self.inVal = value
        print("InitClass2 __init__ : " , value)
        #print(self)
        
    def __del__(self):
        print("InitClass2 __del__ : " , self.inVal)
        #print(self)

initClass = InitClass("11111")

initClass2 = InitClass2("22222")

print(initClass.inVal)
def foo():
    d = InitClass("eqque")
    
foo()


class methodExtenseTest:
    inClassValue = "Surprise!!!"
    def isStaticCall(value):
        print("isStaticCall : ", value)
        #print(self.inClassValue)
    excutableIsStaticCall = staticmethod(isStaticCall)

    def isClassCall(self, value):
        print("isClassCall : ", value)
        print(self.inClassValue)
    excutableIsClassCall = classmethod(isClassCall)
    
    def __init__(self):
        print("methodExtenseTest __init__")
    def __del__(self):
        print("methodExtenseTest __del__")
        
methodExtenseTest.excutableIsStaticCall("excutableIsStaticCall!!!")

methodExtenseTest.excutableIsClassCall("excutableIsClassCall!!!!")


m1 = methodExtenseTest()

#m1.isStaticCall("111111111111111")
#m1.isClassCall("222222222222222")

class GString:
    def __init__(self, init=None):
        self.content = init
    def __sub__(self, strVal):
        for i in strVal:
            self.content = self.content.replace(i,'')
        return GString(self.content)
    def remove(self, strVal):
        for i in strVal:
            self.content = self.content.replace(i,'')
        return GString(self.content)
    

gString = GString("leehan")
gString.remove("lee")
print(gString.content)

gString2 = GString("leehan")
gString2 - "han"
print(gString2.content)

class Animal:
    print("Animal class")
class Tiger:
    a=10
    print("tiger class")
    def __init__(self):
        print("tiger")
class Lion:
    b=20
    print("lion class")
    def __init__(self):
        print("lion")
        
class Liger(Tiger,Lion):
    print("liger class")
    def __init__(self):
        print("liger")
    def ligerMove(self):
        print("liger moved")
        
print(issubclass(Liger, Tiger))
print(issubclass(Liger, Lion))
print(issubclass(Liger, Liger))
print(issubclass(Liger, Animal))

liger = Liger()
liger.c = 30
print(liger.a)
print(liger.b)
print(liger.c)
#print(liger.x) #AttributeError: Liger instance has no attribute 'x'
liger.ligerMove()
#liger.ligerMoveX() #AttributeError: Liger instance has no attribute 'ligerMoveX'

liger = Liger
#liger.ligerMove()
liger.ligerMove(Liger())







print("end")



