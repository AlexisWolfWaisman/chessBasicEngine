from .rules import movementRules

class game(object):
    def __init__(self):
        teams = None
        boards = None
        pieces = []
        matchResults ={
            "win":None,# id or object
            "lose":None, # id or object
            "tie": [], # list of objects or ids
            "punctuation":{   } # by example:  {1 : 25 , 2: 3} ordered by position
            }
        players = None
        rules = None
        factions = {}

class standard_game(game):
    def __init__(self):
        super.__init__()
        pieces = {
  'r': u'♜', 'n': u'♞', 'b': u'♝', 'q': u'♛',
  'k': u'♚', 'p': u'♟', 'R': u'♖', 'N': u'♘',
  'B': u'♗', 'Q': u'♕', 'K': u'♔', 'P': u'♙',
  None: ' '
}


def makeMove(piece,futurePostion,enviroment = []):
    if  chess_movementRules(piece,enviroment) == True:
        piece.setPosition(futurePostion)
