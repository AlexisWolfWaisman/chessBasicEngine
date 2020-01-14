from src.pieces import *
from src.generalMovements import queen_movement
from src.generalMovements import decodedPosition
from src.generalMovements import encodePosition
if __name__ == '__main__':
    Piece_A = queen("white")
    Piece_A.setPosition("b2")
    Piece_A.setCounterside("black")

    Piece_B = pawn("black")
    Piece_B.setPosition("d4")
    Piece_B.setCounterside("white")

    Piece_C = pawn("white")
    Piece_C.setPosition("c3")
    Piece_A.setCounterside("black")


    alcanzables = Piece_A.reacheable_pieces((Piece_B,Piece_C))
    print(alcanzables)
    print(alcanzables[0])

