# 8 queens problem

import numpy as np
import random, collections

def ok(pos):
    
    rows = [sum(x) for x in pos]
    if np.any([x>1 for x in rows]):
        return False
    
    cols = [sum(x) for x in pos.T]
    if np.any([x>1 for x in cols]):
        return False
    
    for offset in range(-len(pos) + 1, len(pos)):
        if np.trace(pos, offset=offset) > 1:
            return False
        
    for offset in range(-len(pos) + 1, len(pos)):
        
        for n, row in enumerate(pos):
            pos[n] = row[::-1]
        
        if np.trace(pos, offset=offset) > 1:
            return False
        
        for n, row in enumerate(pos):
            pos[n] = row[::-1]
            
    return True

def place_a_queen(pos, tried):
    open_rows = [n for n, row in enumerate(pos) if(sum(row) == 0)]
    open_cols = [n for n, col in enumerate(pos.T) if(sum(col) == 0)]
    if len(open_rows) == 0 or len(open_cols) == 0:
        return (False, pos, ())
    tries = 0
    for x in open_cols:
        for y in open_rows:
            if (x, y) in tried:
                continue
            pos[y][x] = 1 
            if ok(pos):
                return (True, pos, (x, y))
            else:
                tries += 1
                pos[y][x] = 0
    return (False, pos, ())


last_move = (0, 0)
queen_positions = []
tried_at_this_point = collections.defaultdict(set)

n_queens = 8

while len(queen_positions) < n_queens:
    
    # Reset the board.
    pos = np.zeros((n_queens, n_queens), dtype=int)
    for move in queen_positions:
        pos[move[1]][move[0]] = 1
        
    print("Placed {0} queens.".format(len(queen_positions)))
    print(queen_positions)
    
    if frozenset(queen_positions) in tried_at_this_point:
        tried = tried_at_this_point[frozenset(queen_positions)]
    else:
        tried = set()
    
    print("Tried before at this point:", tried)
    worked, pos, move = place_a_queen(pos, tried)
    
    if not worked:
        tried_at_this_point[frozenset(queen_positions[:-1])].add(queen_positions[-1])
        pos[queen_positions[-1][1]][queen_positions[-1][0]] = 0
        queen_positions = queen_positions[:-1]
        
    else:
        queen_positions.append(move)
        li = ""
        for row in pos:
            for col in row:
                li += "{0} ".format(col)
            li += "\n"
        
print("Solution:")
print(li)
print(queen_positions)
