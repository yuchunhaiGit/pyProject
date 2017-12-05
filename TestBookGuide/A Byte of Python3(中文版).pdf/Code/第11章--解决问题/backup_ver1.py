#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['C:\\tmp', 'C:\\temp']
running = True
while running:
    your_source=input("Your own path or your own file path:")
    source.append(your_source)
    if input("Do you want to add file or folder(y/n):")=='n\r':
        running = False
# Notice we had to use double quotes inside the string for names with spaces in it.

# 2. The backup must be stored in a main backup directory
target_dir = 'C:\\backup\\log' # Remember to change this to what you will be using

# 3. The files are backed up into a rar file.

# 4. The name of the rar archive is the current date and time
target = target_dir+\
         time.strftime('%Y')+'年'+\
         time.strftime('%m')+'月'+\
         time.strftime('%d')+'日_'+\
         time.strftime('%H')+'时'+\
         time.strftime('%M')+'分'+\
         time.strftime('%S')+'秒'+\
         '.rar'

# 5. We use the rar command to put the files in a rar archive
zip_command = "rar a {0} {1}".format(target,' '.join(source))

# Run the backup
# 通过给系统传递参数来执行压缩命令（压缩使用的是WinRAR所带文件rar.exe来执行压缩）
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
input()
