from src.statusCodes import codes as sCodes
from src.generalMovements import encodePosition,decodedPosition
class piece(object):
    def __init__(self):
        position : None
        movement: None
    # position will be as tuple : (3,2)
    def setPosition(self,p_position):
        self.position = decodedPosition(p_position)
    def getPosition(self):
        return encodePosition(self.position)

    def setMovement(self,p_movement):
        self.movement = p_movement
    def getMovement(self):
        return self.movement

    def checkRules(self,position):
        return True

    def makeMove(self,futurePosition):
        pos = decodedPosition(futurePosition)
        if  pos in self.movement(self.position):
            if self.checkRules(decodedPosition(futurePosition)):
                self.setPosition(futurePosition)
            else:
                answer = 2
                return answer
                #raise NameError(sCodes[answer])
        else:
            print(self.movement(self.position))
            answer = 1
            raise NameError(sCodes[answer])


class king(piece):
    pass
