# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/228:38
#@文件名称:paramiko下载文件
import paramiko
t = paramiko.Transport(('192.168.69.232',22))
t.connect(username='root',password='bqceshi')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get(r'/opt/yu/1.txt','D:/yutest/1.txt')
t.close()
