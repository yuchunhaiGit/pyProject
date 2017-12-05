'''
Created on 2017年9月21日
 
@author: yuchunhai
'''
# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
# 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
theBoard = {'top-L': 'A', 'top-M': 'B', 'top-R': 'C', 'mid-L': 'D', 'mid-M':
'E', 'mid-R': 'F', 'low-L': 'G', 'low-M': 'H', 'low-R': 'I'}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)