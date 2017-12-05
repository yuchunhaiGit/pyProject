__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib import urlopen
import time

def sendMail(subject, content):
    msg_from = '18905255025@126.com'
    #发送方邮箱
    passwd = 'yuchunhai1989'
    #填入发送方邮箱的授权码
    msg_to = 'yutest@126.com'
    #收件人邮箱

    subject = "python邮件测试"
    #主题
    content = "这是我使用python smtplib及email模块发送的邮件"
    #正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.126.com", 465)
        #邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print "发送成功"
    except s.SMTPException,e:
        print "发送失败"
    finally:
        s.quit()

bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"))
while (bsObj.find("a", {"id": "answer"}).attrs['title'] == "NO"):
    print("It is not Christmas yet.")
    time.sleep(3600)
# bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"))
# sendMail("It's Christmas!", "According to http://itischristmas.com, it is Christmas!")