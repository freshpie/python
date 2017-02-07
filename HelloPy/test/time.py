import time
import datetime


print(time.time())
print(time.gmtime())
print(time.localtime())
t=time.gmtime()
print(t.tm_year)
print(time.gmtime().tm_year)
print(time.struct_time.tm_year)
print(time.asctime())

print(time.strftime("%Y%m%d  %A"))
print(time.strftime("%Y", time.gmtime()))


td1 = datetime.timedelta(days=-3)
td2 = datetime.timedelta(hours=5)

print(td1)
print(td2)
print(td1 + td2)

d1 = datetime.date.today()
d2 = datetime.date(2017, 1, 23)
print(d1)
print(d2)
d3 = d1-d2
print(d3) #timedelta
print(d3.days)
