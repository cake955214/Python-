import urllib
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


url = 'http://jow.win168.com.tw/z/zm/zmd/zmdc.djhtm'
html_table = urllib.request.urlopen(url).read()

import bs4

htmlutf8_1 = '<head> <meta charset="utf-8"></head>'
htmlutf8_2 = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tocas-ui/2.3.3/tocas.css"><script src="https://cdnjs.cloudflare.com/ajax/libs/tocas-ui/2.3.3/tocas.js"></script><title>五十大交易量股票</title><style type="text/css">body{padding: 70px 0;}</style>'
htmlutf8_3 = '<div class="ts top fixed inverted borderless large menu"><div class="ts narrow container"><div class="header item">爬蟲股市</div><a href="http://210.240.163.81/data/stock.html" class="item">首頁</a><a href="http://210.240.163.81/data/news.html" class="item">新聞</a><a href="http://210.240.163.81/data/msci.html" class="item">MSCI成分股</a></div></div>'
htmlutf8_4 = '<style>table {margin-left:auto;margin-right:auto;border: 3.5px #FFD382 dashed;border-collapse:collapse;}th, td{border: 3px #FFD382 dashed;padding: px;}a{color: black;text-decoration:none;}</style>'

root = bs4.BeautifulSoup(html_table,"lxml")
item = root.find_all("table", class_="t01")

file = open("msci.html", 'w', encoding='UTF-8')
x = str(item)
x = x[1:]
x = x[:-1]

file.write(htmlutf8_1)
file.write(htmlutf8_2)
file.write(htmlutf8_3)
file.write(htmlutf8_4)
file.write(x)
