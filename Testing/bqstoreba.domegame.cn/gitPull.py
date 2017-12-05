# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/2215:57
#@文件名称:gitPull
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.69.232',22,username='root',password='bqceshi',timeout=4)
stdin,stdout,stderr = client.exec_command(r"cd /code_dir/gnsrc/store-admin/src/;pwd;git pull;git log -p -1",get_pty=True)
print(stdout.readlines())
client.close()