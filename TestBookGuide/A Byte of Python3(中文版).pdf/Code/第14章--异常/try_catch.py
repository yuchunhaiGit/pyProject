# -*-- coding:UTF-8 --*-

#!/usr/bin/python
# Filename: try_except.py

try:
	text = input('Enter something --> ')
except EOFError:
	print('Why did you do an EOF on me?')
except KeyboardInterrupt:
	print('You cancelled the operation.')
else:
	print('You entered {0} 哈哈'.format(text))
	