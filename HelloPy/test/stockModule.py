import urllib.request
import bs4
import time



with open("corpList.csv", 'rt', encoding='utf-8') as f:
    stocks = f.readlines()[1:]
    #print(stocks)

    for stock in stocks:
        columns = stock.split(",")
        name,code = columns[0], columns[1]
        #print(name, code)

        request = urllib.request.Request("http://finance.daum.net/item/main.daum?code="+code)
        response = urllib.request.urlopen(request)
        content = response.read()
        #print(content)

        soup = bs4.BeautifulSoup(content,'html5lib')
        soup_today = soup.select("ul.list_stockrate .curPrice")
        soup_rate = soup.select("ul.list_stockrate .rate")
        #print(soup)
        #print(soup_today)
        #print(soup_rate)
        try:
            today = soup_today[0].text
            rate = soup_rate[0].text
        except IndexError:
            today = "None"
            rate = "None"

        print("{0: <15} {1: <10} {2: >5}".format(name, today, rate))
        time.sleep(1)


#http://finance.daum.net/item/main.daum?code=005930

'''
f = open("corpList.csv", 'rt', encoding='utf-8')

sArr = f.readlines()
for ss in sArr:
    print(ss)
'''

'''
lineStr=""
for ss in s:
    if(ss == '\n'):
        print(lineStr)
        lineStr = ""
    else:
        lineStr = lineStr + ss
'''

#f.close()
