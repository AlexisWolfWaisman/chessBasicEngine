from src.game import *
from src.rules import movementRules
from src.pieces import *
from src.generalMovements import queen_movement
from src.generalMovements import decodedPosition
from src.generalMovements import encodePosition


if __name__ == '__main__':

    Piece_A = queen("white")
    Piece_A.setPosition("b2")
    Piece_A.setCounterside("black")

    Piece_B = king("black")
    Piece_B.setPosition("d4")
    Piece_B.setCounterside("white")

    Piece_C = king("white")
    Piece_C.setPosition("b4")
    Piece_A.setCounterside("black")

    myGame = game()
    myGame.pieces = [Piece_A,Piece_B,Piece_C]


    print("probando movimiento de las piezas")
    print(movementRules(p_piece=Piece_A,p_enviroment=myGame.pieces,p_futurePosition="b5"))





