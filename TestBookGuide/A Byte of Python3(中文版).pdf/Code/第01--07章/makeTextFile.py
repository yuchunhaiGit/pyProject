#window
# 'makeTextFile.py -- create text file'

import os
ls = os.linesep

#get filename
fname = raw_input('Enter file road:')
while True:
    if os.path.exists(fname):
        print "Error: %s' already exits" % (fname)
        fname = raw_input()
    else:
        break
        
#get file content (text) lines
all = []
print "\nEnter lines('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry =='.':
        break
    else:
        all.append(entry)
        
#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' %(x,ls) for x in all])
fobj.close()
print 'done!\nPress Enter to continue!'
raw_input()

    
