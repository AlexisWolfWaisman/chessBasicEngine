from src.pieces import *
from src.generalMovements import queen_movement
from src.generalMovements import decodedPosition
from src.generalMovements import encodePosition
if __name__ == '__main__':
    targetPiece = pawn("white")
    targetPiece.setPosition("b2")
    print(targetPiece.getPosition())
    print("la nueva posicion es:")
    targetPiece.makeMove("b4",opossitePrescence = ("c3","a3"))
    print(targetPiece.getPosition())
