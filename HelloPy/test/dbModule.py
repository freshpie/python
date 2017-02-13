import sqlite3

conFile = sqlite3.connect("test.db")
conMem = sqlite3.connect(":memory:")

curFile = conFile.cursor()
curMem = conMem.cursor()

#curFile.execute("CREATE TABLE PhoneBook(name text, phone_num text)")
curFile.execute("INSERT INTO PhoneBook VALUES('leehan', '010-333-3333')")
curMem.execute("CREATE TABLE PhoneBook(name text, phone_num text)")
curMem.execute("INSERT INTO PhoneBook VALUES('leehan', '010-333-3333')")

name = 'kimhan'
phoneNum = '010-333-1111'
curFile.execute("INSERT INTO PhoneBook VALUES(?,?)", (name, phoneNum))
curMem.execute("INSERT INTO PhoneBook VALUES(?,?)", (name, phoneNum))

name = '333'
phoneNum = '010-221235-1111'
curFile.execute("INSERT INTO PhoneBook VALUES(:name,:phone)", {"name":name, "phone":phoneNum})
curMem.execute("INSERT INTO PhoneBook VALUES(:name,:phone)", {"name":name, "phone":phoneNum})

curFile.execute("SELECT * FROM PhoneBook")
curMem.execute("SELECT * FROM PhoneBook")
#print(len(curFile.fetchall()))

#print(curFile.fetchall())
#print(curMem.fetchall())

rowsFile = curFile.fetchall()
rowsMem = curMem.fetchall()

for row in curFile:
    print(row)

print("rowsFile size:", len(rowsFile))
for row in rowsFile:
    print(row)

print("--------------------------------------------")
curFile.execute("SELECT * FROM PhoneBook ORDER BY name")
for row in curFile:
    print(row)

print("--------------------------------------------")
#str1 -> str2 : 음수
#str1 == str2 : 0
#str1 <- str2 : 양수 
def orderFunc1(str1, str2):
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1 > s2) - (s1 < s2)

conFile.create_collation('customOrder1', orderFunc1)
curFile.execute("SELECT * FROM PhoneBook ORDER BY name COLLATE customOrder1")
for row in curFile:
    print(row)
    
print("--------------------------------------------")
def orderFunc2(str1, str2):
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1 < s2) - (s1 > s2)

conFile.create_collation('customOrder2', orderFunc2)
curFile.execute("SELECT * FROM PhoneBook ORDER BY name COLLATE customOrder2")
for row in curFile:
    print(row)

print("--------------------------------------------")
curFile.execute("SELECT name, length(name) FROM PhoneBook")
for row in curFile:
    print(row)

print("--------------------------------------------")
curFile.execute("SELECT random(*)")
for row in curFile:
    print(row)

print("--------------------------------------------")
for l in conFile.iterdump():
    print(l)


#conFile.commit()
#conMem.commit()


'''
ps1) cur.moveToFirst() cur.MoveTo(xx)... 이렇게 검색결내에서 레크드 이동 안됨
         cursor 객체는 순차 읽기만 가능.   
        따라서 임의의 레코드를 처리하려면 아래와 같이 쿼리 결과를 list 형식으로 를 만들어 사용.
         queryData =  cur.fetchall()     
ps2) 쿼리 결과가 몇건인지 나타내는 cur.rowcount  는 Python 에서는 작동안함.
         cur.execute("SELECT count() FROM PhoneBook;")
         rows = cur.fetchone()
         형식으로 쿼리 결과 갯수를 알아 내야함.
'''