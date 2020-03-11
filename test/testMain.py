from src.pieces import *
from src.generalMovements import queen_movement
from src.generalMovements import decodedPosition
from src.generalMovements import encodePosition
from src.rules import directAmenace
if __name__ == '__main__':

    Piece_A = queen("white")
    Piece_A.setPosition("b2")
    Piece_A.setCounterside("black")

    Piece_B = king("black")
    Piece_B.setPosition("d4")
    Piece_B.setCounterside("white")

    Piece_C = king("white")
    Piece_C.setPosition("c3")
    Piece_A.setCounterside("black")


    print(Piece_A.currentMovement())
    print(directAmenace(Piece_A,Piece_B))


