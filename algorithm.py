from copy import deepcopy
import time


def player(state):
    'Returns whose turn is it to play'

    num_x = 0
    num_0 = 0

    for row in state:
        num_x += row.count('X')
        num_0 += row.count('O')
    
    if num_x == num_0:
        return 'X'
    else:
        return 'O'

def actions(state):
    'Returns a list of possible moves'

    actions = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                actions.append((i,j))

    return actions

def result(state, action):
    'Returns the state after the given action'
    
    s = deepcopy(state)
    i, j = action
    s[i][j] = player(s)

    return s

def terminal(state):
    'Returns True if the game is over'


    '''[[0,0,0],
        [0,0,0],
        [0,0,0]]'''

    for row in state:
        if (row.count('X') == 3) or (row.count('O')) == 3:
            return True

    for i in range(3):
        if state[0][i] == state[1][i] == state[2][i] != 0:
            return True

    if state[0][0] == state[1][1] == state[2][2] != 0:
        return True

    if state[0][2] == state[1][1] == state[2][0] != 0:
        return True

    return all([all(row) for row in state])
    
def utility(state):
    'Returns the numerical value of the terminal state'

    for row in state:
        if (row.count('X') == 3):
            return 1

        elif row.count('O') == 3:
            return -1

    for i in range(3):
        if state[0][i] == state[1][i] == state[2][i] != 0:
            if state[0][i] == 'X':
                return 1
                                    
            elif state[0][i] == 'O':
                return -1

    if state[0][0] == state[1][1] == state[2][2] != 0:
        if state[0][0] == 'X':
                return 1

        elif state[0][0] == 'O':
            return -1

    if state[0][2] == state[1][1] == state[2][0] != 0:
        if state[0][2] == 'X':
                return 1

        elif state[0][2] == 'O':
            return -1
    
    return 0


def maxValue(s, current=None):
    'Returns the best move for the max player'

    state = deepcopy(s)
    best_move = None

    if terminal(state):
        return utility(state), best_move

    v = float('-inf')

    possible_actions = actions(state)

    

    for action in possible_actions:
        min_eval = minValue(result(state, action), current=v)[0] 

        if current is not None:
            if min_eval > current:
                return min_eval, best_move
        # 4 3 2
        v = max(v, min_eval)

        if v <= min_eval:
            best_move = action

    return v, best_move


def minValue(s, current=None):
    'Returns the best move for the min player'
    state = deepcopy(s)
    best_move = None

    if terminal(state):
        return utility(state), best_move

    v = float('inf')
    

    possible_actions = actions(state)
    for action in possible_actions:
        max_eval = maxValue(result(state, action), current=v)[0]
        
        if current is not None:
            if max_eval < current:
                return max_eval, best_move

        v = min(v, max_eval) 
    
        if v >= max_eval:      
            best_move = action
    
    
    return v, best_move


# state = [[0, 'O', 'O'],
#          ['O', 'X', 'X'],
#          ['X', 'X', 'O']]

state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


# state = [['X', 'O', 'X'],
#          ['O', 'O', 'X'],
#          ['X', 0, 0]]

# t0 = time.time()
# print(maxValue(state))

# print(time.time() - t0)


