__author__ = 'yuchunhai'
# -*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib import urlopen
import time

def sendMail(subject, content):
    msg_from = '18905255025@126.com'
    #���ͷ�����
    passwd = 'yuchunhai1989'
    #���뷢�ͷ��������Ȩ��
    msg_to = 'yutest@126.com'
    #�ռ�������

    subject = "python�ʼ�����"
    #����
    content = "������ʹ��python smtplib��emailģ�鷢�͵��ʼ�"
    #����
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.126.com", 465)
        #�ʼ����������˿ں�
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print "���ͳɹ�"
    except s.SMTPException,e:
        print "����ʧ��"
    finally:
        s.quit()

bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"))
while (bsObj.find("a", {"id": "answer"}).attrs['title'] == "NO"):
    print("It is not Christmas yet.")
    time.sleep(3600)
# bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"))
# sendMail("It's Christmas!", "According to http://itischristmas.com, it is Christmas!")