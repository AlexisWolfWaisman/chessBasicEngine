# Dependencies
from .board import *
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# math functions
from numpy import array as NParray, sign
from scipy.spatial.distance import euclidean as computeDistance
from itertools import product as cartessianProd
from math import fabs, floor


def validatePos(position):
  if isinstance(position,str):
    if not(len(position) == 2):
      raise NameError("the length of the word is not fitted")
    if not(position[0].isalpha()):
      raise NameError("the first character is not a letter")
    elif position[0].lower() not in X_axis:
      raise NameError("the first character ( %s ) doesn't belong  to the X-axis"%position[0])
    if not(position[1].isdigit()):
      raise NameError("the second character is not a digit")
    elif int(position[1]) not in Y_axis:
      raise NameError("the second character ( %s ) doesn't belong  to the Y-axis"%position[1])
    return True
# theese functions provides the structure to solve another movements.
distanced_asterisk_movement = lambda initialPos,distance : [x for x in asterisk_movement(initialPos) if floor(computeDistance(x,initialPos)) <= int(distance) ]
square_movement = lambda initialPos,distance: [ x for x in cartessianProd(range(initialPos[0]-distance,initialPos[0]+distance+1),range(initialPos[1]-distance,initialPos[1]+distance+1)) if x!= initialPos ]
spider_movement = lambda initialPos,distance: [x for x in set(square_movement(initialPos,distance)).intersection(set(distanced_asterisk_movement(initialPos,distance)))]
spot_movement = lambda initialPos,distance:  set(spider_movement(initialPos,distance)) - set(map(tuple,NParray(initialPos) + list(cartessianProd((2,-2),repeat=2))))
triangle_movement = lambda initialPos,distance,direction: [x for x in spot_movement(initialPos,distance) if sign(x[1]-initialPos[1])==sign(direction) ]
decodedPosition = lambda  position : (X_axis.index(position[0])+1 , int(position[1]) )
encodePosition = lambda  position : "%s%s"%(X_axis[position[0]-1] , int(position[1]) )
checkBoardConsistent = lambda position: [x for x in board if x != position]
# in all cases we keep in mind that the inital position is not included inside movement posibilities
cross_movement = lambda initialPos : list(set(checkBoardConsistent(initialPos)).intersection(set([x for x in board if x[0]==initialPos[0] or x[1] == initialPos[1] ] )))
X_movement = lambda initialPos :  list(set(checkBoardConsistent(initialPos)).intersection(set([x for x in board if fabs(initialPos[0] - x[0] ) == fabs(initialPos[1] - x[1]) ])))
# queen is the fusion between rook and bishop
asterisk_movement = lambda initialPos : cross_movement(initialPos) + X_movement(initialPos)
# The knigth (easy way to understand) is the opposite movement to queen in a small board (3x3) ; you can perform a knigth movement, just setting it in the squares where the queen can't reach.
# in our context, simply: substract to the square th asterisk.
counterAsterisk_movement = lambda initialPos : [x for x in board if x in (set(square_movement(initialPos,2)) - set(asterisk_movement(initialPos,2)))  ]
# the pawn movement includes attacks; only in the correspondent row at game start you can move more than 1  square.
positive_oneStepTriangle_movement = lambda initialPos: triangle_movement(initialPos,2,1) if initialPos[1] == Y_axis[1] else triangle_movement(initialPos,1,1)
negative_oneStepTriangle_movement = lambda initialPos: triangle_movement(initialPos,2,-1) if initialPos[1] == Y_axis[edgeLong-1] else triangle_movement(initialPos,1,-1)
# the king is easy , just an asterisk of 1 square distance.
oneStepAsterisk_movement = lambda initialPos: distanced_asterisk_movement(initialPos,1)