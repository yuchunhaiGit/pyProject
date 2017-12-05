# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/1522:26
#@文件名称:testMysql
import pymysql
db = pymysql.connect("my5670373.xincache1.cn","my5670373","yuchunhai1989","my5670373")
cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
sql = "SELECT * FROM my5670373.zbp_member; > '%d'"%(1000)
cursor.execute(sql)
results = cursor.fetchall()
print(results)