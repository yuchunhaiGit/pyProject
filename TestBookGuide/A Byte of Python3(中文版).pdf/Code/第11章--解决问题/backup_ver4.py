
import time
import zipfile
import os


source = ['.\\tmp\\mylog.txt',
          '.\\tmp\\pic1.jpg',
          '.\\tmp\\pic2.jpg',
          '.\\tmp\\temp.txt',
          '.\\tmp\\song.wma'
          ]                  #files you want to archive
target_dir = '.\\backup'

today = target_dir+os.sep+time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

##comment = input('Enter a comment --> ')
##if len(comment) == 0: # check if a comment was entered
##    target = today + os.sep + now +'.zip'
##else:
##    target = today + os.sep + now + '_'+ comment.replace(' ', '_') + '.zip'
target = today + os.sep + now +'.zip'

if not os.path.exists(today):
    os.mkdir(today) # make directory
    print('Successfully created directory', today)


for i in range(0,len(source)):
    with zipfile.ZipFile(target,'a') as myzip:
        myzip.write(source[i])
        
print('Successful backup to', target)

input('Press Enter to continue!')
