from scipy.spatial.distance import euclidean as computeDistance
from itertools import product as prodCartesiano
from math import fabs, floor
from board import *

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
asterisk_movement = lambda initialPos,distance : [x for x in queen_movement(initialPos) if floor(computeDistance(x,initialPos)) <= int(distance) ]
square_movement = lambda initialPos,distance: [ x for x in prodCartesiano(range(initialPos[0]-distance,initialPos[0]+distance+1),range(initialPos[1]-distance,initialPos[1]+distance+1)) if x!= initialPos ]
decodedPosition = lambda  position : (X_axis.index(position[0])+1 , int(position[1]) )
encodePosition = lambda  position : (X_axis[position[0]-1] , int(position[1]) )
checkBoardConsistent = lambda position: [x for x in board if x != position]
# in all cases we keep in mind that the inital position is not included inside movement posibilities
rook_movement = lambda initialPos : list(set(checkBoardConsistent(initialPos)).intersection(set([x for x in board if x[0]==initialPos[0] or x[1] == initialPos[1] ] )))
bishop_movement = lambda initialPos :  list(set(checkBoardConsistent(initialPos)).intersection(set([x for x in board if fabs(initialPos[0] - x[0] ) == fabs(initialPos[1] - x[1]) ])))
# queen is the fusion between rook and bishop
queen_movement = lambda initialPos : rook_movement(initialPos) + bishop_movement(initialPos) 
# The knigth (easy way to understand) is the opposite movement to queen in a small board (3x3) ; you can perform a knigth movement, just setting it in the squares where the queen can't reach.
# in our context, simply: substract to the square th asterisk.
knight_movement = lambda initialPos : [x for x in board if x in (set(square_movement(initialPos,2)) - set(asterisk_movement(initialPos,2)))  ]
# the pawn movement includes attacks; only in the correspondent row at game start you can move more than 1  square. 
positive_pawn_movement = lambda initialPos:   [x for x in board if  x[0] in [initialPos[0] + y for y in range(-1,2)] and x[1] == initialPos[1] + 1 and x != initialPos ] + [x for x in board if initialPos[1] == 2 and x[1] == 4 and x[0] == initialPos[0]  and x != initialPos]
negative_pawn_movement = lambda initialPos: [x for x in board if  x[0] in [initialPos[0] - y for y in range(-1,2)] and x[1] == initialPos[1] - 1  and x != initialPos ] + [x for x in board if initialPos[1] == edgeLong-1 and x[1] == 5 and x[0] == initialPos[0] and x != initialPos ]
# the king is easy , just an asterisk of 1 square distance.
king_movement = lambda initialPos: asterisk_movement(initialPos,1)

def regTest(pos):
    def label(piece):
        print("\n" * 2) 
        print("|"+"-"*40+"|")
        print("  %s movement"%piece)
        print("|"+"-"*40+"|")
        print("\n" * 2)

    label("rook")
    rookproof = [
        # just with b2
        ('a', 2),
        ('b', 2),
        ('c', 2),
        ('d', 2),
        ('e', 1),
        ('e', 3),
        ('e', 4),
        ('e', 5),
        ('e', 6),
        ('e', 7),
        ('e', 8),
        ('f', 2),
        ('g', 2),
        ('h', 2)
    ]
    rook_result = [encodePosition(e) for e in sorted(rook_movement(decodedPosition(pos)))]
    for e in rook_result:
        print(e)
    if (rookproof == rook_result):
        print("\neverything is ok!" )
    else:
        raise NameError("the rook is strange!")



    label("bishop")  
    bishopProof = [
      # just with b2
      ('a', 6),
      ('b', 5),
      ('c', 4),
      ('d', 1),
      ('d', 3),
      ('f', 1),
      ('f', 3),
      ('g', 4),
      ('h', 5)
        ]
    bishop_result = [encodePosition(e) for e in sorted(bishop_movement(decodedPosition(pos)))]
    for e in bishop_result:
        print(e)
    if (bishopProof == bishop_result):
        print("\neverything is ok!")
    else:
        raise NameError("the bishop is strange!")


    label("queen")
    queenproof = [
        ('a', 2),
        ('a', 6),
        ('b', 2),
        ('b', 5),
        ('c', 2),
        ('c', 4),
        ('d', 1),
        ('d', 2),
        ('d', 3),
        ('e', 1),
        ('e', 3),
        ('e', 4),
        ('e', 5),
        ('e', 6),
        ('e', 7),
        ('e', 8),
        ('f', 1),
        ('f', 2),
        ('f', 3),
        ('g', 2),
        ('g', 4),
        ('h', 2),
        ('h', 5)
    ]
    queen_result = [encodePosition(e) for e in sorted(queen_movement(decodedPosition(pos)))]
    for e in queen_result:
        print(e)
    if (queenproof == queen_result):
        print("\neverything is ok!")
    else:
        raise NameError("the queen is strange!")

    label("knight")
    knightproof = [
        ('c', 1),
        ('c', 3),
        ('d', 4),
        ('f', 4),
        ('g', 1),
        ('g', 3)
    ]
    knight_result = [encodePosition(e) for e in sorted(knight_movement(decodedPosition(pos)))]
    for e in knight_result:
        print(e)
    if (knightproof == knight_result):
        print("\neverything is ok!")
    else:
        raise NameError("the knight is strange!")



    label("up to down pawn ")
    negPawnproof = [
        ('d', 1),
        ('e', 1),
        ('f', 1)
    ]
    negPawn_result = [encodePosition(e) for e in sorted(negative_pawn_movement(decodedPosition(pos)))]
    for e in negPawn_result:
        print(e)

    if (negPawnproof == negPawn_result):
        print("\neverything is ok!")
    else:
        raise NameError("the negative pawn movement is strange!")


    label("down to up pawn ")
    posPawnproof = [
        ('d', 3),
        ('e', 3),
        ('e', 4),
        ('f', 3)
    ]
    posPawn_result = [encodePosition(e) for e in sorted(positive_pawn_movement(decodedPosition(pos)))]
    for e in posPawn_result:
        print(e)
    if (posPawnproof == posPawn_result):
        print("\neverything is ok!")
    else:
        raise NameError("the positive pawn movement is strange!")

    label("king")
    kingproof = [
        ('d', 1),
        ('d', 2),
        ('d', 3),
        ('e', 1),
        ('e', 3),
        ('f', 1),
        ('f', 2),
        ('f', 3)
    ]
    king_result = [encodePosition(e) for e in sorted(king_movement(decodedPosition(pos)))]
    for e in king_result:
        print(e)
    if (knightproof == knight_result):
        print("\neverything is ok!")
    else:
        raise NameError("the king is strange!")



def newFuncTest(pos):
    inip = decodedPosition(pos)
    finResult = [x for x in set(square_movement(inip,2)).intersection(set(asterisk_movement(inip,2))) if x[1] > inip[1] and fabs(x[0]-inip[0]) <= 1 ]
    for e in finResult:
        print(encodePosition(e))
    # [('f', 4), ('c', 1), ('d', 4), ('f', 0), ('c', 3), ('d', 0), ('g', 1), ('g', 0), ('e', 0), ('c', 0), ('g', 3)]

    print(finResult)



# regTest("e2")
newFuncTest("e2")