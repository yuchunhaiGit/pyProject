#!/usr/bin/python
# Filename: func_local.py
x = 50
def func(x):
    print('x is', x)
    x = x + 1
    print('Changed local x to', x)
func(x)
print('x is still', x)
input()
