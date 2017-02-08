import os
import time
import glob

print(os.path.abspath("."))

print(os.path.basename("/Users/leehan/git/python/helloPy/test/binary"))
print(os.path.dirname("/Users/leehan/git/python/helloPy/test/binary"))

print(os.path.exists("/Users/leehan"))
print(os.path.exists("/usr"))

print(os.path.expanduser("~/leehan"))

print(os.environ)
print(os.path.expandvars("$SYSTEMROOT $USER"))
print(os.path.expandvars("$HOME"))

print(os.path.getmtime("binary"))
print(time.gmtime(os.path.getmtime("binary")))
print(time.ctime(os.path.getmtime("binary")))

print(os.path.getctime("hello.py"))
print(time.gmtime(os.path.getctime("hello.py")))
print(time.ctime(os.path.getctime("hello.py")))


print(os.path.getsize("hello.py"))
print(os.path.getsize("text.txt"))

print(os.path.isfile("hello.py"))
print(os.path.isfile("/Users"))
print(os.path.isdir("hello.py"))
print(os.path.isdir("/Users"))


print(glob.glob(os.path.abspath(".") + "/*.txt"))
for i in glob.iglob(os.path.abspath(".") + "/*.txt"):
    print(i)
    
def traverse(dir, depth):
    for obj in glob.glob(dir+"/*"):
        if depth==0:
            prefix = "|--"
        else:
            prefix ="|" + " "*depth + "+--"
            
        if os.path.isdir(obj):
            print(prefix +"(D)" + os.path.basename(obj))
            traverse(obj, depth+1)
        elif os.path.isfile(obj):
            print(prefix +"(F)" + os.path.basename(obj))
        else:
            print(prefix + "unknown", obj)

traverse("/Users/leehan/git/python", 0)

