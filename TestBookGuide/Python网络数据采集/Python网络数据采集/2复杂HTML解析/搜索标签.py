__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
from urllib import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
#显示具体标签信息
nameList = bsObj.find_all("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
#显示含有标签的数量
nameList1 = bsObj.find_all(text="the prince")
print(len(nameList1))