from src.statusCodes import codes as sCodes
from src.generalMovements import *
from src.rules import *
class piece(object):
    def __init__(self,p_team):
        position : None
        movement: None
        team: p_team

    # position will be as tuple : (3,2)
    def setPosition(self,p_position):
        self.position = decodedPosition(p_position)
    def getPosition(self):
        return encodePosition(self.position)

    def setMovement(self,p_movement):
        self.movement = p_movement
    def getMovement(self):
        return self.movement


    def makeMove(self,futurePosition,alliesPresence= []):
        pos = decodedPosition(futurePosition)
        posibMoves = [x for x in self.movement(self.position) if x not in alliesPresence]
        if  pos in posibMoves:
            self.setPosition(futurePosition)
        else:
            answer = 1
            raise NameError(sCodes[answer])

class queen(piece):
    def __init__(self,p_team):
        super().__init__(p_team)
        self.movement = queen_movement

class knight(piece):
    def __init__(self,p_team):
        super().__init__(p_team)
        self.movement = knight_movement

class rook(piece):
    def __init__(self, p_team):
        super().__init__(p_team)
        self.movement = rook_movement

class bishop(piece):
    def __init__(self, p_team):
        super().__init__(p_team)
        self.movement = bishop_movement

class king(piece):
    def __init__(self, p_team):
        super().__init__(p_team)
        self.movement = king_movement




class pawn(piece):
    def __init__(self, p_team):
        super().__init__(p_team)
        # standard
        self.standardStart(p_team)

    def standardStart(self,p_team):
        if p_team == "white":
            self.movement = positive_pawn_movement
        if p_team == "black":
            self.movement = negative_pawn_movement

    def makeMove(self,futurePosition, alliesPresence = [], opossitePrescence = [] ):
        pos = decodedPosition(futurePosition)
        posibMoves = [ x for x in self.movement(self.position) if x[0] == self.position[0] and x not in alliesPresence]
        if opossitePrescence != []:
            prescence = [decodedPosition(x) for x in opossitePrescence]
            posibMoves = list(set(posibMoves).union(set(prescence)))
        if pos in posibMoves  :
            self.setPosition(futurePosition)
        else:
            answer = 1
            raise NameError(sCodes[answer])




