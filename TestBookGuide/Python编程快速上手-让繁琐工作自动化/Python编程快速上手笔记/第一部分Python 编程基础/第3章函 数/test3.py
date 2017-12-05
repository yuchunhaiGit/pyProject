'''
Created on 2017年9月21日
 
@author: yuchunhai
'''
print("请输入正整数:")
try:
    number = int(input())
except:
    print('你输入有错位，请输入正整数')
print(number)
  
def collatz():
    if (number % 2 == 0):
        print(number//2)
    if (number % 2 == 1):
        print(3*number+1)
collatz()

# print(type(int(number)))
# print(type(number))
# print(type(int()))
# 
# while True:
#     try:
#         number = int(input())
#     except:
#         print('你输入有错位，请输入正整数')
#     if type(int()) != type(number):
#         print('你输入有错位，请输入正整数')
#         number = input()
#         continue
#     else:
#         print(number)
#         break



# print("请输入正整数:")
# try:
#     number = int(input())
# except:
#     print('你输入有错位，请输入正整数')

# def collatz():
#     if (number % 2 == 0):
#                 print(number//2)
#     if (number % 2 == 1):
#                 print(3*number+1)
# collatz()