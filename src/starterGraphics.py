from src.generalMovements import *
from tabulate import  tabulate
from src.board import *

UNICODE_PIECES = {
  'r': u'♜', 'n': u'♞', 'b': u'♝', 'q': u'♛',
  'k': u'♚', 'p': u'♟', 'R': u'♖', 'N': u'♘',
  'B': u'♗', 'Q': u'♕', 'K': u'♔', 'P': u'♙',
  None: ' '
}

def mark(positions):
    table = []
    for col in range(1,edgeLong+1):
        row = [col] + ["█"   if (x,col) in positions else " " for x in range(1,edgeLong+1) ]
        table.append(row)
    return table

def setPiecePos(piece,positions):
    pass

def basicBoard(table):
    print(tabulate(table,headers=X_axis,tablefmt="fancy_grid"))



basicBoard(mark(negative_pawn_movement((3,2))))




