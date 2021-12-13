import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2313"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4

htmlutf8='<head>  <meta charset="utf-8"></head>'	
btn='<a href="http://210.240.163.81/data/day/2313_detail.html">每日財報</a><br><br>'

file = open("2313.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2313"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2313"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2317"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2317_detail.html">每日財報</a><br><br>'

file = open("2317.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2317"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2317"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=3037"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/3037_detail.html">每日財報</a><br><br>'

file = open("3037.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=3037"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=3037"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=3481"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/3481_detail.html">每日財報</a><br><br>'

file = open("3481.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=3481"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=3481"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2888"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2888_detail.html">每日財報</a><br><br>'

file = open("2888.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2888"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2888"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2891"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2891_detail.html">每日財報</a><br><br>'

file = open("2891.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2891"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2891"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2449"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2449_detail.html">每日財報</a><br><br>'

file = open("2449.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2449"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2449"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2303"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2303_detail.html">每日財報</a><br><br>'

file = open("2303.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2303"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2303"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2448"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2448_detail.html">每日財報</a><br><br>'

file = open("2448.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2448"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2448"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=8150"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/8150_detail.html">每日財報</a><br><br>'

file = open("8150.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=8150"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=8150"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=4938"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/4938_detail.html">每日財報</a><br><br>'

file = open("4938.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=4938"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=4938"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2883"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2883_detail.html">每日財報</a><br><br>'

file = open("2883.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2883"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2883"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2337"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2337_detail.html">每日財報</a><br><br>'

file = open("2337.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2337"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2337"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2882"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2882_detail.html">每日財報</a><br><br>'

file = open("2882.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2882"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2882"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2324"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2324_detail.html">每日財報</a><br><br>'

file = open("2324.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2324"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2324"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2515"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2515_detail.html">每日財報</a><br><br>'

file = open("2515.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2515"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2515"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2504"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2504_detail.html">每日財報</a><br><br>'

file = open("2504.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2504"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2504"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2393"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2393_detail.html">每日財報</a><br><br>'

file = open("2393.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2393"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2393"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2367"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2367_detail.html">每日財報</a><br><br>'

file = open("2367.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2367"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2367"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2330"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2330_detail.html">每日財報</a><br><br>'

file = open("2330.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2330"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2330"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2105"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2105_detail.html">每日財報</a><br><br>'

file = open("2105.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2105"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2105"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2409"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2409_detail.html">每日財報</a><br><br>'

file = open("2409.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2409"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2409"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2884"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2884_detail.html">每日財報</a><br><br>'

file = open("2884.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2884"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2884"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=3706"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/3706_detail.html">每日財報</a><br><br>'

file = open("3706.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=3706"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=3706"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=6005"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/6005_detail.html">每日財報</a><br><br>'

file = open("6005.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=6005"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=6005"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=5469"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/5469_detail.html">每日財報</a><br><br>'

file = open("5469.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=5469"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=5469"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2886"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2886_detail.html">每日財報</a><br><br>'

file = open("2886.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2886"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2886"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=3231"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/3231_detail.html">每日財報</a><br><br>'

file = open("3231.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=3231"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=3231"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=6269"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/6269_detail.html">每日財報</a><br><br>'

file = open("6269.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=6269"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=6269"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=1464"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/1464_detail.html">每日財報</a><br><br>'

file = open("1464.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=1464"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=1464"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2801"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2801_detail.html">每日財報</a><br><br>'

file = open("2801.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2801"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2801"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=4958"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/4958_detail.html">每日財報</a><br><br>'

file = open("4958.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=4958"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=4958"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2881"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2881_detail.html">每日財報</a><br><br>'

file = open("2881.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2881"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2881"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2316"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2316_detail.html">每日財報</a><br><br>'

file = open("2316.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2316"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2316"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2834"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2834_detail.html">每日財報</a><br><br>'

file = open("2834.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2834"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2834"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=6116"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/6116_detail.html">每日財報</a><br><br>'

file = open("6116.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=6116"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=6116"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2383"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2383_detail.html">每日財報</a><br><br>'

file = open("2383.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2383"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2383"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2885"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2885_detail.html">每日財報</a><br><br>'

file = open("2885.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2885"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2885"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2887"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2887_detail.html">每日財報</a><br><br>'

file = open("2887.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2887"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2887"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=1589"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/1589_detail.html">每日財報</a><br><br>'

file = open("1589.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=1589"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=1589"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2344"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2344_detail.html">每日財報</a><br><br>'

file = open("2344.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2344"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2344"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=8021"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/8021_detail.html">每日財報</a><br><br>'

file = open("8021.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=8021"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=8021"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2823"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2823_detail.html">每日財報</a><br><br>'

file = open("2823.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2823"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2823"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=3044"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/3044_detail.html">每日財報</a><br><br>'

file = open("3044.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=3044"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=3044"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=3036"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/3036_detail.html">每日財報</a><br><br>'

file = open("3036.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=3036"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=3036"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=9946"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/9946_detail.html">每日財報</a><br><br>'

file = open("9946.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=9946"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=9946"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2892"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/2892_detail.html">每日財報</a><br><br>'

file = open("2892.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=2892"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2892"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=3038"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/3038_detail.html">每日財報</a><br><br>'

file = open("3038.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=3038"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=3038"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=4968"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/4968_detail.html">每日財報</a><br><br>'

file = open("4968.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=4968"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=4968"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=3682"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
	
btn='<a href="http://210.240.163.81/data/day/3682_detail.html">每日財報</a><br><br>'

file = open("3682.html", 'w', encoding='UTF-8')
file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/EquityDistributionCatHis.asp?STOCK_ID=3682"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)

import urllib.request as req
url="https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=3682"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div

item1_string = str(item1)
file.write(item1_string)
file.close()