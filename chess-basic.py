from numpy import prod as multiplicatoria
from numpy import sum as sumatoria 
from scipy.spatial.distance import euclidean as computeDistance
from itertools import product as prodCartesiano
from itertools import permutations
from string import ascii_lowercase as abecedario
from math import fabs
from math import floor

edgeLong = 8
board = list(prodCartesiano(range(1,edgeLong+1),range(1,edgeLong+1)))
X_axis = list(abecedario[:edgeLong])
Y_axis = list(range(1,edgeLong+1))


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

decodedPosition = lambda  position : (X_axis.index(position[0])+1 , int(position[1]) )
encodePosition = lambda  position : (X_axis[position[0]-1] , int(position[1]) )
# in all cases we keep in mind that the inital position is not included inside movement posibilities
rook_movement = lambda initialPos : [ x for x in [x for x in board if x[0]==initialPos[0] or x[1] == initialPos[1]  ] if x != initialPos ]
bishop_movement = lambda initialPos : [ x for x in [x for x in board if fabs(initialPos[0] - x[0] ) == fabs(initialPos[1] - x[1]) ] if x != initialPos ]
# queen is the fusion between rook and bishop
queen_movement = lambda initialPos : rook_movement(initialPos) + bishop_movement(initialPos) 
# theese function provides the structure to solve another movements as knigth or king; even, it is posible to use in a "new" piece.
asterisk_movement = lambda initialPos,distance : [x for x in queen_movement(initialPos) if floor(computeDistance(x,initialPos)) <= int(distance) ]
square_movement = lambda initialPos,distance: [ x for x in prodCartesiano(range(initialPos[0]-distance,initialPos[0]+distance+1),range(initialPos[1]-distance,initialPos[1]+distance+1)) if x!= initialPos ]
# The knigth (easy way to understand) is the opposite movement to queen in a small board (3x3) ; you can perform a knigth movement, just setting it in the squares where the queen can't reach.
# in our context, simply: substract to the square th asterisk.
knight_movement = lambda initialPos : [x for x in board if x in (set(square_movement(initialPos,2)) - set(asterisk_movement(initialPos,2)))  ]
# the pawn movement includes attacks; only in the correspondent row at game start you can move more than 1  square. 
positive_pawn_movement = lambda initialPos:   [x for x in board if  x[0] in [initialPos[0] + y for y in range(-1,2)] and x[1] == initialPos[1] + 1 and x != initialPos ] + [x for x in board if initialPos[1] == 2 and x[1] == 4 and x[0] == initialPos[0]  and x != initialPos] 
negative_pawn_movement = lambda initialPos: [x for x in board if  x[0] in [initialPos[0] - y for y in range(-1,2)] and x[1] == initialPos[1] - 1  and x != initialPos ] + [x for x in board if initialPos[1] == edgeLong-1 and x[1] == 5 and x[0] == initialPos[0] and x != initialPos ]