# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/1-10:52
#@文件名称:pyProject-礼包管理
from selenium import webdriver
import time
url = "http://storeba.domestore.cn/#/web-game-platform/gift-list"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
browser.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div[1]/div/div[5]/button').click()

time.sleep(5)
browser.quit()