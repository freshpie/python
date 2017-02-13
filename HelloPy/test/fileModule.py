from os import *
import time
import glob

print(path.abspath("."))

print(path.basename("/Users/leehan/git/python/helloPy/test/binary"))
print(path.dirname("/Users/leehan/git/python/helloPy/test/binary"))

print(path.exists("/Users/leehan"))
print(path.exists("/usr"))

print(path.expanduser("~/leehan"))

print(environ)
print(path.expandvars("$SYSTEMROOT $USER"))
print(path.expandvars("$HOME"))

print(path.getmtime("binary"))
print(time.gmtime(path.getmtime("binary")))
print(time.ctime(path.getmtime("binary")))

print(path.getctime("hello.py"))
print(time.gmtime(path.getctime("hello.py")))
print(time.ctime(path.getctime("hello.py")))


print(path.getsize("hello.py"))
print(path.getsize("text.txt"))

print(path.isfile("hello.py"))
print(path.isfile("/Users"))
print(path.isdir("hello.py"))
print(path.isdir("/Users"))


print(glob.glob(path.abspath(".") + "/*.txt"))
for i in glob.iglob(path.abspath(".") + "/*.txt"):
    print(i)
    
def traverse(dir, depth):
    for obj in glob.glob(dir+"/*"):
        if depth==0:
            prefix = "|--"
        else:
            prefix ="|" + " "*depth + "+--"
            
        if path.isdir(obj):
            print(prefix +"(D)" + path.basename(obj))
            traverse(obj, depth+1)
        elif path.isfile(obj):
            print(prefix +"(F)" + path.basename(obj))
        else:
            print(prefix + "unknown", obj)

traverse("/Users/leehan/git/python", 0)

