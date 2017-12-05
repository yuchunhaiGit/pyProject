'''
Created on 2017年9月21日
 
@author: yuchunhai
'''

yu = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
yu1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print(yu.items())
    
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_totalv + v
    print("Total number of items: " + str(item_total))

displayInventory(yu)