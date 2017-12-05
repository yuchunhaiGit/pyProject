# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-14:00
#@文件名称:pyProject-232环境静态代码发布svn
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.69.232',22,username='root',password='bqceshi',timeout=4)
stdin,stdout,stderr = client.exec_command("cd /Data/WEB_APP/uc.domegame.cn/ROOT/passport/;svn update")
print(stdout.readlines())
client.close()