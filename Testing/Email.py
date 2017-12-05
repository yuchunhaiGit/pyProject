# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/1523:08
#@文件名称:Email
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = '18601675016@163.com'
receiver = '18601675016@163.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '18601675016@163.com'
password = 'yuchunhai1989'
msg = MIMEText('你好','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()