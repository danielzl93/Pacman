# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    start = problem.getStartState()
    start_state = (start, [])
    fringe.push(start_state)
    visited = [start]

    dfsRecur(problem,fringe, visited)
    goal, actions = fringe.pop()

    return actions

def dfsRecur(problem, fringe, visited):
    node, action = fringe.pop()
    fringe.push((node, action))
    if problem.isGoalState(node):
        return True
    successors = problem.getSuccessors(node)
    length = len(successors)
    if length==0:
        fringe.pop()
    else:
        count = 0
        for next_node, direction, costs in successors:
            if next_node not in visited:
                fringe.push((next_node, action +[direction]))
                visited.append(next_node)
                if dfsRecur(problem, fringe, visited):
                    return True
            else:
                count = count + 1
                if count == length:
                    fringe.pop()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    start = problem.getStartState()
    start_state = (start, [])

    fringe.push(start_state)
    visited = [start]

    while not fringe.isEmpty():
        state = fringe.pop()
        node, actions = state
        if problem.isGoalState(node):
            return actions
        for next_node, direction, cost in problem.getSuccessors(node):
            if not next_node in visited:
                fringe.push((next_node, actions + [direction]))
                visited.append(next_node)

    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    start = problem.getStartState()
    start_state = (start, [])
    visited = []
    fringe.push(start_state, 0)
    while not fringe.isEmpty():
        state = fringe.pop()
        node, actions = state
        if node in visited:
            continue
        visited.append(node)

        if problem.isGoalState(node):
            return actions

        for next_node, direction, cost in problem.getSuccessors(node):
            new = actions + [direction]
            if next_node not in visited:
                fringe.update((next_node, new), problem.getCostOfActions(new))
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    start = problem.getStartState()
    start_state = (start, [])
    visited = []
    fringe.push(start_state, 0)

    while not fringe.isEmpty():
        state = fringe.pop()
        node, actions = state
        
        if node in visited:
            continue
        visited.append(node)

        if problem.isGoalState(node):
            return actions

        for next_node, direction, cost in problem.getSuccessors(node):
            new = actions + [direction]
            if next_node not in visited:
                heu = problem.getCostOfActions(new)+heuristic(next_node
                ,problem)
                fringe.update((next_node, new), heu)
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
