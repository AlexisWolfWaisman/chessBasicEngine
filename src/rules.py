from scipy.spatial.distance import euclidean as computeDistance
from src.generalMovements import encodePosition,decodedPosition
from src.pieces import angleBetweenPoints


#TODO: Check
def check(p_attacker,p_enviroment):
    for x in p_attacker.interceptablePieces(p_enviroment):
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

def movementRules(p_piece,p_enviroment,p_futurePosition=None):
    """
    Theese rules are just a compendium of variables that give the tools for develop the logic of each
    movement. f.e. rook case: if there is an enemy interception the rook can capture, but this is not always true
    in knight case.

    :param p_piece: piece | the current piece
    :param p_enviroment: list | list of pieces
    :param p_futurePosition: tuple | the position where we want set the piece
    :return: dict | keys:
            availableMovement = true if the piece has the position in its movement
            alliedInterception = true if there is an allie piece in the way.
            enemyIntersection = true if there is an enemy piece in the way
    """
    futPos = p_futurePosition
    envir = p_enviroment[:]
    currPiece = p_piece
    pair_of_pos =  decodedPosition(p_piece.getPosition()) , decodedPosition(futPos)
    angle_to_point = angleBetweenPoints(*pair_of_pos)
    dist_to_point = computeDistance(*pair_of_pos)

    # IF IS ALONE ...can move?
    flag1 = futPos in currPiece.currentMovement()

    # There is an allie interception?
    flag2=False
    for x in p_piece.interceptablePieces(envir):
        if x[1].getTeam() == currPiece.getTeam() and angle_to_point == x[0] :
            dist_to_intercepted = computeDistance(decodedPosition(p_piece.getPosition()),decodedPosition(x[1].getPosition()))
            flag2 = dist_to_intercepted < dist_to_point
            if flag2 == True: break

    # There is an enemy interception?
    flag3 = False
    for x in p_piece.interceptablePieces(envir):
        if x[1].getTeam() != currPiece.getTeam() and angle_to_point == x[0]:
            dist_to_intercepted = computeDistance(decodedPosition(p_piece.getPosition()),
                                                  decodedPosition(x[1].getPosition()))
            flag3 = dist_to_intercepted < dist_to_point
            if flag3 == True: break

    return {"availableMovement":flag1,"alliedInterception":flag2,"enemyIntersection":flag3}