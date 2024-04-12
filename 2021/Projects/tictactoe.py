#complete this tictactoe program add a function that checks whether a player won the game:

theboard= {'top-L': ' ','top-M': ' ','top-R': ' ',
           'mid-L': ' ','mid-M': ' ','mid-R': ' ',
           'low-L': ' ','low-M': ' ','low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
    printBoard(theboard)
    print('Turn for ' + turn + '. Move on which space? e.g. top-L,mid-M or low-R')
    move = input()
    theboard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theboard)