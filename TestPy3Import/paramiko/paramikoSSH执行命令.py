# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/228:41
#@文件名称:paramikoSSH执行命令
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.69.232',22,username='root',password='bqceshi',timeout=4)
stdin,stdout,stderr = client.exec_command("cd /code_dir/gnsrc/store-admin/src;pwd;php artisan redis:reload --part=all",)
print(stdout.readlines())
client.close()
