__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
print(bsObj)