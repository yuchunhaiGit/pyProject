__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
from urllib import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())
# ��ȡҳ�������������б�
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # �ҳ�������"/"��ͷ������
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# ��ȡҳ�������������б�
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # �ҳ�������"http"��"www"��ͷ�Ҳ�������ǰURL������
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        # return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
        return getExternalLinks(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("��������ǣ�" + externalLink)
    followExternalOnly(externalLink)

# followExternalOnly("http://oreilly.com")
followExternalOnly("https://www.baidu.com")