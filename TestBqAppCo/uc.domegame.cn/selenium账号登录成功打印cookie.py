# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-14:30
#@文件名称:pyProject-selenium账号登录成功打印cookie
from selenium import webdriver
import time
url = "http://uc.domegame.cn"
name = '18601675016'
pwd = '111111'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div[1]/input').clear()
browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div[1]/input').send_keys(name)
browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div[3]/input').clear()
browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div[3]/input').send_keys(pwd)
browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div[6]/a').click()
time.sleep(5)
#用户昵称
print(browser.get_cookies()[1]['value'])
browser.quit()