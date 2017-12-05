# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-13:50
#@文件名称:pyProject-linux查找域名对应的nginx配置
import paramiko
docName = 'bqwebgame.domegame.cn'
# docName = 'bq.passport.cn'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.69.232',22,username='root',password='bqceshi',timeout=4)
stdin,stdout,stderr = client.exec_command("cd /opt/nginx/conf;pwd;grep -r "+docName,get_pty=True)
print(stdout.readlines())