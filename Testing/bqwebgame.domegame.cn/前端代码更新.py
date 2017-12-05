# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/229:20
#@文件名称:前端代码更新
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.69.232',22,username='root',password='bqceshi',timeout=4)
stdin,stdout,stderr = client.exec_command(r"cd /code_dir/gnsrc/newwebgame-php/trunk/webgame;svn update")
print(stdout.readlines())
stdin,stdout,stderr = client.exec_command(r"cd /code_dir/gnsrc/newwebgame-php/trunk/webgame;pwd;cnpm run prod",get_pty=True)
print(stdout.readlines())
client.close()