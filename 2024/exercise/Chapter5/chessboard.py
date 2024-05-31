chessboard = {'1h': 'bking', '6c': 'wqueen', 
              '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

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
    for i in range(len(board)):
        print(board.keys())

isValidChessBoard(chessboard)
