import random
import math


#BOT_NAME =  # INSERT NAME FOR YOUR BOT HERE OR IT WILL THROW AN EXCEPTION
BOT_NAME = "botty"
currentHigh = -math.inf
currentLow = math.inf
class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    
    #rseed = None  # change this to a value if you want consistent random choices
    rseed = 1
    def __init__(self):
        if self.rseed is None:
            self.rstate = None
        else:
            random.seed(self.rseed)
            self.rstate = random.getstate()

    def get_move(self, state):
        if self.rstate is not None:
            random.setstate(self.rstate)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move.  Very slow and not always smart."""

    def get_move(self, state, depth=None):
        
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None
    
        for move, state in state.successors():
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state):
        """Determine the minimax utility value of the given state.

        Gets called by get_move() to determine the value of each successor state.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the exact minimax utility value of the state
        """
        


        if state.successors() != [] or not state.is_full():
            #for move, sState in state.successors():
            bestM,bestS = self.get_move(state)
            
            return bestS.utility()
        else:
            return state.utility()
                #u = self.minimax(sState)
                #if ((nextp == 1) and (u > best_util)) or ((nextp == -1) and (u < best_util)):
                #    best_util = u
            #if abs(u) > abs(state.utility()):
                #return u
            #else:
                #return state.utility()

            #best_move, best_state = self.get_move(state)
            #newState = self.minimax(state.successors())

        

       # else:
        #    state.utility()
        #if()
        #for iter in 

        #
        # Fill this in!
        #
        #return best_state.utility()  # Change this line!


class MinimaxLookaheadAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move.
 
    Hint: Consider what you did for MinimaxAgent. What do you need to change to get what you want? 
    """

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state.

        Gets called by get_move() to determine the value of successor states.

        The depth data member (set in the constructor) determines the maximum depth of the game 
        tree that gets explored before estimating the state utilities using the evaluation() 
        function.  If depth is 0, no traversal is performed, and minimax returns the results of 
        a call to evaluation().  If depth is None, the entire game tree is traversed.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the (possibly estimated) minimax utility value of the state
        """
        depth_count = 1
        if self.depth_limit == None:
            if state.successors() != [] or not state.is_full():
                #for move, sState in state.successors():
                bestM,bestS = self.get_move(state)
                return bestS.utility()
            else:
                return state.utility()
        elif self.depth_limit == 0:
            return self.evaluation(state)
        # Fill this in!
        #
          # Change this line!
        else:
            return self.minimax_depth(state, depth_count)

    def minimax_depth(self, state, depth):
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None
        depth += 1
        if state.successors() != [] or not state.is_full():
            for move, sState in state.successors():
                if depth < self.depth_limit:
                    util = self.minimax_depth(sState,depth)
                else:
                    util = self.evaluation(sState)
                if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                        best_util, best_move, best_state = util, move, sState        
            return self.evaluation(best_state)
        return self.evaluation(state)
            
                
        """This is just a helper method for minimax(). Feel free to use it or not. """
        

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        Gets called by minimax() once the depth limit has been reached.  
        N.B.: This method must run in "constant" time for all states!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heuristic estimate of the utility value of the state
        """
        p1_score = state.utility() + 1
        p2_score = state.utility() + 1
        #for run in state.get_rows() + state.get_cols() + state.get_diags():
        #    for elt, length in state.scores():
        #        if (elt == 1) and (length >= 3):
         #           p1_score += length**4
          #      elif (elt == -1) and (length >= 3):
           #         p2_score += length**4
        return p1_score - p2_score
        #
        # Fill this in!
        #
        # Note: This cannot be "return state.utility() + c", where c is a constant. 
       
         # Change this line!


class AltMinimaxLookaheadAgent(MinimaxAgent):
    """Alternative heursitic agent used for testing."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state."""
        #
        # Fill this in, if it pleases you.
        #
        return 19  # Change this line, unless you have something better to do.


class MinimaxPruneAgent(MinimaxAgent):
    """Computer agent that uses minimax with alpha-beta pruning to select the best move.
    
    Hint: Consider what you did for MinimaxAgent.  What do you need to change to prune a
    branch of the state space? 
    """
    def minimax(self, state):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by MinimaxAgent.minimax(), but the 
        algorithm should do less work.  You can check this by inspecting the value of the class 
        variable GameState.state_count, which keeps track of how many GameState objects have been 
        created over time.  This agent does not have a depth limit.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to column 1 (we're trading optimality for gradeability here).

        Args: 
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """

        """  nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None
    
        for move, state in state.successors():
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state """
        #
        # Fill this in!
        #

        return self.alphabeta(state,-math.inf,math.inf )

    def alphabeta(self, state,alpha, beta):
        """This is just a helper method for minimax(). Feel free to use it or not."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None
        currentHigh = -math.inf
        currentLow = math.inf
        if state.successors() != [] or not state.is_full():
            for move, sState in state.successors():               
                util = self.alphabeta(sState,alpha,beta)
                if util > currentHigh and util < currentLow:
                    if (nextp == 1):
                        currentHigh = util
                        best_state= sState.utility()
                        break
                    elif (nextp == -1):
                        currentLow = util
                        best_state = sState.utility()
                        break
                #elif ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                       # best_util, best_move, best_state = util, move, sState
                        
            return best_state
        return state.utility()
       


def get_agent(tag):
    if tag == 'random':
        return RandomAgent()
    elif tag == 'human':
        return HumanAgent()
    elif tag == 'mini':
        return MinimaxAgent()
    elif tag == 'prune':
        return MinimaxPruneAgent()
    elif tag.startswith('look'):
        depth = int(tag[4:])
        return MinimaxLookaheadAgent(depth)
    elif tag.startswith('alt'):
        depth = int(tag[3:])
        return AltMinimaxLookaheadAgent(depth)
    else:
        raise ValueError("bad agent tag: '{}'".format(tag))       
