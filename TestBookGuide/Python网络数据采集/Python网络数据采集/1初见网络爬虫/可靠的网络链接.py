__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
# title = getTitle("http://www.pythonscraping.com/pages/page1.html")
# title = getTitle("http://www.yuntalk.com.cn/ZBlog/")
title = getTitle("http://www.yuntalk.cn")

if title == None:
    print("not found")
else:
    print(title)