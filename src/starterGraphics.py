from tabulate import  tabulate
from src.pieces import *

UNICODE_PIECES = {
  'r': u'♜', 'n': u'♞', 'b': u'♝', 'q': u'♛',
  'k': u'♚', 'p': u'♟', 'R': u'♖', 'N': u'♘',
  'B': u'♗', 'Q': u'♕', 'K': u'♔', 'P': u'♙',
  None: ' '
}

def basicBoard(table):
    return (tabulate(table,headers=X_axis,tablefmt="fancy_grid"))


def mark(positions):
    table = []
    for col in range(1,edgeLong+1):
        row = [col] + ["█"   if (x,col) in positions else " " for x in range(1,edgeLong+1) ]
        table.append(row)
    return table

def setPiecePos(piece,positions):
    pass
