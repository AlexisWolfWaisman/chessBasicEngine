from src.pieces import *
from src.generalMovements import queen_movement
from src.generalMovements import decodedPosition
from src.generalMovements import encodePosition
if __name__ == '__main__':
    Piece_A = queen("white")
    Piece_A.setPosition("b2")
    Piece_A.setCounterside("black")

    Piece_B = pawn("black")
    Piece_B.setPosition("c3")
    Piece_B.setCounterside("white")

    print(Piece_A.reacheable_pieces([Piece_B]))
    print(Piece_A)
