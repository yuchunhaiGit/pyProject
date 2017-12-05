# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-14:15
#@文件名称:pyProject-232环境elasticsearch服务状态
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.69.232',22,username='root',password='bqceshi',timeout=4)
stdin,stdout,stderr = client.exec_command("whereis elasticsearch")
print(stdout.readlines())
stdin,stdout,stderr = client.exec_command("/etc/init.d/elasticsearch status")
print(stdout.readlines())
# stdin,stdout,stderr = client.exec_command("/etc/init.d/elasticsearch stop")
# print(stdout.readlines())
# stdin,stdout,stderr = client.exec_command("/etc/init.d/elasticsearch status")
# print(stdout.readlines())
# stdin,stdout,stderr = client.exec_command("/etc/init.d/elasticsearch start")
# print(stdout.readlines())
# stdin,stdout,stderr = client.exec_command("/etc/init.d/elasticsearch status")
# print(stdout.readlines())
client.close()
