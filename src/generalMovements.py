from numpy import array as NParray, sign
from scipy.spatial.distance import euclidean as computeDistance
from itertools import product as cartessianProd
from math import fabs, floor
from src.board import *

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
square_movement = lambda initialPos,distance: [ x for x in cartessianProd(range(initialPos[0]-distance,initialPos[0]+distance+1),range(initialPos[1]-distance,initialPos[1]+distance+1)) if x!= initialPos ]
spider_movement = lambda initialPos,distance: [x for x in set(square_movement(initialPos,distance)).intersection(set(asterisk_movement(initialPos,distance)))]
spot_movement = lambda initialPos,distance:  set(spider_movement(initialPos,distance)) - set(map(tuple,NParray(initialPos) + list(cartessianProd((2,-2),repeat=2))))
triangle_movement = lambda initialPos,distance,direction: [x for x in spot_movement(initialPos,distance) if sign(x[1]-initialPos[1])==sign(direction) ]
decodedPosition = lambda  position : (X_axis.index(position[0])+1 , int(position[1]) )
encodePosition = lambda  position : "%s%s"%(X_axis[position[0]-1] , int(position[1]) )
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
positive_pawn_movement = lambda initialPos: triangle_movement(initialPos,2,1) if initialPos[1] == Y_axis[1] else triangle_movement(initialPos,1,1)
negative_pawn_movement = lambda initialPos: triangle_movement(initialPos,2,-1) if initialPos[1] == Y_axis[edgeLong-1] else triangle_movement(initialPos,1,-1)
# the king is easy , just an asterisk of 1 square distance.
king_movement = lambda initialPos: asterisk_movement(initialPos,1)


"""
def regTest(pos):
    def label(piece):
        print("\n" * 2) 
        print("|"+"-"*40+"|")
        print("  %s movement"%piece)
        print("|"+"-"*40+"|")
        print("\n" * 2)

    label("rook")
    rookproof =   ['a2', 'b1', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'] # just with b2
    rook_result = [encodePosition(e) for e in sorted(rook_movement(decodedPosition(pos)))]
    for e in rook_result:
        print(e)
    if (rookproof == rook_result):
        print("\neverything is ok!" )
    else:
        print(rook_result)
        raise NameError("the rook is strange!")



    label("bishop")  
    bishopProof = ['a1', 'a3', 'c1', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'] # just with b2
    bishop_result = [encodePosition(e) for e in sorted(bishop_movement(decodedPosition(pos)))]
    for e in bishop_result:
        print(e)
    if (bishopProof == bishop_result):
        print("\neverything is ok!")
    else:
        raise NameError("the bishop is strange!")


    label("queen")
    queenproof = ['a1', 'a2', 'a3', 'b1', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'd2', 'd4', 'e2', 'e5', 'f2', 'f6', 'g2', 'g7', 'h2', 'h8'] # just with b2
    queen_result = [encodePosition(e) for e in sorted(queen_movement(decodedPosition(pos)))]
    for e in queen_result:
        print(e)
    if (queenproof == queen_result):
        print("\neverything is ok!")
    else:
        raise NameError("the queen is strange!")

    label("knight")
    knightproof =['a4', 'c4', 'd1', 'd3'] # just with b2
    knight_result = [encodePosition(e) for e in sorted(knight_movement(decodedPosition(pos)))]
    for e in knight_result:
        print(e)
    if (knightproof == knight_result):
        print("\neverything is ok!")
    else:
        raise NameError("the knight is strange!")



    label("up to down pawn ")
    negPawnproof = ['a1', 'b1', 'c1']  # just with b2
    negPawn_result = [encodePosition(e) for e in sorted(negative_pawn_movement(decodedPosition(pos)))]
    for e in negPawn_result:
        print(e)

    if (negPawnproof == negPawn_result):
        print("\neverything is ok!")
    else:
        raise NameError("the negative pawn movement is strange!")


    label("down to up pawn ")
    posPawnproof = ['a3', 'b3', 'b4', 'c3']  # just with b2
    posPawn_result = [encodePosition(e) for e in sorted(positive_pawn_movement(decodedPosition(pos)))]
    for e in posPawn_result:
        print(e)
    if (posPawnproof == posPawn_result):
        print("\neverything is ok!")
    else:
        raise NameError("the positive pawn movement is strange!")

    label("king")
    kingproof = ['a1', 'a2', 'a3', 'b1', 'b3', 'c1', 'c2', 'c3'] # just with b2
    king_result = [encodePosition(e) for e in sorted(king_movement(decodedPosition(pos)))]
    for e in king_result:
        print(e)
    if (knightproof == knight_result):
        print("\neverything is ok!")
    else:
        raise NameError("the king is strange!")
def newFuncTest(pos):
    inip = decodedPosition(pos)
    print(triangle_movement(inip,2,1))
    # finResult = sorted(diamond_movement(inip))
    # for e in finResult:
    #     print(encodePosition(e))
    # [('f', 4), ('c', 1), ('d', 4), ('f', 0), ('c', 3), ('d', 0), ('g', 1), ('g', 0), ('e', 0), ('c', 0), ('g', 3)]
regTest("b2")
# newFuncTest("e3")
"""