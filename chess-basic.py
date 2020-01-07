from numpy import prod as multiplicatoria
from numpy import sum as sumatoria 
from itertools import product as prodCartesiano
from itertools import permutations
from string import ascii_lowercase as abecedario
from math import fabs

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
tower_movement = lambda initialPos : [ x for x in [x for x in board if x[0]==initialPos[0] or x[1] == initialPos[1]  ] if x != initialPos ]
bishop_movement = lambda initialPos : [ x for x in [x for x in board if fabs(initialPos[0] - x[0] ) == fabs(initialPos[1] - x[1]) ] if x != initialPos ]
# the pawn movement includes attacks; only in the correspondent row at game start you can move more than 1  square. 
positive_pawn_movement = lambda initialPos: [x for x in board if  x[0] in [initialPos[0] + y for y in range(-1,2)] and x[1] == initialPos[1] + 1  ] + [x for x in board if initialPos[1] == 2 and x[1] == 4 and x[0] == initialPos[0] ]
negative_pawn_movement = lambda initialPos: [x for x in board if  x[0] in [initialPos[0] - y for y in range(-1,2)] and x[1] == initialPos[1] - 1  ] + [x for x in board if initialPos[1] == edgeLong-1 and x[1] == 5 and x[0] == initialPos[0] ]
# Knight explained: if you add 2 to a coordinate and 1 to the rest, you have the elements of a permutation (all the possibilities between these sums) in which the only ones available are all those whose absolute value of the subtraction of them is 1 or 3.
# by example: knight at d4, can move to e6 or c6... e=5  so abs(5-6) == 1 and c=3 so abs(3-6) = 3. Every absolute value in the substraction between the coordinates from the available position  ... must be in the set formed by 1 and 3.
horse_movement =lambda initialPos : [x for x in board if x in [x for x in list(permutations([sumatoria(x) for x in prodCartesiano(set(initialPos),(-1,1,2,-2))],2)) if fabs(x[0] - x[1]) in (1,3) ] ]
 


def test(test_position):
  if validatePos(test_position):          
    for e in bishop_movement(decodedPosition(test_position)):
      print(encodePosition(e))

   



test("d7")

#print("---------------\n"*2)
#test("c7")

#pieces = ["Tower","Queen","King","Pawn","Bishop","knight"]
# intial pos is something like: "a3"
