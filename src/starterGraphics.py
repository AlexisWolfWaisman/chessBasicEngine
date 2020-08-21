# Dependencies
from .board import *
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from tabulate import  tabulate


UNICODE_PIECES = {
  'r': u'♜', 'n': u'♞', 'b': u'♝', 'q': u'♛',
  'k': u'♚', 'p': u'♟', 'R': u'♖', 'N': u'♘',
  'B': u'♗', 'Q': u'♕', 'K': u'♔', 'P': u'♙',
  None: ' '
}

# this goes first, because after locate all posible movements (including current position) we set the piece (graph)
def mark(positions):
    table = []
    for col in range(1,edgeLong+1):
        row = [col] + ["█"   if (x,col) in positions else " " for x in range(1,edgeLong+1) ]
        table.append(row)
    return table


def setPiecePos(piece,positions):
    table = mark(positions)


def basicBoard():
    table_aux = [[element] + board_row for element in Y_axis]
    return (tabulate(table_aux,headers=X_axis,tablefmt="fancy_grid"))