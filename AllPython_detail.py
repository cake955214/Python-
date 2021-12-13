import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2313&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2313.html">每月財報</a><br><br>'
file = open("2313_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2317&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2317.html">每月財報</a><br><br>'
file = open("2317_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=3037&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/3037.html">每月財報</a><br><br>'
file = open("3037_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=3481&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/3481.html">每月財報</a><br><br>'
file = open("3481_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2888&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2888.html">每月財報</a><br><br>'
file = open("2888_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2891&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2891.html">每月財報</a><br><br>'
file = open("2891_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2449&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2449.html">每月財報</a><br><br>'
file = open("2449_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2303&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2303.html">每月財報</a><br><br>'
file = open("2303_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2448&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2448.html">每月財報</a><br><br>'
file = open("2448_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=8150&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/8150.html">每月財報</a><br><br>'
file = open("8150_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=4938&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/4938.html">每月財報</a><br><br>'
file = open("4938_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2883&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2883.html">每月財報</a><br><br>'
file = open("2883_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2337&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2337.html">每月財報</a><br><br>'
file = open("2337_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2882&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2882.html">每月財報</a><br><br>'
file = open("2882_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2324&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2324.html">每月財報</a><br><br>'
file = open("2324_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2515&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2515.html">每月財報</a><br><br>'
file = open("2515_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2504&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2504.html">每月財報</a><br><br>'
file = open("2504_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2393&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2393.html">每月財報</a><br><br>'
file = open("2393_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2367&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2367.html">每月財報</a><br><br>'
file = open("2367_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2330&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2330.html">每月財報</a><br><br>'
file = open("2330_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2105&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2105.html">每月財報</a><br><br>'
file = open("2105_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2409&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2409.html">每月財報</a><br><br>'
file = open("2409_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2884&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2884.html">每月財報</a><br><br>'
file = open("2884_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=3706&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/3706.html">每月財報</a><br><br>'
file = open("3706_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=6005&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/6005.html">每月財報</a><br><br>'
file = open("6005_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=5469&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/5469.html">每月財報</a><br><br>'
file = open("5469_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2886&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2886.html">每月財報</a><br><br>'
file = open("2886_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=3231&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/3231.html">每月財報</a><br><br>'
file = open("3231_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=6269&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/6269.html">每月財報</a><br><br>'
file = open("6269_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=1464&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/1464.html">每月財報</a><br><br>'
file = open("1464_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2801&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2801.html">每月財報</a><br><br>'
file = open("2801_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=4958&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/4958.html">每月財報</a><br><br>'
file = open("4958_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2881&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2881.html">每月財報</a><br><br>'
file = open("2881_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2316&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2316.html">每月財報</a><br><br>'
file = open("2316_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2834&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2834.html">每月財報</a><br><br>'
file = open("2834_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=6116&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/6116.html">每月財報</a><br><br>'
file = open("6116_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2383&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2383.html">每月財報</a><br><br>'
file = open("2383_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2885&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2885.html">每月財報</a><br><br>'
file = open("2885_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2887&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2887.html">每月財報</a><br><br>'
file = open("2887_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=1589&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/1589.html">每月財報</a><br><br>'
file = open("1589_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2344&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2344.html">每月財報</a><br><br>'
file = open("2344_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=8021&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/8021.html">每月財報</a><br><br>'
file = open("8021_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2823&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2823.html">每月財報</a><br><br>'
file = open("2823_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=3044&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/3044.html">每月財報</a><br><br>'
file = open("3044_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=3036&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/3036.html">每月財報</a><br><br>'
file = open("3036_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=9946&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/9946.html">每月財報</a><br><br>'
file = open("9946_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=2892&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/2892.html">每月財報</a><br><br>'
file = open("2892_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=3038&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/3038.html">每月財報</a><br><br>'
file = open("3038_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=4968&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/4968.html">每月財報</a><br><br>'
file = open("4968_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

import urllib.request as req
url="https://goodinfo.tw/StockInfo/ShowK_ChartCompare.asp?STOCK_ID=3682&STOCK_ID2=&CHT_CAT2=DATE"
request=req.Request( url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

htmlutf8='<head>  <meta charset="utf-8"></head>'
btn='<a href="http://210.240.163.81/data/month/3682.html">每月財報</a><br><br>'
file = open("3682_detail.html", 'w', encoding='UTF-8')

file.write(htmlutf8)
file.write(btn)

root=bs4.BeautifulSoup(data,"html.parser")

item1=root.find("div",id='divDetail') #div


item1_string = str(item1)

file.write(item1_string)
file.close()

