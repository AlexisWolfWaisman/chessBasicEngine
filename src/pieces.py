# Dependencies
from src.generalMovements import cross_movement,X_movement,asterisk_movement,counterAsterisk_movement,\
oneStepAsterisk_movement,positive_oneStepTriangle_movement,negative_oneStepTriangle_movement,\
encodePosition,decodedPosition,computeDistance
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# math functions
from math import atan2,pi
angleBetweenPoints = lambda origin,destiny: int(atan2(destiny[1] - origin[1], destiny[0] - origin[0]) * 180 / pi)

class piece(object):
    team = None
    position = None
    movementFunction = None


    def __init__(self,p_team=None,p_position=None,p_movementFunction=None):
        self.setTeam(p_team)
        self.setPosition(p_position)
        self.setMovementFunction(p_movementFunction)

    def __str__(self):
        return "%s %s"%(self.team , type(self).__name__)

# ------------------- Setters and getters ----------------------------------------------------
    def setTeam(self,p_team):
        if p_team != None:
            self.team = p_team
    def getTeam(self):
        return self.team

    def setPosition(self,p_position):
        if p_position != None:
            self.position = decodedPosition(p_position)
    def getPosition(self):
        return encodePosition(self.position)

    def setMovementFunction(self,p_movementFunction):
        if p_movementFunction != None: #TODO it must be a lambda function
            self.movementFunction = p_movementFunction

    def getMovementFunction(self):
        return self.movementFunction

    def getMovement(self):
        return self.getMovementFunction()(self.position)


# ------------------- End ------------------------------------------------------------------


#----------------- General features about all pieces ----------------------------------------
    def currentMovement(self,position):
        return[ encodePosition(x) for x in  self.getMovement()]

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
                interceptables.append(elem)
        return interceptables

# ------------------- End ------------------------------------------------------------------



#---------------------- Pieces (Chess) -----------------------------------------------------
class queen(piece):
    def __init__(self,p_team):
        super().__init__(p_team,p_movementFunction=asterisk_movement)
        # super().setMovementFunction(None)



    def changePosition(self,p_position):
        super.setPosition(p_position)





class knight(piece):
    def __init__(self,p_team):
        super().__init__(p_team)
        self.movement = counterAsterisk_movement

class rook(piece):
    def __init__(self, p_team):
        super().__init__(p_team)
        self.movement = cross_movement

class bishop(piece):
    def __init__(self, p_team):
        super().__init__(p_team)
        self.movement = X_movement

class king(piece):
    def __init__(self, p_team):
        super().__init__(p_team)
        self.movement = oneStepAsterisk_movement


class pawn(piece):
    def __init__(self, p_team):
        super().__init__(p_team)
        # standard
        self.standardStart(p_team)

    def standardStart(self,p_team):
        if p_team == "white":
            self.movement = positive_oneStepTriangle_movement
        if p_team == "black":
            self.movement = negative_oneStepTriangle_movement

# ------------------- End ------------------------------------------------------------------