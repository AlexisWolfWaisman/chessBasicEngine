from src.statusCodes import codes as sCodes
from src.generalMovements import *
from numpy import angle
from math import atan2,pi
# angleBetweenPoints = lambda origin,destiny: angle(complex(destiny[0]-origin[0],destiny[1]-origin[1]),deg=True)
angleBetweenPoints = lambda origin,destiny: int(atan2(destiny[1] - origin[1], destiny[0] - origin[0]) * 180 / pi)
class piece(object):
    team = None
    position = None
    movement = None
    counterside = []
    sameSide = []

    def __init__(self,p_team):
        self.setTeam(p_team)

    def __str__(self):
        return "%s %s"%(self.team , type(self).__name__)

# ------------------- Setters and getters ----------------------------------------------------
    def setTeam(self,p_team):
        self.team = p_team
    def getTeam(self):
        return self.team

    def setPosition(self,p_position):
        self.position = decodedPosition(p_position)
    def getPosition(self):
        return encodePosition(self.position)

    def setMovement(self,p_movement):
        self.movement = p_movement
    def getMovement(self):
        return self.movement

    def setCounterside(self,p_oposition):
            self.counterside.append(p_oposition)
    def getCounterside(self):
        return self.counterside

    def setSameSide(self,p_sameSide):
        self.sameSide = p_sameSide
    def getSameSide(self):
        return self.sameSide

# ------------------- End ------------------------------------------------------------------


#----------------- General features about all pieces ----------------------------------------
    def currentMovement(self):
        return[ encodePosition(x) for x in  self.getMovement()(self.position)]

    def neighbourhood_pieces_around_in_plane(self,p_enviroment=[]):
        """
        This searchs in all the plane pieces to catch by the current. Without knowing the current movement.
        :param p_enviroment: list of pieces
        :return: dict
        """
        enviroment = p_enviroment[:]
        # self is filtered
        #print([str(x) for x in enviroment])
        enviroment.pop(enviroment.index(self))
        #print([str(x) for x in enviroment])
        compass = dict(zip(range(0,360,45),[[]]*8))
        for elem in enviroment:
            keyIndex = angleBetweenPoints(self.position,elem.position)
            # nearby elements are "reachable" , just them.
            elemDistance = computeDistance(self.position,elem.position)
            currentNeighbour = compass[keyIndex]
            if currentNeighbour != []:
                currentDistance = currentNeighbour[1]
                if elemDistance < currentDistance:
                    compass[keyIndex] = (elem,elemDistance)#elem.__str__(),elem.getPosition(),elemDistance)
            else:
                compass[keyIndex] =  (elem,elemDistance) #(elem.__str__(),elem.getPosition(),elemDistance)

        for k,v in compass.items():
            if len(v) > 0:
                compass[k] = v[0]
            else:
                compass[k] = None

        return compass

    def interceptablePieces(self,enviroment=[]):
        interceptables = []
        for elem in self.neighbourhood_pieces_around_in_plane(enviroment).items():
            if elem[1] != None and elem[1].getPosition() in self.currentMovement():
                interceptables.append(elem[1])
        return interceptables
# ------------------- End ------------------------------------------------------------------



#---------------------- Pieces (Chess) -----------------------------------------------------
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

# ------------------- End ------------------------------------------------------------------





