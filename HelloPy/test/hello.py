#encoding: utf-8

colors=['red','black']
print(colors)
colors.append("yeee")
print(colors)
colors.insert(1,"vie")
print(colors) 
colors.extend(['ccc','bbbb'])
print(colors)
colors2=['rrrr','hhh']
colors.extend(colors2)
print(colors)
print(colors.index('yeee'))
print(colors.pop(4))
print(colors)
print(colors.pop())
print(colors.sort())
print(colors)

a={1,2,3}
b={2,3,4,5}
print(a.intersection(b))

a = ({1,2,3,4,5,6},2,3)
print(a.count({1,2,3,4,5}))
d=dict(a="sche",b={"t1",10},c=3)
print(d)
print(d.items())
print(d.keys())
print(d.values())


for k,v in d.items():
    print(k,v)
    print(str(k) +" = "+ str(v))
    print(str(id(k))+" | "+ str(id(v)))
    








