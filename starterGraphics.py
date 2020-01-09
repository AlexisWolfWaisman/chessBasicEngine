from piecesMovement import *
from tabulate import  tabulate
from board import *


def mark(positions):
    table = []
    for col in range(1,edgeLong+1):
        row = [col] + ["█"   if (x,col) in positions else " " for x in range(1,edgeLong+1) ]
        table.append(row)
    return table


def basicBoard(table):
    print(tabulate(table,headers=X_axis,tablefmt="fancy_grid"))



basicBoard(mark(queen_movement((3,3))))




