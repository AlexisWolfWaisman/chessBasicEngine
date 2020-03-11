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

    def addTeamInFaction(self,p_team,p_faction):
        if p_team in self.teams and p_faction in self.factions.keys and p_team not in self.factions.values:
                    self.factions[p_faction].append(p_team)

        if p_team in self.teams and p_faction not in self.factions.keys and p_team not in self.factions.values:
                    self.factions[p_faction] = [p_team]


    def popTeamFromFaction(self,p_team,p_faction):
        if p_team in self.teams and p_team in self.factions[p_faction] :
            self.factions[p_faction].remove(p_team)

    def whichFaction(self,p_piece):
        for k,v in self.factions.items():
            if v == p_piece.getTeam():
                return k




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
    if  movementRules(piece,enviroment) == True:
        piece.setPosition(futurePostion)