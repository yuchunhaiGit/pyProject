__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

# class TestWikipedia(unittest.TestCase):
class TestWiki(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        # ����������ǰ100��ҳ��
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print("Done!")
    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/") + 6):]
        urlTitle = urlTitle.replace("_", " ")
        urlTitle = urllib.unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        if content is not None:
            return True
        return False

    # def getNextLink(self):
    #     #ʹ�õ�5�½��ܵķ��������������
if __name__ == '__main__':
    unittest.main()