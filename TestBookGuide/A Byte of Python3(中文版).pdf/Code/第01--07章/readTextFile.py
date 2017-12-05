#windows
'readTextFile.py -- read and display text file'

#get filename
fname = raw_input("Enter filename:")
print

#attempt to open file for reading
try:
    fobj = open(fname,'r')
except IOError, e:
    print "*** file open error:", e
#display contents to the screen
for eachLine in fobj:
    print eachLine,
fobj.close()
print
raw_input("Press Enter to Continue !")
