import sys
import traceback

class NegativeDivisionError(Exception):
    def __init__(self,value):
        self.value = value


def foo(x):
    assert type(x) == int, ["타입 오루ㅠ","wfef"]
    return x*10

try:
    a=[1,2,3]
    #print(a[6])
    #raise NameError("rrr")
    #raise NegativeDivisionError(4)
    raise ZeroDivisionError
except IndexError as e:
    print("out of index!!!!!")
    print(e.args)
except TypeError:
    print("type error!!!")
except NameError as e:
    print(e.args)
    print("name error!!!")
except NegativeDivisionError as e:
    print(e.args)
    print(e.value)
    print("NegativeDivisionError 에러가 났음")
except:
    print("에러가 났음")
    exc, value, tb = sys.exc_info()
    print(exc, value, tb)    
    traceback.print_exc()
else:
    print("정상입니다.")
finally:
    print("무조건~")
    
try:
    print(foo(12))
except AssertionError as e:
    print(e.args[0])
    
