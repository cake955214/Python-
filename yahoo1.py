import urllib.request as req
import urllib.parse

url="https://tw.stock.yahoo.com/news_list/url/d/e/N12.html"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("big5")

import bs4

htmlutf8_1 = '<head> <meta charset="utf-8"></head>'
htmlutf8_2 = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tocas-ui/2.3.3/tocas.css"><script src="https://cdnjs.cloudflare.com/ajax/libs/tocas-ui/2.3.3/tocas.js"></script><title>五十大交易量股票</title><style type="text/css">body{padding: 70px 0;}</style>'
htmlutf8_3 = '<div class="ts top fixed inverted borderless large menu"><div class="ts narrow container"><div class="header item">爬蟲股市</div><a href="http://210.240.163.81/data/stock.html" class="item">首頁</a><a href="http://210.240.163.81/data/news.html" class="item">新聞</a><a href="http://210.240.163.81/data/msci.html" class="item">MSCI成分股</a></div></div>'
htmlutf8_4 = '<style>table {margin-left:auto;margin-right:auto;</style>'

root = bs4.BeautifulSoup(data,"html.parser")
file = open("news.html", 'w', encoding='UTF-8')

item1 = root.find("table", id='newListContainer') #div
item1_string = str(item1)

file.write(htmlutf8_1)
file.write(htmlutf8_2)
file.write(htmlutf8_3)
file.write(htmlutf8_4)
item1_string = item1_string[-8788:-84]+item1_string[-81:] # 去除下一頁
file.write(item1_string)
file.close()