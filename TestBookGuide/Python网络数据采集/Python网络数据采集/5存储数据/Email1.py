# __author__ = 'yuchunhai'
# -*-coding:utf-8-*-
# import smtplib
# from email.mime.text import MIMEText
# msg = MIMEText("The body of the email is here")
# msg['Subject'] = "An Email Alert"
# msg['From'] = "yutest@qq.com"
# msg['To'] = "yutest@qq.com"
# s = smtplib.SMTP('localhost')
# s.send_message(msg)
# s.quit()
import pymysql
import smtplib
from email.mime.text import MIMEText

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

# yutest@126.com/18905255025@126.com/yuchunhai1989