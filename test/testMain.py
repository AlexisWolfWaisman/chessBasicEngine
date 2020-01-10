from src.pieces import piece
from src.generalMovements import queen_movement
from src.generalMovements import decodedPosition
from src.generalMovements import encodePosition
if __name__ == '__main__':
    justAqueen = piece()
    justAqueen.setMovement(queen_movement)
    justAqueen.setPosition("e2")
    print(justAqueen.getPosition())
    justAqueen.makeMove("e3")
    print("\n"+"La actual es:\n")
    print(justAqueen.getPosition())