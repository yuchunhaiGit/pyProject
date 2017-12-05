__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
from urllib import urlretrieve
from urllib import urlopen
from bs4 import BeautifulSoup
import os

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        # print(getDownloadPath(baseUrl,absoluteUrl, downloadDirectory))
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
        print(getDownloadPath(baseUrl, fileUrl, downloadDirectory))