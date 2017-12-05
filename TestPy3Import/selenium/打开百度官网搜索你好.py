# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-11:36
#@文件名称:pyProject-打开百度官网搜索你好
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.baidu.com')
browser.find_element_by_xpath('//*[@id="kw"]').clear()
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('你好')
browser.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(2)
browser.quit()
