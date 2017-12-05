# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/1416:58
#@文件名称:刷新redis
# 意思就是execute_command() 他是a single session，每次执行完后都要回到缺省目录
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.69.232',22,username='root',password='bqceshi',timeout=4)
stdin,stdout,stderr = client.exec_command("cd /code_dir/gnsrc/store-admin/src;pwd;php artisan redis:reload --part=all",)
print(stdout.readlines())
client.close()

