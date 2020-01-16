from scipy.spatial.distance import euclidean as computeDistance
from src.generalMovements import encodePosition,decodedPosition
#TODO: directAmenace
def directAmenace(attacker,target,enviroment=[]):
    # attacker and target are objects
    reachP = attacker.reacheable_pieces([target]) if enviroment == [] else enviroment
    for key,value in reachP.items():
        if value == target and target.getPosition() in attacker.currentMovement():
            return True
    return False

#TODO: Check
def check(king,alliesPresence = [], opossitePrescence = [] ):
    pass


#TODO: castling
def castling(side,team):
    """
    :param self: object
    :param side: string | options: Q/K (Queenside/Kingside)
    :param team: string | W/B (White/Black)
    :return:
    """
    # White QueenSide --> WQS
    posibilities = {"WQ":{"King":"d1","Rook":"c1"},
                    "WK":{"King":"g1","Rook":"f1"},
                    "BQ":{"King":"b8","Rook":"c8"},
                    "BK": {"King": "f8", "Rook": "e8"}
                    }
    return posibilities[team.upper()+side.upper()]

# TODO: enpassant
def enpassant(self):
    pass

# TODO: Crowning (pawn becomes another piece)
def crowning(self):
    pass

# TODO: Draw by STALEMATE
"""
When the player to move isn’t in check, but none of his pieces can move
"""
def stalemate():
    pass


#TODO: draw by 50-move rule
"""
A type of draw where both players make 50 moves consecutively without either player advancing a pawn or making a capture.
"""
def fiftyMovesRule():
    pass

#TODO: draw by repetition
def repetition():
    pass
"""
 A type of draw where the same position is reached three times with the same player to move. Does not require the same moves and can occur at any point in the game.
"""

if __name__ == '__main__':
    print(castling("K","W"))