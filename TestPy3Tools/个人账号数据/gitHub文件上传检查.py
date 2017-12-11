# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/5-11:11
#@文件名称:pyProject-gitHub文件上传检查
from selenium import webdriver
import time
url = "https://github.com/login"
name = '18905255025@qq.com'
pwd = 'yuchunhai1989'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
browser.find_element_by_xpath('//*[@id="login_field"]').clear()
browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(name)
browser.find_element_by_xpath('//*[@id="password"]').clear()
browser.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[3]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="your_repos"]/div/div[2]/ul/li/a/span/span').click()
time.sleep(2)
browser.refresh()
time.sleep(5)
# browser.quit()