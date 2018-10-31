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

    def legal_moves(self, state):
        """Return a list of the allowable moves at this point. A state represents the number of stones in each pit on the board.
        >>> state1 =  State(True, [4,4,4,4,4,4,0,4,4,4,4,4,4,0])
        >>> state2 =  State(True, [4,4,0,4,4,4,0,4,4,4,4,4,4,0])
        >>> state3 =  State(False, [4,4,4,4,4,4,0,4,4,0,4,4,4,0])


        >>> legal_moves(state1)
        [0, 1, 2, 3, 4, 5]
        >>> legal_moves(state2)
        [0, 1, 3, 4, 5]
        >>> legal_moves(state3)
        [0, 1, 3, 4, 5]
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
        """Return the state that results from making a move from a state. For Mancala, a move is an integer in the range 0 to 5, inclusive."""
        if(move in legal_moves(state)):

            #Convert moves to appropriate positions if its the Min players turn
            if(not state.isMax):
                    move = move + 7

            #steps before the final one
            step = 0
            curr = move

            #make a deepcopy of the state
            result = copy.deepcopy(state)

            while(step < result.pos[move]):
                curr = (curr + 1) % 14

                if((result.isMax and curr != 13) || (not(result.isMax) and curr != 6)):
                    result.pos[cur] = result.pos[cur] + 1
                    step = step + 1

                    #final move on mancala
                    if((step == result.pos[move] and result.isMax and curr == 6) || (step == result.pos[move] and not(result.isMax) and curr == 13)):
                        result.isMax = result.isMax
                    #final move on empty spot for max
                    elif((step == result.pos[move] and result.isMax and (curr in ([0,1,2,3,4,5])) and result.pos[cur] == 1) || (step == result.pos[move] and not(result.isMax) and (curr in ([7,8,9,10,11,12])) and result.pos[cur] == 1)):
                        result.pos[cur] = result.pos[cur] + result.pos[12-curr]
                        result.isMax = not(result.isMax)
                    #normal final move
                    elif(step == result.pos[move]):
                        result.isMax = not(result.isMax)

            #make the number of gems in the initial position = 0
            result.pos[move] = 0
            return result

# def utility(self, state, player):
#     "Return the value of this final state to player."
#
# def terminal_test(self, state):
#     "Return True if this is a final state for the game."
#
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
