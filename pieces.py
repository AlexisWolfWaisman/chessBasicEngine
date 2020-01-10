class piece(object):
    def __init__(self):
        position : None
        movement: None

    def setPosition(self,p_position):
        self.position = p_position
    def getPosition(self):
        return self.position

    def setMovement(self,p_movement):
        self.movement = p_movement
    def getMovement(self):
        return self.movement

    def makeMove(self,position):




class king(piece):
    pass
