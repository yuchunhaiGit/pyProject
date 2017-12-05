__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
import csv
from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html)
# ���Աȱ���ǵ�ǰҳ���ϵĵ�һ�����
table = bsObj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

# csvFile = open("C:/Users/yuchunhai/Desktop/yutestpython2/python/files/editors.csv", 'wt', newline="", encoding='utf-8')
csvFile = open("C:/Users/yuchunhai/Desktop/yutestpython2/python/files/editors.csv", 'wt',encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()