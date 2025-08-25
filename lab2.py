#Puzzle Problem. 
from collections import deque  

# Moves: Up, Down, Left, Right
moves = { 
    'U': -3,  # move up 
    'D': 3,   # move down 
    'L': -1,  # move left 
    'R': 1    # move right 
} 

# Check if move is valid
def is_valid(pos, move):     
    if move == 'L' and pos % 3 == 0:         
        return False     
    if move == 'R' and pos % 3 == 2: 
        return False     
    if move == 'U' and pos < 3:         
        return False     
    if move == 'D' and pos > 5: 
        return False     
    return True 

# Generate new states
def get_neighbors(state): 
    neighbors = []     
    zero_pos = state.index('0')     
    for m, step in moves.items():         
        if is_valid(zero_pos, m):             
            new_state = list(state)             
            swap_pos = zero_pos + step             
            new_state[zero_pos], new_state[swap_pos] = new_state[swap_pos], new_state[zero_pos]             
            neighbors.append(''.join(new_state))     
    return neighbors 

# BFS implementation 
def bfs(start, goal):     
    visited = set([start])     
    queue = deque([start])     
    while queue:         
        state = queue.popleft()         
        print(state)         
        if state == goal: 
            print("Goal reached!")             
            return         
        for neighbor in get_neighbors(state):             
            if neighbor not in visited:                 
                visited.add(neighbor)                 
                queue.append(neighbor) 

# DFS implementation 
def dfs(start, goal):     
    visited = set([start])     
    stack = [start]     
    while stack:         
        state = stack.pop()         
        print(state)         
        if state == goal: 
            print("Goal reached!")             
            return         
        for neighbor in get_neighbors(state):             
            if neighbor not in visited:                 
                visited.add(neighbor)                 
                stack.append(neighbor) 

# Example run 
if __name__ == "__main__":
    print("BFS for 8-Puzzle:") 
    bfs("123405678", "123456780")  # 0 is the blank 

    print("\nDFS for 8-Puzzle:") 
    dfs("123405678", "123456780")


# Maze Navigation Problem 

from collections import deque  

# Maze representation (0 = free path, 1 = wall)
maze = [ 
    [0, 1, 0, 0, 0], 
    [0, 1, 0, 1, 0], 
    [0, 0, 0, 1, 0], 
    [1, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0] 
] 

start = (0, 0)  # Starting point
goal = (4, 4)   # Goal point
rows, cols = len(maze), len(maze[0]) 

# BFS algorithm for shortest path in a maze
def bfs(maze, start, goal): 
    queue = deque([([start], start)])  # (path so far, current position)     
    visited = set() 

    while queue: 
        path, (x, y) = queue.popleft()         

        # Goal reached
        if (x, y) == goal:             
            return path         

        if (x, y) in visited:             
            continue         
        visited.add((x, y)) 

        # Explore neighbors (Up, Down, Left, Right)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]: 
            nx, ny = x + dx, y + dy             
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0: 
                queue.append((path + [(nx, ny)], (nx, ny)))     

    return None 

# Example run
if __name__ == "__main__":
    print("BFS Path:", bfs(maze, start, goal))  
