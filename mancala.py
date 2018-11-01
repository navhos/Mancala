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

import cs210_utils
import copy

class State():
    """A node in a search tree. It has a
    name a string
    isMax is True if it is a maximizing node, otherwise it is minimizing node
    children is the list of children
    value is what it evaluates to if it is a leaf.
    """
    def __init__(self, isMax, pos):
        self.isMax = isMax
        self.pos = pos
        # self.allchildren = children

    def pos(self):
        return self.pos

    # def isLeaf(self):
    #     """returns true of this is a leaf node"""
    #     return self.allchildren is None

    # def children(self):
    #     """returns the list of all children."""
    #     return self.allchildren

class Mancala():
    """
    >>> mancala = Mancala()
    >>> state1 =  State(True, [4,4,4,4,4,4,0,4,4,4,4,4,4,0])
    >>> state2 =  State(True, [4,4,0,4,4,4,0,4,4,4,4,4,4,0])
    >>> state3 =  State(False, [4,4,4,4,4,4,0,4,4,0,4,4,4,0])


    >>> mancala.legal_moves(state1)
    [0, 1, 2, 3, 4, 5]
    >>> mancala.legal_moves(state2)
    [0, 1, 3, 4, 5]
    >>> mancala.legal_moves(state3)
    [0, 1, 3, 4, 5]

    >>> state1_0 = mancala.make_move(0, state1)
    >>> state1_0.isMax
    False
    >>> state1_0.pos
    [0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    >>> state1_0 = mancala.make_move(2, state1)
    >>> state1_0.isMax
    True
    >>> state1_0.pos
    [4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0]

    >>> state3_0 = mancala.make_move(0, state3)
    >>> state3_0.isMax
    True
    >>> state3_0.pos
    [4, 4, 4, 4, 4, 4, 0, 0, 5, 1, 5, 5, 4, 0]

    >>> state4 = State(True, [0,4,4,4,4,8,0,4,4,4,4,4,4,0])
    >>> state4_5 = mancala.make_move(5, state4)
    >>> state4_5.isMax
    False
    >>> state4_5.pos
    [6, 4, 4, 4, 4, 0, 1, 5, 5, 5, 5, 5, 0, 0]
    """
    def __init__(self):
        self.state = State(True, [4,4,4,4,4,4,0,4,4,4,4,4,4,0])

    def legal_moves(self, state):
        """Return a list of the allowable moves at this point. A state represents the number of stones in each pit on the board.

        """
        if(state.isMax):
            moves = [0, 1 , 2 , 3, 4, 5]
        else:
            moves = [7, 8, 9, 10, 11, 12]

        result = []

        for i in range(0,6):
            if(state.pos[moves[i]] != 0):
                result.append(moves[i])

        if(not state.isMax):
            for i in range(len(result)):
                result[i] = result[i]-7

        return result

    def make_move(self, move, state):
        """Return the state that results from making a move from a state. For Mancala, a move is an integer in the range 0 to 5, inclusive.
        >>>
        """
        mancala = Mancala()
        if(move in mancala.legal_moves(state)):

            #Convert moves to appropriate positions if its the Min players turn
            if(not state.isMax):
                    move = move + 7

            #steps before the final one
            step = 0
            curr = move

            #make a deepcopy of the state
            result = copy.deepcopy(state)
            result.pos[move] = 0

            while(step < state.pos[move]):
                curr = (curr + 1) % 14

                if((result.isMax and curr != 13) or (not(result.isMax) and curr != 6)):
                    result.pos[curr] = result.pos[curr] + 1
                    step = step + 1

                    #final move on mancala
                    if((step == state.pos[move] and result.isMax and curr == 6) or (step == state.pos[move] and not(result.isMax) and curr == 13)):
                        result.isMax = result.isMax
                    #final move on empty spot for max
                    elif((step == state.pos[move] and result.isMax and (curr in ([0,1,2,3,4,5])) and result.pos[curr] == 1) or (step == state.pos[move] and not(result.isMax) and (curr in ([7,8,9,10,11,12])) and result.pos[curr] == 1)):
                        result.pos[curr] = result.pos[curr] + result.pos[12-curr]
                        result.pos[12-curr] = 0
                        result.isMax = not(result.isMax)
                    #normal final move
                    elif(step == state.pos[move]):
                        result.isMax = not(result.isMax)

            #make the number of gems in the initial position = 0
            return result

    # def utility(self, state, player):
    #     "Return the value of this final state to player."
    #
    def terminal_test(self, state):
        "Return True if this is a final state for the game."


    def to_move(self, state):
        """Return the player whose move it is in this state.
        returns isMax
        1 is Max player
        0 is Min player
        """
        return state.isMax
    #
    # def display(self, state):
    #     "Print or otherwise display the state."

if __name__ == '__main__':
    cs210_utils.cs210_mainstartup()
