from src.game import *
from src.rules import movementRules
from src.rules import check
from src.pieces import *
from src.generalMovements import queen_movement
from src.generalMovements import decodedPosition
from src.generalMovements import encodePosition


if __name__ == '__main__':

    Piece_A = queen("white")
    Piece_A.setPosition("b2")

    Piece_B = king("black")
    Piece_B.setPosition("e5")

    Piece_C = king("white")
    Piece_C.setPosition("b4")

    Piece_D = pawn("black")
    Piece_D.setPosition("c3")


    myGame = game()
    myGame.pieces = [Piece_A,Piece_B,Piece_C,Piece_D]



    # print("probando movimiento de las piezas")
    # print(movementRules(p_piece=Piece_A,p_enviroment=myGame.pieces,p_futurePosition="e5"))

    # print("probando la amenaza al rey")
    # print(check(myGame.pieces[0],myGame.pieces))





