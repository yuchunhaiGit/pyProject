'''
Created on 2017年9月21日
 
@author: yuchunhai
'''
allGuests = {}
# yu = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

while True:
    print('请手动输入id：')
    id = input()
    if id == '':
        break
    if id in allGuests:
        print("已经存在,程序停止运行")
        break
    if id not in allGuests:
        print('请手动输入yu：')
        yu = input()
        yuNew = {id:yu}
        allGuests.update(yuNew)
        print(allGuests)
        def totalBrought(guests, item):
            numBrought = 0
            for k, v in guests.items():
                numBrought = numBrought + v.get(item, 0)
            return numBrought
        print('Number of things being brought:')
        print(' - Apples ' + str(totalBrought(allGuests, 'rope')))
        print(' - Cups ' + str(totalBrought(allGuests, 'torch')))
        print(' - Cakes ' + str(totalBrought(allGuests, 'gold coin')))
        print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'dagger')))
        print(' - Apple Pies ' + str(totalBrought(allGuests, 'arrow')))

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#              'Bob': {'ham sandwiches': 3, 'apples': 2},
#              'Carol': {'cups': 3, 'apple pies': 1}}
# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought
# # yu = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# print('Number of things being brought:')
# print(' - Apples ' + str(totalBrought(allGuests, 'rope')))
# print(' - Cups ' + str(totalBrought(allGuests, 'torch')))
# print(' - Cakes ' + str(totalBrought(allGuests, 'gold coin')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'dagger')))
# print(' - Apple Pies ' + str(totalBrought(allGuests, 'arrow')))