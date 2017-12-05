#!/usr/bin/python
# Filename: backup_ver2.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
# 要备份的文件或目录
source = ['"C:\\tmp"', 'C:\\temp']
# Notice we had to use double quotes inside the string for names with spaces in it.
# 当要备份的文件的目录名中有空格时，要用如'"C:\\program files"'形式的表示方法。

# 2. The backup must be stored in a main backup directory
# 存放备份文件的目录名
target_dir = 'C:\\Backup' # Remember to change this to what you will be using

# 3. The files are backed up into a rar file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the rar archive
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print('Successfully created directory', today)
else:
    print('{0} directory already exists'.format(today))
# The name of the zip file
target = today + os.sep + now + '.rar'

# 5. We use the zip command to put the files in a zip archive
zip_command = "rar a {0} {1}".format(target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup Failed')

input('Press Enter to continue!')
