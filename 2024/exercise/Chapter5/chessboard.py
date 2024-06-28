chessboard = {'1h': 'bking', '6c': 'wqueen', 
              '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '8z':'bking'}

move = []
letter = ['a','b','c','d','e','f','g','h']
for i in range(1,9):
    for x in range(len(letter)):
        move.append(str(i) + letter[x])

piece = []
color = ['b','w']
name = ['king','queen','bishop','rook','knight','pawn']
for i in range(len(color)):
    for x in range(len(name)):
        piece.append(color[i] + name[x])


#TODO: use piece and move to check if the dictionary have a valid piece and moves
def isValidChessBoard(board):
    for chessmove in board: # check if the move is a valid chess move
        if chessmove not in move:
            print(chessmove + " is not a valid chess move")
        elif board[chessmove] not in piece:
            print(board[chessmove] + ' is not a chess piece')
    # return False
        
print(isValidChessBoard(chessboard))
