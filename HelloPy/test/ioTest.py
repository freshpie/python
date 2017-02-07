#encoding: utf-8
import pickle

print("{0:#>10}".format("han"))
print("{0:#^10}".format("han"))
print("{0:#<10}".format("han"))

print("{0:#=10}".format(12))
print("{0:#=10}".format(-12))

print("{0:#>-10}".format(12))
print("{0:#>-10}".format(-12))
print("{0:#>+10}".format(12))
print("{0:#>+10}".format(-12))
print("{0:#> 10}".format(12))
print("{0:#> 10}".format(-12))


#a= input("a : ")
#b= input("b : ")
#c= int(a)/int(b)
#print("{0:.2%}".format(c))
#open(file, mode, buffering, encoding, errors, newline, closefd, opener)
f=open("text.txt", "w", encoding="utf-8")

f.write("aaaa")
f.write("\n안녕하세요.")
f.close()

f=open("text.txt", encoding="utf-8")
print(f.read())

f.seek(0)

print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.close()
print(f.closed)

class test:
    classVar = '2322'
    def testPrint(self):
        self.classVar = "이한"
        print(self.classVar + " 안녕하세요")
"""
f=open("binary", "wb")
c1 = test()
pickle.dump(c1, f)
f.close()
"""

f=open("binary", "rb")
a = pickle.load(f)
a.testPrint()
f.close()


#numArr = [1,2,3,574,3,2]
#f=open("binary", "wb")
#pickle.dump(numArr, f)

f=open("binary", "rb")
numArr = pickle.load(f)
f.close()
print(numArr)





