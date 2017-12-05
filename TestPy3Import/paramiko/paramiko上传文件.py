# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/228:37
#@文件名称:paramiko上传文件
import paramiko
t = paramiko.Transport(('192.168.69.232',22))
t.connect(username='root',password='bqceshi')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(r'D:/yutest/login.vue','/opt/yutest/login.vue')
t.close()