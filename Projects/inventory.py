#inventoryitems = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory: ')
    totalnumber = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalnumber = totalnumber + v
    
    print('Total number of items: ' + str(totalnumber))


def addToInventory(inventory, addItems):
    for v in range(len(addItems)):
        inventory.setdefault(addItems[v], 0)
        inventory[addItems[v]] = inventory[addItems[v]] + 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)