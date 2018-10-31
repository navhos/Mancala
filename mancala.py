##############################################################################
#
# File:         mancala.py
# Date:         Mon 15 October
# Author:       Navid Al Hossain
# Description:  Mancala
#
##############################################################################

# State is a list of length 15
# Stones in each position
# 0-5: Player1
# 6: Player1 Mancala
# 7-12: Player2
# 13: Player2 mancala


class State(Displayable):
    """A node in a search tree. It has a
    name a string
    isMax is True if it is a maximizing node, otherwise it is minimizing node
    children is the list of children
    value is what it evaluates to if it is a leaf.
    """
    def __init__(self, name, isMax, pos, children):
        self.name = name
        self.isMax = isMax
        self.pos = pos
        self.allchildren = children

    def pos(self):
        return self.pos

    def isLeaf(self):
        """returns true of this is a leaf node"""
        return self.allchildren is None

    def children(self):
        """returns the list of all children."""
        return self.allchildren

def legal_moves(self, state):
    """Return a list of the allowable moves at this point. A state represents the number of stones in each pit on the board.

    """"

    for(i in state):




def make_move(self, move, state):
    "Return the state that results from making a move from a state. For Mancala, a move is an integer in the range 0 to 5, inclusive."

def utility(self, state, player):
    "Return the value of this final state to player."

def terminal_test(self, state):
    "Return True if this is a final state for the game."

def to_move(self, state):
    "Return the player whose move it is in this state."
    return state.isMax

def display(self, state):
    "Print or otherwise display the state."

if __name__ == '__main__':
    cs210_utils.cs210_mainstartup()
