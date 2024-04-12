tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    
    colswidth = [0] * len(tableData)
    
    for i in range(len(colswidth)):
        for y in range(len(tableData[i])):
            if colswidth[i] < len(tableData[i][y]):
                colswidth[i] = len(tableData[i][y])
    
    for i in range(4):
        for y in range(len(colswidth)):
                print(tableData[y][i].rjust(colswidth[y]), end=' ')
        print()

printTable()