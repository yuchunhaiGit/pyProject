# # coding=utf-8
# # @作者:yuchunhai
# #@Time:2017/12/7-9:48
# #@文件名称:pyProject-获取下载连接1源码
# # -*- coding=utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,WebDriverException,TimeoutException
# import xlwt
# #左侧目录的xpath
# catalogue_list = ['//*[@id="accordion"]/div[1]/div[1]/h4/a',
#                   '//*[@id="accordion"]/div[2]/div[1]/h4/a',
#                   '//*[@id="accordion"]/div[3]/div[1]/h4/a',
#                   '//*[@id="accordion"]/div[4]/div[1]/h4/a',
#                   '//*[@id="accordion"]/div[5]/div[1]/h4/a',
#                   '//*[@id="accordion"]/div[6]/div[1]/h4/a',
#                   '//*[@id="accordion"]/div[7]/div[1]/h4/a',
#                   '//*[@id="accordion"]/div[8]/div[1]/h4/a'
#                   ]
# catalogue_name = [u'企业解决方案',
#                   u'MSDN技术资源库',
#                   u'工具和资源',
#                   u'应用程序',
#                   u'开发人员工具',
#                   u'操作系统',
#                   u'服务器',
#                   u'设计人员工具'
#                   ]
#
# count = 0
# software_name_list = []
# software_url_list = []
#
#
# def builddriver(kind):
#     chromedriver_path = 'D:\\WebDrivers\\chromedriver_win32\\chromedriver.exe'
#     phantomjs_path = 'D:\\WebDrivers\\phantomjs\\bin\\phantomjs.exe'
#     if kind == 'Chrome':
#         driver = webdriver.Chrome(executable_path=chromedriver_path)
#     elif kind == 'Phantomjs':
#         driver = webdriver.PhantomJS(executable_path=phantomjs_path)
#     return driver
#
# #关闭弹出的捐款对话框
# def clickdialog():
#     global driver
#     try:
#         dialog_close_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
#         if dialog_close_button:
#             dialog_close_button.click()
#             time.sleep(3)
#     except NoSuchElementException:
#         pass
#     except ElementNotVisibleException:
#         pass
#
# #通过该函数调用所有的点击功能，防止对话框干扰
# def click_when_dialog(target_item):
#     try:
#         target_item.click()
#     except WebDriverException:
#         clickdialog()
#         target_item.click()
#     except NoSuchElementException, e:
#         raise e
#     except TimeoutException:
#         time.sleep(2)
#         target_item.click()
#     # 处理某灵异bug……
#     except WebDriverException:
#         time.sleep(2)
#         target_item.click()
#     finally:
#         time.sleep(4)
#
#
# def get_one_kind_software(kind_name_selector, type_name):
#     global software_name_list, software_url_list
#     software_file = open(type_name + '.txt', 'w')
#     kind_name = driver.find_element_by_xpath(kind_name_selector)
#     click_when_dialog(kind_name)
#     kind_id = kind_name.get_attribute('data-target')[1:]
#     software_item = driver.find_elements_by_xpath('//*[@id="' + kind_id + '"]/div/ul/li')  # 目录下的软件列表项
#     # 顺序点击每个目录项
#     for i in range(0, len(software_item)):
#         click_when_dialog(software_item[i])
#         # 获取右侧数据
#         # 多语言：
#         # 获取多语言列表
#         multi_languate_list = driver.find_elements_by_xpath('//*[@id="view_data_container"]/ul/li/a')
#         if multi_languate_list:
#             for j in range(0, len(multi_languate_list) - 1):
#                 software_id = 'lang_' + multi_languate_list[j].get_attribute('data-id')
#                 try:
#                     click_when_dialog(multi_languate_list[j])
#                 except NoSuchElementException:
#                     continue
#                 # 获取具体内容
#                 try:
#                     software_name = driver.find_element_by_xpath('//*[@id="' + software_id + '"]/ul/li/div/label').text
#                     software_url = driver.find_element_by_xpath(
#                         '//*[@id="' + software_id + '"]/ul/li/div/label/input').get_attribute('data-url')
#                 except NoSuchElementException:
#                     # 可能未加载完，但实际有
#                     time.sleep(4)
#                     try:
#                         software_name = driver.find_element_by_xpath(
#                             '//*[@id="' + software_id + '"]/ul/li/div/label').text
#                         software_url = driver.find_element_by_xpath(
#                             '//*[@id="' + software_id + '"]/ul/li/div/label/input').get_attribute('data-url')
#                     # 这个真没有……
#                     except NoSuchElementException:
#                         continue
#                 software_name_list.append(software_name)
#                 software_url_list.append(software_url)
#     for i in range(0, len(software_name_list)):
#         software_file.write(software_name_list[i] + '    ' + software_url_list[i] + '\n')
#     print type_name + '已爬取完成。\n'
#     # 清空已写入至文件的列表
#     software_name_list = []
#     software_url_list = []
#     software_file.close()
#
#
# def file_to_excel():
#     global count
#     workbook = xlwt.Workbook()
#     sheet_list = []
#     for sheet_name in catalogue_name:
#         sheet = workbook.add_sheet(unicode(sheet_name), cell_overwrite_ok=True)
#         sheet_list.append(sheet)
#     # 依次打开文件并写入对应的sheet
#     for i in range(0, len(catalogue_name)):
#         count = 0
#         software_file = open(unicode(catalogue_name[i]) + '.txt', 'r')
#         for line in software_file:
#             sheet_list[i].write(count, 0, unicode(line.split('    ')[0]))
#             sheet_list[i].write(count, 1, unicode(line.split('    ')[1]))
#             count += 1
#         software_file.close()
#     print u'软件存储完成'
#     workbook.save('software.xls')
#
# driver = builddriver('Chrome')
# if __name__ == "__main__":
#     global driver
#     driver.get('http://msdn.itellyou.cn/')
#     time.sleep(5)
#     for k in range(0, len(catalogue_list)):
#         get_one_kind_software(catalogue_list[k], catalogue_name[k])
#     driver.close()
#     file_to_excel()
#
